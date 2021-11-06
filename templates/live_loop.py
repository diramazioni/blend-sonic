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
        bpy.context.scene['sp_loop'] = {self.identifier: ''}
{%- endblock -%}


{%- block execode %}

        # if self.identifier in bpy.context.scene['sp_loop']:
        # else:
        #     yield "old_name = '' ; print('new session')"
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

#       "bpy.context.scene['sp_loop'][self.auto_name] = False;"
        #         # "self.infoMessage = '[stop]';" \
        #
        # yield "if not bpy.context.scene['sp_loop'][self.auto_name]:" \


{{ macro.opt_join() }}
{{ macro.arg_join() }}
{{ macro.block_send('', 'self.auto_name') }}

        yield "if not play: " \
              "send = f_call + ['stop']+ do_end + ['end'];"

{%- endblock %}


