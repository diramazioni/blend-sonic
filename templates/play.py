{% extends "base.py" %}

{%- block draw %}
        pass
{% endblock -%}

{%- block create %} {{ super() }}
        self.newInput("Float", "Note Freq", "freq", value = 80.0)
{% endblock %}

{% block execode -%}
if s["Note Freq"].isUsed: yield "arg = [str(freq)]+arg" 
{%- endblock %}

{%- block execute -%}
        send = ['play {0}'.format(', '.join(arg)) ]
{%- endblock %}