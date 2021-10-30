{% extends "note.py" %}

{% block imports %}
{{ super() }}
from {{ menu_levels[2:] }} constant_def import chord_names

chord_items = [(k,k,'') for k in chord_names ]

{% endblock %}

{%- block classMembers %}
{{ super() }}
    chordList : EnumProperty(name="Chord", items = chord_items, default = ':major', update=propertyChanged)
{%- endblock %}

{%- block draw %}
{{ super() }}
        layout.prop(self, "chordList")
{%- endblock %}
{%- block extra_input %}{% endblock %}

{%- block checkEnum %}
        if not s["tonic"].isUsed:
            yield "args_.append(str(self.noteList))"
        if not s["chord"].isUsed:
            yield "chord = str(self.chordList) if \
            self.chordList.startswith(':') else \
            '\"'+str(self.chordList)+'\"'"
            yield "args_.append(chord)"
{%- endblock %}

{%- block execode %}
    {{ macro.arg_join() }} {{ macro.opt_join() }} 
    {{ macro.inline_send() }} 
{%- endblock -%}