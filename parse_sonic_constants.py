from transitions import Machine

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
        
        self.const = {}
        
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

    def proc_class(self):
        print("proc_class> ", (self.line, self.l))        
        if not self.line.startswith("    class"):
            print("bailout not a class")
            self.next_line()
            return {}
        cc = self.line.split()        
        c_name , c_parent = (cc[0],cc[2])
        if c_parent != "SonicPiSynth":
            inherit = True
        else:
            inherit = False
        #self.next_line()
        p_class = {}
        synth_name = ""
        synth_slang = ""
        while self.line != "    end\n":
            #print("while", self.line)
            s = self.line
            if "def name" in s:                    
                self.next_line()
                synth_slang = self.line.strip().strip('"')
            elif "def synth_name" in s:
                self.next_line()
                synth_name = self.line.strip().strip('"')
            else: 
                self.next_line()
        #print(synth_name, synth_slang)
        self.next_line()
        self.empty_skip()
        p_class[synth_name] = {"slang":synth_slang}
        return p_class
        
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
        
    
def init():
    const_file = open('synthinfo.rb').readlines()
    ps = ParseSynth(const_file)
    return ps

    
if __name__ == '__main__':
        
    ps = init()
    
    ps.start()
    ps.skip_to("class BaseInfo")
    ps.skip_to("def default_arg_info")    
    arg_base = ps.do_arg_info()
    print(arg_base)
    ps.const['arg'] = {'base': arg_base}
    ps.skip_to("class DullBell < SonicPiSynth")
    stop_class_line = '    class BaseInfo\n'
    while(ps.line != stop_class_line):
        #ps.empty_skip()
        synth = ps.proc_class()
        print(synth)
        print("-"*80)
        if len(synth)==0:
            print("ops")
            break
    