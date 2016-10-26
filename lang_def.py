null = None; true = True; false = False;
#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/

lang_core = {
  "live_loop": {
    "async_block": true,
    "opts": {
      "sync_bpm": ":foo",
      "sync": ":foo",
      "auto_cue": true,
      "init": "",
      "delay": 0,
      "seed": 0
    },
    "signature": {
      "&block": null,
      "name": "nil",
      "*args": null
    },
    "introduced": "2,1,0",
    "summary": "A loop for live coding",
    "accepts_block": true,
    "args": [
      {
        "name": ":symbol"
      }
    ],
    "requires_block": true,
    "intro_fn": true
  },
  "with_random_seed": {
    "signature": {
      "&block": null,
      "seed": null
    },
    "introduced": "2,0,0",
    "summary": "Specify random seed for code block",
    "accepts_block": true,
    "args": [
      {
        "seed": ":number"
      }
    ],
    "requires_block": true
  },
  "sync": {
    "opts": {
      "bpm_sync": false
    },
    "signature": {
      "opts": "{}",
      "cue_ids": null
    },
    "introduced": "2,0,0",
    "summary": "Sync with other threads",
    "accepts_block": false,
    "args": [
      {
        "cue_id": ":symbol"
      }
    ],
    "advances_time": true
  },
  "tick": {
    "opts": {
      "step": 1,
      "offset": 0
    },
    "signature": {
      "*args": null
    },
    "introduced": "2,6,0",
    "summary": "Increment a tick and return value",
    "accepts_block": false,
    "returns": ":number",
    "args": [
      {
        "key": ":symbol"
      }
    ],
    "alt_args": [
      {
        "key": ":symbol"
      },
      {
        "value": ":number"
      }
    ]
  },
  "knit": {
    "signature": {
      "*args": null
    },
    "introduced": "2,2,0",
    "summary": "Knit a sequence of repeated values",
    "accepts_block": false,
    "returns": ":ring",
    "args": [
      {
        "value": ":anything"
      },
      {
        "count": ":number"
      }
    ]
  },
  "stretch": {
    "signature": {
      "*args": null
    },
    "introduced": "2,6,0",
    "summary": "Stretch a sequence of values",
    "accepts_block": false,
    "returns": ":ring",
    "args": [
      {
        "list": ":anything"
      },
      {
        "count": ":number"
      }
    ]
  },
  "run_code": {
    "signature": {
      "code": null
    },
    "introduced": "2,11,0",
    "summary": "Evaluate the code passed as a String as a new Run",
    "accepts_block": false,
    "returns": null,
    "args": [
      {
        "code": ":string"
      }
    ]
  },
  "rand_i": {
    "args": [
      {
        "max": ":number_or_range"
      }
    ],
    "signature": {
      "max": 2
    },
    "introduced": "2,0,0",
    "summary": "Generate a random whole number below a value (exclusive)",
    "accepts_block": false
  },
  "rand": {
    "signature": {
      "max": 1
    },
    "introduced": "2,0,0",
    "summary": "Generate a random float below a value",
    "accepts_block": false,
    "args": [
      {
        "max": ":number_or_range"
      }
    ],
    "intro_fn": true
  },
  "dice": {
    "args": [
      {
        "num_sides": ":number"
      }
    ],
    "signature": {
      "num_sides": 6
    },
    "introduced": "2,0,0",
    "summary": "Random dice throw",
    "accepts_block": false
  },
  "tick_reset": {
    "signature": {
      "*args": null
    },
    "introduced": "2,6,0",
    "summary": "Reset tick to 0",
    "returns": ":number",
    "accepts_block": false,
    "alt_args": [
      {
        "key": ":symbol"
      }
    ]
  },
  "puts": {
    "signature": {
      "*msgs": null
    },
    "introduced": "2,0,0",
    "summary": "Display a message in the output pane",
    "accepts_block": false,
    "args": [
      {
        "output": ":anything"
      }
    ],
    "intro_fn": true
  },
  "quantise": {
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
    "introduced": "2,1,0",
    "summary": "Quantise a value to resolution",
    "accepts_block": false
  },
  "rrand": {
    "opts": {
      "step": 1
    },
    "signature": {
      "*opts": null,
      "min": null,
      "max": null
    },
    "introduced": "2,0,0",
    "summary": "Generate a random float between two numbers",
    "accepts_block": false,
    "args": [
      {
        "min": ":number"
      },
      {
        "max": ":number"
      }
    ],
    "intro_fn": true
  },
  "bools": {
    "signature": {
      "*args": null
    },
    "introduced": "2,2,0",
    "summary": "Create a ring of boolean values",
    "accepts_block": false,
    "returns": ":ring",
    "args": [
      {
        "list": ":array"
      }
    ]
  },
  "assert_equal": {
    "signature": {
      "arg2": null,
      "arg1": null,
      "msg": "nil"
    },
    "introduced": "2,8,0",
    "summary": "Ensure args are equal",
    "accepts_block": false,
    "args": [
      {
        "arg1": ":anything"
      },
      {
        "arg2": ":anything"
      }
    ],
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
  "rand_look": {
    "args": [
      {
        "max": ":number_or_range"
      }
    ],
    "signature": {
      "*args": null
    },
    "introduced": "2,11,0",
    "summary": "Generate a random number without consuming a rand",
    "accepts_block": false
  },
  "rand_i_look": {
    "args": [
      {
        "max": ":number_or_range"
      }
    ],
    "signature": {
      "*args": null
    },
    "introduced": "2,11,0",
    "summary": "Generate a random whole number without consuming a rand",
    "accepts_block": false
  },
  "rt": {
    "args": [
      {
        "seconds": ":number"
      }
    ],
    "signature": {
      "t": null
    },
    "introduced": "2,0,0",
    "summary": "Real time conversion",
    "accepts_block": false
  },
  "rand_back": {
    "args": [
      {
        "amount": ":number"
      }
    ],
    "signature": {
      "amount": 1
    },
    "introduced": "2,7,0",
    "summary": "Roll back random generator",
    "accepts_block": false
  },
  "choose": {
    "args": [
      {
        "list": ":array"
      }
    ],
    "signature": {
      "args": null
    },
    "introduced": "2,0,0",
    "summary": "Random list selection",
    "accepts_block": false
  },
  "use_cue_logging": {
    "args": [
      {
        "true_or_false": ":boolean"
      }
    ],
    "signature": {
      "&block": null,
      "v": null
    },
    "introduced": "2,6,0",
    "summary": "Enable and disable cue logging",
    "accepts_block": false
  },
  "osc": {
    "signature": {
      "*args": null,
      "path": null
    }
  },
  "use_osc": {
    "signature": {
      "host_or_port": null,
      "port": "nil"
    }
  },
  "print": {
    "signature": {
      "*msgs": null
    },
    "introduced": "2,0,0",
    "summary": "Display a message in the output pane",
    "accepts_block": false,
    "args": [
      {
        "output": ":anything"
      }
    ],
    "intro_fn": true
  },
  "rrand_i": {
    "args": [
      {
        "min": ":number"
      },
      {
        "max": ":number"
      }
    ],
    "signature": {
      "min": null,
      "max": null
    },
    "introduced": "2,0,0",
    "summary": "Generate a random whole number between two points inclusively",
    "accepts_block": false
  },
  "spread": {
    "opts": {
      "rotate": false
    },
    "signature": {
      "size": null,
      "*args": null,
      "num_accents": null
    },
    "introduced": "2,4,0",
    "summary": "Euclidean distribution for beats",
    "accepts_block": false,
    "returns": ":ring",
    "args": [
      {
        "num_accents": ":number"
      },
      {
        "size": ":number"
      }
    ]
  },
  "run_file": {
    "signature": {
      "path": null
    },
    "introduced": "2,11,0",
    "summary": "Evaluate the contents of the file as a new Run",
    "accepts_block": false,
    "returns": null,
    "args": [
      {
        "filename": ":path"
      }
    ]
  },
  "look": {
    "opts": {
      "offset": 0
    },
    "signature": {
      "*args": null
    },
    "introduced": "2,6,0",
    "summary": "Obtain value of a tick",
    "returns": ":number",
    "accepts_block": false,
    "alt_args": [
      {
        "key": ":symbol"
      }
    ]
  },
  "with_bpm": {
    "signature": {
      "bpm": null,
      "&block": null
    },
    "introduced": "2,0,0",
    "summary": "Set the tempo for the code block",
    "accepts_block": true,
    "args": [
      {
        "bpm": ":number"
      }
    ],
    "requires_block": true
  },
  "at": {
    "async_block": true,
    "signature": {
      "&block": null,
      "times": 0,
      "params": "nil"
    },
    "introduced": "2,1,0",
    "summary": "Asynchronous Time. Run a block at the given time(s)",
    "accepts_block": true,
    "args": [
      {
        "times": ":list"
      },
      {
        "params": ":list"
      }
    ],
    "requires_block": true
  },
  "comment": {
    "accepts_block": true,
    "signature": {
      "&block": null,
      "*args": null
    },
    "introduced": "2,0,0",
    "requires_block": true,
    "summary": "Block level commenting"
  },
  "block_duration": {
    "async_block": false,
    "signature": {
      "&block": null
    },
    "introduced": "2,9,0",
    "summary": "Return block duration",
    "accepts_block": true,
    "args": [],
    "requires_block": true
  },
  "on": {
    "signature": {
      "&blk": null,
      "condition": null
    },
    "introduced": "2,10,0",
    "summary": "Optionally evaluate block",
    "accepts_block": false,
    "returns": null,
    "args": [
      {
        "condition": ":truthy"
      }
    ]
  },
  "time_shift": {
    "signature": {
      "delta": null,
      "&blk": null
    },
    "introduced": "2,11,0",
    "summary": "Slide time forwards or backwards for the given block",
    "accepts_block": true,
    "returns": null,
    "args": [
      {
        "delta_time": ":number"
      }
    ]
  },
  "dec": {
    "opts": {},
    "signature": {
      "n": null
    },
    "introduced": "2, 1, 0",
    "summary": "Decrement",
    "accepts_block": false,
    "args": [
      {
        "n": ":number"
      }
    ]
  },
  "current_beat_duration": {
    "accepts_block": false,
    "introduced": "2,6,0",
    "summary": "Duration of current beat"
  },
  "ndefine": {
    "signature": {
      "name": null,
      "&block": null
    },
    "introduced": "2,1,0",
    "summary": "Define a new function",
    "accepts_block": true,
    "args": [
      {
        "name": ":symbol"
      }
    ],
    "requires_block": true
  },
  "rand_skip": {
    "args": [
      {
        "amount": ":number"
      }
    ],
    "signature": {
      "amount": 1
    },
    "introduced": "2,7,0",
    "summary": "Jump forward random generator",
    "accepts_block": false
  },
  "block_slept?": {
    "async_block": false,
    "signature": {
      "&block": null
    },
    "introduced": "2,9,0",
    "summary": "Determine if block contains sleep time",
    "accepts_block": true,
    "args": [],
    "requires_block": true
  },
  "load_example": {
    "args": [
      {
        "path": ":string"
      }
    ],
    "signature": {
      "example_name": null
    },
    "introduced": "2,10,0",
    "summary": "Load a built-in example",
    "accepts_block": false
  },
  "in_thread": {
    "async_block": true,
    "opts": {
      "sync_bpm": ":foo",
      "name": ":foo",
      "sync": ":foo",
      "delay": 0
    },
    "signature": {
      "&block": null,
      "*opts": null
    },
    "introduced": "2,0,0",
    "summary": "Run code block at the same time",
    "accepts_block": true,
    "requires_block": true
  },
  "bt": {
    "args": [
      {
        "seconds": ":number"
      }
    ],
    "signature": {
      "t": null
    },
    "introduced": "2,8,0",
    "summary": "Beat time conversion",
    "accepts_block": false
  },
  "spark": {
    "introduced": "2,5,0",
    "signature": {
      "*values": null
    },
    "hiden": false,
    "summary": "Print a string representing a list of numeric values as a spark graph/bar chart",
    "accepts_block": false
  },
  "load_buffer": {
    "args": [
      {
        "path": ":string"
      }
    ],
    "signature": {
      "path": null
    },
    "introduced": "2,10,0",
    "summary": "Load the contents of a file to the current buffer",
    "accepts_block": false
  },
  "line": {
    "opts": {
      "steps": 1,
      "inclusive": false
    },
    "signature": {
      "start": null,
      "*args": null,
      "finish": null
    },
    "introduced": "2,5,0",
    "summary": "Create a ring buffer representing a straight line",
    "accepts_block": false,
    "returns": ":ring",
    "args": [
      {
        "start": ":number"
      },
      {
        "finish": ":number"
      }
    ],
    "memoize": true
  },
  "halves": {
    "signature": {
      "start": null,
      "num_halves": 1
    },
    "introduced": "2,10,0",
    "summary": "Create a ring of successive halves",
    "accepts_block": false,
    "returns": ":ring",
    "args": [
      {
        "start": ":number"
      },
      {
        "num_halves": ":int"
      }
    ],
    "memoize": true
  },
  "shuffle": {
    "args": [
      {
        "list": ":array"
      }
    ],
    "signature": {
      "list": null
    },
    "introduced": "2,1,0",
    "summary": "Randomise order of a list",
    "accepts_block": false
  },
  "range": {
    "opts": {
      "step": 1,
      "inclusive": false
    },
    "signature": {
      "start": null,
      "*args": null,
      "finish": null
    },
    "introduced": "2,2,0",
    "summary": "Create a ring buffer with the specified start, finish and step size",
    "accepts_block": false,
    "returns": ":ring",
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
    "memoize": true
  },
  "current_bpm": {
    "accepts_block": false,
    "introduced": "2,0,0",
    "summary": "Get current tempo"
  },
  "rand_reset": {
    "args": [],
    "introduced": "2,7,0",
    "summary": "Reset rand generator to last seed",
    "accepts_block": false
  },
  "wait": {
    "signature": {
      "time": null
    },
    "introduced": "2,0,0",
    "summary": "Wait for duration",
    "accepts_block": false,
    "args": [
      {
        "beats": ":number"
      }
    ],
    "advances_time": true
  },
  "version": {
    "accepts_block": false,
    "introduced": "2,0,0",
    "summary": "Get current version information"
  },
  "pick": {
    "opts": {
      "skip": 0
    },
    "signature": {
      "*args": null
    },
    "introduced": "2,10,0",
    "summary": "Randomly pick from list (with duplicates)",
    "accepts_block": false,
    "args": [
      {
        "list": ":array"
      },
      {
        "n": ":number_or_nil"
      }
    ]
  },
  "ramp": {
    "signature": {
      "*args": null
    },
    "introduced": "2,6,0",
    "summary": "Create a ramp vector",
    "accepts_block": false,
    "returns": ":ramp",
    "args": [
      {
        "list": ":array"
      }
    ]
  },
  "sleep": {
    "signature": {
      "beats": null
    },
    "introduced": "2,0,0",
    "summary": "Wait for beat duration",
    "accepts_block": false,
    "args": [
      {
        "beats": ":number"
      }
    ],
    "advances_time": true
  },
  "tick_reset_all": {
    "alt_args": [
      {
        "key": ":symbol"
      },
      {
        "value": ":number"
      }
    ],
    "introduced": "2,6,0",
    "summary": "Reset all ticks",
    "accepts_block": false,
    "returns": null,
    "args": [
      {
        "value": ":number"
      }
    ]
  },
  "ring": {
    "signature": {
      "*args": null
    },
    "introduced": "2,2,0",
    "summary": "Create a ring buffer",
    "accepts_block": false,
    "returns": ":ring",
    "args": [
      {
        "list": ":array"
      }
    ]
  },
  "current_random_seed": {
    "accepts_block": false,
    "introduced": "2,10,0",
    "summary": "Get current random seed"
  },
  "one_in": {
    "args": [
      {
        "num": ":number"
      }
    ],
    "signature": {
      "num": null
    },
    "introduced": "2,0,0",
    "summary": "Random true value with specified probability",
    "accepts_block": false
  },
  "with_bpm_mul": {
    "signature": {
      "mul": null,
      "&block": null
    },
    "introduced": "2,3,0",
    "summary": "Set new tempo as a multiple of current tempo for block",
    "accepts_block": true,
    "args": [
      {
        "mul": ":number"
      }
    ],
    "requires_block": true
  },
  "beat": {
    "args": [],
    "introduced": "2,10,0",
    "summary": "Get current beat",
    "accepts_block": false
  },
  "vt": {
    "accepts_block": false,
    "introduced": "2,1,0",
    "summary": "Get virtual time"
  },
  "factor?": {
    "args": [
      {
        "val": ":number"
      },
      {
        "factor": ":number"
      }
    ],
    "signature": {
      "val": null,
      "factor": null
    },
    "introduced": "2,1,0",
    "summary": "Factor test",
    "accepts_block": false
  },
  "with_cue_logging": {
    "signature": {
      "&block": null,
      "v": null
    },
    "introduced": "2,6,0",
    "summary": "Block-level enable and disable cue logging",
    "accepts_block": true,
    "args": [
      {
        "true_or_false": ":boolean"
      }
    ],
    "requires_block": true
  },
  "tick_set": {
    "signature": {
      "*args": null
    },
    "introduced": "2,6,0",
    "summary": "Set tick to a specific value",
    "accepts_block": false,
    "returns": ":number",
    "args": [
      {
        "value": ":number"
      }
    ],
    "alt_args": [
      {
        "key": ":symbol"
      },
      {
        "value": ":number"
      }
    ]
  },
  "uncomment": {
    "accepts_block": true,
    "signature": {
      "&block": null,
      "*args": null
    },
    "introduced": "2,0,0",
    "requires_block": true,
    "summary": "Block level comment ignoring"
  },
  "vector": {
    "signature": {
      "*args": null
    },
    "introduced": "2,6,0",
    "summary": "Create a vector",
    "accepts_block": false,
    "returns": ":vector",
    "args": [
      {
        "list": ":array"
      }
    ]
  },
  "clear": {
    "returns": null,
    "args": [],
    "introduced": "2,11,0",
    "summary": "Clear all thread locals to defaults",
    "accepts_block": false
  },
  "doubles": {
    "signature": {
      "start": null,
      "num_doubles": 1
    },
    "introduced": "2,10,0",
    "summary": "Create a ring of successive doubles",
    "accepts_block": false,
    "returns": ":ring",
    "args": [
      {
        "start": ":number"
      },
      {
        "num_doubles": ":int"
      }
    ],
    "memoize": true
  },
  "stop": {
    "returns": null,
    "accepts_block": false,
    "introduced": "2,5,0",
    "summary": "Stop current thread or run"
  },
  "assert": {
    "signature": {
      "arg": null,
      "msg": "nil"
    },
    "introduced": "2,8,0",
    "summary": "Ensure arg is valid",
    "accepts_block": false,
    "args": [
      {
        "arg": ":anything"
      }
    ],
    "alt_args": [
      {
        "arg": ":anything"
      },
      {
        "error_msg": ":string"
      }
    ]
  },
  "inc": {
    "opts": {},
    "signature": {
      "n": null
    },
    "introduced": "2, 1, 0",
    "summary": "Increment",
    "accepts_block": false,
    "args": [
      {
        "n": ":number"
      }
    ]
  },
  "sync_bpm": {
    "opts": {},
    "signature": {
      "opts": "{}",
      "cue_ids": null
    },
    "introduced": "2,10,0",
    "summary": "Sync and inherit BPM from other threads ",
    "accepts_block": false,
    "args": [
      {
        "cue_id": ":symbol"
      }
    ],
    "advances_time": true
  },
  "use_bpm": {
    "signature": {
      "bpm": null,
      "&block": null
    },
    "introduced": "2,0,0",
    "summary": "Set the tempo",
    "accepts_block": false,
    "args": [
      {
        "bpm": ":number"
      }
    ],
    "intro_fn": true
  },
  "rdist": {
    "opts": {
      "step": 1
    },
    "signature": {
      "centre": 0,
      "width": null,
      "*opts": null
    },
    "introduced": "2,3,0",
    "summary": "Random number in centred distribution",
    "accepts_block": false,
    "args": [
      {
        "width": ":number"
      },
      {
        "centre": ":number"
      }
    ],
    "alt_args": [
      {
        "width": ":number"
      }
    ]
  },
  "with_tempo": {
    "signature": {
      "&block": null,
      "*args": null
    }
  },
  "use_bpm_mul": {
    "args": [
      {
        "mul": ":number"
      }
    ],
    "signature": {
      "mul": null,
      "&block": null
    },
    "introduced": "2,3,0",
    "summary": "Set new tempo as a multiple of current tempo",
    "accepts_block": false
  },
  "reset": {
    "returns": null,
    "args": [],
    "introduced": "2,11,0",
    "summary": "Reset all thread locals",
    "accepts_block": false
  },
  "density": {
    "args": [
      {
        "d": ":density"
      }
    ],
    "signature": {
      "&block": null,
      "d": null
    },
    "introduced": "2,3,0",
    "summary": "Squash and repeat time",
    "accepts_block": true
  },
  "use_random_seed": {
    "args": [
      {
        "seed": ":number"
      }
    ],
    "signature": {
      "&block": null,
      "seed": null
    },
    "introduced": "2,0,0",
    "summary": "Set random seed generator to known seed",
    "accepts_block": false
  },
  "spark_graph": {
    "accepts_block": false,
    "signature": {
      "*values": null
    },
    "introduced": "2,5,0",
    "summary": "Returns a string representing a list of numeric values as a spark graph/bar chart"
  },
  "define": {
    "signature": {
      "name": null,
      "&block": null
    },
    "introduced": "2,0,0",
    "summary": "Define a new function",
    "accepts_block": true,
    "args": [
      {
        "name": ":symbol"
      }
    ],
    "requires_block": true,
    "intro_fn": true
  },
  "defonce": {
    "opts": {
      "override": false
    },
    "signature": {
      "name": null,
      "&block": null,
      "*opts": null
    },
    "introduced": "2,0,0",
    "summary": "Define a named value only once",
    "accepts_block": true,
    "args": [
      {
        "name": ":symbol"
      }
    ],
    "requires_block": true
  },
  "cue": {
    "opts": {
      "another_key": "foo: 64",
      "key": "foo: 64",
      "your_key": ":bar"
    },
    "signature": {
      "cue_id": null,
      "*opts": null
    },
    "introduced": "2,0,0",
    "summary": "Cue other threads",
    "accepts_block": false,
    "args": [
      {
        "cue_id": ":symbol"
      }
    ]
  }
}

#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/

lang_sound = {
  "use_merged_sample_defaults": {
    "opts": {},
    "signature": {
      "&block": null,
      "*args": null
    },
    "introduced": "2,9,0",
    "summary": "Merge new sample defaults",
    "accepts_block": false
  },
  "with_sample_defaults": {
    "opts": {},
    "signature": {
      "&block": null,
      "*args": null
    },
    "introduced": "2,5,0",
    "summary": "Block-level use new sample defaults",
    "accepts_block": false,
    "requires_block": false
  },
  "sample_names": {
    "signature": {
      "group": null
    },
    "introduced": "2,0,0",
    "summary": "Get sample names",
    "accepts_block": false,
    "returns": ":ring",
    "args": [
      {
        "group": ":symbol"
      }
    ],
    "memoize": true
  },
  "use_tuning": {
    "args": [
      {
        "tuning": ":symbol"
      },
      {
        "fundamental_note": ":symbol_or_number"
      }
    ],
    "signature": {
      "fundamental_note": ":c",
      "&block": null,
      "tuning": null
    },
    "introduced": "2,6,0",
    "summary": "Use alternative tuning systems",
    "accepts_block": false
  },
  "set_sched_ahead_time!": {
    "signature": {
      "t": null
    },
    "introduced": "2,0,0",
    "summary": "Set sched ahead time globally",
    "modifies_env": true,
    "accepts_block": false,
    "args": [
      {
        "time": ":number"
      }
    ]
  },
  "with_arg_bpm_scaling": {
    "accepts_block": true,
    "signature": {
      "&block": null,
      "bool": null
    },
    "introduced": "2,0,0",
    "requires_block": true,
    "summary": "Block-level enable and disable BPM scaling"
  },
  "sample_free": {
    "signature": {
      "*paths": null
    },
    "introduced": "2,9,0",
    "summary": "Free a sample on the synth server",
    "accepts_block": false,
    "returns": null,
    "args": [
      {
        "path": ":string"
      }
    ]
  },
  "recording_delete": {
    "accepts_block": false,
    "hiden": true
  },
  "sample_groups": {
    "accepts_block": false,
    "memoize": true,
    "introduced": "2,0,0",
    "summary": "Get all sample groups"
  },
  "with_sample_bpm": {
    "opts": {
      "num_beats": 1
    },
    "signature": {
      "sample_name": null,
      "&block": null,
      "*args": null
    },
    "introduced": "2,1,0",
    "summary": "Block-scoped sample-duration-based bpm modification",
    "accepts_block": true,
    "args": [
      {
        "string_or_number": ":sample_name_or_duration"
      }
    ],
    "requires_block": true
  },
  "midi_to_hz": {
    "args": [
      {
        "note": ":symbol_or_number"
      }
    ],
    "signature": {
      "n": null
    },
    "introduced": "2,0,0",
    "summary": "MIDI to Hz conversion",
    "accepts_block": false
  },
  "chord_invert": {
    "signature": {
      "notes": null,
      "shift": null
    },
    "introduced": "2,6,0",
    "summary": "Chord inversion",
    "accepts_block": false,
    "returns": ":ring",
    "args": [
      {
        "notes": ":list"
      },
      {
        "shift": ":number"
      }
    ]
  },
  "with_merged_sample_defaults": {
    "opts": {},
    "signature": {
      "&block": null,
      "*args": null
    },
    "introduced": "2,9,0",
    "summary": "Block-level use merged sample defaults",
    "accepts_block": false,
    "requires_block": false
  },
  "sample_info": {
    "args": [
      {
        "path": ":string"
      }
    ],
    "signature": {
      "*args": null
    },
    "introduced": "2,0,0",
    "summary": "Get sample information",
    "accepts_block": false
  },
  "set_mixer_control!": {
    "opts": {
      "lpf": 131,
      "limiter_bypass": 0,
      "hpf_bypass": 0,
      "hpf": 0,
      "lpf_bypass": 0,
      "pre_amp": 1,
      "amp": 1,
      "leak_dc_bypass": 0
    },
    "signature": {
      "opts": null
    },
    "introduced": "2,7,0",
    "summary": "Control master mixer",
    "accepts_block": false
  },
  "current_octave": {
    "accepts_block": false,
    "introduced": "2,9,0",
    "summary": "Get current octave shift"
  },
  "sample_paths": {
    "signature": {
      "*args": null
    },
    "introduced": "2,10,0",
    "summary": "Sample Pack Filter Resolution",
    "accepts_block": false,
    "returns": ":ring",
    "args": [
      {
        "pre_args": ":source_and_filter_types"
      }
    ]
  },
  "current_sched_ahead_time": {
    "accepts_block": false,
    "introduced": "2,0,0",
    "summary": "Get current sched ahead time"
  },
  "with_timing_warnings": {
    "signature": {
      "&block": null,
      "v": null
    }
  },
  "should_trigger?": {
    "signature": {
      "args_h": null
    }
  },
  "with_octave": {
    "signature": {
      "&block": null,
      "shift": null
    },
    "introduced": "2,9,0",
    "summary": "Block level octave transposition",
    "accepts_block": true,
    "args": [
      {
        "octave_shift": ":number"
      }
    ],
    "intro_fn": true
  },
  "start_amp_monitor": {},
  "reset_mixer!": {
    "opts": {},
    "signature": {
      "": null
    },
    "introduced": "2,9,0",
    "summary": "Reset master mixer",
    "accepts_block": false
  },
  "fx_names": {
    "accepts_block": false,
    "memoize": true,
    "introduced": "2,10,0",
    "summary": "Get all FX names"
  },
  "sample_duration": {
    "opts": {
      "attack": 0,
      "rate": 1,
      "rpitch": 0,
      "pitch_stretch": 1,
      "finish": 1,
      "beat_stretch": 1,
      "start": 0,
      "release": 0,
      "decay": 0,
      "sustain": 1
    },
    "signature": {
      "*args": null
    },
    "introduced": "2,0,0",
    "summary": "Get duration of sample in beats",
    "accepts_block": false,
    "args": [
      {
        "path": ":string"
      }
    ]
  },
  "current_arg_checks": {
    "accepts_block": false,
    "introduced": "2,0,0",
    "summary": "Get current arg checking status"
  },
  "use_synth": {
    "signature": {
      "&block": null,
      "*args": null,
      "synth_name": null
    },
    "introduced": "2,0,0",
    "summary": "Switch current synth",
    "accepts_block": false,
    "args": [
      {
        "synth_name": ":symbol"
      }
    ],
    "intro_fn": true
  },
  "recording_stop": {
    "accepts_block": false,
    "introduced": "2,0,0",
    "hiden": true,
    "summary": "Stop recording"
  },
  "chord_degree": {
    "signature": {
      "degree": null,
      "*opts": null,
      "tonic": null,
      "number_of_notes": 4,
      "scale": ":major"
    },
    "introduced": "2,1,0",
    "summary": "Construct chords of stacked thirds, based on scale degrees",
    "accepts_block": false,
    "returns": ":ring",
    "args": [
      {
        "degree": ":symbol_or_number"
      },
      {
        "tonic": ":symbol"
      },
      {
        "scale": ":symbol"
      },
      {
        "number_of_notes": ":number"
      }
    ],
    "memoize": true
  },
  "with_synth": {
    "signature": {
      "&block": null,
      "*args": null,
      "synth_name": null
    },
    "introduced": "2,0,0",
    "summary": "Block-level synth switching",
    "accepts_block": true,
    "args": [
      {
        "synth_name": ":symbol"
      }
    ],
    "requires_block": true
  },
  "current_debug": {
    "accepts_block": false,
    "introduced": "2,0,0",
    "summary": "Get current debug status"
  },
  "use_sample_defaults": {
    "opts": {},
    "signature": {
      "&block": null,
      "*args": null
    },
    "introduced": "2,5,0",
    "summary": "Use new sample defaults",
    "accepts_block": false
  },
  "scale_names": {
    "accepts_block": false,
    "memoize": true,
    "introduced": "2,6,0",
    "summary": "All scale names"
  },
  "with_synth_defaults": {
    "opts": {},
    "signature": {
      "&block": null,
      "*args": null
    },
    "introduced": "2,0,0",
    "summary": "Block-level use new synth defaults",
    "accepts_block": true,
    "requires_block": true
  },
  "degree": {
    "args": [
      {
        "degree": ":symbol_or_number"
      },
      {
        "tonic": ":symbol"
      },
      {
        "scale": ":symbol"
      }
    ],
    "signature": {
      "degree": null,
      "tonic": null,
      "scale": null
    },
    "introduced": "2,1,0",
    "summary": "Convert a degree into a note",
    "accepts_block": false
  },
  "ratio_to_pitch": {
    "args": [
      {
        "ratio": ":number"
      }
    ],
    "signature": {
      "r": null
    },
    "introduced": "2,7,0",
    "summary": "relative frequency ratio to MIDI pitch",
    "accepts_block": false
  },
  "set_mixer_standard_stereo!": {},
  "use_fx": {
    "signature": {
      "&block": null,
      "*args": null
    }
  },
  "sample_buffer": {
    "args": [
      {
        "path": ":string"
      }
    ],
    "signature": {
      "*args": null
    },
    "introduced": "2,0,0",
    "summary": "Get sample data",
    "accepts_block": false
  },
  "play_chord": {
    "opts": {
      "pan_slide": 1,
      "amp_slide": 1,
      "amp": 1,
      "decay_level": 1,
      "pan": 0,
      "env_curve": 1,
      "release": 0,
      "decay": 0,
      "sustain": 1,
      "sustain_level": 1,
      "attack": 0,
      "attack_level": 1,
      "on": 1,
      "slide": 0,
      "pitch": 0
    },
    "signature": {
      "notes": null,
      "*args": null
    },
    "introduced": "2,0,0",
    "summary": "Play notes simultaneously",
    "accepts_block": false,
    "args": [
      {
        "notes": ":list"
      }
    ]
  },
  "note_range": {
    "opts": {
      "pitches": []
    },
    "signature": {
      "high_note": null,
      "low_note": null,
      "*opts": null
    },
    "introduced": "2,6,0",
    "summary": "Get a range of notes",
    "accepts_block": false,
    "returns": ":ring",
    "args": [
      {
        "low_note": ":note"
      },
      {
        "high_note": ":note"
      }
    ]
  },
  "control": {
    "opts": {},
    "signature": {
      "*args": null
    },
    "introduced": "2,0,0",
    "summary": "Control running synth",
    "accepts_block": false,
    "args": [
      {
        "node": ":synth_node"
      }
    ]
  },
  "recording_save": {
    "signature": {
      "filename": null
    },
    "introduced": "2,0,0",
    "summary": "Save recording",
    "accepts_block": false,
    "args": [
      {
        "path": ":string"
      }
    ],
    "hiden": true
  },
  "use_synth_defaults": {
    "opts": {},
    "signature": {
      "&block": null,
      "*args": null
    },
    "introduced": "2,0,0",
    "summary": "Use new synth defaults",
    "accepts_block": false
  },
  "scale": {
    "opts": {
      "num_octaves": 1
    },
    "signature": {
      "tonic_or_name": null,
      "*opts": null
    },
    "introduced": "2,0,0",
    "summary": "Create scale",
    "accepts_block": false,
    "returns": ":ring",
    "args": [
      {
        "tonic": ":symbol"
      },
      {
        "name": ":symbol"
      }
    ],
    "intro_fn": true,
    "memoize": true
  },
  "sample_split_filts_and_opts": {
    "signature": {
      "args": null
    }
  },
  "use_timing_warnings": {
    "signature": {
      "&block": null,
      "v": null
    }
  },
  "set_mixer_stereo_mode!": {},
  "chord_names": {
    "accepts_block": false,
    "memoize": true,
    "introduced": "2,6,0",
    "summary": "All chord names"
  },
  "load_sample_at_path": {
    "signature": {
      "path": null
    }
  },
  "load_samples": {
    "args": [
      {
        "paths": ":list"
      }
    ],
    "signature": {
      "*args": null
    },
    "introduced": "2,0,0",
    "summary": "Pre-load all matching samples",
    "accepts_block": false
  },
  "sample": {
    "opts": {
      "pitch_dis": 0,
      "lpf_decay": 0,
      "release": 0,
      "lpf_attack_level": 0,
      "pitch_stretch": 1,
      "hpf_init_level": 130,
      "lpf_env_curve": 1,
      "rpitch": 0,
      "hpf_attack": 0,
      "window_size": 0,
      "clamp_time": 0,
      "hpf_max": 200,
      "amp": 1,
      "hpf_env_curve": 1,
      "start": 0,
      "hpf_sustain_level": 0,
      "pan": 0,
      "relax_time": 0,
      "compress": 0,
      "lpf_init_level": 30,
      "hpf_release_level": 0,
      "slope_below": 1,
      "lpf_min": 30,
      "slide": 0,
      "lpf_release_level": 0,
      "lpf_sustain": 0,
      "pitch": 0,
      "hpf_decay_level": 0,
      "slope_above": 1,
      "lpf_decay_level": 0,
      "hpf": 0,
      "hpf_decay": 0,
      "norm": 0,
      "rate": 1,
      "threshold": 0,
      "path": "/path/to/file",
      "beat_stretch": 1,
      "lpf_release": 0,
      "lpf": 131,
      "hpf_release": 0,
      "lpf_sustain_level": 0,
      "hpf_sustain": 0,
      "lpf_attack": 0,
      "sustain": 1,
      "hpf_attack_level": 0,
      "attack": 0,
      "time_dis": 0,
      "onset": 0,
      "finish": 1,
      "pre_amp": 1
    },
    "signature": {
      "&blk": null,
      "*args": null
    },
    "introduced": "2,0,0",
    "summary": "Trigger sample",
    "accepts_block": true,
    "args": [
      {
        "name_or_path": ":symbol_or_string"
      }
    ],
    "intro_fn": true
  },
  "kill": {
    "opts": {},
    "signature": {
      "node": null
    },
    "introduced": "2,0,0",
    "summary": "Kill synth",
    "accepts_block": false,
    "args": [
      {
        "node": ":synth_node"
      }
    ]
  },
  "pitch_ratio": {
    "signature": {
      "*args": null
    }
  },
  "with_arg_checks": {
    "signature": {
      "&block": null,
      "v": null
    },
    "introduced": "2,0,0",
    "summary": "Block-level enable and disable arg checks",
    "accepts_block": true,
    "args": [
      {
        "true_or_false": ":boolean"
      }
    ],
    "requires_block": true
  },
  "current_transpose": {
    "accepts_block": false,
    "introduced": "2,0,0",
    "summary": "Get current transposition"
  },
  "midi_notes": {
    "signature": {
      "*args": null
    },
    "introduced": "2,7,0",
    "summary": "Create a ring buffer of midi note numbers",
    "accepts_block": false,
    "returns": ":ring",
    "args": [
      {
        "list": ":array"
      }
    ],
    "memoize": true
  },
  "current_sample_defaults": {
    "accepts_block": false,
    "introduced": "2,5,0",
    "summary": "Get current sample defaults"
  },
  "with_tuning": {
    "args": [
      {
        "tuning": ":symbol"
      },
      {
        "fundamental_note": ":symbol_or_number"
      }
    ],
    "signature": {
      "fundamental_note": ":c",
      "&block": null,
      "tuning": null
    },
    "introduced": "2,6,0",
    "summary": "Block-level tuning modification",
    "accepts_block": true
  },
  "set_volume!": {
    "signature": {
      "vol": null
    },
    "introduced": "2,0,0",
    "modifies_env": true,
    "summary": "Set Volume globally",
    "accepts_block": false,
    "args": [
      {
        "vol": ":number"
      }
    ]
  },
  "octs": {
    "signature": {
      "start": null,
      "num_octs": 1
    },
    "introduced": "2,8,0",
    "summary": "Create a ring of octaves",
    "accepts_block": false,
    "returns": ":ring",
    "args": [
      {
        "start": ":note"
      },
      {
        "num_octaves": ":pos_int"
      }
    ]
  },
  "resolve_sample_paths": {
    "signature": {
      "filts_and_sources": null
    }
  },
  "note": {
    "opts": {
      "octave": 4
    },
    "signature": {
      "*args": null,
      "n": null
    },
    "introduced": "2,0,0",
    "summary": "Describe note",
    "accepts_block": false,
    "args": [
      {
        "note": ":symbol_or_number"
      }
    ]
  },
  "use_arg_checks": {
    "args": [
      {
        "true_or_false": ":boolean"
      }
    ],
    "signature": {
      "&block": null,
      "v": null
    },
    "introduced": "2,0,0",
    "summary": "Enable and disable arg checks",
    "accepts_block": false
  },
  "note_info": {
    "opts": {
      "octave": 4
    },
    "signature": {
      "*args": null,
      "n": null
    },
    "introduced": "2,0,0",
    "summary": "Get note info",
    "accepts_block": false,
    "args": [
      {
        "note": ":symbol_or_number"
      }
    ]
  },
  "recording_start": {
    "accepts_block": false,
    "introduced": "2,0,0",
    "hiden": true,
    "summary": "Start recording"
  },
  "play_pattern_timed": {
    "opts": {
      "pan_slide": 1,
      "amp_slide": 1,
      "amp": 1,
      "decay_level": 1,
      "pan": 0,
      "env_curve": 1,
      "release": 0,
      "decay": 0,
      "sustain": 1,
      "sustain_level": 1,
      "attack": 0,
      "attack_level": 1,
      "on": 1,
      "slide": 0,
      "pitch": 0
    },
    "signature": {
      "notes": null,
      "*args": null,
      "times": null
    },
    "introduced": "2,0,0",
    "summary": "Play pattern of notes with specific times",
    "accepts_block": false,
    "args": [
      {
        "notes": ":list"
      },
      {
        "times": ":list_or_number"
      }
    ]
  },
  "set_mixer_mono_mode!": {},
  "sample_free_all": {
    "returns": null,
    "args": [],
    "introduced": "2,9,0",
    "summary": "Free all loaded samples on the synth server",
    "accepts_block": false
  },
  "hz_to_midi": {
    "args": [
      {
        "freq": ":number"
      }
    ],
    "signature": {
      "freq": null
    },
    "introduced": "2,0,0",
    "summary": "Hz to MIDI conversion",
    "accepts_block": false
  },
  "with_transpose": {
    "signature": {
      "&block": null,
      "shift": null
    },
    "introduced": "2,0,0",
    "summary": "Block-level note transposition",
    "accepts_block": true,
    "args": [
      {
        "note_shift": ":number"
      }
    ],
    "requires_block": true
  },
  "invert_chord": {
    "signature": {
      "*args": null
    }
  },
  "current_synth": {
    "accepts_block": false,
    "introduced": "2,0,0",
    "summary": "Get current synth"
  },
  "use_octave": {
    "signature": {
      "&block": null,
      "shift": null
    },
    "introduced": "2,9,0",
    "summary": "Note octave transposition",
    "accepts_block": false,
    "args": [
      {
        "octave_shift": ":number"
      }
    ],
    "intro_fn": true
  },
  "load_synthdefs": {
    "args": [
      {
        "path": ":string"
      }
    ],
    "signature": {
      "path": "synthdef_path"
    },
    "introduced": "2,0,0",
    "summary": "Load external synthdefs",
    "accepts_block": false
  },
  "use_debug": {
    "args": [
      {
        "true_or_false": ":boolean"
      }
    ],
    "signature": {
      "&block": null,
      "v": null
    },
    "introduced": "2,0,0",
    "summary": "Enable and disable debug",
    "accepts_block": false
  },
  "play": {
    "opts": {
      "pan_slide": 1,
      "amp_slide": 1,
      "amp": 1,
      "decay_level": 1,
      "pan": 0,
      "env_curve": 1,
      "release": 0,
      "decay": 0,
      "sustain": 1,
      "sustain_level": 1,
      "attack": 0,
      "attack_level": 1,
      "on": 1,
      "slide": 0,
      "pitch": 0
    },
    "signature": {
      "&blk": null,
      "*args": null,
      "n": null
    },
    "introduced": "2,0,0",
    "summary": "Play current synth",
    "accepts_block": true,
    "args": [
      {
        "note": ":symbol_or_number"
      }
    ],
    "intro_fn": true
  },
  "rest?": {
    "args": [
      {
        "note_or_args": ":number_symbol_or_map"
      }
    ],
    "signature": {
      "n": null
    },
    "introduced": "2,1,0",
    "summary": "Determine if note or args is a rest",
    "accepts_block": false
  },
  "sample_loaded?": {
    "args": [
      {
        "path": ":string"
      }
    ],
    "signature": {
      "*args": null
    },
    "introduced": "2,2,0",
    "summary": "Test if sample was pre-loaded",
    "accepts_block": false
  },
  "use_transpose": {
    "signature": {
      "&block": null,
      "shift": null
    },
    "introduced": "2,0,0",
    "summary": "Note transposition",
    "accepts_block": false,
    "args": [
      {
        "note_shift": ":number"
      }
    ],
    "intro_fn": true
  },
  "use_arg_bpm_scaling": {
    "args": [
      {
        "bool": ":boolean"
      }
    ],
    "signature": {
      "&block": null,
      "bool": null
    },
    "introduced": "2,0,0",
    "summary": "Enable and disable BPM scaling",
    "accepts_block": false
  },
  "with_debug": {
    "signature": {
      "&block": null,
      "v": null
    },
    "introduced": "2,0,0",
    "summary": "Block-level enable and disable debug",
    "accepts_block": true,
    "args": [
      {
        "true_or_false": ":boolean"
      }
    ],
    "requires_block": true
  },
  "resolve_sample_path": {
    "signature": {
      "filts_and_sources": null
    }
  },
  "with_afx": {
    "signature": {
      "fx_name": null,
      "&block": null,
      "*args": null
    }
  },
  "synth_names": {
    "accepts_block": false,
    "memoize": true,
    "introduced": "2,9,0",
    "summary": "Get all synth names"
  },
  "current_synth_defaults": {
    "accepts_block": false,
    "introduced": "2,0,0",
    "summary": "Get current synth defaults"
  },
  "synth": {
    "opts": {
      "pan_slide": 1,
      "amp_slide": 1,
      "amp": 1,
      "decay_level": 1,
      "pan": 0,
      "env_curve": 1,
      "release": 0,
      "decay": 0,
      "sustain": 1,
      "sustain_level": 1,
      "attack": 0,
      "attack_level": 1,
      "on": 1,
      "slide": 0,
      "pitch": 0
    },
    "signature": {
      "&blk": null,
      "*args": null,
      "synth_name": null
    },
    "introduced": "2,0,0",
    "summary": "Trigger specific synth",
    "accepts_block": true,
    "args": [
      {
        "synth_name": ":symbol"
      }
    ]
  },
  "use_external_synths": {
    "signature": {
      "&block": null,
      "v": null
    }
  },
  "chord": {
    "opts": {
      "num_octaves": 1,
      "invert": 0
    },
    "signature": {
      "tonic_or_name": null,
      "*opts": null
    },
    "introduced": "2,0,0",
    "summary": "Create chord",
    "accepts_block": false,
    "returns": ":ring",
    "args": [
      {
        "tonic": ":symbol"
      },
      {
        "name": ":symbol"
      }
    ],
    "intro_fn": true,
    "memoize": true
  },
  "play_pattern": {
    "opts": {},
    "signature": {
      "notes": null,
      "*args": null
    },
    "introduced": "2,0,0",
    "summary": "Play pattern of notes",
    "accepts_block": false,
    "args": [
      {
        "notes": ":list"
      }
    ]
  },
  "current_volume": {
    "accepts_block": false,
    "introduced": "2,0,0",
    "summary": "Get current volume"
  },
  "current_amp": {},
  "all_sample_names": {
    "accepts_block": false,
    "memoize": true,
    "introduced": "2,0,0",
    "summary": "Get all sample names"
  },
  "current_cent_tuning": {
    "accepts_block": false,
    "introduced": "2,9,0",
    "summary": "Get current cent shift"
  },
  "status": {
    "accepts_block": false,
    "introduced": "2,0,0",
    "summary": "Get server status"
  },
  "set_control_delta!": {
    "signature": {
      "t": null
    },
    "introduced": "2,1,0",
    "summary": "Set control delta globally",
    "modifies_env": true,
    "accepts_block": false,
    "args": [
      {
        "time": ":number"
      }
    ]
  },
  "with_fx": {
    "opts": {
      "kill_delay": 1,
      "reps": 1
    },
    "signature": {
      "fx_name": null,
      "&block": null,
      "*args": null
    },
    "introduced": "2,0,0",
    "summary": "Use Studio FX",
    "accepts_block": true,
    "args": [
      {
        "fx_name": ":symbol"
      }
    ],
    "requires_block": true,
    "intro_fn": true
  },
  "pitch_to_ratio": {
    "args": [
      {
        "pitch": ":midi_number"
      }
    ],
    "signature": {
      "m": null
    },
    "introduced": "2,5,0",
    "summary": "relative MIDI pitch to frequency ratio",
    "accepts_block": false
  },
  "with_merged_synth_defaults": {
    "opts": {},
    "signature": {
      "&block": null,
      "*args": null
    },
    "introduced": "2,0,0",
    "summary": "Block-level merge synth defaults",
    "accepts_block": true,
    "requires_block": true
  },
  "set_cent_tuning!": {
    "signature": {
      "shift": null
    },
    "introduced": "2,10,0",
    "summary": "Global Cent tuning",
    "accepts_block": false,
    "args": [
      {
        "cent_shift": ":number"
      }
    ],
    "intro_fn": false
  },
  "use_sample_bpm": {
    "opts": {
      "num_beats": 1
    },
    "signature": {
      "sample_name": null,
      "*args": null
    },
    "introduced": "2,1,0",
    "summary": "Sample-duration-based bpm modification",
    "accepts_block": false,
    "args": [
      {
        "string_or_number": ":sample_name_or_duration"
      }
    ]
  },
  "use_cent_tuning": {
    "signature": {
      "&block": null,
      "shift": null
    },
    "introduced": "2,9,0",
    "summary": "Cent tuning",
    "accepts_block": false,
    "args": [
      {
        "cent_shift": ":number"
      }
    ],
    "intro_fn": true
  },
  "truthy?": {
    "signature": {
      "val": null
    }
  },
  "set_mixer_invert_stereo!": {},
  "with_cent_tuning": {
    "signature": {
      "&block": null,
      "shift": null
    },
    "introduced": "2,9,0",
    "summary": "Block-level cent tuning",
    "accepts_block": true,
    "args": [
      {
        "cent_shift": ":number"
      }
    ],
    "requires_block": true
  },
  "load_sample": {
    "args": [
      {
        "path": ":string"
      }
    ],
    "signature": {
      "*args": null
    },
    "introduced": "2,0,0",
    "summary": "Pre-load first matching sample",
    "accepts_block": false
  },
  "with_timing_guarantees": {
    "args": [
      {
        "bool": ":true_or_false"
      }
    ],
    "signature": {
      "&block": null,
      "v": null
    },
    "introduced": "2,10,0",
    "summary": "Block-scoped inhibition of synth triggers if too late",
    "accepts_block": true
  },
  "use_merged_synth_defaults": {
    "opts": {},
    "signature": {
      "&block": null,
      "*args": null
    },
    "introduced": "2,0,0",
    "summary": "Merge synth defaults",
    "accepts_block": false
  },
  "use_timing_guarantees": {
    "args": [
      {
        "bool": ":true_or_false"
      }
    ],
    "signature": {
      "&block": null,
      "v": null
    },
    "introduced": "2,10,0",
    "summary": "Inhibit synth triggers if too late",
    "accepts_block": true
  }
}

sound_args_types_conversion = {}

sound_opts_types_conversion = {}

#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/

synths = {
  "PrettyBell": {
    "opts": {
      "note_slide": 0,
      "pan_slide": 0,
      "pan": 0,
      "env_curve": 2,
      "pan_slide_shape": 1,
      "sustain_level": 1,
      "note_slide_curve": 0,
      "note_slide_shape": 1,
      "pan_slide_curve": 0,
      "note": 52,
      "amp_slide": 0,
      "amp": 1,
      "amp_slide_shape": 1,
      "release": 1,
      "decay": 0,
      "sustain": 0,
      "attack_level": 1,
      "attack": 0,
      "decay_level": 1,
      "amp_slide_curve": 0
    },
    "name": ":pretty_bell",
    "inherit_arg": true,
    "summary": "Pretty Bell",
    "inherit_base": "DullBell",
    "hiden": true
  },
  "ModFM": {
    "opts": {
      "note_slide": 0,
      "decay": 0,
      "divisor_slide_shape": 1,
      "cutoff": 100,
      "pan_slide_shape": 1,
      "mod_wave": 1,
      "mod_pulse_width": 0.5,
      "note_slide_shape": 1,
      "cutoff_slide": 0,
      "note": 52,
      "cutoff_slide_curve": 0,
      "depth_slide_curve": 0,
      "amp_slide": 0,
      "amp": 1,
      "decay_level": 1,
      "mod_phase": 0.25,
      "release": 1,
      "pan": 0,
      "attack_level": 1,
      "mod_range": 5,
      "depth_slide": 0,
      "cutoff_slide_shape": 1,
      "amp_slide_curve": 0,
      "mod_invert_wave": 0,
      "mod_phase_offset": 0,
      "pan_slide": 0,
      "env_curve": 2,
      "divisor_slide_curve": 0,
      "divisor_slide": 0,
      "note_slide_curve": 0,
      "depth": 1,
      "pan_slide_curve": 0,
      "amp_slide_shape": 1,
      "depth_slide_shape": 1,
      "sustain": 0,
      "sustain_level": 1,
      "attack": 0,
      "divisor": 2
    },
    "name": ":mod_fm",
    "inherit_arg": true,
    "summary": "Basic FM synthesis with frequency modulation.",
    "inherit_base": "FM",
    "hiden": true
  },
  "SubPulse": {
    "opts": {
      "note_slide": 0,
      "pan_slide": 0,
      "pan": 0,
      "env_curve": 2,
      "sub_amp": 1,
      "sub_amp_slide": 0,
      "pan_slide_shape": 1,
      "sub_detune_slide_shape": 1,
      "attack": 0,
      "sustain_level": 1,
      "pulse_width_slide": 0,
      "note_slide_curve": 0,
      "pulse_width": 0.5,
      "sub_amp_slide_curve": 0,
      "note_slide_shape": 1,
      "cutoff_slide": 0,
      "pulse_width_slide_shape": 1,
      "pan_slide_curve": 0,
      "note": 52,
      "cutoff_slide_curve": 0,
      "amp_slide": 0,
      "amp": 1,
      "cutoff": 100,
      "release": 1,
      "decay": 0,
      "sustain": 0,
      "attack_level": 1,
      "sub_detune": -12,
      "amp_slide_shape": 1,
      "decay_level": 1,
      "sub_amp_slide_shape": 1,
      "cutoff_slide_shape": 1,
      "amp_slide_curve": 0,
      "sub_detune_slide": 0
    },
    "name": ":subpulse",
    "inherit_arg": true,
    "summary": "Pulse Wave with sub",
    "inherit_base": "Pulse",
    "hiden": true
  },
  "BasicMonoPlayer": {
    "opts": {
      "amp_slide_shape": 1,
      "pan_slide_curve": 0,
      "amp_slide": 0,
      "amp": 1,
      "pan_slide": 0,
      "hpf": -1,
      "pan": 0,
      "lpf_slide_shape": 1,
      "lpf": -1,
      "pan_slide_shape": 1,
      "rate": 1,
      "lpf_slide": 0,
      "amp_slide_curve": 0,
      "hpf_slide_shape": 1,
      "hpf_slide": 0,
      "hpf_slide_curve": 0,
      "lpf_slide_curve": 0
    },
    "name": ":basic_mono_player",
    "inherit_arg": false,
    "summary": "Basic Mono Sample Player (no env)",
    "inherit_base": "StudioInfo",
    "hiden": true
  },
  "Singer": {
    "opts": {
      "amp_slide_shape": 1,
      "pan_slide_curve": 0,
      "note": 52,
      "note_slide": 0,
      "amp_slide": 0,
      "amp": 1,
      "pan_slide": 0,
      "decay": 0,
      "env_curve": 2,
      "release": 4.0,
      "pan": 0,
      "sustain": 0,
      "attack_level": 1,
      "pan_slide_shape": 1,
      "attack": 1,
      "decay_level": 1,
      "sustain_level": 1,
      "note_slide_curve": 0,
      "amp_slide_curve": 0,
      "note_slide_shape": 1
    },
    "name": ":singer",
    "inherit_arg": false,
    "summary": "Singer",
    "inherit_base": "SonicPiSynth",
    "hiden": true
  },
  "ModPulse": {
    "opts": {
      "pulse_width_slide_curve": 0,
      "mod_phase_offset": 0,
      "note_slide": 0,
      "pan_slide": 0,
      "pan": 0,
      "env_curve": 2,
      "mod_pulse_width_slide_curve": 0,
      "mod_range_slide_shape": 1,
      "mod_range_slide_curve": 0,
      "pan_slide_shape": 1,
      "mod_pulse_width_slide": 0,
      "attack": 0,
      "sustain_level": 1,
      "pulse_width_slide": 0,
      "note_slide_curve": 0,
      "mod_wave": 1,
      "mod_pulse_width": 0.5,
      "mod_phase_slide": 0,
      "note_slide_shape": 1,
      "cutoff_slide": 0,
      "pulse_width_slide_shape": 1,
      "pan_slide_curve": 0,
      "note": 52,
      "cutoff_slide_curve": 0,
      "amp_slide": 0,
      "amp": 1,
      "amp_slide_shape": 1,
      "mod_phase": 0.25,
      "release": 1,
      "decay": 0,
      "sustain": 0,
      "attack_level": 1,
      "mod_pulse_width_slide_shape": 1,
      "cutoff": 100,
      "mod_range": 5,
      "decay_level": 1,
      "cutoff_slide_shape": 1,
      "mod_phase_slide_shape": 1,
      "amp_slide_curve": 0,
      "mod_invert_wave": 0,
      "mod_phase_slide_curve": 0,
      "mod_range_slide": 0,
      "pulse_width": 0.5
    },
    "name": ":mod_pulse",
    "inherit_arg": false,
    "summary": "Modulated Pulse",
    "inherit_base": "SonicPiSynth",
    "hiden": false
  },
  "BasicMixer": {
    "opts": {
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "amp_slide": 0.1,
      "amp": 1
    },
    "name": ":basic_mixer",
    "inherit_arg": false,
    "summary": "Basic Mixer",
    "inherit_base": "BaseMixer",
    "hiden": true
  },
  "Beep": {
    "opts": {
      "amp_slide_shape": 1,
      "pan_slide_curve": 0,
      "note": 52,
      "note_slide": 0,
      "amp_slide": 0,
      "amp": 1,
      "pan_slide": 0,
      "decay": 0,
      "env_curve": 2,
      "release": 1,
      "pan": 0,
      "sustain": 0,
      "attack_level": 1,
      "pan_slide_shape": 1,
      "attack": 0,
      "decay_level": 1,
      "sustain_level": 1,
      "note_slide_curve": 0,
      "amp_slide_curve": 0,
      "note_slide_shape": 1
    },
    "name": ":beep",
    "inherit_arg": false,
    "summary": "Sine Wave",
    "inherit_base": "SonicPiSynth",
    "hiden": false
  },
  "Growl": {
    "opts": {
      "res": 0.7,
      "note_slide": 0,
      "pan_slide": 0,
      "pan": 0,
      "env_curve": 2,
      "res_slide_shape": 1,
      "res_slide_curve": 0,
      "pan_slide_shape": 1,
      "attack": 0.1,
      "sustain_level": 1,
      "note_slide_curve": 0,
      "note_slide_shape": 1,
      "cutoff_slide": 0,
      "pan_slide_curve": 0,
      "note": 52,
      "cutoff_slide_curve": 0,
      "amp_slide": 0,
      "amp": 1,
      "amp_slide_shape": 1,
      "release": 1,
      "decay": 0,
      "sustain": 0,
      "attack_level": 1,
      "cutoff": 130,
      "decay_level": 1,
      "cutoff_slide_shape": 1,
      "amp_slide_curve": 0,
      "res_slide": 0
    },
    "name": ":growl",
    "inherit_arg": false,
    "summary": "Growl",
    "inherit_base": "SonicPiSynth",
    "hiden": false
  },
  "ChipNoise": {
    "opts": {
      "amp_slide_shape": 0,
      "pan_slide_curve": 0,
      "release": 0,
      "amp_slide": 0,
      "pan_slide_shape": 1,
      "pan_slide": 0,
      "pan": 0,
      "env_curve": 0,
      "amp": 1,
      "decay": 0,
      "sustain": 1,
      "attack_level": 1,
      "freq_band": 0,
      "attack": 0,
      "decay_level": 1,
      "freq_band_slide": 0,
      "sustain_level": 1,
      "amp_slide_curve": 1,
      "freq_band_slide_curve": 0,
      "freq_band_slide_shape": 1
    },
    "name": ":chipnoise",
    "inherit_arg": false,
    "summary": "Chip Noise",
    "inherit_base": "Noise",
    "hiden": true
  },
  "Tri": {
    "opts": {
      "note_slide": 0,
      "pan_slide": 0,
      "pan": 0,
      "env_curve": 2,
      "pan_slide_shape": 1,
      "attack": 0,
      "sustain_level": 1,
      "pulse_width_slide": 0,
      "note_slide_curve": 0,
      "pulse_width": 0.5,
      "note_slide_shape": 1,
      "cutoff_slide": 0,
      "pulse_width_slide_shape": 1,
      "pan_slide_curve": 0,
      "note": 52,
      "cutoff_slide_curve": 0,
      "amp_slide": 0,
      "amp": 1,
      "cutoff": 100,
      "release": 1,
      "decay": 0,
      "sustain": 0,
      "attack_level": 1,
      "amp_slide_shape": 1,
      "decay_level": 1,
      "cutoff_slide_shape": 1,
      "amp_slide_curve": 0
    },
    "name": ":tri",
    "inherit_arg": true,
    "summary": "Triangle Wave",
    "inherit_base": "Pulse",
    "hiden": true
  },
  "Pulse": {
    "opts": {
      "note_slide": 0,
      "pan_slide": 0,
      "decay": 0,
      "env_curve": 2,
      "cutoff": 100,
      "pan_slide_shape": 1,
      "attack_level": 1,
      "pulse_width_slide": 0,
      "note_slide_curve": 0,
      "pulse_width": 0.5,
      "note_slide_shape": 1,
      "cutoff_slide": 0,
      "pulse_width_slide_shape": 1,
      "pan_slide_curve": 0,
      "note": 52,
      "cutoff_slide_curve": 0,
      "amp_slide": 0,
      "amp": 1,
      "amp_slide_shape": 1,
      "release": 1,
      "pan": 0,
      "sustain": 0,
      "sustain_level": 1,
      "attack": 0,
      "decay_level": 1,
      "cutoff_slide_shape": 1,
      "amp_slide_curve": 0
    },
    "name": ":pulse",
    "inherit_arg": true,
    "summary": "Pulse Wave",
    "inherit_base": "Square",
    "hiden": true
  },
  "GNoise": {
    "opts": {
      "res": 0,
      "pan_slide": 0,
      "pan": 0,
      "env_curve": 2,
      "res_slide_shape": 1,
      "cutoff": 110,
      "sustain": 0,
      "pan_slide_shape": 1,
      "attack_level": 1,
      "cutoff_slide": 0,
      "pan_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "amp_slide": 0,
      "amp": 1,
      "amp_slide_shape": 1,
      "release": 1,
      "decay": 0,
      "res_slide_curve": 0,
      "sustain_level": 1,
      "attack": 0,
      "decay_level": 1,
      "cutoff_slide_shape": 1,
      "amp_slide_curve": 0,
      "res_slide": 0
    },
    "name": ":gnoise",
    "inherit_arg": true,
    "summary": "Grey Noise",
    "inherit_base": "Noise",
    "hiden": true
  },
  "Hoover": {
    "opts": {
      "res": 0.1,
      "note_slide": 0,
      "pan_slide": 0,
      "pan": 0,
      "env_curve": 2,
      "res_slide_shape": 1,
      "res_slide_curve": 0,
      "pan_slide_shape": 1,
      "attack": 0.05,
      "sustain_level": 1,
      "note_slide_curve": 0,
      "note_slide_shape": 1,
      "cutoff_slide": 0,
      "pan_slide_curve": 0,
      "note": 52,
      "cutoff_slide_curve": 0,
      "amp_slide": 0,
      "amp": 1,
      "amp_slide_shape": 1,
      "release": 1,
      "decay": 0,
      "sustain": 0,
      "attack_level": 1,
      "cutoff": 130,
      "decay_level": 1,
      "cutoff_slide_shape": 1,
      "amp_slide_curve": 0,
      "res_slide": 0
    },
    "name": ":hoover",
    "inherit_arg": false,
    "summary": "Hoover",
    "inherit_base": "SonicPiSynth",
    "hiden": false
  },
  "SynthPiano": {
    "opts": {
      "note_slide": 0,
      "pan_slide": 0,
      "pan": 0,
      "stereo_width": 0,
      "pan_slide_shape": 1,
      "hard": 0.5,
      "sustain_level": 1,
      "note_slide_curve": 0,
      "note_slide_shape": 1,
      "pan_slide_curve": 0,
      "note": 52,
      "amp_slide": 0,
      "amp": 1,
      "amp_slide_shape": 1,
      "release": 1,
      "decay": 0,
      "sustain": 0,
      "attack_level": 1,
      "attack": 0,
      "decay_level": 1,
      "amp_slide_curve": 0,
      "vel": 0.2
    },
    "name": ":piano",
    "inherit_arg": false,
    "summary": "SynthPiano",
    "inherit_base": "SonicPiSynth",
    "hiden": false
  },
  "BasicStereoPlayer": {
    "opts": {
      "hpf": -1,
      "pan_slide": 0,
      "lpf": -1,
      "pan_slide_shape": 1,
      "rate": 1,
      "hpf_slide_shape": 1,
      "lpf_slide_curve": 0,
      "pan_slide_curve": 0,
      "amp_slide": 0,
      "amp": 1,
      "amp_slide_shape": 1,
      "pan": 0,
      "lpf_slide_shape": 1,
      "lpf_slide": 0,
      "amp_slide_curve": 0,
      "hpf_slide_curve": 0,
      "hpf_slide": 0
    },
    "name": ":basic_stereo_player",
    "inherit_arg": true,
    "summary": "Basic Stereo Sample Player (no env)",
    "inherit_base": "BasicMonoPlayer",
    "hiden": true
  },
  "DarkAmbience": {
    "opts": {
      "res": 0.7,
      "detune1_slide_curve": 0,
      "detune2": 24,
      "detune1_slide": 0,
      "note_slide": 0,
      "pan_slide": 0,
      "pan": 0,
      "env_curve": 2,
      "noise": 0,
      "res_slide_shape": 1,
      "res_slide_curve": 0,
      "pan_slide_shape": 1,
      "detune1": 12,
      "attack": 0,
      "detune2_slide": 0,
      "sustain_level": 1,
      "note_slide_curve": 0,
      "ring": 0.2,
      "detune1_slide_shape": 1,
      "note_slide_shape": 1,
      "cutoff_slide": 0,
      "detune2_slide_shape": 1,
      "pan_slide_curve": 0,
      "note": 52,
      "cutoff_slide_curve": 0,
      "room": 70,
      "amp_slide": 0,
      "amp": 1,
      "amp_slide_shape": 1,
      "reverb_time": 100,
      "release": 1,
      "decay": 0,
      "sustain": 0,
      "attack_level": 1,
      "cutoff": 110,
      "decay_level": 1,
      "cutoff_slide_shape": 1,
      "detune2_slide_curve": 0,
      "amp_slide_curve": 0,
      "res_slide": 0
    },
    "name": ":dark_ambience",
    "inherit_arg": false,
    "summary": "Dark Ambience",
    "inherit_base": "SonicPiSynth",
    "hiden": false
  },
  "SynthInfo": {
    "opts": {},
    "inherit_arg": true,
    "hiden": true,
    "inherit_base": "BaseInfo"
  },
  "ModTri": {
    "opts": {
      "mod_phase_offset": 0,
      "note_slide": 0,
      "pan_slide": 0,
      "pan": 0,
      "env_curve": 2,
      "mod_pulse_width_slide_curve": 0,
      "mod_range_slide_shape": 1,
      "mod_range_slide_curve": 0,
      "pan_slide_shape": 1,
      "mod_pulse_width_slide": 0,
      "attack": 0,
      "sustain_level": 1,
      "note_slide_curve": 0,
      "mod_wave": 1,
      "mod_pulse_width": 0.5,
      "mod_phase_slide": 0,
      "note_slide_shape": 1,
      "cutoff_slide": 0,
      "pan_slide_curve": 0,
      "note": 52,
      "cutoff_slide_curve": 0,
      "amp_slide": 0,
      "amp": 1,
      "amp_slide_shape": 1,
      "mod_phase": 0.25,
      "release": 1,
      "decay": 0,
      "sustain": 0,
      "attack_level": 1,
      "mod_pulse_width_slide_shape": 1,
      "cutoff": 100,
      "mod_range": 5,
      "decay_level": 1,
      "cutoff_slide_shape": 1,
      "mod_phase_slide_shape": 1,
      "amp_slide_curve": 0,
      "mod_invert_wave": 0,
      "mod_phase_slide_curve": 0,
      "mod_range_slide": 0
    },
    "name": ":mod_tri",
    "inherit_arg": false,
    "summary": "Modulated Triangle Wave",
    "inherit_base": "SonicPiSynth",
    "hiden": false
  },
  "StudioInfo": {
    "opts": {},
    "inherit_arg": true,
    "hiden": true,
    "inherit_base": "SonicPiSynth"
  },
  "BaseMixer": {
    "opts": {},
    "inherit_arg": true,
    "hiden": true,
    "inherit_base": "StudioInfo"
  },
  "Pitchless": {
    "opts": {},
    "inherit_arg": true,
    "hiden": true,
    "inherit_base": "SonicPiSynth"
  },
  "Hollow": {
    "opts": {
      "res": 0.99,
      "note_slide": 0,
      "pan_slide": 0,
      "pan": 0,
      "env_curve": 2,
      "noise": 1,
      "res_slide_shape": 1,
      "res_slide_curve": 0,
      "pan_slide_shape": 1,
      "attack": 0,
      "sustain_level": 1,
      "note_slide_curve": 0,
      "note_slide_shape": 1,
      "cutoff_slide": 0,
      "pan_slide_curve": 0,
      "note": 52,
      "cutoff_slide_curve": 0,
      "amp_slide": 0,
      "amp": 1,
      "amp_slide_shape": 1,
      "release": 1,
      "decay": 0,
      "sustain": 0,
      "attack_level": 1,
      "cutoff": 90,
      "decay_level": 1,
      "cutoff_slide_shape": 1,
      "amp_slide_curve": 0,
      "norm": 0,
      "res_slide": 0
    },
    "name": ":hollow",
    "inherit_arg": false,
    "summary": "Hollow",
    "inherit_base": "SonicPiSynth",
    "hiden": false
  },
  "MainMixer": {
    "opts": {
      "pre_amp_slide": 0.02,
      "force_mono": 0,
      "hpf_bypass": 0,
      "amp_slide": 0.02,
      "hpf": 0,
      "amp_slide_shape": 1,
      "lpf_bypass": 0,
      "invert_stereo": 0,
      "amp": 1,
      "lpf_slide_curve": 0,
      "hpf_slide_curve": 0,
      "lpf": 135.5,
      "lpf_slide_shape": 1,
      "lpf_slide": 0.02,
      "limiter_bypass": 0,
      "amp_slide_curve": 0,
      "pre_amp": 1,
      "hpf_slide": 0.02,
      "hpf_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "pre_amp_slide_shape": 1
    },
    "name": ":mixer",
    "inherit_arg": false,
    "summary": "Main Mixer",
    "inherit_base": "BaseMixer",
    "hiden": true
  },
  "SynthPluck": {
    "opts": {
      "noise_amp": 0.8,
      "note_slide": 0,
      "pan_slide": 0,
      "pan": 0,
      "pluck_decay": 30,
      "pan_slide_shape": 1,
      "sustain_level": 1,
      "coef": 0.3,
      "note_slide_curve": 0,
      "note_slide_shape": 1,
      "pan_slide_curve": 0,
      "note": 52,
      "amp_slide": 0,
      "amp": 1,
      "amp_slide_shape": 1,
      "release": 1,
      "decay": 0,
      "sustain": 0,
      "attack_level": 1,
      "attack": 0,
      "max_delay_time": 0.125,
      "decay_level": 1,
      "amp_slide_curve": 0
    },
    "name": ":pluck",
    "inherit_arg": false,
    "summary": "SynthPluck",
    "inherit_base": "SonicPiSynth",
    "hiden": false
  },
  "SoundIn": {
    "opts": {
      "amp_slide_shape": 1,
      "pan_slide_curve": 0,
      "release": 0,
      "amp_slide": 0,
      "pan_slide_shape": 1,
      "pan_slide": 0,
      "pan": 0,
      "env_curve": 0,
      "amp": 1,
      "decay": 0,
      "sustain": 1,
      "attack_level": 1,
      "attack": 0,
      "decay_level": 1,
      "sustain_level": 1,
      "amp_slide_curve": 0,
      "input": 1
    },
    "name": ":sound_in",
    "inherit_arg": false,
    "summary": "Sound In",
    "inherit_base": "SonicPiSynth",
    "hiden": false
  },
  "DPulse": {
    "opts": {
      "detune_slide": 0,
      "pulse_width_slide_curve": 0,
      "note_slide": 0,
      "pan_slide": 0,
      "decay": 0,
      "env_curve": 2,
      "detune": 0.1,
      "cutoff": 100,
      "pan_slide_shape": 1,
      "attack_level": 1,
      "pulse_width_slide": 0,
      "note_slide_curve": 0,
      "dpulse_width_slide": 0,
      "pulse_width": 0.5,
      "note_slide_shape": 1,
      "cutoff_slide": 0,
      "pulse_width_slide_shape": 1,
      "pan_slide_curve": 0,
      "note": 52,
      "cutoff_slide_curve": 0,
      "amp_slide": 0,
      "amp": 1,
      "amp_slide_shape": 1,
      "dpulse_width": 0.5,
      "release": 1,
      "pan": 0,
      "sustain": 0,
      "sustain_level": 1,
      "attack": 0,
      "detune_slide_shape": 1,
      "decay_level": 1,
      "cutoff_slide_shape": 1,
      "dpulse_width_slide_shape": 1,
      "detune_slide_curve": 0,
      "amp_slide_curve": 0
    },
    "name": ":dpulse",
    "inherit_arg": true,
    "summary": "Detuned Pulse Wave",
    "inherit_base": "DSaw",
    "hiden": true
  },
  "ModSaw": {
    "opts": {
      "mod_phase_offset": 0,
      "note_slide": 0,
      "pan_slide": 0,
      "pan": 0,
      "env_curve": 2,
      "mod_pulse_width_slide_curve": 0,
      "mod_range_slide_shape": 1,
      "mod_range_slide_curve": 0,
      "pan_slide_shape": 1,
      "mod_pulse_width_slide": 0,
      "attack": 0,
      "sustain_level": 1,
      "note_slide_curve": 0,
      "mod_wave": 1,
      "mod_pulse_width": 0.5,
      "mod_phase_slide": 0,
      "note_slide_shape": 1,
      "cutoff_slide": 0,
      "pan_slide_curve": 0,
      "note": 52,
      "cutoff_slide_curve": 0,
      "amp_slide": 0,
      "amp": 1,
      "amp_slide_shape": 1,
      "mod_phase": 0.25,
      "release": 1,
      "decay": 0,
      "sustain": 0,
      "attack_level": 1,
      "mod_pulse_width_slide_shape": 1,
      "cutoff": 100,
      "mod_range": 5,
      "decay_level": 1,
      "cutoff_slide_shape": 1,
      "mod_phase_slide_shape": 1,
      "amp_slide_curve": 0,
      "mod_invert_wave": 0,
      "mod_phase_slide_curve": 0,
      "mod_range_slide": 0
    },
    "name": ":mod_saw",
    "inherit_arg": false,
    "summary": "Modulated Saw Wave",
    "inherit_base": "SonicPiSynth",
    "hiden": false
  },
  "Supersaw": {
    "opts": {
      "res": 0.7,
      "note_slide": 0,
      "pan_slide": 0,
      "pan": 0,
      "env_curve": 2,
      "res_slide_shape": 1,
      "res_slide_curve": 0,
      "pan_slide_shape": 1,
      "attack": 0,
      "sustain_level": 1,
      "note_slide_curve": 0,
      "note_slide_shape": 1,
      "cutoff_slide": 0,
      "pan_slide_curve": 0,
      "note": 52,
      "cutoff_slide_curve": 0,
      "amp_slide": 0,
      "amp": 1,
      "amp_slide_shape": 1,
      "release": 1,
      "decay": 0,
      "sustain": 0,
      "attack_level": 1,
      "cutoff": 130,
      "decay_level": 1,
      "cutoff_slide_shape": 1,
      "amp_slide_curve": 0,
      "res_slide": 0
    },
    "name": ":supersaw",
    "inherit_arg": false,
    "summary": "Supersaw",
    "inherit_base": "SonicPiSynth",
    "hiden": false
  },
  "PNoise": {
    "opts": {
      "res": 0,
      "pan_slide": 0,
      "pan": 0,
      "env_curve": 2,
      "res_slide_shape": 1,
      "cutoff": 110,
      "sustain": 0,
      "pan_slide_shape": 1,
      "attack_level": 1,
      "cutoff_slide": 0,
      "pan_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "amp_slide": 0,
      "amp": 1,
      "amp_slide_shape": 1,
      "release": 1,
      "decay": 0,
      "res_slide_curve": 0,
      "sustain_level": 1,
      "attack": 0,
      "decay_level": 1,
      "cutoff_slide_shape": 1,
      "amp_slide_curve": 0,
      "res_slide": 0
    },
    "name": ":pnoise",
    "inherit_arg": true,
    "summary": "Pink Noise",
    "inherit_base": "Noise",
    "hiden": true
  },
  "Square": {
    "opts": {
      "note_slide": 0,
      "pan_slide": 0,
      "pan": 0,
      "env_curve": 2,
      "pan_slide_shape": 1,
      "attack": 0,
      "sustain_level": 1,
      "note_slide_curve": 0,
      "note_slide_shape": 1,
      "cutoff_slide": 0,
      "pan_slide_curve": 0,
      "note": 52,
      "cutoff_slide_curve": 0,
      "amp_slide": 0,
      "amp": 1,
      "amp_slide_shape": 1,
      "release": 1,
      "decay": 0,
      "sustain": 0,
      "attack_level": 1,
      "cutoff": 100,
      "decay_level": 1,
      "cutoff_slide_shape": 1,
      "amp_slide_curve": 0
    },
    "name": ":square",
    "inherit_arg": false,
    "summary": "Square Wave",
    "inherit_base": "SonicPiSynth",
    "hiden": false
  },
  "ModSine": {
    "opts": {
      "mod_phase_offset": 0,
      "note_slide": 0,
      "pan_slide": 0,
      "pan": 0,
      "env_curve": 2,
      "mod_pulse_width_slide_curve": 0,
      "mod_range_slide_shape": 1,
      "mod_range_slide_curve": 0,
      "pan_slide_shape": 1,
      "mod_pulse_width_slide": 0,
      "attack": 0,
      "sustain_level": 1,
      "note_slide_curve": 0,
      "mod_wave": 1,
      "mod_pulse_width": 0.5,
      "mod_phase_slide": 0,
      "note_slide_shape": 1,
      "cutoff_slide": 0,
      "pan_slide_curve": 0,
      "note": 52,
      "cutoff_slide_curve": 0,
      "amp_slide": 0,
      "amp": 1,
      "amp_slide_shape": 1,
      "mod_phase": 0.25,
      "release": 1,
      "decay": 0,
      "sustain": 0,
      "attack_level": 1,
      "mod_pulse_width_slide_shape": 1,
      "cutoff": 100,
      "mod_range": 5,
      "decay_level": 1,
      "cutoff_slide_shape": 1,
      "mod_phase_slide_shape": 1,
      "amp_slide_curve": 0,
      "mod_invert_wave": 0,
      "mod_phase_slide_curve": 0,
      "mod_range_slide": 0
    },
    "name": ":mod_sine",
    "inherit_arg": false,
    "summary": "Modulated Sine Wave",
    "inherit_base": "SonicPiSynth",
    "hiden": false
  },
  "SynthViolin": {
    "opts": {
      "vibrato_depth_slide_shape": 1,
      "note_slide": 0,
      "pan_slide": 0,
      "pan": 0,
      "env_curve": 2,
      "vibrato_depth": 0.15,
      "vibrato_delay": 0.5,
      "vibrato_rate_slide_curve": 0,
      "pan_slide_shape": 1,
      "attack": 0,
      "vibrato_rate_slide_shape": 1,
      "sustain_level": 1,
      "note_slide_curve": 0,
      "vibrato_depth_slide_curve": 0,
      "note_slide_shape": 1,
      "cutoff_slide": 0,
      "pan_slide_curve": 0,
      "note": 52,
      "cutoff_slide_curve": 0,
      "amp_slide": 0,
      "amp": 1,
      "amp_slide_shape": 1,
      "release": 1,
      "decay": 0,
      "sustain": 0,
      "attack_level": 1,
      "cutoff": 100,
      "decay_level": 1,
      "vibrato_onset": 0.1,
      "cutoff_slide_shape": 1,
      "amp_slide_curve": 0,
      "vibrato_rate": 6
    },
    "name": ":synth_violin",
    "inherit_arg": false,
    "summary": "Blade Runner style strings",
    "inherit_base": "SonicPiSynth",
    "hiden": false
  },
  "DSaw": {
    "opts": {
      "detune_slide": 0,
      "note_slide": 0,
      "pan_slide": 0,
      "pan": 0,
      "env_curve": 2,
      "detune": 0.1,
      "pan_slide_shape": 1,
      "attack": 0,
      "sustain_level": 1,
      "note_slide_curve": 0,
      "note_slide_shape": 1,
      "cutoff_slide": 0,
      "pan_slide_curve": 0,
      "note": 52,
      "cutoff_slide_curve": 0,
      "amp_slide": 0,
      "amp": 1,
      "amp_slide_shape": 1,
      "release": 1,
      "decay": 0,
      "sustain": 0,
      "attack_level": 1,
      "cutoff": 100,
      "detune_slide_shape": 1,
      "decay_level": 1,
      "cutoff_slide_shape": 1,
      "detune_slide_curve": 0,
      "amp_slide_curve": 0
    },
    "name": ":dsaw",
    "inherit_arg": false,
    "summary": "Detuned Saw wave",
    "inherit_base": "SonicPiSynth",
    "hiden": false
  },
  "CNoise": {
    "opts": {
      "res": 0,
      "pan_slide": 0,
      "pan": 0,
      "env_curve": 2,
      "res_slide_shape": 1,
      "cutoff": 110,
      "sustain": 0,
      "pan_slide_shape": 1,
      "attack_level": 1,
      "cutoff_slide": 0,
      "pan_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "amp_slide": 0,
      "amp": 1,
      "amp_slide_shape": 1,
      "release": 1,
      "decay": 0,
      "res_slide_curve": 0,
      "sustain_level": 1,
      "attack": 0,
      "decay_level": 1,
      "cutoff_slide_shape": 1,
      "amp_slide_curve": 0,
      "res_slide": 0
    },
    "name": ":cnoise",
    "inherit_arg": true,
    "summary": "Clip Noise",
    "inherit_base": "Noise",
    "hiden": true
  },
  "DarkSeaHorn": {
    "opts": {
      "amp_slide_shape": 1,
      "pan_slide_curve": 0,
      "note": 52,
      "note_slide": 0,
      "amp_slide": 0,
      "amp": 1,
      "pan_slide": 0,
      "decay": 0,
      "env_curve": 2,
      "release": 4.0,
      "pan": 0,
      "sustain": 0,
      "attack_level": 1,
      "pan_slide_shape": 1,
      "attack": 1,
      "decay_level": 1,
      "sustain_level": 1,
      "note_slide_curve": 0,
      "amp_slide_curve": 0,
      "note_slide_shape": 1
    },
    "name": ":dark_sea_horn",
    "inherit_arg": false,
    "summary": "Dark Sea Horn",
    "inherit_base": "SonicPiSynth",
    "hiden": true
  },
  "DullBell": {
    "opts": {
      "amp_slide_shape": 1,
      "pan_slide_curve": 0,
      "note": 52,
      "note_slide": 0,
      "amp_slide": 0,
      "amp": 1,
      "pan_slide": 0,
      "decay": 0,
      "env_curve": 2,
      "release": 1,
      "pan": 0,
      "sustain": 0,
      "attack_level": 1,
      "pan_slide_shape": 1,
      "attack": 0,
      "decay_level": 1,
      "sustain_level": 1,
      "note_slide_curve": 0,
      "amp_slide_curve": 0,
      "note_slide_shape": 1
    },
    "name": ":dull_bell",
    "inherit_arg": false,
    "summary": "Dull Bell",
    "inherit_base": "SonicPiSynth",
    "hiden": false
  },
  "ChipLead": {
    "opts": {
      "note_slide": 0,
      "pan_slide": 0,
      "pan": 0,
      "env_curve": 2,
      "width": 0,
      "pan_slide_shape": 1,
      "sustain_level": 1,
      "note_slide_curve": 0,
      "note_slide_shape": 1,
      "pan_slide_curve": 0,
      "note": 60,
      "amp_slide": 0,
      "amp": 1,
      "amp_slide_shape": 1,
      "release": 1,
      "decay": 0,
      "sustain": 0,
      "attack_level": 1,
      "attack": 0,
      "note_resolution": 0.1,
      "decay_level": 1,
      "amp_slide_curve": 0
    },
    "name": ":chiplead",
    "inherit_arg": false,
    "summary": "Chip Lead",
    "inherit_base": "SonicPiSynth",
    "hiden": false
  },
  "Saw": {
    "opts": {
      "note_slide": 0,
      "pan_slide": 0,
      "pan": 0,
      "env_curve": 2,
      "pan_slide_shape": 1,
      "sustain_level": 1,
      "note_slide_curve": 0,
      "note_slide_shape": 1,
      "pan_slide_curve": 0,
      "note": 52,
      "amp_slide": 0,
      "amp": 1,
      "amp_slide_shape": 1,
      "release": 1,
      "decay": 0,
      "sustain": 0,
      "attack_level": 1,
      "attack": 0,
      "decay_level": 1,
      "amp_slide_curve": 0
    },
    "name": ":saw",
    "inherit_arg": true,
    "summary": "Saw Wave",
    "inherit_base": "Beep",
    "hiden": true
  },
  "SonicPiSynth": {
    "opts": {},
    "inherit_arg": true,
    "hiden": true,
    "inherit_base": "SynthInfo"
  },
  "ModDSaw": {
    "opts": {
      "detune_slide_shape": 1,
      "detune_slide": 0,
      "mod_phase_offset": 0,
      "note_slide": 0,
      "detune": 0.1,
      "pan_slide": 0,
      "pan": 0,
      "env_curve": 2,
      "mod_pulse_width_slide_curve": 0,
      "mod_range_slide_shape": 1,
      "mod_range_slide_curve": 0,
      "pan_slide_shape": 1,
      "mod_pulse_width_slide": 0,
      "attack": 0,
      "sustain_level": 1,
      "note_slide_curve": 0,
      "mod_wave": 1,
      "mod_pulse_width": 0.5,
      "mod_phase_slide": 0,
      "note_slide_shape": 1,
      "cutoff_slide": 0,
      "pan_slide_curve": 0,
      "note": 52,
      "cutoff_slide_curve": 0,
      "amp_slide": 0,
      "amp": 1,
      "amp_slide_shape": 1,
      "mod_phase": 0.25,
      "release": 1,
      "decay": 0,
      "sustain": 0,
      "attack_level": 1,
      "mod_pulse_width_slide_shape": 1,
      "cutoff": 100,
      "mod_range": 5,
      "decay_level": 1,
      "cutoff_slide_shape": 1,
      "mod_phase_slide_shape": 1,
      "detune_slide_curve": 0,
      "amp_slide_curve": 0,
      "mod_invert_wave": 0,
      "mod_phase_slide_curve": 0,
      "mod_range_slide": 0
    },
    "name": ":mod_dsaw",
    "inherit_arg": false,
    "summary": "Modulated Detuned Saw Waves",
    "inherit_base": "SonicPiSynth",
    "hiden": false
  },
  "StereoPlayer": {
    "opts": {
      "lpf_decay": 0,
      "release": 0,
      "lpf_min_slide": 0,
      "lpf_env_curve": 2,
      "window_size_slide_shape": 1,
      "lpf": -1,
      "pan_slide_shape": 1,
      "slope_above_slide_curve": 0,
      "window_size": 0.2,
      "lpf_slide_curve": 0,
      "amp": 1,
      "hpf_env_curve": 2,
      "start": 0,
      "pitch_slide_shape": 1,
      "decay": 0,
      "lpf_slide_shape": 1,
      "attack_level": 1,
      "compress": 0,
      "relax_time": 0.01,
      "lpf_slide": 0,
      "window_size_slide_curve": 0,
      "amp_slide_curve": 0,
      "lpf_release_level": -1,
      "lpf_sustain": -1,
      "hpf_slide": 0,
      "slope_below": 1,
      "lpf_min": -1,
      "hpf": -1,
      "hpf_decay": 0,
      "slope_above_slide": 0,
      "rate": 1,
      "threshold": 0.2,
      "pitch_dis_slide_shape": 1,
      "slope_below_slide_curve": 0,
      "lpf_release": 0,
      "pre_amp_slide": 0,
      "hpf_attack": 0,
      "lpf_sustain_level": -1,
      "amp_slide_shape": 1,
      "lpf_attack": 0,
      "time_dis_slide_curve": 0,
      "sustain_level": 1,
      "hpf_slide_curve": 0,
      "window_size_slide": 0,
      "clamp_time_slide_shape": 1,
      "time_dis": 0.0,
      "finish": 1,
      "pitch_dis_slide_curve": 0,
      "pre_amp": 1,
      "lpf_min_slide_curve": 0,
      "pre_amp_slide_curve": 0,
      "pitch_dis": 0.0,
      "lpf_attack_level": -1,
      "clamp_time_slide": 0,
      "clamp_time_slide_curve": 0,
      "norm": 0,
      "time_dis_slide_shape": 1,
      "hpf_max_slide_curve": 0,
      "relax_time_slide": 0,
      "hpf_max_slide": 0,
      "lpf_min_slide_shape": 1,
      "hpf_max": -1,
      "clamp_time": 0.01,
      "hpf_max_slide_shape": 1,
      "amp_slide": 0,
      "decay_level": 1,
      "threshold_slide": 0,
      "pan": 0,
      "relax_time_slide_curve": 0,
      "time_dis_slide": 0,
      "pan_slide": 0,
      "lpf_init_level": -1,
      "hpf_release_level": -1,
      "pre_amp_slide_shape": 1,
      "relax_time_slide_shape": 1,
      "threshold_slide_shape": 1,
      "hpf_decay_level": -1,
      "slope_above": 0.5,
      "env_curve": 2,
      "pitch_dis_slide": 0,
      "pitch": 0,
      "threshold_slide_curve": 0,
      "hpf_sustain_level": -1,
      "lpf_decay_level": -1,
      "slope_below_slide_shape": 1,
      "pitch_slide": 0,
      "hpf_init_level": -1,
      "hpf_slide_shape": 1,
      "slope_below_slide": 0,
      "pan_slide_curve": 0,
      "hpf_release": 0,
      "hpf_sustain": -1,
      "sustain": -1,
      "hpf_attack_level": -1,
      "attack": 0,
      "slope_above_slide_shape": 1,
      "pitch_slide_curve": 0
    },
    "name": ":stereo_player",
    "inherit_arg": true,
    "summary": "Stereo Sample Player",
    "inherit_base": "MonoPlayer",
    "hiden": true
  },
  "MonoPlayer": {
    "opts": {
      "lpf_decay": 0,
      "threshold_slide": 0,
      "lpf_min_slide": 0,
      "lpf_env_curve": 2,
      "pan": 0,
      "lpf": -1,
      "pan_slide_shape": 1,
      "relax_time_slide_curve": 0,
      "window_size": 0.2,
      "lpf_slide_curve": 0,
      "amp": 1,
      "hpf_env_curve": 2,
      "start": 0,
      "pitch_slide_shape": 1,
      "decay": 0,
      "lpf_init_level": -1,
      "attack_level": 1,
      "compress": 0,
      "relax_time": 0.01,
      "lpf_slide": 0,
      "window_size_slide_curve": 0,
      "amp_slide_curve": 0,
      "lpf_release_level": -1,
      "lpf_sustain": -1,
      "hpf_slide": 0,
      "slope_below": 1,
      "lpf_min": -1,
      "hpf": -1,
      "hpf_decay": 0,
      "release": 0,
      "slope_above_slide": 0,
      "rate": 1,
      "hpf_release": 0,
      "pitch_dis_slide_shape": 1,
      "pitch": 0,
      "slope_below_slide_curve": 0,
      "lpf_release": 0,
      "pre_amp_slide": 0,
      "hpf_attack": 0,
      "hpf_sustain": -1,
      "time_dis_slide_shape": 1,
      "amp_slide_shape": 1,
      "lpf_attack": 0,
      "time_dis_slide_curve": 0,
      "sustain_level": 1,
      "threshold_slide_shape": 1,
      "window_size_slide": 0,
      "clamp_time_slide_shape": 1,
      "time_dis": 0.0,
      "finish": 1,
      "pitch_dis_slide_curve": 0,
      "pre_amp": 1,
      "lpf_min_slide_curve": 0,
      "pre_amp_slide_curve": 0,
      "pitch_dis": 0.0,
      "lpf_attack_level": -1,
      "clamp_time_slide": 0,
      "clamp_time_slide_curve": 0,
      "relax_time_slide_shape": 1,
      "lpf_min_slide_shape": 1,
      "hpf_max_slide_curve": 0,
      "relax_time_slide": 0,
      "hpf_max_slide": 0,
      "hpf_max": -1,
      "clamp_time": 0.01,
      "hpf_max_slide_shape": 1,
      "amp_slide": 0,
      "decay_level": 1,
      "hpf_sustain_level": -1,
      "window_size_slide_shape": 1,
      "slope_above_slide_curve": 0,
      "time_dis_slide": 0,
      "pan_slide": 0,
      "lpf_slide_shape": 1,
      "hpf_release_level": -1,
      "pre_amp_slide_shape": 1,
      "lpf_decay_level": -1,
      "hpf_slide_curve": 0,
      "hpf_decay_level": -1,
      "slope_above": 0.5,
      "env_curve": 2,
      "pitch_dis_slide": 0,
      "norm": 0,
      "threshold_slide_curve": 0,
      "slope_below_slide_shape": 1,
      "pitch_slide": 0,
      "hpf_init_level": -1,
      "hpf_slide_shape": 1,
      "slope_below_slide": 0,
      "pan_slide_curve": 0,
      "threshold": 0.2,
      "lpf_sustain_level": -1,
      "sustain": -1,
      "hpf_attack_level": -1,
      "attack": 0,
      "slope_above_slide_shape": 1,
      "pitch_slide_curve": 0
    },
    "name": ":mono_player",
    "inherit_arg": false,
    "summary": "Mono Sample Player",
    "inherit_base": "BasicMonoPlayer",
    "hiden": true
  },
  "ChipBass": {
    "opts": {
      "pan_slide_curve": 0,
      "note": 60,
      "note_slide": 0,
      "amp_slide": 0,
      "amp": 1,
      "pan_slide": 0,
      "decay": 0,
      "env_curve": 2,
      "release": 1,
      "pan": 0,
      "sustain": 0,
      "attack_level": 1,
      "amp_slide_shape": 1,
      "note_resolution": 0.1,
      "attack": 0,
      "pan_slide_shape": 1,
      "decay_level": 1,
      "sustain_level": 1,
      "note_slide_curve": 0,
      "amp_slide_curve": 0,
      "note_slide_shape": 1
    },
    "name": ":chipbass",
    "inherit_arg": false,
    "summary": "Chip Bass",
    "inherit_base": "SonicPiSynth",
    "hiden": false
  },
  "FM": {
    "opts": {
      "note_slide": 0,
      "pan_slide": 0,
      "pan": 0,
      "env_curve": 2,
      "depth_slide": 0,
      "divisor_slide_curve": 0,
      "pan_slide_shape": 1,
      "attack": 0,
      "sustain_level": 1,
      "divisor_slide": 0,
      "note_slide_curve": 0,
      "depth": 1,
      "note_slide_shape": 1,
      "cutoff_slide": 0,
      "pan_slide_curve": 0,
      "note": 52,
      "cutoff_slide_curve": 0,
      "depth_slide_curve": 0,
      "amp_slide": 0,
      "amp": 1,
      "amp_slide_shape": 1,
      "depth_slide_shape": 1,
      "release": 1,
      "decay": 0,
      "sustain": 0,
      "attack_level": 1,
      "cutoff": 100,
      "decay_level": 1,
      "cutoff_slide_shape": 1,
      "amp_slide_curve": 0,
      "divisor": 2,
      "divisor_slide_shape": 1
    },
    "name": ":fm",
    "inherit_arg": false,
    "summary": "Basic FM synthesis",
    "inherit_base": "SonicPiSynth",
    "hiden": false
  },
  "BNoise": {
    "opts": {
      "res": 0,
      "pan_slide": 0,
      "pan": 0,
      "env_curve": 2,
      "res_slide_shape": 1,
      "cutoff": 110,
      "sustain": 0,
      "pan_slide_shape": 1,
      "attack_level": 1,
      "cutoff_slide": 0,
      "pan_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "amp_slide": 0,
      "amp": 1,
      "amp_slide_shape": 1,
      "release": 1,
      "decay": 0,
      "res_slide_curve": 0,
      "sustain_level": 1,
      "attack": 0,
      "decay_level": 1,
      "cutoff_slide_shape": 1,
      "amp_slide_curve": 0,
      "res_slide": 0
    },
    "name": ":bnoise",
    "inherit_arg": true,
    "summary": "Brown Noise",
    "inherit_base": "Noise",
    "hiden": true
  },
  "Prophet": {
    "opts": {
      "res": 0.7,
      "note_slide": 0,
      "pan_slide": 0,
      "pan": 0,
      "env_curve": 2,
      "res_slide_shape": 1,
      "res_slide_curve": 0,
      "pan_slide_shape": 1,
      "attack": 0,
      "sustain_level": 1,
      "note_slide_curve": 0,
      "note_slide_shape": 1,
      "cutoff_slide": 0,
      "pan_slide_curve": 0,
      "note": 52,
      "cutoff_slide_curve": 0,
      "amp_slide": 0,
      "amp": 1,
      "amp_slide_shape": 1,
      "release": 1,
      "decay": 0,
      "sustain": 0,
      "attack_level": 1,
      "cutoff": 110,
      "decay_level": 1,
      "cutoff_slide_shape": 1,
      "amp_slide_curve": 0,
      "res_slide": 0
    },
    "name": ":prophet",
    "inherit_arg": false,
    "summary": "The Prophet",
    "inherit_base": "SonicPiSynth",
    "hiden": false
  },
  "Noise": {
    "opts": {
      "res": 0,
      "pan_slide": 0,
      "decay": 0,
      "env_curve": 2,
      "res_slide_shape": 1,
      "res_slide_curve": 0,
      "pan_slide_shape": 1,
      "attack": 0,
      "sustain_level": 1,
      "cutoff_slide": 0,
      "pan_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "amp_slide": 0,
      "amp": 1,
      "amp_slide_shape": 1,
      "release": 1,
      "pan": 0,
      "sustain": 0,
      "attack_level": 1,
      "cutoff": 110,
      "decay_level": 1,
      "cutoff_slide_shape": 1,
      "amp_slide_curve": 0,
      "res_slide": 0
    },
    "name": ":noise",
    "inherit_arg": false,
    "summary": "Noise",
    "inherit_base": "Pitchless",
    "hiden": false
  },
  "DTri": {
    "opts": {
      "detune_slide": 0,
      "note_slide": 0,
      "pan_slide": 0,
      "decay": 0,
      "env_curve": 2,
      "detune": 0.1,
      "cutoff": 100,
      "pan_slide_shape": 1,
      "attack_level": 1,
      "note_slide_curve": 0,
      "note_slide_shape": 1,
      "cutoff_slide": 0,
      "pan_slide_curve": 0,
      "note": 52,
      "cutoff_slide_curve": 0,
      "amp_slide": 0,
      "amp": 1,
      "amp_slide_shape": 1,
      "release": 1,
      "pan": 0,
      "sustain": 0,
      "sustain_level": 1,
      "attack": 0,
      "detune_slide_shape": 1,
      "decay_level": 1,
      "cutoff_slide_shape": 1,
      "detune_slide_curve": 0,
      "amp_slide_curve": 0
    },
    "name": ":dtri",
    "inherit_arg": true,
    "summary": "Detuned Triangle Wave",
    "inherit_base": "DSaw",
    "hiden": true
  },
  "TB303": {
    "opts": {
      "res": 0.9,
      "amp_slide_shape": 1,
      "cutoff_decay": 0,
      "pulse_width_slide_curve": 0,
      "note_slide": 0,
      "cutoff_sustain_level": 1,
      "decay": 0,
      "cutoff": 120,
      "sustain": 0,
      "pan_slide_shape": 1,
      "cutoff_min": 30,
      "pulse_width_slide": 0,
      "wave": 0,
      "pulse_width": 0.5,
      "note_slide_shape": 1,
      "cutoff_release": 1,
      "pulse_width_slide_shape": 1,
      "note": 52,
      "cutoff_slide_curve": 0,
      "amp_slide": 0,
      "amp": 1,
      "decay_level": 1,
      "release": 1,
      "pan": 0,
      "attack_level": 1,
      "cutoff_slide_shape": 1,
      "amp_slide_curve": 0,
      "cutoff_slide": 0,
      "pan_slide": 0,
      "res_slide_shape": 1,
      "env_curve": 2,
      "cutoff_min_slide_curve": 0,
      "res_slide": 0,
      "note_slide_curve": 0,
      "cutoff_sustain": 0,
      "cutoff_attack": 0,
      "cutoff_min_slide": 0,
      "pan_slide_curve": 0,
      "cutoff_decay_level": 1,
      "cutoff_attack_level": 1,
      "res_slide_curve": 0,
      "sustain_level": 1,
      "cutoff_min_slide_shape": 1,
      "attack": 0
    },
    "name": ":tb303",
    "inherit_arg": false,
    "summary": "TB-303 Emulation",
    "inherit_base": "SonicPiSynth",
    "hiden": false
  },
  "Zawa": {
    "opts": {
      "res": 0.9,
      "pulse_width_slide_curve": 0,
      "note_slide": 0,
      "disable_wave": 0,
      "pan_slide": 0,
      "pan": 0,
      "range": 24,
      "res_slide_shape": 1,
      "pulse_width_slide_shape": 1,
      "res_slide_curve": 0,
      "phase_slide_curve": 0,
      "pan_slide_shape": 1,
      "attack": 0,
      "phase": 1,
      "sustain_level": 1,
      "pulse_width_slide": 0,
      "note_slide_curve": 0,
      "invert_wave": 0,
      "wave": 3,
      "phase_slide": 0,
      "pulse_width": 0.5,
      "phase_offset": 0,
      "note_slide_shape": 1,
      "cutoff_slide": 0,
      "phase_slide_shape": 1,
      "pan_slide_curve": 0,
      "note": 52,
      "cutoff_slide_curve": 0,
      "range_slide_curve": 0,
      "amp_slide": 0,
      "amp": 1,
      "amp_slide_shape": 1,
      "release": 1,
      "decay": 0,
      "sustain": 0,
      "attack_level": 1,
      "range_slide_shape": 1,
      "cutoff": 100,
      "decay_level": 1,
      "cutoff_slide_shape": 1,
      "amp_slide_curve": 0,
      "range_slide": 0,
      "res_slide": 0
    },
    "name": ":zawa",
    "inherit_arg": false,
    "summary": "Zawa",
    "inherit_base": "SonicPiSynth",
    "hiden": false
  },
  "SoundInStereo": {
    "opts": {
      "pan_slide": 0,
      "decay": 0,
      "env_curve": 0,
      "pan_slide_shape": 1,
      "sustain_level": 1,
      "input": 1,
      "pan_slide_curve": 0,
      "amp_slide": 0,
      "amp": 1,
      "amp_slide_shape": 1,
      "release": 0,
      "pan": 0,
      "sustain": 1,
      "attack_level": 1,
      "attack": 0,
      "decay_level": 1,
      "amp_slide_curve": 0
    },
    "name": ":sound_in_stereo",
    "inherit_arg": true,
    "summary": "Sound In Stereo",
    "inherit_base": "SoundIn",
    "hiden": true
  },
  "TechSaws": {
    "opts": {
      "res": 0.7,
      "note_slide": 0,
      "pan_slide": 0,
      "pan": 0,
      "env_curve": 2,
      "res_slide_shape": 1,
      "res_slide_curve": 0,
      "pan_slide_shape": 1,
      "attack": 0,
      "sustain_level": 1,
      "note_slide_curve": 0,
      "note_slide_shape": 1,
      "cutoff_slide": 0,
      "pan_slide_curve": 0,
      "note": 52,
      "cutoff_slide_curve": 0,
      "amp_slide": 0,
      "amp": 1,
      "amp_slide_shape": 1,
      "release": 1,
      "decay": 0,
      "sustain": 0,
      "attack_level": 1,
      "cutoff": 130,
      "decay_level": 1,
      "cutoff_slide_shape": 1,
      "amp_slide_curve": 0,
      "res_slide": 0
    },
    "name": ":tech_saws",
    "inherit_arg": false,
    "summary": "TechSaws",
    "inherit_base": "SonicPiSynth",
    "hiden": false
  }
}

synth_nodes = {
  ":hoover": "Hoover",
  ":fx_normaliser": "FXNormaliser",
  ":dark_ambience": "DarkAmbience",
  ":fx_nrbpf": "FXNRBPF",
  ":fx_replace_nhpf": "FXNormHPF",
  ":fx_bpf": "FXBPF",
  ":fx_band_eq": "FXBandEQ",
  ":fx_replace_normaliser": "FXNormaliser",
  ":pnoise": "PNoise",
  ":basic_mixer": "BasicMixer",
  ":fm": "FM",
  ":supersaw": "Supersaw",
  ":dpulse": "DPulse",
  ":fx_nhpf": "FXNormHPF",
  ":basic_stereo_player": "BasicStereoPlayer",
  ":hollow": "Hollow",
  ":fx_whammy": "FXWhammy",
  ":fx_panslicer": "FXPanSlicer",
  ":dull_bell": "DullBell",
  ":mono_player": "MonoPlayer",
  ":mod_fm": "ModFM",
  ":fx_rhpf": "FXRHPF",
  ":gnoise": "GNoise",
  ":fx_compressor": "FXCompressor",
  ":fx_replace_slicer": "FXSlicer",
  ":mod_dsaw": "ModDSaw",
  ":pluck": "SynthPluck",
  ":fx_level": "FXLevel",
  ":fx_pan": "FXPan",
  ":growl": "Growl",
  ":fx_rlpf": "FXRLPF",
  ":mod_tri": "ModTri",
  ":beep": "Beep",
  ":pretty_bell": "PrettyBell",
  ":fx_ixi_techno": "FXIXITechno",
  ":fx_replace_reverb": "FXReverb",
  ":fx_ring_mod": "FXRingMod",
  ":mod_sine": "ModSine",
  ":mod_saw": "ModSaw",
  ":tb303": "TB303",
  ":fx_flanger": "FXFlanger",
  ":fx_krush": "FXKrush",
  ":fx_vowel": "FXVowel",
  ":fx_hpf": "FXHPF",
  ":sine": "Beep",
  ":pulse": "Pulse",
  ":fx_tanh": "FXTanh",
  ":fx_bitcrusher": "FXBitcrusher",
  ":saw": "Saw",
  ":fx_rbpf": "FXRBPF",
  ":fx_replace_distortion": "FXDistortion",
  ":sound_in": "SoundIn",
  ":dsaw": "DSaw",
  ":zawa": "Zawa",
  ":fx_replace_rhpf": "FXRHPF",
  ":fx_reverb": "FXReverb",
  ":fx_lpf": "FXLPF",
  ":fx_replace_nrlpf": "FXNormRLPF",
  ":subpulse": "SubPulse",
  ":noise": "Noise",
  ":fx_nbpf": "FXNBPF",
  ":fx_replace_hpf": "FXHPF",
  ":stereo_player": "StereoPlayer",
  ":fx_pitch_shift": "FXPitchShift",
  ":fx_nlpf": "FXNormLPF",
  ":fx_mono": "FXMono",
  ":bnoise": "BNoise",
  ":fx_distortion": "FXDistortion",
  ":fx_slicer": "FXSlicer",
  ":tech_saws": "TechSaws",
  ":fx_replace_nlpf": "FXNormLPF",
  ":dtri": "DTri",
  ":chipnoise": "ChipNoise",
  ":fx_replace_wobble": "FXWobble",
  ":main_mixer": "MainMixer",
  ":basic_mono_player": "BasicMonoPlayer",
  ":square": "Square",
  ":fx_replace_compressor": "FXCompressor",
  ":mod_beep": "ModSine",
  ":fx_replace_rlpf": "FXRLPF",
  ":prophet": "Prophet",
  ":fx_octaver": "FXOctaver",
  ":fx_replace_level": "FXLevel",
  ":fx_echo": "FXEcho",
  ":blade": "SynthViolin",
  ":fx_wobble": "FXWobble",
  ":fx_nrhpf": "FXNormRHPF",
  ":piano": "SynthPiano",
  ":fx_replace_pan": "FXPan",
  ":fx_replace_nrhpf": "FXNormRHPF",
  ":fx_replace_ixi_techno": "FXIXITechno",
  ":fx_gverb": "FXGVerb",
  ":fx_nrlpf": "FXNormRLPF",
  ":fx_replace_lpf": "FXLPF",
  ":cnoise": "CNoise",
  ":fx_replace_echo": "FXEcho",
  ":chipbass": "ChipBass",
  ":chiplead": "ChipLead",
  ":mod_pulse": "ModPulse",
  ":sound_in_stereo": "SoundInStereo",
  ":tri": "Tri"
}

fx = {
  "FXWhammy": {
    "opts": {
      "transpose": 12,
      "deltime": 0.05,
      "mix_slide_curve": 0,
      "mix": 1,
      "grainsize": 0.075,
      "mix_slide": 0,
      "pre_mix": 1,
      "transpose_slide": 0,
      "pre_amp_slide": 0,
      "pre_mix_slide_curve": 0,
      "amp_slide": 0,
      "amp": 1,
      "amp_slide_shape": 1,
      "transpose_slide_curve": 0,
      "pre_mix_slide": 0,
      "max_delay_time": 1,
      "pre_amp_slide_shape": 1,
      "pre_mix_slide_shape": 1,
      "transpose_slide_shape": 1,
      "amp_slide_curve": 0,
      "pre_amp": 1,
      "mix_slide_shape": 1,
      "pre_amp_slide_curve": 0
    },
    "name": ":fx_whammy",
    "inherit_arg": true,
    "summary": "Whammy",
    "inherit_base": "FXInfo",
    "hiden": false
  },
  "FXLPF": {
    "opts": {
      "mix_slide_curve": 0,
      "mix": 1,
      "mix_slide": 0,
      "pre_mix": 1,
      "pre_amp_slide": 0,
      "cutoff_slide": 0,
      "pre_mix_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "amp_slide": 0,
      "amp": 1,
      "amp_slide_shape": 1,
      "pre_mix_slide": 0,
      "cutoff": 100,
      "pre_amp_slide_shape": 1,
      "pre_mix_slide_shape": 1,
      "amp_slide_curve": 0,
      "pre_amp": 1,
      "mix_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "cutoff_slide_shape": 1
    },
    "name": ":fx_lpf",
    "inherit_arg": true,
    "summary": "Low Pass Filter",
    "inherit_base": "FXInfo",
    "hiden": false
  },
  "FXFlanger": {
    "opts": {
      "decay_slide_curve": 0,
      "feedback_slide": 0,
      "stereo_invert_wave": 0,
      "phase_slide_shape": 1,
      "mix_slide_curve": 0,
      "mix": 1,
      "delay_slide_curve": 0,
      "feedback_slide_shape": 1,
      "depth": 5,
      "phase_slide_curve": 0,
      "max_delay": 20,
      "invert_wave": 0,
      "phase": 4,
      "feedback": 0,
      "mix_slide": 0,
      "delay_slide_shape": 1,
      "delay_slide": 0,
      "wave": 4,
      "phase_slide": 0,
      "feedback_slide_curve": 0,
      "pre_mix": 1,
      "phase_offset": 0,
      "decay_slide_shape": 1,
      "pre_amp_slide": 0,
      "decay_slide": 0,
      "pre_mix_slide_curve": 0,
      "depth_slide_curve": 0,
      "amp_slide": 0,
      "amp": 1,
      "amp_slide_shape": 1,
      "depth_slide_shape": 1,
      "decay": 2,
      "pre_mix_slide": 0,
      "delay": 5,
      "depth_slide": 0,
      "pre_amp_slide_shape": 1,
      "pre_mix_slide_shape": 1,
      "amp_slide_curve": 0,
      "pre_amp": 1,
      "invert_flange": 0,
      "mix_slide_shape": 1,
      "pre_amp_slide_curve": 0
    },
    "name": ":fx_flanger",
    "inherit_arg": true,
    "summary": "Flanger",
    "inherit_base": "FXInfo",
    "hiden": false
  },
  "FXRBPF": {
    "opts": {
      "centre_slide": 0,
      "res": 0.5,
      "centre": 100,
      "mix": 1,
      "centre_slide_curve": 0,
      "res_slide_shape": 1,
      "res_slide": 0,
      "mix_slide": 0,
      "pre_mix": 1,
      "pre_amp_slide": 0,
      "pre_mix_slide_curve": 0,
      "amp_slide": 0,
      "amp": 1,
      "amp_slide_shape": 1,
      "centre_slide_shape": 1,
      "res_slide_curve": 0,
      "pre_mix_slide": 0,
      "pre_mix_slide_shape": 1,
      "pre_amp_slide_shape": 1,
      "mix_slide_curve": 0,
      "amp_slide_curve": 0,
      "pre_amp": 1,
      "mix_slide_shape": 1,
      "pre_amp_slide_curve": 0
    },
    "name": ":fx_rbpf",
    "inherit_arg": true,
    "summary": "Resonant Band Pass Filter",
    "inherit_base": "FXBPF",
    "hiden": true
  },
  "FXGVerb": {
    "opts": {
      "damp_slide_curve": 0,
      "spread_slide_shape": 1,
      "mix_slide_curve": 0,
      "mix": 1,
      "pre_damp_slide": 0,
      "dry_slide_curve": 0,
      "tail_level": 0.5,
      "pre_damp": 0.5,
      "damp_slide_shape": 1,
      "dry": 1,
      "mix_slide": 0,
      "dry_slide_shape": 1,
      "pre_damp_slide_shape": 1,
      "pre_mix": 1,
      "ref_level": 0.7,
      "pre_amp_slide": 0,
      "pre_mix_slide_curve": 0,
      "spread_slide_curve": 0,
      "room": 10,
      "amp_slide": 0,
      "amp": 1,
      "amp_slide_shape": 1,
      "pre_damp_slide_curve": 0,
      "damp_slide": 0,
      "release": 3,
      "spread": 0.5,
      "pre_mix_slide": 0,
      "dry_slide": 0,
      "damp": 0.5,
      "pre_amp_slide_shape": 1,
      "pre_mix_slide_shape": 1,
      "amp_slide_curve": 0,
      "pre_amp": 1,
      "mix_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "spread_slide": 0
    },
    "name": ":fx_gverb",
    "inherit_arg": true,
    "summary": "GVerb",
    "inherit_base": "FXInfo",
    "hiden": false
  },
  "FXNormHPF": {
    "opts": {
      "mix_slide_curve": 0,
      "mix": 1,
      "mix_slide": 0,
      "pre_mix": 1,
      "pre_amp_slide": 0,
      "cutoff_slide": 0,
      "pre_mix_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "amp_slide": 0,
      "amp": 1,
      "amp_slide_shape": 1,
      "pre_mix_slide": 0,
      "cutoff": 100,
      "pre_amp_slide_shape": 1,
      "pre_mix_slide_shape": 1,
      "amp_slide_curve": 0,
      "pre_amp": 1,
      "mix_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "cutoff_slide_shape": 1
    },
    "name": ":fx_nhpf",
    "inherit_arg": true,
    "summary": "Normalised High Pass Filter",
    "inherit_base": "FXHPF",
    "hiden": true
  },
  "FXIXITechno": {
    "opts": {
      "res": 0.8,
      "cutoff_max_slide_curve": 0,
      "cutoff_min_slide": 0,
      "mix_slide_curve": 0,
      "mix": 1,
      "res_slide_shape": 1,
      "phase_slide_curve": 0,
      "cutoff_max_slide": 0,
      "cutoff_max_slide_shape": 1,
      "phase": 4,
      "res_slide": 0,
      "mix_slide": 0,
      "phase_slide": 0,
      "cutoff_min_slide_shape": 1,
      "pre_mix": 1,
      "phase_offset": 0,
      "pre_amp_slide": 0,
      "phase_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "amp_slide": 0,
      "amp": 1,
      "amp_slide_shape": 1,
      "cutoff_max": 120,
      "res_slide_curve": 0,
      "pre_mix_slide": 0,
      "cutoff_min": 60,
      "pre_amp_slide_shape": 1,
      "cutoff_min_slide_curve": 0,
      "pre_mix_slide_shape": 1,
      "amp_slide_curve": 0,
      "pre_amp": 1,
      "mix_slide_shape": 1,
      "pre_amp_slide_curve": 0
    },
    "name": ":fx_ixi_techno",
    "inherit_arg": true,
    "summary": "Techno from IXI Lang",
    "inherit_base": "FXInfo",
    "hiden": false
  },
  "FXRLPF": {
    "opts": {
      "res": 0.5,
      "mix_slide_curve": 0,
      "mix": 1,
      "res_slide_shape": 1,
      "res_slide": 0,
      "mix_slide": 0,
      "pre_mix": 1,
      "pre_amp_slide": 0,
      "cutoff_slide": 0,
      "pre_mix_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "amp_slide": 0,
      "amp": 1,
      "amp_slide_shape": 1,
      "res_slide_curve": 0,
      "pre_mix_slide": 0,
      "cutoff": 100,
      "pre_amp_slide_shape": 1,
      "pre_mix_slide_shape": 1,
      "amp_slide_curve": 0,
      "pre_amp": 1,
      "mix_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "cutoff_slide_shape": 1
    },
    "name": ":fx_rlpf",
    "inherit_arg": true,
    "summary": "Resonant Low Pass Filter",
    "inherit_base": "FXLPF",
    "hiden": true
  },
  "FXSlicer": {
    "opts": {
      "pulse_width_slide_curve": 0,
      "mix_slide": 0,
      "mix_slide_curve": 0,
      "mix_slide_shape": 1,
      "amp_min": 0,
      "phase_slide_curve": 0,
      "invert_wave": 0,
      "phase": 0.25,
      "pulse_width_slide": 0,
      "wave": 1,
      "phase_slide": 0,
      "pulse_width": 0.5,
      "pre_mix": 1,
      "amp_max": 1,
      "probability_slide": 0,
      "pulse_width_slide_shape": 1,
      "smooth_up_slide": 0,
      "amp_slide": 0,
      "smooth_up_slide_curve": 0,
      "amp_min_slide": 0,
      "smooth_up_slide_shape": 1,
      "prob_pos_slide": 0,
      "smooth_down_slide_curve": 0,
      "smooth_up": 0,
      "probability_slide_curve": 0,
      "amp_max_slide": 0,
      "smooth_slide_curve": 0,
      "pre_amp_slide_shape": 1,
      "smooth_slide": 0,
      "amp_slide_curve": 0,
      "smooth_down_slide": 0,
      "amp_max_slide_shape": 1,
      "mix": 1,
      "prob_pos_slide_curve": 0,
      "pre_mix_slide_curve": 0,
      "amp_min_slide_shape": 1,
      "seed": 0,
      "probability_slide_shape": 1,
      "phase_offset": 0,
      "smooth_slide_shape": 1,
      "pre_amp": 1,
      "pre_amp_slide": 0,
      "amp_max_slide_curve": 0,
      "phase_slide_shape": 1,
      "prob_pos_slide_shape": 1,
      "amp_slide_shape": 1,
      "amp": 1,
      "smooth_down_slide_shape": 1,
      "pre_mix_slide": 0,
      "probability": 0,
      "smooth": 0,
      "smooth_down": 0,
      "pre_mix_slide_shape": 1,
      "amp_min_slide_curve": 0,
      "prob_pos": 0,
      "pre_amp_slide_curve": 0
    },
    "name": ":fx_slicer",
    "inherit_arg": true,
    "summary": "Slicer",
    "inherit_base": "FXInfo",
    "hiden": false
  },
  "FXNormLPF": {
    "opts": {
      "mix_slide_curve": 0,
      "mix": 1,
      "mix_slide": 0,
      "pre_mix": 1,
      "pre_amp_slide": 0,
      "cutoff_slide": 0,
      "pre_mix_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "amp_slide": 0,
      "amp": 1,
      "amp_slide_shape": 1,
      "pre_mix_slide": 0,
      "cutoff": 100,
      "pre_amp_slide_shape": 1,
      "pre_mix_slide_shape": 1,
      "amp_slide_curve": 0,
      "pre_amp": 1,
      "mix_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "cutoff_slide_shape": 1
    },
    "name": ":fx_nlpf",
    "inherit_arg": true,
    "summary": "Normalised Low Pass Filter.",
    "inherit_base": "FXLPF",
    "hiden": true
  },
  "FXPanSlicer": {
    "opts": {
      "pan_max_slide_curve": 0,
      "amp": 1,
      "pulse_width_slide_curve": 0,
      "phase_offset": 0,
      "pulse_width_slide": 0,
      "pan_min": -1,
      "mix_slide_curve": 0,
      "mix_slide_shape": 1,
      "amp_min": 0,
      "phase_slide_curve": 0,
      "pan_min_slide_curve": 0,
      "invert_wave": 0,
      "phase": 0.25,
      "mix_slide": 0,
      "smooth": 0,
      "wave": 1,
      "phase_slide": 0,
      "pulse_width": 0.5,
      "pre_mix": 1,
      "probability_slide_curve": 0,
      "probability_slide": 0,
      "pulse_width_slide_shape": 1,
      "smooth_up_slide": 0,
      "amp_slide": 0,
      "smooth_up_slide_curve": 0,
      "amp_min_slide": 0,
      "smooth_up_slide_shape": 1,
      "prob_pos_slide": 0,
      "smooth_up": 0,
      "amp_max_slide": 0,
      "pan_max": 1,
      "smooth_slide_curve": 0,
      "pre_amp_slide_shape": 1,
      "smooth_slide": 0,
      "pan_max_slide": 0,
      "amp_slide_curve": 0,
      "mix": 1,
      "amp_max_slide_shape": 1,
      "smooth_down_slide": 0,
      "prob_pos_slide_curve": 0,
      "pre_mix_slide_curve": 0,
      "amp_min_slide_shape": 1,
      "pan_max_slide_shape": 1,
      "seed": 0,
      "prob_pos": 0,
      "pan_min_slide_shape": 1,
      "amp_max": 1,
      "smooth_slide_shape": 1,
      "pan_min_slide": 0,
      "pre_amp_slide": 0,
      "amp_max_slide_curve": 0,
      "phase_slide_shape": 1,
      "prob_pos_slide_shape": 1,
      "amp_slide_shape": 1,
      "smooth_down_slide_curve": 0,
      "smooth_down_slide_shape": 1,
      "pre_mix_slide": 0,
      "probability": 0,
      "probability_slide_shape": 1,
      "smooth_down": 0,
      "pre_mix_slide_shape": 1,
      "amp_min_slide_curve": 0,
      "pre_amp": 1,
      "pre_amp_slide_curve": 0
    },
    "name": ":fx_panslicer",
    "inherit_arg": true,
    "summary": "Pan Slicer",
    "inherit_base": "FXSlicer",
    "hiden": true
  },
  "FXMono": {
    "opts": {
      "pan_slide": 0,
      "mix_slide_curve": 0,
      "mix": 1,
      "pan_slide_curve": 0,
      "pan_slide_shape": 1,
      "mix_slide": 0,
      "pre_mix": 1,
      "pre_amp_slide": 0,
      "pre_mix_slide_curve": 0,
      "amp_slide": 0,
      "amp": 1,
      "amp_slide_shape": 1,
      "pan": 0,
      "pre_mix_slide": 0,
      "pre_amp_slide_shape": 1,
      "pre_mix_slide_shape": 1,
      "amp_slide_curve": 0,
      "pre_amp": 1,
      "mix_slide_shape": 1,
      "pre_amp_slide_curve": 0
    },
    "name": ":fx_mono",
    "inherit_arg": true,
    "summary": "Mono",
    "inherit_base": "FXInfo",
    "hiden": false
  },
  "FXNormaliser": {
    "opts": {
      "mix_slide_curve": 0,
      "mix": 1,
      "level": 1,
      "level_slide_curve": 0,
      "mix_slide": 0,
      "pre_mix": 1,
      "pre_amp_slide": 0,
      "pre_mix_slide_curve": 0,
      "amp_slide": 0,
      "amp": 1,
      "amp_slide_shape": 1,
      "level_slide": 0,
      "pre_mix_slide": 0,
      "pre_amp_slide_shape": 1,
      "pre_mix_slide_shape": 1,
      "amp_slide_curve": 0,
      "pre_amp": 1,
      "level_slide_shape": 1,
      "mix_slide_shape": 1,
      "pre_amp_slide_curve": 0
    },
    "name": ":fx_normaliser",
    "inherit_arg": true,
    "summary": "Normaliser",
    "inherit_base": "FXInfo",
    "hiden": false
  },
  "FXReverb": {
    "opts": {
      "damp_slide_curve": 0,
      "mix_slide_curve": 0,
      "mix": 0.4,
      "room_slide": 0,
      "mix_slide": 0,
      "room_slide_curve": 0,
      "pre_mix": 1,
      "pre_amp_slide": 0,
      "pre_mix_slide_curve": 0,
      "damp_slide_shape": 1,
      "room": 0.6,
      "amp_slide": 0,
      "amp": 1,
      "amp_slide_shape": 1,
      "room_slide_shape": 1,
      "damp_slide": 0,
      "pre_mix_slide": 0,
      "damp": 0.5,
      "pre_amp_slide_shape": 1,
      "pre_mix_slide_shape": 1,
      "amp_slide_curve": 0,
      "pre_amp": 1,
      "mix_slide_shape": 1,
      "pre_amp_slide_curve": 0
    },
    "name": ":fx_reverb",
    "inherit_arg": true,
    "summary": "Reverb",
    "inherit_base": "FXInfo",
    "hiden": false
  },
  "FXPitchShift": {
    "opts": {
      "pitch_dis": 0.0,
      "pitch_slide_curve": 0,
      "mix_slide_curve": 0,
      "mix": 1,
      "pitch": 0,
      "time_dis_slide_shape": 1,
      "pitch_dis_slide_shape": 1,
      "mix_slide": 0,
      "pitch_slide": 0,
      "window_size": 0.2,
      "time_dis_slide": 0,
      "pre_mix": 1,
      "pre_amp_slide": 0,
      "pre_mix_slide_curve": 0,
      "amp_slide": 0,
      "amp": 1,
      "amp_slide_shape": 1,
      "pitch_dis_slide": 0,
      "pitch_slide_shape": 1,
      "window_size_slide_shape": 1,
      "time_dis_slide_curve": 0,
      "pre_mix_slide": 0,
      "window_size_slide": 0,
      "time_dis": 0.0,
      "pre_amp_slide_shape": 1,
      "window_size_slide_curve": 0,
      "pre_mix_slide_shape": 1,
      "pitch_dis_slide_curve": 0,
      "amp_slide_curve": 0,
      "pre_amp": 1,
      "mix_slide_shape": 1,
      "pre_amp_slide_curve": 0
    },
    "name": ":fx_pitch_shift",
    "inherit_arg": true,
    "summary": "Pitch shift",
    "inherit_base": "FXInfo",
    "hiden": false
  },
  "FXKrush": {
    "opts": {
      "res": 0,
      "cutoff_slide": 0,
      "mix_slide_curve": 0,
      "mix": 1,
      "res_slide_shape": 1,
      "gain": 5,
      "res_slide": 0,
      "mix_slide": 0,
      "pre_mix": 1,
      "pre_amp_slide": 0,
      "gain_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "amp_slide": 0,
      "amp": 1,
      "amp_slide_shape": 1,
      "gain_slide": 0,
      "gain_slide__curve": 0,
      "res_slide_curve": 0,
      "pre_mix_slide": 0,
      "cutoff": 100,
      "pre_amp_slide_shape": 1,
      "pre_mix_slide_shape": 1,
      "amp_slide_curve": 0,
      "pre_amp": 1,
      "mix_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "cutoff_slide_shape": 1
    },
    "name": ":fx_krush",
    "inherit_arg": true,
    "summary": "krush",
    "inherit_base": "FXInfo",
    "hiden": false
  },
  "FXInfo": {
    "opts": {
      "pre_mix_slide_curve": 0,
      "amp_slide": 0,
      "amp": 1,
      "amp_slide_shape": 1,
      "mix_slide_curve": 0,
      "mix": 1,
      "pre_mix_slide": 0,
      "pre_amp_slide_shape": 1,
      "mix_slide": 0,
      "pre_mix_slide_shape": 1,
      "amp_slide_curve": 0,
      "pre_amp": 1,
      "pre_mix": 1,
      "mix_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "pre_amp_slide": 0
    },
    "inherit_arg": false,
    "hiden": true,
    "inherit_base": "BaseInfo"
  },
  "FXCompressor": {
    "opts": {
      "clamp_time_slide": 0,
      "clamp_time_slide_curve": 0,
      "mix_slide_curve": 0,
      "mix": 1,
      "threshold_slide_curve": 0,
      "slope_above_slide": 0,
      "slope_below_slide_shape": 1,
      "relax_time_slide_curve": 0,
      "mix_slide": 0,
      "threshold_slide_shape": 1,
      "relax_time_slide": 0,
      "clamp_time": 0.01,
      "pre_mix": 1,
      "slope_below_slide_curve": 0,
      "slope_above_slide_shape": 1,
      "pre_amp_slide": 0,
      "pre_mix_slide_curve": 0,
      "threshold": 0.2,
      "amp_slide": 0,
      "amp": 1,
      "amp_slide_shape": 1,
      "slope_below_slide": 0,
      "threshold_slide": 0,
      "clamp_time_slide_shape": 1,
      "slope_above_slide_curve": 0,
      "pre_mix_slide": 0,
      "relax_time": 0.01,
      "pre_amp_slide_shape": 1,
      "relax_time_slide_shape": 1,
      "pre_mix_slide_shape": 1,
      "amp_slide_curve": 0,
      "pre_amp": 1,
      "slope_above": 0.5,
      "mix_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "slope_below": 1
    },
    "name": ":fx_compressor",
    "inherit_arg": true,
    "summary": "Compressor",
    "inherit_base": "FXInfo",
    "hiden": false
  },
  "FXVowel": {
    "opts": {
      "voice": 0,
      "mix_slide_curve": 0,
      "mix": 1,
      "mix_slide": 0,
      "pre_mix": 1,
      "pre_amp_slide": 0,
      "pre_mix_slide_curve": 0,
      "vowel_sound": 1,
      "amp_slide": 0,
      "amp": 1,
      "amp_slide_shape": 1,
      "pre_mix_slide": 0,
      "pre_amp_slide_shape": 1,
      "pre_mix_slide_shape": 1,
      "amp_slide_curve": 0,
      "pre_amp": 1,
      "mix_slide_shape": 1,
      "pre_amp_slide_curve": 0
    },
    "name": ":fx_vowel",
    "inherit_arg": true,
    "summary": "Vowel",
    "inherit_base": "FXInfo",
    "hiden": false
  },
  "FXLevel": {
    "opts": {
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "amp_slide": 0,
      "amp": 1
    },
    "name": ":fx_level",
    "inherit_arg": false,
    "summary": "Level Amplifier",
    "inherit_base": "FXInfo",
    "hiden": false
  },
  "FXNormRLPF": {
    "opts": {
      "res": 0.5,
      "mix_slide_curve": 0,
      "mix": 1,
      "res_slide_shape": 1,
      "res_slide": 0,
      "mix_slide": 0,
      "pre_mix": 1,
      "pre_amp_slide": 0,
      "cutoff_slide": 0,
      "pre_mix_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "amp_slide": 0,
      "amp": 1,
      "amp_slide_shape": 1,
      "res_slide_curve": 0,
      "pre_mix_slide": 0,
      "cutoff": 100,
      "pre_amp_slide_shape": 1,
      "pre_mix_slide_shape": 1,
      "amp_slide_curve": 0,
      "pre_amp": 1,
      "mix_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "cutoff_slide_shape": 1
    },
    "name": ":fx_nrlpf",
    "inherit_arg": true,
    "summary": "Normalised Resonant Low Pass Filter",
    "inherit_base": "FXRLPF",
    "hiden": true
  },
  "FXEcho": {
    "opts": {
      "decay_slide_curve": 0,
      "decay_slide": 0,
      "mix_slide_curve": 0,
      "mix": 1,
      "max_phase": 2,
      "phase_slide_curve": 0,
      "phase": 0.25,
      "mix_slide": 0,
      "phase_slide": 0,
      "decay_slide_shape": 1,
      "pre_mix": 1,
      "pre_amp_slide": 0,
      "phase_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "amp_slide": 0,
      "amp": 1,
      "amp_slide_shape": 1,
      "decay": 2,
      "pre_mix_slide": 0,
      "pre_amp_slide_shape": 1,
      "pre_mix_slide_shape": 1,
      "amp_slide_curve": 0,
      "pre_amp": 1,
      "mix_slide_shape": 1,
      "pre_amp_slide_curve": 0
    },
    "name": ":fx_echo",
    "inherit_arg": true,
    "summary": "Echo",
    "inherit_base": "FXInfo",
    "hiden": false
  },
  "FXNRBPF": {
    "opts": {
      "centre_slide": 0,
      "res": 0.5,
      "mix_slide_curve": 0,
      "centre": 100,
      "mix": 1,
      "pre_mix_slide_shape": 1,
      "res_slide_shape": 1,
      "res_slide": 0,
      "mix_slide": 0,
      "pre_mix": 1,
      "pre_amp_slide": 0,
      "pre_mix_slide_curve": 0,
      "amp_slide": 0,
      "amp": 1,
      "amp_slide_shape": 1,
      "centre_slide_shape": 1,
      "res_slide_curve": 0,
      "pre_mix_slide": 0,
      "pre_amp_slide_shape": 1,
      "centre_slide_curve": 0,
      "amp_slide_curve": 0,
      "pre_amp": 1,
      "mix_slide_shape": 1,
      "pre_amp_slide_curve": 0
    },
    "name": ":fx_nrbpf",
    "inherit_arg": true,
    "summary": "Normalised Resonant Band Pass Filter",
    "inherit_base": "FXRBPF",
    "hiden": true
  },
  "FXTanh": {
    "opts": {
      "krunch_slide_curve": 0,
      "mix_slide_curve": 0,
      "mix": 1,
      "mix_slide": 0,
      "krunch_slide": 0,
      "pre_mix": 1,
      "krunch": 5,
      "pre_amp_slide": 0,
      "pre_mix_slide_curve": 0,
      "krunch_slide_shape": 1,
      "amp_slide": 0,
      "amp": 1,
      "amp_slide_shape": 1,
      "pre_mix_slide": 0,
      "pre_amp_slide_shape": 1,
      "pre_mix_slide_shape": 1,
      "amp_slide_curve": 0,
      "pre_amp": 1,
      "mix_slide_shape": 1,
      "pre_amp_slide_curve": 0
    },
    "name": ":fx_tanh",
    "inherit_arg": true,
    "summary": "Hyperbolic Tangent",
    "inherit_base": "FXInfo",
    "hiden": false
  },
  "FXWobble": {
    "opts": {
      "res": 0.8,
      "cutoff_max_slide_shape": 1,
      "pulse_width_slide": 0,
      "mix_slide_curve": 0,
      "mix_slide_shape": 1,
      "seed": 0,
      "phase_slide_curve": 0,
      "invert_wave": 0,
      "phase": 0.5,
      "mix_slide": 0,
      "smooth": 0,
      "wave": 0,
      "phase_slide": 0,
      "pulse_width": 0.5,
      "pre_mix": 1,
      "phase_offset": 0,
      "probability_slide": 0,
      "pulse_width_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "cutoff_min_slide_shape": 1,
      "amp_slide": 0,
      "amp": 1,
      "smooth_up_slide_shape": 1,
      "prob_pos_slide": 0,
      "filter": 0,
      "smooth_up": 0,
      "cutoff_min_slide": 0,
      "smooth_slide_curve": 0,
      "pre_amp_slide_shape": 1,
      "smooth_slide": 0,
      "amp_slide_curve": 0,
      "smooth_down_slide": 0,
      "pulse_width_slide_curve": 0,
      "cutoff_max_slide_curve": 0,
      "cutoff_max": 120,
      "cutoff_min_slide_curve": 0,
      "mix": 1,
      "prob_pos_slide_curve": 0,
      "res_slide_shape": 1,
      "smooth_up_slide": 0,
      "smooth_down_slide_curve": 0,
      "prob_pos_slide_shape": 1,
      "cutoff_max_slide": 0,
      "res_slide": 0,
      "prob_pos": 0,
      "probability_slide_shape": 1,
      "probability_slide_curve": 0,
      "smooth_slide_shape": 1,
      "pre_amp_slide": 0,
      "phase_slide_shape": 1,
      "probability": 0,
      "amp_slide_shape": 1,
      "smooth_up_slide_curve": 0,
      "smooth_down_slide_shape": 1,
      "res_slide_curve": 0,
      "pre_mix_slide": 0,
      "cutoff_min": 60,
      "smooth_down": 0,
      "pre_mix_slide_shape": 1,
      "pre_amp": 1,
      "pre_amp_slide_curve": 0
    },
    "name": ":fx_wobble",
    "inherit_arg": true,
    "summary": "Wobble",
    "inherit_base": "FXInfo",
    "hiden": false
  },
  "FXPan": {
    "opts": {
      "pan_slide": 0,
      "mix_slide_curve": 0,
      "mix": 1,
      "pan_slide_curve": 0,
      "pan_slide_shape": 1,
      "mix_slide": 0,
      "pre_mix": 1,
      "pre_amp_slide": 0,
      "pre_mix_slide_curve": 0,
      "amp_slide": 0,
      "amp": 1,
      "amp_slide_shape": 1,
      "pan": 0,
      "pre_mix_slide": 0,
      "pre_amp_slide_shape": 1,
      "pre_mix_slide_shape": 1,
      "amp_slide_curve": 0,
      "pre_amp": 1,
      "mix_slide_shape": 1,
      "pre_amp_slide_curve": 0
    },
    "name": ":fx_pan",
    "inherit_arg": true,
    "summary": "Pan",
    "inherit_base": "FXInfo",
    "hiden": false
  },
  "FXDistortion": {
    "opts": {
      "mix_slide_curve": 0,
      "mix": 1,
      "distort_slide_shape": 1,
      "distort_slide_curve": 0,
      "mix_slide": 0,
      "distort_slide": 0,
      "pre_mix": 1,
      "pre_amp_slide": 0,
      "pre_mix_slide_curve": 0,
      "distort": 0.5,
      "amp_slide": 0,
      "amp": 1,
      "amp_slide_shape": 1,
      "pre_mix_slide": 0,
      "pre_amp_slide_shape": 1,
      "pre_mix_slide_shape": 1,
      "amp_slide_curve": 0,
      "pre_amp": 1,
      "mix_slide_shape": 1,
      "pre_amp_slide_curve": 0
    },
    "name": ":fx_distortion",
    "inherit_arg": true,
    "summary": "Distortion",
    "inherit_base": "FXInfo",
    "hiden": false
  },
  "FXNormRHPF": {
    "opts": {
      "res": 0.5,
      "mix_slide_curve": 0,
      "mix": 1,
      "res_slide_shape": 1,
      "res_slide": 0,
      "mix_slide": 0,
      "pre_mix": 1,
      "pre_amp_slide": 0,
      "cutoff_slide": 0,
      "pre_mix_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "amp_slide": 0,
      "amp": 1,
      "amp_slide_shape": 1,
      "res_slide_curve": 0,
      "pre_mix_slide": 0,
      "cutoff": 100,
      "pre_amp_slide_shape": 1,
      "pre_mix_slide_shape": 1,
      "amp_slide_curve": 0,
      "pre_amp": 1,
      "mix_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "cutoff_slide_shape": 1
    },
    "name": ":fx_nrhpf",
    "inherit_arg": true,
    "summary": "Normalised Resonant High Pass Filter",
    "inherit_base": "FXRHPF",
    "hiden": true
  },
  "FXRHPF": {
    "opts": {
      "res": 0.5,
      "mix_slide_curve": 0,
      "mix": 1,
      "res_slide_shape": 1,
      "res_slide": 0,
      "mix_slide": 0,
      "pre_mix": 1,
      "pre_amp_slide": 0,
      "cutoff_slide": 0,
      "pre_mix_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "amp_slide": 0,
      "amp": 1,
      "amp_slide_shape": 1,
      "res_slide_curve": 0,
      "pre_mix_slide": 0,
      "cutoff": 100,
      "pre_amp_slide_shape": 1,
      "pre_mix_slide_shape": 1,
      "amp_slide_curve": 0,
      "pre_amp": 1,
      "mix_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "cutoff_slide_shape": 1
    },
    "name": ":fx_rhpf",
    "inherit_arg": true,
    "summary": "Resonant High Pass Filter",
    "inherit_base": "FXHPF",
    "hiden": true
  },
  "FXBandEQ": {
    "opts": {
      "res": 0.6,
      "freq_slide_shape": 1,
      "db_slide": 0,
      "mix_slide_curve": 0,
      "mix": 1,
      "res_slide_shape": 1,
      "freq_slide_curve": 0,
      "db": 0.6,
      "res_slide": 0,
      "mix_slide": 0,
      "db_slide_shape": 1,
      "pre_mix": 1,
      "pre_amp_slide": 0,
      "freq": 100,
      "pre_mix_slide_curve": 0,
      "amp_slide": 0,
      "amp": 1,
      "amp_slide_shape": 1,
      "res_slide_curve": 0,
      "pre_mix_slide": 0,
      "freq_slide": 0,
      "pre_amp_slide_shape": 1,
      "pre_mix_slide_shape": 1,
      "amp_slide_curve": 0,
      "pre_amp": 1,
      "mix_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "db_slide_curve": 0
    },
    "name": ":fx_band_eq",
    "inherit_arg": true,
    "summary": "Band EQ Filter",
    "inherit_base": "FXInfo",
    "hiden": false
  },
  "FXNBPF": {
    "opts": {
      "centre_slide": 0,
      "res": 0.6,
      "centre": 100,
      "mix": 1,
      "centre_slide_curve": 0,
      "res_slide_shape": 1,
      "res_slide": 0,
      "mix_slide": 0,
      "pre_mix": 1,
      "pre_amp_slide": 0,
      "pre_mix_slide_curve": 0,
      "amp_slide": 0,
      "amp": 1,
      "amp_slide_shape": 1,
      "centre_slide_shape": 1,
      "res_slide_curve": 0,
      "pre_mix_slide": 0,
      "pre_mix_slide_shape": 1,
      "pre_amp_slide_shape": 1,
      "mix_slide_curve": 0,
      "amp_slide_curve": 0,
      "pre_amp": 1,
      "mix_slide_shape": 1,
      "pre_amp_slide_curve": 0
    },
    "name": ":fx_nbpf",
    "inherit_arg": true,
    "summary": "Normalised Band Pass Filter",
    "inherit_base": "FXBPF",
    "hiden": true
  },
  "FXHPF": {
    "opts": {
      "mix_slide_curve": 0,
      "mix": 1,
      "mix_slide": 0,
      "pre_mix": 1,
      "pre_amp_slide": 0,
      "cutoff_slide": 0,
      "pre_mix_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "amp_slide": 0,
      "amp": 1,
      "amp_slide_shape": 1,
      "pre_mix_slide": 0,
      "cutoff": 100,
      "pre_amp_slide_shape": 1,
      "pre_mix_slide_shape": 1,
      "amp_slide_curve": 0,
      "pre_amp": 1,
      "mix_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "cutoff_slide_shape": 1
    },
    "name": ":fx_hpf",
    "inherit_arg": true,
    "summary": "High Pass Filter",
    "inherit_base": "FXInfo",
    "hiden": false
  },
  "FXChorus": {
    "opts": {
      "decay_slide_curve": 0,
      "decay_slide": 0,
      "mix_slide_curve": 0,
      "mix": 1,
      "max_phase": 1,
      "phase_slide_curve": 0,
      "phase": 0.25,
      "mix_slide": 0,
      "phase_slide": 0,
      "decay_slide_shape": 1,
      "pre_mix": 1,
      "pre_amp_slide": 0,
      "phase_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "amp_slide": 0,
      "amp": 1,
      "amp_slide_shape": 1,
      "decay": 1e-05,
      "pre_mix_slide": 0,
      "pre_amp_slide_shape": 1,
      "pre_mix_slide_shape": 1,
      "amp_slide_curve": 0,
      "pre_amp": 1,
      "mix_slide_shape": 1,
      "pre_amp_slide_curve": 0
    },
    "name": ":fx_chorus",
    "inherit_arg": true,
    "summary": "Chorus",
    "inherit_base": "FXInfo",
    "hiden": true
  },
  "FXRingMod": {
    "opts": {
      "freq_slide_shape": 1,
      "mix_slide_curve": 0,
      "mix": 1,
      "freq_slide_curve": 0,
      "mix_slide": 0,
      "pre_mix": 1,
      "mod_amp_slide": 0,
      "pre_amp_slide": 0,
      "freq": 30,
      "pre_mix_slide_curve": 0,
      "amp_slide": 0,
      "amp": 1,
      "amp_slide_shape": 1,
      "mod_amp_slide_shape": 1,
      "pre_mix_slide": 0,
      "freq_slide": 0,
      "pre_amp_slide_shape": 1,
      "mod_amp": 1,
      "pre_mix_slide_shape": 1,
      "amp_slide_curve": 0,
      "pre_amp": 1,
      "mix_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "mod_amp_slide_curve": 0
    },
    "name": ":fx_ring_mod",
    "inherit_arg": true,
    "summary": "Ring Modulator",
    "inherit_base": "FXInfo",
    "hiden": false
  },
  "FXBitcrusher": {
    "opts": {
      "sample_rate_slide_shape": 1,
      "bits_slide_shape": 1,
      "mix_slide_curve": 0,
      "mix": 1,
      "sample_rate": 10000,
      "bits_slide": 0,
      "sample_rate_slide": 0,
      "mix_slide": 0,
      "bits_slide_curve": 0,
      "pre_mix": 1,
      "sample_rate_slide_curve": 0,
      "pre_amp_slide": 0,
      "cutoff_slide": 0,
      "pre_mix_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "amp_slide": 0,
      "amp": 1,
      "amp_slide_shape": 1,
      "bits": 8,
      "pre_mix_slide": 0,
      "cutoff": 0,
      "pre_amp_slide_shape": 1,
      "pre_mix_slide_shape": 1,
      "amp_slide_curve": 0,
      "pre_amp": 1,
      "mix_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "cutoff_slide_shape": 1
    },
    "name": ":fx_bitcrusher",
    "inherit_arg": true,
    "summary": "Bitcrusher",
    "inherit_base": "FXInfo",
    "hiden": false
  },
  "FXOctaver": {
    "opts": {
      "subsub_amp_slide_curve": 0,
      "super_amp_slide": 0,
      "mix_slide_curve": 0,
      "mix": 1,
      "sub_amp": 1,
      "sub_amp_slide": 0,
      "sub_amp_slide_shape": 1,
      "mix_slide": 0,
      "subsub_amp_slide_shape": 1,
      "super_amp": 1,
      "pre_mix": 1,
      "pre_amp_slide": 0,
      "super_amp_slide_curve": 0,
      "pre_mix_slide_curve": 0,
      "sub_amp_slide_curve": 0,
      "amp_slide": 0,
      "amp": 1,
      "amp_slide_shape": 1,
      "subsub_amp": 1,
      "subsub_amp_slide": 0,
      "pre_mix_slide": 0,
      "super_amp_slide_shape": 1,
      "pre_amp_slide_shape": 1,
      "pre_mix_slide_shape": 1,
      "amp_slide_curve": 0,
      "pre_amp": 1,
      "mix_slide_shape": 1,
      "pre_amp_slide_curve": 0
    },
    "name": ":fx_octaver",
    "inherit_arg": true,
    "summary": "Octaver",
    "inherit_base": "FXInfo",
    "hiden": false
  },
  "FXBPF": {
    "opts": {
      "centre_slide": 0,
      "res": 0.6,
      "centre": 100,
      "mix_slide_curve": 0,
      "mix": 1,
      "centre_slide_curve": 0,
      "res_slide_shape": 1,
      "res_slide": 0,
      "mix_slide": 0,
      "pre_mix": 1,
      "pre_amp_slide": 0,
      "pre_mix_slide_curve": 0,
      "amp_slide": 0,
      "amp": 1,
      "amp_slide_shape": 1,
      "centre_slide_shape": 1,
      "res_slide_curve": 0,
      "pre_mix_slide": 0,
      "pre_amp_slide_shape": 1,
      "pre_mix_slide_shape": 1,
      "amp_slide_curve": 0,
      "pre_amp": 1,
      "mix_slide_shape": 1,
      "pre_amp_slide_curve": 0
    },
    "name": ":fx_bpf",
    "inherit_arg": true,
    "summary": "Band Pass Filter",
    "inherit_base": "FXInfo",
    "hiden": false
  }
}

samples = {
  "Percussive Sounds": [
    ":perc_bell",
    ":perc_snap",
    ":perc_snap2",
    ":perc_swash",
    ":perc_till"
  ],
  "Sounds featuring guitars": [
    ":guit_harmonics",
    ":guit_e_fifths",
    ":guit_e_slide",
    ":guit_em9"
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
  "Miscellaneous Sounds": [
    ":misc_burp",
    ":misc_crow",
    ":misc_cineboom"
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
  "Snare Drums": [
    ":sn_dub",
    ":sn_dolf",
    ":sn_zome"
  ],
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
  "Bass Sounds": [
    ":bass_hit_c",
    ":bass_hard_c",
    ":bass_thick_c",
    ":bass_drop_c",
    ":bass_woodsy_c",
    ":bass_voxy_c",
    ":bass_voxy_hit_c",
    ":bass_dnb_f"
  ]
}

