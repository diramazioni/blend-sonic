import bpy
from bpy.props import *
from ... base_types.node import AnimationNode

import random



class SonicSendNode(bpy.types.Node, AnimationNode):
    bl_idname = "an_spSendNode"
    bl_label = "Send to Sonic-PI"

    #send = BoolProperty(name = "send", default = False)
  
    def create(self):        
        self.newInput("Boolean", "signal", "run", value = False)
        self.newInput("Integer", "skip run", "skip_run")
        self.newInput("String List", "code lines", "code")
        
        bpy.context.scene['sp_skip'] = {self.identifier: 0}

    def draw(self, layout):
        #layout.prop(self, "send")
        #layout.prop(self, "skip_run")
        pass
    
    def execute(self, run, skip_run, code ):
        if not 'sp_queue' in bpy.context.scene: return
        if self.identifier in bpy.context.scene['sp_skip']:                
            counter = bpy.context.scene['sp_skip'][self.identifier]
            #print("%s > %s " % (self.identifier, counter))
        else:
            bpy.context.scene['sp_skip'][self.identifier] = 0
            counter = 0        
        '''
        if 'sp_skip' in bpy.context.scene:
            if self.identifier in bpy.context.scene['sp_skip']:                
                counter = bpy.context.scene['sp_skip'][self.identifier]
                #print("%s > %s " % (self.identifier, counter))
            else:
                bpy.context.scene['sp_skip'][self.identifier] = 0
                counter = 0
        else:
            bpy.context.scene['sp_skip'] = {self.identifier: 0}
            counter = 0
        '''
        if counter > skip_run:  # reset
            counter = 0
        if counter == skip_run:  # run !!!          
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
    
    '''
    def edit(self):
        self.updateOutputName()
        emptySocket = self.inputs["..."]
        origin = emptySocket.directOrigin
        if origin is None: return
        socket = self.newInputSocket()
        socket.linkWith(origin)
        emptySocket.removeLinks()
        
    def removeUnlinkedInputs(self):
        for socket in self.inputs[:-1]:
            if not socket.is_linked:
                socket.remove()    
    '''                