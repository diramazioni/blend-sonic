import bpy
from bpy.props import *
{% block imports %}
from ... base_types.node import AnimationNode
{% endblock %}

import random

class Sonic{{ fn_name |capitalize }}Node(bpy.types.Node, AnimationNode):
    bl_idname = "an_sp_{{ fn_name |capitalize }}Node"
    bl_label = "{{ fn_name }}: {{ fn.summary }}"
    bl_description = "{{ fn.summary }}"
    
    searchTags = ['SP{{ fn_name }}']

    infoMessage = StringProperty()
        
    def draw(self, layout):
        if self.infoMessage != "":
            layout.label(self.infoMessage, icon = "QUESTION")
{%- block draw %}        
{%- endblock %}

    def create(self):   
{% block newInput%}
        self.newInput("String List", "code in", "code_in")                  
{%- endblock -%}
{%- block newOutput %}
        self.newOutput("String List", "code out", "code_out")
{%- endblock -%}        

{% block create %}
{%- endblock -%}

{% set inp = "In" %}
{% set count_args = 1 %}

{% if fn.args %} {% set count_args = fn.args | length %}
{% for arg, val in fn.args.items() %}
        self.newInput("{{ args_types[val] }}", "{{ arg }}", "{{arg +inp }}")     
{%- endfor %}{%- endif %}

{% if fn.opts %}{% for opt, val in fn.opts|dictsort %}
        self.newInput("{{ opts_types[opt] }}", "{{ opt }}", "{{opt +inp}}", value = {{ val }})     
{%- endfor %}{%- endif %}

        for socket in self.inputs[{{ count_args }}:]:
            socket.useIsUsedProperty = True
            socket.isUsed = False
            #socket.value = False
        for socket in self.inputs[{{ count_args }}:]:
            socket.hide = True

    def getExecutionCode(self):
        #yield "send = []"
        yield "args_ = []"
        yield "opts_ = []"
        
        s = self.inputs

    {% if fn.args %}
        #yield "args_ = []"        
        {%- for arg, val in fn.args|dictsort %}
        yield "if len(str({{ arg+inp }})): args_.append(str({{arg+inp }}))" 
        {%- endfor %}
        yield "if len(args_): args_ = list(filter(None, args_ ))"        
    {% endif %}        
    {% if fn.opts %}
        #yield "opts_ = []"        
        {%- for opt, val in fn.opts|dictsort %} 
        if s["{{ opt }}"].isUsed: 
            yield "opts_.append('{{ opt+inp }}: ' + str({{ opt+inp }}) )" 
    {%- endfor %}{% endif %}        
        {% block execode -%}{%- endblock %}
        yield '{% block execute -%}{%- endblock %}'
        
    {%- block code_out %}
        yield 'code_out = code_in + send'
    {%- endblock %}        
        yield 'self.infoMessage = code_out' #str((opts_, args_, code_out))'
    def delete(self):        
        print("Removing node: {{ fn_name }}", self.name)        
        
    
    