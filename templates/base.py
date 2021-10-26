{%- set inp = "In" %}

{% import "includes.py" as macro with context %}

import bpy
from bpy.props import *

{% block imports %}
from {{ menu_levels }} base_types.node import AnimationNode
from {{ menu_levels }} tree_info import keepNodeState
{% endblock %}


class Sonic{{ fn_name |capitalize }}Node(bpy.types.Node, AnimationNode):
    bl_idname = "an_sp_{{ fn_name |capitalize }}Node"
    bl_label = "{{ fn_name }}: {{ fn.summary }}"
    bl_description = "{{ fn.summary }}"
    
    searchTags = ['SP {{ fn_name }}']
    onlySearchTags = True
    
    infoMessage = StringProperty()

{%- block classMembers %}{%- endblock %}
            
    def draw(self, layout):
{%- block draw %}
        if self.infoMessage != "":
            layout.label(self.infoMessage, icon = "TRIA_RIGHT")
{%- endblock %}

    def create(self):   
{%- block newInput%}
        self.newInput("String List", "code in", "code_in")                  
{%- endblock -%}
{%- block newOutput %}
        self.newOutput("String List", "code out", "code_out")
{%- endblock -%}        

{%- block create %}{%- endblock -%}



{%- set count_args = 1 %}
{%- if fn.args %} {% set count_args = fn.args | length + 1%}
{{ macro.newArgInput(fn.args) }}
{%- endif %}

{%- if fn.alt_args %} 
{{ macro.newArgInput(fn.alt_args) }}
{%- endif %}

        self.recreateInputs()

{%- if fn.opts %}
{{ macro.newOptInput() }}
{%- endif %}
        
{%- block extra_create %}{%- endblock %}

{%- with %}{% set post_args = '' %}
{%- block post_create %}
{{ macro.hideInput(count_args, post_args) }}
{%- endblock %}{%- endwith %}
    
    @keepNodeState    
    def recreateInputs(self):
{%- block recreateInputs %}
        pass
{%- endblock %}

    def getExecutionCode(self):
    {%- block exe_decl %}
        #yield "send = []"
        yield "prefix, postfix, list_ = ('','','')"
        yield "args_ , opts_ = ([],[])"        
        s = self.inputs
    {%- endblock %}
    
{%- block checkEnum %}{%- endblock %}

{%- block checkArgs %}        
    {%- if fn.args %}
        {{ macro.argCheck(fn.args) }}
    {% endif %}        
    {%- if fn.alt_args %}
        {{ macro.argCheck(fn.alt_args) }}
    {% endif %}        
    {%- if fn.opts %}
        {{ macro.optCheck() }}
    {% endif %}
{%- endblock %}

{%- block extra_input %}{%- endblock %}

{%- block execode %}
{{ macro.opt_join() }} 
{{ macro.arg_join() }} 
{%- endblock %}

        
{%- block code_out %}
        yield 'code_out = code_in + send'
{%- endblock %}

{%- block infoMessage %}
        yield 'self.infoMessage = code_out' 
{%- endblock %}

    def delete(self):        
        print("Removing node: {{ fn_name }}", self.name)        

{%- block used_module %}
{%- endblock %}        
    