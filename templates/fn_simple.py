{% extends "inline_fn.py" %}

{%- block execode -%} 
        {{ super() }}
        yield "args_ = ', '.join(args_)"
        yield "send = '({{ fn.name }} ' + args_ +sep+ opts_ + ')'"
{%- endblock -%}


        