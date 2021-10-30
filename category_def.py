from lang_def import *
from constant_def import samples

#                0         1      2       3        4          5          6         7        8        9
categories = ['common', 'synth', 'fx', 'do_end', 'use', 'functions', 'control', 'buffer', 'env', 'general']

all_lang_ref = list(lang_core.keys()) + list(lang_sound.keys())

# def all_synth_names():
#     for key, value in synths.items():
#         if value['hiden'] != True and key != 'SoundIn' and value['name'] in synth_nodes:
#             yield value['name']
#
# all_synth = {s: synths[synth_nodes[s]] for s in all_synth_names()}

# def all_fx_names():
#     for key, value in fx.items():
#         if value['hiden'] != True and value['name'] in synth_nodes:
#             yield value['name']

# all_fx = {s: fx[synth_nodes[s]] for s in all_fx_names()}

def predef_sample_names():
    all = []
    for key, value in samples.items():
        yield all
        all += value

predef_samples = [ s for s in predef_sample_names()][0]

def lng(ref):
    if ref in lang_core:
        return lang_core[ref]
    elif ref in lang_sound:
        return lang_sound[ref]
    else: return None

def sn(ref):
    c_name = synth_nodes[ref]
    if 'FX' in c_name:
        return fx[c_name]
    else:
        return synths[c_name]



has_intro_fn = [key for key, value in lang_sound.items()
            if 'intro_fn' in value and value['intro_fn'] is not False
            ] + [key for key, value in lang_core.items()
            if 'intro_fn' in value and value['intro_fn'] is not False
            ]
has_async_block = [key for key, value in lang_core.items()
                 if 'async_block' in value and value['async_block'] is not False
                 ] + [key for key, value in lang_sound.items()
                 if 'async_block' in value and value['async_block'] is not False
                 ]
has_modifies_env = [key for key, value in lang_core.items()
                    if 'modifies_env' in value and value['modifies_env'] is not False
                    ] + [ key for key, value in lang_sound.items()
                    if 'modifies_env' in value and value['modifies_env'] is not False
                    ]
has_accepts_block = [key for key, value in lang_core.items()
                   if 'accepts_block' in value and value['accepts_block'] is not False
                   ] + [key for key, value in lang_sound.items()
                   if 'accepts_block' in value and value['accepts_block'] is not False
                   ]

has_accepts_block_false = [key for key, value in lang_core.items()
                        if 'accepts_block' in value and value['accepts_block'] is False and key not in has_modifies_env
                        ] + [key for key, value in lang_sound.items()
                        if 'accepts_block' in value and value['accepts_block'] is False and key not in has_modifies_env
                        ]
has_requires_block = [key for key, value in lang_core.items()
                    if 'requires_block' in value and value['requires_block'] is not False
                    ] + [key for key, value in lang_sound.items()
                    if 'requires_block' in value and value['requires_block'] is not False
                    ]

has_returns = [key for key, value in lang_core.items()
             if 'returns' in value and value['returns'] is not False
             ] + [key for key, value in lang_sound.items()
             if 'returns' in value and value['returns'] is not False
             ]

has_memoize = [key for key, value in lang_core.items()
                  if 'memoize' in value and value['memoize'] is not False
                  ] + [ key for key, value in lang_sound.items()
                  if 'memoize' in value and value['memoize'] is not False
                  ]

has_inline = [key for key, value in lang_core.items()
            if 'inline' in value and value['inline'] is True
            ] + [key for key, value in lang_sound.items()
            if 'inline' in value and value['inline'] is True
            ] + has_memoize



# advances_time_c = {key: value for key, value in lang_core.items()
#                   if value['hiden'] is False
#                   if 'advances_time' in value and value['advances_time'] is not False
#                   }
# advances_time_s = {key: value for key, value in lang_sound.items()
#                   if value['hiden'] is False
#                   if 'advances_time' in value and value['advances_time'] is not False
#                   }

# accepts_block_sign_c = {key: value for key, value in lang_core.items()
#                    if value['hiden'] is False
#                    if 'accepts_block' in value and value['accepts_block'] is not False and '&block' in value['signature']
#                    }
# accepts_block_sign_s = {key: value for key, value in lang_sound.items()
#                    if value['hiden'] is False
#                    if 'accepts_block' in value and value['accepts_block'] is not False and '&block' in value['signature']
#                    }


'''
we want to distinguish between functions that are inline
ie doesn't have new line before so output single strings
puts (spark_graph (range 1, 5).shuffle)
here spark_graph, range, shuffle are inline
(it seems memoize is the closest but many is missing)
'''


# fn_ringed are function like tick, shuffle (ring).fn(arg)
fn_ringed = ['pick', 'tick', 'look', 'shuffle', 'choose', 'stretch', ]
# fn_embeded are functions surrounded by () like (knit 1, 5)
fn_embeded = ['bools', 'chord', 'chord_degree', 'chord_invert', 'doubles', 'halves', 'knit', 'line', 'midi_notes',
              'note_range', 'octs', 'ramp', 'range', 'ring', 'scale', 'scale',  'spread', 'vector']
