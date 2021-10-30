{% extends "base.py" %}
{% block imports %}
{{ super() }}
#from {{ menu_levels }} events import propertyChanged
import operator
from . constant_def import notes

notes_k = sorted(notes.items(), key=operator.itemgetter(1))
notes_items = [(k[0],k[0],'') for k in notes_k ]
{% endblock %}

{%- block classMembers %}
    noteList : EnumProperty(name="Note", items = notes_items)
{%- endblock %}
{%- block draw %}
        layout.prop(self, "noteList")
        row = layout.row(align = True)
        self.invokeFunction(row, "newInputSocket", text = "New Note", description = "Create a new note socket", icon = "SOUND")
        self.invokeFunction(row, "removeUnlinkedInputs", description = "Remove all notes", confirm = True,
            icon = "X")            
{%- endblock %}
{%- block newInput %}                 
{%- endblock -%}
{%- block create %}
        self.newInput("Node Control", "...")
        #self.newInputSocket()    
{%- endblock -%}
{%- block post_create %}

    def getInputSocketVariables(self):
        return {socket.identifier: "element_" + str(i) for i, socket in enumerate(self.inputs)}
    
    def newInputSocket(self):
        socket = self.newInput("Text", "Element")
        socket.dataIsModified = True
        socket.display.text = True
        socket.value = self.noteList
        socket.text = socket.value 
        socket.removeable = True
        socket.moveable = True
        socket.defaultDrawType = "PREFER_PROPERTY"
        socket.moveUp()
        return socket
    
    def removeUnlinkedInputs(self):
        for socket in self.inputs[:-1]:
            if not socket.is_linked:
                socket.remove()     
    def edit(self):
        self.updateOutputName()
        emptySocket = self.inputs["..."]
        origin = emptySocket.directOrigin
        if origin is None: return
        socket = self.newInputSocket()
        socket.linkWith(origin)
        emptySocket.removeLinks() 
        socket.text = origin.value # it doesn't work but at least it doesn't display the wrong value    
        
    def updateOutputName(self):
        name = "Notes ({})".format(len(self.inputs) - 1)
        if len(self.outputs) > 0:
            self.outputs[0].name = name        
{%- endblock %}
{%- block exe_decl %}{%- endblock -%}

{%- block execode %}
        variableNames = ["element_" + str(i) for i, socket in enumerate(self.inputs) if socket.dataType != "Node Control"]
        createPyListExpression = "[" + ", ".join(variableNames) + "]"
        createListExpression = self.outputs[0].getFromValuesCode().replace("value", createPyListExpression)
        return "code_out = " + createListExpression
{%- endblock -%}
{%- block code_out %}{%- endblock -%}
{%- block infoMessage %}{%- endblock %}
        