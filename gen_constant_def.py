from transitions import Machine
import re

import inspect

'''
def generic_slide_doc(k):
    return "Amount of time (in beats) for the {0} value to change. A long {0}_slide value means that the {0} takes a long time to slide from the previous value to the new value. A {0}_slide of 0 means that the {0} instantly changes to the new value.".format(k)
def generic_slide_curve_doc(k):
    return "Shape of the slide curve (only honoured if slide shape is 5). 0 means linear and positive and negative numbers curve the segment up and down respectively."
def generic_slide_shape_doc(k):
    return "Shape of curve. 0: step, 1: linear, 3: sine, 4: welch, 5: custom (use *_slide_curve: opt e.g. amp_slide_curve:), 6: squared, 7: cubed. "
'''
class ParseSynth(object):
    
    '''
    def proc_arg_info(self):
        arg_dict = {}
        lines = self.lines[self.l+1:]
        doc = False
        k = ""
        for s in lines:
            self.l += 1
            if "end" in s: break
            if doc == False and "=>" in s:
                k = s.split("=>")[0].strip()
                continue
            elif "{" in s: 
                doc = True
                continue
            elif "}" in s: 
                doc = False
                continue
            elif ":doc =>" in s and doc: 
                d = s.split("=>")[1]
                if "generic_slide_doc" in d:
                    d = generic_slide_doc(k)
                elif "generic_slide_curve_doc" in d:
                    d = generic_slide_curve_doc(k)
                if "generic_slide_shape_doc" in d:
                    d = generic_slide_shape_doc(k)
                arg_dict[k] = d
                continue
        #print(arg_dict)
        return arg_dict
    '''
    line = ""
    def __init__(self, lines):
        self.lines = lines # all lines
        self.l = 0  # cursor of current line
        self.line = lines[self.l]
        #self.line = "" # current line
        
        
        self.class_name_dict = {}
        self.synths = {}
        
        self._debug = False
                
    def proc_class(self):
        print("> ", (self.line, self.l))
        
        class_match = re.match( r'.* class (.*) < (.*)\n', self.line)
        try:            
            m = class_match.group(1)
        except AttributeError:
            print("bailout not a class", (self.line, self.l))
            self.next_line()
            return False
        c_name , c_parent = (class_match.group(1), class_match.group(2))
        
        end_class = "    end\n"

        #self.next_line()        
        synth_name = ""
        synth_descr = ""
        arg_def = {}

        while self.line != end_class:            
            s = self.line            
            if "def name" in s:                
                self.next_line()
                synth_descr = self.line.strip().strip('"')                
            elif "def synth_name" in s:
                self.next_line()
                synth_name = self.line.strip().strip('"')
            elif "def arg_defaults" in s:
                self.next_line(); self.next_line()                
                while "}" not in self.line:
                    l = self.line.strip()
                    if not l: self.next_line(); continue
                    arg, v = l.split('=>')                   
                    v = v.strip(',').strip()
                    arg = arg.strip()[1:] + ":" # remove : and add @end
                    arg_def[arg.strip()] = v
                    self.next_line()
                for k, v in arg_def.items(): # fix value reference
                    if v[0] == ":":
                        v = v[1:]+ ":" 
                        ref = arg_def[v]
                        print(k,v,ref)
                        arg_def[k] = eval(str(ref))
                    else: arg_def[k] = eval(v)
            else:                 
                self.next_line()

        if not len(synth_name): 
            #print("EMPTY"); 
            self.next_line()
            self.empty_skip()
            return True
        synth_name = ":" + synth_name
        self.class_name_dict[c_name] = synth_name
        
        baseClass = ["SonicPiSynth","Pitchless", "FXInfo", 
                     "BaseInfo", "StudioInfo",  "BaseMixer"]
        user_facing = baseClass[:3] 
        # no "BaseInfo", "StudioInfo", "BaseMixer",

        hiden = 0
        def inherit_super(parent):
            parent_synt_name = self.class_name_dict[parent] # take the ref by class
            parent_synt = self.synths[parent_synt_name]            
            if parent_synt:
                arg_def.update(parent_synt["arg_defaults"])
                return parent_synt['inherit_base']
        
        super_c = c_parent        
        while super_c not in baseClass:
            super_c = inherit_super(super_c)
        if super_c not in user_facing:
            print("/ ", super_c)
            hiden = 1

        self.synths[synth_name] = {
            "descr": synth_descr, 
            "arg_defaults": arg_def,
            "class_name": c_name,
            "inherit_base": c_parent,
            "hiden": hiden,
        }
        self.goNext()
        
        return True

    def parse_play_opts(self):
        arg_def = {}
        self.skip_to("DEFAULT_PLAY_OPTS")
        self.next_line()
        while len(self.line.strip()) >0:
            k = self.line.split(":")[0].strip()
            if k:
                arg_def[k+":"] = 1
            self.next_line()
        # Guess the defaults zero arg.... if someone knows tell me
        for k in ["pan:", "slide:", "pitch:"]:
            arg_def[k] = 0       
        return arg_def

    def empty_skip(self):
        while self.line == '\n':
            self.next_line()
        
    def next_line(self):
        self.l = self.l + 1
        self.line = self.lines[self.l]
        '''
        if self._debug:
            curframe = inspect.currentframe()
            calframe = inspect.getouterframes(curframe, 2)
            print('next line call from :', calframe[1][3], calframe[1][2])
        '''
    def skip_to(self, match):        
        #print("skip>", match)
        while match not in self.line:
            self.next_line()
              
    def goNext(self):
        self.next_line()
        self.empty_skip()

       
    
