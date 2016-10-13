null = None; true = True; false = False;
#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/

lang_sound = {
  "all_sample_names": {},
  "chord": {
    "args_in": {
      "*opts": null,
      "tonic_or_name": null
    }
  },
  "chord_degree": {
    "args_in": {
      "*opts": null,
      "degree": null,
      "number_of_notes": 4,
      "scale": ":major",
      "tonic": null
    }
  },
  "chord_invert": {
    "args_in": {
      "notes": null,
      "shift": null
    }
  },
  "chord_names": {},
  "control": {
    "args_in": {
      "*args": null
    }
  },
  "current_amp": {},
  "current_arg_checks": {},
  "current_cent_tuning": {},
  "current_debug": {},
  "current_octave": {},
  "current_sample_defaults": {},
  "current_sched_ahead_time": {},
  "current_synth": {},
  "current_synth_defaults": {},
  "current_transpose": {},
  "current_volume": {},
  "degree": {
    "args_in": {
      "degree": null,
      "scale": null,
      "tonic": null
    }
  },
  "fx_names": {},
  "hz_to_midi": {
    "args_in": {
      "freq": null
    }
  },
  "invert_chord": {
    "args_in": {
      "*args": null
    }
  },
  "kill": {
    "args_in": {
      "node": null
    }
  },
  "load_sample": {
    "args_in": {
      "*args": null
    }
  },
  "load_sample_at_path": {
    "args_in": {
      "path": null
    }
  },
  "load_samples": {
    "args_in": {
      "*args": null
    }
  },
  "load_synthdefs": {
    "args_in": {
      "path": "synthdef_path"
    }
  },
  "midi_notes": {
    "args_in": {
      "*args": null
    }
  },
  "midi_to_hz": {
    "args_in": {
      "n": null
    }
  },
  "note": {
    "args_in": {
      "*args": null,
      "n": null
    }
  },
  "note_info": {
    "args_in": {
      "*args": null,
      "n": null
    }
  },
  "note_range": {
    "args_in": {
      "*opts": null,
      "high_note": null,
      "low_note": null
    }
  },
  "octs": {
    "args_in": {
      "num_octs": 1,
      "start": null
    }
  },
  "pitch_ratio": {
    "args_in": {
      "*args": null
    }
  },
  "pitch_to_ratio": {
    "args_in": {
      "m": null
    }
  },
  "play": {
    "args_in": {
      "&blk": null,
      "*args": null,
      "n": null
    }
  },
  "play_chord": {
    "args_in": {
      "*args": null,
      "notes": null
    }
  },
  "play_pattern": {
    "args_in": {
      "*args": null,
      "notes": null
    }
  },
  "play_pattern_timed": {
    "args_in": {
      "*args": null,
      "notes": null,
      "times": null
    }
  },
  "ratio_to_pitch": {
    "args_in": {
      "r": null
    }
  },
  "recording_delete": {},
  "recording_save": {
    "args_in": {
      "filename": null
    }
  },
  "recording_start": {},
  "recording_stop": {},
  "reset_mixer!": {
    "args_in": {
      "": null
    }
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
    "args_in": {
      "n": null
    }
  },
  "sample": {
    "args_in": {
      "&blk": null,
      "*args": null
    }
  },
  "sample_buffer": {
    "args_in": {
      "*args": null
    }
  },
  "sample_duration": {
    "args_in": {
      "*args": null
    }
  },
  "sample_free": {
    "args_in": {
      "*paths": null
    }
  },
  "sample_free_all": {},
  "sample_groups": {},
  "sample_info": {
    "args_in": {
      "*args": null
    }
  },
  "sample_loaded?": {
    "args_in": {
      "*args": null
    }
  },
  "sample_names": {
    "args_in": {
      "group": null
    }
  },
  "sample_paths": {
    "args_in": {
      "*args": null
    }
  },
  "sample_split_filts_and_opts": {
    "args_in": {
      "args": null
    }
  },
  "scale": {
    "args_in": {
      "*opts": null,
      "tonic_or_name": null
    }
  },
  "scale_names": {},
  "set_cent_tuning!": {
    "args_in": {
      "shift": null
    }
  },
  "set_control_delta!": {
    "args_in": {
      "t": null
    }
  },
  "set_mixer_control!": {
    "args_in": {
      "opts": null
    }
  },
  "set_mixer_invert_stereo!": {},
  "set_mixer_mono_mode!": {},
  "set_mixer_standard_stereo!": {},
  "set_mixer_stereo_mode!": {},
  "set_sched_ahead_time!": {
    "args_in": {
      "t": null
    }
  },
  "set_volume!": {
    "args_in": {
      "vol": null
    }
  },
  "should_trigger?": {
    "args_in": {
      "args_h": null
    }
  },
  "start_amp_monitor": {},
  "status": {},
  "synth": {
    "args_in": {
      "&blk": null,
      "*args": null,
      "synth_name": null
    }
  },
  "synth_names": {},
  "truthy?": {
    "args_in": {
      "val": null
    }
  },
  "use_arg_bpm_scaling": {
    "args_in": {
      "&block": null,
      "bool": null
    }
  },
  "use_arg_checks": {
    "args_in": {
      "&block": null,
      "v": null
    }
  },
  "use_cent_tuning": {
    "args_in": {
      "&block": null,
      "shift": null
    }
  },
  "use_debug": {
    "args_in": {
      "&block": null,
      "v": null
    }
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
    "args_in": {
      "&block": null,
      "*args": null
    }
  },
  "use_merged_synth_defaults": {
    "args_in": {
      "&block": null,
      "*args": null
    }
  },
  "use_octave": {
    "args_in": {
      "&block": null,
      "shift": null
    }
  },
  "use_sample_bpm": {
    "args_in": {
      "*args": null,
      "sample_name": null
    }
  },
  "use_sample_defaults": {
    "args_in": {
      "&block": null,
      "*args": null
    }
  },
  "use_synth": {
    "args_in": {
      "&block": null,
      "*args": null,
      "synth_name": null
    }
  },
  "use_synth_defaults": {
    "args_in": {
      "&block": null,
      "*args": null
    }
  },
  "use_timing_guarantees": {
    "args_in": {
      "&block": null,
      "v": null
    }
  },
  "use_timing_warnings": {
    "args_in": {
      "&block": null,
      "v": null
    }
  },
  "use_transpose": {
    "args_in": {
      "&block": null,
      "shift": null
    }
  },
  "use_tuning": {
    "args_in": {
      "&block": null,
      "fundamental_note": ":c",
      "tuning": null
    }
  },
  "with_afx": {
    "args_in": {
      "&block": null,
      "*args": null,
      "fx_name": null
    }
  },
  "with_arg_bpm_scaling": {
    "args_in": {
      "&block": null,
      "bool": null
    }
  },
  "with_arg_checks": {
    "args_in": {
      "&block": null,
      "v": null
    }
  },
  "with_cent_tuning": {
    "args_in": {
      "&block": null,
      "shift": null
    }
  },
  "with_debug": {
    "args_in": {
      "&block": null,
      "v": null
    }
  },
  "with_fx": {
    "args_in": {
      "&block": null,
      "*args": null,
      "fx_name": null
    }
  },
  "with_merged_sample_defaults": {
    "args_in": {
      "&block": null,
      "*args": null
    }
  },
  "with_merged_synth_defaults": {
    "args_in": {
      "&block": null,
      "*args": null
    }
  },
  "with_octave": {
    "args_in": {
      "&block": null,
      "shift": null
    }
  },
  "with_sample_bpm": {
    "args_in": {
      "&block": null,
      "*args": null,
      "sample_name": null
    }
  },
  "with_sample_defaults": {
    "args_in": {
      "&block": null,
      "*args": null
    }
  },
  "with_synth": {
    "args_in": {
      "&block": null,
      "*args": null,
      "synth_name": null
    }
  },
  "with_synth_defaults": {
    "args_in": {
      "&block": null,
      "*args": null
    }
  },
  "with_timing_guarantees": {
    "args_in": {
      "&block": null,
      "v": null
    }
  },
  "with_timing_warnings": {
    "args_in": {
      "&block": null,
      "v": null
    }
  },
  "with_transpose": {
    "args_in": {
      "&block": null,
      "shift": null
    }
  },
  "with_tuning": {
    "args_in": {
      "&block": null,
      "fundamental_note": ":c",
      "tuning": null
    }
  }
}
