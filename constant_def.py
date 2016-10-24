null = None

'''
we want to distinguish between functions that are inline
ie doesn't have new line before so output single strings
puts (spark_graph (range 1, 5).shuffle)
here spark_graph, range, shuffle are inline
(it seems memoize is the closest but many is missing)
exclude memoize:
['all_sample_names', 'chord', 'chord_degree', 'chord_names',
'doubles', 'fx_names', 'halves', 'line', 'midi_notes', 'range',
'sample_groups', 'sample_names', 'scale', 'scale_names', 'synth_names']
'''


# is_selection are function like tick, shuffle (ring).fn(arg)
is_selection = ['pick', 'tick', 'look', 'shuffle']
# is_embed are functions surrounded by () like (knit 1, 5)
is_embed = ['stretch', 'spark_graph', 'vector']

is_inline = is_selection + is_embed +\
            ['beat', 'bt', 'choose', 'degree', 'dice', 'hz_to_midi', 'one_in', 'midi_to_hz',  'note', 'note_info',
             'pitch_to_ratio', 'quantise', 'ramp', 'rand', 'rrand', 'rrand_i', 'rand_i', 'rand_i_look', 'rand_look',
             'ratio_to_pitch', 'rdist', 'rt', 'vt']

## buffer fn
is_buffer_fn = ['load_buffer', 'load_sample',
                'run_code', 'run_file', 'sample_free', 'sample_free_all',
                ]
## these func can be sync based on the examples
missing_intro_fn = ['current_random_seed', 'synth']
## these func can be async based on the examples
missing_async_block = ['density', 'with_fx', 'sample', 'synth', 'play']
## these func has wrong accepts_block (based on the examples)
wrong_accepts_block = ['on', 'with_merged_sample_defaults', 'with_sample_defaults']


## set hide to false if not set and hide the one we are not going to use
is_to_hide = ['assert', 'assert_equal', 'current_arg_checks', 'current_beat_duration', 'current_bpm',
           'current_cent_tuning', 'current_debug', 'current_octave', 'current_random_seed',
           'current_sample_defaults', 'current_sched_ahead_time', 'current_synth', 'current_synth_defaults',
           'current_transpose', 'current_volume', 'dec', 'inc', 'print', 'puts', 'version', 'wait', 'load_samples',
              'sample_buffer', 'sample_info', 'sample_duration', 'load_synthdefs', 'load_example',
           ]


opts_default_val = {
  "another_key": "foo: 64",  #only used in cue accepts: Numbers, Symbols, Booleans and Nil, or Vectors/Rings of immutable types"
  "amp": 1, 
  "amp_slide": 1,  
  "attack": 0,  
  "attack_level": 1, 
  "auto_cue": True,  
  "bpm_sync": False,  
  "delay": 0,  
  "decay": 0,  
  "decay_level": 1, 
  "env_curve": 1, 
  "on": 1, # Boolean
  "pan": 0, 
  "pan_slide": 1, 
  "pitch": 0, 
  "release": 0, 
  "slide": 0, 
  "sustain": 1, 
  "sustain_level": 1,    
  "invert": 0, 
  "num_beats": 1, 
  "num_octaves": 1, 
  "octave": 4, 
  "pre_amp": 1, 
  "reps": 1,
  "pitches": [],
  "kill_delay": 1,
  "leak_dc_bypass": 0,
  "limiter_bypass": 0,
  "lpf": 131, # max 131
  "lpf_bypass": 0,
  "beat_stretch": 1,
  "finish": 1, #from 0 to 1
  "pitch_stretch": 1,  #from 0 to 1
  "rate": 1,
  "rpitch": 0,
  "start": 0,  #from 0 to 1
  "clamp_time": 0, # ?
  "compress": 0,  # Boolean
  "key": "foo: 64", #only used in cue
  "hpf": 0,
  "hpf_bypass": 0,
  "hpf_attack": 0,
  "hpf_attack_level": 0 ,
  "hpf_decay": 0 ,
  "hpf_decay_level": 0,
  "hpf_env_curve": 1,
  "hpf_init_level": 130,
  "hpf_max": 200,
  "hpf_release": 0 ,
  "hpf_release_level": 0,
  "hpf_sustain": 0 ,
  "hpf_sustain_level": 0,
  "inclusive": False,
  "init": "",  
  "lpf_attack": 0 ,
  "lpf_attack_level": 0 ,
  "lpf_decay": 0 ,
  "lpf_decay_level": 0 ,
  "lpf_env_curve": 1,
  "lpf_init_level": 30,
  "lpf_min": 30,
  "lpf_release": 0 ,
  "lpf_release_level": 0 ,
  "lpf_sustain": 0 ,
  "lpf_sustain_level": 0 ,
  "name": ":foo", # symbol
  "norm": 0, #?
  "onset": 0,
  "offset": 0,  
  "override": False,
  "rotate": False,
  "seed": 0, #? not sure if it expect the seed or a boolean
  "skip": 0,
  "step": 1,
  "steps": 1,
  "sync": ":foo", # symbol
  "sync_bpm": ":foo", # symbol
  "your_key": ":bar",
  "path": "/path/to/file",
  "pitch_dis": 0,
  "relax_time": 0, # ?
  "slope_above": 1,
  "slope_below": 1,
  "threshold": 0, #?
  "time_dis": 0, #?
  "window_size": 0 #?
}

