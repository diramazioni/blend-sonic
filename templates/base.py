{% import "includes.py" as ins %}

import bpy
from bpy.props import *

{% block imports %}
from {{ menu_levels }} base_types.node import AnimationNode
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

{% macro newArgInput(args) -%}
{% for ar in args %}
{%- for arg, val in ar.items() %}
        self.newInput("{{ args_types[val] }}", "{{ arg }}", "{{arg +inp }}")     
{%- endfor %}{%- endfor %}
{%- endmacro %} 

{%- set inp = "In" %}
{%- set count_args = 1 %}
{%- if fn.args %} {% set count_args = fn.args | length + 1%}
{{ newArgInput(fn.args) }}
{%- endif %}

{%- if fn.alt_args %} 
{{ newArgInput(fn.alt_args) }}
{%- endif %}

{%- if fn.opts %}
 {%- for opt, val in fn.opts|dictsort %}
  {%- if opts_types[opt] == "String" %}        
        self.newInput("{{ opts_types[opt] }}", "{{ opt }}", "{{opt +inp}}", value = "{{ val }}")  
  {%- else %}
        self.newInput("{{ opts_types[opt] }}", "{{ opt }}", "{{opt +inp}}", value = {{ val }})     
  {%- endif %}        
 {%- endfor %}
{%- endif %}
{% macro hideInput(start, end) %}
        for socket in self.inputs[{{ start }}:{{ end }}]:
            socket.useIsUsedProperty = True
            socket.isUsed = False
            #socket.value = False
        for socket in self.inputs[{{ start }}:{{ end }}]:
            socket.hide = True
{%- endmacro %} 

{%- with %}{% set post_args = '' %}
{%- block post_create %}
{{ hideInput(count_args, post_args) }}
{%- endblock %}
{%- endwith %}
    def getExecutionCode(self):
    {%- block exe_decl %}
        #yield "send = []"
        yield "prefix, postfix, list_ = ('','','')"
        yield "args_ , opts_ = ([],[])"        
        s = self.inputs
    {%- endblock %}
{% macro argCheck(args) -%}
{% for ar in args %}
    {%- for arg, val in ar.items() %}        
        if s["{{ arg }}"].isUsed: 
        {%- if arg  == "list" %}
            yield "list_ = '['+', '.join(listIn)+']'"
        {%- elif args_types[val] == "String List"  and arg  != "list"%}
            yield "args_.append(', '.join({{ arg+inp }}))" 
        {%- elif args_types[val] == "Float" %}
            yield "args_.append('{0:.3g}'.format({{ arg+inp }}))"
        {%- elif args_types[val] == "Boolean" %}
            yield "if {{ arg+inp }} == True: args_.append('true')"
            yield "else: args_.append('false')"            
        {% else %}
            yield "if len(str({{ arg+inp }})): args_.append(str({{arg+inp }}))" 
        {% endif %}        
    {%- endfor %}
{%- endfor %}
        yield "if len(args_): args_ = list(filter(None, args_ ))"        
{%- endmacro %} 
{% macro optCheck() -%}
    {%- for opt, val in fn.opts|dictsort  %}
        if s["{{ opt }}"].isUsed: 
            yield "pre = '{{ opt }}: '"
        {%- if opts_types[opt] == "String List" %}
            yield "opts_.append( pre + ', '.join({{ opt+inp }}))" 
        {%- elif opts_types[opt] == "Float" %}
            yield "opts_.append( pre + '{0:.3g}'.format({{ opt+inp }}))"
        {%- elif opts_types[opt] == "Boolean" %}
            yield "if {{ opt+inp }} == True: opts_.append('true')"
            yield "else: opts_.append(pre + 'false')"            
        {% else %}
            yield "if len(str({{ opt+inp }})): opts_.append(pre + str({{opt+inp }}))" 
        {% endif %}        
    {%- endfor %}
{%- endmacro %} 
{%- block includeArgs %}        
    {%- if fn.args %}
        {{ argCheck(fn.args) }}
    {% endif %}        
    {%- if fn.alt_args %}
        {{ argCheck(fn.alt_args) }}
    {% endif %}        
    {%- if fn.opts %}
        {{ optCheck() }}
    {% endif %}
{%- endblock %}
{%- block extra_input %}{%- endblock %}
{%- block execode %}
        yield "opts_ = ', '.join(opts_)"
        yield "if len(opts_): sep=', '"
        yield "else: sep=''"           
{%- endblock %}
        yield '{% block execute -%}{%- endblock %}'
        
{%- block code_out %}
        yield 'code_out = code_in + send'
{%- endblock %}
{%- block infoMessage %}
        yield 'self.infoMessage = code_out' 
{%- endblock %}
        #str((opts_, args_, code_out))'
    def delete(self):        
        print("Removing node: {{ fn_name }}", self.name)        
        
    