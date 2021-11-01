
import os
import shutil as sh
from jinja2 import Environment, FileSystemLoader


from collections import defaultdict, OrderedDict

from category_def import *

from constant_def import opts_default_val, opts_types_conversion, args_types_conversion


pwd = os.path.dirname(os.path.abspath(__file__))
nodes = os.path.join(pwd, 'build', 'nodes')
ui = os.path.join(pwd, 'build', 'ui')

written = defaultdict(list)
templates = 'templates'
ext = ".py"
 
def render_template(template_file, context):

    template_env = Environment(
        autoescape = False, loader = FileSystemLoader(os.path.join(pwd, templates)), extensions=['jinja2.ext.with_'], trim_blocks = False )
    return template_env.get_template(template_file).render(context)
 
 
def gen_an_code():
    def prep_dir(categories):
        print("preparing nodes directory")
        for dst in [nodes, ui]:
            if os.path.exists(dst):
                sh.rmtree(dst)
            os.makedirs(dst)
            src = os.path.join(pwd, templates, '__init__.py')
            dst = os.path.join(nodes, '__init__.py')
            sh.copy2(src,  dst)

        for cat in categories:
            if cat == 'common': continue
            dst = os.path.join(nodes, cat)
            os.makedirs(dst)
            dst = os.path.join(nodes, cat, '__init__.py')
            sh.copy2(src,  dst)

    def write_template(cat, context, fn_name, templ_name):
        print("w: %s %s %s " % (cat, templ_name, fn_name))
        dest_name = 'sp_' + fn_name + ext
        override_template = os.path.join(pwd, templates, fn_name + ext)
        in_template = os.path.join(pwd, templates, templ_name + ext)
        if os.path.exists(override_template): templ_name = fn_name + ext
        elif os.path.exists(in_template): templ_name = templ_name + ext
        else: raise Exception('template not found %s %s' % (fn_name, templ_name+ext))
        if cat == categories[0]: fname = os.path.join(nodes, dest_name)
        else: fname = os.path.join(nodes, cat, dest_name)
        with open(fname, 'w') as f:
            template_out = render_template(templ_name, context)
            f.write(template_out)
        written[templ_name].append(fn_name)

    def insert_in_file(file_path, search, insert):
        import fileinput
        for line in fileinput.FileInput(file_path, inplace=1):
            if search in line:
                line = line.replace(line, line + insert)
                print(line, end='')
            else:
                print(line, end='')

    def write_menu_template(dest_name):
        # copy original
        src = os.path.join(pwd, 'sub', 'animation_nodes', 'animation_nodes', 'ui', 'node_menu.py')
        dst = os.path.join(pwd, templates, 'node_menu.py')
        sh.copy2(src, dst)
        search = 'layout.menu("AN_MT_sound_menu"'
        insert = '''{% block layout_main %}
    layout.menu("SP_MT_menu", text = "Sonic-PI", icon = "SOUND")
{% endblock %}
'''
        insert_in_file(file_path=dst, search=search, insert=insert)
        search = 'bpy.context.space_data.node_tree'
        insert = '''
{% macro insNode(synth_name, synth_descr) -%}
        insertNode(layout, "an_sp_{{ synth_name|capitalize }}Node", "{{synth_descr}}")
{%- endmacro %}

{% block new_menu %}
class SonicPI_Menu(bpy.types.Menu):
    bl_idname = "SP_MT_menu"
    bl_label = "Sonic-PI Menu"

    def draw(self, context):
        layout = self.layout
        {{ insNode('send', 'Send to SonicPI') }}
        {% for fn_name, fn in menu['common']|dictsort %}
        {{ insNode(fn_name, fn.name) }}
        {%- endfor %}
        layout.separator()

        {% for cat in categories[1:] %}
        layout.menu("SP_MT_{{ cat }}_menu", text = "{{ cat|capitalize }}")
        {%- endfor %}
        

        #layout.menu("SP_MT_synth_menu", text = "Synth")
        #layout.menu("SP_MT_fx_menu", text = "FX")
{% for cat in categories[1:] %}

class SonicPI_{{ cat|capitalize }}_Menu(bpy.types.Menu):
    bl_idname = "SP_MT_{{ cat }}_menu"
    bl_label = "{{ cat|capitalize }} Menu"

    def draw(self, context):
        layout = self.layout
        {% for synth_name, synth in menu[cat]|dictsort %}
        {{ insNode(synth_name, synth_name) }}
        {%- endfor %}
{%- endfor %}     
{% endblock -%}    

'''
        insert_in_file(file_path=dst, search=search, insert=insert)

    def write_menu(menu):
        dest_name = "node_menu.py"
        write_menu_template(dest_name)
        context = {
            'menu': menu,
            'categories': categories
        }


        fname = os.path.join(ui, dest_name)

        with open(fname, 'w') as f:
            template = render_template(dest_name, context)
            f.write(template)
        written[dest_name].append('menu')

    # categories


    prep_dir(categories)
    menu = defaultdict(dict)
    context = {
        'args_types': args_types_conversion,
        'opts_types': opts_types_conversion,
    }

    for fn_name in sub_list(all_lang_ref, is_to_hide):
        ########################
        #   menu assignment
        menu_levels = '....'
        # if fn_name is is_to_hide: continue
        if fn_name in is_fn:
            category = categories[5] # functions

        elif fn_name in is_common:
            category = categories[0] # common
            menu_levels = '...'
        elif fn_name in has_requires_block:
            category = categories[3] # block
        elif fn_name in is_use_env:
            category = categories[4] # use
        elif fn_name in is_control:
            category = categories[6] # control
        elif fn_name in is_buffer_fn:
            category = categories[7] # buffer
        elif fn_name in has_modifies_env:
            category = categories[8]  # env
        else:
            category = categories[9] # general
        ########################
        #   template assignment
        if fn_name in fn_simple + fn_embeded:
            templ_name = "fn_simple"
        elif fn_name in fn_normal:
            templ_name = "fn_normal"
        elif fn_name in fn_ringed:
            templ_name = "fn_ringed"
        elif fn_name in has_requires_block:
            templ_name = "with_block"
        elif fn_name in has_accepts_block_false:
            templ_name = "with_no_block"
        elif fn_name in sub_list(has_accepts_block, has_requires_block):  # optional block
            # templ_name = "with_no_block"
            templ_name = "with_opt_block"
        else:
            templ_name = None
        if not templ_name: continue
        fn = lng(fn_name )

        context.update({
            'fn_name': fn_name,
            'fn': fn,
            "menu_levels": menu_levels,
            "category": category
        })
        menu[category][fn_name] = fn

        write_template(category, context, fn_name, templ_name)
    ## fx
    for synth_name, synth in fx.items():
        if synth['hiden']: continue
        menu_levels = '....'
        # fn_name =  synth['name'][1:]
        synth_name = synth_name[2:]
        templ_name = 'with_fx'
        category = categories[2]

        fn = lng('with_fx')
        fn.update(synth)

        context.update({
            'fn_name': synth_name,
            'fn': fn,
            "menu_levels": menu_levels,
            "category": category
        })
        menu[category][synth_name] = fn
        write_template("fx", context, synth_name, templ_name)
    '''
    for synth_name, synth in synths.items():
        if synth['hiden']: continue
        menu_levels = '....'
        # fn_name =  synth['name'][1:]
        synth_name = synth_name[2:]
        templ_name = 'with_fx'
        category = categories[2]

        fn = lng('with_fx')
        fn.update(synth)

        context.update({
            'fn_name': synth_name,
            'fn': fn,
            "menu_levels": menu_levels,
            "category": category
        })
        menu[category][synth_name] = fn
        write_template("fx", context, synth_name, templ_name)
    '''
    write_menu(menu)

