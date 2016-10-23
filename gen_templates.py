
import os
import shutil as sh
from jinja2 import Environment, FileSystemLoader


from constant_def import opts_default_val, opts_types_conversion, args_types_conversion
from lang_def import *

    #generators, all_synth, all_fx

pwd = os.path.dirname(os.path.abspath(__file__))

 
def render_template(template_file, context):
    template_env = Environment( 
        autoescape = False, loader = FileSystemLoader(os.path.join(pwd, 'templates')), trim_blocks = False )
    return template_env.get_template(template_file).render(context)
 
 
def gen_an_code():
    def prep_dir():
        print("preparing nodes directory")
        dst = os.path.join(pwd, 'nodes')
        sh.rmtree(dst)        
        os.makedirs(dst)
        src = os.path.join(pwd, 'templates', '__init__.py')
        dst = os.path.join(pwd, 'nodes', '__init__.py')
        sh.copy2(src,  dst)
        
        dst = os.path.join(pwd, 'nodes', 'synth')
        os.makedirs(dst)
        dst = os.path.join(pwd, 'nodes', 'synth', '__init__.py')
        sh.copy2(src,  dst)
        
        dst = os.path.join(pwd, 'nodes', 'fx')
        os.makedirs(dst)
        dst = os.path.join(pwd, 'nodes', 'fx', '__init__.py')
        sh.copy2(src,  dst)
        
    def write_node(cat, context, synth_name, templ_name):
        print("generating nodes for:", synth_name)
        if cat == "generators":
            dest_name = "SonicPI_"+synth_name+".py"
            cat = ""
        elif cat == "synth":
            dest_name = synth_name+".py"
        elif cat == "fx":
            dest_name = synth_name+".py"
        fname = os.path.join(pwd, 'nodes', cat, dest_name)
        with open(fname, 'w') as f:
            template = render_template(templ_name, context)
            f.write(template)        
    
    prep_dir()
    
    ## generators
    for synth_name, synth in generators.items():
        synth_name = synth_name[1:]
        templ_name = synth_name +'.py'
        
        context = {
            'synth_name': synth_name,
            'arg_defaults': synth['arg_defaults'],
            'synth': synth,
        }
        write_node("generators", context, synth_name, templ_name)
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
    
    
    
    context = {
        'generators': generators,
        'all_synth':all_synth, 
        'all_fx': all_fx
    }
    dest_name = "node_menu.py"
    fname = os.path.join(pwd, 'ui', dest_name)
    with open(fname, 'w') as f:
        template = render_template(dest_name, context)
        f.write(template)
    '''

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
        print("DONE")
    else:            
        restore_orig()
        print("original restored")