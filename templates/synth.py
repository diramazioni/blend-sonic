{% extends "base.py" %}

{%- block imports %}
from .... base_types.node import AnimationNode
{% endblock %}

{%- block draw %}
        pass
{% endblock -%}

{%- block create %} {{ super() }}
{% endblock %}

{%- block execode -%}
    yield "send = ['use_synth_defaults {0}'.format(', '.join(opts)) ]"
{%- endblock %}

{%- block execute -%}
    send = ['use_synth :{{ synth_name }} '] + send       
{%- endblock %}