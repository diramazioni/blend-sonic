{% macro hideInput(start, end) %}
        for socket in self.inputs[{{ start }}:{{ end }}]:
            socket.useIsUsedProperty = True
            socket.isUsed = False
            #socket.value = False
        for socket in self.inputs[{{ start }}:{{ end }}]:
            socket.hide = True
{%- endmacro %}

{%- macro inline_send(fn_name) %}
        yield "opts_ = ', '.join(opts_)"
        yield "sep=', ' if len(opts_) else '' "
        yield "args_ = ', '.join(args_)"
        yield "send = '({{ fn_name }} ' + args_ +sep+ opts_ + ')'"
{%- endmacro -%}