opts_types_conversion = {
  "another_key": "String",  # immutable  
  "amp": "Float",
  "amp_slide": "Float",
  "attack": "Float", 
  "attack_level": "Float",
  "auto_cue": "Boolean",  
  "bpm_sync": "Boolean",
  "decay": "Float",
  "decay_level": "Float",
  "delay": "Float",  # beats
  "env_curve": "Integer",
  "on": "Boolean",
  "pan": "Float",
  "pan_slide": "Float",
  "pitch": "Float",
  "release": "Float",
  "slide": "Float",
  "sustain": "Float",
  "sustain_level": "Float",    
  "inclusive": "Boolean",
  "init": "String", # ? there are no examples...
  "invert": "Integer",  
  "num_beats": "Integer",
  "num_octaves": "Integer",
  "octave": "Integer", 
  "pitches": "String List", # notes [ :A, :B4, :C4 ]
  "pre_amp": "Float",
  "reps": "Integer",
  "kill_delay": "Float",
  "leak_dc_bypass": "Boolean",
  "limiter_bypass": "Boolean",
  "lpf": "Float",
  "lpf_bypass": "Boolean",
  "beat_stretch": "Float", # positive
  "finish": "Float",
  "pitch_stretch": "Float",
  "rate": "Float",
  "rpitch": "Float",
  "start": "Float",
  "clamp_time": "Float", # ?
  "compress": "Boolean",
  "key": "String", # notes etc immutable
  "hpf": "Float",
  "hpf_bypass": "Boolean",
  "hpf_attack": "Float",
  "hpf_attack_level": "Float",
  "hpf_decay": "Float",
  "hpf_decay_level": "Float",
  "hpf_env_curve": "Integer",
  "hpf_init_level": "Integer",
  "hpf_max": "Integer",
  "hpf_release": "Float",
  "hpf_release_level": "Float",
  "hpf_sustain": "Float",
  "hpf_sustain_level": "Float",
  "lpf_attack": "Float",
  "lpf_attack_level": "Float",
  "lpf_decay": "Float",
  "lpf_decay_level": "Float",
  "lpf_env_curve": "Integer",
  "lpf_init_level": "Integer",
  "lpf_min": "Integer",
  "lpf_release": "Float",
  "lpf_release_level": "Float",
  "lpf_sustain": "Float",
  "lpf_sustain_level": "Float",
  "name": "String",  
  "norm": "Float", #?
  "onset": "Integer", 
  "offset": "Integer",  
  "override": "Boolean",
  "rotate": "Boolean",
  "seed": "Integer",
  "skip": "Integer",
  "step": "Float",
  "steps": "Integer", # positive
  "sync": "String", # symbol
  "sync_bpm": "String", # symbol
  "your_key": "String",  # symbol
  "path": "String",
  "pitch_dis": "Float",
  "relax_time": "Float", # ?
  "slope_above": "Float",
  "slope_below": "Float",
  "threshold": "Float",
  "time_dis": "Float",
  "window_size": "Float"  
}

