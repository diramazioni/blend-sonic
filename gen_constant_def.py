from constant_def import opts_default_val, opts_types_conversion, args_types_conversion

from collections import defaultdict
import re
import json

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
        f_name, argu, arg_def = None, None, None
        if func_with_arg:
            args = {}
            f_name, argu = (func_with_arg.group(1), func_with_arg.group(2))
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
            nextL = ""  # self.lines[self.l+1].strip()
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
                name = catch_val('doc name:') #self.line.strip().split(':')[2][:-1]
                if name[1:] != f_name: 
                    raise Exception("name %s != f_name %s %s %s" % 
                                    (name, f_name, self.line, self.l))
                printDone()
            elif key == 'summary:':
                summary = catch_val(key).strip('\"') #self.line.split('"')[1]
                self.consts[f_name][key[:-1]] = summary
                self.func_doc[f_name][key[:-1]] = summary
                printDone()
            elif key in ['args:', 'alt_args:']:
                def parse_arg(val):
                    arg_dict = {}
                    args_type_iter = re.compile('\[(:\w*), (:\w*)\]')
                    for ar_match in args_type_iter.finditer(val):
                        arg_ref, arg_type = ar_match.group(1), ar_match.group(2)
                        arg_ref = arg_ref[1:]  # remove initial :
                        arg_dict[arg_ref] = arg_type

                        if arg_type not in args_types_conversion:
                            self.warn["new arg %s" % arg_type].append(f_name)
                            self.new_arg[arg_type] = "__to_do__"
                    return arg_dict

                args_d = {}
                line = catch_val(key)
                if line == '[]':
                    print('empty')
                    self.next_line()
                    continue
                elif line.endswith(']]'):
                    line = catch_val2(key)
                    args_d = parse_arg(line)
                elif line.endswith(']]]'):
                    line = line[1:-1]
                    #line = catch_val2(key)
                    args_d = parse_arg(line)
                else:
                    lines = catch_multiline(key)
                    line = '|'.join(lines)
                    args_d.update(parse_arg(line))
                    #for line in lines:

                self.consts[f_name][key[:-1]] = args_d
                printDone()
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
                                print(opt_dict)
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
                    arg, v = l.split('=>')
                    v = v.strip(',').strip()
                    arg = arg.strip()[1:] + ":"  # remove : and add @end
                    arg_def[arg.strip()] = v
                    self.next_line()
                for k, v in arg_def.items():  # fix value reference
                    if v[0] == ":":
                        v = v[1:] + ":"
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
            tmp = parent_synt["arg_defaults"].copy()
            tmp.update(arg_def)
            arg_def = tmp

        synth = {
            "arg_defaults": arg_def,
            "inherit_base": c_parent,
            "inherit_arg": super_merge,
        }
        if len(synth_name):
            synth['name'] = ":"+synth_name
            hiden = False
        else: hiden = True
        if len(synth_descr):    synth['descr'] = synth_descr
        if c_parent not in user_facing:  hiden = True
        synth['hiden'] = hiden
        if 'FX' in c_name:
            self.fx[c_name] = synth
        else:   self.consts[c_name] = synth
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
    with open('sonicpi/synths/synthinfo.rb') as infile:
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
    print("TOT samples", len(ps.samples))
    print("TOT funct_doc", len(ps.func_doc))
    return ps

def parseSound():
    with open('sonicpi/lang/sound.rb') as infile:
        const_file = infile.readlines()
    stop_class_line = '      private'
    ps = ParseConst(const_file)
    defaults_opts = ps.parse_play_opts()
    #dump_dict([{"opts_default_val":defaults_opts }],'lang_def.py', 'w', "" )
    ps.skip_to("def octs(")
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
    ## set hide to false if not set
    for synth_name, val in ps.consts.items():
        if 'hiden' not in val:
            val['hiden'] = False


    print("="*80)
    print("TOT lang_sound", len(ps.consts))
    print("TOT funct_doc", len(ps.func_doc))
    return ps

def parseCore():
    with open('sonicpi/lang/core.rb') as infile:
        const_file = infile.readlines()
    stop_class_line = '      def __on_thread_death'
    ps = ParseConst(const_file)
    ps.skip_to("THREAD_RAND_SEED_MAX")
    ps.next_line(2)
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
    ## set hide to false if not set
    for synth_name, val in ps.consts.items():
        if 'hiden' not in val:
            val['hiden'] = False

    print("="*80)
    print("TOT lang_core", len(ps.consts))
    print("TOT funct_doc", len(ps.func_doc))

    return ps




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
        for k, v in dictionary.items():   # split json in separate k = val        
            d = json.dumps(v, sort_keys = True, ensure_ascii = False, indent = 2)
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

