null = None; true = True; false = False;
#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/

lang_core = {
  "beat": {
    "introduced": "2,10,0",
    "name": "beat",
    "hiden": true,
    "summary": "Get current beat",
    "accepts_block": false,
    "args": []
  },
  "rand_i": {
    "introduced": "2,0,0",
    "name": "rand_i",
    "accepts_block": false,
    "hiden": false,
    "summary": "Generate a random whole number below a value (exclusive)",
    "args": [
      {
        "max": ":number_or_range"
      }
    ],
    "signature": {
      "max": 2
    },
    "inline": true
  },
  "tick": {
    "introduced": "2,6,0",
    "name": "tick",
    "accepts_block": false,
    "hiden": false,
    "summary": "Increment a tick and return value",
    "args": [],
    "signature": {
      "*args": null
    },
    "alt_args": [
      {
        "list": ":array"
      },
      {
        "key": ":symbol"
      },
      {
        "value": ":number"
      }
    ],
    "opts": {
      "offset": 0,
      "step": 1
    },
    "returns": ":number",
    "inline": true
  },
  "puts": {
    "introduced": "2,0,0",
    "name": "puts",
    "accepts_block": false,
    "hiden": true,
    "summary": "Display a message in the output pane",
    "args": [
      {
        "output": ":anything"
      }
    ],
    "signature": {
      "*msgs": null
    },
    "intro_fn": true
  },
  "spread": {
    "introduced": "2,4,0",
    "name": "spread",
    "accepts_block": false,
    "hiden": false,
    "summary": "Euclidean distribution for beats",
    "args": [
      {
        "num_accents": ":number"
      },
      {
        "size": ":number"
      }
    ],
    "signature": {
      "num_accents": null,
      "size": null,
      "*args": null
    },
    "opts": {
      "rotate": false
    },
    "returns": ":ring",
    "inline": true
  },
  "live_loop": {
    "introduced": "2,1,0",
    "name": "live_loop",
    "accepts_block": true,
    "async_block": true,
    "intro_fn": true,
    "summary": "A loop for live coding",
    "args": [
      {
        "name": ":symbol"
      }
    ],
    "signature": {
      "name": "nil",
      "&block": null,
      "*args": null
    },
    "hiden": false,
    "opts": {
      "init": "",
      "auto_cue": true,
      "delay": 0,
      "sync": ":foo",
      "sync_bpm": ":foo",
      "seed": 0
    },
    "requires_block": true
  },
  "clear": {
    "introduced": "2,11,0",
    "name": "clear",
    "accepts_block": false,
    "hiden": false,
    "summary": "Clear all thread locals to defaults",
    "args": [],
    "returns": null
  },
  "defonce": {
    "introduced": "2,0,0",
    "name": "defonce",
    "accepts_block": true,
    "hiden": false,
    "summary": "Define a named value only once",
    "args": [
      {
        "name": ":symbol"
      }
    ],
    "signature": {
      "&block": null,
      "name": null,
      "*opts": null
    },
    "opts": {
      "override": false
    },
    "requires_block": true
  },
  "knit": {
    "introduced": "2,2,0",
    "name": "knit",
    "accepts_block": false,
    "hiden": false,
    "summary": "Knit a sequence of repeated values",
    "args": [
      {
        "value": ":anything"
      },
      {
        "count": ":number"
      }
    ],
    "signature": {
      "*args": null
    },
    "returns": ":ring",
    "inline": true
  },
  "rand_back": {
    "introduced": "2,7,0",
    "name": "rand_back",
    "accepts_block": false,
    "hiden": false,
    "summary": "Roll back random generator",
    "args": [
      {
        "amount": ":number"
      }
    ],
    "signature": {
      "amount": 1
    }
  },
  "load_buffer": {
    "introduced": "2,10,0",
    "name": "load_buffer",
    "accepts_block": false,
    "hiden": false,
    "summary": "Load the contents of a file to the current buffer",
    "args": [
      {
        "path": ":string"
      }
    ],
    "signature": {
      "path": null
    }
  },
  "look": {
    "introduced": "2,6,0",
    "name": "look",
    "accepts_block": false,
    "hiden": false,
    "summary": "Obtain value of a tick",
    "alt_args": [
      {
        "list": ":array"
      },
      {
        "key": ":symbol"
      }
    ],
    "signature": {
      "*args": null
    },
    "opts": {
      "offset": 0
    },
    "returns": ":number",
    "inline": true
  },
  "block_duration": {
    "introduced": "2,9,0",
    "name": "block_duration",
    "accepts_block": true,
    "async_block": false,
    "hiden": false,
    "summary": "Return block duration",
    "args": [],
    "signature": {
      "&block": null
    },
    "requires_block": true
  },
  "version": {
    "introduced": "2,0,0",
    "name": "version",
    "hiden": true,
    "summary": "Get current version information",
    "accepts_block": false
  },
  "doubles": {
    "introduced": "2,10,0",
    "name": "doubles",
    "accepts_block": false,
    "hiden": false,
    "summary": "Create a ring of successive doubles",
    "args": [
      {
        "start": ":number"
      },
      {
        "num_doubles": ":int"
      }
    ],
    "signature": {
      "start": null,
      "num_doubles": 1
    },
    "memoize": true,
    "returns": ":ring",
    "inline": true
  },
  "pick": {
    "introduced": "2,10,0",
    "name": "pick",
    "accepts_block": false,
    "hiden": false,
    "summary": "Randomly pick from list (with duplicates)",
    "args": [
      {
        "n": ":number_or_nil"
      }
    ],
    "signature": {
      "*args": null
    },
    "alt_args": [
      {
        "list": ":array"
      }
    ],
    "opts": {
      "skip": 0
    },
    "inline": true
  },
  "quantise": {
    "introduced": "2,1,0",
    "name": "quantise",
    "accepts_block": false,
    "hiden": false,
    "summary": "Quantise a value to resolution",
    "args": [
      {
        "n": ":number"
      },
      {
        "step": ":positive_number"
      }
    ],
    "signature": {
      "step": null,
      "n": null
    },
    "inline": true
  },
  "with_cue_logging": {
    "introduced": "2,6,0",
    "name": "with_cue_logging",
    "accepts_block": true,
    "hiden": false,
    "summary": "Block-level enable and disable cue logging",
    "args": [
      {
        "true_or_false": ":boolean"
      }
    ],
    "signature": {
      "&block": null,
      "v": null
    },
    "requires_block": true
  },
  "use_osc": {
    "hiden": true,
    "signature": {
      "host_or_port": null,
      "port": "nil"
    }
  },
  "load_example": {
    "introduced": "2,10,0",
    "name": "load_example",
    "accepts_block": false,
    "hiden": true,
    "summary": "Load a built-in example",
    "args": [
      {
        "path": ":string"
      }
    ],
    "signature": {
      "example_name": null
    }
  },
  "density": {
    "introduced": "2,3,0",
    "name": "density",
    "accepts_block": true,
    "async_block": true,
    "hiden": false,
    "summary": "Squash and repeat time",
    "args": [
      {
        "d": ":density"
      }
    ],
    "signature": {
      "d": null,
      "&block": null
    },
    "requires_block": true
  },
  "bools": {
    "introduced": "2,2,0",
    "name": "bools",
    "accepts_block": false,
    "hiden": false,
    "summary": "Create a ring of boolean values",
    "args": [
      {
        "list": ":array"
      }
    ],
    "signature": {
      "*args": null
    },
    "returns": ":ring",
    "inline": true
  },
  "cue": {
    "introduced": "2,0,0",
    "name": "cue",
    "accepts_block": false,
    "hiden": false,
    "summary": "Cue other threads",
    "args": [
      {
        "cue_id": ":symbol"
      }
    ],
    "signature": {
      "*opts": null,
      "cue_id": null
    },
    "opts": {
      "another_key": "foo: 64",
      "your_key": ":bar",
      "key": "foo: 64"
    }
  },
  "range": {
    "introduced": "2,2,0",
    "name": "range",
    "accepts_block": false,
    "hiden": false,
    "summary": "Create a ring buffer with the specified start, finish and step size",
    "args": [
      {
        "start": ":number"
      },
      {
        "finish": ":number"
      },
      {
        "step_size": ":number"
      }
    ],
    "signature": {
      "finish": null,
      "start": null,
      "*args": null
    },
    "memoize": true,
    "opts": {
      "inclusive": false,
      "step": 1
    },
    "returns": ":ring",
    "inline": true
  },
  "ramp": {
    "introduced": "2,6,0",
    "name": "ramp",
    "accepts_block": false,
    "hiden": false,
    "summary": "Create a ramp vector",
    "args": [
      {
        "list": ":array"
      }
    ],
    "signature": {
      "*args": null
    },
    "returns": ":ramp",
    "inline": true
  },
  "rand": {
    "introduced": "2,0,0",
    "name": "rand",
    "accepts_block": false,
    "hiden": false,
    "summary": "Generate a random float below a value",
    "args": [
      {
        "max": ":number_or_range"
      }
    ],
    "signature": {
      "max": 1
    },
    "intro_fn": true,
    "inline": true
  },
  "rand_skip": {
    "introduced": "2,7,0",
    "name": "rand_skip",
    "accepts_block": false,
    "hiden": false,
    "summary": "Jump forward random generator",
    "args": [
      {
        "amount": ":number"
      }
    ],
    "signature": {
      "amount": 1
    }
  },
  "shuffle": {
    "introduced": "2,1,0",
    "name": "shuffle",
    "accepts_block": false,
    "hiden": false,
    "summary": "Randomise order of a list",
    "args": [],
    "signature": {
      "list": null
    },
    "alt_args": [
      {
        "list": ":array"
      }
    ],
    "inline": true
  },
  "rand_look": {
    "introduced": "2,11,0",
    "name": "rand_look",
    "accepts_block": false,
    "hiden": false,
    "summary": "Generate a random number without consuming a rand",
    "args": [
      {
        "max": ":number_or_range"
      }
    ],
    "signature": {
      "*args": null
    },
    "inline": true
  },
  "note_list": {
    "accepts_block": false,
    "name": "note_list",
    "hiden": false,
    "summary": "Make a list of notes",
    "args": [],
    "signature": {},
    "introduced": "blend-sonic",
    "opts": {}
  },
  "with_bpm_mul": {
    "introduced": "2,3,0",
    "name": "with_bpm_mul",
    "accepts_block": true,
    "hiden": false,
    "summary": "Set new tempo as a multiple of current tempo for block",
    "args": [
      {
        "mul": ":number"
      }
    ],
    "signature": {
      "mul": null,
      "&block": null
    },
    "requires_block": true
  },
  "sleep": {
    "introduced": "2,0,0",
    "name": "sleep",
    "accepts_block": false,
    "advances_time": true,
    "summary": "Wait for beat duration",
    "args": [],
    "signature": {
      "beats": null
    },
    "alt_args": [
      {
        "beats": ":number"
      }
    ],
    "hiden": false
  },
  "ring": {
    "introduced": "2,2,0",
    "name": "ring",
    "accepts_block": false,
    "hiden": false,
    "summary": "Create a ring buffer",
    "args": [
      {
        "list": ":array"
      }
    ],
    "signature": {
      "*args": null
    },
    "returns": ":ring",
    "inline": true
  },
  "sync": {
    "introduced": "2,0,0",
    "name": "sync",
    "accepts_block": false,
    "advances_time": true,
    "summary": "Sync with other threads",
    "args": [
      {
        "cue_id": ":symbol"
      }
    ],
    "signature": {
      "opts": "{}",
      "cue_ids": null
    },
    "hiden": false,
    "opts": {
      "bpm_sync": false
    }
  },
  "with_tempo": {
    "hiden": true,
    "signature": {
      "&block": null,
      "*args": null
    }
  },
  "factor": {
    "introduced": "2,1,0",
    "name": "factor?",
    "accepts_block": false,
    "hiden": false,
    "summary": "Factor test",
    "args": [
      {
        "val": ":number"
      },
      {
        "factor": ":number"
      }
    ],
    "signature": {
      "factor": null,
      "val": null
    }
  },
  "comment": {
    "introduced": "2,0,0",
    "name": "comment",
    "hiden": true,
    "summary": "Block level commenting",
    "accepts_block": true,
    "signature": {
      "&block": null,
      "*args": null
    },
    "requires_block": true
  },
  "spark": {
    "introduced": "2,5,0",
    "name": "spark",
    "hiden": true,
    "summary": "Print a string representing a list of numeric values as a spark graph/bar chart",
    "accepts_block": false,
    "signature": {
      "*values": null
    }
  },
  "tick_reset": {
    "introduced": "2,6,0",
    "name": "tick_reset",
    "accepts_block": false,
    "hiden": false,
    "summary": "Reset tick to 0",
    "alt_args": [
      {
        "key": ":symbol"
      }
    ],
    "signature": {
      "*args": null
    },
    "returns": ":number"
  },
  "in_thread": {
    "introduced": "2,0,0",
    "name": "in_thread",
    "async_block": true,
    "hiden": false,
    "summary": "Run code block at the same time",
    "accepts_block": true,
    "signature": {
      "&block": null,
      "*opts": null
    },
    "opts": {
      "name": ":foo",
      "sync": ":foo",
      "sync_bpm": ":foo",
      "delay": 0
    },
    "requires_block": true
  },
  "halves": {
    "introduced": "2,10,0",
    "name": "halves",
    "accepts_block": false,
    "hiden": false,
    "summary": "Create a ring of successive halves",
    "args": [
      {
        "start": ":number"
      },
      {
        "num_halves": ":int"
      }
    ],
    "signature": {
      "start": null,
      "num_halves": 1
    },
    "memoize": true,
    "returns": ":ring",
    "inline": true
  },
  "osc": {
    "hiden": true,
    "signature": {
      "path": null,
      "*args": null
    }
  },
  "use_bpm": {
    "introduced": "2,0,0",
    "name": "use_bpm",
    "accepts_block": false,
    "hiden": false,
    "summary": "Set the tempo",
    "args": [
      {
        "bpm": ":number"
      }
    ],
    "signature": {
      "&block": null,
      "bpm": null
    },
    "intro_fn": true
  },
  "sync_bpm": {
    "introduced": "2,10,0",
    "name": "sync_bpm",
    "accepts_block": false,
    "advances_time": true,
    "summary": "Sync and inherit BPM from other threads ",
    "args": [
      {
        "cue_id": ":symbol"
      }
    ],
    "signature": {
      "opts": "{}",
      "cue_ids": null
    },
    "hiden": false,
    "opts": {}
  },
  "inc": {
    "introduced": "2, 1, 0",
    "name": "inc",
    "accepts_block": false,
    "hiden": true,
    "summary": "Increment",
    "args": [
      {
        "n": ":number"
      }
    ],
    "signature": {
      "n": null
    },
    "opts": {}
  },
  "rt": {
    "introduced": "2,0,0",
    "name": "rt",
    "accepts_block": false,
    "hiden": false,
    "summary": "Real time conversion",
    "args": [
      {
        "seconds": ":number"
      }
    ],
    "signature": {
      "t": null
    },
    "inline": true
  },
  "time_now": {
    "accepts_block": false,
    "name": "time_now",
    "hiden": false,
    "summary": "return a number based on current time",
    "args": [],
    "signature": {},
    "introduced": "blend-sonic",
    "opts": {}
  },
  "rdist": {
    "introduced": "2,3,0",
    "name": "rdist",
    "accepts_block": false,
    "hiden": false,
    "summary": "Random number in centred distribution",
    "args": [
      {
        "width": ":number"
      }
    ],
    "signature": {
      "centre": 0,
      "*opts": null,
      "width": null
    },
    "alt_args": [
      {
        "width": ":number"
      },
      {
        "centre": ":number"
      }
    ],
    "opts": {
      "step": 1
    },
    "inline": true
  },
  "with_bpm": {
    "introduced": "2,0,0",
    "name": "with_bpm",
    "accepts_block": true,
    "hiden": false,
    "summary": "Set the tempo for the code block",
    "args": [
      {
        "bpm": ":number"
      }
    ],
    "signature": {
      "&block": null,
      "bpm": null
    },
    "requires_block": true
  },
  "stretch": {
    "introduced": "2,6,0",
    "name": "stretch",
    "accepts_block": false,
    "hiden": false,
    "summary": "Stretch a sequence of values",
    "args": [
      {
        "count": ":int"
      }
    ],
    "signature": {
      "*args": null
    },
    "alt_args": [
      {
        "list": ":array"
      }
    ],
    "returns": ":ring",
    "inline": true
  },
  "one_in": {
    "introduced": "2,0,0",
    "name": "one_in",
    "accepts_block": false,
    "hiden": false,
    "summary": "Random true value with specified probability",
    "args": [
      {
        "num": ":number"
      }
    ],
    "signature": {
      "num": null
    },
    "inline": true
  },
  "uncomment": {
    "introduced": "2,0,0",
    "name": "uncomment",
    "hiden": true,
    "summary": "Block level comment ignoring",
    "accepts_block": true,
    "signature": {
      "&block": null,
      "*args": null
    },
    "requires_block": true
  },
  "run_file": {
    "introduced": "2,11,0",
    "name": "run_file",
    "accepts_block": false,
    "hiden": false,
    "summary": "Evaluate the contents of the file as a new Run",
    "args": [
      {
        "filename": ":path"
      }
    ],
    "signature": {
      "path": null
    },
    "returns": null
  },
  "rand_reset": {
    "introduced": "2,7,0",
    "name": "rand_reset",
    "hiden": false,
    "summary": "Reset rand generator to last seed",
    "accepts_block": false,
    "args": []
  },
  "ndefine": {
    "introduced": "2,1,0",
    "name": "ndefine",
    "accepts_block": true,
    "hiden": true,
    "summary": "Define a new function",
    "args": [
      {
        "name": ":symbol"
      }
    ],
    "signature": {
      "name": null,
      "&block": null
    },
    "requires_block": true
  },
  "bt": {
    "introduced": "2,8,0",
    "name": "bt",
    "accepts_block": false,
    "hiden": true,
    "summary": "Beat time conversion",
    "args": [
      {
        "seconds": ":number"
      }
    ],
    "signature": {
      "t": null
    }
  },
  "define": {
    "introduced": "2,0,0",
    "name": "define",
    "accepts_block": true,
    "intro_fn": true,
    "summary": "Define a new function",
    "args": [
      {
        "name": ":symbol"
      }
    ],
    "signature": {
      "name": null,
      "&block": null
    },
    "hiden": false,
    "requires_block": true
  },
  "use_cue_logging": {
    "introduced": "2,6,0",
    "name": "use_cue_logging",
    "accepts_block": false,
    "hiden": false,
    "summary": "Enable and disable cue logging",
    "args": [
      {
        "true_or_false": ":boolean"
      }
    ],
    "signature": {
      "&block": null,
      "v": null
    }
  },
  "wait": {
    "introduced": "2,0,0",
    "name": "wait",
    "accepts_block": false,
    "advances_time": true,
    "summary": "Wait for duration",
    "args": [
      {
        "beats": ":number"
      }
    ],
    "signature": {
      "time": null
    },
    "hiden": true
  },
  "use_random_seed": {
    "introduced": "2,0,0",
    "name": "use_random_seed",
    "accepts_block": false,
    "hiden": false,
    "summary": "Set random seed generator to known seed",
    "args": [
      {
        "seed": ":number"
      }
    ],
    "signature": {
      "&block": null,
      "seed": null
    }
  },
  "assert_equal": {
    "introduced": "2,8,0",
    "name": "assert_equal",
    "accepts_block": false,
    "hiden": false,
    "summary": "Ensure args are equal",
    "args": [
      {
        "arg1": ":anything"
      },
      {
        "arg2": ":anything"
      }
    ],
    "signature": {
      "msg": "nil",
      "arg2": null,
      "arg1": null
    },
    "alt_args": [
      {
        "arg1": ":anything"
      },
      {
        "arg2": ":anything"
      },
      {
        "error_msg": ":string"
      }
    ]
  },
  "vt": {
    "introduced": "2,1,0",
    "name": "vt",
    "hiden": false,
    "summary": "Get virtual time",
    "accepts_block": false,
    "inline": true
  },
  "rrand_i": {
    "introduced": "2,0,0",
    "name": "rrand_i",
    "accepts_block": false,
    "hiden": false,
    "summary": "Generate a random whole number between two points inclusively",
    "args": [
      {
        "min": ":number"
      },
      {
        "max": ":number"
      }
    ],
    "signature": {
      "max": null,
      "min": null
    },
    "inline": true
  },
  "dec": {
    "introduced": "2, 1, 0",
    "name": "dec",
    "accepts_block": false,
    "hiden": true,
    "summary": "Decrement",
    "args": [
      {
        "n": ":number"
      }
    ],
    "signature": {
      "n": null
    },
    "opts": {}
  },
  "tick_set": {
    "introduced": "2,6,0",
    "name": "tick_set",
    "accepts_block": false,
    "hiden": false,
    "summary": "Set tick to a specific value",
    "args": [
      {
        "value": ":number"
      }
    ],
    "signature": {
      "*args": null
    },
    "alt_args": [
      {
        "key": ":symbol"
      },
      {
        "value": ":number"
      }
    ],
    "returns": ":number"
  },
  "dice": {
    "introduced": "2,0,0",
    "name": "dice",
    "accepts_block": false,
    "hiden": false,
    "summary": "Random dice throw",
    "args": [
      {
        "num_sides": ":number"
      }
    ],
    "signature": {
      "num_sides": 6
    },
    "inline": true
  },
  "current_beat_duration": {
    "introduced": "2,6,0",
    "name": "current_beat_duration",
    "hiden": true,
    "summary": "Duration of current beat",
    "accepts_block": false
  },
  "vector": {
    "introduced": "2,6,0",
    "name": "vector",
    "accepts_block": false,
    "hiden": false,
    "summary": "Create a vector",
    "args": [
      {
        "list": ":array"
      }
    ],
    "signature": {
      "*args": null
    },
    "returns": ":vector",
    "inline": true
  },
  "spark_graph": {
    "introduced": "2,5,0",
    "name": "spark_graph",
    "hiden": true,
    "summary": "Returns a string representing a list of numeric values as a spark graph/bar chart",
    "accepts_block": false,
    "signature": {
      "*values": null
    }
  },
  "current_random_seed": {
    "introduced": "2,10,0",
    "name": "current_random_seed",
    "hiden": true,
    "summary": "Get current random seed",
    "accepts_block": false,
    "intro_fn": true
  },
  "tick_reset_all": {
    "introduced": "2,6,0",
    "name": "tick_reset_all",
    "accepts_block": false,
    "hiden": false,
    "summary": "Reset all ticks",
    "alt_args": [
      {
        "key": ":symbol"
      },
      {
        "value": ":number"
      }
    ],
    "returns": null,
    "args": [
      {
        "value": ":number"
      }
    ]
  },
  "current_bpm": {
    "introduced": "2,0,0",
    "name": "current_bpm",
    "hiden": true,
    "summary": "Get current tempo",
    "accepts_block": false
  },
  "on": {
    "introduced": "2,10,0",
    "name": "on",
    "accepts_block": true,
    "hiden": false,
    "summary": "Optionally evaluate block",
    "args": [
      {
        "condition": ":truthy"
      }
    ],
    "signature": {
      "&blk": null,
      "condition": null
    },
    "returns": null,
    "requires_block": true
  },
  "stop": {
    "introduced": "2,5,0",
    "name": "stop",
    "hiden": false,
    "summary": "Stop current thread or run",
    "accepts_block": false,
    "alt_args": [],
    "returns": null,
    "args": [
      {
        "true_stops": ":boolean"
      }
    ]
  },
  "at": {
    "introduced": "2,1,0",
    "name": "at",
    "accepts_block": true,
    "async_block": true,
    "hiden": false,
    "summary": "Asynchronous Time. Run a block at the given time(s)",
    "args": [
      {
        "times": ":list"
      },
      {
        "params": ":list"
      }
    ],
    "signature": {
      "params": "nil",
      "&block": null,
      "times": 0
    },
    "requires_block": true
  },
  "rand_i_look": {
    "introduced": "2,11,0",
    "name": "rand_i_look",
    "accepts_block": false,
    "hiden": false,
    "summary": "Generate a random whole number without consuming a rand",
    "args": [
      {
        "max": ":number_or_range"
      }
    ],
    "signature": {
      "*args": null
    },
    "inline": true
  },
  "time_shift": {
    "introduced": "2,11,0",
    "name": "time_shift",
    "accepts_block": true,
    "hiden": false,
    "summary": "Slide time forwards or backwards for the given block",
    "args": [
      {
        "delta_time": ":number"
      }
    ],
    "signature": {
      "&blk": null,
      "delta": null
    },
    "returns": null,
    "requires_block": true
  },
  "print": {
    "introduced": "2,0,0",
    "name": "print",
    "accepts_block": false,
    "hiden": true,
    "summary": "Display a message in the output pane",
    "args": [
      {
        "output": ":anything"
      }
    ],
    "signature": {
      "*msgs": null
    },
    "intro_fn": true
  },
  "rrand": {
    "introduced": "2,0,0",
    "name": "rrand",
    "accepts_block": false,
    "hiden": false,
    "summary": "Generate a random float between two numbers",
    "args": [
      {
        "min": ":number"
      },
      {
        "max": ":number"
      }
    ],
    "signature": {
      "*opts": null,
      "max": null,
      "min": null
    },
    "opts": {
      "step": 1
    },
    "intro_fn": true,
    "inline": true
  },
  "with_random_seed": {
    "introduced": "2,0,0",
    "name": "with_random_seed",
    "accepts_block": true,
    "hiden": false,
    "summary": "Specify random seed for code block",
    "args": [
      {
        "seed": ":number"
      }
    ],
    "signature": {
      "&block": null,
      "seed": null
    },
    "requires_block": true
  },
  "use_bpm_mul": {
    "introduced": "2,3,0",
    "name": "use_bpm_mul",
    "accepts_block": false,
    "hiden": false,
    "summary": "Set new tempo as a multiple of current tempo",
    "args": [
      {
        "mul": ":number"
      }
    ],
    "signature": {
      "mul": null,
      "&block": null
    }
  },
  "line": {
    "introduced": "2,5,0",
    "name": "line",
    "accepts_block": false,
    "hiden": false,
    "summary": "Create a ring buffer representing a straight line",
    "args": [
      {
        "start": ":number"
      },
      {
        "finish": ":number"
      }
    ],
    "signature": {
      "finish": null,
      "start": null,
      "*args": null
    },
    "memoize": true,
    "opts": {
      "steps": 1,
      "inclusive": false
    },
    "returns": ":ring",
    "inline": true
  },
  "run_code": {
    "introduced": "2,11,0",
    "name": "run_code",
    "accepts_block": false,
    "hiden": false,
    "summary": "Evaluate the code passed as a String as a new Run",
    "args": [
      {
        "code": ":string"
      }
    ],
    "signature": {
      "code": null
    },
    "returns": null
  },
  "choose": {
    "introduced": "2,0,0",
    "name": "choose",
    "accepts_block": false,
    "hiden": false,
    "summary": "Random list selection",
    "args": [],
    "signature": {
      "args": null
    },
    "alt_args": [
      {
        "list": ":array"
      }
    ],
    "inline": true
  },
  "block_slept": {
    "introduced": "2,9,0",
    "name": "block_slept?",
    "accepts_block": true,
    "async_block": false,
    "hiden": false,
    "summary": "Determine if block contains sleep time",
    "args": [],
    "signature": {
      "&block": null
    },
    "requires_block": true
  },
  "reset": {
    "introduced": "2,11,0",
    "name": "reset",
    "accepts_block": false,
    "hiden": false,
    "summary": "Reset all thread locals",
    "args": [],
    "returns": null
  },
  "assert": {
    "introduced": "2,8,0",
    "name": "assert",
    "accepts_block": false,
    "hiden": false,
    "summary": "Ensure arg is valid",
    "args": [
      {
        "is_true": ":boolean"
      }
    ],
    "signature": {
      "msg": "nil",
      "arg": null
    },
    "alt_args": []
  }
}

