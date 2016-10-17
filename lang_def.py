null = None; true = True; false = False;
#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/

lang_sound = {
  "chord": {
    "accepts_block": false,
    "args_in": {
      "*opts": null,
      "tonic_or_name": null
    },
    "args_types": {
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
    "summary": "Create chord"
  },
  "chord_degree": {
    "accepts_block": false,
    "args_in": {
      "*opts": null,
      "degree": null,
      "number_of_notes": 4,
      "scale": ":major",
      "tonic": null
    },
    "args_types": {
      "degree": ":symbol_or_number",
      "number_of_notes": ":number",
      "scale": ":symbol",
      "tonic": ":symbol"
    },
    "introduced": "2,1,0",
    "memoize": true,
    "opts": null,
    "returns": ":ring",
    "summary": "Construct chords of stacked thirds, based on scale degrees"
  },
  "chord_invert": {
    "accepts_block": false,
    "args_in": {
      "notes": null,
      "shift": null
    },
    "args_types": {
      "notes": ":list",
      "shift": ":number"
    },
    "introduced": "2,6,0",
    "opts": null,
    "returns": ":ring",
    "summary": "Chord inversion"
  },
  "chord_names": {
    "accepts_block": false,
    "args_types": {},
    "introduced": "2,6,0",
    "memoize": true,
    "opts": null,
    "summary": "All chord names"
  },
  "control": {
    "accepts_block": false,
    "args_in": {
      "*args": null
    },
    "args_types": {
      "node": ":synth_node"
    },
    "introduced": "2,0,0",
    "opts": {},
    "summary": "Control running synth"
  },
  "current_amp": {},
  "current_arg_checks": {
    "accepts_block": false,
    "args_types": {},
    "introduced": "2,0,0",
    "opts": null,
    "summary": "Get current arg checking status"
  },
  "current_cent_tuning": {
    "accepts_block": false,
    "args_types": {},
    "introduced": "2,9,0",
    "opts": null,
    "summary": "Get current cent shift"
  },
  "current_debug": {
    "accepts_block": false,
    "args_types": {},
    "introduced": "2,0,0",
    "opts": null,
    "summary": "Get current debug status"
  },
  "current_octave": {
    "accepts_block": false,
    "args_types": {},
    "introduced": "2,9,0",
    "opts": null,
    "summary": "Get current octave shift"
  },
  "current_sample_defaults": {
    "accepts_block": false,
    "args_types": {},
    "introduced": "2,5,0",
    "opts": null,
    "summary": "Get current sample defaults"
  },
  "current_sched_ahead_time": {
    "accepts_block": false,
    "args_types": {},
    "introduced": "2,0,0",
    "opts": null,
    "summary": "Get current sched ahead time"
  },
  "current_synth": {
    "accepts_block": false,
    "args_types": {},
    "introduced": "2,0,0",
    "opts": null,
    "summary": "Get current synth"
  },
  "current_synth_defaults": {
    "accepts_block": false,
    "args_types": {},
    "introduced": "2,0,0",
    "opts": null,
    "summary": "Get current synth defaults"
  },
  "current_transpose": {
    "accepts_block": false,
    "args_types": {},
    "introduced": "2,0,0",
    "opts": null,
    "summary": "Get current transposition"
  },
  "current_volume": {
    "accepts_block": false,
    "args_types": {},
    "introduced": "2,0,0",
    "opts": null,
    "summary": "Get current volume"
  },
  "hz_to_midi": {
    "accepts_block": false,
    "args_in": {
      "freq": null
    },
    "args_types": {
      "freq": ":number"
    },
    "introduced": "2,0,0",
    "opts": null,
    "summary": "Hz to MIDI conversion"
  },
  "invert_chord": {
    "args_in": {
      "*args": null
    }
  },
  "kill": {
    "accepts_block": false,
    "args_in": {
      "node": null
    },
    "args_types": {
      "node": ":synth_node"
    },
    "introduced": "2,0,0",
    "opts": {},
    "summary": "Kill synth"
  },
  "load_sample": {
    "accepts_block": false,
    "args_in": {
      "*args": null
    },
    "args_types": {
      "path": ":string"
    },
    "introduced": "2,0,0",
    "opts": null,
    "summary": "Pre-load first matching sample"
  },
  "load_sample_at_path": {
    "args_in": {
      "path": null
    }
  },
  "midi_notes": {
    "accepts_block": false,
    "args_in": {
      "*args": null
    },
    "args_types": {
      "list": ":array"
    },
    "introduced": "2,7,0",
    "memoize": true,
    "opts": null,
    "returns": ":ring",
    "summary": "Create a ring buffer of midi note numbers"
  },
  "midi_to_hz": {
    "accepts_block": false,
    "args_in": {
      "n": null
    },
    "args_types": {
      "note": ":symbol_or_number"
    },
    "introduced": "2,0,0",
    "opts": null,
    "summary": "MIDI to Hz conversion"
  },
  "note": {
    "accepts_block": false,
    "args_in": {
      "*args": null,
      "n": null
    },
    "args_types": {
      "note": ":symbol_or_number"
    },
    "introduced": "2,0,0",
    "opts": {
      "octave": 4
    },
    "summary": "Describe note"
  },
  "note_info": {
    "accepts_block": false,
    "args_in": {
      "*args": null,
      "n": null
    },
    "args_types": {
      "note": ":symbol_or_number"
    },
    "intro_fn": true,
    "introduced": "2,0,0",
    "memoize": true,
    "opts": {
      "num_octaves": 1
    },
    "returns": ":ring",
    "summary": "Get note info"
  },
  "note_range": {
    "accepts_block": false,
    "args_in": {
      "*opts": null,
      "high_note": null,
      "low_note": null
    },
    "args_types": {
      "high_note": ":note",
      "low_note": ":note"
    },
    "introduced": "2,6,0",
    "opts": {
      "pitches": []
    },
    "returns": ":ring",
    "summary": "Get a range of notes"
  },
  "octs": {
    "accepts_block": false,
    "args_in": {
      "num_octs": 1,
      "start": null
    },
    "args_types": {
      "num_octaves": ":pos_int",
      "start": ":note"
    },
    "introduced": "2,8,0",
    "opts": null,
    "returns": ":ring",
    "summary": "Create a ring of octaves"
  },
  "pitch_ratio": {
    "args_in": {
      "*args": null
    }
  },
  "pitch_to_ratio": {
    "accepts_block": false,
    "args_in": {
      "m": null
    },
    "args_types": {
      "pitch": ":midi_number"
    },
    "introduced": "2,5,0",
    "opts": null,
    "summary": "relative MIDI pitch to frequency ratio"
  },
  "play": {
    "accepts_block": true,
    "args_in": {
      "&blk": null,
      "*args": null,
      "n": null
    },
    "args_types": {
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
    "summary": "Play current synth"
  },
  "play_chord": {
    "accepts_block": false,
    "args_in": {
      "*args": null,
      "notes": null
    },
    "args_types": {
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
    "summary": "Play notes simultaneously"
  },
  "play_pattern": {
    "accepts_block": false,
    "args_in": {
      "*args": null,
      "notes": null
    },
    "args_types": {
      "notes": ":list"
    },
    "introduced": "2,0,0",
    "opts": {},
    "summary": "Play pattern of notes"
  },
  "play_pattern_timed": {
    "accepts_block": false,
    "args_in": {
      "*args": null,
      "notes": null,
      "times": null
    },
    "args_types": {
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
    "summary": "Play pattern of notes with specific times"
  },
  "ratio_to_pitch": {
    "accepts_block": false,
    "args_in": {
      "r": null
    },
    "args_types": {
      "ratio": ":number"
    },
    "introduced": "2,7,0",
    "opts": null,
    "summary": "relative frequency ratio to MIDI pitch"
  },
  "recording_delete": {
    "accepts_block": false,
    "args_types": {},
    "hide": true,
    "opts": null
  },
  "recording_save": {
    "accepts_block": false,
    "args_in": {
      "filename": null
    },
    "args_types": {
      "path": ":string"
    },
    "hide": true,
    "introduced": "2,0,0",
    "opts": null,
    "summary": "Save recording"
  },
  "recording_start": {
    "accepts_block": false,
    "args_types": {},
    "hide": true,
    "introduced": "2,0,0",
    "opts": null,
    "summary": "Start recording"
  },
  "recording_stop": {
    "accepts_block": false,
    "args_types": {},
    "hide": true,
    "introduced": "2,0,0",
    "opts": null,
    "summary": "Stop recording"
  },
  "reset_mixer!": {
    "accepts_block": false,
    "args_in": {
      "": null
    },
    "args_types": {},
    "introduced": "2,9,0",
    "opts": {},
    "summary": "Reset master mixer"
  },
  "resolve_sample_path": {
    "args_in": {
      "filts_and_sources": null
    }
  },
  "resolve_sample_paths": {
    "args_in": {
      "filts_and_sources": null
    }
  },
  "rest?": {
    "accepts_block": false,
    "args_in": {
      "n": null
    },
    "args_types": {
      "note_or_args": ":number_symbol_or_map"
    },
    "introduced": "2,1,0",
    "summary": "Determine if note or args is a rest"
  },
  "sample": {
    "accepts_block": true,
    "args_in": {
      "&blk": null,
      "*args": null
    },
    "args_types": {
      "name_or_path": ":symbol_or_string"
    },
    "intro_fn": true,
    "introduced": "2,0,0",
    "opts": {
      "path": "String"
    },
    "summary": "Trigger sample"
  },
  "sample_buffer": {
    "accepts_block": false,
    "args_in": {
      "*args": null
    },
    "args_types": {
      "path": ":string"
    },
    "introduced": "2,0,0",
    "opts": null,
    "summary": "Get sample data"
  },
  "sample_duration": {
    "accepts_block": false,
    "args_in": {
      "*args": null
    },
    "args_types": {
      "path": ":string"
    },
    "introduced": "2,0,0",
    "opts": {
      "rpitch": 0
    },
    "summary": "Get duration of sample in beats"
  },
  "sample_free": {
    "accepts_block": false,
    "args_in": {
      "*paths": null
    },
    "args_types": {
      "path": ":string"
    },
    "introduced": "2,9,0",
    "opts": null,
    "returns": null,
    "summary": "Free a sample on the synth server"
  },
  "sample_free_all": {
    "accepts_block": false,
    "args_types": {},
    "introduced": "2,9,0",
    "opts": null,
    "returns": null,
    "summary": "Free all loaded samples on the synth server"
  },
  "sample_info": {
    "accepts_block": false,
    "args_in": {
      "*args": null
    },
    "args_types": {
      "path": ":string"
    },
    "introduced": "2,0,0",
    "opts": null,
    "summary": "Get sample information"
  },
  "sample_loaded?": {
    "accepts_block": false,
    "args_in": {
      "*args": null
    },
    "args_types": {
      "path": ":string"
    },
    "introduced": "2,2,0",
    "opts": null,
    "summary": "Test if sample was pre-loaded"
  },
  "sample_names": {
    "accepts_block": false,
    "args_in": {
      "group": null
    },
    "args_types": {
      "group": ":symbol"
    },
    "introduced": "2,0,0",
    "memoize": true,
    "opts": null,
    "returns": ":ring",
    "summary": "Get sample names"
  },
  "sample_paths": {
    "accepts_block": false,
    "args_in": {
      "*args": null
    },
    "args_types": {
      "pre_args": ":source_and_filter_types"
    },
    "introduced": "2,10,0",
    "opts": null,
    "returns": ":ring",
    "summary": "Sample Pack Filter Resolution"
  },
  "sample_split_filts_and_opts": {
    "args_in": {
      "args": null
    }
  },
  "scale_names": {
    "accepts_block": false,
    "args_types": {},
    "introduced": "2,6,0",
    "memoize": true,
    "opts": null,
    "summary": "All scale names"
  },
  "set_cent_tuning!": {
    "accepts_block": false,
    "args_in": {
      "shift": null
    },
    "args_types": {
      "cent_shift": ":number"
    },
    "intro_fn": false,
    "introduced": "2,10,0",
    "opts": null,
    "summary": "Global Cent tuning"
  },
  "set_control_delta!": {
    "accepts_block": false,
    "args_in": {
      "t": null
    },
    "args_types": {
      "time": ":number"
    },
    "introduced": "2,1,0",
    "modifies_env": true,
    "opts": null,
    "summary": "Set control delta globally"
  },
  "set_mixer_control!": {
    "accepts_block": false,
    "args_in": {
      "opts": null
    },
    "args_types": {},
    "introduced": "2,7,0",
    "opts": {
      "leak_dc_bypass": 0
    },
    "summary": "Control master mixer"
  },
  "set_mixer_invert_stereo!": {},
  "set_mixer_mono_mode!": {},
  "set_mixer_standard_stereo!": {},
  "set_mixer_stereo_mode!": {},
  "set_sched_ahead_time!": {
    "accepts_block": false,
    "args_in": {
      "t": null
    },
    "args_types": {
      "time": ":number"
    },
    "introduced": "2,0,0",
    "modifies_env": true,
    "opts": null,
    "summary": "Set sched ahead time globally"
  },
  "set_volume!": {
    "accepts_block": false,
    "args_in": {
      "vol": null
    },
    "args_types": {
      "vol": ":number"
    },
    "introduced": "2,0,0",
    "modifies_env": true,
    "opts": null,
    "summary": "Set Volume globally"
  },
  "should_trigger?": {
    "args_in": {
      "args_h": null
    }
  },
  "start_amp_monitor": {},
  "status": {
    "accepts_block": false,
    "args_types": {},
    "introduced": "2,0,0",
    "opts": null,
    "summary": "Get server status"
  },
  "synth": {
    "accepts_block": true,
    "args_in": {
      "&blk": null,
      "*args": null,
      "synth_name": null
    },
    "args_types": {
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
    "summary": "Trigger specific synth"
  },
  "truthy?": {
    "args_in": {
      "val": null
    }
  },
  "use_arg_bpm_scaling": {
    "accepts_block": false,
    "args_in": {
      "&block": null,
      "bool": null
    },
    "args_types": {
      "bool": ":boolean"
    },
    "introduced": "2,0,0",
    "opts": null,
    "summary": "Enable and disable BPM scaling"
  },
  "use_arg_checks": {
    "accepts_block": false,
    "args_in": {
      "&block": null,
      "v": null
    },
    "args_types": {
      "true_or_false": ":boolean"
    },
    "introduced": "2,0,0",
    "opts": null,
    "summary": "Enable and disable arg checks"
  },
  "use_cent_tuning": {
    "accepts_block": false,
    "args_in": {
      "&block": null,
      "shift": null
    },
    "args_types": {
      "cent_shift": ":number"
    },
    "intro_fn": true,
    "introduced": "2,9,0",
    "opts": null,
    "summary": "Cent tuning"
  },
  "use_debug": {
    "accepts_block": false,
    "args_in": {
      "&block": null,
      "v": null
    },
    "args_types": {
      "true_or_false": ":boolean"
    },
    "introduced": "2,0,0",
    "opts": null,
    "summary": "Enable and disable debug"
  },
  "use_external_synths": {
    "args_in": {
      "&block": null,
      "v": null
    }
  },
  "use_fx": {
    "args_in": {
      "&block": null,
      "*args": null
    }
  },
  "use_merged_sample_defaults": {
    "accepts_block": false,
    "args_in": {
      "&block": null,
      "*args": null
    },
    "args_types": {},
    "introduced": "2,9,0",
    "opts": {},
    "summary": "Merge new sample defaults"
  },
  "use_merged_synth_defaults": {
    "accepts_block": false,
    "args_in": {
      "&block": null,
      "*args": null
    },
    "args_types": {},
    "introduced": "2,0,0",
    "opts": {},
    "summary": "Merge synth defaults"
  },
  "use_octave": {
    "accepts_block": false,
    "args_in": {
      "&block": null,
      "shift": null
    },
    "args_types": {
      "octave_shift": ":number"
    },
    "intro_fn": true,
    "introduced": "2,9,0",
    "opts": null,
    "summary": "Note octave transposition"
  },
  "use_sample_bpm": {
    "accepts_block": false,
    "args_in": {
      "*args": null,
      "sample_name": null
    },
    "args_types": {
      "string_or_number": ":sample_name_or_duration"
    },
    "introduced": "2,1,0",
    "opts": {
      "num_beats": 1
    },
    "summary": "Sample-duration-based bpm modification"
  },
  "use_sample_defaults": {
    "accepts_block": false,
    "args_in": {
      "&block": null,
      "*args": null
    },
    "args_types": {},
    "introduced": "2,5,0",
    "opts": {},
    "summary": "Use new sample defaults"
  },
  "use_synth": {
    "accepts_block": false,
    "args_in": {
      "&block": null,
      "*args": null,
      "synth_name": null
    },
    "args_types": {
      "synth_name": ":symbol"
    },
    "intro_fn": true,
    "introduced": "2,0,0",
    "opts": null,
    "summary": "Switch current synth"
  },
  "use_synth_defaults": {
    "accepts_block": false,
    "args_in": {
      "&block": null,
      "*args": null
    },
    "args_types": {},
    "introduced": "2,0,0",
    "opts": {},
    "summary": "Use new synth defaults"
  },
  "use_timing_guarantees": {
    "accepts_block": true,
    "args_in": {
      "&block": null,
      "v": null
    },
    "args_types": {
      "bool": ":true_or_false"
    },
    "introduced": "2,10,0",
    "opts": null,
    "summary": "Inhibit synth triggers if too late"
  },
  "use_timing_warnings": {
    "args_in": {
      "&block": null,
      "v": null
    }
  },
  "use_transpose": {
    "accepts_block": false,
    "args_in": {
      "&block": null,
      "shift": null
    },
    "args_types": {
      "note_shift": ":number"
    },
    "intro_fn": true,
    "introduced": "2,0,0",
    "opts": null,
    "summary": "Note transposition"
  },
  "use_tuning": {
    "accepts_block": false,
    "args_in": {
      "&block": null,
      "fundamental_note": ":c",
      "tuning": null
    },
    "args_types": {
      "fundamental_note": ":symbol_or_number",
      "tuning": ":symbol"
    },
    "introduced": "2,6,0",
    "opts": null,
    "summary": "Use alternative tuning systems"
  },
  "with_afx": {
    "args_in": {
      "&block": null,
      "*args": null,
      "fx_name": null
    }
  },
  "with_arg_bpm_scaling": {
    "accepts_block": true,
    "args_in": {
      "&block": null,
      "bool": null
    },
    "args_types": {},
    "introduced": "2,0,0",
    "opts": null,
    "requires_block": true,
    "summary": "Block-level enable and disable BPM scaling"
  },
  "with_arg_checks": {
    "accepts_block": true,
    "args_in": {
      "&block": null,
      "v": null
    },
    "args_types": {
      "true_or_false": ":boolean"
    },
    "introduced": "2,0,0",
    "opts": null,
    "requires_block": true,
    "summary": "Block-level enable and disable arg checks"
  },
  "with_cent_tuning": {
    "accepts_block": true,
    "args_in": {
      "&block": null,
      "shift": null
    },
    "args_types": {
      "cent_shift": ":number"
    },
    "introduced": "2,9,0",
    "opts": null,
    "requires_block": true,
    "summary": "Block-level cent tuning"
  },
  "with_debug": {
    "accepts_block": true,
    "args_in": {
      "&block": null,
      "v": null
    },
    "args_types": {
      "true_or_false": ":boolean"
    },
    "introduced": "2,0,0",
    "opts": null,
    "requires_block": true,
    "summary": "Block-level enable and disable debug"
  },
  "with_fx": {
    "accepts_block": true,
    "args_in": {
      "&block": null,
      "*args": null,
      "fx_name": null
    },
    "args_types": {
      "fx_name": ":symbol"
    },
    "intro_fn": true,
    "introduced": "2,0,0",
    "opts": {
      "kill_delay": 1
    },
    "requires_block": true,
    "summary": "Use Studio FX"
  },
  "with_merged_sample_defaults": {
    "accepts_block": false,
    "args_in": {
      "&block": null,
      "*args": null
    },
    "args_types": {},
    "introduced": "2,9,0",
    "opts": {},
    "requires_block": false,
    "summary": "Block-level use merged sample defaults"
  },
  "with_merged_synth_defaults": {
    "accepts_block": true,
    "args_in": {
      "&block": null,
      "*args": null
    },
    "args_types": {},
    "introduced": "2,0,0",
    "opts": {},
    "requires_block": true,
    "summary": "Block-level merge synth defaults"
  },
  "with_octave": {
    "accepts_block": true,
    "args_in": {
      "&block": null,
      "shift": null
    },
    "args_types": {
      "octave_shift": ":number"
    },
    "intro_fn": true,
    "introduced": "2,9,0",
    "opts": null,
    "summary": "Block level octave transposition"
  },
  "with_sample_bpm": {
    "accepts_block": true,
    "args_in": {
      "&block": null,
      "*args": null,
      "sample_name": null
    },
    "args_types": {
      "string_or_number": ":sample_name_or_duration"
    },
    "introduced": "2,1,0",
    "opts": {
      "num_beats": 1
    },
    "requires_block": true,
    "summary": "Block-scoped sample-duration-based bpm modification"
  },
  "with_sample_defaults": {
    "accepts_block": false,
    "args_in": {
      "&block": null,
      "*args": null
    },
    "args_types": {},
    "introduced": "2,5,0",
    "opts": {},
    "requires_block": false,
    "summary": "Block-level use new sample defaults"
  },
  "with_synth": {
    "accepts_block": true,
    "args_in": {
      "&block": null,
      "*args": null,
      "synth_name": null
    },
    "args_types": {
      "synth_name": ":symbol"
    },
    "introduced": "2,0,0",
    "opts": null,
    "requires_block": true,
    "summary": "Block-level synth switching"
  },
  "with_synth_defaults": {
    "accepts_block": true,
    "args_in": {
      "&block": null,
      "*args": null
    },
    "args_types": {},
    "introduced": "2,0,0",
    "opts": {},
    "requires_block": true,
    "summary": "Block-level use new synth defaults"
  },
  "with_timing_guarantees": {
    "accepts_block": true,
    "args_in": {
      "&block": null,
      "v": null
    },
    "args_types": {
      "bool": ":true_or_false"
    },
    "introduced": "2,10,0",
    "opts": null,
    "summary": "Block-scoped inhibition of synth triggers if too late"
  },
  "with_timing_warnings": {
    "args_in": {
      "&block": null,
      "v": null
    }
  },
  "with_transpose": {
    "accepts_block": true,
    "args_in": {
      "&block": null,
      "shift": null
    },
    "args_types": {
      "note_shift": ":number"
    },
    "introduced": "2,0,0",
    "opts": null,
    "requires_block": true,
    "summary": "Block-level note transposition"
  },
  "with_tuning": {
    "accepts_block": true,
    "args_in": {
      "&block": null,
      "fundamental_note": ":c",
      "tuning": null
    },
    "args_types": {
      "fundamental_note": ":symbol_or_number",
      "tuning": ":symbol"
    },
    "introduced": "2,6,0",
    "opts": null,
    "summary": "Block-level tuning modification"
  }
}
