{% extends "with_block.py" %}

{% block imports %}
{{ super() }}
from ... events import propertyChanged
import string
import random
{% endblock %}

{%- block classMembers %}
    play: BoolProperty(name="stop/play the loop", default=True, update=propertyChanged)
    auto_name: StringProperty()
{%- endblock %}

{% block util_func %}
    def name_generator(self,size=5, chars=string.ascii_uppercase):
       return ':'+''.join(random.choice(chars) for _ in range(size))

{% endblock -%}

{%- block draw -%}
{{ super() }}
        col = layout.column(align=True)
        col.prop(self, "play", text="", icon="OUTLINER_OB_SPEAKER")
{%- endblock -%}

{%- block create %}
        self.auto_name = self.name_generator()
        if 'sp_loop' in bpy.context.scene:
            bpy.context.scene['sp_loop'][self.identifier] = ''
        else:
            bpy.context.scene['sp_loop'] = {self.identifier: ''}

{%- endblock -%}


{%- block execode %}
        if not self.identifier in bpy.context.scene['sp_loop']: bpy.context.scene['sp_loop'][self.identifier] = ''
        yield "old_name = bpy.context.scene['sp_loop'][self.identifier]"
        yield "play = self.play;  name_ = self.auto_name;"
        yield "if not play and old_name == name_:" \
              "self.infoMessage = 'stoping ' + name_;" \
              "bpy.context.scene['sp_loop'][self.identifier] = ''"
        yield "elif play and old_name != name_:" \
              "name_ = self.auto_name;" \
              "self.auto_name = self.name_generator();" \
              "bpy.context.scene['sp_loop'][self.identifier] = self.auto_name;" \
              "self.infoMessage = 'new ' + self.auto_name;"
        yield "elif not play and old_name != name_: self.infoMessage = 'stop'"
        yield "else : self.infoMessage = 'play ' + name_"


{{ macro.opt_join() }}
{{ macro.arg_join() }}

        yield "f_call = intro_fn_ + '{{fn.name}} ' + self.auto_name + args_ + sep + opts_ "
        yield "f_call = [f_call + ' do ' + async_]"
        yield "send = f_call + do_end + ['end']"

        yield "if not play: " \
              "send = f_call + ['stop']+ do_end + ['end'];"

{%- endblock %}