#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/

lang_sound = {
  "current_sched_ahead_time": {
    "introduced": "2,0,0",
    "name": "current_sched_ahead_time",
    "hiden": true,
    "summary": "Get current sched ahead time",
    "accepts_block": false
  },
  "sample_split_filts_and_opts": {
    "hiden": true,
    "signature": {
      "args": null
    }
  },
  "truthy": {
    "hiden": false,
    "signature": {
      "val": null
    }
  },
  "set_control_delta": {
    "introduced": "2,1,0",
    "name": "set_control_delta!",
    "accepts_block": false,
    "hiden": false,
    "summary": "Set control delta globally",
    "modifies_env": true,
    "signature": {
      "t": null
    },
    "args": [
      {
        "time": ":number"
      }
    ]
  },
  "sample_groups": {
    "introduced": "2,0,0",
    "name": "sample_groups",
    "accepts_block": false,
    "hiden": true,
    "summary": "Get all sample groups",
    "memoize": true
  },
  "hz_to_midi": {
    "introduced": "2,0,0",
    "name": "hz_to_midi",
    "accepts_block": false,
    "hiden": false,
    "summary": "Hz to MIDI conversion",
    "args": [
      {
        "freq": ":number"
      }
    ],
    "signature": {
      "freq": null
    },
    "inline": true
  },
  "current_amp": {
    "hiden": true
  },
  "current_cent_tuning": {
    "introduced": "2,9,0",
    "name": "current_cent_tuning",
    "hiden": true,
    "summary": "Get current cent shift",
    "accepts_block": false
  },
  "time_now": {
    "accepts_block": false,
    "name": "time_now",
    "hiden": false,
    "summary": "return a number based on current time",
    "args": [],
    "signature": {},
    "introduced": "blend-sonic",
    "opts": {}
  },
  "current_arg_checks": {
    "introduced": "2,0,0",
    "name": "current_arg_checks",
    "hiden": true,
    "summary": "Get current arg checking status",
    "accepts_block": false
  },
  "use_debug": {
    "introduced": "2,0,0",
    "name": "use_debug",
    "accepts_block": false,
    "hiden": false,
    "summary": "Enable and disable debug",
    "args": [
      {
        "true_or_false": ":boolean"
      }
    ],
    "signature": {
      "&block": null,
      "v": null
    }
  },
  "use_octave": {
    "introduced": "2,9,0",
    "name": "use_octave",
    "accepts_block": false,
    "hiden": false,
    "summary": "Note octave transposition",
    "args": [
      {
        "octave_shift": ":number"
      }
    ],
    "signature": {
      "shift": null,
      "&block": null
    },
    "intro_fn": true
  },
  "use_timing_guarantees": {
    "introduced": "2,10,0",
    "name": "use_timing_guarantees",
    "accepts_block": false,
    "hiden": false,
    "summary": "Inhibit synth triggers if too late",
    "args": [
      {
        "bool": ":true_or_false"
      }
    ],
    "signature": {
      "&block": null,
      "v": null
    },
    "requires_block": false
  },
  "sample_free": {
    "introduced": "2,9,0",
    "name": "sample_free",
    "accepts_block": false,
    "hiden": false,
    "summary": "Free a sample on the synth server",
    "args": [
      {
        "path": ":string"
      }
    ],
    "signature": {
      "*paths": null
    },
    "returns": null
  },
  "use_synth": {
    "introduced": "2,0,0",
    "name": "use_synth",
    "accepts_block": false,
    "hiden": false,
    "summary": "Switch current synth",
    "args": [
      {
        "synth_name": ":symbol"
      }
    ],
    "signature": {
      "synth_name": null,
      "&block": null,
      "*args": null
    },
    "intro_fn": true
  },
  "play_chord": {
    "introduced": "2,0,0",
    "name": "play_chord",
    "accepts_block": false,
    "hiden": false,
    "summary": "Play notes simultaneously",
    "args": [
      {
        "notes": ":list"
      }
    ],
    "signature": {
      "notes": null,
      "*args": null
    },
    "opts": {
      "attack_level": 1,
      "sustain_level": 1,
      "attack": 0,
      "sustain": 1,
      "release": 0,
      "amp_slide": 1,
      "amp": 1,
      "pan_slide": 1,
      "pan": 0,
      "decay": 0,
      "env_curve": 1,
      "decay_level": 1,
      "on": 1,
      "pitch": 0,
      "slide": 0
    }
  },
  "set_mixer_stereo_mode!": {
    "hiden": false
  },
  "with_sample_defaults": {
    "introduced": "2,5,0",
    "name": "with_sample_defaults",
    "hiden": false,
    "summary": "Block-level use new sample defaults",
    "accepts_block": true,
    "signature": {
      "&block": null,
      "*args": null
    },
    "opts": {},
    "requires_block": true
  },
  "with_synth": {
    "introduced": "2,0,0",
    "name": "with_synth",
    "accepts_block": true,
    "hiden": false,
    "summary": "Block-level synth switching",
    "args": [
      {
        "synth_name": ":symbol"
      }
    ],
    "signature": {
      "synth_name": null,
      "&block": null,
      "*args": null
    },
    "requires_block": true
  },
  "use_sample_defaults": {
    "introduced": "2,5,0",
    "name": "use_sample_defaults",
    "hiden": false,
    "summary": "Use new sample defaults",
    "accepts_block": false,
    "signature": {
      "&block": null,
      "*args": null
    },
    "opts": {
      "compress": 0,
      "relax_time": 0,
      "lpf_release_level": 0,
      "sustain": 1,
      "pitch_stretch": 1,
      "amp": 1,
      "norm": 0,
      "hpf_release_level": 0,
      "hpf_max": 200,
      "window_size": 0,
      "hpf_attack": 0,
      "hpf_sustain": 0,
      "rate": 1,
      "attack": 0,
      "hpf_attack_level": 0,
      "rpitch": 0,
      "lpf_attack_level": 0,
      "slide": 0,
      "pan": 0,
      "hpf_decay": 0,
      "lpf_env_curve": 1,
      "lpf_min": 30,
      "pitch_dis": 0,
      "lpf_decay_level": 0,
      "time_dis": 0,
      "lpf_sustain_level": 0,
      "onset": 0,
      "beat_stretch": 1,
      "release": 0,
      "hpf_sustain_level": 0,
      "lpf": 131,
      "lpf_attack": 0,
      "hpf_release": 0,
      "pre_amp": 1,
      "slope_above": 1,
      "pitch": 0,
      "hpf_env_curve": 1,
      "hpf_decay_level": 0,
      "threshold": 0,
      "hpf": 0,
      "hpf_init_level": 130,
      "path": "/path/to/file",
      "clamp_time": 0,
      "lpf_sustain": 0,
      "slope_below": 1,
      "finish": 1,
      "lpf_init_level": 30,
      "lpf_release": 0,
      "start": 0,
      "lpf_decay": 0
    }
  },
  "chord": {
    "accepts_block": false,
    "inline": true,
    "returns": ":ring",
    "hiden": false,
    "summary": "Create chord",
    "memoize": true,
    "opts": {
      "invert": 0,
      "num_octaves": 1
    },
    "signature": {
      "*opts": null,
      "tonic_or_name": null
    },
    "introduced": "2,0,0",
    "name": "chord",
    "args": [],
    "intro_fn": true,
    "alt_args": [
      {
        "tonic": ":symbol"
      },
      {
        "chord": ":symbol"
      }
    ]
  },
  "with_arg_bpm_scaling": {
    "introduced": "2,0,0",
    "name": "with_arg_bpm_scaling",
    "hiden": false,
    "summary": "Block-level enable and disable BPM scaling",
    "accepts_block": true,
    "signature": {
      "&block": null,
      "bool": null
    },
    "requires_block": true
  },
  "use_merged_sample_defaults": {
    "introduced": "2,9,0",
    "name": "use_merged_sample_defaults",
    "hiden": false,
    "summary": "Merge new sample defaults",
    "accepts_block": false,
    "signature": {
      "&block": null,
      "*args": null
    },
    "opts": {}
  },
  "load_sample_at_path": {
    "hiden": false,
    "signature": {
      "path": null
    }
  },
  "with_timing_warnings": {
    "hiden": true,
    "signature": {
      "&block": null,
      "v": null
    }
  },
  "with_merged_synth_defaults": {
    "introduced": "2,0,0",
    "name": "with_merged_synth_defaults",
    "hiden": false,
    "summary": "Block-level merge synth defaults",
    "accepts_block": true,
    "signature": {
      "&block": null,
      "*args": null
    },
    "opts": {},
    "requires_block": true
  },
  "start_amp_monitor": {
    "hiden": true
  },
  "current_volume": {
    "introduced": "2,0,0",
    "name": "current_volume",
    "hiden": true,
    "summary": "Get current volume",
    "accepts_block": false
  },
  "use_synth_defaults": {
    "introduced": "2,0,0",
    "name": "use_synth_defaults",
    "hiden": false,
    "summary": "Use new synth defaults",
    "accepts_block": false,
    "signature": {
      "&block": null,
      "*args": null
    },
    "opts": {}
  },
  "play_pattern": {
    "introduced": "2,0,0",
    "name": "play_pattern",
    "accepts_block": false,
    "hiden": false,
    "summary": "Play pattern of notes",
    "args": [
      {
        "notes": ":list"
      }
    ],
    "signature": {
      "notes": null,
      "*args": null
    },
    "opts": {}
  },
  "synth": {
    "introduced": "2,0,0",
    "name": "synth",
    "accepts_block": true,
    "async_block": true,
    "hiden": false,
    "summary": "Trigger specific synth",
    "args": [
      {
        "synth_name": ":symbol"
      }
    ],
    "signature": {
      "synth_name": null,
      "&blk": null,
      "*args": null
    },
    "opts": {
      "attack_level": 1,
      "sustain_level": 1,
      "attack": 0,
      "sustain": 1,
      "release": 0,
      "amp_slide": 1,
      "amp": 1,
      "pan_slide": 1,
      "pan": 0,
      "decay": 0,
      "env_curve": 1,
      "decay_level": 1,
      "on": 1,
      "pitch": 0,
      "slide": 0
    },
    "intro_fn": true,
    "requires_block": false
  },
  "recording_delete": {
    "accepts_block": false,
    "name": "recording_delete",
    "hiden": true
  },
  "sample_free_all": {
    "introduced": "2,9,0",
    "name": "sample_free_all",
    "accepts_block": false,
    "hiden": false,
    "summary": "Free all loaded samples on the synth server",
    "args": [],
    "returns": null
  },
  "current_sample_defaults": {
    "introduced": "2,5,0",
    "name": "current_sample_defaults",
    "hiden": true,
    "summary": "Get current sample defaults",
    "accepts_block": false
  },
  "note_list": {
    "accepts_block": false,
    "name": "note_list",
    "hiden": false,
    "summary": "Make a list of notes",
    "args": [],
    "signature": {},
    "introduced": "blend-sonic",
    "opts": {}
  },
  "degree": {
    "introduced": "2,1,0",
    "name": "degree",
    "accepts_block": false,
    "hiden": false,
    "summary": "Convert a degree into a note",
    "args": [],
    "signature": {
      "scale": null,
      "tonic": null,
      "degree": null
    },
    "alt_args": [
      {
        "degree": ":symbol"
      },
      {
        "tonic": ":symbol"
      },
      {
        "scale": ":symbol"
      }
    ],
    "inline": true
  },
  "status": {
    "introduced": "2,0,0",
    "name": "status",
    "hiden": true,
    "summary": "Get server status",
    "accepts_block": false
  },
  "set_mixer_mono_mode!": {
    "hiden": false
  },
  "resolve_sample_paths": {
    "hiden": true,
    "signature": {
      "filts_and_sources": null
    }
  },
  "current_octave": {
    "introduced": "2,9,0",
    "name": "current_octave",
    "hiden": true,
    "summary": "Get current octave shift",
    "accepts_block": false
  },
  "set_sched_ahead_time": {
    "introduced": "2,0,0",
    "name": "set_sched_ahead_time!",
    "accepts_block": false,
    "hiden": false,
    "summary": "Set sched ahead time globally",
    "modifies_env": true,
    "signature": {
      "t": null
    },
    "args": [
      {
        "time": ":number"
      }
    ]
  },
  "with_afx": {
    "hiden": true,
    "signature": {
      "&block": null,
      "*args": null,
      "fx_name": null
    }
  },
  "with_octave": {
    "introduced": "2,9,0",
    "name": "with_octave",
    "accepts_block": true,
    "hiden": false,
    "summary": "Block level octave transposition",
    "args": [
      {
        "octave_shift": ":number"
      }
    ],
    "signature": {
      "shift": null,
      "&block": null
    },
    "intro_fn": true,
    "requires_block": true
  },
  "reset_mixer": {
    "introduced": "2,9,0",
    "name": "reset_mixer!",
    "accepts_block": false,
    "hiden": false,
    "summary": "Reset master mixer",
    "modifies_env": true,
    "signature": {
      "": null
    },
    "opts": {}
  },
  "with_transpose": {
    "introduced": "2,0,0",
    "name": "with_transpose",
    "accepts_block": true,
    "hiden": false,
    "summary": "Block-level note transposition",
    "args": [
      {
        "note_shift": ":number"
      }
    ],
    "signature": {
      "shift": null,
      "&block": null
    },
    "requires_block": true
  },
  "play": {
    "introduced": "2,0,0",
    "name": "play",
    "accepts_block": true,
    "async_block": true,
    "hiden": false,
    "summary": "Play current synth",
    "args": [
      {
        "note": ":symbol_or_number"
      }
    ],
    "signature": {
      "&blk": null,
      "n": null,
      "*args": null
    },
    "opts": {
      "attack_level": 1,
      "sustain_level": 1,
      "attack": 0,
      "sustain": 1,
      "release": 0,
      "amp_slide": 1,
      "amp": 1,
      "pan_slide": 1,
      "pan": 0,
      "decay": 0,
      "env_curve": 1,
      "decay_level": 1,
      "on": 1,
      "pitch": 0,
      "slide": 0
    },
    "intro_fn": true,
    "requires_block": false
  },
  "invert_chord": {
    "hiden": true,
    "signature": {
      "*args": null
    }
  },
  "current_synth": {
    "introduced": "2,0,0",
    "name": "current_synth",
    "hiden": true,
    "summary": "Get current synth",
    "accepts_block": false
  },
  "use_external_synths": {
    "hiden": true,
    "signature": {
      "&block": null,
      "v": null
    }
  },
  "synth_names": {
    "introduced": "2,9,0",
    "name": "synth_names",
    "accepts_block": false,
    "hiden": true,
    "summary": "Get all synth names",
    "memoize": true
  },
  "with_cent_tuning": {
    "introduced": "2,9,0",
    "name": "with_cent_tuning",
    "accepts_block": true,
    "hiden": false,
    "summary": "Block-level cent tuning",
    "args": [
      {
        "cent_shift": ":number"
      }
    ],
    "signature": {
      "shift": null,
      "&block": null
    },
    "requires_block": true
  },
  "current_synth_defaults": {
    "introduced": "2,0,0",
    "name": "current_synth_defaults",
    "hiden": true,
    "summary": "Get current synth defaults",
    "accepts_block": false
  },
  "recording_stop": {
    "introduced": "2,0,0",
    "name": "recording_stop",
    "hiden": true,
    "summary": "Stop recording",
    "accepts_block": false
  },
  "set_mixer_invert_stereo!": {
    "hiden": false
  },
  "use_timing_warnings": {
    "hiden": true,
    "signature": {
      "&block": null,
      "v": null
    }
  },
  "octs": {
    "introduced": "2,8,0",
    "name": "octs",
    "accepts_block": false,
    "hiden": false,
    "summary": "Create a ring of octaves",
    "args": [
      {
        "start": ":note"
      },
      {
        "num_octaves": ":pos_int"
      }
    ],
    "signature": {
      "start": null,
      "num_octs": 1
    },
    "returns": ":ring",
    "inline": true
  },
  "note_range": {
    "introduced": "2,6,0",
    "name": "note_range",
    "accepts_block": false,
    "hiden": false,
    "summary": "Get a range of notes",
    "args": [
      {
        "low_note": ":note"
      },
      {
        "high_note": ":note"
      }
    ],
    "signature": {
      "*opts": null,
      "high_note": null,
      "low_note": null
    },
    "opts": {
      "pitches": []
    },
    "returns": ":ring",
    "inline": true
  },
  "with_sample_bpm": {
    "introduced": "2,1,0",
    "name": "with_sample_bpm",
    "accepts_block": true,
    "hiden": false,
    "summary": "Block-scoped sample-duration-based bpm modification",
    "args": [
      {
        "string_or_number": ":sample_name_or_duration"
      }
    ],
    "signature": {
      "sample_name": null,
      "&block": null,
      "*args": null
    },
    "opts": {
      "num_beats": 1
    },
    "requires_block": true
  },
  "load_sample": {
    "introduced": "2,0,0",
    "name": "load_sample",
    "accepts_block": false,
    "hiden": false,
    "summary": "Pre-load first matching sample",
    "args": [
      {
        "path": ":string"
      }
    ],
    "signature": {
      "*args": null
    }
  },
  "use_transpose": {
    "introduced": "2,0,0",
    "name": "use_transpose",
    "accepts_block": false,
    "hiden": false,
    "summary": "Note transposition",
    "args": [
      {
        "note_shift": ":number"
      }
    ],
    "signature": {
      "shift": null,
      "&block": null
    },
    "intro_fn": true
  },
  "sample_buffer": {
    "introduced": "2,0,0",
    "name": "sample_buffer",
    "accepts_block": false,
    "hiden": true,
    "summary": "Get sample data",
    "args": [
      {
        "path": ":string"
      }
    ],
    "signature": {
      "*args": null
    }
  },
  "recording_save": {
    "introduced": "2,0,0",
    "name": "recording_save",
    "accepts_block": false,
    "hiden": true,
    "summary": "Save recording",
    "args": [
      {
        "path": ":string"
      }
    ],
    "signature": {
      "filename": null
    }
  },
  "use_cent_tuning": {
    "introduced": "2,9,0",
    "name": "use_cent_tuning",
    "accepts_block": false,
    "hiden": false,
    "summary": "Cent tuning",
    "args": [
      {
        "cent_shift": ":number"
      }
    ],
    "signature": {
      "shift": null,
      "&block": null
    },
    "intro_fn": true
  },
  "with_merged_sample_defaults": {
    "introduced": "2,9,0",
    "name": "with_merged_sample_defaults",
    "hiden": false,
    "summary": "Block-level use merged sample defaults",
    "accepts_block": true,
    "signature": {
      "&block": null,
      "*args": null
    },
    "opts": {},
    "requires_block": true
  },
  "use_arg_bpm_scaling": {
    "introduced": "2,0,0",
    "name": "use_arg_bpm_scaling",
    "accepts_block": false,
    "hiden": false,
    "summary": "Enable and disable BPM scaling",
    "args": [
      {
        "bool": ":boolean"
      }
    ],
    "signature": {
      "&block": null,
      "bool": null
    }
  },
  "use_arg_checks": {
    "introduced": "2,0,0",
    "name": "use_arg_checks",
    "accepts_block": false,
    "hiden": false,
    "summary": "Enable and disable arg checks",
    "args": [
      {
        "true_or_false": ":boolean"
      }
    ],
    "signature": {
      "&block": null,
      "v": null
    }
  },
  "set_volume": {
    "introduced": "2,0,0",
    "name": "set_volume!",
    "accepts_block": false,
    "hiden": false,
    "summary": "Set Volume globally",
    "modifies_env": true,
    "signature": {
      "vol": null
    },
    "args": [
      {
        "vol": ":number"
      }
    ]
  },
  "load_samples": {
    "introduced": "2,0,0",
    "name": "load_samples",
    "accepts_block": false,
    "hiden": false,
    "summary": "Pre-load all matching samples",
    "args": [
      {
        "paths": ":list"
      }
    ],
    "signature": {
      "*args": null
    }
  },
  "with_debug": {
    "introduced": "2,0,0",
    "name": "with_debug",
    "accepts_block": true,
    "hiden": false,
    "summary": "Block-level enable and disable debug",
    "args": [
      {
        "true_or_false": ":boolean"
      }
    ],
    "signature": {
      "&block": null,
      "v": null
    },
    "requires_block": true
  },
  "use_fx": {
    "hiden": true,
    "signature": {
      "&block": null,
      "*args": null
    }
  },
  "rest": {
    "introduced": "2,1,0",
    "name": "rest?",
    "accepts_block": false,
    "hiden": false,
    "summary": "Determine if note or args is a rest",
    "args": [
      {
        "note_or_args": ":number_symbol_or_map"
      }
    ],
    "signature": {
      "n": null
    }
  },
  "set_mixer_standard_stereo!": {
    "hiden": false
  },
  "sample_duration": {
    "introduced": "2,0,0",
    "name": "sample_duration",
    "accepts_block": false,
    "hiden": true,
    "summary": "Get duration of sample in beats",
    "args": [
      {
        "path": ":string"
      }
    ],
    "signature": {
      "*args": null
    },
    "opts": {
      "decay": 0,
      "finish": 1,
      "beat_stretch": 1,
      "rate": 1,
      "attack": 0,
      "sustain": 1,
      "release": 0,
      "start": 0,
      "pitch_stretch": 1,
      "rpitch": 0
    }
  },
  "sample": {
    "accepts_block": true,
    "async_block": true,
    "hiden": false,
    "summary": "Trigger sample",
    "opts": {
      "compress": 0,
      "relax_time": 0,
      "lpf_release_level": 0,
      "sustain": 1,
      "pitch_stretch": 1,
      "amp": 1,
      "norm": 0,
      "hpf_release_level": 0,
      "hpf_max": 200,
      "window_size": 0,
      "hpf_attack": 0,
      "hpf_sustain": 0,
      "rate": 1,
      "attack": 0,
      "hpf_attack_level": 0,
      "rpitch": 0,
      "lpf_attack_level": 0,
      "slide": 0,
      "pan": 0,
      "hpf_decay": 0,
      "lpf_env_curve": 1,
      "lpf_min": 30,
      "pitch_dis": 0,
      "lpf_decay_level": 0,
      "time_dis": 0,
      "lpf_sustain_level": 0,
      "onset": 0,
      "beat_stretch": 1,
      "release": 0,
      "hpf_sustain_level": 0,
      "lpf": 131,
      "lpf_attack": 0,
      "hpf_release": 0,
      "pre_amp": 1,
      "slope_above": 1,
      "pitch": 0,
      "hpf_env_curve": 1,
      "hpf_decay_level": 0,
      "threshold": 0,
      "hpf": 0,
      "hpf_init_level": 130,
      "path": "/path/to/file",
      "clamp_time": 0,
      "lpf_sustain": 0,
      "slope_below": 1,
      "finish": 1,
      "lpf_init_level": 30,
      "lpf_release": 0,
      "start": 0,
      "lpf_decay": 0
    },
    "intro_fn": true,
    "requires_block": false,
    "introduced": "2,0,0",
    "name": "sample",
    "args": [],
    "signature": {
      "&blk": null,
      "*args": null
    },
    "alt_args": [
      {
        "name_or_path": ":symbol_or_string"
      }
    ]
  },
  "with_timing_guarantees": {
    "introduced": "2,10,0",
    "name": "with_timing_guarantees",
    "accepts_block": true,
    "hiden": false,
    "summary": "Block-scoped inhibition of synth triggers if too late",
    "args": [
      {
        "bool": ":true_or_false"
      }
    ],
    "signature": {
      "&block": null,
      "v": null
    },
    "requires_block": true
  },
  "control": {
    "introduced": "2,0,0",
    "name": "control",
    "accepts_block": false,
    "hiden": false,
    "summary": "Control running synth",
    "args": [
      {
        "node": ":synth_node"
      }
    ],
    "signature": {
      "*args": null
    },
    "opts": {}
  },
  "with_arg_checks": {
    "introduced": "2,0,0",
    "name": "with_arg_checks",
    "accepts_block": true,
    "hiden": false,
    "summary": "Block-level enable and disable arg checks",
    "args": [
      {
        "true_or_false": ":boolean"
      }
    ],
    "signature": {
      "&block": null,
      "v": null
    },
    "requires_block": true
  },
  "use_tuning": {
    "introduced": "2,6,0",
    "name": "use_tuning",
    "accepts_block": false,
    "hiden": false,
    "summary": "Use alternative tuning systems",
    "args": [
      {
        "tuning": ":symbol"
      },
      {
        "fundamental_note": ":symbol_or_number"
      }
    ],
    "signature": {
      "&block": null,
      "tuning": null,
      "fundamental_note": ":c"
    }
  },
  "use_merged_synth_defaults": {
    "introduced": "2,0,0",
    "name": "use_merged_synth_defaults",
    "hiden": false,
    "summary": "Merge synth defaults",
    "accepts_block": false,
    "signature": {
      "&block": null,
      "*args": null
    },
    "opts": {}
  },
  "sample_loaded": {
    "introduced": "2,2,0",
    "name": "sample_loaded?",
    "accepts_block": false,
    "hiden": false,
    "summary": "Test if sample was pre-loaded",
    "args": [
      {
        "path": ":string"
      }
    ],
    "signature": {
      "*args": null
    }
  },
  "scale_names": {
    "introduced": "2,6,0",
    "name": "scale_names",
    "accepts_block": false,
    "hiden": true,
    "summary": "All scale names",
    "memoize": true
  },
  "midi_to_hz": {
    "introduced": "2,0,0",
    "name": "midi_to_hz",
    "accepts_block": false,
    "hiden": false,
    "summary": "MIDI to Hz conversion",
    "args": [
      {
        "note": ":symbol_or_number"
      }
    ],
    "signature": {
      "n": null
    },
    "inline": true
  },
  "kill": {
    "introduced": "2,0,0",
    "name": "kill",
    "accepts_block": false,
    "hiden": false,
    "summary": "Kill synth",
    "args": [
      {
        "node": ":synth_node"
      }
    ],
    "signature": {
      "node": null
    },
    "opts": {}
  },
  "set_cent_tuning": {
    "introduced": "2,10,0",
    "name": "set_cent_tuning!",
    "accepts_block": false,
    "hiden": false,
    "summary": "Global Cent tuning",
    "modifies_env": true,
    "signature": {
      "shift": null
    },
    "intro_fn": false,
    "args": [
      {
        "cent_shift": ":number"
      }
    ]
  },
  "current_debug": {
    "introduced": "2,0,0",
    "name": "current_debug",
    "hiden": true,
    "summary": "Get current debug status",
    "accepts_block": false
  },
  "with_synth_defaults": {
    "introduced": "2,0,0",
    "name": "with_synth_defaults",
    "hiden": false,
    "summary": "Block-level use new synth defaults",
    "accepts_block": true,
    "signature": {
      "&block": null,
      "*args": null
    },
    "opts": {},
    "requires_block": true
  },
  "use_sample_bpm": {
    "introduced": "2,1,0",
    "name": "use_sample_bpm",
    "accepts_block": false,
    "hiden": false,
    "summary": "Sample-duration-based bpm modification",
    "args": [],
    "signature": {
      "sample_name": null,
      "*args": null
    },
    "alt_args": [
      {
        "string_or_number": ":sample_name_or_duration"
      }
    ],
    "opts": {
      "num_beats": 1
    }
  },
  "chord_names": {
    "introduced": "2,6,0",
    "name": "chord_names",
    "accepts_block": false,
    "hiden": true,
    "summary": "All chord names",
    "memoize": true
  },
  "recording_start": {
    "introduced": "2,0,0",
    "name": "recording_start",
    "hiden": true,
    "summary": "Start recording",
    "accepts_block": false
  },
  "ratio_to_pitch": {
    "introduced": "2,7,0",
    "name": "ratio_to_pitch",
    "accepts_block": false,
    "hiden": false,
    "summary": "relative frequency ratio to MIDI pitch",
    "args": [
      {
        "ratio": ":number"
      }
    ],
    "signature": {
      "r": null
    },
    "inline": true
  },
  "midi_notes": {
    "introduced": "2,7,0",
    "name": "midi_notes",
    "accepts_block": false,
    "hiden": false,
    "summary": "Create a ring buffer of midi note numbers",
    "args": [
      {
        "list": ":array"
      }
    ],
    "signature": {
      "*args": null
    },
    "memoize": true,
    "returns": ":ring",
    "inline": true
  },
  "play_pattern_timed": {
    "introduced": "2,0,0",
    "name": "play_pattern_timed",
    "accepts_block": false,
    "hiden": false,
    "summary": "Play pattern of notes with specific times",
    "args": [
      {
        "notes": ":list"
      },
      {
        "times": ":list_or_number"
      }
    ],
    "signature": {
      "notes": null,
      "times": null,
      "*args": null
    },
    "opts": {
      "attack_level": 1,
      "sustain_level": 1,
      "attack": 0,
      "sustain": 1,
      "release": 0,
      "amp_slide": 1,
      "amp": 1,
      "pan_slide": 1,
      "pan": 0,
      "decay": 0,
      "env_curve": 1,
      "decay_level": 1,
      "on": 1,
      "pitch": 0,
      "slide": 0
    }
  },
  "chord_degree": {
    "introduced": "2,1,0",
    "name": "chord_degree",
    "accepts_block": false,
    "hiden": false,
    "summary": "Construct chords of stacked thirds, based on scale degrees",
    "args": [
      {
        "number_of_notes": ":int"
      }
    ],
    "signature": {
      "scale": ":major",
      "number_of_notes": 4,
      "*opts": null,
      "tonic": null,
      "degree": null
    },
    "alt_args": [
      {
        "degree": ":symbol"
      },
      {
        "tonic": ":symbol"
      },
      {
        "scale": ":symbol"
      }
    ],
    "memoize": true,
    "returns": ":ring",
    "inline": true
  },
  "sample_names": {
    "introduced": "2,0,0",
    "name": "sample_names",
    "accepts_block": false,
    "hiden": true,
    "summary": "Get sample names",
    "args": [
      {
        "group": ":symbol"
      }
    ],
    "signature": {
      "group": null
    },
    "memoize": true,
    "returns": ":ring"
  },
  "sample_info": {
    "introduced": "2,0,0",
    "name": "sample_info",
    "accepts_block": false,
    "hiden": true,
    "summary": "Get sample information",
    "args": [
      {
        "path": ":string"
      }
    ],
    "signature": {
      "*args": null
    }
  },
  "should_trigger": {
    "hiden": false,
    "signature": {
      "args_h": null
    }
  },
  "set_mixer_control": {
    "introduced": "2,7,0",
    "name": "set_mixer_control!",
    "accepts_block": false,
    "hiden": false,
    "summary": "Control master mixer",
    "modifies_env": true,
    "signature": {
      "opts": null
    },
    "opts": {
      "lpf": 131,
      "lpf_bypass": 0,
      "hpf": 0,
      "pre_amp": 1,
      "hpf_bypass": 0,
      "leak_dc_bypass": 0,
      "amp": 1,
      "limiter_bypass": 0
    }
  },
  "sample_paths": {
    "introduced": "2,10,0",
    "name": "sample_paths",
    "accepts_block": false,
    "hiden": true,
    "summary": "Sample Pack Filter Resolution",
    "args": [
      {
        "pre_args": ":source_and_filter_types"
      }
    ],
    "signature": {
      "*args": null
    },
    "returns": ":ring"
  },
  "scale": {
    "accepts_block": false,
    "inline": true,
    "returns": ":ring",
    "hiden": false,
    "summary": "Create scale",
    "memoize": true,
    "opts": {
      "num_octaves": 1
    },
    "signature": {
      "*opts": null,
      "tonic_or_name": null
    },
    "introduced": "2,0,0",
    "name": "scale",
    "args": [],
    "intro_fn": true,
    "alt_args": [
      {
        "tonic": ":symbol"
      },
      {
        "scale": ":symbol"
      }
    ]
  },
  "pitch_to_ratio": {
    "introduced": "2,5,0",
    "name": "pitch_to_ratio",
    "accepts_block": false,
    "hiden": false,
    "summary": "relative MIDI pitch to frequency ratio",
    "args": [
      {
        "pitch": ":midi_number"
      }
    ],
    "signature": {
      "m": null
    },
    "inline": true
  },
  "load_synthdefs": {
    "introduced": "2,0,0",
    "name": "load_synthdefs",
    "accepts_block": false,
    "hiden": true,
    "summary": "Load external synthdefs",
    "args": [
      {
        "path": ":string"
      }
    ],
    "signature": {
      "path": "synthdef_path"
    }
  },
  "all_sample_names": {
    "introduced": "2,0,0",
    "name": "all_sample_names",
    "accepts_block": false,
    "hiden": true,
    "summary": "Get all sample names",
    "memoize": true
  },
  "chord_invert": {
    "introduced": "2,6,0",
    "name": "chord_invert",
    "accepts_block": false,
    "hiden": false,
    "summary": "Chord inversion",
    "args": [
      {
        "notes": ":list"
      },
      {
        "shift": ":number"
      }
    ],
    "signature": {
      "notes": null,
      "shift": null
    },
    "returns": ":ring",
    "inline": true
  },
  "pitch_ratio": {
    "hiden": true,
    "signature": {
      "*args": null
    }
  },
  "with_fx": {
    "introduced": "2,0,0",
    "name": "with_fx",
    "accepts_block": true,
    "async_block": true,
    "intro_fn": true,
    "summary": "Use Studio FX",
    "args": [
      {
        "fx_name": ":symbol"
      }
    ],
    "signature": {
      "&block": null,
      "*args": null,
      "fx_name": null
    },
    "hiden": false,
    "opts": {
      "kill_delay": 1,
      "reps": 1
    },
    "requires_block": true
  },
  "note_info": {
    "introduced": "2,0,0",
    "name": "note_info",
    "accepts_block": false,
    "hiden": true,
    "summary": "Get note info",
    "args": [
      {
        "note": ":symbol_or_number"
      }
    ],
    "signature": {
      "n": null,
      "*args": null
    },
    "opts": {
      "octave": 4
    }
  },
  "current_transpose": {
    "introduced": "2,0,0",
    "name": "current_transpose",
    "hiden": true,
    "summary": "Get current transposition",
    "accepts_block": false
  },
  "fx_names": {
    "introduced": "2,10,0",
    "name": "fx_names",
    "accepts_block": false,
    "hiden": true,
    "summary": "Get all FX names",
    "memoize": true
  },
  "note": {
    "introduced": "2,0,0",
    "name": "note",
    "accepts_block": false,
    "hiden": false,
    "summary": "Describe note",
    "args": [],
    "signature": {
      "n": null,
      "*args": null
    },
    "alt_args": [
      {
        "note": ":symbol"
      }
    ],
    "opts": {}
  },
  "resolve_sample_path": {
    "hiden": true,
    "signature": {
      "filts_and_sources": null
    }
  },
  "with_tuning": {
    "introduced": "2,6,0",
    "name": "with_tuning",
    "accepts_block": true,
    "hiden": false,
    "summary": "Block-level tuning modification",
    "args": [
      {
        "tuning": ":symbol"
      },
      {
        "fundamental_note": ":symbol_or_number"
      }
    ],
    "signature": {
      "&block": null,
      "tuning": null,
      "fundamental_note": ":c"
    },
    "requires_block": true
  }
}

