{% extends "inline_fn.py" %}

{%- block execode -%} 
        yield "args_ = ', '.join(args_)"
        yield "opts_ = ', '.join(opts_)"
        yield "if len(opts_): sep=', '"
        yield "else: sep=''"
        yield "send = '({{ fn_name }} ' + args_ +sep+ opts_ + ')'"
{%- endblock -%}


        