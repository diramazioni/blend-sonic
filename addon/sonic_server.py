#    This Addon control Sonic PI with OSC 
#
# ***** BEGIN GPL LICENSE BLOCK *****
#
#    Copyright (C) 2015  JPfeP <http://www.jpfep.net/>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# ***** END GPL LICENCE BLOCK *****

bl_info = {
    "name": "BlendSonicPI",
    "author": "Eli Spizzichino",
    "version": (0, 1),
    "blender": (2, 7, 7),
    "location": "",
    "description": "Realtime control of Sonic PI using OSC protocol",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "System"}

import bpy
import random

from bpy.props import (
    BoolProperty, StringProperty, FloatProperty,
    IntProperty, PointerProperty, CollectionProperty
)

add = bpy.utils.register_class
remove = bpy.utils.unregister_class

NOT_FOUND = 0
FOUND = 1
STOPPED = 2
RUNNING = 3



try:
    STATUS = FOUND
    if ('pythonosc' in locals()): pass
        #print('sonic server : reload event. handled')
    else:
        import pythonosc
        from pythonosc import osc_message_builder
        from pythonosc import udp_client
        #print('sonic-pi: loaded pythonosc')

except:
    STATUS = NOT_FOUND
    print('python osc not found!, or failed to reimport')

osc_statemachine = {'status': STATUS}    

class SonicPI_UI_Panel(bpy.types.Panel):
    bl_idname = "wm.sonic_pi_panel"
    bl_label = "BlendSonicPI Settings"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_category = "SonicPI"
 
    def draw(self, context):
        state = osc_statemachine['status']
        
        props = context.scene.sp_prop
        layout = self.layout
        col = layout.column(align=True)
        col.label(text="Sonic-PI server:")
        row = col.row(align=True)
        
        if state == NOT_FOUND:
            col.label('failed to (re)import pythonosc - see console')
            return
        
        if state in {FOUND, STOPPED}:
            row.prop(props, 'ip', text='')
            row.prop(props, 'port', text='')
            row = col.row(align=True)
            row.prop(props, 'up_timer', text='timer click')
            row = col.row(align=True)
            mode = 'start'
            icon = 'PLAY'
        elif state == RUNNING:
            mode = 'stop'
            icon = 'PAUSE'
            
            op = row.operator("wm.sonic_pi_txt", text="play text", icon='SOUND')
            row = col.row(align=True)

        op = row.operator("wm.sonic_pi_client", text=mode, icon=icon)
        op.mode = mode
        #op.speed = 0.1
        
        


class SonicPiProps(bpy.types.PropertyGroup):
    ip = StringProperty(default='127.0.0.1')
    port = IntProperty(default=4557)
    up_timer = FloatProperty(min=0.001, max=60, default=0.1)
    
class SonicPiClient(bpy.types.Operator, object):

    bl_idname = "wm.sonic_pi_client"
    bl_label = "start and stop Sonic-Pi Client "

    _timer = None
    client = None
    
    speed = FloatProperty(default=0.1)
    mode = StringProperty()
    
    
    def modal(self, context, event):
    
        if osc_statemachine['status'] == STOPPED:
            self.cancel(context)
            return {'FINISHED'}

        if not (event.type == 'TIMER'):
            return {'PASS_THROUGH'}
        
        queue = context.scene['sp_queue']        
        for agent in queue.keys():
            code = queue.pop(agent)
            if code:  self.run_code(agent, code)
        #for agent, code in context.scene['sp_queue'].items():
            #self.run_code(agent, code)
        
        
        
        return {'PASS_THROUGH'}

    def event_dispatcher(self, context, type_op):
        props = context.scene.sp_prop
        self.client = udp_client.UDPClient(props.ip, props.port)

        if type_op == 'start':
            self.speed = props.up_timer 
            
            wm = context.window_manager
            self._timer = wm.event_timer_add(self.speed, context.window)
            wm.modal_handler_add(self)

            osc_statemachine['status'] = RUNNING            
            
            context.scene['sp_queue'] = {}
            context.scene['sp_agent'] = ""
            
            agent = 'Starting BlendSonic'
            note = 20
            c2 = 'play {0}{1}'.format(note, '')
            c1 = 'use_synth :{0}'.format('pulse') 
            code = [c1,c2]
            
            context.scene['sp_queue'][agent] = code
       
            #start_server_comms(props.ip, props.port, [i.path for i in paths])

        if type_op == 'stop':
            self.stop_all()
            #osc_statemachine['server'].shutdown()
            #osc_statemachine['server'].server_close()
            osc_statemachine['status'] = STOPPED
    
    def stop_all(self):
        msg = osc_message_builder.OscMessageBuilder(address="/stop-all-jobs")
        msg = msg.build()
        if self.client:
            print("sonic-pi STOP ")
            self.client.send(msg)
        

    def run_code(self, agent='', code=[]):
        print("AGENT:", (agent, code))
        msg = osc_message_builder.OscMessageBuilder(address="/run-code")
        msg.add_arg(agent)
        msg.add_arg('\n'.join(code))
        msg = msg.build()
        self.client.send(msg)
        
    def execute(self, context):

        self.event_dispatcher(context, self.mode)
        
        return {'RUNNING_MODAL'}

    def cancel(self, context):
        wm = context.window_manager
        wm.event_timer_remove(self._timer)
        
class SonicPi_txt(bpy.types.Operator, object):

    bl_idname = "wm.sonic_pi_txt"
    bl_label = "run sonic-pi code from text buffers starting with 'sp_'"
    
    
    def execute(self, context):
        for tname in bpy.data.texts.keys():
            if tname[:3] == 'sp_':
                sp_t = bpy.data.texts.get(tname)
                code = [s.body for s in sp_t.lines]                
                context.scene['sp_queue'][tname] = code
        return {'FINISHED'}
    
        
def register():
    add(SonicPiProps)
    bpy.types.Scene.sp_prop = PointerProperty(name="properties", type=SonicPiProps)
    add(SonicPI_UI_Panel)
    add(SonicPiClient)
    
    add(SonicPi_txt)



def unregister():
    remove(SonicPiProps)    
    remove(SonicPI_UI_Panel)
    remove(SonicPiClient)

    del bpy.types.Scene.sp_prop
    
    remove(SonicPi_txt)