{% extends "inline_fn.py" %}
{%- block imports %}
from .... base_types.node import AnimationNode
from .... events import propertyChanged
{% endblock %}

{%- block classMembers %}        
    dot = BoolProperty(name = "Add dot", default = False, update = propertyChanged)
{%- endblock %}
{%- block draw %}
        col = layout.column(align = True)
        col.prop(self, "dot", text = "", icon = "RADIOBUT_ON")
{%- endblock %}
{%- block execode -%}
        yield "opts_ = ', '.join(opts_)"
        yield "args_ = '('+', '.join(args_)+')'"
        
        yield "if len(opts_): sep=', '"
        yield "else: sep=''"
        yield "if self.dot: dot_='.'"
        yield "else: dot_=' '"        
        
        yield "send = dot_ +'{{ fn_name }}' + args_ + sep+ opts_"
{%- endblock -%}


        