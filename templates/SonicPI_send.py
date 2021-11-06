import bpy
from bpy.props import *
from ... base_types import AnimationNode, VectorizedSocket
from ... events import propertyChanged



class SonicSendNode(bpy.types.Node, AnimationNode):
    bl_idname = "an_sp_SendNode"
    bl_label = "Send to Sonic-PI"

    #send = BoolProperty(name = "send", default = False)
    stop: BoolProperty(name = "Add stop", default = False, update = propertyChanged)
  
    def setup(self):
        self.newInput("Boolean", "signal", "run", value = True)
        self.newInput("Text List", "code lines", "code")
        # bpy.context.scene['sp_var'] = {}
        bpy.context.scene['sp_queue'] = {self.identifier: ""}
        bpy.context.scene['sp_last'] = {self.identifier: ""}

    def draw(self, layout):
        col = layout.column(align = True)
        col.prop(self, "stop", text = "", icon = "OUTLINER_OB_SPEAKER")
    
    def execute(self, run, code ):
        if not 'sp_queue' in bpy.context.scene: return

        if self.identifier in bpy.context.scene['sp_last']:
            _last_code = bpy.context.scene['sp_last'][self.identifier]
        else:
            _last_code = ""

        if not self.stop: code = ['stop']+code
        if run == True:
            if code != _last_code:
                bpy.context.scene['sp_queue'][self.identifier] = code
                bpy.context.scene['sp_last'][self.identifier] = code

    
    def delete(self):        
        print("Removing node: ", self.name)   
        #print(dir(self))
                
