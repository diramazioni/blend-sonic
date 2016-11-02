

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
        yield "if len(args_): args_ = list(filter(None, args_ ))"        
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

{%- macro inline_send(fn_name) %}
        yield "opts_ = ', '.join(opts_)"
        yield "sep=', ' if len(opts_) else '' "
        yield "args_ = ', '.join(args_)"
        yield "send = '({{ fn_name }} ' + args_ +sep+ opts_ + ')'"
{%- endmacro -%}





