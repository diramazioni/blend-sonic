from transitions import Machine
import re

import inspect


def generic_slide_doc(k):
    return "Amount of time (in beats) for the {0} value to change. A long {0}_slide value means that the {0} takes a long time to slide from the previous value to the new value. A {0}_slide of 0 means that the {0} instantly changes to the new value.".format(k)
def generic_slide_curve_doc(k):
    return "Shape of the slide curve (only honoured if slide shape is 5). 0 means linear and positive and negative numbers curve the segment up and down respectively."
def generic_slide_shape_doc(k):
    return "Shape of curve. 0: step, 1: linear, 3: sine, 4: welch, 5: custom (use *_slide_curve: opt e.g. amp_slide_curve:), 6: squared, 7: cubed. "

class ParseSynth(object):
    
    states = ['start', 'skip', 'proc_arg_info', 'each_class', 'proc_arg_defaults', 'done']
    #              trigger, source, destination
    #['skip_to', '*', 'skip', 'after="skip"'],
    transitions = [ 
        ['start', 'start', 'skip'], 
        ['do_end', '*', 'done'],
    ]    
    
    
    def __init__(self, lines):
        self.lines = lines # all lines
        self.line = "" # current line
        self.l = 0  # cursor of current line
        
        self.class_name_dict = {}
        self.synths = {}
        
        self._debug = False
        
        self.machine = Machine(model = self, states = ParseSynth.states, transitions = ParseSynth.transitions, initial='start')
        
        self.machine.add_transition('skip_to', '*', 'skip', after='skip_m')
        self.machine.add_transition('do_arg_info', 'skip', 'proc_arg_info', after='proc_arg_info')
        #self.machine.add_transition('do_class', '*', 'each_class', after='proc_class')
        #self.machine.add_transition('do_arg_info', 'skip', 'proc_arg_info', after='proc_arg_info')
        #self.machine.on_enter_skip('skip')
        #self.machine.on_enter_each_class('proc_class')
        self.machine.on_enter_done('do_end')

    def next_line(self):
        self.l += 1
        self.line = self.lines[self.l]
        '''
        if self._debug:
            curframe = inspect.currentframe()
            calframe = inspect.getouterframes(curframe, 2)
            print('next line call from :', calframe[1][3], calframe[1][2])
        '''
    def goNext(self):
        self.next_line()
        self.empty_skip()
        
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
        '''
        if "SoundIn <" in self.line:
            self._debug = True
            print("="*30)
        else:
            self._debug = False        
        '''            
        while self.line != end_class:            
            s = self.line            
            #if self._debug: print(self.line)
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
                    arg_def[arg.strip()] = v
                    self.next_line()
                for k, v in arg_def.items(): # fix value reference
                    if v[0] == ":":
                        ref = arg_def[v]
                        arg_def[k] = ref
            else:                 
                self.next_line()
                #if self._debug: print("NEXT2", self.line)
        #print(synth_name, synth_slang)
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
        
    def skip_m(self, match):        
        print("skip>", match)
        if not match: return True
        for s in self.lines[self.l:]:
            self.l += 1
            if match in s:
                self.line = s
                return True

    def proc_arg_info(self):
        print("state=", self.state)
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
    
    
    def empty_skip(self):
        while self.line == '\n':
            self.next_line()

    def do_end(self):        
        print("END")
        
    
def parseSynth():
    const_file = open('synthinfo.rb').readlines()
    ps = ParseSynth(const_file)
    ps.start()
    ps.skip_to("class BaseInfo")
    ps.skip_to("def default_arg_info")    
    arg_base = ps.do_arg_info()
    print(arg_base)
    ps.synths['__BaseInfo__'] = {'arg_info':arg_base}
    
    ps.skip_to("class SoundIn < SonicPiSynth")
    stop_class_line = '    class BaseInfo\n'
    while(ps.line != stop_class_line):
        #ps.empty_skip()
        op = ps.proc_class()
        if not op:
            print("ops")
            break        
    js_dump(ps.synths)
    return ps

def js_dump(const):
    import json
    with open('synths.json', 'w') as outfile:
        json.dump(const, outfile, sort_keys = True, indent = 2)    
        
if __name__ == '__main__':
        
    ps = parseSynth()
    
