{% extends "base.py" %}

{%- block imports %}
from .... base_types.node import AnimationNode
{% endblock %}

{%- block draw %}
{{ super() }}
{% endblock -%}

{%- block create %} 
{%- endblock -%}
{% block newInput%}
{%- endblock -%}
{%- block newOutput %}
        self.newOutput("String", "code out", "code_out")
{%- endblock -%}
{%- block execode -%} 
        yield "send = '({{ fn_name }} ' + ', '.join(args_) + ', '.join(opts_) + ')'"
{%- endblock -%}


{%- block execute -%}

{%- endblock -%} {# + ', '.join(args) + ', '.join(opts) #}

{%- block code_out %}
        yield 'code_out = send'
{% endblock %}        