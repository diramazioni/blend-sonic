{% extends "inline_fn.py" %}

{%- block execode -%}
{{ macro.opt_join() }}
{{ macro.arg_join() }} 
        yield "if len(args_): args_= '('+ args_ +')'"
        yield "send = '{{ fn.name }}' + args_ +sep+ opts_ "
{{ macro.add_fix() }}         
{%- endblock -%}


        