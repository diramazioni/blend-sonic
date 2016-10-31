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

{% block post_create %}
        self.newInput("String", "prefix", "prefix_")
        self.newInput("String", "postfix", "postfix_")
{{ hideInput(count_args, post_args ) }}        
{%- endblock %}
{%- block extra_input %}
        if s["prefix"].isUsed: yield "prefix = prefix_ +' '"
        if s["postfix"].isUsed: yield "postfix = ' ' + postfix_ "
{%- endblock %}
{%- block execode -%}        
{{ super() }}     
{%- endblock -%}

{%- block execute -%}{%- endblock -%} 
{%- block code_out %}
        yield 'code_out = code_in + prefix + send + postfix'
{%- endblock %}

      