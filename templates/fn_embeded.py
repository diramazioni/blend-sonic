{% extends "inline_fn.py" %}

{%- block execode -%} 
{{ macro.opt_join() }}
{{ macro.arg_join() }}
{{ macro.fn_embeded_send() }}
{{ macro.add_fix() }} 
{%- endblock -%}


        