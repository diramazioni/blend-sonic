null = None; true = True; false = False;
#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/

lang_sound = {
  "all_sample_names": {
    "accepts_block": false,
    "introduced": "2,0,0",
    "memoize": true,
    "opts": null,
    "summary": "Get all sample names"
  },
  "chord": {
    "accepts_block": false,
    "args": {
      "name": ":symbol",
      "tonic": ":symbol"
    },
    "intro_fn": true,
    "introduced": "2,0,0",
    "memoize": true,
    "opts": {
      "num_octaves": 1
    },
    "returns": ":ring",
    "signature": {
      "*opts": null,
      "tonic_or_name": null
    },
    "summary": "Create chord"
  },
  "chord_degree": {
    "accepts_block": false,
    "args": {
      "degree": ":symbol_or_number",
      "number_of_notes": ":number",
      "scale": ":symbol",
      "tonic": ":symbol"
    },
    "introduced": "2,1,0",
    "memoize": true,
    "opts": null,
    "returns": ":ring",
    "signature": {
      "*opts": null,
      "degree": null,
      "number_of_notes": 4,
      "scale": ":major",
      "tonic": null
    },
    "summary": "Construct chords of stacked thirds, based on scale degrees"
  },
  "chord_invert": {
    "accepts_block": false,
    "args": {
      "notes": ":list",
      "shift": ":number"
    },
    "introduced": "2,6,0",
    "opts": null,
    "returns": ":ring",
    "signature": {
      "notes": null,
      "shift": null
    },
    "summary": "Chord inversion"
  },
  "chord_names": {
    "accepts_block": false,
    "introduced": "2,6,0",
    "memoize": true,
    "opts": null,
    "summary": "All chord names"
  },
  "control": {
    "accepts_block": false,
    "args": {
      "node": ":synth_node"
    },
    "introduced": "2,0,0",
    "opts": {},
    "signature": {
      "*args": null
    },
    "summary": "Control running synth"
  },
  "current_amp": {},
  "current_arg_checks": {
    "accepts_block": false,
    "introduced": "2,0,0",
    "opts": null,
    "summary": "Get current arg checking status"
  },
  "current_cent_tuning": {
    "accepts_block": false,
    "introduced": "2,9,0",
    "opts": null,
    "summary": "Get current cent shift"
  },
  "current_debug": {
    "accepts_block": false,
    "introduced": "2,0,0",
    "opts": null,
    "summary": "Get current debug status"
  },
  "current_octave": {
    "accepts_block": false,
    "introduced": "2,9,0",
    "opts": null,
    "summary": "Get current octave shift"
  },
  "current_sample_defaults": {
    "accepts_block": false,
    "introduced": "2,5,0",
    "opts": null,
    "summary": "Get current sample defaults"
  },
  "current_sched_ahead_time": {
    "accepts_block": false,
    "introduced": "2,0,0",
    "opts": null,
    "summary": "Get current sched ahead time"
  },
  "current_synth": {
    "accepts_block": false,
    "introduced": "2,0,0",
    "opts": null,
    "summary": "Get current synth"
  },
  "current_synth_defaults": {
    "accepts_block": false,
    "introduced": "2,0,0",
    "opts": null,
    "summary": "Get current synth defaults"
  },
  "current_transpose": {
    "accepts_block": false,
    "introduced": "2,0,0",
    "opts": null,
    "summary": "Get current transposition"
  },
  "current_volume": {
    "accepts_block": false,
    "introduced": "2,0,0",
    "opts": null,
    "summary": "Get current volume"
  },
  "degree": {
    "accepts_block": false,
    "args": {
      "degree": ":symbol_or_number",
      "scale": ":symbol",
      "tonic": ":symbol"
    },
    "introduced": "2,1,0",
    "signature": {
      "degree": null,
      "scale": null,
      "tonic": null
    },
    "summary": "Convert a degree into a note"
  },
  "fx_names": {
    "accepts_block": false,
    "introduced": "2,10,0",
    "memoize": true,
    "opts": null,
    "summary": "Get all FX names"
  },
  "hz_to_midi": {
    "accepts_block": false,
    "args": {
      "freq": ":number"
    },
    "introduced": "2,0,0",
    "opts": null,
    "signature": {
      "freq": null
    },
    "summary": "Hz to MIDI conversion"
  },
  "invert_chord": {
    "signature": {
      "*args": null
    }
  },
  "kill": {
    "accepts_block": false,
    "args": {
      "node": ":synth_node"
    },
    "introduced": "2,0,0",
    "opts": {},
    "signature": {
      "node": null
    },
    "summary": "Kill synth"
  },
  "load_sample": {
    "accepts_block": false,
    "args": {
      "path": ":string"
    },
    "introduced": "2,0,0",
    "opts": null,
    "signature": {
      "*args": null
    },
    "summary": "Pre-load first matching sample"
  },
  "load_sample_at_path": {
    "signature": {
      "path": null
    }
  },
  "load_samples": {
    "accepts_block": false,
    "args": {
      "paths": ":list"
    },
    "introduced": "2,0,0",
    "opts": null,
    "signature": {
      "*args": null
    },
    "summary": "Pre-load all matching samples"
  },
  "load_synthdefs": {
    "accepts_block": false,
    "args": {
      "path": ":string"
    },
    "introduced": "2,0,0",
    "opts": null,
    "signature": {
      "path": "synthdef_path"
    },
    "summary": "Load external synthdefs"
  },
  "midi_notes": {
    "accepts_block": false,
    "args": {
      "list": ":array"
    },
    "introduced": "2,7,0",
    "memoize": true,
    "opts": null,
    "returns": ":ring",
    "signature": {
      "*args": null
    },
    "summary": "Create a ring buffer of midi note numbers"
  },
  "midi_to_hz": {
    "accepts_block": false,
    "args": {
      "note": ":symbol_or_number"
    },
    "introduced": "2,0,0",
    "opts": null,
    "signature": {
      "n": null
    },
    "summary": "MIDI to Hz conversion"
  },
  "note": {
    "accepts_block": false,
    "args": {
      "note": ":symbol_or_number"
    },
    "introduced": "2,0,0",
    "opts": {
      "octave": 4
    },
    "signature": {
      "*args": null,
      "n": null
    },
    "summary": "Describe note"
  },
  "note_info": {
    "accepts_block": false,
    "args": {
      "note": ":symbol_or_number"
    },
    "introduced": "2,0,0",
    "opts": {
      "octave": 4
    },
    "signature": {
      "*args": null,
      "n": null
    },
    "summary": "Get note info"
  },
  "note_range": {
    "accepts_block": false,
    "args": {
      "high_note": ":note",
      "low_note": ":note"
    },
    "introduced": "2,6,0",
    "opts": {
      "pitches": []
    },
    "returns": ":ring",
    "signature": {
      "*opts": null,
      "high_note": null,
      "low_note": null
    },
    "summary": "Get a range of notes"
  },
  "octs": {
    "accepts_block": false,
    "args": {
      "num_octaves": ":pos_int",
      "start": ":note"
    },
    "introduced": "2,8,0",
    "opts": null,
    "returns": ":ring",
    "signature": {
      "num_octs": 1,
      "start": null
    },
    "summary": "Create a ring of octaves"
  },
  "pitch_ratio": {
    "signature": {
      "*args": null
    }
  },
  "pitch_to_ratio": {
    "accepts_block": false,
    "args": {
      "pitch": ":midi_number"
    },
    "introduced": "2,5,0",
    "opts": null,
    "signature": {
      "m": null
    },
    "summary": "relative MIDI pitch to frequency ratio"
  },
  "play": {
    "accepts_block": true,
    "args": {
      "note": ":symbol_or_number"
    },
    "intro_fn": true,
    "introduced": "2,0,0",
    "opts": {
      "amp": 1,
      "amp_slide": 1,
      "attack": 0,
      "attack_level": 1,
      "decay": 0,
      "decay_level": 1,
      "env_curve": 1,
      "on": 1,
      "pan": 0,
      "pan_slide": 1,
      "pitch": 0,
      "release": 0,
      "slide": 0,
      "sustain": 1,
      "sustain_level": 1
    },
    "signature": {
      "&blk": null,
      "*args": null,
      "n": null
    },
    "summary": "Play current synth"
  },
  "play_chord": {
    "accepts_block": false,
    "args": {
      "notes": ":list"
    },
    "introduced": "2,0,0",
    "opts": {
      "amp": 1,
      "amp_slide": 1,
      "attack": 0,
      "attack_level": 1,
      "decay": 0,
      "decay_level": 1,
      "env_curve": 1,
      "on": 1,
      "pan": 0,
      "pan_slide": 1,
      "pitch": 0,
      "release": 0,
      "slide": 0,
      "sustain": 1,
      "sustain_level": 1
    },
    "signature": {
      "*args": null,
      "notes": null
    },
    "summary": "Play notes simultaneously"
  },
  "play_pattern": {
    "accepts_block": false,
    "args": {
      "notes": ":list"
    },
    "introduced": "2,0,0",
    "opts": {},
    "signature": {
      "*args": null,
      "notes": null
    },
    "summary": "Play pattern of notes"
  },
  "play_pattern_timed": {
    "accepts_block": false,
    "args": {
      "notes": ":list",
      "times": ":list_or_number"
    },
    "introduced": "2,0,0",
    "opts": {
      "amp": 1,
      "amp_slide": 1,
      "attack": 0,
      "attack_level": 1,
      "decay": 0,
      "decay_level": 1,
      "env_curve": 1,
      "on": 1,
      "pan": 0,
      "pan_slide": 1,
      "pitch": 0,
      "release": 0,
      "slide": 0,
      "sustain": 1,
      "sustain_level": 1
    },
    "signature": {
      "*args": null,
      "notes": null,
      "times": null
    },
    "summary": "Play pattern of notes with specific times"
  },
  "ratio_to_pitch": {
    "accepts_block": false,
    "args": {
      "ratio": ":number"
    },
    "introduced": "2,7,0",
    "opts": null,
    "signature": {
      "r": null
    },
    "summary": "relative frequency ratio to MIDI pitch"
  },
  "recording_delete": {
    "accepts_block": false,
    "hide": true,
    "opts": null
  },
  "recording_save": {
    "accepts_block": false,
    "args": {
      "path": ":string"
    },
    "hide": true,
    "introduced": "2,0,0",
    "opts": null,
    "signature": {
      "filename": null
    },
    "summary": "Save recording"
  },
  "recording_start": {
    "accepts_block": false,
    "hide": true,
    "introduced": "2,0,0",
    "opts": null,
    "summary": "Start recording"
  },
  "recording_stop": {
    "accepts_block": false,
    "hide": true,
    "introduced": "2,0,0",
    "opts": null,
    "summary": "Stop recording"
  },
  "reset_mixer!": {
    "accepts_block": false,
    "introduced": "2,9,0",
    "opts": {},
    "signature": {
      "": null
    },
    "summary": "Reset master mixer"
  },
  "resolve_sample_path": {
    "signature": {
      "filts_and_sources": null
    }
  },
  "resolve_sample_paths": {
    "signature": {
      "filts_and_sources": null
    }
  },
  "rest?": {
    "accepts_block": false,
    "args": {
      "note_or_args": ":number_symbol_or_map"
    },
    "introduced": "2,1,0",
    "signature": {
      "n": null
    },
    "summary": "Determine if note or args is a rest"
  },
  "sample": {
    "accepts_block": true,
    "args": {
      "name_or_path": ":symbol_or_string"
    },
    "intro_fn": true,
    "introduced": "2,0,0",
    "opts": {
      "path": "String"
    },
    "signature": {
      "&blk": null,
      "*args": null
    },
    "summary": "Trigger sample"
  },
  "sample_buffer": {
    "accepts_block": false,
    "args": {
      "path": ":string"
    },
    "introduced": "2,0,0",
    "opts": null,
    "signature": {
      "*args": null
    },
    "summary": "Get sample data"
  },
  "sample_duration": {
    "accepts_block": false,
    "args": {
      "path": ":string"
    },
    "introduced": "2,0,0",
    "opts": {
      "rpitch": 0
    },
    "signature": {
      "*args": null
    },
    "summary": "Get duration of sample in beats"
  },
  "sample_free": {
    "accepts_block": false,
    "args": {
      "path": ":string"
    },
    "introduced": "2,9,0",
    "opts": null,
    "returns": null,
    "signature": {
      "*paths": null
    },
    "summary": "Free a sample on the synth server"
  },
  "sample_free_all": {
    "accepts_block": false,
    "args": {},
    "introduced": "2,9,0",
    "opts": null,
    "returns": null,
    "summary": "Free all loaded samples on the synth server"
  },
  "sample_groups": {
    "accepts_block": false,
    "introduced": "2,0,0",
    "memoize": true,
    "opts": null,
    "summary": "Get all sample groups"
  },
  "sample_info": {
    "accepts_block": false,
    "args": {
      "path": ":string"
    },
    "introduced": "2,0,0",
    "opts": null,
    "signature": {
      "*args": null
    },
    "summary": "Get sample information"
  },
  "sample_loaded?": {
    "accepts_block": false,
    "args": {
      "path": ":string"
    },
    "introduced": "2,2,0",
    "opts": null,
    "signature": {
      "*args": null
    },
    "summary": "Test if sample was pre-loaded"
  },
  "sample_names": {
    "accepts_block": false,
    "args": {
      "group": ":symbol"
    },
    "introduced": "2,0,0",
    "memoize": true,
    "opts": null,
    "returns": ":ring",
    "signature": {
      "group": null
    },
    "summary": "Get sample names"
  },
  "sample_paths": {
    "accepts_block": false,
    "args": {
      "pre_args": ":source_and_filter_types"
    },
    "introduced": "2,10,0",
    "opts": null,
    "returns": ":ring",
    "signature": {
      "*args": null
    },
    "summary": "Sample Pack Filter Resolution"
  },
  "sample_split_filts_and_opts": {
    "signature": {
      "args": null
    }
  },
  "scale": {
    "accepts_block": false,
    "args": {
      "name": ":symbol",
      "tonic": ":symbol"
    },
    "intro_fn": true,
    "introduced": "2,0,0",
    "memoize": true,
    "opts": {
      "num_octaves": 1
    },
    "returns": ":ring",
    "signature": {
      "*opts": null,
      "tonic_or_name": null
    },
    "summary": "Create scale"
  },
  "scale_names": {
    "accepts_block": false,
    "introduced": "2,6,0",
    "memoize": true,
    "opts": null,
    "summary": "All scale names"
  },
  "set_cent_tuning!": {
    "accepts_block": false,
    "args": {
      "cent_shift": ":number"
    },
    "intro_fn": false,
    "introduced": "2,10,0",
    "opts": null,
    "signature": {
      "shift": null
    },
    "summary": "Global Cent tuning"
  },
  "set_control_delta!": {
    "accepts_block": false,
    "args": {
      "time": ":number"
    },
    "introduced": "2,1,0",
    "modifies_env": true,
    "opts": null,
    "signature": {
      "t": null
    },
    "summary": "Set control delta globally"
  },
  "set_mixer_control!": {
    "accepts_block": false,
    "introduced": "2,7,0",
    "opts": {
      "leak_dc_bypass": 0
    },
    "signature": {
      "opts": null
    },
    "summary": "Control master mixer"
  },
  "set_mixer_invert_stereo!": {},
  "set_mixer_mono_mode!": {},
  "set_mixer_standard_stereo!": {},
  "set_mixer_stereo_mode!": {},
  "set_sched_ahead_time!": {
    "accepts_block": false,
    "args": {
      "time": ":number"
    },
    "introduced": "2,0,0",
    "modifies_env": true,
    "opts": null,
    "signature": {
      "t": null
    },
    "summary": "Set sched ahead time globally"
  },
  "set_volume!": {
    "accepts_block": false,
    "args": {
      "vol": ":number"
    },
    "introduced": "2,0,0",
    "modifies_env": true,
    "opts": null,
    "signature": {
      "vol": null
    },
    "summary": "Set Volume globally"
  },
  "should_trigger?": {
    "signature": {
      "args_h": null
    }
  },
  "start_amp_monitor": {},
  "status": {
    "accepts_block": false,
    "introduced": "2,0,0",
    "opts": null,
    "summary": "Get server status"
  },
  "synth": {
    "accepts_block": true,
    "args": {
      "synth_name": ":symbol"
    },
    "introduced": "2,0,0",
    "opts": {
      "amp": 1,
      "amp_slide": 1,
      "attack": 0,
      "attack_level": 1,
      "decay": 0,
      "decay_level": 1,
      "env_curve": 1,
      "on": 1,
      "pan": 0,
      "pan_slide": 1,
      "pitch": 0,
      "release": 0,
      "slide": 0,
      "sustain": 1,
      "sustain_level": 1
    },
    "signature": {
      "&blk": null,
      "*args": null,
      "synth_name": null
    },
    "summary": "Trigger specific synth"
  },
  "synth_names": {
    "accepts_block": false,
    "introduced": "2,9,0",
    "memoize": true,
    "opts": null,
    "summary": "Get all synth names"
  },
  "truthy?": {
    "signature": {
      "val": null
    }
  },
  "use_arg_bpm_scaling": {
    "accepts_block": false,
    "args": {
      "bool": ":boolean"
    },
    "introduced": "2,0,0",
    "opts": null,
    "signature": {
      "&block": null,
      "bool": null
    },
    "summary": "Enable and disable BPM scaling"
  },
  "use_arg_checks": {
    "accepts_block": false,
    "args": {
      "true_or_false": ":boolean"
    },
    "introduced": "2,0,0",
    "opts": null,
    "signature": {
      "&block": null,
      "v": null
    },
    "summary": "Enable and disable arg checks"
  },
  "use_cent_tuning": {
    "accepts_block": false,
    "args": {
      "cent_shift": ":number"
    },
    "intro_fn": true,
    "introduced": "2,9,0",
    "opts": null,
    "signature": {
      "&block": null,
      "shift": null
    },
    "summary": "Cent tuning"
  },
  "use_debug": {
    "accepts_block": false,
    "args": {
      "true_or_false": ":boolean"
    },
    "introduced": "2,0,0",
    "opts": null,
    "signature": {
      "&block": null,
      "v": null
    },
    "summary": "Enable and disable debug"
  },
  "use_external_synths": {
    "signature": {
      "&block": null,
      "v": null
    }
  },
  "use_fx": {
    "signature": {
      "&block": null,
      "*args": null
    }
  },
  "use_merged_sample_defaults": {
    "accepts_block": false,
    "introduced": "2,9,0",
    "opts": {},
    "signature": {
      "&block": null,
      "*args": null
    },
    "summary": "Merge new sample defaults"
  },
  "use_merged_synth_defaults": {
    "accepts_block": false,
    "introduced": "2,0,0",
    "opts": {},
    "signature": {
      "&block": null,
      "*args": null
    },
    "summary": "Merge synth defaults"
  },
  "use_octave": {
    "accepts_block": false,
    "args": {
      "octave_shift": ":number"
    },
    "intro_fn": true,
    "introduced": "2,9,0",
    "opts": null,
    "signature": {
      "&block": null,
      "shift": null
    },
    "summary": "Note octave transposition"
  },
  "use_sample_bpm": {
    "accepts_block": false,
    "args": {
      "string_or_number": ":sample_name_or_duration"
    },
    "introduced": "2,1,0",
    "opts": {
      "num_beats": 1
    },
    "signature": {
      "*args": null,
      "sample_name": null
    },
    "summary": "Sample-duration-based bpm modification"
  },
  "use_sample_defaults": {
    "accepts_block": false,
    "introduced": "2,5,0",
    "opts": {},
    "signature": {
      "&block": null,
      "*args": null
    },
    "summary": "Use new sample defaults"
  },
  "use_synth": {
    "accepts_block": false,
    "args": {
      "synth_name": ":symbol"
    },
    "intro_fn": true,
    "introduced": "2,0,0",
    "opts": null,
    "signature": {
      "&block": null,
      "*args": null,
      "synth_name": null
    },
    "summary": "Switch current synth"
  },
  "use_synth_defaults": {
    "accepts_block": false,
    "introduced": "2,0,0",
    "opts": {},
    "signature": {
      "&block": null,
      "*args": null
    },
    "summary": "Use new synth defaults"
  },
  "use_timing_guarantees": {
    "accepts_block": true,
    "args": {
      "bool": ":true_or_false"
    },
    "introduced": "2,10,0",
    "opts": null,
    "signature": {
      "&block": null,
      "v": null
    },
    "summary": "Inhibit synth triggers if too late"
  },
  "use_timing_warnings": {
    "signature": {
      "&block": null,
      "v": null
    }
  },
  "use_transpose": {
    "accepts_block": false,
    "args": {
      "note_shift": ":number"
    },
    "intro_fn": true,
    "introduced": "2,0,0",
    "opts": null,
    "signature": {
      "&block": null,
      "shift": null
    },
    "summary": "Note transposition"
  },
  "use_tuning": {
    "accepts_block": false,
    "args": {
      "fundamental_note": ":symbol_or_number",
      "tuning": ":symbol"
    },
    "introduced": "2,6,0",
    "opts": null,
    "signature": {
      "&block": null,
      "fundamental_note": ":c",
      "tuning": null
    },
    "summary": "Use alternative tuning systems"
  },
  "with_afx": {
    "signature": {
      "&block": null,
      "*args": null,
      "fx_name": null
    }
  },
  "with_arg_bpm_scaling": {
    "accepts_block": true,
    "introduced": "2,0,0",
    "opts": null,
    "requires_block": true,
    "signature": {
      "&block": null,
      "bool": null
    },
    "summary": "Block-level enable and disable BPM scaling"
  },
  "with_arg_checks": {
    "accepts_block": true,
    "args": {
      "true_or_false": ":boolean"
    },
    "introduced": "2,0,0",
    "opts": null,
    "requires_block": true,
    "signature": {
      "&block": null,
      "v": null
    },
    "summary": "Block-level enable and disable arg checks"
  },
  "with_cent_tuning": {
    "accepts_block": true,
    "args": {
      "cent_shift": ":number"
    },
    "introduced": "2,9,0",
    "opts": null,
    "requires_block": true,
    "signature": {
      "&block": null,
      "shift": null
    },
    "summary": "Block-level cent tuning"
  },
  "with_debug": {
    "accepts_block": true,
    "args": {
      "true_or_false": ":boolean"
    },
    "introduced": "2,0,0",
    "opts": null,
    "requires_block": true,
    "signature": {
      "&block": null,
      "v": null
    },
    "summary": "Block-level enable and disable debug"
  },
  "with_fx": {
    "accepts_block": true,
    "args": {
      "fx_name": ":symbol"
    },
    "intro_fn": true,
    "introduced": "2,0,0",
    "opts": {
      "kill_delay": 1
    },
    "requires_block": true,
    "signature": {
      "&block": null,
      "*args": null,
      "fx_name": null
    },
    "summary": "Use Studio FX"
  },
  "with_merged_sample_defaults": {
    "accepts_block": false,
    "introduced": "2,9,0",
    "opts": {},
    "requires_block": false,
    "signature": {
      "&block": null,
      "*args": null
    },
    "summary": "Block-level use merged sample defaults"
  },
  "with_merged_synth_defaults": {
    "accepts_block": true,
    "introduced": "2,0,0",
    "opts": {},
    "requires_block": true,
    "signature": {
      "&block": null,
      "*args": null
    },
    "summary": "Block-level merge synth defaults"
  },
  "with_octave": {
    "accepts_block": true,
    "args": {
      "octave_shift": ":number"
    },
    "intro_fn": true,
    "introduced": "2,9,0",
    "opts": null,
    "signature": {
      "&block": null,
      "shift": null
    },
    "summary": "Block level octave transposition"
  },
  "with_sample_bpm": {
    "accepts_block": true,
    "args": {
      "string_or_number": ":sample_name_or_duration"
    },
    "introduced": "2,1,0",
    "opts": {
      "num_beats": 1
    },
    "requires_block": true,
    "signature": {
      "&block": null,
      "*args": null,
      "sample_name": null
    },
    "summary": "Block-scoped sample-duration-based bpm modification"
  },
  "with_sample_defaults": {
    "accepts_block": false,
    "introduced": "2,5,0",
    "opts": {},
    "requires_block": false,
    "signature": {
      "&block": null,
      "*args": null
    },
    "summary": "Block-level use new sample defaults"
  },
  "with_synth": {
    "accepts_block": true,
    "args": {
      "synth_name": ":symbol"
    },
    "introduced": "2,0,0",
    "opts": null,
    "requires_block": true,
    "signature": {
      "&block": null,
      "*args": null,
      "synth_name": null
    },
    "summary": "Block-level synth switching"
  },
  "with_synth_defaults": {
    "accepts_block": true,
    "introduced": "2,0,0",
    "opts": {},
    "requires_block": true,
    "signature": {
      "&block": null,
      "*args": null
    },
    "summary": "Block-level use new synth defaults"
  },
  "with_timing_guarantees": {
    "accepts_block": true,
    "args": {
      "bool": ":true_or_false"
    },
    "introduced": "2,10,0",
    "opts": null,
    "signature": {
      "&block": null,
      "v": null
    },
    "summary": "Block-scoped inhibition of synth triggers if too late"
  },
  "with_timing_warnings": {
    "signature": {
      "&block": null,
      "v": null
    }
  },
  "with_transpose": {
    "accepts_block": true,
    "args": {
      "note_shift": ":number"
    },
    "introduced": "2,0,0",
    "opts": null,
    "requires_block": true,
    "signature": {
      "&block": null,
      "shift": null
    },
    "summary": "Block-level note transposition"
  },
  "with_tuning": {
    "accepts_block": true,
    "args": {
      "fundamental_note": ":symbol_or_number",
      "tuning": ":symbol"
    },
    "introduced": "2,6,0",
    "opts": null,
    "signature": {
      "&block": null,
      "fundamental_note": ":c",
      "tuning": null
    },
    "summary": "Block-level tuning modification"
  }
}
