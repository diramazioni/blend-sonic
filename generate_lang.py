import os
sonicpi = os.path.join("sub", "sonic-pi", "app", "server", "ruby", "lib", "sonicpi")
core = os.path.join(sonicpi, "lang", "core.rb")
sounds = os.path.join(sonicpi, "lang", "sound.rb")
synths = os.path.join(sonicpi, "synths", "synthinfo.rb")

from constant_def import *
from category_def import is_to_hide, is_fn

#opts_default_val, opts_types_conversion, args_types_conversion, \
# is_inline, is_buffer_fn, missing_intro_fn, missing_async_block, wrong_accepts_block, is_to_hide

from collections import defaultdict, Counter, OrderedDict
import re
import json

class OrderedCounter(Counter, OrderedDict):
    pass

class ParseConst(object):
    
    '''
    def proc_arg_info(self):

        def generic_slide_doc(k):
            return "Amount of time (in beats) for the {0} value to change. A long {0}_slide value means that the {0} takes a long time to slide from the previous value to the new value. A {0}_slide of 0 means that the {0} instantly changes to the new value.".format(k)
        def generic_slide_curve_doc(k):
            return "Shape of the slide curve (only honoured if slide shape is 5). 0 means linear and positive and negative numbers curve the segment up and down respectively."
        def generic_slide_shape_doc(k):
            return "Shape of curve. 0: step, 1: linear, 3: sine, 4: welch, 5: custom (use *_slide_curve: opt e.g. amp_slide_curve:), 6: squared, 7: cubed. "

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

        self.consts = {}
        self.fx = {}
        self.samples = {}
        self.active = {}
        self.func_doc = {}
        self.opts_doc = {}
        self.new_arg = {}
        self.new_opt = {}


        self.warn = defaultdict(list)
        self._debug = False

    def empty_skip(self):
        while self.line == '\n':
            self.next_line()

    def next_line(self, times=1):
        for i in range(times):
            self.l = self.l + 1
            self.line = self.lines[self.l]
        if self.line.strip().startswith('#'):
            self.next_line()

    def skip_to(self, match):
        while match not in self.line:
            self.next_line()

    def skip_ex(self, match):
        while self.line != match:
            self.next_line()

    def goNext(self, times=1):
        self.next_line(times)
        self.empty_skip()

    def eval_val(self, val):
        try:
            result = int(val)
            return result
        except ValueError:
            try:
                result = float(val)
                return result
            except ValueError:
                result = str(val)
                return result

    def next_has(self, val, stop_line):
        if self.line.startswith(stop_line) or self.line.strip().startswith(val):
            return True
        elif self.line.strip().startswith('#'):
            self.next_line()
        elif len(self.line.strip()):
            # self.next_line()
            return False
        l = self.l+1
        nextL = self.lines[l].strip('\"').strip()
        while not len(nextL):
            l += 1
            nextL = self.lines[l].strip('\"').strip()
        if nextL.startswith(val):
            return True # exit the loop
        else: return False

    def parse_def(self):
        self.empty_skip()
        print()
        print("******* ", (self.line.strip(), self.l))
        end_class = "      end\n"
        func_simple_re = re.compile(r'\s*def (\w*[\?!]?).*')
        func_with_arg_re = re.compile(r'\s*def (\w*[\?!]?)\((.*)\)')
        func_simple = func_simple_re.match(self.line)
        func_with_arg = func_with_arg_re.match(self.line)
        if func_with_arg:
            args = {}
            f_name, argu = (func_with_arg.group(1), func_with_arg.group(2))
            if f_name.endswith(('?', '!')): f_name = f_name[:-1]
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
            self.consts[f_name] = {'signature': args}
        elif func_simple:
            f_name = func_simple.group(1)
            self.skip_ex(end_class)
            self.consts[f_name] = {}
        else:
            raise Exception("bailout not a func", (self.line, self.l))

        self.next_line()
        if not len(self.line.strip()):
            self.empty_skip()
        return f_name

    def parse_doc(self, f_name, stop_line, defaults_opts={}):
        def nextLines():
            start, end = (self.l+1,self.l)
            re_key= re.compile(r'^\s*[\w^:]*:\s*.*')
            re_end_line = re.compile(r'.*\n*\"[\n, ]*\],?\n*$')
            while True:
                end += 1
                nextL = self.lines[end].strip()
                if not len(nextL):
                    continue
                elif nextL.startswith(key): break
                elif nextL.startswith('def '): break
                elif nextL == ']':
                    end += 1
                    break
                elif re.match(re_end_line, nextL):
                    end += 1
                    break
                elif re.match(re_key, nextL):
                    break
                else:
                    continue
            to_eval = self.lines[start: end]
            self.l = end
            self.line = self.lines[end]
            return to_eval

        def catch_multiline2(start_key='examples:'):
            sl = catch_val1(start_key)
            re_sl = re.compile('\[ *\"(.*)\"[\n, ]*\],?\n*$', re.DOTALL)
            sl_m = re.match(re_sl, sl)
            re_split = re.compile('\",(?:\n)? *\"')
            if sl.strip(',') == '[]':
                self.next_line()
                return None
                #elif (sl.endswith('\"]') or sl.endswith('\"     ]') or sl.endswith('"],')):
            elif sl_m:
                jn = re.split(re_split, sl)
                jn = '\n'.join(jn)
                # jn = re.sub('\\\"', "'", jn)
                #jn = jn.replace('\"', "'")
                jn_m = re.match(re_sl, jn)
                jn = jn_m.group(1)
                self.next_line()
                return jn
            else:
                nl = nextLines()
                nl = [n for n in nl if len(n.strip())]


                nl[0] = sl + nl[0]
                if len(nl) > 1:
                    jn = '\n'.join(nl)
                    jn = re.split(re_split, jn)
                    jn = '\n'.join(jn)
                else :
                    jn = '\n'.join(nl)

                jn_m = re.match(re_sl, jn)
                if jn_m:
                    jn = jn_m.group(1)
                else:
                    jn = re.match('\[([^\]]*)\]$', jn, re.DOTALL).group(1)
                return jn

        def catch_multiline(key):
            doc = []
            c = 0
            while True:    # wtf so many special cases
                l = self.line.strip()
                #print(l)
                if c < 1:
                    print(">>>>>", (key, self.line))
                    if 'examples:' in key:
                        val = self.line.split('[')[1].strip('][\"').strip()
                    elif 'args:' in key:
                        val = '['+self.line.split('[')[2].strip().strip(',')
                    elif 'opts:' in key:
                        val = self.line.split('{')[1].strip('{\"').strip()
                    else:
                        print("::::", l)
                        if l.endswith(','):
                            val = catch_val(key).strip('\" ,').strip()
                        else:
                            val = catch_val1(key).strip('\" ').strip()
                    if val: doc.append(val)
                else:
                    print("=====", (key, self.line))
                    if key != 'args:': val = l.strip(',]')
                    else: val = l.strip(',')[:-1]
                    if val: doc.append(val)
                
                nextL = ""#self.lines[self.l+1].strip()                
                c = self.l+1
                while not len(nextL):
                    nextL = self.lines[c].strip()
                    c += 1
                #print('@@@@ ', nextL)
                if not len(l):
                    pass
                if key == 'args:':
                    if l.endswith(']],'):
                        print('[[]] END args')
                        break

                elif key == 'examples:':
                    if nextL == ']':
                        print('[[]] END ex ]')
                        self.l = c+1
                        self.line = self.lines[c+1]
                        break
                        #print('NNN] END:')                    
                    
                    elif (l.endswith('\"]') or l.endswith('\"     ]') or l.endswith('],')):
                        print('[[]] END ex')
                        self.l = c-1
                        self.line = self.lines[c-1]
                        break
                    
                elif l.endswith('},') and 'opts:' in key:
                    print('[[]] END opts')
                    break                    
                elif 'args:' in nextL:
                    break           
                elif l.endswith('",'):
                    if 'opts:' in key:
                        print('&&&&:')                                            
                    elif not nextL.startswith('\"'):
                        print('---- END:')
                        break           
                c += 1
                self.next_line()
            if key in ['opts:', 'args:']:
                return doc
            else:
                return '\n'.join(doc)
        def catch_key():
            return re.match(r'^\s*(?:doc )?([^:]*):\s*.*', self.line).group(1)+':'
        def catch_val(key):
            return re.match(r'\s*'+key+'\s*(.*),.*', self.line).group(1)
        def catch_val1(key):
            return re.match(r'\s*'+key+'\s*(.*)$', self.line).group(1)
            #return self.line.split(':')[1].strip().strip(',')        
        def catch_val2(key):
            return re.match(r'\s*'+key+'\s*\[(.*)\],?.*', self.line).group(1)

        self.func_doc[f_name] = {}
        while not self.next_has('def ', stop_line):
            # if f_name == "define":
            #     print("######## PROBE")
            if not len(self.line.strip()):
                self.empty_skip()
            l = self.line.strip()
            if l.startswith('def ') :
                return True
            elif l.startswith('#'):
                self.next_line()
                continue
            elif l.startswith('private'):
                break
            print(self.l, " ####", l, end="")
            key = catch_key()
            if key == 'doc:':
                doc = catch_multiline('doc:')
                self.func_doc[f_name][key[:-1]] = doc.strip('\"')
                self.next_line()
                printDone()
                continue
            elif key == 'examples:':
                examples = catch_multiline2('examples:')
                if examples:
                    self.func_doc[f_name][key[:-1]] = examples
                #self.next_line()
                printDone()
                continue

            elif key == 'name:':
                name = catch_val('doc name:')
                self.consts[f_name][key[:-1]] = name[1:]
                if name.endswith('!'): self.consts[f_name]['modifies_env'] = True
                printDone()
            elif key == 'summary:':
                summary = catch_val(key).strip('\"')
                self.consts[f_name][key[:-1]] = summary
                self.func_doc[f_name][key[:-1]] = summary
                printDone()
            ###############################
            elif key in ['args:', 'alt_args:']:
                def parse_arg(val):
                    arg_dict = []
                    args_type_iter = re.compile('\[(:\w*), (:\w*)\]')
                    for ar_match in args_type_iter.finditer(val):
                        arg_ref, arg_type = ar_match.group(1), ar_match.group(2)
                        arg_ref = arg_ref[1:]  # remove initial :
                        arg_dict.append({arg_ref: arg_type})

                        if arg_type not in args_types_conversion:
                            self.warn["new arg %s" % arg_type].append(f_name)
                            self.new_arg[arg_type] = "__to_do__"
                    return arg_dict

                line = catch_val(key)
                if line == '[]':
                    print('empty')
                    self.next_line()
                    continue
                elif line.endswith(']]'):
                    line = catch_val2(key)
                elif line.endswith(']]]'):
                    line = line[1:-1]
                    #line = catch_val2(key)
                else:
                    lines = catch_multiline(key)
                    line = '|'.join(lines)
                    #for line in lines:
                args_d = parse_arg(line)

                self.consts[f_name][key[:-1]] = args_d
                printDone()
            ###############################
            elif key == 'opts:':
                opt_dict = catch_val(key) 
                if "nil" in opt_dict:
                    opt_dict = None
                elif 'DEFAULT_PLAY_OPTS' in opt_dict:
                    opt_dict = defaults_opts
                    #if arg_type not in self.args_types: 
                elif '{}' in opt_dict:
                    opt_dict = {}
                else:
                    opt_dict = {}
                    opt_lines = catch_multiline(key)
                    for o in opt_lines:
                        if o == '}': break
                        opt_with_arg_re = re.compile(r':?(\w*):? *(?:=>)? *\"(.*)\"}?')
                        opt_arg = opt_with_arg_re.match(o)
                        if opt_arg:                
                            opt, doc =  opt_arg.group(1), opt_arg.group(2)                
                            self.opts_doc[opt] = doc
                            if opt in opts_default_val:
                                opt_dict[opt] = opts_default_val[opt]
                                # print(opt_dict)
                            else:
                                self.warn["no default value for opt %s" % opt].append(f_name)
                                self.new_opt[opt] = "__to_do__"
                        else:
                            raise Exception("no opt match in", (opt_dict, self.l))
                if opt_dict is not None:
                    self.consts[f_name][key[:-1]] = opt_dict
                printDone()
            elif key == 'introduced:':
                val = catch_val(key)                
                val = val.split('new')[1].strip("()")                
                self.consts[f_name][key[:-1]] = val
            elif key in ['accepts_block:', 'requires_block:', 'modifies_env:', 'memoize:', 'intro_fn:', 'async_block:', 'advances_time:']:
                val = catch_val(key)
                val = True if val == "true" else False
                self.consts[f_name][key[:-1]] = val
                printDone()
            elif key == 'hide:':
                val = catch_val1(key)
                val = True if val == "true" else False
                self.consts[f_name]['hiden'] = val
                printDone()
            elif key == 'returns:':
                val = catch_val(key)
                if "nil" in val:
                    val = None
                if val and val not in args_types_conversion:
                    self.warn["new returns %s" % val].append(f_name)
                    self.new_arg[val] = "__to_do__"                    

                self.consts[f_name][key[:-1]] = val
                #self.warn["return types %s"% val].append(f_name)
                printDone()
            #['amp:', 'hpf:', 'hpf_bypass:', 'kill_delay:', 'leak_dc_bypass:','limiter_bypass:', 'lpf:','lpf_bypass:', 'num_octaves:']
            #elif key in ['kill_delay:'] : # handle special cases
                
                
            else:
                self.warn["no_catch %s"% key].append(f_name)
                print("\n[ERROR]", (f_name, self.line))
                return False # bailout gracefully ! WATCH OUT  !
            #print("[**] END")
            self.next_line()
        if not len(self.line.strip()):
            self.empty_skip()
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


    def parse_class(self, stop_line):


        print("> ", (self.line, self.l))

        class_match = re.match(r'.* class (.*) < (.*)$', self.line)
        try:
            m = class_match.group(1)
        except AttributeError:
            print("bailout not a class", (self.line, self.l))
            return False
        c_name, c_parent = (class_match.group(1), class_match.group(2))
        self.next_line()


        synth_name = ""
        synth_descr = ""
        arg_def = {}

        super_merge = None
        while self.line != stop_line:
            s = self.line
            if "def name" in s:
                self.next_line()
                synth_descr = self.line.strip().strip('"')
                self.goNext(2)
            elif "def synth_name" in s:
                self.next_line()
                synth_name = self.line.strip().strip('"')
                self.goNext(2)
            elif "def arg_defaults" in s:
                self.next_line()
                if self.line.strip() == '{':
                    super_merge = False
                    self.next_line()
                elif self.line.strip() == 'super.merge({':
                    super_merge = True
                    self.next_line()
                elif '{' in self.line and len(self.line.strip()) > 1 :
                    super_merge = False

                while "}" not in self.line:
                    l = self.line.strip().strip('{')
                    if not l:
                        self.next_line()
                        continue
                    arg = ""
                    v = ""
                    if('=>' in l):
                        arg, v = l.split('=>')
                        v = v.strip(',').strip()
                        arg = arg.strip()[1:]
                    elif ":" in l: # found also this variant prop: val in un case
                        arg, v = l.split(':')
                        v = v.strip(',').strip()
                    else:
                        raise Exception("bailout arg_defaults not found", (self.line, self.l))

                    if len(arg) > 0 and len(v) > 0:
                        arg_def[arg.strip()] = v
                    self.next_line()
                for k, v in arg_def.items():  # fix value reference
                    if v[0] == ":":
                        v = v[1:]
                        ref = arg_def[v]
                        arg_def[k] = self.eval_val(ref)
                    else:
                        arg_def[k] = self.eval_val(v)
                self.empty_skip()
            else:
                self.next_line()

        baseClass = ["FXInfo", "SonicPiSynth", "Pitchless",
                     "BaseInfo", "StudioInfo", "BaseMixer"]
        user_facing = baseClass[:3]

        def inherit_super(parent, arg_def):
            # start_arg = arg_def
            while True:
                if 'FX' in parent:
                    parent_synt = self.fx[parent]
                else:
                    parent_synt = self.consts[parent]
                tmp = parent_synt["arg_defaults"]
                tmp.update(arg_def)
                arg_def = tmp
                parent = parent_synt['inherit_base']
                if not parent or parent in baseClass[1:]:
                    break
                elif parent_synt['inherit_arg']:
                    continue
                else:
                    break
            return arg_def

            # parent_synt_name = self.tmp_dict[parent]  # take the ref by class

        if c_name == 'FXInfo':
            print('d')
        if super_merge is None: super_merge = True
        if super_merge and c_parent not in baseClass[1:]:
            # arg_def = inherit_super(super_c, arg_def)
            if 'FX' in c_parent:
                parent_synt = self.fx[c_parent]
            else:
                parent_synt = self.consts[c_parent]
            tmp = parent_synt["opts"].copy()
            tmp.update(arg_def)
            arg_def = tmp

        synth = {
            "opts": arg_def,
            "inherit_base": c_parent,
            "inherit_arg": super_merge,
        }
        if len(synth_name):
            if 'FX' in c_name:
                synth_name = synth_name.split('fx_')[1]
            synth['name'] = ":"+synth_name
            hiden = False
        else: hiden = True
        if len(synth_descr):    synth['summary'] = synth_descr
        if c_parent not in user_facing:  hiden = True
        synth['hiden'] = hiden
        if 'FX' in c_name:
            self.fx[c_name] = synth
        else:   self.consts[c_name] = synth

        for opt in arg_def:
            if not opt in opts_types_conversion:
                self.warn["new opt %s" % opt].append(c_name)
                self.new_opt[opt] = "Float"
        self.goNext()

        return True

    def parse_samples(self):
        self.skip_to('@@grouped_samples')
        self.next_line()
        category = ''
        while not '@@all_samples' in self.line:
            l = self.line.strip()
            if l == '{' or l == '}' or not len(l):
                pass
            elif 'desc' in l:
                category = l.split(' => ')[1].strip().strip(',"')
                self.samples[category] = []
            elif 'samples' in l:
                self.next_line()
                while True:
                    l = self.line.strip()
                    s = l.strip(',]}')
                    self.samples[category].append(s)

                    self.next_line()
                    if ']}' in l: break
            self.next_line()


        self.skip_to('@@synth_infos')
        self.next_line(2)
        while not '}' in self.line:
            l = self.line.strip()
            if not len(l) or l.startswith('#'):
                pass
            else:
                synth_name, c_name = l.split(' => ')
                c_name = c_name.split('.')[0]
                self.active[synth_name] = c_name
            self.next_line()



####################### class end


def parseSynth():
    with open(synths) as infile:
        const_file = infile.readlines()

    '''
    ps.skip_to("class BaseInfo")
    ps.skip_to("def default_arg_info")    
    arg_base = ps.proc_arg_info()
    print(arg_base)
    ps.consts['__BaseInfo__'] = {'arg_info':arg_base}
    '''

    stop_class_line = 'class BaseInfo'
    end_class = "    end\n"
    ps = ParseConst(const_file)
    ps.skip_to("class SynthInfo < BaseInfo")
    while(stop_class_line not in ps.line):
        #ps.empty_skip()
        op = ps.parse_class(end_class)
        if not op:
            print("ops went WRONG")
            break
    ps.parse_samples()
    ########
    ## hide not active synth
    for synth_name, val in ps.consts.items():
        if synth_name not in ps.active.values():
            if not val['hiden']:
                val['hiden'] = True
                ps.warn["hiding synth" ].append(synth_name)
    for synth_name, val in ps.fx.items():
        if synth_name not in ps.active.values():
            if not val['hiden']:
                val['hiden'] = True
                ps.warn["hiding fx" ].append(synth_name)


    print("="*80)
    print("TOT synths", len(ps.consts))
    print("TOT fx", len(ps.fx))
    print("TOT samples", sum(len(sam) for sam in ps.samples))
    print("TOT funct_doc", len(ps.func_doc))
    print("new opt ", ps.new_opt)
    return ps

def parseSound():
    with open(sounds) as infile:
        const_file = infile.readlines()
    stop_class_line = '      private'
    ps = ParseConst(const_file)
    defaults_opts = ps.parse_play_opts()
    #dump_dict([{"opts_default_val":defaults_opts }],'lang_def.py', 'w', "" )
    ps.skip_to("def use_timing_guarantees(v, &block)")
    f_name = ""
    while not ps.line.startswith(stop_class_line):
        if ps.line.startswith(stop_class_line): break
        elif ps.line.startswith('      def'):
            f_name = ps.parse_def()
            #print(ps.line)
        else:
            op = ps.parse_doc(f_name, stop_class_line, defaults_opts)
            if not op:
                print("ops went WRONG")
                break

    ########


    print("="*80)
    print("TOT lang_sound", len(ps.consts))
    print("TOT funct_doc", len(ps.func_doc))
    return ps

def parseCore():
    with open(core) as infile:
        const_file = infile.readlines()
    stop_class_line = '      def __on_thread_death'
    ps = ParseConst(const_file)
    ps.skip_to("def set(k, val)")
    #ps.next_line(2)
    f_name = ""
    while not ps.line.startswith(stop_class_line):
        if ps.line.startswith(stop_class_line): break
        elif ps.line.startswith('      def'):
            f_name = ps.parse_def()
        else:
            op = ps.parse_doc(f_name, stop_class_line)
            if not op:
                print("ops went WRONG")
                break

    ########


    print("="*80)
    print("TOT lang_core", len(ps.consts))
    print("TOT funct_doc", len(ps.func_doc))

    return ps


def find_optional_args(consts):
    print('+'*30)
    print('find_optional_args')
    for fn, v in consts.items():
        if not 'alt_args' in v or not 'args' in v: continue
        print('\n'+fn)

        args = min(v['args'], v['alt_args'], key=len)
        alt_args = max(v['args'], v['alt_args'], key=len)
        print('args ', args)
        print('alt_args ', alt_args)
        v['args'] = args
        v['alt_args'] = alt_args

def printDone():
    print(' ==> OK')

def printWarning(ps):
    # for k in ps.consts.keys():
    # if k not in ps.funct_doc: print("no DOC", k)
    if len(ps.warn):
        print("---WARN---" * 16)
        for k, v in sorted(ps.warn.items()):
            print(k, v)


def dump_dict(dict_def, out_file_name, out_mode, helper_func):

    def dict2var(dictionary):
        text = []
        for k, v in dictionary.items():   #  sort_keys = True,
            d = json.dumps(v, ensure_ascii = False, indent = 2)
            text.append(k+" = " + d + "\n\n")
            print("writing %s in %s" % (k,out_file_name))
        return ('\n').join(text)
    
    with open(out_file_name, out_mode) as outfile:
        
        if out_mode == "w":
            outfile.write('null = None; true = True; false = False;\n')
        outfile.write("#\#/"*10+'\n\n')
        for const in dict_def:
            outfile.write(dict2var(const))
        outfile.write(helper_func)

    '''
    with open('synths.json', 'w') as outfile:
        json.dump(const, outfile, sort_keys = True, indent = 2) )
    '''

def parse():
    pC = parseCore()
    pS = parseSound()
    pSy = parseSynth()

    find_optional_args(pC.consts)
    addMetaData(pC.consts)
    addMetaData(pS.consts)

    ## core
    dump_dict([{"lang_core":pC.consts },
               ],'lang_def.py', 'w', "" )
    # {"core_args_types_conversion": pC.new_arg},
    # {"core_opts_types_conversion": pC.new_opt}
    func_doc = pC.func_doc
    opts_doc = pC.opts_doc
    ## sound
    dump_dict([
        {"lang_sound":pS.consts },
        {"sound_args_types_conversion": pS.new_arg },
        {"sound_opts_types_conversion": pS.new_opt}
    ],'lang_def.py', 'a', "" )
    func_doc.update(pS.func_doc)
    opts_doc.update(pS.opts_doc)
    ## synth
    dump_dict([{"synths":pSy.consts },
               {"synth_nodes": pSy.active},
               {"fx": pSy.fx},
               {"samples": pSy.samples},
               {"synth_args_types_conversion": pSy.new_arg},
               {"synth_opts_types_conversion": pSy.new_opt}
               ],'lang_def.py', 'a', "" )
    synth_doc = pSy.func_doc
    synth_opts_doc = pSy.opts_doc
    ## doc
    dump_dict([
        {"funct_doc": func_doc},
        {"opts_doc": opts_doc},
        {"synth_doc": synth_doc},
        {"synth_opts_doc": synth_opts_doc}
    ],'lang_doc.py', 'w', "" )

    printWarning(pC)
    printWarning(pS)
    printWarning(pSy)

    print("DONE")
    print(pS.new_opt)
    '''
    from gen_template import *
    do_jinja(ps.consts)
    '''


def addMetaData(consts):
    print('+'*30)
    print('add / fix metaData')
    ###################################
    ## these func can be sync based on the examples
    missing_intro_fn = ['current_random_seed', 'synth']
    ## these func can be async based on the examples
    missing_async_block = ['density', 'with_fx', 'sample', 'synth', 'play']
    ## these func has wrong accepts_block (based on the examples)
    wrong_block = {
        'play': {"accepts_block": True, "requires_block": False},
        'sample': {"accepts_block": True, "requires_block": False},
        'synth': {"accepts_block": True, "requires_block": False},
        'on': {"accepts_block": True, "requires_block": True},
        'time_shift': {"accepts_block": True, "requires_block": True},
        'density': {"accepts_block": True, "requires_block": True},
        'with_octave': {"accepts_block": True, "requires_block": True},
        'with_timing_guarantees': {"accepts_block": True, "requires_block": True},
        'with_tuning': {"accepts_block": True, "requires_block": True},
        'with_merged_sample_defaults': {"accepts_block": True, "requires_block": True},
        'with_sample_defaults': {"accepts_block": True, "requires_block": True},
        'use_timing_guarantees': {"accepts_block": False, "requires_block": False},
    }
    #{'tick': 0}, {'shuffle': 0}, {'choose': 0}, {'stretch': 0}, {'stretch': 1}
    arg_fixes = {
                'live_loop': {
                    "args": [],
                    "alt_args": [{"name": ":symbol"}
                                 ]},
                'pick': {
                    "args": [{"n": ":number_or_nil" }],
                    "alt_args":[{"list": ":array" }
                                ]},
                'tick': {
                    "args": [],
                    "alt_args": [{"list": ":array"},
                                 { "key": ":symbol"},
                                 { "value": ":number"}
                                 ]},
                'look': {
                    "alt_args": [{"list": ":array"},
                                 { "key": ":symbol"}
                                 ]},
                'shuffle': {
                    "args": [],
                    "alt_args": [{"list": ":array"}
                                 ]},
                'choose': {
                    "args": [],
                    "alt_args": [{"list": ":array"}
                                 ]},
                'stretch': {
                    "args": [{"count": ":int"}],
                    "alt_args": [{"list": ":array"}
                                 ]},
                'assert': { # override
                    "args": [{"is_true": ":boolean"}],
                    "alt_args": []},
                'stop': { # override
                    "args": [{"signal": ":boolean"}],
                    "alt_args": []},
                'note': { # override
                    "args": [],
                    "alt_args": [{ "note": ":symbol"},],
                    "opts": {}},
                'chord': { # override
                    "args": [],
                    "alt_args": [{"tonic": ":symbol" },
                             {"chord": ":symbol"}]},
                'scale': {  # override
                    "args": [],
                    "alt_args": [{"tonic": ":symbol"},
                                 {"scale": ":symbol"}]},
                'degree': {  # override
                    "args": [],
                    "alt_args": [{"degree": ":symbol"},
                                 {"tonic": ":symbol"},
                                 {"scale": ":symbol"}]},
                'chord_degree': {  # override
                    "args": [{"number_of_notes": ":int"}],
                    "alt_args": [{"degree": ":symbol"},
                                 {"tonic": ":symbol"},
                                 {"scale": ":symbol"}]},
                'sample': {  # override
                    "args": [],
                    "alt_args": [{"name_or_path": ":symbol_or_string"}]},
                'use_sample_bpm': {  # override
                    "args": [],
                    "alt_args": [{"string_or_number": ":sample_name_or_duration"}]},
                # 'sleep': {  # override
                #     "args": [],
                #     "alt_args": [{"beats": ":number"}]},
                'with_fx': {  # override
                    "args": [],
                    "alt_args": [{"fx_name": ":symbol"}]},
    }
    new_functions = {
        "note_list": {
            "accepts_block": False,
            "summary": "Make a list of notes",
            "opts": {},
            "signature": {},
            "hiden": False,
            "args": [],
            "name": "note_list",
            "introduced": "blend-sonic"
        },
        "time_now": {
            "accepts_block": False,
            "summary": "return a number based on current time",
            "opts": {},
            "signature": {},
            "hiden": False,
            "args": [],
            "name": "time_now",
            "introduced": "blend-sonic"
        },
    }
    consts.update(new_functions)

    if 'use_sample_defaults' in consts: consts['use_sample_defaults']['opts'] = consts['sample']['opts']
    #for fn, val in new_functions.items():

    # using the list in category_def
    for fn, val in consts.items():
        if 'hiden' not in val and fn not in is_to_hide:
            val['hiden'] = False
        elif fn in is_to_hide:
            val['hiden'] = True
        if fn in missing_async_block:
            val['async_block'] = True
        if fn in missing_intro_fn:
            val['intro_fn'] = True
        if fn in is_fn:
            val['inline'] = True
        if fn in wrong_block.keys():
            for k, v in wrong_block[fn].items():
                val[k] = v
        if fn in arg_fixes.keys():
            # val.update(remove_mandatory_arg[fn])
            for k, v in arg_fixes[fn].items():
                val[k] = v


def gen_helper_func():
    return '''

    '''

# from lang_def import *






if __name__ == '__main__':
    parse()


