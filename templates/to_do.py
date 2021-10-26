{% extends "base.py" %}

{%- block imports %}
from ... base_types.node import AnimationNode
{% endblock %}

{%- block draw %}
        pass
{% endblock -%}

{%- block create %} {{ super() }}
{% endblock %}

{%- block execode -%}
{{ super() }}
{%- endblock %}

{%- block execute -%}
        send = [{{ fn_name }}]
{%- endblock %}