args_types_conversion = {
  ":anything": "String", 
  ":array": "String List", # notes (ring) :A3, :B4, :C4 
  ":boolean": "Boolean", 
  ":density": "Integer",  # positive Int 
  ":int": "Integer",  
  ":list": "String List", # notes [ :A, :B4, :C4 ]
  ":list_or_number": "String List", # notes AND int_List [ :A, :B4, :C4 ], [ 1,2,3 ]
  ":midi_number": "Integer", # note (only used in pitch_to_ratio)
  ":note": "Integer", # note (ring) # :A3 or 60
  ":number": "Float",
  ":number_or_nil": "Integer", # posiyive int, can be null
  ":number_or_range": "String", # int or (range 1, 5)  
  ":number_symbol_or_map": "Integer", # note (only used in :rest?)
  ":path": "String",  # escaped with \"
  ":pos_int": "Integer", # note (ring)
  ":positive_number": "Float",  
  ":ramp": "Integer",  # only used in ramp as return value
  ":sample_name_or_duration": "String", # string_or_number (only used in :use_sample_bpm :with_sample_bpm)
  ":source_and_filter_types": "String", # same as symbol_or_string sample (only used in :sample_paths)
  ":string": "String",
  ":symbol": "String", # note/reference with :
  ":symbol_or_number": "String", # note/reference: :A or 60
  ":symbol_or_string": "String", # note/reference: :A or 60
  ":synth_node": "String", # reference to var = 
  ":truthy": "Boolean", # true except for: false, nil and 0
  ":true_or_false": "String", # true or false (lowercase)
  ":ring": "String List", # only used as return value for array of notes (ring)
  ":vector": "Integer List" # only used as return value for vector
}
'''
simple_sampler_args = [':amp', ':amp_slide', ':amp_slide_shape', ':amp_slide_curve', ':pan', ':pan_slide', ':pan_slide_shape', ':pan_slide_curve', ':cutoff', ':cutoff_slide', ':cutoff_slide_shape', ':cutoff_slide_curve', ':lpf', ':lpf_slide', ':lpf_slide_shape', ':lpf_slide_curve', ':hpf', ':hpf_slide', ':hpf_slide_shape', ':hpf_slide_curve', ':rate', ':slide', ':beat_stretch', ':rpitch', ':attack', ':decay', ':sustain', ':release', ':attack_level', ':decay_level', ':sustain_level', ':env_curve']
'''

