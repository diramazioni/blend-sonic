{% extends "scale.py" %}

{% block imports %}
{{ super() }}
from {{ menu_levels[2:] }} constant_def import degree_names
degree_items = [(':'+k.lower(),k,'') for k in degree_names ]
{% endblock %}

{%- block classMembers %}
    degreeList = EnumProperty(name="Degree", items = degree_items, update=propertyChanged)
{{ super() }}
{%- endblock %}

{%- block draw %}
        layout.prop(self, "degreeList")
{{ super() }}
{%- endblock %}
{%- block checkEnum %}
{{ super() }}
        if not s["degree"].isUsed:
            yield "args_.append(str(self.degreeList))"
{%- endblock %}
