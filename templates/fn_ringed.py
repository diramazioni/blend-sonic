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
        yield "args_ = ', '.join(args_) if len(args_ ) else ''"

        yield "if self.dot: send = list_+'.'+'{{ fn.name }}' +args_ +sep +opts_"
        yield "else: send = '{{ fn.name }}' + '(' + list_ +args_ +sep +opts_+')'"        

        #yield "send = dot_ +'{{ fn.name }}' + args_ + sep+ opts_"
{%- endblock -%}


        