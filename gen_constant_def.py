from constant_def import opts_default_val, opts_types_conversion, args_types_conversion

from collections import defaultdict
import re

import sys
#import inspect

'''
def generic_slide_doc(k):
    return "Amount of time (in beats) for the {0} value to change. A long {0}_slide value means that the {0} takes a long time to slide from the previous value to the new value. A {0}_slide of 0 means that the {0} instantly changes to the new value.".format(k)
def generic_slide_curve_doc(k):
    return "Shape of the slide curve (only honoured if slide shape is 5). 0 means linear and positive and negative numbers curve the segment up and down respectively."
def generic_slide_shape_doc(k):
    return "Shape of curve. 0: step, 1: linear, 3: sine, 4: welch, 5: custom (use *_slide_curve: opt e.g. amp_slide_curve:), 6: squared, 7: cubed. "
'''
class ParseConst(object):
    
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
    #line = ""
    def __init__(self, lines):
        self.lines = lines # all lines
        self.l = 0  # cursor of current line
        self.line = lines[self.l]
        #self.line = "" # current line
        
        
        self.tmp_dict = {}
        self.consts = {}            
        self.funct_doc = {}
        self.opts_doc = {}
        self.new_arg = {}
        self.new_opt = {}
        
        
        
        self.warn = defaultdict(list)
        self._debug = False
                
    def proc_class(self):
        print("> ", (self.line, self.l))
        
        class_match = re.match( r'.* class (.*) < (.*)\n', self.line)
        try:            
            m = class_match.group(1)
        except AttributeError:
            print("bailout not a class", (self.line, self.l))
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
        self.tmp_dict[c_name] = synth_name
        
        baseClass = ["SonicPiSynth","Pitchless", "FXInfo", 
                     "BaseInfo", "StudioInfo",  "BaseMixer"]
        user_facing = baseClass[:3] 
        # no "BaseInfo", "StudioInfo", "BaseMixer",

        hiden = 0
        def inherit_super(parent):
            parent_synt_name = self.tmp_dict[parent] # take the ref by class
            parent_synt = self.consts[parent_synt_name]            
            if parent_synt:
                arg_def.update(parent_synt["arg_defaults"])
                return parent_synt['inherit_base']
        
        super_c = c_parent        
        while super_c not in baseClass:
            super_c = inherit_super(super_c)
        if super_c not in user_facing:
            print("/ ", super_c)
            hiden = 1

        self.consts[synth_name] = {
            "descr": synth_descr, 
            "arg_defaults": arg_def,
            "class_name": c_name,
            "inherit_base": c_parent,
            "hiden": hiden,
        }
        self.goNext()
        
        return True

    def eval_val(self, val):
        if val.isdigit():
            return eval(val)
        else:
            return str(val)
        
    def next_has(self, val):
        l = self.l+1
        nextL = self.lines[l].strip('\"').strip()
        while not len(nextL):
            l += 1
            nextL = self.lines[l].strip('\"').strip()
        if nextL.startswith(val):   return True
        else: return False
        
    def parse_lang(self, defaults_opts, do_doc):
        def catch_multiline(first_line):                
            doc = []
            c = 0
            while True:    # wtf so many special cases
                l = self.line.strip()
                #print(l)
                if c < 1:
                    print(">>>>>", (first_line, self.line))
                    if 'examples:' in first_line:
                        val = self.line.split('[')[1].strip('][\"').strip()
                    elif 'opts:' in first_line:
                        val = self.line.split('{')[1].strip('{\"').strip()
                    else:
                        print("::::", l)
                        if l.endswith(','):
                            val = catch_val(first_line).strip('\" ,').strip()
                        else:
                            val = catch_val1(first_line).strip('\"').strip()
                    if val: doc.append(val)
                else:
                    print("=====", (first_line, self.line))
                    val = l.strip(',]')
                    if val: doc.append(val)
                
                nextL = ""#self.lines[self.l+1].strip()                
                c = self.l+1
                while not len(nextL):
                    nextL = self.lines[c].strip('"').strip()
                    c += 1
                #print('@@@@ ', nextL)
                if not len(l):
                    pass
                
                elif 'examples:' in first_line:
                    if 'def ' in nextL:
                        print('[[]] examples END found def:')
                        break
                    
                    elif nextL == ']':
                        pass
                        #print('NNN] END:')                    
                    
                    elif (l.endswith('\"]') or l.endswith('],') ):
                        print('[[]] examples END:')
                        break
                    
                elif l.endswith('},') and 'opts:' in first_line:
                    print('[[]] opts END:')
                    break                    
                elif 'args:' in nextL:
                    break           
                elif l.endswith('",'):
                    if 'opts:' in first_line: 
                        print('&&&&:')                                            
                    elif not nextL.startswith('\"'):
                        print('---- END:')
                        break           
                c += 1    
                self.next_line()
            if 'opts:' in first_line:
                return doc
            else:
                return '\n'.join(doc)
        def catch_key():
            return re.match(r'^\s*(?:doc )?([^:]*):\s*.*', self.line).group(1)+':'
        def catch_val(key):
            return re.match(r'\s*'+key+'\s*(.*),.*', self.line).group(1) 
        def catch_val1(key):
            return re.match(r'\s*'+key+'\s*(.*).*', self.line).group(1) 
            #return self.line.split(':')[1].strip().strip(',')        
        def catch_val2(key):
            return re.match(r'\s*'+key+'\s*\[(.*)\],?.*', self.line).group(1) 
        self.empty_skip()
        print()
        print("******* ", (self.line.strip(), self.l))
        end_class = "      end\n"
        func_simple_re =   re.compile(r'\s*def (\w*[\?!]?).*')
        func_with_arg_re = re.compile(r'\s*def (\w*[\?!]?)\((.*)\)')
        func_simple = func_simple_re.match(self.line)
        func_with_arg = func_with_arg_re.match(self.line)
        f_name, argu, arg_def = None, None, None
        if func_with_arg:
            args = {}
            f_name , argu = (func_with_arg.group(1), func_with_arg.group(2))
            argu_l = argu.split(', ')
            for arg in argu_l:                
                if '=' in arg:  
                    arg_name, arg_val = arg.split('=')
                    arg_name, arg_val = arg_name.strip(), arg_val.strip() 
                    args[arg_name] = self.eval_val(arg_val.strip())
                else:
                    arg_name = arg.strip()
                    args[arg_name] = None
                    
            self.skip_ex(end_class)
            self.consts[f_name] = {'args_in': args}
        elif func_simple:
            f_name = func_simple.group(1)
            self.skip_ex(end_class)
            self.consts[f_name] = {}
        else:
            raise Exception("bailout not a func", (self.line, self.l))

        self.next_line()
        if not len(self.line.strip()):
            self.empty_skip()
        if not self.line.strip().startswith('doc name:'):
            if self.line.strip().startswith('def'):
                #self.warn["no_doc"].append(f_name)       
                return True
            else:
                self.warn["unexpected end of def"].append(f_name)            
                return False
       
        self.funct_doc[f_name] = {}       
        while not self.next_has('def '): #not func_simple_re.match(self.line): 
            
            if not len(self.line.strip()):
                self.empty_skip()
            l = self.line.strip()
            if l.startswith('private'):
                break
            if l.startswith('#'): 
                self.next_line()
                return True
            print("####", l)
            key = catch_key()
            if key == 'doc:':
                doc = catch_multiline('doc:')
                self.funct_doc[f_name][key[:-1]] = doc
                self.next_line() ; continue
            elif key == 'examples:':
                examples = catch_multiline('examples:')            
                self.funct_doc[f_name][key[:-1]] = examples
                self.next_line() ; continue
            
            if key == 'name:':
                name = catch_val('doc name:') #self.line.strip().split(':')[2][:-1]
                if name[1:] != f_name: 
                    raise Exception("name %s != f_name %s %s %s" % 
                                    (name, f_name, self.line, self.l))
            elif key == 'summary:':
                summary = catch_val(key).strip('\"') #self.line.split('"')[1]
                self.consts[f_name][key[:-1]] = summary
                self.funct_doc[f_name][key[:-1]] = summary
            elif key == 'args:':
                args_type_line_re = catch_val2(key)
                args_type_iter = re.compile('\[(:\w*), (:\w*)\]') 
                arg_dict = {}
                for ar_match in args_type_iter.finditer(args_type_line_re):                
                    arg_ref, arg_type = ar_match.group(1), ar_match.group(2)
                    arg_ref = arg_ref[1:] # remove initial :                                
                    arg_dict[arg_ref] = arg_type
                    
                    if arg_type not in args_types_conversion:
                        self.warn["new arg %s" % arg_type].append(f_name)
                        self.new_arg[arg_type] = "__to_do__"
    
                self.consts[f_name]['args_types'] = arg_dict                
            elif key == 'opts:':
                opts = []
                opt_line = catch_val(key) 
                if "nil" in opt_line:
                    opt_line = None
                elif 'DEFAULT_PLAY_OPTS' in opt_line:
                    opt_line = defaults_opts
                    #if arg_type not in self.args_types: 
                elif '{}' in opt_line:
                    opt_line = {}
                else:
                    opt_line = ""
                    opt_lines = catch_multiline('opts:')
                    for opt_line in opt_lines:                        
                        opt_with_arg_re = re.compile(r':?(\w*):? *(?:=>)? *\"(.*)\"}?')
                        opt_arg = opt_with_arg_re.match(opt_line)                
                        if opt_arg:                
                            opt, doc =  opt_arg.group(1), opt_arg.group(2)                
                            self.opts_doc[opt] = doc
                            if opt in opts_default_val:
                                opt_line = {opt: opts_default_val[opt]}
                                self.consts[f_name][key[:-1]] = opt_line
                            else:
                                self.warn["no default value for opt %s" % opt].append(f_name)
                                self.new_opt[opt] = "__to_do__"

                        else:
                            print("no opt match in", opt_line)
                            return False
                        
                self.consts[f_name][key[:-1]] = opt_line
            elif key == 'introduced:':
                val = catch_val(key)                
                val = val.split('new')[1].strip("()")                
                self.consts[f_name][key[:-1]] = val
            elif key in ['accepts_block:', 'requires_block:', 'modifies_env:', 'memoize:', 'intro_fn:']:
                val = catch_val(key)
                val = True if val == "true" else False
                self.consts[f_name][key[:-1]] = val 
            elif key == 'returns:':
                val = catch_val(key)
                if "nil" in val:
                    val = None
                if val and val not in args_types_conversion:
                    self.warn["new returns %s" % val].append(f_name)
                    self.new_arg[val] = "__to_do__"                    
                    
                self.consts[f_name][key[:-1]] = val
                #self.warn["return types %s"% val].append(f_name)
            #['amp:', 'hpf:', 'hpf_bypass:', 'kill_delay:', 'leak_dc_bypass:','limiter_bypass:', 'lpf:','lpf_bypass:', 'num_octaves:']
            #elif key in ['kill_delay:'] : # handle special cases
                
                
            else:
                self.warn["no_catch %s"% key].append(f_name)
            self.next_line()

        mandatory_keys = ["args_types", "opts", "summary", "accepts_block", "introduced"] #"args_in",
        for key in mandatory_keys:
            if key not in self.consts[f_name]:
                self.warn["no_mandatory_keys %s"% key].append(f_name)

        return True
        
        
    def parse_play_opts(self):
        arg_def = {}
        self.skip_to("DEFAULT_PLAY_OPTS")
        self.next_line()
        while len(self.line.strip()) >0:
            opt = self.line.split(":")[0].strip()
            if opt:
                arg_def[opt] = 1
            doc = self.line.split('"')[1]
            self.opts_doc[opt] = doc            
            self.next_line()
        # Guess the defaults zero arg.... if someone knows tell me
        for opt in ["pan", "slide", "pitch", "attack", "decay", "release"]:
            arg_def[opt] = 0       
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
        while match not in self.line:
            self.next_line()
            
    def skip_ex(self, match):        
        while self.line != match:
            self.next_line()
              
    def goNext(self):
        self.next_line()
        self.empty_skip()

       
    
