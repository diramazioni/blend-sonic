{% extends "degree.py" %}

{%- block checkArgs %}        
    {%- if fn.alt_args %}
        {{ macro.argCheck(fn.alt_args) }}
    {% endif %}        
    {%- if fn.args %}
        {{ macro.argCheck(fn.args) }}
    {% endif %}        
    {%- if fn.opts %}
        {{ macro.optCheck() }}
    {% endif %}
{%- endblock %}