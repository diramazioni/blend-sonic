{% extends "inline_fn.py" %}

{% block imports %}
{{ super() }}
from {{ menu_levels }} events import propertyChanged
import operator
from {{ menu_levels[2:] }} constant_def import notes

notes_k = sorted(notes.items(), key=operator.itemgetter(1))
notes_items = [(k[0],k[0][1:],'') for k in notes_k ]
{% endblock %}

{%- block classMembers %}
    noteList : EnumProperty(name="Note", items = notes_items, update=propertyChanged)
{%- endblock %}
{%- block draw %}
        layout.prop(self, "noteList")
        row = layout.row(align = True)
        self.invokeFunction(row, "prevEl", text = "Prev", description = "get to the previous note", icon = "TRIA_LEFT")
        self.invokeFunction(row, "nextEl", text = "Next", description = "get to the next note", icon = "TRIA_RIGHT")
        
{%- endblock %}

{%- block post_create %}
{{ macro.hideInput(count_args, post_args ) }} 

    def nextEl(self):
        for i, k in enumerate(notes_k):
            if k[0] == self.noteList:
                idx = i+1 if len(notes_k)> i+1 else 0
                if k[1] == notes_k[idx][1]:
                    idx += 1
                self.noteList = notes_k[idx][0]
                return

    def prevEl(self):
        for i, k in enumerate(notes_k):
            if k[0] == self.noteList:
                idx = i-1 if i>= 0 else len(notes_k)
                if k[1] == notes_k[idx][1]:
                    idx -= 1
                self.noteList = notes_k[idx][0]
                return

    def updateOutputName(self):
        name = "Notes ({})".format(len(self.inputs) - 1)
        if len(self.outputs) > 0:
            self.outputs[0].name = name
            
{%- endblock %}

{%- block extra_input %}{%- endblock %}

{%- block checkEnum %}
        if not s["note"].isUsed:
            yield "send = self.noteList"
        else:
            yield "send = str(noteIn)"
{%- endblock %}

{%- block execode %}       
        #yield "if len(noteIn): send = str(noteIn)"        
        #yield "else: send = self.noteList"
{%- endblock -%}

{%- block code_out %}
        yield "code_out =  code_in + send"
{%- endblock -%}
        