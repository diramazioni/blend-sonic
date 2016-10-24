import bpy
from bpy.props import *
{% block imports %}
from ... base_types.node import AnimationNode
{% endblock %}

import random

class Sonic{{ fn_name |capitalize }}Node(bpy.types.Node, AnimationNode):
    bl_idname = "an_sp{{ fn_name |capitalize }}Node"
    bl_label = "{{ fn.summary }}"
        
    def draw(self, layout):
{% block draw %}
        pass
{% endblock %}
    
    def create(self):        
{% block create %}
        self.newInput("String List", "code in", "code_in")        
        self.newOutput("String List", "code out", "code_out")
{% endblock -%}
        
        
        
{% if fn.opts %}{% for opt, val in fn.opts|dictsort %}
        self.newInput("Float", "{{ opt }}", "{{ opt[:-1] }}", value = {{ val }})     
{%- endfor %}{%- endif %}

        for socket in self.inputs[1:]:
            socket.useIsUsedProperty = True
            socket.isUsed = False
        for socket in self.inputs[2:]:
            socket.hide = True

    def getExecutionCode(self):
        yield "send = ''"
        yield "arg = []"
        s = self.inputs
        
        {% if fn.opts %}{% for opt, val in fn.opts|dictsort %} 
        if s["{{ opt }}"].isUsed: yield "arg.append('{{ opt }} ' + str({{ opt[:-1] }}) )" 
        {%- endfor %}{%- endif %}        
        {% block execode -%}{%- endblock %}
        yield "{% block execute -%}{%- endblock %}"
        
        yield "code_out = code_in + send"
{#   
    '''          
    def execute(self, code_in {%- block exe_def -%}
                {% for opt, val in arg_defaults|dictsort %}, {{ opt[1:] }}{% endfor %} {% endblock -%} 
                ):

        code_out = code_in + send
        return code_out
''' #}
        
        
        
    
    def delete(self):        
        print("Removing node: ", self.name)        
        
    
    