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
        self.newInput("String", "line in", "code_in")
{%- endblock -%}
{%- block newOutput %}
        self.newOutput("String", "line out", "code_out")
{%- endblock -%}
{%- block execode -%}        
        yield "send = '({{ fn_name }} ' + ', '.join(args_) + ', '.join(opts_) + ')'"
{%- endblock -%}


{%- block execute -%}{%- endblock -%} 
    {%- block code_out %}
        yield 'code_out = code_in + send'
    {%- endblock %}

      