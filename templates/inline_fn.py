{% extends "base.py" %}


{%- block draw %}
{{ super() }}
{% endblock -%}


{% block newInput%}
        self.newInput("Text", "line in", "code_in")
{%- endblock -%}
{%- block newOutput %}
        self.newOutput("Text", "line out", "code_out")
{%- endblock -%}

{% block extra_create %}
        self.newInput("Text", "prefix", "prefix_")
        self.newInput("Text", "postfix", "postfix_")
{%- endblock %}

{% block post_create %}
{{ macro.hideInput(count_args, post_args ) }}       
{%- endblock %}

{%- block extra_input %}
        if s["prefix"].isUsed: yield "prefix = prefix_"
        if s["postfix"].isUsed: yield "postfix = postfix_ "
{%- endblock %}

{%- block execode %}
{{ macro.opt_join() }} 
{{ macro.inline_send() }} 
{%- endblock -%}

{%- block code_out %}
        yield 'code_out = code_in + send'
{%- endblock %}

      