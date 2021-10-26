import bpy
from bpy.props import *
from ... base_types.node import AnimationNode
from ... events import propertyChanged



class SonicSendNode(bpy.types.Node, AnimationNode):
    bl_idname = "an_sp_SendNode"
    bl_label = "Send to Sonic-PI"

    #send = BoolProperty(name = "send", default = False)
    stop = BoolProperty(name = "Add stop", default = False, update = propertyChanged)
  
    def create(self):        
        self.newInput("Boolean", "signal", "run", value = True)
        self.newInput("Integer", "skip run", "skip_run")
        self.newInput("String List", "code lines", "code")
        bpy.context.scene['sp_var'] = {}
        bpy.context.scene['sp_skip'] = {self.identifier: 0}

    def draw(self, layout):
        col = layout.column(align = True)
        col.prop(self, "stop", text = "", icon = "OUTLINER_OB_SPEAKER")
    
    def execute(self, run, skip_run, code ):
        if not 'sp_queue' in bpy.context.scene: return
        if self.identifier in bpy.context.scene['sp_skip']:                
            counter = bpy.context.scene['sp_skip'][self.identifier]
            #print("%s > %s " % (self.identifier, counter))
        else:
            bpy.context.scene['sp_skip'][self.identifier] = 0
            counter = 0        
        if counter > skip_run:  # reset
            counter = 0
        if counter == skip_run:  # run !!!
            if not self.stop: code = ['stop']+code
            if run == True:
                bpy.context.scene['sp_queue'][self.identifier] = code
                #self.send = False
                counter += 1
        else:     # increment
            counter += 1
        bpy.context.scene['sp_skip'][self.identifier] = counter
            
    
    def delete(self):        
        print("Removing node: ", self.name)   
        #print(dir(self))
                