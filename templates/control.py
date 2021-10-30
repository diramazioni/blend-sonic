{% extends "with_no_block.py" %}



{% block extra_create %}
{{ super() }}
        self.newInput("Float", "number", "number_")
{%- endblock %}
{%- block extra_input %}
{{ super() }}
        if s["number"].isUsed: yield "postfix += str(round(number_, 2)) +' '"
{%- endblock %}


{%- block execode %}
        #if s["node"].isUsed: yield "if nodeIn in bpy.context.scene['sp_var']: print(bpy.context.scene['sp_var'][nodeIn])"
{%- endblock %}

{#
{% block create %}
        self.newInput("Text List", "opt in", "opt_in")
{%- endblock %}
{% block post_create %}
{{ macro.hideInput(2, post_args ) }}       
    def edit(self):
        inputSocket = self.inputs[1]
        dataOrigin = inputSocket.dataOrigin
        if dataOrigin is not None:
            self.recreateInputs()
{%- endblock %}

{%- block recreateInputs %}
        if self.inputs["opt in"].is_linked:
            print(self.activeInputIndex)
            opt_in_ = self.inputs["opt in"].value
            for opt in opt_in_:
                key, value = opt.split(':')
                print('opt', (key, value ))
{%- endblock %}

#}