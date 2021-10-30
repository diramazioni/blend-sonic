{% extends "base.py" %}


{%- block draw %}
{{ super() }}
        row = layout.row(align = True)
        self.invokeFunction(row, "newInputSocket",
            text = "New Input",
            description = "Create a new input socket",
            icon = "PLUS")
        self.invokeFunction(row, "removeUnlinkedInputs",
            description = "Remove unlinked inputs",
            confirm = True,
            icon = "X")        
{% endblock %}


{%- block create %}{%- endblock -%}
{% block post_create %}
{% set post_args = -1 %}
        self.newInput("Text List", "do_end lines", "do_end")
{{ hideInput(count_args, post_args ) }}        
{%- endblock %}

{%- block execode -%}
{{ super() }}  
        yield "args_ = ' '+', '.join(args_)"
        yield "f_call = '{{ fn.name }}' + args_ + sep+ opts_ "        
        yield "f_call = [f_call + ' do ']"
        yield "do_end = f_call + do_end + ['end']"
        yield "print(do_end )"
        yield "send = do_end"
{%- endblock %}

{%- block code_out %}
        yield 'self.infoMessage = f_call[0]' 
        yield 'code_out = code_in + send'
{%- endblock %}