def run():
    pC = parseCore()
    pS = parseSound()
    pSy = parseSynth()
    ## core
    dump_dict([{"lang_core":pC.consts },
               {"core_args_types_conversion": pC.new_arg},
               {"core_opts_types_conversion": pC.new_opt}
               ],'lang_def.py', 'w', "" )
    func_doc = pC.func_doc
    opts_doc = pC.opts_doc
    ## sound
    dump_dict([
        {"lang_sound":pS.consts },
        {"sound_args_types_conversion":pS.new_arg },
        {"sound_opts_types_conversion": pS.new_opt}
    ],'lang_def.py', 'a', "" )
    func_doc.update(pS.func_doc)
    opts_doc.update(pS.opts_doc)
    ## synth
    dump_dict([{"synths":pSy.consts },
               {"synth_nodes": pSy.active},
               {"fx": pSy.fx},
               {"samples": pSy.samples},
               ],'lang_def.py', 'a', gen_helper_func() )
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

    '''
    from gen_template import *
    do_jinja(ps.consts)
    '''



def gen_helper_func():
    return '''


all_lang_ref = list(lang_core.keys()) + list(lang_sound.keys())

def all_synth_names():
    for key, value in synths.items():
        if value['hiden'] != True and key != 'SoundIn' and value['name'] in synth_nodes:
            yield value['name']

all_synth = [ synths[synth_nodes[s]] for s in all_synth_names()]

def all_fx_names():
    for key, value in fx.items():
        if value['hiden'] != True and value['name'] in synth_nodes:
            yield value['name']

all_fx = [ fx[synth_nodes[s]] for s in all_fx_names()]

def all_sample_names():
    all = []
    for key, value in samples.items():
        yield all
        all += value

all_sample = [ s for s in all_sample_names()][0]

def sn(ref):
    c_name = synth_nodes[ref]
    if 'FX' in c_name:
        return fx[c_name]
    else:
        return synths[c_name]

opt_c = {key: value for key, value in lang_core.items()
        if value['hiden'] != True
        if 'opts' in value and value['opts'] is not None
        if len(value['opts']) > 0 }

opt_s = {key: value for key, value in lang_sound.items()
        if value['hiden'] != True
        if 'opts' in value and value['opts'] is not None
        if len(value['opts'].keys()) > 0 }

intro_fn_c = {key: value for key, value in lang_core.items()
          if value['hiden'] is False
          if 'intro_fn' in value and value['intro_fn'] is not False
               }
intro_fn_s = {key: value for key, value in lang_sound.items()
          if value['hiden'] is False
          if 'intro_fn' in value and value['intro_fn'] is not False
               }

accepts_block_c = {key: value for key, value in lang_core.items()
              if value['hiden'] is False
              if 'accepts_block' in value and value['accepts_block'] is not False
              }
accepts_block_s = {key: value for key, value in lang_sound.items()
              if value['hiden'] is False
              if 'accepts_block' in value and value['accepts_block'] is not False
              }
requires_block_c = {key: value for key, value in lang_core.items()
                   if value['hiden'] is False
                   if 'requires_block' in value and value['requires_block'] is not False
                   }
requires_block_s = {key: value for key, value in lang_sound.items()
                   if value['hiden'] is False
                   if 'requires_block' in value and value['requires_block'] is not False
                   }
modifies_env_c = {key: value for key, value in lang_core.items()
                    if value['hiden'] is False
                    if 'modifies_env' in value and value['modifies_env'] is not False
                    }
modifies_env_s = {key: value for key, value in lang_sound.items()
                    if value['hiden'] is False
                    if 'modifies_env' in value and value['modifies_env'] is not False
                    }
memoize_c = {key: value for key, value in lang_core.items()
                  if value['hiden'] is False
                  if 'memoize' in value and value['memoize'] is not False
                  }
memoize_s = {key: value for key, value in lang_sound.items()
                  if value['hiden'] is False
                  if 'memoize' in value and value['memoize'] is not False
                  }
async_block_c = {key: value for key, value in lang_core.items()
                  if value['hiden'] is False
                  if 'async_block' in value and value['async_block'] is not False
                  }
async_block_s = {key: value for key, value in lang_sound.items()
                  if value['hiden'] is False
                  if 'async_block' in value and value['async_block'] is not False
                  }
advances_time_c = {key: value for key, value in lang_core.items()
                  if value['hiden'] is False
                  if 'advances_time' in value and value['advances_time'] is not False
                  }
advances_time_s = {key: value for key, value in lang_sound.items()
                  if value['hiden'] is False
                  if 'advances_time' in value and value['advances_time'] is not False
                  }
returns_c = {key: value for key, value in lang_core.items()
                  if value['hiden'] is False
                  if 'returns' in value and value['returns'] is not False
                  }
returns_s = {key: value for key, value in lang_sound.items()
                  if value['hiden'] is False
                  if 'returns' in value and value['returns'] is not False
                  }
accepts_block_sign_c = {key: value for key, value in lang_core.items()
                   if value['hiden'] is False
                   if 'accepts_block' in value and value['accepts_block'] is not False and '&block' in value['signature']
                   }
accepts_block_sign_s = {key: value for key, value in lang_sound.items()
                   if value['hiden'] is False
                   if 'accepts_block' in value and value['accepts_block'] is not False and '&block' in value['signature']
                   }


if __name__ == '__main__':
    print("synth: ", len(all_synth))
    print("fx: ",len(all_fx))
    print("samples: ",len(all_sample))
    '''

