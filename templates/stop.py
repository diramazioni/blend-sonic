{% extends "with_no_block.py" %}



{%- block execode -%}
{{ super() }}          
        yield "if args_ == '(true)': send = ['stop']"
        yield "else: send = []"
{%- endblock %}

