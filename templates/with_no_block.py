{% extends "base.py" %}



{%- block create %}{%- endblock -%}


{%- block execode -%}
{{ super() }}  
        yield "args_ = '('+', '.join(args_)+')'"
        yield "send = ['{{ fn_name }}' + args_ + sep+ opts_ ]"
{%- endblock %}

{%- block infoMessage %}
        yield 'self.infoMessage = send[0]' 
{%- endblock %}