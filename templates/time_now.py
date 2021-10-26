{% extends "inline_fn.py" %}

{% block imports %}
from {{ menu_levels }} events import propertyChanged
import datetime as dt
{{ super() }}

dt_type = ['microsecond', 'second', 'minute', 'hour']
time_items = [(k,k,'') for k in dt_type ]
{%- endblock -%}

{%- block classMembers %}
    dtList = EnumProperty(name="Current time in", items = time_items, update=propertyChanged)
{%- endblock %}

{% block newInput%}
        self.newInput("Float", "Divider", "divider" , value = 1.0)
{%- endblock -%}

{%- block newOutput %}
        self.newOutput("Integer", "time", "code_out")
{%- endblock -%}

{% block extra_create %}{%- endblock %}
{%- block extra_input %}{%- endblock %}

{%- block draw %}
{{ super() }}
        layout.prop(self, "dtList")
{%- endblock %}

{%- block post_create %}
    def getDiv(self):
        return  self.inputs["Divider"].value if self.inputs["Divider"].value != 0.0 else 1.0
    def getMilli(self):
        return round(dt.datetime.now().time().microsecond / self.getDiv())
    def getSecond(self):
        return round(dt.datetime.now().time().second / self.getDiv())
    def getMinute(self):
        return round(dt.datetime.now().time().minute / self.getDiv())
    def getHour(self):
        return round(dt.datetime.now().time().hour / self.getDiv())
{%- endblock -%}

{%- block execode %}        
{%- endblock -%}

{%- block code_out %}
        if self.dtList == dt_type[0]:
            yield "code_out = self.getMilli()"
        elif self.dtList == dt_type[1]:
            yield "code_out = self.getSecond()"
        elif self.dtList == dt_type[2]:
            yield "code_out = self.getMinute()"
        elif self.dtList == dt_type[3]:
            yield "code_out = self.getHour()"
            
{%- endblock %}
{%- block infoMessage %}
        #yield 'self.infoMessage = str(code_out)' 
{%- endblock %}

{%- block used_module %}
    def getUsedModules(self):
        return ["datetime"]
{%- endblock %}     
