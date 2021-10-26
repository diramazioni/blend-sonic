{% extends "with_no_block.py" %}

{% block imports %}
{{ super() }}
from collections import Counter
{%- endblock %}

{% block extra_create %}
        self.newOutput("Boolean", "signal out", "signal")
{%- endblock %}

{%- block extra_input %}
        
{%- endblock %}

{%- block execode -%}
{{ super() }}          
        #yield "signal = signal{{inp}}"
        yield '''if args_ == 'false': 
                send = ['stop']
                signal = False
                '''
        yield '''else: 
                send = []
                signal = True
                '''
{%- endblock %}

        # yield "print('> ', self.count)"
        # yield '''if not signalIn and self.count == 0:
        #       signal = True
        #       self.count +=1
        #       print('T'*10, self.count)'''
        # yield '''elif not signalIn and self.count >= 1:
        #       signal = False
        #       self.count += 1
        #       print('F'*10)'''
        #
        # yield '''elif signalIn:
        #       signal = False
        #       self.count = 0
        #       #print('S'*10)'''