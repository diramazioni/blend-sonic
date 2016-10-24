from lang_def import *

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
            if value['hiden'] is False
            if 'intro_fn' in value and value['intro_fn'] is not False
            ] + [key for key, value in lang_core.items()
                 if value['hiden'] is False
                 if 'intro_fn' in value and value['intro_fn'] is not False
                 ]
has_async_block = [key for key, value in lang_core.items()
                 if value['hiden'] is False
                 if 'async_block' in value and value['async_block'] is not False
                 ] + [key for key, value in lang_sound.items()
                 if value['hiden'] is False
                 if 'async_block' in value and value['async_block'] is not False
                 ]
has_modifies_env = [key for key, value in lang_core.items()
                    if value['hiden'] is False
                    if key.endswith(('?', '!')) or 'modifies_env' in value and value['modifies_env'] is not False
                    ] + [
                       key for key, value in lang_sound.items()
                       if value['hiden'] is False
                       if key.endswith(('?', '!')) or 'modifies_env' in value and value['modifies_env'] is not False
                       ]
has_accepts_block = [key for key, value in lang_core.items()
                   if value['hiden'] is False
                   if 'accepts_block' in value and value['accepts_block'] is not False
                   ] + [key for key, value in lang_sound.items()
                   if value['hiden'] is False
                   if 'accepts_block' in value and value['accepts_block'] is not False
                   ]

has_accepts_block_false = [key for key, value in lang_core.items()
                         if value['hiden'] is False
                         if 'accepts_block' in value and value['accepts_block'] is False and key not in has_modifies_env
                         ] + [key for key, value in lang_sound.items()
                              if value['hiden'] is False
                              if 'accepts_block' in value and value['accepts_block'] is False and key not in has_modifies_env
                              ]
has_requires_block = [key for key, value in lang_core.items()
                    if value['hiden'] is False
                    if 'requires_block' in value and value['requires_block'] is not False
                    ] + [key for key, value in lang_sound.items()
                    if value['hiden'] is False
                    if 'requires_block' in value and value['requires_block'] is not False
                    ]

has_returns = [key for key, value in lang_core.items()
             if value['hiden'] is False
             if 'returns' in value and value['returns'] is not False
             ] + [key for key, value in lang_sound.items()
             if value['hiden'] is False
             if 'returns' in value and value['returns'] is not False
             ]

has_memoize = [key for key, value in lang_core.items()
                  if value['hiden'] is False
                  if 'memoize' in value and value['memoize'] is not False
                  ] + [
            key for key, value in lang_sound.items()
                  if value['hiden'] is False
                  if 'memoize' in value and value['memoize'] is not False
                  ]

has_inline = [key for key, value in lang_core.items()
                      if value['hiden'] is False
                      if 'inline' in value and value['inline'] is True
                      ] + [key for key, value in lang_sound.items()
                           if value['hiden'] is False
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
fn_ringed = ['pick', 'tick', 'look', 'shuffle', 'choose', 'stretch',]
# fn_embeded are functions surrounded by () like (knit 1, 5)
fn_embeded = ['bools', 'chord', 'chord_degree', 'chord_invert', 'doubles', 'halves', 'knit', 'line', 'midi_notes',
              'note_range', 'octs', 'ramp', 'range', 'ring', 'scale', 'scale', 'spark_graph', 'spread', 'vector']
# fn_simple dice 2
fn_simple = ['dice', 'one_in', 'pitch_to_ratio', 'ratio_to_pitch']
# fn_normal degree(2, :C3, :minor)
fn_normal = ['degree', 'hz_to_midi', 'midi_to_hz', 'note', 'quantise', 'rand', 'rand_i',
             'rand_i_look', 'rand_look', 'rdist', 'rrand', 'rrand_i', 'rt', 'vt']

is_inline_fn = fn_ringed + fn_embeded + fn_simple + fn_normal

is_just_output = ['all_sample_names', 'assert', 'assert_equal', 'beat', 'bt', 'chord_names', 'current_arg_checks',
               'current_beat_duration', 'current_bpm', 'current_cent_tuning', 'current_debug', 'current_octave',
               'current_random_seed', 'current_sample_defaults', 'current_sched_ahead_time', 'current_synth',
               'current_synth_defaults', 'current_transpose', 'current_volume', 'fx_names', 'note_info',
               'sample_duration', 'sample_groups', 'sample_info', 'sample_names', 'sample_paths', 'scale_names',
               'synth_names', 'version', 'spark', 'status']
# set hide to false if not set and hide the one we are not going to use
is_rec = ['recording_delete', 'recording_save', 'recording_start', 'recording_stop']
is_dups = ['wait','with_afx', 'use_fx', 'use_timing_warnings', 'invert_chord', 'pitch_ratio', 'print', 'sample_buffer','with_tempo']
is_to_hide = [ 'dec', 'inc', 'puts',
               'load_synthdefs', 'load_example', 'comment', 'uncomment','resolve_sample_paths', 'resolve_sample_path',
               'use_osc', 'osc','with_timing_warnings','use_timing_warnings', 'use_external_synths',
               'start_amp_monitor', 'current_amp', 'sample_split_filts_and_opts','ndefine'
           ] + is_just_output + is_dups + is_rec





#####################################
# other static category
all_lang_def = list(set(all_lang_ref) - set(set(all_lang_ref) - set(has_accepts_block) - set(has_accepts_block_false))
                                        - set(has_modifies_env) )
is_buffer_fn = ['load_buffer', 'load_sample', 'load_samples', 'load_sample_at_path',
                'run_code', 'run_file', 'sample_free', 'sample_free_all',
                ]

is_control = [ 'clear', 'control', 'cue', 'kill', 'rand_back',
              'rand_reset', 'rand_skip', 'reset', 'sleep', 'stop', 'sync', 'sync_bpm', 'tick_reset', 'tick_reset_all',
              'tick_set',]
is_common = ['play', 'play_chord', 'play_pattern', 'play_pattern_timed','live_loop', 'sample', 'synth', 'with_fx']
ring_returns = [ret for ret in has_returns if lng(ret)['returns'] == ":ring" ]

is_use_env = [ret for ret in all_lang_ref if ret.startswith('use_') ]


# print(sub_list([1,2,3,4,5], [1,2], [3,4]))
def sub_list(list_source, *lists_subtract):
    final = []
    for key in lists_subtract:
        final += key
    sub = list(set(list_source) - set(final))
    return sorted(sub)

###################################

## these func can be sync based on the examples
missing_intro_fn = ['current_random_seed', 'synth']
## these func can be async based on the examples
missing_async_block = ['density', 'with_fx', 'sample', 'synth', 'play']
## these func has wrong accepts_block (based on the examples)
wrong_accepts_block = ['on', 'with_merged_sample_defaults', 'with_sample_defaults', 'use_timing_guarantees']


if __name__ == '__main__':
    print('should be 0')
    print(sub_list(has_accepts_block_false, has_inline, is_common, is_use_env, is_control, is_buffer_fn))
    # print(sub_list(has_accepts_block, is_control))
    print(sub_list(all_lang_ref, has_accepts_block, has_accepts_block_false, is_to_hide, is_buffer_fn, has_modifies_env))

