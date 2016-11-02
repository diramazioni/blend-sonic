{% extends "with_opt_block.py" %}

{% block imports %}
{{ super() }}
from {{ menu_levels }} events import propertyChanged
from {{ menu_levels[2:] }} constant_def import samples
s_name = [sn for sk in samples.keys() for sn in samples[sk] ]
sample_items = [(k,k[1:],'') for k in s_name ]
{% endblock %}

{%- block classMembers %}
{{ super() }}
{{ macro.enum_member("sampleList", "Sample", "sample_items")  }} 
{%- endblock %}

{%- block draw %}
{{ super() }}
{{ macro.next_prev_buttons("sampleList") }}   
{%- endblock %}

{%- block post_create %}
{{ macro.hideInput(count_args, post_args ) }} 
{{ macro.next_prev("sampleList", "s_name") }}
{%- endblock %}


{%- block checkEnum %}
        if not s["name_or_path"].isUsed:
            yield "args_.append(str(self.sampleList))"
{%- endblock %}