# fn_simple dice 2
fn_simple = ['dice', 'one_in', 'pitch_to_ratio', 'ratio_to_pitch']
# fn_normal degree(2, :C3, :minor)
fn_normal = ['degree', 'hz_to_midi', 'midi_to_hz', 'quantise', 'rand', 'rand_i',
             'rand_i_look', 'rand_look', 'rdist', 'rrand', 'rrand_i', 'rt', 'vt']

is_inline_fn = fn_ringed + fn_embeded + fn_simple + fn_normal

is_just_output = ['all_sample_names', 'beat', 'bt', 'chord_names', 'current_arg_checks',
               'current_beat_duration', 'current_bpm', 'current_cent_tuning', 'current_debug', 'current_octave',
               'current_random_seed', 'current_sample_defaults', 'current_sched_ahead_time', 'current_synth',
               'current_synth_defaults', 'current_transpose', 'current_volume', 'fx_names', 'note_info',
               'sample_duration', 'sample_groups', 'sample_info', 'sample_names', 'sample_paths', 'scale_names',
               'synth_names', 'version', 'spark', 'status']

is_synth = ['with_fx', 'synth', 'with_synth', 'use_synth', 'use_synth_defaults','with_synth_defaults', 'with_merged_synth_defaults']

# set hide to false if not set and hide the one we are not going to use
is_rec = ['recording_delete', 'recording_save', 'recording_start', 'recording_stop']
is_dups = ['wait','with_afx', 'use_fx', 'use_timing_warnings', 'invert_chord', 'pitch_ratio', 'print', 'sample_buffer',
           'with_tempo', 'pitch_ratio', 'load_sample', 'load_sample_at_path',]

is_to_hide = [ 'dec', 'inc', 'puts',
               'load_synthdefs', 'load_example', 'comment', 'uncomment','resolve_sample_paths', 'resolve_sample_path',
               'use_osc', 'osc', 'osc_send', 'with_timing_warnings','use_timing_warnings', 'use_external_synths',
               'start_amp_monitor', 'current_amp', 'sample_split_filts_and_opts','ndefine', 'spark_graph',
           ] + is_just_output + is_dups + is_rec + is_synth


#####################################
# other static category
# all_lang_def = list(set(all_lang_ref) - set(set(all_lang_ref) - set(has_accepts_block) - set(has_accepts_block_false)) set(has_modifies_env) )

is_buffer_fn = ['load_buffer', 'load_samples',
                'run_code', 'run_file',
                ]

is_control = [ 'clear', 'control', 'cue', 'kill', 'rand_back', 'rand_reset', 'rand_skip',
              'reset', 'sample_free', 'sample_free_all', 'sleep', 'stop', 'sync', 'sync_bpm',
               'tick_reset', 'tick_reset_all', 'tick_set',]
is_common = ['play', 'chord', 'note', 'note_list', 'live_loop', 'sample']
# ring_returns = [ret for ret in has_returns if lng(ret)['returns'] == ":ring" ]

is_use_env = [ret for ret in all_lang_ref if ret.startswith('use_') ]





def report():
    print('\nintro_fn: lang_core + lang_sound')
    print(has_intro_fn)
    print('\nasync_block: lang_core + lang_sound')
    print(has_async_block)
    #
    print('\naccepts_block: lang_core + lang_sound ')
    print(has_accepts_block)
    print('\nrequires_block: lang_core + lang_sound ')
    print(has_requires_block)
    #
    print('\n DIFF accept - req (where block is optional)')
    print(list(set(has_accepts_block) - set(has_requires_block)))

    # print('\nNO accepts_block: ')
    # print(sorted(has_accepts_block_false))
    print('\n inline : ')
    print(sorted(has_inline))

    print('\n memoize : ')
    print(sorted(has_memoize))

    print('\nno inline : ')
    print(sorted(list(set(has_accepts_block_false) - set(has_inline) - set(is_buffer_fn))))
    print('\n........ : ')
    # print('\n returns ring: ')
    print(sorted(is_use_env))

    # print('\nreturns: lang_core + lang_sound ')
    # print(has_returns)
    # print('\nlang_core lang_sound with modifies_env:')
    # print(has_modifies_env)
    # print('\nlang_core lang_sound filtered:')
    # print(all_lang_def)


# print(sub_list([1,2,3,4,5], [1,2], [3,4]))
def sub_list(list_source, *lists_subtract):
    final = []
    for key in lists_subtract:
        final += key
    sub = list(set(list_source) - set(final))
    return sorted(sub)



from constant_def import samples

import json
if __name__ == '__main__':
    # from gen_constant_def import parse
    # parse()
    # print(sorted(notes.items(), key=operator.itemgetter(1)))
    # newd = {}
    # for k, v in notes.items():
    #     n = ':'+ k
    #     newd[n] = v
    # print(json.dumps(all_fx, indent = 2))
    # all_sample
    # s_name = [sn for sk in samples.keys() for sn in samples[sk] ]
    print()

    # print([':'+c for c in chord_names])
    # print('should be 0')
    # print(sub_list(has_accepts_block_false, has_inline, is_common, is_use_env, is_control, is_buffer_fn))
    # print(sub_list(has_accepts_block, has_requires_block))
    # print(sub_list(all_lang_ref, has_accepts_block, has_accepts_block_false, is_to_hide, is_buffer_fn, has_modifies_env))