def parseSynth():
    with open('sonicpi/synths/synthinfo.rb') as infile:
        const_file = infile.readlines()
    ps = ParseSynth(const_file)
    '''
    ps.skip_to("class BaseInfo")
    ps.skip_to("def default_arg_info")    
    arg_base = ps.proc_arg_info()
    print(arg_base)
    ps.synths['__BaseInfo__'] = {'arg_info':arg_base}
    '''
    ps.skip_to("class SoundIn < SonicPiSynth")
    stop_class_line = '    class BaseInfo\n'
    while(ps.line != stop_class_line):
        #ps.empty_skip()
        op = ps.proc_class()
        if not op:
            print("ops")
            break
    return ps

def parseSound()
    with open('sonicpi/lang/sound.rb') as infile:
        const_file = infile.readlines()
    ps = ParseSynth(const_file)
    arg_defaults = ps.parse_play_opts()
    print(arg_defaults)
    ps.synths['#play'] = {"arg_defaults":arg_defaults, "descr": "play notes", "hiden": 1, "class_name": "Play"}
    
    return ps

def dump_dict(synths):
    import json
    helper_func = '''
def all_def():
    return { key: value for key, value in synths.items() if value['hiden'] != True }
all_def = all_def()

def all_synth():
    return { key: value for key, value in synths.items() if value['hiden'] != True  if value['inherit_base'] in ["SonicPiSynth", "Pitchless"]}
all_synth = all_synth()

def all_fx():
    return { key: value for key, value in synths.items() if value['hiden'] != True  if value['inherit_base'] == "FXInfo"}
all_fx = all_fx()

def generators():
    return { key: value for key, value in synths.items() if key.startswith('#') }
generators = generators()

if __name__ == '__main__':
    print("synth: ", len(all_synth))
    print("fx: ",len(all_fx))
    print("gen: ",len(generators))
    '''
    def dict2var(dictionary):
        text = []
        for k, v in dictionary.items():   # split json in separate k = val        
            d = json.dumps(v, sort_keys = True, indent = 2) 
            text.append(k+" = " + d + "\n")
        return ('\n').join(text)
    
    with open('sonic_constants.json') as infile:
        const = json.load(infile)
    
    with open('constant_def.py', 'w') as outfile:
        
        outfile.write(dict2var(const))
        
        d = json.dumps(synths, sort_keys = True, indent = 2) 
        outfile.write("synths = " + d)
        outfile.write(helper_func)
        
    '''
    with open('synths.json', 'w') as outfile:
        json.dump(const, outfile, sort_keys = True, indent = 2) )
    '''
if __name__ == '__main__':

    ps = parseSynth()
    dump_dict(ps.synths)
    
    print("DONE")
    '''
    from gen_template import *
    do_jinja(ps.synths)
    '''