{% extends "base.py" %}


{%- block draw %}
{{ super() }}
{% endblock %}

{%- block create %}{%- endblock -%}

{%- block extra_create %}
{{ macro.block_extra_create() }}
{%- endblock %}

{% block post_create %}
{{ macro.hideInput(count_args, post_args ) }}        
{%- endblock %}

{%- block extra_input %}
{{ macro.block_extra_input() }}     
{%- endblock %}


{%- block execode -%}
{{ super() }}  
{{ macro.opt_block_send() }}
{%- endblock %}

{%- block code_out %}
        yield 'code_out = code_in + send'
{%- endblock %}
{%- block infoMessage %}
        yield 'if len(send): self.infoMessage = send[0]' 
{%- endblock %}