def copy_in_an():

    print("copy in Animation Nodes addon")
    dst = os.path.join(pwd, 'build', 'animation_nodes', 'nodes','sonic_pi')
    if os.path.exists(dst): sh.rmtree(dst)
    src = nodes
    sh.copytree(src, dst, symlinks=True)
    src = os.path.join(pwd, 'constant_def.py')
    dst2 = os.path.join(dst, 'constant_def.py')
    sh.copy2(src,  dst2)
    src = os.path.join(pwd, 'templates', 'SonicPI_send.py')
    dst2 = os.path.join(dst, 'SonicPI_send.py')
    sh.copy2(src,  dst2)
    ### node_menu
    src = os.path.join(ui, 'node_menu.py')
    dst2 = os.path.join(pwd, 'build', 'animation_nodes', 'ui', 'node_menu.py')
    sh.copy2(src,  dst2)


def restore_orig():
    src = os.path.join(pwd, 'sub', 'animation_nodes', 'animation_nodes')
    dst = os.path.join(pwd, 'build', 'animation_nodes')
    if os.path.exists(dst): sh.rmtree(dst)
    sh.copytree(src, dst)

    
if __name__ == '__main__':
    import sys
    if not len(sys.argv[1:]):
        gen_an_code()
        copy_in_an()
        for k,v in written.items():
            print(k , sorted(v))
        print("Template Generation finished!")
    else:            
        restore_orig()
        print("original animation_nodes restored")