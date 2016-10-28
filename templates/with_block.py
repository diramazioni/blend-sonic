{% extends "base.py" %}

{%- block imports %}
from .... base_types.node import AnimationNode
{% endblock %}

{%- block draw %}
{{ super() }}
{% endblock -%}

{% block newInput%}
        self.newInput("String List", "do_end lines", "do_end")
{%- endblock -%}


{%- block create %}{%- endblock -%}
{% block post_create %}
{% set post_args = -1 %}
{%- endblock -%}

{%- block execode -%}
{{ super() }}  
        do_end = [' do '] + do_end + ['end']
        do_end_ = '\n'.join(do_end)
        yield "args_ = ' '+', '.join(args_)"
        yield "send = '{{ fn_name }}' + args_ + sep+ opts_ + do_end"
{%- endblock %}

