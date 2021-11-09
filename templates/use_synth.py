{% extends "with_no_block.py" %}

{% block imports %}
{{ super() }}
from {{ menu_levels }} events import propertyChanged
import operator
from {{ menu_levels[2:] }} constant_gen import synths_names

synth_k = sorted(synths_names.items(), key=operator.itemgetter(1))
synth_items = [(k[0],k[0][1:],'') for k in synth_k ]
{% endblock %}

{%- block classMembers %}
    synthList : EnumProperty(name="synth", items = synth_items, update=propertyChanged)
{%- endblock %}
{%- block draw %}
        layout.prop(self, "synthList")
        row = layout.row(align = True)
        self.invokeFunction(row, "prevEl", text = "Prev", description = "get to the previous note", icon = "TRIA_LEFT")
        self.invokeFunction(row, "nextEl", text = "Next", description = "get to the next note", icon = "TRIA_RIGHT")
        
{%- endblock %}

{%- block post_create %}
{{ macro.hideInput(count_args, post_args ) }} 

    def nextEl(self):
        for i, k in enumerate(synth_k):
            if k[0] == self.synthList:
                idx = i+1 if len(synth_k)> i+1 else 0
                if k[1] == synth_k[idx][1]:
                    idx += 1
                self.synthList = synth_k[idx][0]
                return

    def prevEl(self):
        for i, k in enumerate(synth_k):
            if k[0] == self.synthList:
                idx = i-1 if i>= 0 else len(synth_k)
                if k[1] == synth_k[idx][1]:
                    idx -= 1
                self.synthList = synth_k[idx][0]
                return

    def updateOutputName(self):
        name = "Synth ({})".format(len(self.inputs) - 1)
        if len(self.outputs) > 0:
            self.outputs[0].name = name
            
{%- endblock %}

{%- block extra_input %}{%- endblock %}

{%- block checkEnum %}
        if not s["synth_name"].isUsed:
            yield "args_.append(self.synthList)"

{%- endblock %}

{%- block execode %}
{{ super() }}
{%- endblock -%}

{%- block code_out %}
        yield "code_out =  code_in + send"
{%- endblock -%}
        