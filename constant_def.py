null = None



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

notes = {":rest": 0, ":Ds3": 51, ":F5": 77, ":Bb2": 46, ":A2": 45, ":Db2": 37, ":Ds5": 75, ":Bb5": 82, ":Gb2": 42, ":F2": 41, ":Gs4": 68, ":C2": 36, ":B5": 83, ":E3": 52, ":Fs4": 66, ":Cs5": 73, ":C6": 84, ":As3": 58, ":Bb4": 70, ":A4": 69, ":Ds4": 63, ":Db5": 73, ":C5": 72, ":As2": 46, ":Ab3": 56, ":E4": 64, ":Gs3": 56, ":C3": 48, ":G2": 43, ":G3": 55, ":Db3": 49, ":As5": 82, ":Fs2": 42, ":Eb4": 63, ":Ab5": 80, ":Cs4": 61, ":Bb3": 58, ":G4": 67, ":G5": 79, ":B4": 71, ":Gb4": 66, ":Db4": 61, ":E2": 40, ":Ab4": 68, ":A3": 57, ":Cs2": 37, ":D4": 62, ":A5": 81, ":C4": 60, ":F4": 65, ":D2": 38, ":Gb3": 54, ":Eb5": 75, ":D5": 74, ":Gs2": 44, ":D3": 50, ":Gs5": 80, ":Fs5": 78, ":Fs3": 54, ":Ds2": 39, ":As4": 70, ":F3": 53, ":Gb5": 78, ":Eb2": 39, ":Cs3": 49, ":B3": 59, ":E5": 76, ":Eb3": 51, ":Ab2": 44}

scale_names = [':aeolian', ':ahirbhairav', ':augmented', ':augmented2', ':bartok', ':bhairav', ':chinese', ':chromatic', ':diatonic', ':diminished', ':diminished2', ':dorian', ':egyptian', ':enigmatic', ':gong', ':harmonic_major', ':harmonic_minor', ':hex_aeolian', ':hex_dorian', ':hex_major6', ':hex_major7', ':hex_phrygian', ':hex_sus', ':hindu', ':hirajoshi', ':hungarian_minor', ':indian', ':ionian', ':iwato', ':jiao', ':kumoi', ':leading_whole', ':locrian', ':locrian_major', ':lydian', ':lydian_minor', ':major', ':major_pentatonic', ':marva', ':melodic_major', ':melodic_minor', ':melodic_minor_asc', ':melodic_minor_desc', ':messiaen1', ':messiaen2', ':messiaen3', ':messiaen4', ':messiaen5', ':messiaen6', ':messiaen7', ':minor', ':minor_pentatonic', ':mixolydian', ':neapolitan_major', ':neapolitan_minor', ':octatonic', ':pelog', ':phrygian', ':prometheus', ':purvi', ':ritusen', ':romanian_minor', ':scriabin', ':shang', ':spanish', ':super_locrian', ':todi', ':whole', ':whole_tone', ':yu', ':zhi']
chord_names = ['+5', '1', '11', '11+', '13', '5', '6', '6*9', '7', '7+5', '7+5-9', '7-10', '7-5', '7-9', '7sus2', '7sus4', '9', '9+5', '9sus4', ':M', ':M7', ':a', ':add11', ':add13', ':add2', ':add4', ':add9', ':augmented', ':dim', ':dim7', ':diminished', ':diminished7', ':dom7', ':i', ':i7', ':m', 'm+5', ':m11', ':m11+', ':m13', ':m6', ':m6*9', ':m7', 'm7+5', 'm7+5-9', 'm7+9', 'm7-5', 'm7-9', ':m9', 'm9+5', ':madd11', ':madd13', ':madd2', ':madd4', ':madd9', ':maj11', ':maj9', ':major', ':major7', ':minor', ':minor7', ':sus2', ':sus4']
degree_names = ['I','II','III','IV','V', 'VI','VII']