sound_args_types_conversion = {}

sound_opts_types_conversion = {}

#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/

synths = {
  "Prophet": {
    "name": ":prophet",
    "hiden": false,
    "summary": "The Prophet",
    "opts": {
      "note_slide_shape": 1,
      "env_curve": 2,
      "res_slide_shape": 1,
      "pan_slide_curve": 0,
      "amp_slide_shape": 1,
      "attack": 0,
      "sustain": 0,
      "release": 1,
      "cutoff_slide_shape": 1,
      "cutoff_slide": 0,
      "decay_level": 1,
      "pan_slide_shape": 1,
      "cutoff": 110,
      "res_slide_curve": 0,
      "attack_level": 1,
      "sustain_level": 1,
      "note_slide_curve": 0,
      "note_slide": 0,
      "amp_slide": 0,
      "amp": 1,
      "pan_slide": 0,
      "pan": 0,
      "decay": 0,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "res_slide": 0,
      "res": 0.7,
      "note": 52
    },
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth"
  },
  "DPulse": {
    "name": ":dpulse",
    "hiden": true,
    "summary": "Detuned Pulse Wave",
    "opts": {
      "note_slide_shape": 1,
      "env_curve": 2,
      "amp_slide": 0,
      "detune": 0.1,
      "pan_slide_curve": 0,
      "amp_slide_shape": 1,
      "dpulse_width_slide": 0,
      "sustain": 0,
      "release": 1,
      "pulse_width_slide": 0,
      "dpulse_width_slide_shape": 1,
      "attack_level": 1,
      "cutoff_slide": 0,
      "decay_level": 1,
      "pan_slide_shape": 1,
      "pulse_width_slide_shape": 1,
      "detune_slide_curve": 0,
      "detune_slide_shape": 1,
      "cutoff": 100,
      "sustain_level": 1,
      "note_slide_curve": 0,
      "attack": 0,
      "pulse_width": 0.5,
      "note_slide": 0,
      "amp": 1,
      "pan_slide": 0,
      "pan": 0,
      "cutoff_slide_shape": 1,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "decay": 0,
      "pulse_width_slide_curve": 0,
      "note": 52,
      "detune_slide": 0,
      "dpulse_width": 0
    },
    "inherit_arg": true,
    "inherit_base": "DSaw"
  },
  "BasicStereoPlayer": {
    "name": ":basic_stereo_player",
    "hiden": true,
    "summary": "Basic Stereo Sample Player (no env)",
    "opts": {
      "pan_slide_curve": 0,
      "amp_slide_shape": 1,
      "hpf_slide_curve": 0,
      "lpf": -1,
      "hpf_slide": 0,
      "pan_slide_shape": 1,
      "lpf_slide_shape": 1,
      "hpf": -1,
      "rate": 1,
      "lpf_slide": 0,
      "lpf_slide_curve": 0,
      "amp_slide": 0,
      "amp": 1,
      "pan_slide": 0,
      "pan": 0,
      "amp_slide_curve": 0,
      "hpf_slide_shape": 1
    },
    "inherit_arg": true,
    "inherit_base": "BasicMonoPlayer"
  },
  "Saw": {
    "name": ":saw",
    "hiden": true,
    "summary": "Saw Wave",
    "opts": {
      "note_slide_shape": 1,
      "env_curve": 2,
      "pan_slide_curve": 0,
      "amp_slide_shape": 1,
      "sustain": 0,
      "release": 1,
      "decay_level": 1,
      "pan_slide_shape": 1,
      "attack": 0,
      "attack_level": 1,
      "sustain_level": 1,
      "note_slide_curve": 0,
      "note_slide": 0,
      "amp_slide": 0,
      "amp": 1,
      "pan_slide": 0,
      "pan": 0,
      "decay": 0,
      "amp_slide_curve": 0,
      "note": 52
    },
    "inherit_arg": true,
    "inherit_base": "Beep"
  },
  "DSaw": {
    "name": ":dsaw",
    "hiden": false,
    "summary": "Detuned Saw wave",
    "opts": {
      "note_slide_shape": 1,
      "env_curve": 2,
      "detune": 0.1,
      "pan_slide_curve": 0,
      "amp_slide_shape": 1,
      "attack": 0,
      "sustain": 0,
      "release": 1,
      "cutoff_slide_shape": 1,
      "cutoff_slide": 0,
      "decay_level": 1,
      "pan_slide_shape": 1,
      "cutoff": 100,
      "detune_slide_curve": 0,
      "detune_slide_shape": 1,
      "attack_level": 1,
      "sustain_level": 1,
      "note_slide_curve": 0,
      "note_slide": 0,
      "amp_slide": 0,
      "amp": 1,
      "pan_slide": 0,
      "pan": 0,
      "decay": 0,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "note": 52,
      "detune_slide": 0
    },
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth"
  },
  "Supersaw": {
    "name": ":supersaw",
    "hiden": false,
    "summary": "Supersaw",
    "opts": {
      "note_slide_shape": 1,
      "env_curve": 2,
      "res_slide_shape": 1,
      "pan_slide_curve": 0,
      "amp_slide_shape": 1,
      "attack": 0,
      "sustain": 0,
      "release": 1,
      "cutoff_slide_shape": 1,
      "cutoff_slide": 0,
      "decay_level": 1,
      "pan_slide_shape": 1,
      "cutoff": 130,
      "res_slide_curve": 0,
      "attack_level": 1,
      "sustain_level": 1,
      "note_slide_curve": 0,
      "note_slide": 0,
      "amp_slide": 0,
      "amp": 1,
      "pan_slide": 0,
      "pan": 0,
      "decay": 0,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "res_slide": 0,
      "res": 0.7,
      "note": 52
    },
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth"
  },
  "Pitchless": {
    "hiden": true,
    "opts": {},
    "inherit_arg": true,
    "inherit_base": "SonicPiSynth"
  },
  "TechSaws": {
    "name": ":tech_saws",
    "hiden": false,
    "summary": "TechSaws",
    "opts": {
      "note_slide_shape": 1,
      "env_curve": 2,
      "res_slide_shape": 1,
      "pan_slide_curve": 0,
      "amp_slide_shape": 1,
      "attack": 0,
      "sustain": 0,
      "release": 1,
      "cutoff_slide_shape": 1,
      "cutoff_slide": 0,
      "decay_level": 1,
      "pan_slide_shape": 1,
      "cutoff": 130,
      "res_slide_curve": 0,
      "attack_level": 1,
      "sustain_level": 1,
      "note_slide_curve": 0,
      "note_slide": 0,
      "amp_slide": 0,
      "amp": 1,
      "pan_slide": 0,
      "pan": 0,
      "decay": 0,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "res_slide": 0,
      "res": 0.7,
      "note": 52
    },
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth"
  },
  "BasicMonoPlayer": {
    "name": ":basic_mono_player",
    "hiden": true,
    "summary": "Basic Mono Sample Player (no env)",
    "opts": {
      "lpf_slide_shape": 1,
      "amp_slide": 0,
      "rate": 1,
      "pan_slide_curve": 0,
      "amp_slide_shape": 1,
      "lpf_slide_curve": 0,
      "hpf_slide_curve": 0,
      "lpf_slide": 0,
      "amp": 1,
      "pan_slide": 0,
      "pan": 0,
      "lpf": -1,
      "amp_slide_curve": 0,
      "hpf_slide": 0,
      "pan_slide_shape": 1,
      "hpf_slide_shape": 1,
      "hpf": -1
    },
    "inherit_arg": false,
    "inherit_base": "StudioInfo"
  },
  "SynthPiano": {
    "name": ":piano",
    "hiden": false,
    "summary": "SynthPiano",
    "opts": {
      "note_slide_shape": 1,
      "stereo_width": 0,
      "pan_slide_curve": 0,
      "amp_slide_shape": 1,
      "sustain": 0,
      "release": 1,
      "hard": 0.5,
      "vel": 0.2,
      "pan_slide_shape": 1,
      "attack": 0,
      "attack_level": 1,
      "sustain_level": 1,
      "note_slide_curve": 0,
      "note_slide": 0,
      "amp_slide": 0,
      "amp": 1,
      "pan_slide": 0,
      "pan": 0,
      "decay": 0,
      "amp_slide_curve": 0,
      "note": 52,
      "decay_level": 1
    },
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth"
  },
  "MainMixer": {
    "name": ":mixer",
    "hiden": true,
    "summary": "Main Mixer",
    "opts": {
      "lpf_bypass": 0,
      "lpf_slide_shape": 1,
      "amp_slide": 0.02,
      "hpf": 0,
      "limiter_bypass": 0,
      "lpf_slide": 0.02,
      "hpf_bypass": 0,
      "pre_amp_slide_shape": 1,
      "hpf_slide_curve": 0,
      "amp_slide_shape": 1,
      "amp": 1,
      "lpf": 135.5,
      "amp_slide_curve": 0,
      "invert_stereo": 0,
      "hpf_slide": 0.02,
      "hpf_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "force_mono": 0,
      "lpf_slide_curve": 0,
      "pre_amp": 1,
      "pre_amp_slide": 0.02
    },
    "inherit_arg": false,
    "inherit_base": "BaseMixer"
  },
  "Zawa": {
    "name": ":zawa",
    "hiden": false,
    "summary": "Zawa",
    "opts": {
      "note_slide_shape": 1,
      "range_slide_curve": 0,
      "disable_wave": 0,
      "range": 24,
      "res_slide_shape": 1,
      "pan_slide_curve": 0,
      "amp_slide_shape": 1,
      "attack": 0,
      "sustain": 0,
      "release": 1,
      "pulse_width_slide": 0,
      "phase_slide_curve": 0,
      "wave": 3,
      "cutoff_slide_shape": 1,
      "cutoff_slide": 0,
      "decay_level": 1,
      "pan_slide_shape": 1,
      "cutoff": 100,
      "phase_offset": 0,
      "res_slide_curve": 0,
      "attack_level": 1,
      "sustain_level": 1,
      "range_slide_shape": 1,
      "note_slide_curve": 0,
      "pulse_width_slide_shape": 1,
      "note_slide": 0,
      "invert_wave": 0,
      "pulse_width": 0.5,
      "amp_slide": 0,
      "amp": 1,
      "pan_slide": 0,
      "pan": 0,
      "decay": 0,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "phase_slide_shape": 1,
      "res_slide": 0,
      "pulse_width_slide_curve": 0,
      "res": 0.9,
      "note": 52,
      "phase": 1,
      "range_slide": 0,
      "phase_slide": 0
    },
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth"
  },
  "SoundInStereo": {
    "name": ":sound_in_stereo",
    "hiden": true,
    "summary": "Sound In Stereo",
    "opts": {
      "env_curve": 0,
      "pan_slide_curve": 0,
      "amp_slide_shape": 1,
      "sustain": 1,
      "release": 0,
      "decay_level": 1,
      "pan_slide_shape": 1,
      "attack_level": 1,
      "sustain_level": 1,
      "attack": 0,
      "amp_slide": 0,
      "amp": 1,
      "pan_slide": 0,
      "pan": 0,
      "decay": 0,
      "amp_slide_curve": 0,
      "input": 1
    },
    "inherit_arg": true,
    "inherit_base": "SoundIn"
  },
  "ChipNoise": {
    "name": ":chipnoise",
    "hiden": true,
    "summary": "Chip Noise",
    "opts": {
      "attack_level": 1,
      "sustain_level": 1,
      "amp_slide": 0,
      "freq_band_slide": 0,
      "pan_slide_curve": 0,
      "amp_slide_shape": 0,
      "freq_band": 0,
      "sustain": 1,
      "release": 0,
      "attack": 0,
      "amp": 1,
      "pan_slide": 0,
      "pan": 0,
      "decay": 0,
      "amp_slide_curve": 1,
      "env_curve": 0,
      "decay_level": 1,
      "pan_slide_shape": 1,
      "freq_band_slide_shape": 1,
      "freq_band_slide_curve": 0
    },
    "inherit_arg": false,
    "inherit_base": "Noise"
  },
  "Hoover": {
    "name": ":hoover",
    "hiden": false,
    "summary": "Hoover",
    "opts": {
      "note_slide_shape": 1,
      "env_curve": 2,
      "res_slide_shape": 1,
      "pan_slide_curve": 0,
      "amp_slide_shape": 1,
      "attack": 0.05,
      "sustain": 0,
      "release": 1,
      "cutoff_slide_shape": 1,
      "cutoff_slide": 0,
      "decay_level": 1,
      "pan_slide_shape": 1,
      "cutoff": 130,
      "res_slide_curve": 0,
      "attack_level": 1,
      "sustain_level": 1,
      "note_slide_curve": 0,
      "note_slide": 0,
      "amp_slide": 0,
      "amp": 1,
      "pan_slide": 0,
      "pan": 0,
      "decay": 0,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "res_slide": 0,
      "res": 0.1,
      "note": 52
    },
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth"
  },
  "ModTri": {
    "name": ":mod_tri",
    "hiden": false,
    "summary": "Modulated Triangle Wave",
    "opts": {
      "note_slide_shape": 1,
      "mod_phase_slide": 0,
      "env_curve": 2,
      "mod_invert_wave": 0,
      "mod_pulse_width": 0.5,
      "pan_slide_curve": 0,
      "amp_slide_shape": 1,
      "attack": 0,
      "sustain": 0,
      "release": 1,
      "mod_pulse_width_slide": 0,
      "mod_pulse_width_slide_shape": 1,
      "mod_range_slide": 0,
      "cutoff_slide_shape": 1,
      "mod_pulse_width_slide_curve": 0,
      "cutoff_slide": 0,
      "decay_level": 1,
      "pan_slide_shape": 1,
      "mod_phase_slide_shape": 1,
      "cutoff": 100,
      "mod_phase_offset": 0,
      "mod_range_slide_shape": 1,
      "attack_level": 1,
      "sustain_level": 1,
      "note_slide_curve": 0,
      "note_slide": 0,
      "mod_wave": 1,
      "amp_slide": 0,
      "amp": 1,
      "pan_slide": 0,
      "pan": 0,
      "decay": 0,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "mod_range_slide_curve": 0,
      "mod_phase_slide_curve": 0,
      "note": 52,
      "mod_range": 5,
      "mod_phase": 0.25
    },
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth"
  },
  "SynthPluck": {
    "name": ":pluck",
    "hiden": false,
    "summary": "SynthPluck",
    "opts": {
      "note_slide_shape": 1,
      "pan_slide_curve": 0,
      "amp_slide_shape": 1,
      "max_delay_time": 0.125,
      "sustain": 0,
      "release": 1,
      "noise_amp": 0.8,
      "pluck_decay": 30,
      "decay_level": 1,
      "pan_slide_shape": 1,
      "attack": 0,
      "attack_level": 1,
      "sustain_level": 1,
      "note_slide_curve": 0,
      "note_slide": 0,
      "amp_slide": 0,
      "coef": 0.3,
      "amp": 1,
      "pan_slide": 0,
      "pan": 0,
      "decay": 0,
      "amp_slide_curve": 0,
      "note": 52
    },
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth"
  },
  "Growl": {
    "name": ":growl",
    "hiden": false,
    "summary": "Growl",
    "opts": {
      "note_slide_shape": 1,
      "env_curve": 2,
      "res_slide_shape": 1,
      "pan_slide_curve": 0,
      "amp_slide_shape": 1,
      "attack": 0.1,
      "sustain": 0,
      "release": 1,
      "cutoff_slide_shape": 1,
      "cutoff_slide": 0,
      "decay_level": 1,
      "pan_slide_shape": 1,
      "cutoff": 130,
      "res_slide_curve": 0,
      "attack_level": 1,
      "sustain_level": 1,
      "note_slide_curve": 0,
      "note_slide": 0,
      "amp_slide": 0,
      "amp": 1,
      "pan_slide": 0,
      "pan": 0,
      "decay": 0,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "res_slide": 0,
      "res": 0.7,
      "note": 52
    },
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth"
  },
  "ModPulse": {
    "name": ":mod_pulse",
    "hiden": false,
    "summary": "Modulated Pulse",
    "opts": {
      "note_slide_shape": 1,
      "mod_phase_slide": 0,
      "env_curve": 2,
      "mod_invert_wave": 0,
      "mod_pulse_width": 0.5,
      "pan_slide_curve": 0,
      "amp_slide_shape": 1,
      "attack": 0,
      "sustain": 0,
      "release": 1,
      "mod_pulse_width_slide": 0,
      "mod_pulse_width_slide_shape": 1,
      "pulse_width_slide": 0,
      "mod_range_slide": 0,
      "cutoff_slide_shape": 1,
      "mod_pulse_width_slide_curve": 0,
      "cutoff_slide": 0,
      "decay_level": 1,
      "pan_slide_shape": 1,
      "mod_phase_slide_shape": 1,
      "cutoff": 100,
      "mod_phase_offset": 0,
      "mod_range_slide_shape": 1,
      "attack_level": 1,
      "sustain_level": 1,
      "note_slide_curve": 0,
      "pulse_width_slide_shape": 1,
      "note_slide": 0,
      "mod_wave": 1,
      "amp_slide": 0,
      "amp": 1,
      "pan_slide": 0,
      "pan": 0,
      "decay": 0,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "mod_range_slide_curve": 0,
      "pulse_width": 0.5,
      "pulse_width_slide_curve": 0,
      "mod_phase_slide_curve": 0,
      "note": 52,
      "mod_range": 5,
      "mod_phase": 0.25
    },
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth"
  },
  "TB303": {
    "name": ":tb303",
    "hiden": false,
    "summary": "TB-303 Emulation",
    "opts": {
      "note_slide_shape": 1,
      "amp": 1,
      "note_slide_curve": 0,
      "sustain": 0,
      "cutoff_release": 1,
      "attack_level": 1,
      "cutoff_slide": 0,
      "pulse_width_slide_shape": 1,
      "cutoff_min_slide_curve": 0,
      "res_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "cutoff_min": 30,
      "attack": 0,
      "amp_slide": 0,
      "wave": 0,
      "pan": 0,
      "decay": 0,
      "cutoff_sustain": 0,
      "cutoff_slide_curve": 0,
      "cutoff_min_slide_shape": 1,
      "res_slide": 0,
      "res": 0.9,
      "env_curve": 2,
      "pan_slide_curve": 0,
      "amp_slide_shape": 1,
      "pulse_width": 0.5,
      "release": 1,
      "cutoff_decay": 0,
      "pulse_width_slide": 0,
      "decay_level": 1,
      "pan_slide_shape": 1,
      "cutoff": 120,
      "cutoff_decay_level": 1,
      "sustain_level": 1,
      "note": 52,
      "note_slide": 0,
      "pan_slide": 0,
      "cutoff_sustain_level": 1,
      "amp_slide_curve": 0,
      "cutoff_attack": 0,
      "res_slide_shape": 1,
      "pulse_width_slide_curve": 0,
      "cutoff_attack_level": 1,
      "cutoff_min_slide": 0
    },
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth"
  },
  "ModSine": {
    "name": ":mod_sine",
    "hiden": false,
    "summary": "Modulated Sine Wave",
    "opts": {
      "note_slide_shape": 1,
      "mod_phase_slide": 0,
      "env_curve": 2,
      "mod_invert_wave": 0,
      "mod_pulse_width": 0.5,
      "pan_slide_curve": 0,
      "amp_slide_shape": 1,
      "attack": 0,
      "sustain": 0,
      "release": 1,
      "mod_pulse_width_slide": 0,
      "mod_pulse_width_slide_shape": 1,
      "mod_range_slide": 0,
      "cutoff_slide_shape": 1,
      "mod_pulse_width_slide_curve": 0,
      "cutoff_slide": 0,
      "decay_level": 1,
      "pan_slide_shape": 1,
      "mod_phase_slide_shape": 1,
      "cutoff": 100,
      "mod_phase_offset": 0,
      "mod_range_slide_shape": 1,
      "attack_level": 1,
      "sustain_level": 1,
      "note_slide_curve": 0,
      "note_slide": 0,
      "mod_wave": 1,
      "amp_slide": 0,
      "amp": 1,
      "pan_slide": 0,
      "pan": 0,
      "decay": 0,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "mod_range_slide_curve": 0,
      "mod_phase_slide_curve": 0,
      "note": 52,
      "mod_range": 5,
      "mod_phase": 0.25
    },
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth"
  },
  "MonoPlayer": {
    "name": ":mono_player",
    "hiden": true,
    "summary": "Mono Sample Player",
    "opts": {
      "release": 0,
      "slope_above_slide_shape": 1,
      "lpf_slide": 0,
      "sustain": -1,
      "threshold_slide_curve": 0,
      "pre_amp_slide_curve": 0,
      "hpf_max": -1,
      "window_size_slide_curve": 0,
      "window_size": 0.2,
      "threshold_slide_shape": 1,
      "rate": 1,
      "attack": 0,
      "hpf_attack_level": -1,
      "lpf_slide_curve": 0,
      "lpf_decay": 0,
      "amp_slide": 0,
      "amp": 1,
      "pan": 0,
      "decay": 0,
      "hpf_decay": 0,
      "lpf_env_curve": 2,
      "lpf_min": -1,
      "hpf_max_slide_shape": 1,
      "time_dis": 0.0,
      "env_curve": 2,
      "relax_time_slide_curve": 0,
      "pan_slide_curve": 0,
      "amp_slide_shape": 1,
      "threshold_slide": 0,
      "lpf_min_slide_curve": 0,
      "hpf_sustain_level": -1,
      "lpf": -1,
      "hpf_release": 0,
      "decay_level": 1,
      "pitch": 0,
      "amp_slide_curve": 0,
      "sustain_level": 1,
      "slope_above_slide_curve": 0,
      "relax_time_slide": 0,
      "hpf": -1,
      "slope_below_slide": 0,
      "clamp_time": 0.01,
      "lpf_decay_level": -1,
      "lpf_sustain": -1,
      "slope_below": 1,
      "time_dis_slide_shape": 1,
      "pre_amp_slide_shape": 1,
      "time_dis_slide_curve": 0,
      "clamp_time_slide_shape": 1,
      "window_size_slide_shape": 1,
      "lpf_min_slide_shape": 1,
      "compress": 0,
      "relax_time": 0.01,
      "lpf_release_level": -1,
      "time_dis_slide": 0,
      "norm": 0,
      "hpf_release_level": -1,
      "hpf_slide": 0,
      "pan_slide": 0,
      "slope_above_slide": 0,
      "hpf_attack": 0,
      "lpf_slide_shape": 1,
      "pitch_dis_slide": 0,
      "hpf_sustain": -1,
      "finish": 1,
      "clamp_time_slide_curve": 0,
      "slope_below_slide_shape": 1,
      "hpf_max_slide_curve": 0,
      "lpf_attack_level": -1,
      "threshold": 0.2,
      "slope_below_slide_curve": 0,
      "pitch_dis": 0.0,
      "pitch_slide_curve": 0,
      "hpf_slide_curve": 0,
      "hpf_slide_shape": 1,
      "lpf_sustain_level": -1,
      "hpf_max_slide": 0,
      "attack_level": 1,
      "hpf_init_level": -1,
      "pitch_slide": 0,
      "relax_time_slide_shape": 1,
      "lpf_attack": 0,
      "pre_amp": 1,
      "slope_above": 0.5,
      "hpf_env_curve": 2,
      "lpf_min_slide": 0,
      "pre_amp_slide": 0,
      "hpf_decay_level": -1,
      "start": 0,
      "pan_slide_shape": 1,
      "pitch_dis_slide_curve": 0,
      "window_size_slide": 0,
      "clamp_time_slide": 0,
      "lpf_init_level": -1,
      "pitch_slide_shape": 1,
      "lpf_release": 0,
      "pitch_dis_slide_shape": 1
    },
    "inherit_arg": false,
    "inherit_base": "BasicMonoPlayer"
  },
  "DTri": {
    "name": ":dtri",
    "hiden": true,
    "summary": "Detuned Triangle Wave",
    "opts": {
      "note_slide_shape": 1,
      "env_curve": 2,
      "amp_slide": 0,
      "detune": 0.1,
      "pan_slide_curve": 0,
      "amp_slide_shape": 1,
      "sustain": 0,
      "release": 1,
      "attack_level": 1,
      "cutoff_slide": 0,
      "decay_level": 1,
      "pan_slide_shape": 1,
      "detune_slide_curve": 0,
      "detune_slide_shape": 1,
      "cutoff": 100,
      "sustain_level": 1,
      "note_slide_curve": 0,
      "attack": 0,
      "note_slide": 0,
      "amp": 1,
      "pan_slide": 0,
      "pan": 0,
      "cutoff_slide_shape": 1,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "decay": 0,
      "note": 52,
      "detune_slide": 0
    },
    "inherit_arg": true,
    "inherit_base": "DSaw"
  },
  "PNoise": {
    "name": ":pnoise",
    "hiden": true,
    "summary": "Pink Noise",
    "opts": {
      "res": 0,
      "env_curve": 2,
      "pan_slide_curve": 0,
      "amp_slide_shape": 1,
      "sustain": 0,
      "release": 1,
      "res_slide": 0,
      "attack_level": 1,
      "cutoff_slide": 0,
      "decay_level": 1,
      "pan_slide_shape": 1,
      "res_slide_curve": 0,
      "cutoff": 110,
      "sustain_level": 1,
      "attack": 0,
      "amp_slide": 0,
      "amp": 1,
      "pan_slide": 0,
      "pan": 0,
      "cutoff_slide_shape": 1,
      "amp_slide_curve": 0,
      "res_slide_shape": 1,
      "decay": 0,
      "cutoff_slide_curve": 0
    },
    "inherit_arg": true,
    "inherit_base": "Noise"
  },
  "Singer": {
    "name": ":singer",
    "hiden": true,
    "summary": "Singer",
    "opts": {
      "note_slide_shape": 1,
      "attack_level": 1,
      "sustain_level": 1,
      "pan_slide_curve": 0,
      "note_slide_curve": 0,
      "note_slide": 0,
      "sustain": 0,
      "amp_slide_shape": 1,
      "amp_slide": 0,
      "amp": 1,
      "pan_slide": 0,
      "pan": 0,
      "decay": 0,
      "amp_slide_curve": 0,
      "env_curve": 2,
      "decay_level": 1,
      "pan_slide_shape": 1,
      "attack": 1,
      "note": 52,
      "release": 4.0
    },
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth"
  },
  "PrettyBell": {
    "name": ":pretty_bell",
    "hiden": true,
    "summary": "Pretty Bell",
    "opts": {
      "note_slide_shape": 1,
      "env_curve": 2,
      "pan_slide_curve": 0,
      "amp_slide_shape": 1,
      "sustain": 0,
      "release": 1,
      "decay_level": 1,
      "pan_slide_shape": 1,
      "attack": 0,
      "attack_level": 1,
      "sustain_level": 1,
      "note_slide_curve": 0,
      "note_slide": 0,
      "amp_slide": 0,
      "amp": 1,
      "pan_slide": 0,
      "pan": 0,
      "decay": 0,
      "amp_slide_curve": 0,
      "note": 52
    },
    "inherit_arg": true,
    "inherit_base": "DullBell"
  },
  "Hollow": {
    "name": ":hollow",
    "hiden": false,
    "summary": "Hollow",
    "opts": {
      "note_slide_shape": 1,
      "env_curve": 2,
      "res_slide_shape": 1,
      "pan_slide_curve": 0,
      "amp_slide_shape": 1,
      "attack": 0,
      "sustain": 0,
      "release": 1,
      "norm": 0,
      "cutoff_slide_shape": 1,
      "cutoff_slide": 0,
      "decay_level": 1,
      "pan_slide_shape": 1,
      "cutoff": 90,
      "res_slide_curve": 0,
      "attack_level": 1,
      "sustain_level": 1,
      "note_slide_curve": 0,
      "note_slide": 0,
      "noise": 1,
      "amp_slide": 0,
      "amp": 1,
      "pan_slide": 0,
      "pan": 0,
      "decay": 0,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "res_slide": 0,
      "res": 0.99,
      "note": 52
    },
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth"
  },
  "StereoPlayer": {
    "name": ":stereo_player",
    "hiden": true,
    "summary": "Stereo Sample Player",
    "opts": {
      "pitch_slide": 0,
      "lpf_slide": 0,
      "sustain": -1,
      "threshold_slide_curve": 0,
      "pre_amp": 1,
      "lpf_attack_level": -1,
      "hpf_max": -1,
      "window_size_slide_curve": 0,
      "window_size": 0.2,
      "threshold_slide_shape": 1,
      "pan_slide_shape": 1,
      "rate": 1,
      "attack": 0,
      "hpf_attack_level": -1,
      "lpf_slide_curve": 0,
      "lpf_decay": 0,
      "amp_slide": 0,
      "amp": 1,
      "pan": 0,
      "decay": 0,
      "hpf_decay": 0,
      "lpf_env_curve": 2,
      "lpf_min": -1,
      "hpf_max_slide_shape": 1,
      "time_dis": 0.0,
      "env_curve": 2,
      "relax_time_slide_curve": 0,
      "pan_slide_curve": 0,
      "amp_slide_shape": 1,
      "threshold_slide": 0,
      "lpf_min_slide_curve": 0,
      "hpf_sustain_level": -1,
      "lpf": -1,
      "hpf_release": 0,
      "decay_level": 1,
      "pitch": 0,
      "hpf_decay_level": -1,
      "hpf_slide_curve": 0,
      "slope_above_slide_shape": 1,
      "slope_above_slide_curve": 0,
      "relax_time_slide": 0,
      "hpf": -1,
      "slope_below_slide": 0,
      "clamp_time": 0.01,
      "lpf_sustain": -1,
      "slope_below": 1,
      "amp_slide_curve": 0,
      "pre_amp_slide_shape": 1,
      "hpf_slide": 0,
      "clamp_time_slide_shape": 1,
      "window_size_slide_shape": 1,
      "lpf_min_slide_shape": 1,
      "compress": 0,
      "relax_time": 0.01,
      "lpf_release_level": -1,
      "time_dis_slide": 0,
      "norm": 0,
      "hpf_release_level": -1,
      "time_dis_slide_curve": 0,
      "window_size_slide": 0,
      "slope_above_slide": 0,
      "hpf_attack": 0,
      "lpf_slide_shape": 1,
      "pitch_dis_slide": 0,
      "hpf_sustain": -1,
      "time_dis_slide_shape": 1,
      "clamp_time_slide_curve": 0,
      "slope_below_slide_shape": 1,
      "hpf_max_slide_curve": 0,
      "sustain_level": 1,
      "threshold": 0.2,
      "slope_below_slide_curve": 0,
      "pitch_dis": 0.0,
      "pitch_slide_curve": 0,
      "lpf_decay_level": -1,
      "hpf_slide_shape": 1,
      "lpf_sustain_level": -1,
      "hpf_max_slide": 0,
      "attack_level": 1,
      "release": 0,
      "finish": 1,
      "lpf_attack": 0,
      "pre_amp_slide_curve": 0,
      "hpf_env_curve": 2,
      "lpf_min_slide": 0,
      "pre_amp_slide": 0,
      "slope_above": 0.5,
      "start": 0,
      "hpf_init_level": -1,
      "pitch_dis_slide_curve": 0,
      "pan_slide": 0,
      "clamp_time_slide": 0,
      "lpf_init_level": -1,
      "relax_time_slide_shape": 1,
      "lpf_release": 0,
      "pitch_slide_shape": 1,
      "pitch_dis_slide_shape": 1
    },
    "inherit_arg": true,
    "inherit_base": "MonoPlayer"
  },
  "SoundIn": {
    "name": ":sound_in",
    "hiden": false,
    "summary": "Sound In",
    "opts": {
      "attack_level": 1,
      "sustain_level": 1,
      "amp_slide": 0,
      "pan_slide_curve": 0,
      "amp_slide_shape": 1,
      "sustain": 1,
      "release": 0,
      "attack": 0,
      "amp": 1,
      "pan_slide": 0,
      "pan": 0,
      "decay": 0,
      "amp_slide_curve": 0,
      "env_curve": 0,
      "decay_level": 1,
      "pan_slide_shape": 1,
      "input": 1
    },
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth"
  },
  "SubPulse": {
    "name": ":subpulse",
    "hiden": true,
    "summary": "Pulse Wave with sub",
    "opts": {
      "note_slide_shape": 1,
      "sub_detune_slide": 0,
      "env_curve": 2,
      "sub_amp": 1,
      "pan_slide_curve": 0,
      "amp_slide_shape": 1,
      "sustain": 0,
      "release": 1,
      "pan_slide_shape": 1,
      "cutoff_slide_shape": 1,
      "sub_amp_slide": 0,
      "cutoff_slide": 0,
      "decay_level": 1,
      "pulse_width_slide": 0,
      "pulse_width_slide_shape": 1,
      "sub_amp_slide_curve": 0,
      "decay": 0,
      "sub_amp_slide_shape": 1,
      "attack_level": 1,
      "sustain_level": 1,
      "sub_detune": -12,
      "sub_detune_slide_shape": 1,
      "note_slide_curve": 0,
      "attack": 0,
      "amp_slide": 0,
      "amp": 1,
      "pan_slide": 0,
      "pan": 0,
      "cutoff": 100,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "pulse_width": 0.5,
      "note": 52,
      "note_slide": 0
    },
    "inherit_arg": true,
    "inherit_base": "Pulse"
  },
  "Beep": {
    "name": ":beep",
    "hiden": false,
    "summary": "Sine Wave",
    "opts": {
      "note_slide_shape": 1,
      "attack_level": 1,
      "sustain_level": 1,
      "pan_slide_curve": 0,
      "note_slide_curve": 0,
      "note_slide": 0,
      "sustain": 0,
      "amp_slide_shape": 1,
      "amp_slide": 0,
      "amp": 1,
      "pan_slide": 0,
      "pan": 0,
      "decay": 0,
      "amp_slide_curve": 0,
      "env_curve": 2,
      "decay_level": 1,
      "pan_slide_shape": 1,
      "attack": 0,
      "note": 52,
      "release": 1
    },
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth"
  },
  "ModSaw": {
    "name": ":mod_saw",
    "hiden": false,
    "summary": "Modulated Saw Wave",
    "opts": {
      "note_slide_shape": 1,
      "mod_phase_slide": 0,
      "env_curve": 2,
      "mod_invert_wave": 0,
      "mod_pulse_width": 0.5,
      "pan_slide_curve": 0,
      "amp_slide_shape": 1,
      "attack": 0,
      "sustain": 0,
      "release": 1,
      "mod_pulse_width_slide": 0,
      "mod_pulse_width_slide_shape": 1,
      "mod_range_slide": 0,
      "cutoff_slide_shape": 1,
      "mod_pulse_width_slide_curve": 0,
      "cutoff_slide": 0,
      "decay_level": 1,
      "pan_slide_shape": 1,
      "mod_phase_slide_shape": 1,
      "cutoff": 100,
      "mod_phase_offset": 0,
      "mod_range_slide_shape": 1,
      "attack_level": 1,
      "sustain_level": 1,
      "note_slide_curve": 0,
      "note_slide": 0,
      "mod_wave": 1,
      "amp_slide": 0,
      "amp": 1,
      "pan_slide": 0,
      "pan": 0,
      "decay": 0,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "mod_range_slide_curve": 0,
      "mod_phase_slide_curve": 0,
      "note": 52,
      "mod_range": 5,
      "mod_phase": 0.25
    },
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth"
  },
  "Noise": {
    "name": ":noise",
    "hiden": false,
    "summary": "Noise",
    "opts": {
      "env_curve": 2,
      "res_slide_shape": 1,
      "pan_slide_curve": 0,
      "amp_slide_shape": 1,
      "sustain": 0,
      "release": 1,
      "cutoff_slide_shape": 1,
      "cutoff_slide": 0,
      "decay_level": 1,
      "pan_slide_shape": 1,
      "cutoff": 110,
      "res_slide_curve": 0,
      "attack_level": 1,
      "sustain_level": 1,
      "attack": 0,
      "amp_slide": 0,
      "amp": 1,
      "pan_slide": 0,
      "pan": 0,
      "decay": 0,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "res_slide": 0,
      "res": 0
    },
    "inherit_arg": false,
    "inherit_base": "Pitchless"
  },
  "BaseMixer": {
    "hiden": true,
    "opts": {},
    "inherit_arg": true,
    "inherit_base": "StudioInfo"
  },
  "DullBell": {
    "name": ":dull_bell",
    "hiden": false,
    "summary": "Dull Bell",
    "opts": {
      "note_slide_shape": 1,
      "attack_level": 1,
      "sustain_level": 1,
      "pan_slide_curve": 0,
      "note_slide_curve": 0,
      "note_slide": 0,
      "sustain": 0,
      "amp_slide_shape": 1,
      "amp_slide": 0,
      "amp": 1,
      "pan_slide": 0,
      "pan": 0,
      "decay": 0,
      "amp_slide_curve": 0,
      "env_curve": 2,
      "decay_level": 1,
      "pan_slide_shape": 1,
      "attack": 0,
      "note": 52,
      "release": 1
    },
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth"
  },
  "SynthViolin": {
    "name": ":synth_violin",
    "hiden": false,
    "summary": "Blade Runner style strings",
    "opts": {
      "note_slide_shape": 1,
      "env_curve": 2,
      "pan_slide_curve": 0,
      "amp_slide_shape": 1,
      "attack": 0,
      "sustain": 0,
      "release": 1,
      "vibrato_depth_slide_curve": 0,
      "vibrato_delay": 0.5,
      "cutoff_slide_shape": 1,
      "cutoff_slide": 0,
      "decay_level": 1,
      "pan_slide_shape": 1,
      "vibrato_rate_slide_curve": 0,
      "cutoff": 100,
      "vibrato_rate": 6,
      "attack_level": 1,
      "sustain_level": 1,
      "note_slide_curve": 0,
      "note_slide": 0,
      "vibrato_rate_slide_shape": 1,
      "amp_slide": 0,
      "amp": 1,
      "pan_slide": 0,
      "pan": 0,
      "decay": 0,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "vibrato_depth_slide_shape": 1,
      "note": 52,
      "vibrato_depth": 0.15,
      "vibrato_onset": 0.1
    },
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth"
  },
  "ChipBass": {
    "name": ":chipbass",
    "hiden": false,
    "summary": "Chip Bass",
    "opts": {
      "note_slide_shape": 1,
      "attack_level": 1,
      "sustain_level": 1,
      "pan_slide_curve": 0,
      "note_slide_curve": 0,
      "note_slide": 0,
      "sustain": 0,
      "amp_slide_shape": 1,
      "amp_slide": 0,
      "amp": 1,
      "pan_slide": 0,
      "pan": 0,
      "decay": 0,
      "amp_slide_curve": 0,
      "env_curve": 2,
      "decay_level": 1,
      "pan_slide_shape": 1,
      "attack": 0,
      "note_resolution": 0.1,
      "note": 60,
      "release": 1
    },
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth"
  },
  "Pulse": {
    "name": ":pulse",
    "hiden": true,
    "summary": "Pulse Wave",
    "opts": {
      "note_slide_shape": 1,
      "env_curve": 2,
      "amp_slide": 0,
      "pan_slide_curve": 0,
      "amp_slide_shape": 1,
      "sustain": 0,
      "release": 1,
      "pulse_width_slide": 0,
      "attack_level": 1,
      "cutoff_slide": 0,
      "decay_level": 1,
      "pan_slide_shape": 1,
      "pulse_width_slide_shape": 1,
      "cutoff": 100,
      "sustain_level": 1,
      "note_slide_curve": 0,
      "attack": 0,
      "pulse_width": 0.5,
      "note_slide": 0,
      "amp": 1,
      "pan_slide": 0,
      "pan": 0,
      "cutoff_slide_shape": 1,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "decay": 0,
      "note": 52
    },
    "inherit_arg": true,
    "inherit_base": "Square"
  },
  "ModDSaw": {
    "name": ":mod_dsaw",
    "hiden": false,
    "summary": "Modulated Detuned Saw Waves",
    "opts": {
      "note_slide_shape": 1,
      "mod_phase_slide": 0,
      "env_curve": 2,
      "mod_invert_wave": 0,
      "mod_pulse_width": 0.5,
      "pan_slide_curve": 0,
      "amp_slide_shape": 1,
      "attack": 0,
      "sustain": 0,
      "release": 1,
      "mod_pulse_width_slide": 0,
      "mod_pulse_width_slide_shape": 1,
      "mod_range_slide": 0,
      "cutoff_slide_shape": 1,
      "mod_pulse_width_slide_curve": 0,
      "cutoff_slide": 0,
      "decay_level": 1,
      "pan_slide_shape": 1,
      "mod_phase_slide_shape": 1,
      "cutoff": 100,
      "detune_slide_curve": 0,
      "detune_slide": 0,
      "mod_phase_offset": 0,
      "mod_range_slide_shape": 1,
      "attack_level": 1,
      "sustain_level": 1,
      "note_slide_curve": 0,
      "note_slide": 0,
      "mod_wave": 1,
      "amp_slide": 0,
      "amp": 1,
      "pan_slide": 0,
      "pan": 0,
      "decay": 0,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "mod_range_slide_curve": 0,
      "mod_phase_slide_curve": 0,
      "detune_slide_shape": 1,
      "note": 52,
      "mod_range": 5,
      "detune": 0.1,
      "mod_phase": 0.25
    },
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth"
  },
  "CNoise": {
    "name": ":cnoise",
    "hiden": true,
    "summary": "Clip Noise",
    "opts": {
      "res": 0,
      "env_curve": 2,
      "pan_slide_curve": 0,
      "amp_slide_shape": 1,
      "sustain": 0,
      "release": 1,
      "res_slide": 0,
      "attack_level": 1,
      "cutoff_slide": 0,
      "decay_level": 1,
      "pan_slide_shape": 1,
      "res_slide_curve": 0,
      "cutoff": 110,
      "sustain_level": 1,
      "attack": 0,
      "amp_slide": 0,
      "amp": 1,
      "pan_slide": 0,
      "pan": 0,
      "cutoff_slide_shape": 1,
      "amp_slide_curve": 0,
      "res_slide_shape": 1,
      "decay": 0,
      "cutoff_slide_curve": 0
    },
    "inherit_arg": true,
    "inherit_base": "Noise"
  },
  "StudioInfo": {
    "hiden": true,
    "opts": {},
    "inherit_arg": true,
    "inherit_base": "SonicPiSynth"
  },
  "Tri": {
    "name": ":tri",
    "hiden": true,
    "summary": "Triangle Wave",
    "opts": {
      "note_slide_shape": 1,
      "env_curve": 2,
      "pan_slide_curve": 0,
      "amp_slide_shape": 1,
      "sustain": 0,
      "release": 1,
      "pan_slide_shape": 1,
      "cutoff_slide_shape": 1,
      "cutoff_slide": 0,
      "decay_level": 1,
      "pulse_width_slide": 0,
      "pulse_width_slide_shape": 1,
      "decay": 0,
      "attack_level": 1,
      "sustain_level": 1,
      "note_slide_curve": 0,
      "attack": 0,
      "amp_slide": 0,
      "amp": 1,
      "pan_slide": 0,
      "pan": 0,
      "cutoff": 100,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "pulse_width": 0.5,
      "note": 52,
      "note_slide": 0
    },
    "inherit_arg": true,
    "inherit_base": "Pulse"
  },
  "BasicMixer": {
    "name": ":basic_mixer",
    "hiden": true,
    "summary": "Basic Mixer",
    "opts": {
      "amp_slide_curve": 0,
      "amp_slide": 0.1,
      "amp": 1,
      "amp_slide_shape": 1
    },
    "inherit_arg": false,
    "inherit_base": "BaseMixer"
  },
  "SonicPiSynth": {
    "hiden": true,
    "opts": {},
    "inherit_arg": true,
    "inherit_base": "SynthInfo"
  },
  "SynthInfo": {
    "hiden": true,
    "opts": {},
    "inherit_arg": true,
    "inherit_base": "BaseInfo"
  },
  "FM": {
    "name": ":fm",
    "hiden": false,
    "summary": "Basic FM synthesis",
    "opts": {
      "note_slide_shape": 1,
      "env_curve": 2,
      "pan_slide_curve": 0,
      "amp_slide_shape": 1,
      "attack": 0,
      "sustain": 0,
      "release": 1,
      "depth": 1,
      "depth_slide_shape": 1,
      "cutoff_slide_shape": 1,
      "cutoff_slide": 0,
      "decay_level": 1,
      "pan_slide_shape": 1,
      "depth_slide_curve": 0,
      "cutoff": 100,
      "divisor_slide_curve": 0,
      "attack_level": 1,
      "sustain_level": 1,
      "note_slide_curve": 0,
      "note_slide": 0,
      "amp_slide": 0,
      "amp": 1,
      "pan_slide": 0,
      "pan": 0,
      "decay": 0,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "divisor_slide_shape": 1,
      "divisor_slide": 0,
      "depth_slide": 0,
      "note": 52,
      "divisor": 2
    },
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth"
  },
  "ChipLead": {
    "name": ":chiplead",
    "hiden": false,
    "summary": "Chip Lead",
    "opts": {
      "note_slide_shape": 1,
      "env_curve": 2,
      "pan_slide_curve": 0,
      "amp_slide_shape": 1,
      "sustain": 0,
      "release": 1,
      "decay_level": 1,
      "pan_slide_shape": 1,
      "attack": 0,
      "note_resolution": 0.1,
      "attack_level": 1,
      "sustain_level": 1,
      "note_slide_curve": 0,
      "note_slide": 0,
      "amp_slide": 0,
      "amp": 1,
      "pan_slide": 0,
      "pan": 0,
      "decay": 0,
      "amp_slide_curve": 0,
      "note": 60,
      "width": 0
    },
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth"
  },
  "BNoise": {
    "name": ":bnoise",
    "hiden": true,
    "summary": "Brown Noise",
    "opts": {
      "res": 0,
      "env_curve": 2,
      "pan_slide_curve": 0,
      "amp_slide_shape": 1,
      "sustain": 0,
      "release": 1,
      "res_slide": 0,
      "attack_level": 1,
      "cutoff_slide": 0,
      "decay_level": 1,
      "pan_slide_shape": 1,
      "res_slide_curve": 0,
      "cutoff": 110,
      "sustain_level": 1,
      "attack": 0,
      "amp_slide": 0,
      "amp": 1,
      "pan_slide": 0,
      "pan": 0,
      "cutoff_slide_shape": 1,
      "amp_slide_curve": 0,
      "res_slide_shape": 1,
      "decay": 0,
      "cutoff_slide_curve": 0
    },
    "inherit_arg": true,
    "inherit_base": "Noise"
  },
  "ModFM": {
    "name": ":mod_fm",
    "hiden": true,
    "summary": "Basic FM synthesis with frequency modulation.",
    "opts": {
      "note_slide_shape": 1,
      "note_slide_curve": 0,
      "sustain": 0,
      "mod_invert_wave": 0,
      "depth": 1,
      "attack_level": 1,
      "cutoff_slide": 0,
      "divisor_slide_curve": 0,
      "cutoff": 100,
      "attack": 0,
      "mod_wave": 1,
      "amp_slide": 0,
      "amp": 1,
      "pan": 0,
      "decay": 0,
      "cutoff_slide_curve": 0,
      "mod_range": 5,
      "env_curve": 2,
      "mod_pulse_width": 0.5,
      "pan_slide_curve": 0,
      "amp_slide_shape": 1,
      "release": 1,
      "depth_slide_shape": 1,
      "decay_level": 1,
      "pan_slide_shape": 1,
      "depth_slide_curve": 0,
      "sustain_level": 1,
      "mod_phase_offset": 0,
      "note": 52,
      "note_slide": 0,
      "pan_slide": 0,
      "cutoff_slide_shape": 1,
      "amp_slide_curve": 0,
      "divisor": 2,
      "divisor_slide": 0,
      "depth_slide": 0,
      "divisor_slide_shape": 1,
      "mod_phase": 0.25
    },
    "inherit_arg": true,
    "inherit_base": "FM"
  },
  "Square": {
    "name": ":square",
    "hiden": false,
    "summary": "Square Wave",
    "opts": {
      "note_slide_shape": 1,
      "env_curve": 2,
      "pan_slide_curve": 0,
      "amp_slide_shape": 1,
      "attack": 0,
      "sustain": 0,
      "release": 1,
      "cutoff_slide_shape": 1,
      "cutoff_slide": 0,
      "decay_level": 1,
      "pan_slide_shape": 1,
      "cutoff": 100,
      "attack_level": 1,
      "sustain_level": 1,
      "note_slide_curve": 0,
      "note_slide": 0,
      "amp_slide": 0,
      "amp": 1,
      "pan_slide": 0,
      "pan": 0,
      "decay": 0,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "note": 52
    },
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth"
  },
  "DarkAmbience": {
    "name": ":dark_ambience",
    "hiden": false,
    "summary": "Dark Ambience",
    "opts": {
      "note_slide_shape": 1,
      "reverb_time": 100,
      "env_curve": 2,
      "detune1_slide": 0,
      "res_slide_shape": 1,
      "pan_slide_curve": 0,
      "amp_slide_shape": 1,
      "attack": 0,
      "sustain": 0,
      "release": 1,
      "detune2_slide_shape": 1,
      "cutoff_slide_shape": 1,
      "cutoff_slide": 0,
      "decay_level": 1,
      "pan_slide_shape": 1,
      "cutoff": 110,
      "detune1_slide_shape": 1,
      "detune2_slide": 0,
      "ring": 0.2,
      "res_slide_curve": 0,
      "attack_level": 1,
      "sustain_level": 1,
      "detune2": 24,
      "note_slide_curve": 0,
      "room": 70,
      "note_slide": 0,
      "noise": 0,
      "amp_slide": 0,
      "amp": 1,
      "pan_slide": 0,
      "pan": 0,
      "decay": 0,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "res_slide": 0,
      "detune1": 12,
      "res": 0.7,
      "note": 52,
      "detune1_slide_curve": 0,
      "detune2_slide_curve": 0
    },
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth"
  },
  "GNoise": {
    "name": ":gnoise",
    "hiden": true,
    "summary": "Grey Noise",
    "opts": {
      "res": 0,
      "env_curve": 2,
      "pan_slide_curve": 0,
      "amp_slide_shape": 1,
      "sustain": 0,
      "release": 1,
      "res_slide": 0,
      "attack_level": 1,
      "cutoff_slide": 0,
      "decay_level": 1,
      "pan_slide_shape": 1,
      "res_slide_curve": 0,
      "cutoff": 110,
      "sustain_level": 1,
      "attack": 0,
      "amp_slide": 0,
      "amp": 1,
      "pan_slide": 0,
      "pan": 0,
      "cutoff_slide_shape": 1,
      "amp_slide_curve": 0,
      "res_slide_shape": 1,
      "decay": 0,
      "cutoff_slide_curve": 0
    },
    "inherit_arg": true,
    "inherit_base": "Noise"
  },
  "DarkSeaHorn": {
    "name": ":dark_sea_horn",
    "hiden": true,
    "summary": "Dark Sea Horn",
    "opts": {
      "note_slide_shape": 1,
      "attack_level": 1,
      "sustain_level": 1,
      "pan_slide_curve": 0,
      "note_slide_curve": 0,
      "note_slide": 0,
      "sustain": 0,
      "amp_slide_shape": 1,
      "amp_slide": 0,
      "amp": 1,
      "pan_slide": 0,
      "pan": 0,
      "decay": 0,
      "amp_slide_curve": 0,
      "env_curve": 2,
      "decay_level": 1,
      "pan_slide_shape": 1,
      "attack": 1,
      "note": 52,
      "release": 4.0
    },
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth"
  }
}