def parseSynth():
    with open('sonicpi/synths/synthinfo.rb') as infile:
        const_file = infile.readlines()
    ps = ParseConst(const_file)
    '''
    ps.skip_to("class BaseInfo")
    ps.skip_to("def default_arg_info")    
    arg_base = ps.proc_arg_info()
    print(arg_base)
    ps.consts['__BaseInfo__'] = {'arg_info':arg_base}
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

def parseSound():
    with open('sonicpi/lang/sound.rb') as infile:
        const_file = infile.readlines()
    ps = ParseConst(const_file)
    defaults_opts = ps.parse_play_opts()
    #dump_dict([{"opts_default_val":defaults_opts }],'lang_def.py', 'w', "" )
    ps.skip_to("def octs(")
    stop_class_line = '      private'
    while not ps.line.startswith(stop_class_line):
        if ps.line.startswith('      def'):
            #print(ps.line)
            op = ps.parse_lang(defaults_opts, True)
            if not op:
                print("ops")
                break                
        if ps.line.startswith(stop_class_line): break
        else:        ps.goNext()
    
    func_off = ["use_fx", "use_timing_warnings"]
    ##########################################
    print("="*80)
    print("TOT lang_sound", len(ps.consts))
    print("TOT funct_doc", len(ps.funct_doc))
    return ps
    '''
    ps.consts['#play'] = {"arg_defaults":arg_defaults, "descr": "play notes", "hiden": 1, "class_name": "Play"}
    '''
    return ps

def gen_helper_func():
    return '''
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