notes = {
  "A2": 45,
  "A3": 57,
  "A4": 69,
  "A5": 81,
  "Ab2": 44,
  "Ab3": 56,
  "Ab4": 68,
  "Ab5": 80,
  "As2": 46,
  "As3": 58,
  "As4": 70,
  "As5": 82,
  "B3": 59,
  "B4": 71,
  "B5": 83,
  "Bb2": 46,
  "Bb3": 58,
  "Bb4": 70,
  "Bb5": 82,
  "C2": 36,
  "C3": 48,
  "C4": 60,
  "C5": 72,
  "C6": 84,
  "Cs2": 37,
  "Cs3": 49,
  "Cs4": 61,
  "Cs5": 73,
  "D2": 38,
  "D3": 50,
  "D4": 62,
  "D5": 74,
  "Db2": 37,
  "Db3": 49,
  "Db4": 61,
  "Db5": 73,
  "Ds2": 39,
  "Ds3": 51,
  "Ds4": 63,
  "Ds5": 75,
  "E2": 40,
  "E3": 52,
  "E4": 64,
  "E5": 76,
  "Eb2": 39,
  "Eb3": 51,
  "Eb4": 63,
  "Eb5": 75,
  "F2": 41,
  "F3": 53,
  "F4": 65,
  "F5": 77,
  "Fs2": 42,
  "Fs3": 54,
  "Fs4": 66,
  "Fs5": 78,
  "G2": 43,
  "G3": 55,
  "G4": 67,
  "G5": 79,
  "Gb2": 42,
  "Gb3": 54,
  "Gb4": 66,
  "Gb5": 78,
  "Gs2": 44,
  "Gs3": 56,
  "Gs4": 68,
  "Gs5": 80,
  ":rest": ":rest"
}
'''
synthezier = {
  "BEEP": "beep",
  "BLADE": "blade",
  "BNOISE": "bnoise",
  "CNOISE": "cnoise",
  "DARK_AMBIENCE": "dark_ambience",
  "DARK_SEA_HORN": "dark_sea_horn",
  "DPULSE": "dpulse",
  "DSAW": "dsaw",
  "DTRI": "dtri",
  "DULL_BELL": "dull_bell",
  "FM": "fm",
  "GNOISE": "gnoise",
  "GROWL": "growl",
  "HOLLOW": "hollow",
  "HOOVER": "hoover",
  "MOD_DSAW": "mod_dsaw",
  "MOD_FM": "mod_fm",
  "MOD_PULSE": "mod_pulse",
  "MOD_SAW": "mod_saw",
  "MOD_SINE": "mod_sine",
  "MOD_TRI": "mod_tri",
  "NOISE": "noise",
  "PIANO": "piano",
  "PLUCK": "pluck",
  "PRETTY_BELL": "pretty_bell",
  "PROPHET": "prophet",
  "PULSE": "pulse",
  "SAW": "saw",
  "SQUARE": "square",
  "SUBPULSE": "subpulse",
  "SUPERSAW": "supersaw",
  "SYNTH_VIOLIN": "synth_violin",
  "TB303": "tb303",
  "TRI": "tri",
  "ZAWA": "zawa"
}
'''
samples = {
  "AMBI_CHOIR": "ambi_choir",
  "AMBI_DARK_WOOSH": "ambi_dark_woosh",
  "AMBI_DRONE": "ambi_drone",
  "AMBI_GLASS_HUM": "ambi_glass_hum",
  "AMBI_GLASS_RUB": "ambi_glass_rub",
  "AMBI_HAUNTED_HUM": "ambi_haunted_hum",
  "AMBI_LUNAR_LAND": "ambi_lunar_land",
  "AMBI_PIANO": "ambi_piano",
  "AMBI_SOFT_BUZZ": "ambi_soft_buzz",
  "AMBI_SWOOSH": "ambi_swoosh",
  "BASS_DNB_F": "bass_dnb_f",
  "BASS_DROP_C": "bass_drop_c",
  "BASS_HARD_C": "bass_hard_c",
  "BASS_HIT_C": "bass_hit_c",
  "BASS_THICK_C": "bass_thick_c",
  "BASS_VOXY_C": "bass_voxy_c",
  "BASS_VOXY_HIT_C": "bass_voxy_hit_c",
  "BASS_WOODSY_C": "bass_woodsy_c",
  "BD_808": "bd_808",
  "BD_ADA": "bd_ada",
  "BD_BOOM": "bd_boom",
  "BD_FAT": "bd_fat",
  "BD_GAS": "bd_gas",
  "BD_HAUS": "bd_haus",
  "BD_KLUB": "bd_klub",
  "BD_PURE": "bd_pure",
  "BD_SONE": "bd_sone",
  "BD_TEK": "bd_tek",
  "BD_ZOME": "bd_zome",
  "BD_ZUM": "bd_zum",
  "DRUM_BASS_HARD": "drum_bass_hard",
  "DRUM_BASS_SOFT": "drum_bass_soft",
  "DRUM_CYMBAL_CLOSED": "drum_cymbal_closed",
  "DRUM_CYMBAL_HARD": "drum_cymbal_hard",
  "DRUM_CYMBAL_OPEN": "drum_cymbal_open",
  "DRUM_CYMBAL_PEDAL": "drum_cymbal_pedal",
  "DRUM_CYMBAL_SOFT": "drum_cymbal_soft",
  "DRUM_HEAVY_KICK": "drum_heavy_kick",
  "DRUM_SNARE_HARD": "drum_snare_hard",
  "DRUM_SNARE_SOFT": "drum_snare_soft",
  "DRUM_SPLASH_HARD": "drum_splash_hard",
  "DRUM_SPLASH_SOFT": "drum_splash_soft",
  "DRUM_TOM_HI_HARD": "drum_tom_hi_hard",
  "DRUM_TOM_HI_SOFT": "drum_tom_hi_soft",
  "DRUM_TOM_LO_HARD": "drum_tom_lo_hard",
  "DRUM_TOM_LO_SOFT": "drum_tom_lo_soft",
  "DRUM_TOM_MID_HARD": "drum_tom_mid_hard",
  "DRUM_TOM_MID_SOFT": "drum_tom_mid_soft",
  "ELEC_BEEP": "elec_beep",
  "ELEC_BELL": "elec_bell",
  "ELEC_BLIP": "elec_blip",
  "ELEC_BLIP2": "elec_blip2",
  "ELEC_BLUP": "elec_blup",
  "ELEC_BONG": "elec_bong",
  "ELEC_CHIME": "elec_chime",
  "ELEC_CYMBAL": "elec_cymbal",
  "ELEC_FILT_SNARE": "elec_filt_snare",
  "ELEC_FLIP": "elec_flip",
  "ELEC_FUZZ_TOM": "elec_fuzz_tom",
  "ELEC_HI_SNARE": "elec_hi_snare",
  "ELEC_HOLLOW_KICK": "elec_hollow_kick",
  "ELEC_LO_SNARE": "elec_lo_snare",
  "ELEC_MID_SNARE": "elec_mid_snare",
  "ELEC_PING": "elec_ping",
  "ELEC_PLIP": "elec_plip",
  "ELEC_POP": "elec_pop",
  "ELEC_SNARE": "elec_snare",
  "ELEC_SOFT_KICK": "elec_soft_kick",
  "ELEC_TICK": "elec_tick",
  "ELEC_TRIANGLE": "elec_triangle",
  "ELEC_TWANG": "elec_twang",
  "ELEC_TWIP": "elec_twip",
  "ELEC_WOOD": "elec_wood",
  "GUIT_E_FIFTHS": "guit_e_fifths",
  "GUIT_E_SLIDE": "guit_e_slide",
  "GUIT_HARMONICS": "guit_harmonics",
  "LOOP_AMEN": "loop_amen",
  "LOOP_AMEN_FULL": "loop_amen_full",
  "LOOP_COMPUS": "loop_compus",
  "LOOP_INDUSTRIAL": "loop_industrial",
  "MISC_BURP": "misc_burp",
  "PERC_BELL": "perc_bell"
}

