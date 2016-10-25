
import os
import shutil as sh
from jinja2 import Environment, FileSystemLoader

from collections import defaultdict, OrderedDict

from category_def import *
from lang_doc import *
from constant_def import opts_default_val, opts_types_conversion, args_types_conversion


pwd = os.path.dirname(os.path.abspath(__file__))
written = defaultdict(list)
 
def render_template(template_file, context):
    template_env = Environment( 
        autoescape = False, loader = FileSystemLoader(os.path.join(pwd, 'templates')), trim_blocks = False )
    return template_env.get_template(template_file).render(context)
 
 
def gen_an_code():
    def prep_dir(categories):
        print("preparing nodes directory")
        dst = os.path.join(pwd, 'nodes')
        sh.rmtree(dst)        
        os.makedirs(dst)
        src = os.path.join(pwd, 'templates', '__init__.py')
        dst = os.path.join(pwd, 'nodes', '__init__.py')
        sh.copy2(src,  dst)

        for cat in categories:
            if cat == 'common': continue
            dst = os.path.join(pwd, 'nodes', cat)
            os.makedirs(dst)
            dst = os.path.join(pwd, 'nodes', cat, '__init__.py')
            sh.copy2(src,  dst)

    def write_node(cat, context, fn_name, templ_name):
        print("w: %s %s %s " % (cat, templ_name, fn_name))
        dest_name = 'sp_' + fn_name + ".py"
        templ_name = templ_name + '.py'
        fname = os.path.join(pwd, 'nodes', cat, dest_name)
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
    ## is_inline_fn
    for fn_name in is_inline_fn:
        category = categories[4]
        if fn_name in fn_simple + fn_embeded:
            templ_name = "fn_simple"
        elif fn_name in fn_normal:
            templ_name = "fn_normal"
        else:
            templ_name = "fn_simple"

        fn = lng(fn_name )
        
        context = {
            'fn_name': fn_name,
            'fn': fn,
            'args_types': args_types_conversion,
            'opts_types': opts_types_conversion
        }
        menu[category][fn_name] = fn
        write_node(category, context, fn_name, templ_name)

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

    ## fx
    for synth_name, synth in all_fx.items():
        synth_name = synth_name[1:]
        templ_name = 'fx.py'
        
        context = {
            'synth_name': synth_name,
            'arg_defaults': synth['arg_defaults'],
            'synth': synth,
        }
        write_node("fx", context, synth_name, templ_name)
    
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