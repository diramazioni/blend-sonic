{% extends "inline_fn.py" %}
{%- block imports %}
{{ super() }}
from {{ menu_levels }} events import propertyChanged
{% endblock %}

{%- block classMembers %}        
    dot = BoolProperty(name = "Add dot", default = False, update = propertyChanged)
{%- endblock %}
{%- block draw %}
        col = layout.column(align = True)
        col.prop(self, "dot", text = "", icon = "RADIOBUT_ON")
{%- endblock %}
{%- block execode -%}
        {{ super() }}
        yield "args_ = '('+', '.join(args_)+')'"
        yield "if self.dot: dot_='.'"
        yield "else: dot_=' '"        
        
        yield "send = dot_ +'{{ fn.name }}' + args_ + sep+ opts_"
{%- endblock -%}


        