chord = {
  "AUG": "aug",
  "DIM": "dim",
  "DIM7": "dim7",
  "DOM7": "dom7",
  "MAJOR7": "major7",
  "MINOR7": "minor7"
}

scale_mode = {
  "AEOLIAN": "aeolian",
  "AHIRBHAIRAV": "ahirbhairav",
  "AUGMENTED": "augmented",
  "AUGMENTED2": "augmented2",
  "BARTOK": "bartok",
  "BHAIRAV": "bhairav",
  "CHINESE": "chinese",
  "CHROMATIC": "chromatic",
  "DIATONIC": "diatonic",
  "DIMISHED": "diminished",
  "DIMISHED2": "diminished2",
  "DORIAN": "dorian",
  "EGYPTIAN": "egyptian",
  "ENIGMATIC": "enigmatic",
  "GONG": "gong",
  "HARMONIC_MAJOR": "harmonic_major",
  "HARMONIC_MINOR": "harmonic_minor",
  "HEX_AEOLIAN": "hex_aeolian",
  "HEX_DORIAN": "hex_dorian",
  "HEX_MAJOR6": "hex_major6",
  "HEX_MAJOR7": "hex_major7",
  "HEX_PHRYGIAN": "hex_phrygian",
  "HEX_SUS": "hex_sus",
  "HINDU": "hindu",
  "HIRAJOSHI": "hirajoshi",
  "HUNGARIAN_MINOR": "hungarian_minor",
  "I": "i",
  "II": "ii",
  "III": "iii",
  "INDIAN": "indian",
  "IONIAN": "ionian",
  "IV": "iv",
  "IWATO": "iwato",
  "JIAO": "jiao",
  "KUMOI": "kumoi",
  "LEADING_WHOLE": "leading_whole",
  "LOCRIAN": "locrian",
  "LOCRIAN_MAJOR": "locrian_major",
  "LYDIAN": "lydian",
  "LYDIAN_MINOR": "lydian_minor",
  "MAJOR": "major",
  "MAJOR_PENTATONIC": "major_pentatonic",
  "MARVA": "marva",
  "MELODIC_MAJOR": "melodic_major",
  "MELODIC_MINOR": "melodic_minor",
  "MELODIC_MINOR_ASC": "melodic_minor_asc",
  "MELODIC_MINOR_DESC": "melodic_minor_desc",
  "MESSIAEN1": "messiaen1",
  "MESSIAEN2": "messiaen2",
  "MESSIAEN3": "messiaen3",
  "MESSIAEN4": "messiaen4",
  "MESSIAEN5": "messiaen5",
  "MESSIAEN6": "messiaen6",
  "MESSIAEN7": "messiaen7",
  "MINOR": "minor",
  "MINOR_PENTATONIC": "minor_pentatonic",
  "MIXOLYDIAN": "mixolydian",
  "NEAPLOLITAN_MAJOR": "neapolitan_major",
  "NEAPLOLITAN_MINOR": "neapolitan_minor",
  "OCTATONIC": "octatonic",
  "PELOG": "pelog",
  "PHRYGIAN": "phrygian",
  "PROMETHEUS": "prometheus",
  "PRUVI": "purvi",
  "RITUSEN": "ritusen",
  "ROMANIAN_MINOR": "romanian_minor",
  "SCRIABIN": "scriabin",
  "SHANG": "shang",
  "SPANISH": "spanish",
  "SUPER_LOCRIAN": "super_locrian",
  "TODI": "todi",
  "V": "v",
  "VI": "vi",
  "VII": "vii",
  "VIII": "viii",
  "WHOLE": "whole",
  "WHOLE_TONE": "whole_tone",
  "YU": "yu",
  "ZHI": "zhi"
}
