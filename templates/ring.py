{% extends "fn_simple.py" %}

{%- block execode %} 
        yield "list_ = list_[1:-1]"
{{ super() }}
{%- endblock %}