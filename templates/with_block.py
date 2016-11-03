{% extends "base.py" %}


{%- block draw %}
{{ super() }}
{% endblock %}

{%- block create %}{%- endblock -%}

{%- block extra_create %}
{{ macro.block_extra_create() }}  
{%- endblock %}

{% set post_args = -1 %}
{% block post_create %}
{{ macro.hideInput(count_args, post_args ) }}        
{%- endblock %}

{%- block extra_input %}
{{ macro.block_extra_input() }}     
{%- endblock %}

{%- block execode %}
{{ super() }}
{{ macro.block_send('') }}     
{%- endblock %}

{%- block code_out %}
        yield 'code_out = code_in + send'
{%- endblock %}

{%- block infoMessage %}
        #yield 'if len(do_end): self.infoMessage = send[0]' 
{%- endblock %}