synth_nodes = {
  ":pluck": "SynthPluck",
  ":fx_distortion": "FXDistortion",
  ":mod_pulse": "ModPulse",
  ":supersaw": "Supersaw",
  ":fx_nlpf": "FXNormLPF",
  ":fx_wobble": "FXWobble",
  ":saw": "Saw",
  ":fx_nbpf": "FXNBPF",
  ":beep": "Beep",
  ":fx_replace_normaliser": "FXNormaliser",
  ":chipnoise": "ChipNoise",
  ":fx_mono": "FXMono",
  ":fx_gverb": "FXGVerb",
  ":fx_replace_rlpf": "FXRLPF",
  ":fx_slicer": "FXSlicer",
  ":fx_hpf": "FXHPF",
  ":fx_lpf": "FXLPF",
  ":fx_replace_ixi_techno": "FXIXITechno",
  ":fx_replace_lpf": "FXLPF",
  ":fx_bpf": "FXBPF",
  ":mono_player": "MonoPlayer",
  ":tri": "Tri",
  ":mod_beep": "ModSine",
  ":fx_reverb": "FXReverb",
  ":dsaw": "DSaw",
  ":subpulse": "SubPulse",
  ":piano": "SynthPiano",
  ":hollow": "Hollow",
  ":mod_dsaw": "ModDSaw",
  ":fx_replace_nhpf": "FXNormHPF",
  ":fx_replace_nlpf": "FXNormLPF",
  ":blade": "SynthViolin",
  ":fx_ixi_techno": "FXIXITechno",
  ":fx_replace_echo": "FXEcho",
  ":prophet": "Prophet",
  ":fx_octaver": "FXOctaver",
  ":fx_replace_wobble": "FXWobble",
  ":dark_ambience": "DarkAmbience",
  ":fx_ring_mod": "FXRingMod",
  ":fx_replace_slicer": "FXSlicer",
  ":fx_vowel": "FXVowel",
  ":fx_band_eq": "FXBandEQ",
  ":mod_tri": "ModTri",
  ":fx_replace_compressor": "FXCompressor",
  ":tb303": "TB303",
  ":square": "Square",
  ":fx_normaliser": "FXNormaliser",
  ":basic_mono_player": "BasicMonoPlayer",
  ":fx_nrhpf": "FXNormRHPF",
  ":fx_replace_nrlpf": "FXNormRLPF",
  ":dull_bell": "DullBell",
  ":fx_replace_level": "FXLevel",
  ":fx_tanh": "FXTanh",
  ":fx_nhpf": "FXNormHPF",
  ":fx_replace_hpf": "FXHPF",
  ":fx_panslicer": "FXPanSlicer",
  ":chiplead": "ChipLead",
  ":bnoise": "BNoise",
  ":fx_replace_nrhpf": "FXNormRHPF",
  ":pnoise": "PNoise",
  ":fx_replace_rhpf": "FXRHPF",
  ":hoover": "Hoover",
  ":dpulse": "DPulse",
  ":fx_compressor": "FXCompressor",
  ":zawa": "Zawa",
  ":pretty_bell": "PrettyBell",
  ":mod_saw": "ModSaw",
  ":fx_echo": "FXEcho",
  ":fx_nrbpf": "FXNRBPF",
  ":tech_saws": "TechSaws",
  ":growl": "Growl",
  ":dtri": "DTri",
  ":fx_replace_reverb": "FXReverb",
  ":sound_in": "SoundIn",
  ":sound_in_stereo": "SoundInStereo",
  ":gnoise": "GNoise",
  ":fx_flanger": "FXFlanger",
  ":main_mixer": "MainMixer",
  ":fx_rhpf": "FXRHPF",
  ":fx_pan": "FXPan",
  ":fx_replace_pan": "FXPan",
  ":stereo_player": "StereoPlayer",
  ":sine": "Beep",
  ":noise": "Noise",
  ":cnoise": "CNoise",
  ":fx_pitch_shift": "FXPitchShift",
  ":fx_nrlpf": "FXNormRLPF",
  ":mod_sine": "ModSine",
  ":fx_whammy": "FXWhammy",
  ":fx_level": "FXLevel",
  ":basic_stereo_player": "BasicStereoPlayer",
  ":fx_replace_distortion": "FXDistortion",
  ":fx_krush": "FXKrush",
  ":fx_bitcrusher": "FXBitcrusher",
  ":pulse": "Pulse",
  ":mod_fm": "ModFM",
  ":fm": "FM",
  ":fx_rbpf": "FXRBPF",
  ":basic_mixer": "BasicMixer",
  ":chipbass": "ChipBass",
  ":fx_rlpf": "FXRLPF"
}

