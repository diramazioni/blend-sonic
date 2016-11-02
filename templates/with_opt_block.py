{% extends "base.py" %}


{%- block draw %}
{{ super() }}
{% endblock %}

{%- block create %}{%- endblock -%}

{%- block extra_create %}
{%- if fn.intro_fn %}
        self.newInput("String", "intro var", "intro_fn", value = "foo = ")
{%- endif %}
{%- if fn.async_block %}
        self.newInput("String", "async block", "async_block", value = "|bar|")
{%- endif %}
        self.newInput("String List", "do_end lines", "do_end")
{%- endblock %}

{% block post_create %}
{{ macro.hideInput(count_args, post_args ) }}        
{%- endblock %}

{%- block extra_input %}
        if s["intro var"].isUsed: yield "prefix = intro_fn +' '"
        if s["async block"].isUsed: yield "async = ' ' + async_block"
        else: yield "async = ''"
{%- endblock %}
{%- block execode -%}
{{ super() }}  
        yield "args_ = ' '+', '.join(args_)"
        yield "f_call = prefix + '{{ fn.name }}' + args_ + sep+ opts_ "
        if s["do_end lines"].isUsed: 
            yield "f_call = [f_call + ' do ' + async]"
            yield "send = f_call + do_end + ['end']"        
        else:
            yield "send = [f_call + async]"
{%- endblock %}

{%- block code_out %}
        yield 'code_out = code_in + send'
{%- endblock %}
{%- block infoMessage %}
        yield 'if len(send): self.infoMessage = send[0]' 
{%- endblock %}
