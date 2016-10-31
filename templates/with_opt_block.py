{% extends "base.py" %}


{%- block draw %}
{{ super() }}
{% endblock %}

{%- block create %}{%- endblock -%}
{% block post_create %}
{%- if fn.intro_fn or category == "functions"%}
        self.newInput("String", "intro var", "intro_fn", value = "foo = ")
{%- endif %}
{%- if fn.async_block %}
        self.newInput("String", "async block", "async_block", value = "|bar|")
{%- endif %}
        self.newInput("String List", "do_end lines", "do_end")
{{ hideInput(count_args, post_args ) }}        
{%- endblock %}
{%- block extra_input %}
        if s["intro var"].isUsed: yield "prefix = intro_fn +' '"
        if s["async block"].isUsed: yield "postfix = ' ' + async_block"
{%- endblock %}
{%- block execode -%}
{{ super() }}  
        yield "args_ = ' '+', '.join(args_)"
        yield "f_call = prefix + '{{ fn.name }}' + args_ + sep+ opts_ "
        if s["do_end lines"].isUsed: 
            yield "f_call = [f_call + ' do ' + postfix]"
            yield "send = f_call + do_end + ['end']"        
        else:
            yield "send = [f_call + postfix]"
{%- endblock %}

{%- block code_out %}
        yield 'code_out = code_in + send'
{%- endblock %}
{%- block infoMessage %}
        yield 'self.infoMessage = send[0]' 
{%- endblock %}
