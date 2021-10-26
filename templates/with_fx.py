{% extends "with_block.py" %}

{%- block newOutput %}
{{ super() }}
        self.newOutput("String List", "opt out", "opt_out")
{%- endblock -%} 

{%- block execode %}
        yield "opt_out = opts_"
{{ macro.opt_join() }} 
{{ macro.arg_join() }} 
{{ macro.block_send('with_fx ') }}
{%- endblock %}