def dump_dict(dict_def, out_file_name, out_mode, helper_func):
    import json

    def dict2var(dictionary):
        text = []
        for k, v in dictionary.items():   # split json in separate k = val        
            d = json.dumps(v, sort_keys = True, indent = 2) 
            text.append(k+" = " + d + "\n")
        return ('\n').join(text)
    
    with open(out_file_name, out_mode) as outfile:
        
        if out_mode == "w":
            outfile.write('null = None; true = True; false = False;\n')
        outfile.write("#\#/"*10+'\n\n')
        for const in dict_def:
            outfile.write(dict2var(const))
        outfile.write(helper_func)
    print("wrote", out_file_name) 
    '''
    with open('synths.json', 'w') as outfile:
        json.dump(const, outfile, sort_keys = True, indent = 2) )
    '''
if __name__ == '__main__':

    #ps = parseSynth()
    #dump_dict(ps.consts, 'lang_def.py', "synths", gen_helper_func() )
    
    ps = parseSound()
    dump_dict([{"lang_sound":ps.consts }],'lang_def.py', 'w', "" )
    if len(ps.new_arg):
        dump_dict([{"new_args_types_conversion":ps.new_arg }],'lang_def.py', 'a', "" )
    if len(ps.new_opt):
        dump_dict([{"new_opts_types_conversion":ps.new_opt }],'lang_def.py', 'a', "" )
    #ps = parseSynth()
    #dump_dict([{"synths":ps.consts }],'lang_def.py', 'a', "" )
    dump_dict([{"funct_doc":ps.funct_doc }],'lang_doc.py', 'w', "" )
    
    dump_dict([{"opts_doc":ps.opts_doc }],'lang_doc.py', 'a', "" )
    
    #for k in ps.consts.keys():
        #if k not in ps.funct_doc: print("no DOC", k)
    
    #opts_default_val = {k:"" for k in ps.opts_doc.keys()}
    if len(ps.warn):
        print("---WARN---"*16)
        for k,v in sorted(ps.warn.items()):            
            print(k,v)
        
    
    
    print("DONE")
    '''
    from gen_template import *
    do_jinja(ps.consts)
    '''