from lang_def import *


def report():
    # sign_args_c = {key: value for key, value in lang_core.items()
    #                    if value['hiden'] is False
    #                     if 'signature' in value if '*args' in value['signature']
    #                    }
    # sign_args_s = {key: value for key, value in lang_sound.items() if value['hiden'] is False if 'signature' in value if '*args' in value['signature']
    #                    }



    print('\nlang_core with opt:')
    print(list(opt_c.keys()))
    print('\nlang_sound with opt:')
    print(list(opt_s.keys()))
    print('\nlang_core with intro_fn:')
    print(list(intro_fn_c.keys()))
    print('\nlang_sound with intro_fn:')
    print(list(intro_fn_s.keys()))

    print('\nlang_core with requires_block:')
    print(list(requires_block_c.keys()))
    print('\nlang_core with accepts_block:')
    print(list(accepts_block_c.keys()))
    print('\nlang_core with accepts_block in sign:')
    print(list(accepts_block_sign_c.keys()))

    print('\n DIFF core accept - req ')
    print(list(set(accepts_block_c.keys()) - set(requires_block_c.keys())))
    print(list(set(accepts_block_c.keys()) - set(accepts_block_sign_c.keys()) ))


    print('\nlang_sound with requires_block:')
    print(list(requires_block_s.keys()))
    print('\nlang_sound with accepts_block:')
    print(list(accepts_block_s.keys()))
    print('\nlang_sound with accepts_block in sign:')
    print(list(accepts_block_sign_s.keys()))

    print('\n DIFF sound accept - req ')
    print(list(set(accepts_block_s.keys()) - set(requires_block_s.keys())))
    print(list(set(accepts_block_s.keys()) - set(accepts_block_sign_s.keys()) ))

    print('\nlang_core with modifies_env:')
    print(list(modifies_env_c.keys()))
    print('\nlang_sound with modifies_env:')
    print(list(modifies_env_s.keys()))
    print('\nlang_core with memoize:')
    print(list(memoize_c.keys()))
    print('\nlang_sound with memoize:')
    print(list(memoize_s.keys()))
    print('\nlang_core with async_block:')
    print(list(async_block_c.keys()))
    print('\nlang_sound with async_block:')
    print(list(async_block_s.keys()))
    print('\nlang_core with advances_time:')
    print(list(advances_time_c.keys()))
    print('\nlang_sound with advances_time:')
    print(list(advances_time_s.keys()))
    print('\nlang_core with returns:')
    print(list(returns_c.keys()))
    print('\nlang_sound with returns:')
    print(list(returns_s.keys()))
    print('\nlang_core & lang_sound:')
    print(all_lang_ref)

    # print('\nlang_core with args in sign:')
    # print(list(sign_args_c.keys()))
    # print('\nlang_sound with args in sign:')
    # print(list(sign_args_s.keys()))


if __name__ == '__main__':
    run()

    report()