fx = {
  "FXInfo": {
    "hiden": true,
    "opts": {
      "pre_mix_slide_shape": 1,
      "amp_slide": 0,
      "mix": 1,
      "mix_slide_shape": 1,
      "pre_amp_slide_shape": 1,
      "amp_slide_shape": 1,
      "amp": 1,
      "mix_slide": 0,
      "pre_amp_slide_curve": 0,
      "amp_slide_curve": 0,
      "pre_mix_slide": 0,
      "pre_mix_slide_curve": 0,
      "pre_mix": 1,
      "mix_slide_curve": 0,
      "pre_amp": 1,
      "pre_amp_slide": 0
    },
    "inherit_arg": false,
    "inherit_base": "BaseInfo"
  },
  "FXVowel": {
    "name": ":fx_vowel",
    "hiden": false,
    "summary": "Vowel",
    "opts": {
      "pre_mix_slide_shape": 1,
      "mix": 1,
      "amp_slide_shape": 1,
      "pre_amp": 1,
      "voice": 0,
      "mix_slide": 0,
      "vowel_sound": 1,
      "pre_amp_slide_curve": 0,
      "pre_mix": 1,
      "mix_slide_curve": 0,
      "pre_amp_slide": 0,
      "mix_slide_shape": 1,
      "pre_amp_slide_shape": 1,
      "amp_slide": 0,
      "amp": 1,
      "amp_slide_curve": 0,
      "pre_mix_slide": 0,
      "pre_mix_slide_curve": 0
    },
    "inherit_arg": true,
    "inherit_base": "FXInfo"
  },
  "FXBPF": {
    "name": ":fx_bpf",
    "hiden": false,
    "summary": "Band Pass Filter",
    "opts": {
      "pre_mix_slide_shape": 1,
      "mix": 1,
      "amp_slide_shape": 1,
      "centre": 100,
      "pre_amp": 1,
      "mix_slide": 0,
      "res": 0.6,
      "res_slide": 0,
      "pre_amp_slide_curve": 0,
      "pre_mix": 1,
      "mix_slide_curve": 0,
      "pre_amp_slide": 0,
      "mix_slide_shape": 1,
      "pre_amp_slide_shape": 1,
      "amp_slide": 0,
      "amp": 1,
      "amp_slide_curve": 0,
      "res_slide_shape": 1,
      "pre_mix_slide": 0,
      "pre_mix_slide_curve": 0,
      "res_slide_curve": 0,
      "centre_slide_curve": 0,
      "centre_slide_shape": 1,
      "centre_slide": 0
    },
    "inherit_arg": true,
    "inherit_base": "FXInfo"
  },
  "FXFlanger": {
    "name": ":fx_flanger",
    "hiden": false,
    "summary": "Flanger",
    "opts": {
      "invert_flange": 0,
      "pre_mix_slide_shape": 1,
      "depth": 5,
      "feedback_slide_curve": 0,
      "mix": 1,
      "stereo_invert_wave": 0,
      "amp_slide_shape": 1,
      "delay_slide_curve": 0,
      "pre_amp": 1,
      "decay_slide_curve": 0,
      "mix_slide": 0,
      "feedback": 0,
      "depth_slide_shape": 1,
      "decay_slide_shape": 1,
      "depth_slide_curve": 0,
      "pre_amp_slide_curve": 0,
      "pre_mix": 1,
      "delay_slide_shape": 1,
      "decay_slide": 0,
      "mix_slide_curve": 0,
      "pre_amp_slide": 0,
      "delay": 5,
      "mix_slide_shape": 1,
      "feedback_slide_shape": 1,
      "max_delay": 20,
      "invert_wave": 0,
      "pre_amp_slide_shape": 1,
      "amp_slide": 0,
      "amp": 1,
      "feedback_slide": 0,
      "phase_offset": 0,
      "decay": 2,
      "amp_slide_curve": 0,
      "delay_slide": 0,
      "phase_slide_curve": 0,
      "pre_mix_slide": 0,
      "phase_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "depth_slide": 0,
      "wave": 4,
      "phase": 4,
      "phase_slide": 0
    },
    "inherit_arg": true,
    "inherit_base": "FXInfo"
  },
  "FXRHPF": {
    "name": ":fx_rhpf",
    "hiden": true,
    "summary": "Resonant High Pass Filter",
    "opts": {
      "pre_mix_slide_shape": 1,
      "mix": 1,
      "amp_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "mix_slide": 0,
      "res": 0.5,
      "cutoff_slide": 0,
      "res_slide": 0,
      "pre_amp": 1,
      "pre_mix": 1,
      "cutoff": 100,
      "mix_slide_curve": 0,
      "pre_amp_slide": 0,
      "mix_slide_shape": 1,
      "pre_amp_slide_shape": 1,
      "amp_slide": 0,
      "amp": 1,
      "cutoff_slide_shape": 1,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "pre_mix_slide": 0,
      "pre_mix_slide_curve": 0,
      "res_slide_curve": 0,
      "res_slide_shape": 1
    },
    "inherit_arg": true,
    "inherit_base": "FXHPF"
  },
  "FXRingMod": {
    "name": ":fx_ring_mod",
    "hiden": false,
    "summary": "Ring Modulator",
    "opts": {
      "freq": 30,
      "pre_mix_slide_shape": 1,
      "mod_amp_slide_curve": 0,
      "mix": 1,
      "amp_slide_shape": 1,
      "pre_amp": 1,
      "mix_slide": 0,
      "freq_slide": 0,
      "pre_amp_slide_curve": 0,
      "pre_mix": 1,
      "freq_slide_shape": 1,
      "mix_slide_curve": 0,
      "mod_amp_slide": 0,
      "pre_amp_slide": 0,
      "mix_slide_shape": 1,
      "pre_amp_slide_shape": 1,
      "amp_slide": 0,
      "mod_amp_slide_shape": 1,
      "amp": 1,
      "amp_slide_curve": 0,
      "pre_mix_slide": 0,
      "pre_mix_slide_curve": 0,
      "mod_amp": 1,
      "freq_slide_curve": 0
    },
    "inherit_arg": true,
    "inherit_base": "FXInfo"
  },
  "FXChorus": {
    "name": ":fx_chorus",
    "hiden": true,
    "summary": "Chorus",
    "opts": {
      "pre_mix_slide_shape": 1,
      "max_phase": 1,
      "mix": 1,
      "amp_slide_shape": 1,
      "pre_amp": 1,
      "decay_slide_curve": 0,
      "mix_slide": 0,
      "decay_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "pre_mix": 1,
      "decay_slide": 0,
      "mix_slide_curve": 0,
      "pre_amp_slide": 0,
      "mix_slide_shape": 1,
      "pre_amp_slide_shape": 1,
      "amp_slide": 0,
      "amp": 1,
      "decay": 1e-05,
      "amp_slide_curve": 0,
      "pre_mix_slide": 0,
      "phase_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "phase_slide_curve": 0,
      "phase": 0.25,
      "phase_slide": 0
    },
    "inherit_arg": true,
    "inherit_base": "FXInfo"
  },
  "FXPan": {
    "name": ":fx_pan",
    "hiden": false,
    "summary": "Pan",
    "opts": {
      "pre_mix_slide_shape": 1,
      "mix": 1,
      "pan_slide_curve": 0,
      "amp_slide_shape": 1,
      "pre_amp": 1,
      "mix_slide": 0,
      "pre_amp_slide_curve": 0,
      "pre_mix": 1,
      "mix_slide_curve": 0,
      "pre_amp_slide": 0,
      "mix_slide_shape": 1,
      "pan_slide_shape": 1,
      "pre_amp_slide_shape": 1,
      "amp_slide": 0,
      "amp": 1,
      "pan_slide": 0,
      "pan": 0,
      "amp_slide_curve": 0,
      "pre_mix_slide": 0,
      "pre_mix_slide_curve": 0
    },
    "inherit_arg": true,
    "inherit_base": "FXInfo"
  },
  "FXPitchShift": {
    "name": ":fx_pitch_shift",
    "hiden": false,
    "summary": "Pitch shift",
    "opts": {
      "time_dis": 0.0,
      "pre_mix_slide_shape": 1,
      "pitch_dis_slide_curve": 0,
      "mix": 1,
      "amp_slide_shape": 1,
      "pitch_slide": 0,
      "pre_amp": 1,
      "mix_slide": 0,
      "time_dis_slide": 0,
      "window_size": 0.2,
      "time_dis_slide_curve": 0,
      "pitch_dis_slide_shape": 1,
      "window_size_slide_curve": 0,
      "pre_amp_slide_curve": 0,
      "pre_mix": 1,
      "pitch": 0,
      "mix_slide_curve": 0,
      "pre_amp_slide": 0,
      "mix_slide_shape": 1,
      "pitch_dis_slide": 0,
      "time_dis_slide_shape": 1,
      "pre_amp_slide_shape": 1,
      "amp_slide": 0,
      "amp": 1,
      "window_size_slide": 0,
      "amp_slide_curve": 0,
      "pre_mix_slide": 0,
      "pre_mix_slide_curve": 0,
      "pitch_dis": 0.0,
      "pitch_slide_curve": 0,
      "window_size_slide_shape": 1,
      "pitch_slide_shape": 1
    },
    "inherit_arg": true,
    "inherit_base": "FXInfo"
  },
  "FXNormaliser": {
    "name": ":fx_normaliser",
    "hiden": false,
    "summary": "Normaliser",
    "opts": {
      "pre_mix_slide_shape": 1,
      "mix": 1,
      "amp_slide_shape": 1,
      "pre_amp": 1,
      "level": 1,
      "mix_slide": 0,
      "pre_amp_slide_curve": 0,
      "pre_mix": 1,
      "level_slide_curve": 0,
      "mix_slide_curve": 0,
      "pre_amp_slide": 0,
      "mix_slide_shape": 1,
      "pre_amp_slide_shape": 1,
      "level_slide": 0,
      "amp_slide": 0,
      "amp": 1,
      "amp_slide_curve": 0,
      "pre_mix_slide": 0,
      "pre_mix_slide_curve": 0,
      "level_slide_shape": 1
    },
    "inherit_arg": true,
    "inherit_base": "FXInfo"
  },
  "FXNormHPF": {
    "name": ":fx_nhpf",
    "hiden": true,
    "summary": "Normalised High Pass Filter",
    "opts": {
      "pre_mix_slide_shape": 1,
      "mix": 1,
      "amp_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "mix_slide": 0,
      "cutoff_slide": 0,
      "pre_amp": 1,
      "pre_mix": 1,
      "cutoff": 100,
      "mix_slide_curve": 0,
      "pre_amp_slide": 0,
      "mix_slide_shape": 1,
      "pre_amp_slide_shape": 1,
      "amp_slide": 0,
      "amp": 1,
      "cutoff_slide_shape": 1,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "pre_mix_slide": 0,
      "pre_mix_slide_curve": 0
    },
    "inherit_arg": true,
    "inherit_base": "FXHPF"
  },
  "FXEcho": {
    "name": ":fx_echo",
    "hiden": false,
    "summary": "Echo",
    "opts": {
      "pre_mix_slide_shape": 1,
      "max_phase": 2,
      "mix": 1,
      "amp_slide_shape": 1,
      "pre_amp": 1,
      "decay_slide_curve": 0,
      "mix_slide": 0,
      "decay_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "pre_mix": 1,
      "decay_slide": 0,
      "mix_slide_curve": 0,
      "pre_amp_slide": 0,
      "mix_slide_shape": 1,
      "pre_amp_slide_shape": 1,
      "amp_slide": 0,
      "amp": 1,
      "decay": 2,
      "amp_slide_curve": 0,
      "pre_mix_slide": 0,
      "phase_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "phase_slide_curve": 0,
      "phase": 0.25,
      "phase_slide": 0
    },
    "inherit_arg": true,
    "inherit_base": "FXInfo"
  },
  "FXMono": {
    "name": ":fx_mono",
    "hiden": false,
    "summary": "Mono",
    "opts": {
      "pre_mix_slide_shape": 1,
      "mix": 1,
      "pan_slide_curve": 0,
      "amp_slide_shape": 1,
      "pre_amp": 1,
      "mix_slide": 0,
      "pre_amp_slide_curve": 0,
      "pre_mix": 1,
      "mix_slide_curve": 0,
      "pre_amp_slide": 0,
      "mix_slide_shape": 1,
      "pan_slide_shape": 1,
      "pre_amp_slide_shape": 1,
      "amp_slide": 0,
      "amp": 1,
      "pan_slide": 0,
      "pan": 0,
      "amp_slide_curve": 0,
      "pre_mix_slide": 0,
      "pre_mix_slide_curve": 0
    },
    "inherit_arg": true,
    "inherit_base": "FXInfo"
  },
  "FXNBPF": {
    "name": ":fx_nbpf",
    "hiden": true,
    "summary": "Normalised Band Pass Filter",
    "opts": {
      "pre_mix_slide_shape": 1,
      "mix": 1,
      "amp_slide_shape": 1,
      "centre": 100,
      "pre_amp_slide_curve": 0,
      "mix_slide": 0,
      "pre_amp": 1,
      "pre_mix": 1,
      "mix_slide_curve": 0,
      "pre_amp_slide": 0,
      "mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_amp_slide_shape": 1,
      "amp_slide": 0,
      "amp": 1,
      "amp_slide_curve": 0,
      "res_slide_shape": 1,
      "pre_mix_slide": 0,
      "res_slide": 0,
      "res_slide_curve": 0,
      "res": 0.6,
      "centre_slide_curve": 0,
      "centre_slide": 0,
      "centre_slide_shape": 1
    },
    "inherit_arg": true,
    "inherit_base": "FXBPF"
  },
  "FXTanh": {
    "name": ":fx_tanh",
    "hiden": false,
    "summary": "Hyperbolic Tangent",
    "opts": {
      "pre_mix_slide_shape": 1,
      "mix": 1,
      "krunch_slide_curve": 0,
      "amp_slide_shape": 1,
      "pre_amp": 1,
      "mix_slide": 0,
      "pre_amp_slide_curve": 0,
      "pre_mix": 1,
      "krunch": 5,
      "mix_slide_curve": 0,
      "pre_amp_slide": 0,
      "mix_slide_shape": 1,
      "pre_amp_slide_shape": 1,
      "krunch_slide_shape": 1,
      "amp_slide": 0,
      "amp": 1,
      "amp_slide_curve": 0,
      "pre_mix_slide": 0,
      "pre_mix_slide_curve": 0,
      "krunch_slide": 0
    },
    "inherit_arg": true,
    "inherit_base": "FXInfo"
  },
  "FXLPF": {
    "name": ":fx_lpf",
    "hiden": false,
    "summary": "Low Pass Filter",
    "opts": {
      "pre_mix_slide_shape": 1,
      "mix": 1,
      "amp_slide_shape": 1,
      "pre_amp": 1,
      "mix_slide": 0,
      "cutoff_slide_shape": 1,
      "cutoff_slide": 0,
      "pre_amp_slide_curve": 0,
      "pre_mix": 1,
      "mix_slide_curve": 0,
      "pre_amp_slide": 0,
      "mix_slide_shape": 1,
      "pre_amp_slide_shape": 1,
      "amp_slide": 0,
      "amp": 1,
      "cutoff": 100,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "pre_mix_slide": 0,
      "pre_mix_slide_curve": 0
    },
    "inherit_arg": true,
    "inherit_base": "FXInfo"
  },
  "FXKrush": {
    "name": ":fx_krush",
    "hiden": false,
    "summary": "krush",
    "opts": {
      "pre_mix_slide_shape": 1,
      "mix": 1,
      "amp_slide_shape": 1,
      "pre_amp": 1,
      "mix_slide": 0,
      "res": 0,
      "gain": 5,
      "gain_slide_shape": 1,
      "cutoff_slide": 0,
      "res_slide": 0,
      "pre_amp_slide_curve": 0,
      "pre_mix": 1,
      "cutoff": 100,
      "cutoff_slide_curve": 0,
      "mix_slide_curve": 0,
      "pre_amp_slide": 0,
      "mix_slide_shape": 1,
      "pre_amp_slide_shape": 1,
      "amp_slide": 0,
      "amp": 1,
      "cutoff_slide_shape": 1,
      "amp_slide_curve": 0,
      "res_slide_shape": 1,
      "pre_mix_slide": 0,
      "pre_mix_slide_curve": 0,
      "res_slide_curve": 0,
      "gain_slide__curve": 0,
      "gain_slide": 0
    },
    "inherit_arg": true,
    "inherit_base": "FXInfo"
  },
  "FXOctaver": {
    "name": ":fx_octaver",
    "hiden": false,
    "summary": "Octaver",
    "opts": {
      "subsub_amp": 1,
      "pre_mix_slide_shape": 1,
      "mix": 1,
      "amp_slide_shape": 1,
      "sub_amp": 1,
      "super_amp_slide_curve": 0,
      "pre_amp": 1,
      "mix_slide": 0,
      "sub_amp_slide": 0,
      "super_amp_slide_shape": 1,
      "super_amp": 1,
      "pre_amp_slide_curve": 0,
      "pre_mix": 1,
      "sub_amp_slide_curve": 0,
      "mix_slide_curve": 0,
      "pre_amp_slide": 0,
      "mix_slide_shape": 1,
      "subsub_amp_slide_curve": 0,
      "pre_amp_slide_shape": 1,
      "amp_slide": 0,
      "amp": 1,
      "super_amp_slide": 0,
      "sub_amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "pre_mix_slide": 0,
      "pre_mix_slide_curve": 0,
      "subsub_amp_slide_shape": 1,
      "subsub_amp_slide": 0
    },
    "inherit_arg": true,
    "inherit_base": "FXInfo"
  },
  "FXIXITechno": {
    "name": ":fx_ixi_techno",
    "hiden": false,
    "summary": "Techno from IXI Lang",
    "opts": {
      "pre_mix_slide_shape": 1,
      "mix": 1,
      "phase_slide_shape": 1,
      "amp_slide_shape": 1,
      "cutoff_max": 120,
      "cutoff_min_slide": 0,
      "pre_amp": 1,
      "mix_slide": 0,
      "cutoff_max_slide": 0,
      "res_slide": 0,
      "pre_amp_slide_curve": 0,
      "pre_mix": 1,
      "mix_slide_curve": 0,
      "cutoff_max_slide_curve": 0,
      "pre_amp_slide": 0,
      "mix_slide_shape": 1,
      "cutoff_max_slide_shape": 1,
      "cutoff_min": 60,
      "pre_amp_slide_shape": 1,
      "amp_slide": 0,
      "amp": 1,
      "phase_offset": 0,
      "amp_slide_curve": 0,
      "cutoff_min_slide_curve": 0,
      "res_slide_shape": 1,
      "pre_mix_slide": 0,
      "cutoff_min_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "res_slide_curve": 0,
      "res": 0.8,
      "phase_slide_curve": 0,
      "phase": 4,
      "phase_slide": 0
    },
    "inherit_arg": true,
    "inherit_base": "FXInfo"
  },
  "FXGVerb": {
    "name": ":fx_gverb",
    "hiden": false,
    "summary": "GVerb",
    "opts": {
      "pre_mix_slide_shape": 1,
      "damp": 0.5,
      "mix": 1,
      "amp_slide_shape": 1,
      "spread": 0.5,
      "damp_slide_curve": 0,
      "release": 3,
      "pre_amp": 1,
      "spread_slide": 0,
      "mix_slide": 0,
      "damp_slide_shape": 1,
      "dry": 1,
      "room": 10,
      "pre_amp_slide_curve": 0,
      "pre_mix": 1,
      "pre_damp": 0.5,
      "mix_slide_curve": 0,
      "pre_damp_slide_shape": 1,
      "dry_slide": 0,
      "pre_amp_slide": 0,
      "mix_slide_shape": 1,
      "damp_slide": 0,
      "pre_damp_slide_curve": 0,
      "dry_slide_shape": 1,
      "pre_amp_slide_shape": 1,
      "tail_level": 0.5,
      "amp_slide": 0,
      "spread_slide_curve": 0,
      "amp": 1,
      "pre_damp_slide": 0,
      "amp_slide_curve": 0,
      "dry_slide_curve": 0,
      "pre_mix_slide": 0,
      "pre_mix_slide_curve": 0,
      "ref_level": 0.7,
      "spread_slide_shape": 1
    },
    "inherit_arg": true,
    "inherit_base": "FXInfo"
  },
  "FXNormLPF": {
    "name": ":fx_nlpf",
    "hiden": true,
    "summary": "Normalised Low Pass Filter.",
    "opts": {
      "pre_mix_slide_shape": 1,
      "mix": 1,
      "amp_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "mix_slide": 0,
      "cutoff_slide": 0,
      "pre_amp": 1,
      "pre_mix": 1,
      "cutoff": 100,
      "mix_slide_curve": 0,
      "pre_amp_slide": 0,
      "mix_slide_shape": 1,
      "pre_amp_slide_shape": 1,
      "amp_slide": 0,
      "amp": 1,
      "cutoff_slide_shape": 1,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "pre_mix_slide": 0,
      "pre_mix_slide_curve": 0
    },
    "inherit_arg": true,
    "inherit_base": "FXLPF"
  },
  "FXNRBPF": {
    "name": ":fx_nrbpf",
    "hiden": true,
    "summary": "Normalised Resonant Band Pass Filter",
    "opts": {
      "pre_mix_slide_shape": 1,
      "mix": 1,
      "amp_slide_shape": 1,
      "centre": 100,
      "pre_amp": 1,
      "mix_slide": 0,
      "res": 0.5,
      "res_slide": 0,
      "pre_amp_slide_curve": 0,
      "pre_mix": 1,
      "mix_slide_curve": 0,
      "pre_amp_slide": 0,
      "mix_slide_shape": 1,
      "pre_amp_slide_shape": 1,
      "amp_slide": 0,
      "amp": 1,
      "amp_slide_curve": 0,
      "res_slide_shape": 1,
      "pre_mix_slide": 0,
      "pre_mix_slide_curve": 0,
      "res_slide_curve": 0,
      "centre_slide_curve": 0,
      "centre_slide_shape": 1,
      "centre_slide": 0
    },
    "inherit_arg": true,
    "inherit_base": "FXRBPF"
  },
  "FXWhammy": {
    "name": ":fx_whammy",
    "hiden": false,
    "summary": "Whammy",
    "opts": {
      "pre_mix_slide_shape": 1,
      "transpose_slide_shape": 1,
      "mix": 1,
      "transpose": 12,
      "amp_slide_shape": 1,
      "max_delay_time": 1,
      "pre_amp": 1,
      "grainsize": 0.075,
      "mix_slide": 0,
      "deltime": 0.05,
      "transpose_slide_curve": 0,
      "transpose_slide": 0,
      "pre_amp_slide_curve": 0,
      "pre_mix": 1,
      "mix_slide_curve": 0,
      "pre_amp_slide": 0,
      "mix_slide_shape": 1,
      "pre_amp_slide_shape": 1,
      "amp_slide": 0,
      "amp": 1,
      "amp_slide_curve": 0,
      "pre_mix_slide": 0,
      "pre_mix_slide_curve": 0
    },
    "inherit_arg": true,
    "inherit_base": "FXInfo"
  },
  "FXNormRLPF": {
    "name": ":fx_nrlpf",
    "hiden": true,
    "summary": "Normalised Resonant Low Pass Filter",
    "opts": {
      "pre_mix_slide_shape": 1,
      "mix": 1,
      "res_slide_shape": 1,
      "amp_slide_shape": 1,
      "pre_amp": 1,
      "mix_slide": 0,
      "cutoff_slide_shape": 1,
      "cutoff_slide": 0,
      "pre_amp_slide_curve": 0,
      "pre_mix": 1,
      "mix_slide_curve": 0,
      "pre_amp_slide": 0,
      "mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_amp_slide_shape": 1,
      "amp_slide": 0,
      "amp": 1,
      "cutoff": 100,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "pre_mix_slide": 0,
      "res_slide": 0,
      "res_slide_curve": 0,
      "res": 0.5
    },
    "inherit_arg": true,
    "inherit_base": "FXRLPF"
  },
  "FXSlicer": {
    "name": ":fx_slicer",
    "hiden": false,
    "summary": "Slicer",
    "opts": {
      "smooth_down_slide_curve": 0,
      "amp_slide": 0,
      "pulse_width_slide_curve": 0,
      "prob_pos_slide": 0,
      "amp_min_slide_curve": 0,
      "prob_pos_slide_curve": 0,
      "amp_min_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "smooth_slide_curve": 0,
      "amp": 1,
      "smooth_slide": 0,
      "pulse_width_slide": 0,
      "pre_mix": 1,
      "amp_max_slide_curve": 0,
      "phase_offset": 0,
      "phase": 0.25,
      "mix_slide_shape": 1,
      "smooth_up": 0,
      "amp_slide_shape": 1,
      "wave": 1,
      "probability_slide_curve": 0,
      "smooth_up_slide_shape": 1,
      "prob_pos_slide_shape": 1,
      "smooth_down": 0,
      "phase_slide_curve": 0,
      "smooth_slide_shape": 1,
      "pre_mix_slide_shape": 1,
      "mix": 1,
      "smooth": 0,
      "pulse_width": 0.5,
      "prob_pos": 0,
      "mix_slide": 0,
      "smooth_up_slide": 0,
      "pre_amp": 1,
      "probability_slide_shape": 1,
      "pulse_width_slide_shape": 1,
      "probability": 0,
      "mix_slide_curve": 0,
      "probability_slide": 0,
      "pre_amp_slide": 0,
      "smooth_down_slide": 0,
      "smooth_up_slide_curve": 0,
      "invert_wave": 0,
      "pre_amp_slide_shape": 1,
      "amp_max": 1,
      "amp_max_slide": 0,
      "amp_slide_curve": 0,
      "amp_max_slide_shape": 1,
      "pre_mix_slide": 0,
      "phase_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "amp_min_slide": 0,
      "phase_slide": 0,
      "smooth_down_slide_shape": 1,
      "seed": 0,
      "amp_min": 0
    },
    "inherit_arg": true,
    "inherit_base": "FXInfo"
  },
  "FXWobble": {
    "name": ":fx_wobble",
    "hiden": false,
    "summary": "Wobble",
    "opts": {
      "smooth_down_slide_curve": 0,
      "smooth_down": 0,
      "pulse_width_slide_curve": 0,
      "prob_pos_slide": 0,
      "prob_pos_slide_curve": 0,
      "pre_amp_slide_curve": 0,
      "smooth_slide_curve": 0,
      "cutoff_max_slide": 0,
      "wave": 0,
      "smooth_slide": 0,
      "pulse_width_slide": 0,
      "pre_mix": 1,
      "smooth_up_slide_shape": 1,
      "smooth_down_slide": 0,
      "phase": 0.5,
      "mix_slide_shape": 1,
      "smooth_up": 0,
      "probability_slide": 0,
      "cutoff_min": 60,
      "amp_slide": 0,
      "amp": 1,
      "probability_slide_curve": 0,
      "phase_offset": 0,
      "prob_pos_slide_shape": 1,
      "cutoff_min_slide_shape": 1,
      "res_slide": 0,
      "phase_slide_curve": 0,
      "smooth_slide_shape": 1,
      "pre_mix_slide_shape": 1,
      "smooth": 0,
      "mix": 1,
      "amp_slide_shape": 1,
      "cutoff_min_slide_curve": 0,
      "prob_pos": 0,
      "filter": 0,
      "mix_slide": 0,
      "smooth_up_slide": 0,
      "cutoff_min_slide": 0,
      "pre_amp": 1,
      "probability_slide_shape": 1,
      "pulse_width_slide_shape": 1,
      "probability": 0,
      "mix_slide_curve": 0,
      "cutoff_max_slide_curve": 0,
      "pre_amp_slide": 0,
      "res_slide_curve": 0,
      "cutoff_max_slide_shape": 1,
      "invert_wave": 0,
      "pre_amp_slide_shape": 1,
      "pulse_width": 0.5,
      "cutoff_max": 120,
      "res": 0.8,
      "amp_slide_curve": 0,
      "smooth_up_slide_curve": 0,
      "res_slide_shape": 1,
      "pre_mix_slide": 0,
      "phase_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "smooth_down_slide_shape": 1,
      "seed": 0,
      "phase_slide": 0
    },
    "inherit_arg": true,
    "inherit_base": "FXInfo"
  },
  "FXLevel": {
    "name": ":fx_level",
    "hiden": false,
    "summary": "Level Amplifier",
    "opts": {
      "amp_slide_curve": 0,
      "amp_slide": 0,
      "amp": 1,
      "amp_slide_shape": 1
    },
    "inherit_arg": false,
    "inherit_base": "FXInfo"
  },
  "FXDistortion": {
    "name": ":fx_distortion",
    "hiden": false,
    "summary": "Distortion",
    "opts": {
      "pre_mix_slide_shape": 1,
      "mix": 1,
      "distort_slide": 0,
      "amp_slide_shape": 1,
      "pre_amp": 1,
      "distort_slide_shape": 1,
      "mix_slide": 0,
      "distort_slide_curve": 0,
      "pre_amp_slide_curve": 0,
      "pre_mix": 1,
      "mix_slide_curve": 0,
      "pre_amp_slide": 0,
      "mix_slide_shape": 1,
      "distort": 0.5,
      "pre_amp_slide_shape": 1,
      "amp_slide": 0,
      "amp": 1,
      "amp_slide_curve": 0,
      "pre_mix_slide": 0,
      "pre_mix_slide_curve": 0
    },
    "inherit_arg": true,
    "inherit_base": "FXInfo"
  },
  "FXHPF": {
    "name": ":fx_hpf",
    "hiden": false,
    "summary": "High Pass Filter",
    "opts": {
      "pre_mix_slide_shape": 1,
      "mix": 1,
      "amp_slide_shape": 1,
      "pre_amp": 1,
      "mix_slide": 0,
      "cutoff_slide_shape": 1,
      "cutoff_slide": 0,
      "pre_amp_slide_curve": 0,
      "pre_mix": 1,
      "mix_slide_curve": 0,
      "pre_amp_slide": 0,
      "mix_slide_shape": 1,
      "pre_amp_slide_shape": 1,
      "amp_slide": 0,
      "amp": 1,
      "cutoff": 100,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "pre_mix_slide": 0,
      "pre_mix_slide_curve": 0
    },
    "inherit_arg": true,
    "inherit_base": "FXInfo"
  },
  "FXRLPF": {
    "name": ":fx_rlpf",
    "hiden": true,
    "summary": "Resonant Low Pass Filter",
    "opts": {
      "pre_mix_slide_shape": 1,
      "mix": 1,
      "amp_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "mix_slide": 0,
      "res": 0.5,
      "cutoff_slide": 0,
      "res_slide": 0,
      "pre_amp": 1,
      "pre_mix": 1,
      "cutoff": 100,
      "mix_slide_curve": 0,
      "pre_amp_slide": 0,
      "mix_slide_shape": 1,
      "pre_amp_slide_shape": 1,
      "amp_slide": 0,
      "amp": 1,
      "cutoff_slide_shape": 1,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "pre_mix_slide": 0,
      "pre_mix_slide_curve": 0,
      "res_slide_curve": 0,
      "res_slide_shape": 1
    },
    "inherit_arg": true,
    "inherit_base": "FXLPF"
  },
  "FXBitcrusher": {
    "name": ":fx_bitcrusher",
    "hiden": false,
    "summary": "Bitcrusher",
    "opts": {
      "pre_mix_slide_shape": 1,
      "bits_slide_shape": 1,
      "mix": 1,
      "amp_slide_shape": 1,
      "pre_amp": 1,
      "sample_rate": 10000,
      "mix_slide": 0,
      "sample_rate_slide_curve": 0,
      "bits_slide_curve": 0,
      "cutoff_slide": 0,
      "pre_amp_slide_curve": 0,
      "pre_mix": 1,
      "cutoff": 0,
      "mix_slide_curve": 0,
      "sample_rate_slide_shape": 1,
      "pre_amp_slide": 0,
      "mix_slide_shape": 1,
      "pre_amp_slide_shape": 1,
      "amp_slide": 0,
      "sample_rate_slide": 0,
      "amp": 1,
      "cutoff_slide_shape": 1,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "pre_mix_slide": 0,
      "pre_mix_slide_curve": 0,
      "bits": 8,
      "bits_slide": 0
    },
    "inherit_arg": true,
    "inherit_base": "FXInfo"
  },
  "FXReverb": {
    "name": ":fx_reverb",
    "hiden": false,
    "summary": "Reverb",
    "opts": {
      "pre_mix_slide_shape": 1,
      "damp": 0.5,
      "mix": 0.4,
      "amp_slide_shape": 1,
      "damp_slide_curve": 0,
      "pre_amp": 1,
      "mix_slide": 0,
      "damp_slide_shape": 1,
      "room": 0.6,
      "pre_amp_slide_curve": 0,
      "pre_mix": 1,
      "mix_slide_curve": 0,
      "pre_amp_slide": 0,
      "mix_slide_shape": 1,
      "damp_slide": 0,
      "room_slide_shape": 1,
      "pre_amp_slide_shape": 1,
      "amp_slide": 0,
      "amp": 1,
      "amp_slide_curve": 0,
      "pre_mix_slide": 0,
      "pre_mix_slide_curve": 0,
      "room_slide": 0,
      "room_slide_curve": 0
    },
    "inherit_arg": true,
    "inherit_base": "FXInfo"
  },
  "FXBandEQ": {
    "name": ":fx_band_eq",
    "hiden": false,
    "summary": "Band EQ Filter",
    "opts": {
      "freq": 100,
      "pre_mix_slide_shape": 1,
      "mix": 1,
      "amp_slide_shape": 1,
      "pre_amp": 1,
      "mix_slide": 0,
      "res": 0.6,
      "db_slide": 0,
      "res_slide": 0,
      "freq_slide": 0,
      "pre_amp_slide_curve": 0,
      "pre_mix": 1,
      "freq_slide_shape": 1,
      "mix_slide_curve": 0,
      "pre_amp_slide": 0,
      "mix_slide_shape": 1,
      "db_slide_shape": 1,
      "pre_amp_slide_shape": 1,
      "amp_slide": 0,
      "amp": 1,
      "db": 0.6,
      "amp_slide_curve": 0,
      "res_slide_shape": 1,
      "pre_mix_slide": 0,
      "pre_mix_slide_curve": 0,
      "res_slide_curve": 0,
      "db_slide_curve": 0,
      "freq_slide_curve": 0
    },
    "inherit_arg": true,
    "inherit_base": "FXInfo"
  },
  "FXCompressor": {
    "name": ":fx_compressor",
    "hiden": false,
    "summary": "Compressor",
    "opts": {
      "pre_mix_slide_shape": 1,
      "relax_time": 0.01,
      "mix": 1,
      "relax_time_slide_curve": 0,
      "slope_below_slide_shape": 1,
      "amp_slide_shape": 1,
      "threshold_slide": 0,
      "pre_amp": 1,
      "mix_slide": 0,
      "threshold_slide_curve": 0,
      "slope_above": 0.5,
      "threshold_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "pre_mix": 1,
      "clamp_time": 0.01,
      "mix_slide_curve": 0,
      "pre_amp_slide": 0,
      "mix_slide_shape": 1,
      "slope_above_slide_shape": 1,
      "slope_above_slide_curve": 0,
      "relax_time_slide": 0,
      "slope_below_slide": 0,
      "clamp_time_slide_curve": 0,
      "pre_amp_slide_shape": 1,
      "amp_slide": 0,
      "amp": 1,
      "relax_time_slide_shape": 1,
      "clamp_time_slide": 0,
      "amp_slide_curve": 0,
      "threshold": 0.2,
      "pre_mix_slide": 0,
      "pre_mix_slide_curve": 0,
      "slope_above_slide": 0,
      "clamp_time_slide_shape": 1,
      "slope_below": 1,
      "slope_below_slide_curve": 0
    },
    "inherit_arg": true,
    "inherit_base": "FXInfo"
  },
  "FXNormRHPF": {
    "name": ":fx_nrhpf",
    "hiden": true,
    "summary": "Normalised Resonant High Pass Filter",
    "opts": {
      "pre_mix_slide_shape": 1,
      "mix": 1,
      "res_slide_shape": 1,
      "amp_slide_shape": 1,
      "pre_amp": 1,
      "mix_slide": 0,
      "cutoff_slide_shape": 1,
      "cutoff_slide": 0,
      "pre_amp_slide_curve": 0,
      "pre_mix": 1,
      "mix_slide_curve": 0,
      "pre_amp_slide": 0,
      "mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_amp_slide_shape": 1,
      "amp_slide": 0,
      "amp": 1,
      "cutoff": 100,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "pre_mix_slide": 0,
      "res_slide": 0,
      "res_slide_curve": 0,
      "res": 0.5
    },
    "inherit_arg": true,
    "inherit_base": "FXRHPF"
  },
  "FXRBPF": {
    "name": ":fx_rbpf",
    "hiden": true,
    "summary": "Resonant Band Pass Filter",
    "opts": {
      "pre_mix_slide_shape": 1,
      "mix": 1,
      "amp_slide_shape": 1,
      "centre": 100,
      "pre_amp_slide_curve": 0,
      "mix_slide": 0,
      "pre_amp": 1,
      "pre_mix": 1,
      "mix_slide_curve": 0,
      "pre_amp_slide": 0,
      "mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_amp_slide_shape": 1,
      "amp_slide": 0,
      "amp": 1,
      "amp_slide_curve": 0,
      "res_slide_shape": 1,
      "pre_mix_slide": 0,
      "res_slide": 0,
      "res_slide_curve": 0,
      "res": 0.5,
      "centre_slide_curve": 0,
      "centre_slide": 0,
      "centre_slide_shape": 1
    },
    "inherit_arg": true,
    "inherit_base": "FXBPF"
  },
  "FXPanSlicer": {
    "name": ":fx_panslicer",
    "hiden": true,
    "summary": "Pan Slicer",
    "opts": {
      "smooth_down_slide_curve": 0,
      "pulse_width_slide_curve": 0,
      "prob_pos_slide": 0,
      "pre_mix_slide_shape": 1,
      "prob_pos_slide_curve": 0,
      "amp_min_slide_shape": 1,
      "pre_amp": 1,
      "smooth_slide_curve": 0,
      "wave": 1,
      "smooth_slide": 0,
      "pan_max_slide_curve": 0,
      "pulse_width_slide": 0,
      "pre_mix": 1,
      "amp_max_slide_curve": 0,
      "smooth_up_slide_shape": 1,
      "pan_max_slide": 0,
      "phase": 0.25,
      "mix_slide_shape": 1,
      "smooth_up": 0,
      "pan_max": 1,
      "pan_min_slide_curve": 0,
      "amp_slide": 0,
      "amp": 1,
      "probability_slide_curve": 0,
      "phase_offset": 0,
      "pan_min": -1,
      "prob_pos_slide_shape": 1,
      "phase_slide_curve": 0,
      "pan_min_slide": 0,
      "smooth_slide_shape": 1,
      "amp_min_slide_curve": 0,
      "smooth": 0,
      "mix": 1,
      "amp_slide_shape": 1,
      "pulse_width": 0.5,
      "prob_pos": 0,
      "mix_slide": 0,
      "smooth_up_slide": 0,
      "pre_amp_slide_curve": 0,
      "probability_slide_shape": 1,
      "pulse_width_slide_shape": 1,
      "probability": 0,
      "mix_slide_curve": 0,
      "probability_slide": 0,
      "pre_amp_slide": 0,
      "smooth_down_slide": 0,
      "pre_mix_slide_curve": 0,
      "smooth_up_slide_curve": 0,
      "invert_wave": 0,
      "pre_amp_slide_shape": 1,
      "amp_max": 1,
      "amp_max_slide": 0,
      "pan_min_slide_shape": 1,
      "amp_slide_curve": 0,
      "pan_max_slide_shape": 1,
      "amp_max_slide_shape": 1,
      "pre_mix_slide": 0,
      "phase_slide_shape": 1,
      "smooth_down": 0,
      "amp_min_slide": 0,
      "amp_min": 0,
      "smooth_down_slide_shape": 1,
      "seed": 0,
      "phase_slide": 0
    },
    "inherit_arg": true,
    "inherit_base": "FXSlicer"
  }
}

