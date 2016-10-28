{% extends "base.py" %}


{%- block draw %}
{{ super() }}
{% endblock %}

{%- block create %}{%- endblock -%}
{% block post_create %}
{% set post_args = -1 %}
        self.newInput("String List", "do_end lines", "do_end")
{%- endblock %}

{%- block execode -%}
{{ super() }}  
        yield "do_end = [' do '] + do_end + ['end']"
        yield "print(do_end )"
        yield "do_end_ = ', '.join(do_end)"
        yield "args_ = ' '+', '.join(args_)"
        yield "send = '{{ fn.name }}' + args_ + sep+ opts_ + do_end"
{%- endblock %}

