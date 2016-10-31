{% extends "note.py" %}

{% import "includes.py" as ins %}

{% block imports %}
{{ super() }}
from {{ menu_levels[2:] }} constant_def import chord_names

chord_items = [(k,k,'') for k in chord_names ]

{% endblock %}
{%- block classMembers %}
{{ super() }}
    chordList = EnumProperty(name="Chord", items = chord_items, default = ':major', update=propertyChanged)
{%- endblock %}
{%- block draw %}
{{ super() }}
        layout.prop(self, "chordList")
{%- endblock %}
{%- block extra_input %}{% endblock %}

{%- block post_create %}
{{ ins.hideInput(count_args, post_args ) }} 
{{ super() }}
{%- endblock %}

{%- block execode %}
        if not s["tonic"].isUsed:
            yield "args_= [str(self.noteList)]"
        if not s["chord"].isUsed:
            yield "chord = str(self.chordList) if \
            self.chordList.startswith(':') else \
            '\"'+str(self.chordList)+'\"'"
            yield "args_.append(chord)"

    {{ ins.inline_send( fn.name ) }} 
{%- endblock -%}