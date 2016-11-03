{% extends "with_block.py" %}

{%- block execode %}
{{ macro.opt_join() }} 
{{ macro.arg_join() }} 
{{ macro.block_send('with_fx ') }}
{%- endblock %}