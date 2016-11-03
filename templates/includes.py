

{% macro newArgInput(args) -%}

{% for ar in args %}
{%- for arg, val in ar.items() %}
        self.newInput("{{ args_types[val] }}", "{{ arg }}", "{{arg +inp }}")     
{%- endfor %}{%- endfor %}
{%- endmacro %} 

{%- macro newOptInput() %}
 {%- for opt, val in fn.opts|dictsort %}
  {%- if opts_types[opt] == "String" %}        
        self.newInput("{{ opts_types[opt] }}", "{{ opt }}", "{{opt +inp}}", value = "{{ val }}")  
  {%- else %}
        self.newInput("{{ opts_types[opt] }}", "{{ opt }}", "{{opt +inp}}", value = {{ val }})     
  {%- endif %}        
 {%- endfor %}
{%- endmacro %} 

{%- macro block_extra_create() %}
    {%- if fn.intro_fn %}
        self.newInput("String", "intro var", "intro_fn", value = "foo = ")
    {%- endif %}
    {%- if fn.async_block %}
        self.newInput("String", "async block", "async_block", value = "synth")
    {%- endif %}
        self.newInput("String List", "do_end lines", "do_end")
{%- endmacro %} 


{%- macro hideInput(start, end) %}
        for socket in self.inputs[{{ start }}:{{ end }}]:
            socket.useIsUsedProperty = True
            socket.isUsed = False
            #socket.value = False
        for socket in self.inputs[{{ start }}:{{ end }}]:
            socket.hide = True
{%- endmacro %}

{%- macro enum_member(enumList, ename, items) %}
    {{enumList}} = EnumProperty(name="{{ename}}", items = {{items}}, update=propertyChanged)
{%- endmacro %}
 
{%- macro next_prev_buttons(enumList) %}
        layout.prop(self, "{{enumList}}")
        row = layout.row(align = True)
        self.invokeFunction(row, "prevEl", text = "Prev", description = "get to the previous", icon = "TRIA_LEFT")
        self.invokeFunction(row, "nextEl", text = "Next", description = "get to the next", icon = "TRIA_RIGHT")     
{%- endmacro %}

{%- macro next_prev(enumList, items ) %}
    def nextEl(self):
        for i, k in enumerate({{items}}):
            if k == self.{{enumList}}:
                idx = i+1 if len({{items}})> i+1 else 0
                self.{{enumList}} = {{items}}[idx]
                return

    def prevEl(self):
        for i, k in enumerate({{items}}):
            if k == self.{{enumList}}:
                idx = i-1 if i>= 0 else len({{items}})
                self.{{enumList}} = {{items}}[idx]
                return        
{%- endmacro %}

{% macro argCheck(args) -%}
{% for ar in args %}
    {%- for arg, val in ar.items() %}        
        if s["{{ arg }}"].isUsed: 
        {%- if arg  == "list" %}
            yield "list_ = '['+', '.join(listIn)+']'"
        {%- elif args_types[val] == "String List"  and arg  != "list"%}
            yield "args_.append(', '.join({{ arg+inp }}))" 
        {%- elif args_types[val] == "Float" %}
            yield "args_.append('{0:.3g}'.format({{ arg+inp }}))"
        {%- elif args_types[val] == "Boolean" %}
            yield "if {{ arg+inp }} == True: args_.append('true')"
            yield "else: args_.append('false')"            
        {% else %}
            yield "if len(str({{ arg+inp }})): args_.append(str({{arg+inp }}))" 
        {% endif %}        
    {%- endfor %}
{%- endfor %}
        #yield "if len(args_): args_ = list(filter(None, args_ ))"        
{%- endmacro %} 

{% macro optCheck() -%}
    {%- for opt, val in fn.opts|dictsort  %}
        if s["{{ opt }}"].isUsed: 
            yield "pre = '{{ opt }}: '"
        {%- if opts_types[opt] == "String List" %}
            yield "opts_.append( pre + ', '.join({{ opt+inp }}))" 
        {%- elif opts_types[opt] == "Float" %}
            yield "opts_.append( pre + '{0:.3g}'.format({{ opt+inp }}))"
        {%- elif opts_types[opt] == "Boolean" %}
            yield "if {{ opt+inp }} == True: opts_.append('true')"
            yield "else: opts_.append(pre + 'false')"            
        {% else %}
            yield "if len(str({{ opt+inp }})): opts_.append(pre + str({{opt+inp }}))" 
        {% endif %}        
    {%- endfor %}
{%- endmacro %} 

{%- macro block_extra_input() %}
    {%- if fn.intro_fn %}
        if s["intro var"].isUsed: yield "intro_fn_ = intro_fn +' '"
        else: yield "intro_fn_ = ''"
    {%- endif %}{%- if fn.async_block %}
        if s["async block"].isUsed: yield "async_ = ' |'+ async_block + '|'" 
        else: yield "async_ = ''"
    {%- endif %}   
{%- endmacro %} 

{%- macro opt_join() %}
        yield "opts_ = ', '.join(opts_)"
        yield "sep=', ' if len(opts_) else '' "
{%- endmacro %} 

{%- macro arg_join() %}
        yield "args_ = ', '.join(args_) if len(args_) else ''"        
{%- endmacro %} 

{%- macro inline_send() %}
        yield "send = '({{ fn_name }} ' + args_ +sep+ opts_ + ')'"
{%- endmacro -%}

{%- macro fn_simple_send() %}
        yield "send = '({{ fn.name }} ' + list_ + args_ +sep+ opts_ + ')'"
{%- endmacro -%}

{%- macro add_fix() %}
        yield "send = prefix + send + postfix"
{%- endmacro -%}

{%- macro block_send(blk) %}
        yield "f_call = intro_fn_ + '{{blk}}{{fn.name}}' + args_ + sep+ opts_ "        
        yield "f_call = [f_call + ' do ' + async_]"
        yield "send = f_call + do_end + ['end']"    
{%- endmacro -%}

{%- macro no_block_send() %}
        yield "send = [prefix + '{{ fn_name }} ' + args_ + sep+ opts_ + postfix]"
{%- endmacro -%}

{%- macro opt_block_send() %}
        yield "f_call = intro_fn_ + '{{ fn.name }}' + args_ + sep+ opts_ "
        if s["do_end lines"].isUsed: 
            yield "f_call = [f_call + ' do ' + async_]"
            yield "send = f_call + do_end + ['end']"        
        else:
            yield "send = [f_call + async_]"
{%- endmacro -%}