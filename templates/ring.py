{% extends "fn_embeded.py" %}

{%- block execode %} 
        yield "list_ = list_[1:-1]"
{{ super() }}
{%- endblock %}