{% extends "base.py" %}



{% block extra_create %}
        self.newInput("String", "prefix", "prefix_")
        self.newInput("String", "postfix", "postfix_")
{%- endblock %}

{% block post_create %}
{{ macro.hideInput(count_args, post_args ) }}       
{%- endblock %}

{%- block extra_input %}
        if s["prefix"].isUsed: yield "prefix = prefix_ "
        if s["postfix"].isUsed: yield "postfix = postfix_ "
{%- endblock %}

{%- block execode -%}
{{ super() }}  
{{ macro.no_block_send() }}         
{%- endblock %}

{%- block infoMessage %}
        yield 'if len(send): self.infoMessage = send[0]' 
{%- endblock %}