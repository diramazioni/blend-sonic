{% extends "inline_fn.py" %}

{%- block execode -%} 
{{ macro.opt_join() }} {{ macro.arg_join() }} 
{{ macro.fn_simple_send() }}
{{ macro.add_fix() }} 
{%- endblock -%}


        