samples = {
  "Sounds of a Tabla Drum": [
    ":tabla_tas1",
    ":tabla_tas2",
    ":tabla_tas3",
    ":tabla_ke1",
    ":tabla_ke2",
    ":tabla_ke3",
    ":tabla_na",
    ":tabla_na_o",
    ":tabla_tun1",
    ":tabla_tun2",
    ":tabla_tun3",
    ":tabla_te1",
    ":tabla_te2",
    ":tabla_te_ne",
    ":tabla_te_m",
    ":tabla_ghe1",
    ":tabla_ghe2",
    ":tabla_ghe3",
    ":tabla_ghe4",
    ":tabla_ghe5",
    ":tabla_ghe6",
    ":tabla_ghe7",
    ":tabla_ghe8",
    ":tabla_dhec",
    ":tabla_na_s",
    ":tabla_re"
  ],
  "Miscellaneous Sounds": [
    ":misc_burp",
    ":misc_crow",
    ":misc_cineboom"
  ],
  "Sounds for Looping": [
    ":loop_industrial",
    ":loop_compus",
    ":loop_amen",
    ":loop_amen_full",
    ":loop_garzul",
    ":loop_mika",
    ":loop_breakbeat",
    ":loop_safari",
    ":loop_tabla"
  ],
  "Sounds featuring guitars": [
    ":guit_harmonics",
    ":guit_e_fifths",
    ":guit_e_slide",
    ":guit_em9"
  ],
  "Ambient Sounds": [
    ":ambi_soft_buzz",
    ":ambi_swoosh",
    ":ambi_drone",
    ":ambi_glass_hum",
    ":ambi_glass_rub",
    ":ambi_haunted_hum",
    ":ambi_piano",
    ":ambi_lunar_land",
    ":ambi_dark_woosh",
    ":ambi_choir"
  ],
  "Vinyl sounds": [
    ":vinyl_backspin",
    ":vinyl_rewind",
    ":vinyl_scratch",
    ":vinyl_hiss"
  ],
  "Electric Sounds": [
    ":elec_triangle",
    ":elec_snare",
    ":elec_lo_snare",
    ":elec_hi_snare",
    ":elec_mid_snare",
    ":elec_cymbal",
    ":elec_soft_kick",
    ":elec_filt_snare",
    ":elec_fuzz_tom",
    ":elec_chime",
    ":elec_bong",
    ":elec_twang",
    ":elec_wood",
    ":elec_pop",
    ":elec_beep",
    ":elec_blip",
    ":elec_blip2",
    ":elec_ping",
    ":elec_bell",
    ":elec_flip",
    ":elec_tick",
    ":elec_hollow_kick",
    ":elec_twip",
    ":elec_plip",
    ":elec_blup"
  ],
  "Bass Drums": [
    ":bd_ada",
    ":bd_pure",
    ":bd_808",
    ":bd_zum",
    ":bd_gas",
    ":bd_sone",
    ":bd_haus",
    ":bd_zome",
    ":bd_boom",
    ":bd_klub",
    ":bd_fat",
    ":bd_tek"
  ],
  "Drum Sounds": [
    ":drum_heavy_kick",
    ":drum_tom_mid_soft",
    ":drum_tom_mid_hard",
    ":drum_tom_lo_soft",
    ":drum_tom_lo_hard",
    ":drum_tom_hi_soft",
    ":drum_tom_hi_hard",
    ":drum_splash_soft",
    ":drum_splash_hard",
    ":drum_snare_soft",
    ":drum_snare_hard",
    ":drum_cymbal_soft",
    ":drum_cymbal_hard",
    ":drum_cymbal_open",
    ":drum_cymbal_closed",
    ":drum_cymbal_pedal",
    ":drum_bass_soft",
    ":drum_bass_hard",
    ":drum_cowbell",
    ":drum_roll"
  ],
  "Bass Sounds": [
    ":bass_hit_c",
    ":bass_hard_c",
    ":bass_thick_c",
    ":bass_drop_c",
    ":bass_woodsy_c",
    ":bass_voxy_c",
    ":bass_voxy_hit_c",
    ":bass_dnb_f"
  ],
  "Snare Drums": [
    ":sn_dub",
    ":sn_dolf",
    ":sn_zome"
  ],
  "Percussive Sounds": [
    ":perc_bell",
    ":perc_snap",
    ":perc_snap2",
    ":perc_swash",
    ":perc_till"
  ]
}

