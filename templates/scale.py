{% extends "note.py" %}



{% block imports %}
{{ super() }}
from {{ menu_levels[2:] }} constant_def import scale_names
scale_items = [(k,k,'') for k in scale_names ]
{% endblock %}

{%- block classMembers %}
{{ super() }}
    scaleList = EnumProperty(name="Scale", items = scale_items, default = ':major',  update=propertyChanged)
{%- endblock %}

{%- block draw %}
{{ super() }}
        layout.prop(self, "scaleList")
{%- endblock %}

{%- block extra_input %}{% endblock %}

{%- block post_create %}
{{ macro.hideInput(count_args, post_args ) }} 
{{ super() }}
{%- endblock %}
{%- block checkEnum %}
        if not s["tonic"].isUsed:
            yield "args_.append(str(self.noteList))"
        if not s["scale"].isUsed:
            yield "args_.append(str(self.scaleList ))"
{%- endblock %}
{%- block execode %}
    {{ macro.inline_send( fn.name ) }} 
{%- endblock -%}