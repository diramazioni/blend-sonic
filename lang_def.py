null = None
#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/

lang_sound = {
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
    "opts": null,
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
    "opts": null,
    "summary": "Chord inversion"
  },
  "chord_names": {
    "accepts_block": false,
    "args_types": {},
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
    "opts": {},
    "summary": "Control running synth"
  },
  "current_amp": {},
  "current_arg_checks": {
    "accepts_block": false,
    "args_types": {},
    "opts": null,
    "summary": "Get current arg checking status"
  },
  "current_cent_tuning": {
    "accepts_block": false,
    "args_types": {},
    "opts": null,
    "summary": "Get current cent shift"
  },
  "current_debug": {
    "accepts_block": false,
    "args_types": {},
    "opts": null,
    "summary": "Get current debug status"
  },
  "current_octave": {
    "accepts_block": false,
    "args_types": {},
    "opts": null,
    "summary": "Get current octave shift"
  },
  "current_sample_defaults": {
    "accepts_block": false,
    "args_types": {},
    "opts": null,
    "summary": "Get current sample defaults"
  },
  "current_sched_ahead_time": {
    "accepts_block": false,
    "args_types": {},
    "opts": null,
    "summary": "Get current sched ahead time"
  },
  "current_synth_defaults": {
    "accepts_block": false,
    "args_types": {},
    "opts": null,
    "summary": "Get current synth defaults"
  },
  "current_transpose": {
    "accepts_block": false,
    "args_types": {},
    "opts": null,
    "summary": "Get current transposition"
  },
  "current_volume": {
    "accepts_block": false,
    "args_types": {},
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
    "opts": null,
    "summary": "Hz to MIDI conversion"
  },
  "invert_chord": {
    "args_in": {
      "*args": null
    }
  },
  "load_sample": {
    "args_in": {
      "*args": null
    },
    "summary": "Pre-load first matching sample"
  },
  "load_sample_at_path": {
    "args_in": {
      "path": null
    }
  },
  "load_samples": {
    "args_in": {
      "*args": null
    },
    "summary": "Pre-load all matching samples"
  },
  "midi_notes": {
    "accepts_block": false,
    "args_in": {
      "*args": null
    },
    "args_types": {
      "list": ":array"
    },
    "opts": null,
    "summary": "Create a ring buffer of midi note numbers"
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
    "opts": {
      "octave": 4
    },
    "summary": "Describe note"
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
    "opts": "{:pitches => \"An array of notes (symbols or ints) to filter on. Octave information is ignored.\"}",
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
    "opts": null,
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
    "opts": null,
    "summary": "relative MIDI pitch to frequency ratio"
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
  "recording_start": {
    "accepts_block": false,
    "args_types": {},
    "opts": null,
    "summary": "Start recording"
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
  "sample_buffer": {
    "accepts_block": false,
    "args_in": {
      "*args": null
    },
    "args_types": {
      "path": ":string"
    },
    "opts": null,
    "summary": "Get sample data"
  },
  "sample_duration": {
    "args_in": {
      "*args": null
    }
  },
  "sample_info": {
    "accepts_block": false,
    "args_in": {
      "*args": null
    },
    "args_types": {
      "path": ":string"
    },
    "opts": null,
    "summary": "Get sample information"
  },
  "sample_names": {
    "accepts_block": false,
    "args_in": {
      "group": null
    },
    "args_types": {
      "group": ":symbol"
    },
    "opts": null,
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
    "opts": null,
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
    "opts": null,
    "summary": "Set control delta globally"
  },
  "set_mixer_control!": {
    "accepts_block": false,
    "args_in": {
      "opts": null
    },
    "args_types": {},
    "opts": {
      "pre_amp": 1
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
    "opts": null,
    "summary": "Set Volume globally"
  },
  "should_trigger?": {
    "args_in": {
      "args_h": null
    }
  },
  "start_amp_monitor": {},
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
    "opts": null,
    "summary": "Note transposition"
  },
  "use_tuning": {
    "accepts_block": false,
    "args_in": {
      "&block": null,
      "fundamental_note ": " :c",
      "tuning": null
    },
    "args_types": {
      "fundamental_note": ":symbol_or_number",
      "tuning": ":symbol"
    },
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
    "opts": null,
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
    "opts": null,
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
    "opts": null,
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
    "opts": null,
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
    "opts": {
      "reps": 1
    },
    "summary": "Use Studio FX"
  },
  "with_merged_sample_defaults": {
    "accepts_block": false,
    "args_in": {
      "&block": null,
      "*args": null
    },
    "args_types": {},
    "opts": {},
    "summary": "Block-level use merged sample defaults"
  },
  "with_merged_synth_defaults": {
    "accepts_block": true,
    "args_in": {
      "&block": null,
      "*args": null
    },
    "args_types": {},
    "opts": {},
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
    "opts": {
      "num_beats": 1
    },
    "summary": "Block-scoped sample-duration-based bpm modification"
  },
  "with_sample_defaults": {
    "accepts_block": false,
    "args_in": {
      "&block": null,
      "*args": null
    },
    "args_types": {},
    "opts": {},
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
    "opts": null,
    "summary": "Block-level synth switching"
  },
  "with_synth_defaults": {
    "accepts_block": true,
    "args_in": {
      "&block": null,
      "*args": null
    },
    "args_types": {},
    "opts": {},
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
    "opts": null,
    "summary": "Block-level note transposition"
  },
  "with_tuning": {
    "accepts_block": true,
    "args_in": {
      "&block": null,
      "fundamental_note ": " :c",
      "tuning": null
    },
    "args_types": {
      "fundamental_note": ":symbol_or_number",
      "tuning": ":symbol"
    },
    "opts": null,
    "summary": "Block-level tuning modification"
  }
}
