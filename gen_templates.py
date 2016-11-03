
import os
import shutil as sh
from jinja2 import Environment, FileSystemLoader


from collections import defaultdict, OrderedDict

from category_def import *

from constant_def import opts_default_val, opts_types_conversion, args_types_conversion


pwd = os.path.dirname(os.path.abspath(__file__))
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
        dst = os.path.join(pwd, 'nodes')
        sh.rmtree(dst)        
        os.makedirs(dst)
        src = os.path.join(pwd, templates, '__init__.py')
        dst = os.path.join(pwd, 'nodes', '__init__.py')
        sh.copy2(src,  dst)

        for cat in categories:
            if cat == 'common': continue
            dst = os.path.join(pwd, 'nodes', cat)
            os.makedirs(dst)
            dst = os.path.join(pwd, 'nodes', cat, '__init__.py')
            sh.copy2(src,  dst)

    def write_template(cat, context, fn_name, templ_name):
        print("w: %s %s %s " % (cat, templ_name, fn_name))
        dest_name = 'sp_' + fn_name + ext
        override_template = os.path.join(pwd, templates, fn_name + ext)
        in_template = os.path.join(pwd, templates, templ_name + ext)
        if os.path.exists(override_template): templ_name = fn_name + ext
        elif os.path.exists(in_template): templ_name = templ_name + ext
        else: raise Exception('template not found %s %s' % (fn_name, templ_name+ext))
        if cat == categories[0]: fname = os.path.join(pwd, 'nodes', dest_name)
        else: fname = os.path.join(pwd, 'nodes', cat, dest_name)
        with open(fname, 'w') as f:
            template_out = render_template(templ_name, context)
            f.write(template_out)
        written[templ_name].append(fn_name)

    def write_menu(menu):
        context = {
            'menu': menu,
            'categories': categories
        }
        dest_name = "node_menu.py"
        fname = os.path.join(pwd, 'ui', dest_name)
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
    ## is_inline_fn
    for fn_name in sub_list(all_lang_ref, is_to_hide):
        menu_levels = '....'
        # if fn_name is is_to_hide: continue
        if fn_name in is_inline_fn:
            category = categories[5] # functions

        elif fn_name in is_common:
            category = categories[0] # common
            menu_levels = '...'
        elif fn_name in has_requires_block:
            category = categories[3] # do_end
        elif fn_name in is_use_env:
            category = categories[4] # use
        elif fn_name in is_control:
            category = categories[6] # control
        elif fn_name in is_buffer_fn:
            category = categories[7] # buffer
        elif fn_name in has_modifies_env:
            category = categories[8]  # buffer
        else:
            category = categories[9] # general

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
    ## synths
    for synth_name, synth in all_synth.items():
        synth_name = synth_name[1:]
        templ_name = 'synth.py'
        
        context = {
            'synth_name': synth_name,
            'arg_defaults': synth['arg_defaults'],
            'synth': synth,
        }
        write_node("synth", context, synth_name, templ_name)

    
    '''
    write_menu(menu)

def copy_in_an():
    print("copy in Animation Nodes addon")
    dst = os.path.join(pwd, 'animation_nodes-master', 'nodes','sonic_pi')
    if os.path.exists(dst): sh.rmtree(dst)
    src = os.path.join(pwd, 'nodes')
    sh.copytree(src, dst, symlinks=True)
    src = os.path.join(pwd, 'constant_def.py')
    dst2 = os.path.join(dst, 'constant_def.py')
    sh.copy2(src,  dst2)
    src = os.path.join(pwd, 'templates', 'SonicPI_send.py')
    dst2 = os.path.join(dst, 'SonicPI_send.py')
    sh.copy2(src,  dst2)
    src = os.path.join(pwd, 'ui', 'node_menu.py')
    dst2 = os.path.join(pwd, 'animation_nodes-master', 'ui', 'node_menu.py')
    sh.copy2(src,  dst2)



def restore_orig():    
    src = os.path.join(pwd, 'templates', 'node_menu.orig.py')    
    dst = os.path.join(pwd, 'animation_nodes-master', 'ui', 'node_menu.py')
    sh.copy2(src,  dst)
    dst = os.path.join(pwd, 'animation_nodes-master', 'nodes','sonic_pi')
    if os.path.exists(dst): sh.rmtree(dst)
    
if __name__ == '__main__':
    import sys
    if not len(sys.argv[1:]):
        gen_an_code()
        copy_in_an()
        for k,v in written.items():
            print(k , sorted(v))
        print("DONE")
    else:            
        restore_orig()
        print("original restored")