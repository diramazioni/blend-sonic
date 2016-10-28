{% extends "base.py" %}


{%- block draw %}
{{ super() }}
{% endblock -%}

{%- block create %}{%- endblock -%}
{% block newInput%}
        self.newInput("String", "line in", "code_in")
{%- endblock -%}
{%- block newOutput %}
        self.newOutput("String", "line out", "code_out")
{%- endblock -%}
{%- block execode -%}        
{{ super() }}     
{%- endblock -%}


{%- block execute -%}{%- endblock -%} 
{%- block code_out %}
        yield 'self.infoMessage = send' 
        yield 'code_out = code_in + send'
{%- endblock %}

      