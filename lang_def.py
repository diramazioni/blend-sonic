null = None; true = True; false = False;
#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/

lang_core = {
  "version": {
    "name": "version",
    "introduced": "2,0,0",
    "hiden": true,
    "accepts_block": false,
    "summary": "Get current version information"
  },
  "rdist": {
    "name": "rdist",
    "opts": {
      "step": 1
    },
    "signature": {
      "width": null,
      "centre": 0,
      "*opts": null
    },
    "accepts_block": false,
    "summary": "Random number in centred distribution",
    "inline": true,
    "introduced": "2,3,0",
    "hiden": false,
    "args": [
      {
        "width": ":number"
      }
    ],
    "alt_args": [
      {
        "width": ":number"
      },
      {
        "centre": ":number"
      }
    ]
  },
  "sleep": {
    "name": "sleep",
    "advances_time": true,
    "signature": {
      "beats": null
    },
    "accepts_block": false,
    "summary": "Wait for beat duration",
    "introduced": "2,0,0",
    "hiden": false,
    "args": [],
    "alt_args": [
      {
        "beats": ":number"
      }
    ]
  },
  "define": {
    "name": "define",
    "signature": {
      "name": null,
      "&block": null
    },
    "accepts_block": true,
    "summary": "Define a new function",
    "introduced": "2,0,0",
    "hiden": false,
    "requires_block": true,
    "args": [
      {
        "name": ":symbol"
      }
    ],
    "intro_fn": true
  },
  "rand_skip": {
    "name": "rand_skip",
    "signature": {
      "amount": 1
    },
    "accepts_block": false,
    "summary": "Jump forward random generator",
    "introduced": "2,7,0",
    "hiden": false,
    "args": [
      {
        "amount": ":number"
      }
    ]
  },
  "sync_bpm": {
    "name": "sync_bpm",
    "opts": {},
    "signature": {
      "opts": "{}",
      "cue_ids": null
    },
    "accepts_block": false,
    "summary": "Sync and inherit BPM from other threads ",
    "advances_time": true,
    "introduced": "2,10,0",
    "hiden": false,
    "args": [
      {
        "cue_id": ":symbol"
      }
    ]
  },
  "rand_reset": {
    "name": "rand_reset",
    "args": [],
    "summary": "Reset rand generator to last seed",
    "introduced": "2,7,0",
    "hiden": false,
    "accepts_block": false
  },
  "bt": {
    "name": "bt",
    "signature": {
      "t": null
    },
    "accepts_block": false,
    "summary": "Beat time conversion",
    "introduced": "2,8,0",
    "hiden": true,
    "args": [
      {
        "seconds": ":number"
      }
    ]
  },
  "rand_i_look": {
    "name": "rand_i_look",
    "signature": {
      "*args": null
    },
    "accepts_block": false,
    "summary": "Generate a random whole number without consuming a rand",
    "inline": true,
    "introduced": "2,11,0",
    "hiden": false,
    "args": [
      {
        "max": ":number_or_range"
      }
    ]
  },
  "at": {
    "name": "at",
    "signature": {
      "&block": null,
      "params": "nil",
      "times": 0
    },
    "async_block": true,
    "accepts_block": true,
    "summary": "Asynchronous Time. Run a block at the given time(s)",
    "introduced": "2,1,0",
    "hiden": false,
    "requires_block": true,
    "args": [
      {
        "times": ":list"
      },
      {
        "params": ":list"
      }
    ]
  },
  "stretch": {
    "name": "stretch",
    "returns": ":ring",
    "signature": {
      "*args": null
    },
    "accepts_block": false,
    "summary": "Stretch a sequence of values",
    "inline": true,
    "introduced": "2,6,0",
    "hiden": false,
    "args": [
      {
        "count": ":int"
      }
    ],
    "alt_args": [
      {
        "list": ":array"
      }
    ]
  },
  "run_code": {
    "name": "run_code",
    "returns": null,
    "signature": {
      "code": null
    },
    "accepts_block": false,
    "summary": "Evaluate the code passed as a String as a new Run",
    "introduced": "2,11,0",
    "hiden": false,
    "args": [
      {
        "code": ":string"
      }
    ]
  },
  "ramp": {
    "name": "ramp",
    "returns": ":ramp",
    "signature": {
      "*args": null
    },
    "accepts_block": false,
    "summary": "Create a ramp vector",
    "inline": true,
    "introduced": "2,6,0",
    "hiden": false,
    "args": [
      {
        "list": ":array"
      }
    ]
  },
  "spark": {
    "name": "spark",
    "signature": {
      "*values": null
    },
    "accepts_block": false,
    "summary": "Print a string representing a list of numeric values as a spark graph/bar chart",
    "introduced": "2,5,0",
    "hiden": true
  },
  "quantise": {
    "name": "quantise",
    "signature": {
      "n": null,
      "step": null
    },
    "accepts_block": false,
    "summary": "Quantise a value to resolution",
    "inline": true,
    "introduced": "2,1,0",
    "hiden": false,
    "args": [
      {
        "n": ":number"
      },
      {
        "step": ":positive_number"
      }
    ]
  },
  "osc": {
    "signature": {
      "path": null,
      "*args": null
    },
    "hiden": true
  },
  "with_tempo": {
    "signature": {
      "&block": null,
      "*args": null
    },
    "hiden": true
  },
  "inc": {
    "name": "inc",
    "opts": {},
    "signature": {
      "n": null
    },
    "accepts_block": false,
    "summary": "Increment",
    "introduced": "2, 1, 0",
    "hiden": true,
    "args": [
      {
        "n": ":number"
      }
    ]
  },
  "sync": {
    "name": "sync",
    "opts": {
      "bpm_sync": false
    },
    "signature": {
      "opts": "{}",
      "cue_ids": null
    },
    "accepts_block": false,
    "summary": "Sync with other threads",
    "advances_time": true,
    "introduced": "2,0,0",
    "hiden": false,
    "args": [
      {
        "cue_id": ":symbol"
      }
    ]
  },
  "load_buffer": {
    "name": "load_buffer",
    "signature": {
      "path": null
    },
    "accepts_block": false,
    "summary": "Load the contents of a file to the current buffer",
    "introduced": "2,10,0",
    "hiden": false,
    "args": [
      {
        "path": ":string"
      }
    ]
  },
  "assert_equal": {
    "name": "assert_equal",
    "signature": {
      "arg1": null,
      "msg": "nil",
      "arg2": null
    },
    "accepts_block": false,
    "summary": "Ensure args are equal",
    "introduced": "2,8,0",
    "hiden": false,
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
  "comment": {
    "name": "comment",
    "signature": {
      "&block": null,
      "*args": null
    },
    "hiden": true,
    "summary": "Block level commenting",
    "introduced": "2,0,0",
    "requires_block": true,
    "accepts_block": true
  },
  "stop": {
    "name": "stop",
    "returns": null,
    "hiden": false,
    "summary": "Stop current thread or run",
    "introduced": "2,5,0",
    "args": [
      {
        "true_stops": ":boolean"
      }
    ],
    "accepts_block": false,
    "alt_args": []
  },
  "factor": {
    "name": "factor?",
    "signature": {
      "factor": null,
      "val": null
    },
    "accepts_block": false,
    "summary": "Factor test",
    "introduced": "2,1,0",
    "hiden": false,
    "args": [
      {
        "val": ":number"
      },
      {
        "factor": ":number"
      }
    ]
  },
  "tick_reset_all": {
    "name": "tick_reset_all",
    "returns": null,
    "accepts_block": false,
    "summary": "Reset all ticks",
    "introduced": "2,6,0",
    "hiden": false,
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
  "current_random_seed": {
    "name": "current_random_seed",
    "accepts_block": false,
    "summary": "Get current random seed",
    "introduced": "2,10,0",
    "hiden": true,
    "intro_fn": true
  },
  "current_bpm": {
    "name": "current_bpm",
    "introduced": "2,0,0",
    "hiden": true,
    "accepts_block": false,
    "summary": "Get current tempo"
  },
  "spread": {
    "name": "spread",
    "returns": ":ring",
    "signature": {
      "size": null,
      "*args": null,
      "num_accents": null
    },
    "accepts_block": false,
    "summary": "Euclidean distribution for beats",
    "inline": true,
    "introduced": "2,4,0",
    "hiden": false,
    "opts": {
      "rotate": false
    },
    "args": [
      {
        "num_accents": ":number"
      },
      {
        "size": ":number"
      }
    ]
  },
  "use_cue_logging": {
    "name": "use_cue_logging",
    "signature": {
      "&block": null,
      "v": null
    },
    "accepts_block": false,
    "summary": "Enable and disable cue logging",
    "introduced": "2,6,0",
    "hiden": false,
    "args": [
      {
        "true_or_false": ":boolean"
      }
    ]
  },
  "use_bpm": {
    "name": "use_bpm",
    "signature": {
      "&block": null,
      "bpm": null
    },
    "accepts_block": false,
    "summary": "Set the tempo",
    "introduced": "2,0,0",
    "hiden": false,
    "args": [
      {
        "bpm": ":number"
      }
    ],
    "intro_fn": true
  },
  "rand_look": {
    "name": "rand_look",
    "signature": {
      "*args": null
    },
    "accepts_block": false,
    "summary": "Generate a random number without consuming a rand",
    "inline": true,
    "introduced": "2,11,0",
    "hiden": false,
    "args": [
      {
        "max": ":number_or_range"
      }
    ]
  },
  "spark_graph": {
    "name": "spark_graph",
    "signature": {
      "*values": null
    },
    "hiden": true,
    "summary": "Returns a string representing a list of numeric values as a spark graph/bar chart",
    "introduced": "2,5,0",
    "accepts_block": false
  },
  "in_thread": {
    "name": "in_thread",
    "opts": {
      "name": ":foo",
      "sync_bpm": ":foo",
      "sync": ":foo",
      "delay": 0
    },
    "signature": {
      "&block": null,
      "*opts": null
    },
    "async_block": true,
    "hiden": false,
    "summary": "Run code block at the same time",
    "introduced": "2,0,0",
    "requires_block": true,
    "accepts_block": true
  },
  "use_osc": {
    "signature": {
      "host_or_port": null,
      "port": "nil"
    },
    "hiden": true
  },
  "range": {
    "name": "range",
    "returns": ":ring",
    "signature": {
      "start": null,
      "finish": null,
      "*args": null
    },
    "accepts_block": false,
    "summary": "Create a ring buffer with the specified start, finish and step size",
    "inline": true,
    "introduced": "2,2,0",
    "memoize": true,
    "hiden": false,
    "opts": {
      "inclusive": false,
      "step": 1
    },
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
    ]
  },
  "uncomment": {
    "name": "uncomment",
    "signature": {
      "&block": null,
      "*args": null
    },
    "hiden": true,
    "summary": "Block level comment ignoring",
    "introduced": "2,0,0",
    "requires_block": true,
    "accepts_block": true
  },
  "on": {
    "name": "on",
    "returns": null,
    "signature": {
      "condition": null,
      "&blk": null
    },
    "accepts_block": true,
    "summary": "Optionally evaluate block",
    "introduced": "2,10,0",
    "hiden": false,
    "requires_block": true,
    "args": [
      {
        "condition": ":truthy"
      }
    ]
  },
  "choose": {
    "name": "choose",
    "signature": {
      "args": null
    },
    "accepts_block": false,
    "summary": "Random list selection",
    "inline": true,
    "introduced": "2,0,0",
    "hiden": false,
    "args": [],
    "alt_args": [
      {
        "list": ":array"
      }
    ]
  },
  "vector": {
    "name": "vector",
    "returns": ":vector",
    "signature": {
      "*args": null
    },
    "accepts_block": false,
    "summary": "Create a vector",
    "inline": true,
    "introduced": "2,6,0",
    "hiden": false,
    "args": [
      {
        "list": ":array"
      }
    ]
  },
  "use_random_seed": {
    "name": "use_random_seed",
    "signature": {
      "&block": null,
      "seed": null
    },
    "accepts_block": false,
    "summary": "Set random seed generator to known seed",
    "introduced": "2,0,0",
    "hiden": false,
    "args": [
      {
        "seed": ":number"
      }
    ]
  },
  "with_bpm": {
    "name": "with_bpm",
    "signature": {
      "&block": null,
      "bpm": null
    },
    "accepts_block": true,
    "summary": "Set the tempo for the code block",
    "introduced": "2,0,0",
    "hiden": false,
    "requires_block": true,
    "args": [
      {
        "bpm": ":number"
      }
    ]
  },
  "halves": {
    "name": "halves",
    "returns": ":ring",
    "signature": {
      "num_halves": 1,
      "start": null
    },
    "accepts_block": false,
    "summary": "Create a ring of successive halves",
    "inline": true,
    "introduced": "2,10,0",
    "memoize": true,
    "hiden": false,
    "args": [
      {
        "start": ":number"
      },
      {
        "num_halves": ":int"
      }
    ]
  },
  "ring": {
    "name": "ring",
    "returns": ":ring",
    "signature": {
      "*args": null
    },
    "accepts_block": false,
    "summary": "Create a ring buffer",
    "inline": true,
    "introduced": "2,2,0",
    "hiden": false,
    "args": [
      {
        "list": ":array"
      }
    ]
  },
  "tick_reset": {
    "name": "tick_reset",
    "returns": ":number",
    "signature": {
      "*args": null
    },
    "hiden": false,
    "summary": "Reset tick to 0",
    "introduced": "2,6,0",
    "accepts_block": false,
    "alt_args": [
      {
        "key": ":symbol"
      }
    ]
  },
  "rrand_i": {
    "name": "rrand_i",
    "signature": {
      "min": null,
      "max": null
    },
    "accepts_block": false,
    "summary": "Generate a random whole number between two points inclusively",
    "inline": true,
    "introduced": "2,0,0",
    "hiden": false,
    "args": [
      {
        "min": ":number"
      },
      {
        "max": ":number"
      }
    ]
  },
  "beat": {
    "name": "beat",
    "args": [],
    "summary": "Get current beat",
    "introduced": "2,10,0",
    "hiden": true,
    "accepts_block": false
  },
  "cue": {
    "name": "cue",
    "opts": {
      "your_key": ":bar",
      "another_key": "foo: 64",
      "key": "foo: 64"
    },
    "signature": {
      "*opts": null,
      "cue_id": null
    },
    "accepts_block": false,
    "summary": "Cue other threads",
    "introduced": "2,0,0",
    "hiden": false,
    "args": [
      {
        "cue_id": ":symbol"
      }
    ]
  },
  "shuffle": {
    "name": "shuffle",
    "signature": {
      "list": null
    },
    "accepts_block": false,
    "summary": "Randomise order of a list",
    "inline": true,
    "introduced": "2,1,0",
    "hiden": false,
    "args": [],
    "alt_args": [
      {
        "list": ":array"
      }
    ]
  },
  "defonce": {
    "name": "defonce",
    "opts": {
      "override": false
    },
    "signature": {
      "name": null,
      "&block": null,
      "*opts": null
    },
    "accepts_block": true,
    "summary": "Define a named value only once",
    "introduced": "2,0,0",
    "hiden": false,
    "requires_block": true,
    "args": [
      {
        "name": ":symbol"
      }
    ]
  },
  "run_file": {
    "name": "run_file",
    "returns": null,
    "signature": {
      "path": null
    },
    "accepts_block": false,
    "summary": "Evaluate the contents of the file as a new Run",
    "introduced": "2,11,0",
    "hiden": false,
    "args": [
      {
        "filename": ":path"
      }
    ]
  },
  "ndefine": {
    "name": "ndefine",
    "signature": {
      "name": null,
      "&block": null
    },
    "accepts_block": true,
    "summary": "Define a new function",
    "introduced": "2,1,0",
    "hiden": true,
    "requires_block": true,
    "args": [
      {
        "name": ":symbol"
      }
    ]
  },
  "assert": {
    "name": "assert",
    "signature": {
      "arg": null,
      "msg": "nil"
    },
    "accepts_block": false,
    "summary": "Ensure arg is valid",
    "introduced": "2,8,0",
    "hiden": false,
    "args": [
      {
        "is_true": ":boolean"
      }
    ],
    "alt_args": []
  },
  "line": {
    "name": "line",
    "returns": ":ring",
    "signature": {
      "start": null,
      "finish": null,
      "*args": null
    },
    "accepts_block": false,
    "summary": "Create a ring buffer representing a straight line",
    "inline": true,
    "introduced": "2,5,0",
    "memoize": true,
    "hiden": false,
    "opts": {
      "inclusive": false,
      "steps": 1
    },
    "args": [
      {
        "start": ":number"
      },
      {
        "finish": ":number"
      }
    ]
  },
  "puts": {
    "name": "puts",
    "signature": {
      "*msgs": null
    },
    "accepts_block": false,
    "summary": "Display a message in the output pane",
    "introduced": "2,0,0",
    "hiden": true,
    "args": [
      {
        "output": ":anything"
      }
    ],
    "intro_fn": true
  },
  "pick": {
    "name": "pick",
    "opts": {
      "skip": 0
    },
    "signature": {
      "*args": null
    },
    "accepts_block": false,
    "summary": "Randomly pick from list (with duplicates)",
    "inline": true,
    "introduced": "2,10,0",
    "hiden": false,
    "args": [
      {
        "n": ":number_or_nil"
      }
    ],
    "alt_args": [
      {
        "list": ":array"
      }
    ]
  },
  "tick_set": {
    "name": "tick_set",
    "returns": ":number",
    "signature": {
      "*args": null
    },
    "accepts_block": false,
    "summary": "Set tick to a specific value",
    "introduced": "2,6,0",
    "hiden": false,
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
  "load_example": {
    "name": "load_example",
    "signature": {
      "example_name": null
    },
    "accepts_block": false,
    "summary": "Load a built-in example",
    "introduced": "2,10,0",
    "hiden": true,
    "args": [
      {
        "path": ":string"
      }
    ]
  },
  "look": {
    "name": "look",
    "returns": ":number",
    "signature": {
      "*args": null
    },
    "hiden": false,
    "summary": "Obtain value of a tick",
    "inline": true,
    "introduced": "2,6,0",
    "opts": {
      "offset": 0
    },
    "accepts_block": false,
    "alt_args": [
      {
        "list": ":array"
      },
      {
        "key": ":symbol"
      }
    ]
  },
  "block_slept": {
    "name": "block_slept?",
    "signature": {
      "&block": null
    },
    "async_block": false,
    "accepts_block": true,
    "summary": "Determine if block contains sleep time",
    "introduced": "2,9,0",
    "hiden": false,
    "requires_block": true,
    "args": []
  },
  "knit": {
    "name": "knit",
    "returns": ":ring",
    "signature": {
      "*args": null
    },
    "accepts_block": false,
    "summary": "Knit a sequence of repeated values",
    "inline": true,
    "introduced": "2,2,0",
    "hiden": false,
    "args": [
      {
        "value": ":anything"
      },
      {
        "count": ":number"
      }
    ]
  },
  "with_cue_logging": {
    "name": "with_cue_logging",
    "signature": {
      "&block": null,
      "v": null
    },
    "accepts_block": true,
    "summary": "Block-level enable and disable cue logging",
    "introduced": "2,6,0",
    "hiden": false,
    "requires_block": true,
    "args": [
      {
        "true_or_false": ":boolean"
      }
    ]
  },
  "note_list": {
    "name": "note_list",
    "introduced": "blend-sonic",
    "signature": {},
    "hiden": false,
    "summary": "Make a list of notes",
    "opts": {},
    "args": [],
    "accepts_block": false
  },
  "reset": {
    "name": "reset",
    "returns": null,
    "accepts_block": false,
    "summary": "Reset all thread locals",
    "introduced": "2,11,0",
    "hiden": false,
    "args": []
  },
  "rand": {
    "name": "rand",
    "signature": {
      "max": 1
    },
    "accepts_block": false,
    "summary": "Generate a random float below a value",
    "inline": true,
    "introduced": "2,0,0",
    "hiden": false,
    "args": [
      {
        "max": ":number_or_range"
      }
    ],
    "intro_fn": true
  },
  "block_duration": {
    "name": "block_duration",
    "signature": {
      "&block": null
    },
    "async_block": false,
    "accepts_block": true,
    "summary": "Return block duration",
    "introduced": "2,9,0",
    "hiden": false,
    "requires_block": true,
    "args": []
  },
  "dice": {
    "name": "dice",
    "signature": {
      "num_sides": 6
    },
    "accepts_block": false,
    "summary": "Random dice throw",
    "inline": true,
    "introduced": "2,0,0",
    "hiden": false,
    "args": [
      {
        "num_sides": ":number"
      }
    ]
  },
  "one_in": {
    "name": "one_in",
    "signature": {
      "num": null
    },
    "accepts_block": false,
    "summary": "Random true value with specified probability",
    "inline": true,
    "introduced": "2,0,0",
    "hiden": false,
    "args": [
      {
        "num": ":number"
      }
    ]
  },
  "tick": {
    "name": "tick",
    "returns": ":number",
    "signature": {
      "*args": null
    },
    "accepts_block": false,
    "summary": "Increment a tick and return value",
    "inline": true,
    "introduced": "2,6,0",
    "hiden": false,
    "opts": {
      "offset": 0,
      "step": 1
    },
    "args": [],
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
    ]
  },
  "bools": {
    "name": "bools",
    "returns": ":ring",
    "signature": {
      "*args": null
    },
    "accepts_block": false,
    "summary": "Create a ring of boolean values",
    "inline": true,
    "introduced": "2,2,0",
    "hiden": false,
    "args": [
      {
        "list": ":array"
      }
    ]
  },
  "rand_i": {
    "name": "rand_i",
    "signature": {
      "max": 2
    },
    "accepts_block": false,
    "summary": "Generate a random whole number below a value (exclusive)",
    "inline": true,
    "introduced": "2,0,0",
    "hiden": false,
    "args": [
      {
        "max": ":number_or_range"
      }
    ]
  },
  "dec": {
    "name": "dec",
    "opts": {},
    "signature": {
      "n": null
    },
    "accepts_block": false,
    "summary": "Decrement",
    "introduced": "2, 1, 0",
    "hiden": true,
    "args": [
      {
        "n": ":number"
      }
    ]
  },
  "with_random_seed": {
    "name": "with_random_seed",
    "signature": {
      "&block": null,
      "seed": null
    },
    "accepts_block": true,
    "summary": "Specify random seed for code block",
    "introduced": "2,0,0",
    "hiden": false,
    "requires_block": true,
    "args": [
      {
        "seed": ":number"
      }
    ]
  },
  "doubles": {
    "name": "doubles",
    "returns": ":ring",
    "signature": {
      "start": null,
      "num_doubles": 1
    },
    "accepts_block": false,
    "summary": "Create a ring of successive doubles",
    "inline": true,
    "introduced": "2,10,0",
    "memoize": true,
    "hiden": false,
    "args": [
      {
        "start": ":number"
      },
      {
        "num_doubles": ":int"
      }
    ]
  },
  "wait": {
    "name": "wait",
    "advances_time": true,
    "signature": {
      "time": null
    },
    "accepts_block": false,
    "summary": "Wait for duration",
    "introduced": "2,0,0",
    "hiden": true,
    "args": [
      {
        "beats": ":number"
      }
    ]
  },
  "time_shift": {
    "name": "time_shift",
    "returns": null,
    "signature": {
      "delta": null,
      "&blk": null
    },
    "accepts_block": true,
    "summary": "Slide time forwards or backwards for the given block",
    "introduced": "2,11,0",
    "hiden": false,
    "requires_block": true,
    "args": [
      {
        "delta_time": ":number"
      }
    ]
  },
  "print": {
    "name": "print",
    "signature": {
      "*msgs": null
    },
    "accepts_block": false,
    "summary": "Display a message in the output pane",
    "introduced": "2,0,0",
    "hiden": true,
    "args": [
      {
        "output": ":anything"
      }
    ],
    "intro_fn": true
  },
  "with_bpm_mul": {
    "name": "with_bpm_mul",
    "signature": {
      "&block": null,
      "mul": null
    },
    "accepts_block": true,
    "summary": "Set new tempo as a multiple of current tempo for block",
    "introduced": "2,3,0",
    "hiden": false,
    "requires_block": true,
    "args": [
      {
        "mul": ":number"
      }
    ]
  },
  "time_now": {
    "name": "time_now",
    "introduced": "blend-sonic",
    "signature": {},
    "hiden": false,
    "summary": "return a number based on current time",
    "opts": {},
    "args": [],
    "accepts_block": false
  },
  "clear": {
    "name": "clear",
    "returns": null,
    "accepts_block": false,
    "summary": "Clear all thread locals to defaults",
    "introduced": "2,11,0",
    "hiden": false,
    "args": []
  },
  "rt": {
    "name": "rt",
    "signature": {
      "t": null
    },
    "accepts_block": false,
    "summary": "Real time conversion",
    "inline": true,
    "introduced": "2,0,0",
    "hiden": false,
    "args": [
      {
        "seconds": ":number"
      }
    ]
  },
  "live_loop": {
    "name": "live_loop",
    "opts": {
      "sync_bpm": ":foo",
      "delay": 0,
      "sync": ":foo",
      "init": "",
      "auto_cue": true,
      "seed": 0
    },
    "signature": {
      "name": "nil",
      "&block": null,
      "*args": null
    },
    "async_block": true,
    "accepts_block": true,
    "summary": "A loop for live coding",
    "introduced": "2,1,0",
    "hiden": false,
    "requires_block": true,
    "args": [
      {
        "name": ":symbol"
      }
    ],
    "intro_fn": true
  },
  "current_beat_duration": {
    "name": "current_beat_duration",
    "introduced": "2,6,0",
    "hiden": true,
    "accepts_block": false,
    "summary": "Duration of current beat"
  },
  "rrand": {
    "name": "rrand",
    "opts": {
      "step": 1
    },
    "signature": {
      "*opts": null,
      "min": null,
      "max": null
    },
    "accepts_block": false,
    "summary": "Generate a random float between two numbers",
    "inline": true,
    "introduced": "2,0,0",
    "hiden": false,
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
  "vt": {
    "name": "vt",
    "accepts_block": false,
    "summary": "Get virtual time",
    "inline": true,
    "introduced": "2,1,0",
    "hiden": false
  },
  "rand_back": {
    "name": "rand_back",
    "signature": {
      "amount": 1
    },
    "accepts_block": false,
    "summary": "Roll back random generator",
    "introduced": "2,7,0",
    "hiden": false,
    "args": [
      {
        "amount": ":number"
      }
    ]
  },
  "density": {
    "name": "density",
    "signature": {
      "&block": null,
      "d": null
    },
    "async_block": true,
    "accepts_block": true,
    "summary": "Squash and repeat time",
    "introduced": "2,3,0",
    "hiden": false,
    "requires_block": true,
    "args": [
      {
        "d": ":density"
      }
    ]
  },
  "use_bpm_mul": {
    "name": "use_bpm_mul",
    "signature": {
      "&block": null,
      "mul": null
    },
    "accepts_block": false,
    "summary": "Set new tempo as a multiple of current tempo",
    "introduced": "2,3,0",
    "hiden": false,
    "args": [
      {
        "mul": ":number"
      }
    ]
  }
}

#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/

lang_sound = {
  "with_merged_sample_defaults": {
    "name": "with_merged_sample_defaults",
    "opts": {},
    "signature": {
      "&block": null,
      "*args": null
    },
    "hiden": false,
    "summary": "Block-level use merged sample defaults",
    "introduced": "2,9,0",
    "requires_block": true,
    "accepts_block": true
  },
  "current_octave": {
    "name": "current_octave",
    "introduced": "2,9,0",
    "hiden": true,
    "accepts_block": false,
    "summary": "Get current octave shift"
  },
  "ratio_to_pitch": {
    "name": "ratio_to_pitch",
    "signature": {
      "r": null
    },
    "accepts_block": false,
    "summary": "relative frequency ratio to MIDI pitch",
    "inline": true,
    "introduced": "2,7,0",
    "hiden": false,
    "args": [
      {
        "ratio": ":number"
      }
    ]
  },
  "rest": {
    "name": "rest?",
    "signature": {
      "n": null
    },
    "accepts_block": false,
    "summary": "Determine if note or args is a rest",
    "introduced": "2,1,0",
    "hiden": false,
    "args": [
      {
        "note_or_args": ":number_symbol_or_map"
      }
    ]
  },
  "use_synth_defaults": {
    "name": "use_synth_defaults",
    "opts": {},
    "signature": {
      "&block": null,
      "*args": null
    },
    "hiden": false,
    "summary": "Use new synth defaults",
    "introduced": "2,0,0",
    "accepts_block": false
  },
  "pitch_to_ratio": {
    "name": "pitch_to_ratio",
    "signature": {
      "m": null
    },
    "accepts_block": false,
    "summary": "relative MIDI pitch to frequency ratio",
    "inline": true,
    "introduced": "2,5,0",
    "hiden": false,
    "args": [
      {
        "pitch": ":midi_number"
      }
    ]
  },
  "invert_chord": {
    "signature": {
      "*args": null
    },
    "hiden": true
  },
  "scale": {
    "name": "scale",
    "returns": ":ring",
    "intro_fn": true,
    "summary": "Create scale",
    "opts": {
      "num_octaves": 1
    },
    "hiden": false,
    "signature": {
      "tonic_or_name": null,
      "*opts": null
    },
    "args": [],
    "memoize": true,
    "inline": true,
    "introduced": "2,0,0",
    "accepts_block": false,
    "alt_args": [
      {
        "tonic": ":symbol"
      },
      {
        "scale": ":symbol"
      }
    ]
  },
  "chord_invert": {
    "name": "chord_invert",
    "returns": ":ring",
    "signature": {
      "shift": null,
      "notes": null
    },
    "accepts_block": false,
    "summary": "Chord inversion",
    "inline": true,
    "introduced": "2,6,0",
    "hiden": false,
    "args": [
      {
        "notes": ":list"
      },
      {
        "shift": ":number"
      }
    ]
  },
  "with_octave": {
    "name": "with_octave",
    "signature": {
      "shift": null,
      "&block": null
    },
    "accepts_block": true,
    "summary": "Block level octave transposition",
    "introduced": "2,9,0",
    "hiden": false,
    "requires_block": true,
    "args": [
      {
        "octave_shift": ":number"
      }
    ],
    "intro_fn": true
  },
  "with_merged_synth_defaults": {
    "name": "with_merged_synth_defaults",
    "opts": {},
    "signature": {
      "&block": null,
      "*args": null
    },
    "hiden": false,
    "summary": "Block-level merge synth defaults",
    "introduced": "2,0,0",
    "requires_block": true,
    "accepts_block": true
  },
  "with_synth_defaults": {
    "name": "with_synth_defaults",
    "opts": {},
    "signature": {
      "&block": null,
      "*args": null
    },
    "hiden": false,
    "summary": "Block-level use new synth defaults",
    "introduced": "2,0,0",
    "requires_block": true,
    "accepts_block": true
  },
  "with_sample_bpm": {
    "name": "with_sample_bpm",
    "opts": {
      "num_beats": 1
    },
    "signature": {
      "sample_name": null,
      "&block": null,
      "*args": null
    },
    "accepts_block": true,
    "summary": "Block-scoped sample-duration-based bpm modification",
    "introduced": "2,1,0",
    "hiden": false,
    "requires_block": true,
    "args": [
      {
        "string_or_number": ":sample_name_or_duration"
      }
    ]
  },
  "with_timing_warnings": {
    "signature": {
      "&block": null,
      "v": null
    },
    "hiden": true
  },
  "status": {
    "name": "status",
    "introduced": "2,0,0",
    "hiden": true,
    "accepts_block": false,
    "summary": "Get server status"
  },
  "start_amp_monitor": {
    "hiden": true
  },
  "resolve_sample_path": {
    "signature": {
      "filts_and_sources": null
    },
    "hiden": true
  },
  "resolve_sample_paths": {
    "signature": {
      "filts_and_sources": null
    },
    "hiden": true
  },
  "with_debug": {
    "name": "with_debug",
    "signature": {
      "&block": null,
      "v": null
    },
    "accepts_block": true,
    "summary": "Block-level enable and disable debug",
    "introduced": "2,0,0",
    "hiden": false,
    "requires_block": true,
    "args": [
      {
        "true_or_false": ":boolean"
      }
    ]
  },
  "synth": {
    "name": "synth",
    "opts": {
      "pitch": 0,
      "slide": 0,
      "amp": 1,
      "pan": 0,
      "attack_level": 1,
      "attack": 0,
      "decay": 0,
      "sustain": 1,
      "amp_slide": 1,
      "decay_level": 1,
      "pan_slide": 1,
      "sustain_level": 1,
      "release": 0,
      "on": 1,
      "env_curve": 1
    },
    "signature": {
      "&blk": null,
      "synth_name": null,
      "*args": null
    },
    "async_block": true,
    "accepts_block": true,
    "summary": "Trigger specific synth",
    "introduced": "2,0,0",
    "hiden": true,
    "requires_block": false,
    "args": [
      {
        "synth_name": ":symbol"
      }
    ],
    "intro_fn": true
  },
  "set_mixer_invert_stereo!": {
    "hiden": false
  },
  "current_amp": {
    "hiden": true
  },
  "sample_paths": {
    "name": "sample_paths",
    "returns": ":ring",
    "signature": {
      "*args": null
    },
    "accepts_block": false,
    "summary": "Sample Pack Filter Resolution",
    "introduced": "2,10,0",
    "hiden": true,
    "args": [
      {
        "pre_args": ":source_and_filter_types"
      }
    ]
  },
  "set_mixer_standard_stereo!": {
    "hiden": false
  },
  "set_mixer_control": {
    "name": "set_mixer_control!",
    "opts": {
      "lpf_bypass": 0,
      "hpf": 0,
      "amp": 1,
      "pre_amp": 1,
      "hpf_bypass": 0,
      "leak_dc_bypass": 0,
      "limiter_bypass": 0,
      "lpf": 131
    },
    "signature": {
      "opts": null
    },
    "hiden": false,
    "summary": "Control master mixer",
    "introduced": "2,7,0",
    "modifies_env": true,
    "accepts_block": false
  },
  "sample": {
    "name": "sample",
    "intro_fn": true,
    "summary": "Trigger sample",
    "opts": {
      "hpf_max": 200,
      "hpf_release_level": 0,
      "lpf_sustain_level": 0,
      "finish": 1,
      "hpf_release": 0,
      "clamp_time": 0,
      "lpf_decay_level": 0,
      "attack": 0,
      "lpf_release": 0,
      "threshold": 0,
      "slope_above": 1,
      "hpf_init_level": 130,
      "relax_time": 0,
      "norm": 0,
      "onset": 0,
      "slide": 0,
      "rate": 1,
      "pitch_dis": 0,
      "rpitch": 0,
      "time_dis": 0,
      "lpf_init_level": 30,
      "lpf_env_curve": 1,
      "lpf_decay": 0,
      "hpf_decay_level": 0,
      "hpf": 0,
      "lpf_attack": 0,
      "hpf_sustain": 0,
      "lpf_min": 30,
      "amp": 1,
      "pan": 0,
      "hpf_attack": 0,
      "beat_stretch": 1,
      "hpf_decay": 0,
      "pitch_stretch": 1,
      "start": 0,
      "pre_amp": 1,
      "lpf": 131,
      "release": 0,
      "path": "/path/to/file",
      "slope_below": 1,
      "lpf_sustain": 0,
      "hpf_sustain_level": 0,
      "compress": 0,
      "hpf_env_curve": 1,
      "lpf_release_level": 0,
      "hpf_attack_level": 0,
      "lpf_attack_level": 0,
      "sustain": 1,
      "window_size": 0,
      "pitch": 0
    },
    "hiden": false,
    "signature": {
      "&blk": null,
      "*args": null
    },
    "async_block": true,
    "args": [],
    "introduced": "2,0,0",
    "requires_block": false,
    "accepts_block": true,
    "alt_args": [
      {
        "name_or_path": ":symbol_or_string"
      }
    ]
  },
  "midi_notes": {
    "name": "midi_notes",
    "returns": ":ring",
    "signature": {
      "*args": null
    },
    "accepts_block": false,
    "summary": "Create a ring buffer of midi note numbers",
    "inline": true,
    "introduced": "2,7,0",
    "memoize": true,
    "hiden": false,
    "args": [
      {
        "list": ":array"
      }
    ]
  },
  "chord_degree": {
    "name": "chord_degree",
    "returns": ":ring",
    "signature": {
      "scale": ":major",
      "*opts": null,
      "degree": null,
      "number_of_notes": 4,
      "tonic": null
    },
    "accepts_block": false,
    "summary": "Construct chords of stacked thirds, based on scale degrees",
    "inline": true,
    "introduced": "2,1,0",
    "memoize": true,
    "hiden": false,
    "args": [
      {
        "number_of_notes": ":int"
      }
    ],
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
    ]
  },
  "use_synth": {
    "name": "use_synth",
    "signature": {
      "&block": null,
      "synth_name": null,
      "*args": null
    },
    "accepts_block": false,
    "summary": "Switch current synth",
    "introduced": "2,0,0",
    "hiden": true,
    "args": [
      {
        "synth_name": ":symbol"
      }
    ],
    "intro_fn": true
  },
  "use_cent_tuning": {
    "name": "use_cent_tuning",
    "signature": {
      "shift": null,
      "&block": null
    },
    "accepts_block": false,
    "summary": "Cent tuning",
    "introduced": "2,9,0",
    "hiden": false,
    "args": [
      {
        "cent_shift": ":number"
      }
    ],
    "intro_fn": true
  },
  "set_sched_ahead_time": {
    "name": "set_sched_ahead_time!",
    "signature": {
      "t": null
    },
    "accepts_block": false,
    "summary": "Set sched ahead time globally",
    "introduced": "2,0,0",
    "hiden": false,
    "modifies_env": true,
    "args": [
      {
        "time": ":number"
      }
    ]
  },
  "with_timing_guarantees": {
    "name": "with_timing_guarantees",
    "signature": {
      "&block": null,
      "v": null
    },
    "accepts_block": true,
    "summary": "Block-scoped inhibition of synth triggers if too late",
    "introduced": "2,10,0",
    "hiden": false,
    "requires_block": true,
    "args": [
      {
        "bool": ":true_or_false"
      }
    ]
  },
  "chord_names": {
    "name": "chord_names",
    "summary": "All chord names",
    "memoize": true,
    "introduced": "2,6,0",
    "hiden": true,
    "accepts_block": false
  },
  "load_sample_at_path": {
    "signature": {
      "path": null
    },
    "hiden": true
  },
  "use_arg_bpm_scaling": {
    "name": "use_arg_bpm_scaling",
    "signature": {
      "bool": null,
      "&block": null
    },
    "accepts_block": false,
    "summary": "Enable and disable BPM scaling",
    "introduced": "2,0,0",
    "hiden": false,
    "args": [
      {
        "bool": ":boolean"
      }
    ]
  },
  "sample_names": {
    "name": "sample_names",
    "returns": ":ring",
    "signature": {
      "group": null
    },
    "accepts_block": false,
    "summary": "Get sample names",
    "introduced": "2,0,0",
    "memoize": true,
    "hiden": true,
    "args": [
      {
        "group": ":symbol"
      }
    ]
  },
  "scale_names": {
    "name": "scale_names",
    "summary": "All scale names",
    "memoize": true,
    "introduced": "2,6,0",
    "hiden": true,
    "accepts_block": false
  },
  "set_cent_tuning": {
    "name": "set_cent_tuning!",
    "signature": {
      "shift": null
    },
    "accepts_block": false,
    "summary": "Global Cent tuning",
    "introduced": "2,10,0",
    "hiden": false,
    "modifies_env": true,
    "args": [
      {
        "cent_shift": ":number"
      }
    ],
    "intro_fn": false
  },
  "sample_split_filts_and_opts": {
    "signature": {
      "args": null
    },
    "hiden": true
  },
  "recording_start": {
    "name": "recording_start",
    "introduced": "2,0,0",
    "hiden": true,
    "accepts_block": false,
    "summary": "Start recording"
  },
  "control": {
    "name": "control",
    "opts": {},
    "signature": {
      "*args": null
    },
    "accepts_block": false,
    "summary": "Control running synth",
    "introduced": "2,0,0",
    "hiden": false,
    "args": [
      {
        "node": ":synth_node"
      }
    ]
  },
  "sample_groups": {
    "name": "sample_groups",
    "summary": "Get all sample groups",
    "memoize": true,
    "introduced": "2,0,0",
    "hiden": true,
    "accepts_block": false
  },
  "with_afx": {
    "signature": {
      "&block": null,
      "fx_name": null,
      "*args": null
    },
    "hiden": true
  },
  "set_mixer_mono_mode!": {
    "hiden": false
  },
  "note_list": {
    "name": "note_list",
    "introduced": "blend-sonic",
    "signature": {},
    "hiden": false,
    "summary": "Make a list of notes",
    "opts": {},
    "args": [],
    "accepts_block": false
  },
  "sample_duration": {
    "name": "sample_duration",
    "opts": {
      "attack": 0,
      "start": 0,
      "rate": 1,
      "decay": 0,
      "sustain": 1,
      "rpitch": 0,
      "pitch_stretch": 1,
      "release": 0,
      "finish": 1,
      "beat_stretch": 1
    },
    "signature": {
      "*args": null
    },
    "accepts_block": false,
    "summary": "Get duration of sample in beats",
    "introduced": "2,0,0",
    "hiden": true,
    "args": [
      {
        "path": ":string"
      }
    ]
  },
  "use_timing_warnings": {
    "signature": {
      "&block": null,
      "v": null
    },
    "hiden": true
  },
  "current_arg_checks": {
    "name": "current_arg_checks",
    "introduced": "2,0,0",
    "hiden": true,
    "accepts_block": false,
    "summary": "Get current arg checking status"
  },
  "sample_free": {
    "name": "sample_free",
    "returns": null,
    "signature": {
      "*paths": null
    },
    "accepts_block": false,
    "summary": "Free a sample on the synth server",
    "introduced": "2,9,0",
    "hiden": false,
    "args": [
      {
        "path": ":string"
      }
    ]
  },
  "sample_info": {
    "name": "sample_info",
    "signature": {
      "*args": null
    },
    "accepts_block": false,
    "summary": "Get sample information",
    "introduced": "2,0,0",
    "hiden": true,
    "args": [
      {
        "path": ":string"
      }
    ]
  },
  "use_sample_defaults": {
    "name": "use_sample_defaults",
    "opts": {
      "hpf_max": 200,
      "hpf_release_level": 0,
      "lpf_sustain_level": 0,
      "finish": 1,
      "hpf_release": 0,
      "clamp_time": 0,
      "lpf_decay_level": 0,
      "attack": 0,
      "lpf_release": 0,
      "threshold": 0,
      "slope_above": 1,
      "hpf_init_level": 130,
      "relax_time": 0,
      "norm": 0,
      "onset": 0,
      "slide": 0,
      "rate": 1,
      "pitch_dis": 0,
      "rpitch": 0,
      "time_dis": 0,
      "lpf_init_level": 30,
      "lpf_env_curve": 1,
      "lpf_decay": 0,
      "hpf_decay_level": 0,
      "hpf": 0,
      "lpf_attack": 0,
      "hpf_sustain": 0,
      "lpf_min": 30,
      "amp": 1,
      "pan": 0,
      "hpf_attack": 0,
      "beat_stretch": 1,
      "hpf_decay": 0,
      "pitch_stretch": 1,
      "start": 0,
      "pre_amp": 1,
      "lpf": 131,
      "release": 0,
      "path": "/path/to/file",
      "slope_below": 1,
      "lpf_sustain": 0,
      "hpf_sustain_level": 0,
      "compress": 0,
      "hpf_env_curve": 1,
      "lpf_release_level": 0,
      "hpf_attack_level": 0,
      "lpf_attack_level": 0,
      "sustain": 1,
      "window_size": 0,
      "pitch": 0
    },
    "signature": {
      "&block": null,
      "*args": null
    },
    "hiden": false,
    "summary": "Use new sample defaults",
    "introduced": "2,5,0",
    "accepts_block": false
  },
  "note_range": {
    "name": "note_range",
    "returns": ":ring",
    "signature": {
      "low_note": null,
      "*opts": null,
      "high_note": null
    },
    "accepts_block": false,
    "summary": "Get a range of notes",
    "inline": true,
    "introduced": "2,6,0",
    "hiden": false,
    "opts": {
      "pitches": []
    },
    "args": [
      {
        "low_note": ":note"
      },
      {
        "high_note": ":note"
      }
    ]
  },
  "note_info": {
    "name": "note_info",
    "opts": {
      "octave": 4
    },
    "signature": {
      "n": null,
      "*args": null
    },
    "accepts_block": false,
    "summary": "Get note info",
    "introduced": "2,0,0",
    "hiden": true,
    "args": [
      {
        "note": ":symbol_or_number"
      }
    ]
  },
  "play_pattern": {
    "name": "play_pattern",
    "opts": {},
    "signature": {
      "notes": null,
      "*args": null
    },
    "accepts_block": false,
    "summary": "Play pattern of notes",
    "introduced": "2,0,0",
    "hiden": false,
    "args": [
      {
        "notes": ":list"
      }
    ]
  },
  "load_synthdefs": {
    "name": "load_synthdefs",
    "signature": {
      "path": "synthdef_path"
    },
    "accepts_block": false,
    "summary": "Load external synthdefs",
    "introduced": "2,0,0",
    "hiden": true,
    "args": [
      {
        "path": ":string"
      }
    ]
  },
  "use_external_synths": {
    "signature": {
      "&block": null,
      "v": null
    },
    "hiden": true
  },
  "use_timing_guarantees": {
    "name": "use_timing_guarantees",
    "signature": {
      "&block": null,
      "v": null
    },
    "accepts_block": false,
    "summary": "Inhibit synth triggers if too late",
    "introduced": "2,10,0",
    "hiden": false,
    "requires_block": false,
    "args": [
      {
        "bool": ":true_or_false"
      }
    ]
  },
  "use_octave": {
    "name": "use_octave",
    "signature": {
      "shift": null,
      "&block": null
    },
    "accepts_block": false,
    "summary": "Note octave transposition",
    "introduced": "2,9,0",
    "hiden": false,
    "args": [
      {
        "octave_shift": ":number"
      }
    ],
    "intro_fn": true
  },
  "with_arg_checks": {
    "name": "with_arg_checks",
    "signature": {
      "&block": null,
      "v": null
    },
    "accepts_block": true,
    "summary": "Block-level enable and disable arg checks",
    "introduced": "2,0,0",
    "hiden": false,
    "requires_block": true,
    "args": [
      {
        "true_or_false": ":boolean"
      }
    ]
  },
  "kill": {
    "name": "kill",
    "opts": {},
    "signature": {
      "node": null
    },
    "accepts_block": false,
    "summary": "Kill synth",
    "introduced": "2,0,0",
    "hiden": false,
    "args": [
      {
        "node": ":synth_node"
      }
    ]
  },
  "current_sched_ahead_time": {
    "name": "current_sched_ahead_time",
    "introduced": "2,0,0",
    "hiden": true,
    "accepts_block": false,
    "summary": "Get current sched ahead time"
  },
  "play": {
    "name": "play",
    "opts": {
      "pitch": 0,
      "slide": 0,
      "amp": 1,
      "pan": 0,
      "attack_level": 1,
      "attack": 0,
      "decay": 0,
      "sustain": 1,
      "amp_slide": 1,
      "decay_level": 1,
      "pan_slide": 1,
      "sustain_level": 1,
      "release": 0,
      "on": 1,
      "env_curve": 1
    },
    "signature": {
      "n": null,
      "&blk": null,
      "*args": null
    },
    "async_block": true,
    "accepts_block": true,
    "summary": "Play current synth",
    "introduced": "2,0,0",
    "hiden": false,
    "requires_block": false,
    "args": [
      {
        "note": ":symbol_or_number"
      }
    ],
    "intro_fn": true
  },
  "recording_save": {
    "name": "recording_save",
    "signature": {
      "filename": null
    },
    "accepts_block": false,
    "summary": "Save recording",
    "introduced": "2,0,0",
    "hiden": true,
    "args": [
      {
        "path": ":string"
      }
    ]
  },
  "set_mixer_stereo_mode!": {
    "hiden": false
  },
  "use_tuning": {
    "name": "use_tuning",
    "signature": {
      "tuning": null,
      "fundamental_note": ":c",
      "&block": null
    },
    "accepts_block": false,
    "summary": "Use alternative tuning systems",
    "introduced": "2,6,0",
    "hiden": false,
    "args": [
      {
        "tuning": ":symbol"
      },
      {
        "fundamental_note": ":symbol_or_number"
      }
    ]
  },
  "current_synth_defaults": {
    "name": "current_synth_defaults",
    "introduced": "2,0,0",
    "hiden": true,
    "accepts_block": false,
    "summary": "Get current synth defaults"
  },
  "with_cent_tuning": {
    "name": "with_cent_tuning",
    "signature": {
      "shift": null,
      "&block": null
    },
    "accepts_block": true,
    "summary": "Block-level cent tuning",
    "introduced": "2,9,0",
    "hiden": false,
    "requires_block": true,
    "args": [
      {
        "cent_shift": ":number"
      }
    ]
  },
  "current_sample_defaults": {
    "name": "current_sample_defaults",
    "introduced": "2,5,0",
    "hiden": true,
    "accepts_block": false,
    "summary": "Get current sample defaults"
  },
  "use_merged_sample_defaults": {
    "name": "use_merged_sample_defaults",
    "opts": {},
    "signature": {
      "&block": null,
      "*args": null
    },
    "hiden": false,
    "summary": "Merge new sample defaults",
    "introduced": "2,9,0",
    "accepts_block": false
  },
  "current_cent_tuning": {
    "name": "current_cent_tuning",
    "introduced": "2,9,0",
    "hiden": true,
    "accepts_block": false,
    "summary": "Get current cent shift"
  },
  "with_transpose": {
    "name": "with_transpose",
    "signature": {
      "shift": null,
      "&block": null
    },
    "accepts_block": true,
    "summary": "Block-level note transposition",
    "introduced": "2,0,0",
    "hiden": false,
    "requires_block": true,
    "args": [
      {
        "note_shift": ":number"
      }
    ]
  },
  "recording_stop": {
    "name": "recording_stop",
    "introduced": "2,0,0",
    "hiden": true,
    "accepts_block": false,
    "summary": "Stop recording"
  },
  "with_arg_bpm_scaling": {
    "name": "with_arg_bpm_scaling",
    "signature": {
      "bool": null,
      "&block": null
    },
    "hiden": false,
    "summary": "Block-level enable and disable BPM scaling",
    "introduced": "2,0,0",
    "requires_block": true,
    "accepts_block": true
  },
  "synth_names": {
    "name": "synth_names",
    "summary": "Get all synth names",
    "memoize": true,
    "introduced": "2,9,0",
    "hiden": true,
    "accepts_block": false
  },
  "should_trigger": {
    "signature": {
      "args_h": null
    },
    "hiden": false
  },
  "pitch_ratio": {
    "signature": {
      "*args": null
    },
    "hiden": true
  },
  "use_debug": {
    "name": "use_debug",
    "signature": {
      "&block": null,
      "v": null
    },
    "accepts_block": false,
    "summary": "Enable and disable debug",
    "introduced": "2,0,0",
    "hiden": false,
    "args": [
      {
        "true_or_false": ":boolean"
      }
    ]
  },
  "chord": {
    "name": "chord",
    "returns": ":ring",
    "intro_fn": true,
    "summary": "Create chord",
    "opts": {
      "invert": 0,
      "num_octaves": 1
    },
    "hiden": false,
    "signature": {
      "tonic_or_name": null,
      "*opts": null
    },
    "args": [],
    "memoize": true,
    "inline": true,
    "introduced": "2,0,0",
    "accepts_block": false,
    "alt_args": [
      {
        "tonic": ":symbol"
      },
      {
        "chord": ":symbol"
      }
    ]
  },
  "sample_buffer": {
    "name": "sample_buffer",
    "signature": {
      "*args": null
    },
    "accepts_block": false,
    "summary": "Get sample data",
    "introduced": "2,0,0",
    "hiden": true,
    "args": [
      {
        "path": ":string"
      }
    ]
  },
  "octs": {
    "name": "octs",
    "returns": ":ring",
    "signature": {
      "start": null,
      "num_octs": 1
    },
    "accepts_block": false,
    "summary": "Create a ring of octaves",
    "inline": true,
    "introduced": "2,8,0",
    "hiden": false,
    "args": [
      {
        "start": ":note"
      },
      {
        "num_octaves": ":pos_int"
      }
    ]
  },
  "use_sample_bpm": {
    "name": "use_sample_bpm",
    "opts": {
      "num_beats": 1
    },
    "signature": {
      "sample_name": null,
      "*args": null
    },
    "accepts_block": false,
    "summary": "Sample-duration-based bpm modification",
    "introduced": "2,1,0",
    "hiden": false,
    "args": [],
    "alt_args": [
      {
        "string_or_number": ":sample_name_or_duration"
      }
    ]
  },
  "current_synth": {
    "name": "current_synth",
    "introduced": "2,0,0",
    "hiden": true,
    "accepts_block": false,
    "summary": "Get current synth"
  },
  "midi_to_hz": {
    "name": "midi_to_hz",
    "signature": {
      "n": null
    },
    "accepts_block": false,
    "summary": "MIDI to Hz conversion",
    "inline": true,
    "introduced": "2,0,0",
    "hiden": false,
    "args": [
      {
        "note": ":symbol_or_number"
      }
    ]
  },
  "fx_names": {
    "name": "fx_names",
    "summary": "Get all FX names",
    "memoize": true,
    "introduced": "2,10,0",
    "hiden": true,
    "accepts_block": false
  },
  "load_sample": {
    "name": "load_sample",
    "signature": {
      "*args": null
    },
    "accepts_block": false,
    "summary": "Pre-load first matching sample",
    "introduced": "2,0,0",
    "hiden": true,
    "args": [
      {
        "path": ":string"
      }
    ]
  },
  "hz_to_midi": {
    "name": "hz_to_midi",
    "signature": {
      "freq": null
    },
    "accepts_block": false,
    "summary": "Hz to MIDI conversion",
    "inline": true,
    "introduced": "2,0,0",
    "hiden": false,
    "args": [
      {
        "freq": ":number"
      }
    ]
  },
  "with_tuning": {
    "name": "with_tuning",
    "signature": {
      "tuning": null,
      "fundamental_note": ":c",
      "&block": null
    },
    "accepts_block": true,
    "summary": "Block-level tuning modification",
    "introduced": "2,6,0",
    "hiden": false,
    "requires_block": true,
    "args": [
      {
        "tuning": ":symbol"
      },
      {
        "fundamental_note": ":symbol_or_number"
      }
    ]
  },
  "note": {
    "name": "note",
    "opts": {},
    "signature": {
      "n": null,
      "*args": null
    },
    "accepts_block": false,
    "summary": "Describe note",
    "introduced": "2,0,0",
    "hiden": false,
    "args": [],
    "alt_args": [
      {
        "note": ":symbol"
      }
    ]
  },
  "truthy": {
    "signature": {
      "val": null
    },
    "hiden": false
  },
  "reset_mixer": {
    "name": "reset_mixer!",
    "opts": {},
    "signature": {
      "": null
    },
    "hiden": false,
    "summary": "Reset master mixer",
    "introduced": "2,9,0",
    "modifies_env": true,
    "accepts_block": false
  },
  "use_arg_checks": {
    "name": "use_arg_checks",
    "signature": {
      "&block": null,
      "v": null
    },
    "accepts_block": false,
    "summary": "Enable and disable arg checks",
    "introduced": "2,0,0",
    "hiden": false,
    "args": [
      {
        "true_or_false": ":boolean"
      }
    ]
  },
  "play_chord": {
    "name": "play_chord",
    "opts": {
      "pitch": 0,
      "slide": 0,
      "amp": 1,
      "pan": 0,
      "attack_level": 1,
      "attack": 0,
      "decay": 0,
      "sustain": 1,
      "amp_slide": 1,
      "decay_level": 1,
      "pan_slide": 1,
      "sustain_level": 1,
      "release": 0,
      "on": 1,
      "env_curve": 1
    },
    "signature": {
      "notes": null,
      "*args": null
    },
    "accepts_block": false,
    "summary": "Play notes simultaneously",
    "introduced": "2,0,0",
    "hiden": false,
    "args": [
      {
        "notes": ":list"
      }
    ]
  },
  "current_debug": {
    "name": "current_debug",
    "introduced": "2,0,0",
    "hiden": true,
    "accepts_block": false,
    "summary": "Get current debug status"
  },
  "current_transpose": {
    "name": "current_transpose",
    "introduced": "2,0,0",
    "hiden": true,
    "accepts_block": false,
    "summary": "Get current transposition"
  },
  "all_sample_names": {
    "name": "all_sample_names",
    "summary": "Get all sample names",
    "memoize": true,
    "introduced": "2,0,0",
    "hiden": true,
    "accepts_block": false
  },
  "degree": {
    "name": "degree",
    "signature": {
      "scale": null,
      "degree": null,
      "tonic": null
    },
    "accepts_block": false,
    "summary": "Convert a degree into a note",
    "inline": true,
    "introduced": "2,1,0",
    "hiden": false,
    "args": [],
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
    ]
  },
  "sample_loaded": {
    "name": "sample_loaded?",
    "signature": {
      "*args": null
    },
    "accepts_block": false,
    "summary": "Test if sample was pre-loaded",
    "introduced": "2,2,0",
    "hiden": false,
    "args": [
      {
        "path": ":string"
      }
    ]
  },
  "with_sample_defaults": {
    "name": "with_sample_defaults",
    "opts": {},
    "signature": {
      "&block": null,
      "*args": null
    },
    "hiden": false,
    "summary": "Block-level use new sample defaults",
    "introduced": "2,5,0",
    "requires_block": true,
    "accepts_block": true
  },
  "with_fx": {
    "name": "with_fx",
    "intro_fn": true,
    "summary": "Use Studio FX",
    "opts": {
      "reps": 1,
      "kill_delay": 1
    },
    "hiden": true,
    "signature": {
      "&block": null,
      "fx_name": null,
      "*args": null
    },
    "async_block": true,
    "args": [],
    "introduced": "2,0,0",
    "requires_block": true,
    "accepts_block": true,
    "alt_args": [
      {
        "fx_name": ":symbol"
      }
    ]
  },
  "load_samples": {
    "name": "load_samples",
    "signature": {
      "*args": null
    },
    "accepts_block": false,
    "summary": "Pre-load all matching samples",
    "introduced": "2,0,0",
    "hiden": false,
    "args": [
      {
        "paths": ":list"
      }
    ]
  },
  "use_fx": {
    "signature": {
      "&block": null,
      "*args": null
    },
    "hiden": true
  },
  "time_now": {
    "name": "time_now",
    "introduced": "blend-sonic",
    "signature": {},
    "hiden": false,
    "summary": "return a number based on current time",
    "opts": {},
    "args": [],
    "accepts_block": false
  },
  "set_volume": {
    "name": "set_volume!",
    "signature": {
      "vol": null
    },
    "accepts_block": false,
    "summary": "Set Volume globally",
    "introduced": "2,0,0",
    "hiden": false,
    "modifies_env": true,
    "args": [
      {
        "vol": ":number"
      }
    ]
  },
  "play_pattern_timed": {
    "name": "play_pattern_timed",
    "opts": {
      "pitch": 0,
      "slide": 0,
      "amp": 1,
      "pan": 0,
      "attack_level": 1,
      "attack": 0,
      "decay": 0,
      "sustain": 1,
      "amp_slide": 1,
      "decay_level": 1,
      "pan_slide": 1,
      "sustain_level": 1,
      "release": 0,
      "on": 1,
      "env_curve": 1
    },
    "signature": {
      "notes": null,
      "times": null,
      "*args": null
    },
    "accepts_block": false,
    "summary": "Play pattern of notes with specific times",
    "introduced": "2,0,0",
    "hiden": false,
    "args": [
      {
        "notes": ":list"
      },
      {
        "times": ":list_or_number"
      }
    ]
  },
  "use_merged_synth_defaults": {
    "name": "use_merged_synth_defaults",
    "opts": {},
    "signature": {
      "&block": null,
      "*args": null
    },
    "hiden": false,
    "summary": "Merge synth defaults",
    "introduced": "2,0,0",
    "accepts_block": false
  },
  "current_volume": {
    "name": "current_volume",
    "introduced": "2,0,0",
    "hiden": true,
    "accepts_block": false,
    "summary": "Get current volume"
  },
  "with_synth": {
    "name": "with_synth",
    "signature": {
      "&block": null,
      "synth_name": null,
      "*args": null
    },
    "accepts_block": true,
    "summary": "Block-level synth switching",
    "introduced": "2,0,0",
    "hiden": true,
    "requires_block": true,
    "args": [
      {
        "synth_name": ":symbol"
      }
    ]
  },
  "sample_free_all": {
    "name": "sample_free_all",
    "returns": null,
    "accepts_block": false,
    "summary": "Free all loaded samples on the synth server",
    "introduced": "2,9,0",
    "hiden": false,
    "args": []
  },
  "use_transpose": {
    "name": "use_transpose",
    "signature": {
      "shift": null,
      "&block": null
    },
    "accepts_block": false,
    "summary": "Note transposition",
    "introduced": "2,0,0",
    "hiden": false,
    "args": [
      {
        "note_shift": ":number"
      }
    ],
    "intro_fn": true
  },
  "recording_delete": {
    "name": "recording_delete",
    "hiden": true,
    "accepts_block": false
  },
  "set_control_delta": {
    "name": "set_control_delta!",
    "signature": {
      "t": null
    },
    "accepts_block": false,
    "summary": "Set control delta globally",
    "introduced": "2,1,0",
    "hiden": false,
    "modifies_env": true,
    "args": [
      {
        "time": ":number"
      }
    ]
  }
}

sound_args_types_conversion = {}

sound_opts_types_conversion = {}

#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/

synths = {
  "Noise": {
    "name": ":noise",
    "inherit_arg": false,
    "inherit_base": "Pitchless",
    "summary": "Noise",
    "opts": {
      "pan_slide_shape": 1,
      "res_slide_shape": 1,
      "res": 0,
      "pan": 0,
      "cutoff_slide_shape": 1,
      "decay": 0,
      "decay_level": 1,
      "cutoff_slide_curve": 0,
      "sustain_level": 1,
      "cutoff": 110,
      "release": 1,
      "res_slide_curve": 0,
      "res_slide": 0,
      "pan_slide_curve": 0,
      "attack": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "attack_level": 1,
      "sustain": 0,
      "amp_slide": 0,
      "amp": 1,
      "pan_slide": 0,
      "cutoff_slide": 0,
      "env_curve": 2
    },
    "hiden": false
  },
  "SubPulse": {
    "name": ":subpulse",
    "inherit_arg": true,
    "inherit_base": "Pulse",
    "summary": "Pulse Wave with sub",
    "opts": {
      "pulse_width_slide_shape": 1,
      "sub_amp_slide_curve": 0,
      "pulse_width": 0.5,
      "pan_slide_shape": 1,
      "sub_detune": -12,
      "sub_amp_slide_shape": 1,
      "pulse_width_slide": 0,
      "pan": 0,
      "note": 52,
      "note_slide": 0,
      "attack": 0,
      "decay": 0,
      "note_slide_shape": 1,
      "decay_level": 1,
      "cutoff_slide_curve": 0,
      "sustain_level": 1,
      "cutoff": 100,
      "sub_detune_slide": 0,
      "release": 1,
      "pan_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "attack_level": 1,
      "sub_amp": 1,
      "note_slide_curve": 0,
      "sub_detune_slide_shape": 1,
      "sustain": 0,
      "amp_slide": 0,
      "amp": 1,
      "pan_slide": 0,
      "sub_amp_slide": 0,
      "cutoff_slide": 0,
      "env_curve": 2
    },
    "hiden": true
  },
  "Tri": {
    "name": ":tri",
    "inherit_arg": true,
    "inherit_base": "Pulse",
    "summary": "Triangle Wave",
    "opts": {
      "pulse_width_slide_shape": 1,
      "pulse_width": 0.5,
      "pan_slide_shape": 1,
      "pulse_width_slide": 0,
      "pan": 0,
      "note": 52,
      "note_slide": 0,
      "attack": 0,
      "decay": 0,
      "note_slide_shape": 1,
      "decay_level": 1,
      "cutoff_slide_curve": 0,
      "sustain_level": 1,
      "cutoff": 100,
      "release": 1,
      "pan_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "attack_level": 1,
      "note_slide_curve": 0,
      "sustain": 0,
      "amp_slide": 0,
      "amp": 1,
      "pan_slide": 0,
      "cutoff_slide": 0,
      "env_curve": 2
    },
    "hiden": true
  },
  "ModSaw": {
    "name": ":mod_saw",
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "summary": "Modulated Saw Wave",
    "opts": {
      "mod_pulse_width": 0.5,
      "pan_slide_shape": 1,
      "mod_wave": 1,
      "mod_range_slide": 0,
      "mod_invert_wave": 0,
      "mod_pulse_width_slide_shape": 1,
      "pan": 0,
      "note": 52,
      "note_slide": 0,
      "mod_phase_slide": 0,
      "attack": 0,
      "decay": 0,
      "note_slide_shape": 1,
      "decay_level": 1,
      "cutoff_slide_curve": 0,
      "sustain_level": 1,
      "cutoff": 100,
      "mod_pulse_width_slide": 0,
      "release": 1,
      "mod_range_slide_shape": 1,
      "mod_range": 5,
      "pan_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "mod_phase_slide_curve": 0,
      "mod_pulse_width_slide_curve": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "mod_range_slide_curve": 0,
      "attack_level": 1,
      "note_slide_curve": 0,
      "mod_phase_offset": 0,
      "sustain": 0,
      "amp_slide": 0,
      "amp": 1,
      "pan_slide": 0,
      "mod_phase_slide_shape": 1,
      "cutoff_slide": 0,
      "mod_phase": 0.25,
      "env_curve": 2
    },
    "hiden": false
  },
  "Square": {
    "name": ":square",
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "summary": "Square Wave",
    "opts": {
      "pan_slide_shape": 1,
      "pan": 0,
      "note": 52,
      "note_slide": 0,
      "attack": 0,
      "decay": 0,
      "note_slide_shape": 1,
      "decay_level": 1,
      "cutoff_slide_curve": 0,
      "sustain_level": 1,
      "cutoff": 100,
      "release": 1,
      "pan_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "attack_level": 1,
      "note_slide_curve": 0,
      "sustain": 0,
      "amp_slide": 0,
      "amp": 1,
      "pan_slide": 0,
      "cutoff_slide": 0,
      "env_curve": 2
    },
    "hiden": false
  },
  "PrettyBell": {
    "name": ":pretty_bell",
    "inherit_arg": true,
    "inherit_base": "DullBell",
    "summary": "Pretty Bell",
    "opts": {
      "pan_slide_shape": 1,
      "pan": 0,
      "note": 52,
      "note_slide": 0,
      "attack": 0,
      "decay": 0,
      "note_slide_shape": 1,
      "decay_level": 1,
      "sustain_level": 1,
      "release": 1,
      "pan_slide_curve": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "attack_level": 1,
      "note_slide_curve": 0,
      "sustain": 0,
      "amp_slide": 0,
      "amp": 1,
      "pan_slide": 0,
      "env_curve": 2
    },
    "hiden": true
  },
  "ModDSaw": {
    "name": ":mod_dsaw",
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "summary": "Modulated Detuned Saw Waves",
    "opts": {
      "mod_pulse_width": 0.5,
      "pan_slide_shape": 1,
      "mod_wave": 1,
      "mod_range_slide": 0,
      "mod_invert_wave": 0,
      "mod_pulse_width_slide_shape": 1,
      "pan": 0,
      "detune_slide_curve": 0,
      "note": 52,
      "note_slide": 0,
      "mod_phase_slide": 0,
      "attack": 0,
      "decay": 0,
      "note_slide_shape": 1,
      "decay_level": 1,
      "cutoff_slide_curve": 0,
      "sustain_level": 1,
      "cutoff": 100,
      "mod_pulse_width_slide": 0,
      "release": 1,
      "mod_range_slide_shape": 1,
      "mod_range": 5,
      "pan_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "mod_phase_slide_curve": 0,
      "mod_pulse_width_slide_curve": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "mod_range_slide_curve": 0,
      "attack_level": 1,
      "note_slide_curve": 0,
      "mod_phase_offset": 0,
      "detune_slide": 0,
      "sustain": 0,
      "amp_slide": 0,
      "amp": 1,
      "pan_slide": 0,
      "mod_phase_slide_shape": 1,
      "cutoff_slide": 0,
      "detune": 0.1,
      "mod_phase": 0.25,
      "detune_slide_shape": 1,
      "env_curve": 2
    },
    "hiden": false
  },
  "BasicMixer": {
    "name": ":basic_mixer",
    "inherit_arg": false,
    "inherit_base": "BaseMixer",
    "summary": "Basic Mixer",
    "opts": {
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "amp_slide": 0.1,
      "amp": 1
    },
    "hiden": true
  },
  "BasicStereoPlayer": {
    "name": ":basic_stereo_player",
    "inherit_arg": true,
    "inherit_base": "BasicMonoPlayer",
    "summary": "Basic Stereo Sample Player (no env)",
    "opts": {
      "hpf": -1,
      "lpf_slide": 0,
      "pan_slide_shape": 1,
      "pan": 0,
      "hpf_slide_shape": 1,
      "lpf": -1,
      "hpf_slide": 0,
      "lpf_slide_curve": 0,
      "pan_slide_curve": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "rate": 1,
      "lpf_slide_shape": 1,
      "amp_slide": 0,
      "amp": 1,
      "pan_slide": 0,
      "hpf_slide_curve": 0
    },
    "hiden": true
  },
  "Beep": {
    "name": ":beep",
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "summary": "Sine Wave",
    "opts": {
      "pan_slide_curve": 0,
      "amp_slide": 0,
      "attack": 0,
      "pan": 0,
      "amp_slide_shape": 1,
      "note_slide_shape": 1,
      "note": 52,
      "note_slide": 0,
      "sustain_level": 1,
      "note_slide_curve": 0,
      "decay": 0,
      "sustain": 0,
      "pan_slide_shape": 1,
      "amp": 1,
      "pan_slide": 0,
      "decay_level": 1,
      "attack_level": 1,
      "release": 1,
      "env_curve": 2,
      "amp_slide_curve": 0
    },
    "hiden": false
  },
  "TechSaws": {
    "name": ":tech_saws",
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "summary": "TechSaws",
    "opts": {
      "pan_slide_shape": 1,
      "res_slide_shape": 1,
      "res": 0.7,
      "pan": 0,
      "note": 52,
      "note_slide": 0,
      "attack": 0,
      "decay": 0,
      "note_slide_shape": 1,
      "decay_level": 1,
      "cutoff_slide_curve": 0,
      "sustain_level": 1,
      "cutoff": 130,
      "release": 1,
      "res_slide_curve": 0,
      "res_slide": 0,
      "pan_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "attack_level": 1,
      "note_slide_curve": 0,
      "sustain": 0,
      "amp_slide": 0,
      "amp": 1,
      "pan_slide": 0,
      "cutoff_slide": 0,
      "env_curve": 2
    },
    "hiden": false
  },
  "PNoise": {
    "name": ":pnoise",
    "inherit_arg": true,
    "inherit_base": "Noise",
    "summary": "Pink Noise",
    "opts": {
      "amp_slide": 0,
      "res": 0,
      "pan": 0,
      "cutoff_slide_shape": 1,
      "decay": 0,
      "sustain_level": 1,
      "cutoff_slide_curve": 0,
      "decay_level": 1,
      "cutoff": 110,
      "release": 1,
      "res_slide_curve": 0,
      "res_slide": 0,
      "pan_slide_curve": 0,
      "attack": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "attack_level": 1,
      "env_curve": 2,
      "res_slide_shape": 1,
      "pan_slide_shape": 1,
      "amp": 1,
      "pan_slide": 0,
      "cutoff_slide": 0,
      "sustain": 0
    },
    "hiden": true
  },
  "GNoise": {
    "name": ":gnoise",
    "inherit_arg": true,
    "inherit_base": "Noise",
    "summary": "Grey Noise",
    "opts": {
      "amp_slide": 0,
      "res": 0,
      "pan": 0,
      "cutoff_slide_shape": 1,
      "decay": 0,
      "sustain_level": 1,
      "cutoff_slide_curve": 0,
      "decay_level": 1,
      "cutoff": 110,
      "release": 1,
      "res_slide_curve": 0,
      "res_slide": 0,
      "pan_slide_curve": 0,
      "attack": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "attack_level": 1,
      "env_curve": 2,
      "res_slide_shape": 1,
      "pan_slide_shape": 1,
      "amp": 1,
      "pan_slide": 0,
      "cutoff_slide": 0,
      "sustain": 0
    },
    "hiden": true
  },
  "Pitchless": {
    "opts": {},
    "inherit_arg": true,
    "hiden": true,
    "inherit_base": "SonicPiSynth"
  },
  "Growl": {
    "name": ":growl",
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "summary": "Growl",
    "opts": {
      "pan_slide_shape": 1,
      "res_slide_shape": 1,
      "res": 0.7,
      "pan": 0,
      "note": 52,
      "note_slide": 0,
      "attack": 0.1,
      "decay": 0,
      "note_slide_shape": 1,
      "decay_level": 1,
      "cutoff_slide_curve": 0,
      "sustain_level": 1,
      "cutoff": 130,
      "release": 1,
      "res_slide_curve": 0,
      "res_slide": 0,
      "pan_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "attack_level": 1,
      "note_slide_curve": 0,
      "sustain": 0,
      "amp_slide": 0,
      "amp": 1,
      "pan_slide": 0,
      "cutoff_slide": 0,
      "env_curve": 2
    },
    "hiden": false
  },
  "DPulse": {
    "name": ":dpulse",
    "inherit_arg": true,
    "inherit_base": "DSaw",
    "summary": "Detuned Pulse Wave",
    "opts": {
      "pulse_width_slide_shape": 1,
      "pulse_width": 0.5,
      "amp_slide": 0,
      "pulse_width_slide": 0,
      "dpulse_width_slide_shape": 1,
      "pan": 0,
      "detune_slide_curve": 0,
      "note": 52,
      "note_slide": 0,
      "attack": 0,
      "decay": 0,
      "note_slide_shape": 1,
      "sustain_level": 1,
      "cutoff_slide_curve": 0,
      "decay_level": 1,
      "cutoff": 100,
      "release": 1,
      "dpulse_width": 0,
      "dpulse_width_slide": 0,
      "pan_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "pulse_width_slide_curve": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "attack_level": 1,
      "note_slide_curve": 0,
      "detune_slide": 0,
      "sustain": 0,
      "pan_slide_shape": 1,
      "amp": 1,
      "pan_slide": 0,
      "detune_slide_shape": 1,
      "cutoff_slide": 0,
      "env_curve": 2,
      "detune": 0.1
    },
    "hiden": true
  },
  "SynthPiano": {
    "name": ":piano",
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "summary": "SynthPiano",
    "opts": {
      "pan_slide_shape": 1,
      "vel": 0.2,
      "pan": 0,
      "note": 52,
      "note_slide": 0,
      "attack": 0,
      "decay": 0,
      "note_slide_shape": 1,
      "decay_level": 1,
      "sustain_level": 1,
      "release": 1,
      "pan_slide_curve": 0,
      "hard": 0.5,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "stereo_width": 0,
      "attack_level": 1,
      "note_slide_curve": 0,
      "sustain": 0,
      "amp_slide": 0,
      "amp": 1,
      "pan_slide": 0
    },
    "hiden": false
  },
  "ModPulse": {
    "name": ":mod_pulse",
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "summary": "Modulated Pulse",
    "opts": {
      "pulse_width_slide_shape": 1,
      "pulse_width": 0.5,
      "mod_pulse_width": 0.5,
      "pan_slide_shape": 1,
      "mod_wave": 1,
      "pulse_width_slide": 0,
      "mod_range_slide": 0,
      "mod_invert_wave": 0,
      "mod_pulse_width_slide_shape": 1,
      "pan": 0,
      "note": 52,
      "note_slide": 0,
      "mod_phase_slide": 0,
      "attack": 0,
      "decay": 0,
      "note_slide_shape": 1,
      "decay_level": 1,
      "cutoff_slide_curve": 0,
      "sustain_level": 1,
      "cutoff": 100,
      "mod_pulse_width_slide": 0,
      "release": 1,
      "mod_range_slide_shape": 1,
      "mod_range": 5,
      "pan_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "mod_phase_slide_curve": 0,
      "mod_pulse_width_slide_curve": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "mod_range_slide_curve": 0,
      "attack_level": 1,
      "note_slide_curve": 0,
      "mod_phase_offset": 0,
      "sustain": 0,
      "amp_slide": 0,
      "amp": 1,
      "pan_slide": 0,
      "mod_phase_slide_shape": 1,
      "cutoff_slide": 0,
      "mod_phase": 0.25,
      "pulse_width_slide_curve": 0,
      "env_curve": 2
    },
    "hiden": false
  },
  "BasicMonoPlayer": {
    "name": ":basic_mono_player",
    "inherit_arg": false,
    "inherit_base": "StudioInfo",
    "summary": "Basic Mono Sample Player (no env)",
    "opts": {
      "hpf": -1,
      "pan_slide_curve": 0,
      "lpf_slide": 0,
      "amp_slide": 0,
      "hpf_slide_shape": 1,
      "pan": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "lpf": -1,
      "rate": 1,
      "lpf_slide_shape": 1,
      "hpf_slide": 0,
      "pan_slide_shape": 1,
      "amp": 1,
      "pan_slide": 0,
      "hpf_slide_curve": 0,
      "lpf_slide_curve": 0
    },
    "hiden": true
  },
  "ModSine": {
    "name": ":mod_sine",
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "summary": "Modulated Sine Wave",
    "opts": {
      "mod_pulse_width": 0.5,
      "pan_slide_shape": 1,
      "mod_wave": 1,
      "mod_range_slide": 0,
      "mod_invert_wave": 0,
      "mod_pulse_width_slide_shape": 1,
      "pan": 0,
      "note": 52,
      "note_slide": 0,
      "mod_phase_slide": 0,
      "attack": 0,
      "decay": 0,
      "note_slide_shape": 1,
      "decay_level": 1,
      "cutoff_slide_curve": 0,
      "sustain_level": 1,
      "cutoff": 100,
      "mod_pulse_width_slide": 0,
      "release": 1,
      "mod_range_slide_shape": 1,
      "mod_range": 5,
      "pan_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "mod_phase_slide_curve": 0,
      "mod_pulse_width_slide_curve": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "mod_range_slide_curve": 0,
      "attack_level": 1,
      "note_slide_curve": 0,
      "mod_phase_offset": 0,
      "sustain": 0,
      "amp_slide": 0,
      "amp": 1,
      "pan_slide": 0,
      "mod_phase_slide_shape": 1,
      "cutoff_slide": 0,
      "mod_phase": 0.25,
      "env_curve": 2
    },
    "hiden": false
  },
  "ModTri": {
    "name": ":mod_tri",
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "summary": "Modulated Triangle Wave",
    "opts": {
      "mod_pulse_width": 0.5,
      "pan_slide_shape": 1,
      "mod_wave": 1,
      "mod_range_slide": 0,
      "mod_invert_wave": 0,
      "mod_pulse_width_slide_shape": 1,
      "pan": 0,
      "note": 52,
      "note_slide": 0,
      "mod_phase_slide": 0,
      "attack": 0,
      "decay": 0,
      "note_slide_shape": 1,
      "decay_level": 1,
      "cutoff_slide_curve": 0,
      "sustain_level": 1,
      "cutoff": 100,
      "mod_pulse_width_slide": 0,
      "release": 1,
      "mod_range_slide_shape": 1,
      "mod_range": 5,
      "pan_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "mod_phase_slide_curve": 0,
      "mod_pulse_width_slide_curve": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "mod_range_slide_curve": 0,
      "attack_level": 1,
      "note_slide_curve": 0,
      "mod_phase_offset": 0,
      "sustain": 0,
      "amp_slide": 0,
      "amp": 1,
      "pan_slide": 0,
      "mod_phase_slide_shape": 1,
      "cutoff_slide": 0,
      "mod_phase": 0.25,
      "env_curve": 2
    },
    "hiden": false
  },
  "MainMixer": {
    "name": ":mixer",
    "inherit_arg": false,
    "inherit_base": "BaseMixer",
    "summary": "Main Mixer",
    "opts": {
      "lpf_bypass": 0,
      "hpf": 0,
      "pre_amp_slide_curve": 0,
      "lpf_slide": 0.02,
      "invert_stereo": 0,
      "hpf_slide_shape": 1,
      "hpf_bypass": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "lpf": 135.5,
      "limiter_bypass": 0,
      "force_mono": 0,
      "lpf_slide_shape": 1,
      "hpf_slide": 0.02,
      "amp_slide": 0.02,
      "amp": 1,
      "pre_amp": 1,
      "lpf_slide_curve": 0,
      "hpf_slide_curve": 0,
      "pre_amp_slide": 0.02,
      "pre_amp_slide_shape": 1
    },
    "hiden": true
  },
  "Supersaw": {
    "name": ":supersaw",
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "summary": "Supersaw",
    "opts": {
      "pan_slide_shape": 1,
      "res_slide_shape": 1,
      "res": 0.7,
      "pan": 0,
      "note": 52,
      "note_slide": 0,
      "attack": 0,
      "decay": 0,
      "note_slide_shape": 1,
      "decay_level": 1,
      "cutoff_slide_curve": 0,
      "sustain_level": 1,
      "cutoff": 130,
      "release": 1,
      "res_slide_curve": 0,
      "res_slide": 0,
      "pan_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "attack_level": 1,
      "note_slide_curve": 0,
      "sustain": 0,
      "amp_slide": 0,
      "amp": 1,
      "pan_slide": 0,
      "cutoff_slide": 0,
      "env_curve": 2
    },
    "hiden": false
  },
  "ChipNoise": {
    "name": ":chipnoise",
    "inherit_arg": false,
    "inherit_base": "Noise",
    "summary": "Chip Noise",
    "opts": {
      "freq_band_slide": 0,
      "pan_slide_curve": 0,
      "amp_slide": 0,
      "freq_band_slide_shape": 1,
      "pan": 0,
      "amp_slide_shape": 0,
      "amp_slide_curve": 1,
      "freq_band": 0,
      "attack_level": 1,
      "sustain_level": 1,
      "attack": 0,
      "decay": 0,
      "sustain": 1,
      "pan_slide_shape": 1,
      "amp": 1,
      "pan_slide": 0,
      "decay_level": 1,
      "release": 0,
      "freq_band_slide_curve": 0,
      "env_curve": 0
    },
    "hiden": true
  },
  "CNoise": {
    "name": ":cnoise",
    "inherit_arg": true,
    "inherit_base": "Noise",
    "summary": "Clip Noise",
    "opts": {
      "amp_slide": 0,
      "res": 0,
      "pan": 0,
      "cutoff_slide_shape": 1,
      "decay": 0,
      "sustain_level": 1,
      "cutoff_slide_curve": 0,
      "decay_level": 1,
      "cutoff": 110,
      "release": 1,
      "res_slide_curve": 0,
      "res_slide": 0,
      "pan_slide_curve": 0,
      "attack": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "attack_level": 1,
      "env_curve": 2,
      "res_slide_shape": 1,
      "pan_slide_shape": 1,
      "amp": 1,
      "pan_slide": 0,
      "cutoff_slide": 0,
      "sustain": 0
    },
    "hiden": true
  },
  "DullBell": {
    "name": ":dull_bell",
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "summary": "Dull Bell",
    "opts": {
      "pan_slide_curve": 0,
      "amp_slide": 0,
      "attack": 0,
      "pan": 0,
      "amp_slide_shape": 1,
      "note_slide_shape": 1,
      "note": 52,
      "note_slide": 0,
      "sustain_level": 1,
      "note_slide_curve": 0,
      "decay": 0,
      "sustain": 0,
      "pan_slide_shape": 1,
      "amp": 1,
      "pan_slide": 0,
      "decay_level": 1,
      "attack_level": 1,
      "release": 1,
      "env_curve": 2,
      "amp_slide_curve": 0
    },
    "hiden": false
  },
  "SynthViolin": {
    "name": ":synth_violin",
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "summary": "Blade Runner style strings",
    "opts": {
      "pan_slide_shape": 1,
      "vibrato_depth_slide_curve": 0,
      "vibrato_depth_slide_shape": 1,
      "pan": 0,
      "vibrato_depth": 0.15,
      "note": 52,
      "note_slide": 0,
      "attack": 0,
      "vibrato_rate": 6,
      "decay": 0,
      "note_slide_shape": 1,
      "decay_level": 1,
      "cutoff_slide_curve": 0,
      "sustain_level": 1,
      "cutoff": 100,
      "release": 1,
      "vibrato_rate_slide_shape": 1,
      "pan_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "vibrato_onset": 0.1,
      "vibrato_rate_slide_curve": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "attack_level": 1,
      "vibrato_delay": 0.5,
      "note_slide_curve": 0,
      "sustain": 0,
      "amp_slide": 0,
      "amp": 1,
      "pan_slide": 0,
      "cutoff_slide": 0,
      "env_curve": 2
    },
    "hiden": false
  },
  "Hoover": {
    "name": ":hoover",
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "summary": "Hoover",
    "opts": {
      "pan_slide_shape": 1,
      "res_slide_shape": 1,
      "res": 0.1,
      "pan": 0,
      "note": 52,
      "note_slide": 0,
      "attack": 0.05,
      "decay": 0,
      "note_slide_shape": 1,
      "decay_level": 1,
      "cutoff_slide_curve": 0,
      "sustain_level": 1,
      "cutoff": 130,
      "release": 1,
      "res_slide_curve": 0,
      "res_slide": 0,
      "pan_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "attack_level": 1,
      "note_slide_curve": 0,
      "sustain": 0,
      "amp_slide": 0,
      "amp": 1,
      "pan_slide": 0,
      "cutoff_slide": 0,
      "env_curve": 2
    },
    "hiden": false
  },
  "SynthInfo": {
    "opts": {},
    "inherit_arg": true,
    "hiden": true,
    "inherit_base": "BaseInfo"
  },
  "ChipLead": {
    "name": ":chiplead",
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "summary": "Chip Lead",
    "opts": {
      "width": 0,
      "pan_slide_shape": 1,
      "pan": 0,
      "pan_slide_curve": 0,
      "note": 60,
      "note_slide": 0,
      "attack": 0,
      "decay": 0,
      "note_slide_shape": 1,
      "decay_level": 1,
      "sustain_level": 1,
      "release": 1,
      "note_resolution": 0.1,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "attack_level": 1,
      "note_slide_curve": 0,
      "sustain": 0,
      "amp_slide": 0,
      "amp": 1,
      "pan_slide": 0,
      "env_curve": 2
    },
    "hiden": false
  },
  "StudioInfo": {
    "opts": {},
    "inherit_arg": true,
    "hiden": true,
    "inherit_base": "SonicPiSynth"
  },
  "FM": {
    "name": ":fm",
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "summary": "Basic FM synthesis",
    "opts": {
      "depth_slide_curve": 0,
      "pan_slide_shape": 1,
      "divisor_slide_shape": 1,
      "divisor_slide_curve": 0,
      "depth_slide_shape": 1,
      "pan": 0,
      "note": 52,
      "note_slide": 0,
      "attack": 0,
      "decay": 0,
      "note_slide_shape": 1,
      "decay_level": 1,
      "cutoff_slide_curve": 0,
      "sustain_level": 1,
      "cutoff": 100,
      "release": 1,
      "divisor": 2,
      "pan_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "depth": 1,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "divisor_slide": 0,
      "attack_level": 1,
      "note_slide_curve": 0,
      "sustain": 0,
      "amp_slide": 0,
      "amp": 1,
      "pan_slide": 0,
      "cutoff_slide": 0,
      "depth_slide": 0,
      "env_curve": 2
    },
    "hiden": false
  },
  "SoundInStereo": {
    "name": ":sound_in_stereo",
    "inherit_arg": true,
    "inherit_base": "SoundIn",
    "summary": "Sound In Stereo",
    "opts": {
      "amp_slide_shape": 1,
      "pan_slide_shape": 1,
      "pan": 0,
      "attack": 0,
      "decay": 0,
      "decay_level": 1,
      "sustain_level": 1,
      "release": 0,
      "pan_slide_curve": 0,
      "input": 1,
      "amp_slide_curve": 0,
      "attack_level": 1,
      "sustain": 1,
      "amp_slide": 0,
      "amp": 1,
      "pan_slide": 0,
      "env_curve": 0
    },
    "hiden": true
  },
  "Hollow": {
    "name": ":hollow",
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "summary": "Hollow",
    "opts": {
      "noise": 1,
      "pan_slide_shape": 1,
      "norm": 0,
      "res_slide_shape": 1,
      "res": 0.99,
      "pan": 0,
      "note": 52,
      "note_slide": 0,
      "attack": 0,
      "decay": 0,
      "note_slide_shape": 1,
      "decay_level": 1,
      "cutoff_slide_curve": 0,
      "sustain_level": 1,
      "cutoff": 90,
      "release": 1,
      "res_slide_curve": 0,
      "res_slide": 0,
      "pan_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "attack_level": 1,
      "note_slide_curve": 0,
      "sustain": 0,
      "amp_slide": 0,
      "amp": 1,
      "pan_slide": 0,
      "cutoff_slide": 0,
      "env_curve": 2
    },
    "hiden": false
  },
  "BaseMixer": {
    "opts": {},
    "inherit_arg": true,
    "hiden": true,
    "inherit_base": "StudioInfo"
  },
  "Saw": {
    "name": ":saw",
    "inherit_arg": true,
    "inherit_base": "Beep",
    "summary": "Saw Wave",
    "opts": {
      "pan_slide_shape": 1,
      "pan": 0,
      "note": 52,
      "note_slide": 0,
      "attack": 0,
      "decay": 0,
      "note_slide_shape": 1,
      "decay_level": 1,
      "sustain_level": 1,
      "release": 1,
      "pan_slide_curve": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "attack_level": 1,
      "note_slide_curve": 0,
      "sustain": 0,
      "amp_slide": 0,
      "amp": 1,
      "pan_slide": 0,
      "env_curve": 2
    },
    "hiden": true
  },
  "DarkAmbience": {
    "name": ":dark_ambience",
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "summary": "Dark Ambience",
    "opts": {
      "noise": 0,
      "pan_slide_shape": 1,
      "detune2_slide_curve": 0,
      "res_slide_shape": 1,
      "res": 0.7,
      "detune1_slide": 0,
      "pan": 0,
      "detune2": 24,
      "note": 52,
      "note_slide": 0,
      "attack": 0,
      "reverb_time": 100,
      "decay": 0,
      "detune2_slide_shape": 1,
      "note_slide_shape": 1,
      "decay_level": 1,
      "cutoff_slide_curve": 0,
      "sustain_level": 1,
      "cutoff": 110,
      "detune2_slide": 0,
      "release": 1,
      "res_slide_curve": 0,
      "res_slide": 0,
      "detune1_slide_shape": 1,
      "pan_slide_curve": 0,
      "ring": 0.2,
      "room": 70,
      "cutoff_slide_shape": 1,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "attack_level": 1,
      "note_slide_curve": 0,
      "sustain": 0,
      "amp_slide": 0,
      "amp": 1,
      "pan_slide": 0,
      "cutoff_slide": 0,
      "detune1": 12,
      "detune1_slide_curve": 0,
      "env_curve": 2
    },
    "hiden": false
  },
  "DTri": {
    "name": ":dtri",
    "inherit_arg": true,
    "inherit_base": "DSaw",
    "summary": "Detuned Triangle Wave",
    "opts": {
      "amp_slide": 0,
      "pan": 0,
      "detune_slide_curve": 0,
      "note": 52,
      "note_slide": 0,
      "attack": 0,
      "decay": 0,
      "note_slide_shape": 1,
      "sustain_level": 1,
      "cutoff_slide_curve": 0,
      "decay_level": 1,
      "cutoff": 100,
      "release": 1,
      "pan_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "attack_level": 1,
      "note_slide_curve": 0,
      "detune_slide": 0,
      "sustain": 0,
      "pan_slide_shape": 1,
      "amp": 1,
      "pan_slide": 0,
      "detune_slide_shape": 1,
      "cutoff_slide": 0,
      "env_curve": 2,
      "detune": 0.1
    },
    "hiden": true
  },
  "SoundIn": {
    "name": ":sound_in",
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "summary": "Sound In",
    "opts": {
      "pan_slide_curve": 0,
      "input": 1,
      "amp_slide": 0,
      "pan": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "attack_level": 1,
      "sustain_level": 1,
      "attack": 0,
      "decay": 0,
      "sustain": 1,
      "pan_slide_shape": 1,
      "amp": 1,
      "pan_slide": 0,
      "decay_level": 1,
      "release": 0,
      "env_curve": 0
    },
    "hiden": false
  },
  "TB303": {
    "name": ":tb303",
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "summary": "TB-303 Emulation",
    "opts": {
      "cutoff_sustain_level": 1,
      "res": 0.9,
      "pulse_width_slide": 0,
      "note_slide": 0,
      "attack": 0,
      "wave": 0,
      "cutoff_decay": 0,
      "cutoff_min_slide": 0,
      "cutoff_slide_curve": 0,
      "sustain_level": 1,
      "cutoff": 120,
      "res_slide_curve": 0,
      "res_slide": 0,
      "cutoff_slide_shape": 1,
      "amp_slide_curve": 0,
      "cutoff_sustain": 0,
      "attack_level": 1,
      "res_slide_shape": 1,
      "amp": 1,
      "pan_slide": 0,
      "cutoff_attack_level": 1,
      "env_curve": 2,
      "pulse_width_slide_shape": 1,
      "pulse_width": 0.5,
      "cutoff_min_slide_curve": 0,
      "cutoff_min_slide_shape": 1,
      "amp_slide": 0,
      "pan": 0,
      "note": 52,
      "decay": 0,
      "note_slide_shape": 1,
      "cutoff_attack": 0,
      "decay_level": 1,
      "release": 1,
      "pan_slide_curve": 0,
      "cutoff_release": 1,
      "amp_slide_shape": 1,
      "cutoff_decay_level": 1,
      "cutoff_min": 30,
      "note_slide_curve": 0,
      "sustain": 0,
      "pan_slide_shape": 1,
      "pulse_width_slide_curve": 0,
      "cutoff_slide": 0
    },
    "hiden": false
  },
  "DarkSeaHorn": {
    "name": ":dark_sea_horn",
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "summary": "Dark Sea Horn",
    "opts": {
      "pan_slide_curve": 0,
      "amp_slide": 0,
      "attack": 1,
      "pan": 0,
      "amp_slide_shape": 1,
      "note_slide_shape": 1,
      "note": 52,
      "note_slide": 0,
      "sustain_level": 1,
      "note_slide_curve": 0,
      "decay": 0,
      "sustain": 0,
      "pan_slide_shape": 1,
      "amp": 1,
      "pan_slide": 0,
      "decay_level": 1,
      "attack_level": 1,
      "release": 4.0,
      "env_curve": 2,
      "amp_slide_curve": 0
    },
    "hiden": true
  },
  "Prophet": {
    "name": ":prophet",
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "summary": "The Prophet",
    "opts": {
      "pan_slide_shape": 1,
      "res_slide_shape": 1,
      "res": 0.7,
      "pan": 0,
      "note": 52,
      "note_slide": 0,
      "attack": 0,
      "decay": 0,
      "note_slide_shape": 1,
      "decay_level": 1,
      "cutoff_slide_curve": 0,
      "sustain_level": 1,
      "cutoff": 110,
      "release": 1,
      "res_slide_curve": 0,
      "res_slide": 0,
      "pan_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "attack_level": 1,
      "note_slide_curve": 0,
      "sustain": 0,
      "amp_slide": 0,
      "amp": 1,
      "pan_slide": 0,
      "cutoff_slide": 0,
      "env_curve": 2
    },
    "hiden": false
  },
  "MonoPlayer": {
    "name": ":mono_player",
    "inherit_arg": false,
    "inherit_base": "BasicMonoPlayer",
    "summary": "Mono Sample Player",
    "opts": {
      "hpf_release_level": -1,
      "lpf_sustain_level": -1,
      "relax_time_slide_curve": 0,
      "clamp_time": 0.01,
      "lpf_decay_level": -1,
      "pitch": 0,
      "slope_above": 0.5,
      "hpf_init_level": -1,
      "window_size_slide_shape": 1,
      "time_dis_slide": 0,
      "amp_slide_curve": 0,
      "rate": 1,
      "window_size_slide": 0,
      "clamp_time_slide_shape": 1,
      "lpf_env_curve": 2,
      "lpf_decay": 0,
      "pre_amp_slide_shape": 1,
      "threshold_slide_curve": 0,
      "slope_below_slide_shape": 1,
      "hpf_sustain": -1,
      "pitch_dis_slide_shape": 1,
      "hpf_slide_shape": 1,
      "hpf_decay": 0,
      "lpf": -1,
      "pan_slide": 0,
      "time_dis_slide_curve": 0,
      "hpf_slide": 0,
      "slope_above_slide": 0,
      "pre_amp": 1,
      "release": 0,
      "lpf_slide_curve": 0,
      "pan_slide_curve": 0,
      "lpf_attack_level": -1,
      "lpf_sustain": -1,
      "hpf_sustain_level": -1,
      "pre_amp_slide_curve": 0,
      "hpf_env_curve": 2,
      "pitch_slide_shape": 1,
      "pan_slide_shape": 1,
      "slope_below_slide_curve": 0,
      "hpf_decay_level": -1,
      "hpf_max_slide": 0,
      "hpf_slide_curve": 0,
      "hpf_max": -1,
      "lpf_slide": 0,
      "norm": 0,
      "hpf": -1,
      "finish": 1,
      "hpf_release": 0,
      "attack": 0,
      "hpf_max_slide_shape": 1,
      "lpf_release": 0,
      "sustain_level": 1,
      "pitch_slide": 0,
      "lpf_release_level": -1,
      "pre_amp_slide": 0,
      "threshold": 0.2,
      "slope_above_slide_curve": 0,
      "relax_time": 0.01,
      "clamp_time_slide_curve": 0,
      "threshold_slide_shape": 1,
      "attack_level": 1,
      "slope_below_slide": 0,
      "threshold_slide": 0,
      "pitch_dis": 0.0,
      "env_curve": 2,
      "lpf_min_slide_curve": 0,
      "amp": 1,
      "lpf_init_level": -1,
      "time_dis": 0.0,
      "lpf_attack": 0,
      "lpf_min": -1,
      "pan": 0,
      "hpf_attack": 0,
      "slope_above_slide_shape": 1,
      "start": 0,
      "pitch_dis_slide_curve": 0,
      "window_size": 0.2,
      "decay_level": 1,
      "clamp_time_slide": 0,
      "relax_time_slide_shape": 1,
      "pitch_slide_curve": 0,
      "lpf_min_slide": 0,
      "slope_below": 1,
      "time_dis_slide_shape": 1,
      "amp_slide_shape": 1,
      "compress": 0,
      "lpf_min_slide_shape": 1,
      "pitch_dis_slide": 0,
      "hpf_attack_level": -1,
      "window_size_slide_curve": 0,
      "lpf_slide_shape": 1,
      "sustain": -1,
      "amp_slide": 0,
      "relax_time_slide": 0,
      "decay": 0,
      "hpf_max_slide_curve": 0
    },
    "hiden": true
  },
  "BNoise": {
    "name": ":bnoise",
    "inherit_arg": true,
    "inherit_base": "Noise",
    "summary": "Brown Noise",
    "opts": {
      "amp_slide": 0,
      "res": 0,
      "pan": 0,
      "cutoff_slide_shape": 1,
      "decay": 0,
      "sustain_level": 1,
      "cutoff_slide_curve": 0,
      "decay_level": 1,
      "cutoff": 110,
      "release": 1,
      "res_slide_curve": 0,
      "res_slide": 0,
      "pan_slide_curve": 0,
      "attack": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "attack_level": 1,
      "env_curve": 2,
      "res_slide_shape": 1,
      "pan_slide_shape": 1,
      "amp": 1,
      "pan_slide": 0,
      "cutoff_slide": 0,
      "sustain": 0
    },
    "hiden": true
  },
  "StereoPlayer": {
    "name": ":stereo_player",
    "inherit_arg": true,
    "inherit_base": "MonoPlayer",
    "summary": "Stereo Sample Player",
    "opts": {
      "hpf_release_level": -1,
      "lpf_sustain_level": -1,
      "clamp_time": 0.01,
      "lpf_decay_level": -1,
      "pitch": 0,
      "slope_above": 0.5,
      "window_size_slide_curve": 0,
      "hpf_init_level": -1,
      "window_size_slide_shape": 1,
      "time_dis_slide": 0,
      "amp_slide_curve": 0,
      "rate": 1,
      "window_size_slide": 0,
      "clamp_time_slide_shape": 1,
      "lpf_env_curve": 2,
      "lpf_decay": 0,
      "pre_amp_slide_shape": 1,
      "threshold_slide_curve": 0,
      "lpf_min_slide_curve": 0,
      "hpf_sustain": -1,
      "pitch_dis_slide_shape": 1,
      "hpf_slide_shape": 1,
      "hpf_decay": 0,
      "lpf": -1,
      "pan_slide": 0,
      "relax_time_slide_curve": 0,
      "hpf_slide": 0,
      "slope_above_slide": 0,
      "pre_amp": 1,
      "release": 0,
      "lpf_slide_curve": 0,
      "pan_slide_curve": 0,
      "lpf_sustain": -1,
      "hpf_sustain_level": -1,
      "pre_amp_slide_curve": 0,
      "hpf_env_curve": 2,
      "pitch_slide_shape": 1,
      "pan_slide_shape": 1,
      "slope_below_slide_curve": 0,
      "hpf_decay_level": -1,
      "hpf_max_slide": 0,
      "hpf_max": -1,
      "lpf_slide": 0,
      "norm": 0,
      "hpf": -1,
      "compress": 0,
      "hpf_release": 0,
      "attack": 0,
      "hpf_max_slide_shape": 1,
      "lpf_release": 0,
      "pitch_dis_slide": 0,
      "pitch_slide": 0,
      "sustain_level": 1,
      "lpf_release_level": -1,
      "pre_amp_slide": 0,
      "threshold": 0.2,
      "slope_above_slide_curve": 0,
      "relax_time": 0.01,
      "clamp_time_slide_curve": 0,
      "threshold_slide_shape": 1,
      "attack_level": 1,
      "slope_below_slide": 0,
      "threshold_slide": 0,
      "pitch_dis": 0.0,
      "env_curve": 2,
      "slope_below_slide_shape": 1,
      "amp": 1,
      "lpf_init_level": -1,
      "time_dis": 0.0,
      "decay": 0,
      "lpf_attack": 0,
      "lpf_min": -1,
      "pan": 0,
      "hpf_attack": 0,
      "slope_above_slide_shape": 1,
      "start": 0,
      "pitch_dis_slide_curve": 0,
      "window_size": 0.2,
      "decay_level": 1,
      "clamp_time_slide": 0,
      "relax_time_slide_shape": 1,
      "pitch_slide_curve": 0,
      "lpf_min_slide": 0,
      "slope_below": 1,
      "time_dis_slide_shape": 1,
      "amp_slide_shape": 1,
      "finish": 1,
      "lpf_min_slide_shape": 1,
      "hpf_slide_curve": 0,
      "hpf_attack_level": -1,
      "lpf_attack_level": -1,
      "lpf_slide_shape": 1,
      "sustain": -1,
      "amp_slide": 0,
      "relax_time_slide": 0,
      "time_dis_slide_curve": 0,
      "hpf_max_slide_curve": 0
    },
    "hiden": true
  },
  "ChipBass": {
    "name": ":chipbass",
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "summary": "Chip Bass",
    "opts": {
      "note_resolution": 0.1,
      "note_slide_shape": 1,
      "attack": 0,
      "amp_slide_curve": 0,
      "amp_slide_shape": 1,
      "pan": 0,
      "pan_slide_curve": 0,
      "note": 60,
      "note_slide": 0,
      "sustain_level": 1,
      "note_slide_curve": 0,
      "decay": 0,
      "sustain": 0,
      "amp_slide": 0,
      "amp": 1,
      "pan_slide": 0,
      "decay_level": 1,
      "attack_level": 1,
      "release": 1,
      "pan_slide_shape": 1,
      "env_curve": 2
    },
    "hiden": false
  },
  "DSaw": {
    "name": ":dsaw",
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "summary": "Detuned Saw wave",
    "opts": {
      "pan_slide_shape": 1,
      "pan": 0,
      "detune_slide_curve": 0,
      "note": 52,
      "note_slide": 0,
      "attack": 0,
      "decay": 0,
      "note_slide_shape": 1,
      "decay_level": 1,
      "cutoff_slide_curve": 0,
      "sustain_level": 1,
      "cutoff": 100,
      "release": 1,
      "detune_slide_shape": 1,
      "pan_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "attack_level": 1,
      "note_slide_curve": 0,
      "sustain": 0,
      "amp_slide": 0,
      "amp": 1,
      "pan_slide": 0,
      "detune_slide": 0,
      "cutoff_slide": 0,
      "detune": 0.1,
      "env_curve": 2
    },
    "hiden": false
  },
  "Zawa": {
    "name": ":zawa",
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "summary": "Zawa",
    "opts": {
      "phase": 1,
      "range_slide_shape": 1,
      "pulse_width": 0.5,
      "pan_slide_shape": 1,
      "phase_offset": 0,
      "pulse_width_slide_shape": 1,
      "res": 0.9,
      "phase_slide_shape": 1,
      "pulse_width_slide": 0,
      "pan": 0,
      "phase_slide": 0,
      "note": 52,
      "note_slide": 0,
      "attack": 0,
      "wave": 3,
      "decay": 0,
      "note_slide_shape": 1,
      "decay_level": 1,
      "cutoff_slide_curve": 0,
      "sustain_level": 1,
      "cutoff": 100,
      "invert_wave": 0,
      "release": 1,
      "res_slide_curve": 0,
      "range_slide": 0,
      "res_slide": 0,
      "pan_slide_curve": 0,
      "range": 24,
      "cutoff_slide_shape": 1,
      "range_slide_curve": 0,
      "phase_slide_curve": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "attack_level": 1,
      "note_slide_curve": 0,
      "sustain": 0,
      "amp_slide": 0,
      "amp": 1,
      "pan_slide": 0,
      "cutoff_slide": 0,
      "disable_wave": 0,
      "pulse_width_slide_curve": 0,
      "res_slide_shape": 1
    },
    "hiden": false
  },
  "SynthPluck": {
    "name": ":pluck",
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "summary": "SynthPluck",
    "opts": {
      "pan_slide_shape": 1,
      "coef": 0.3,
      "pan": 0,
      "note": 52,
      "note_slide": 0,
      "attack": 0,
      "decay": 0,
      "note_slide_shape": 1,
      "decay_level": 1,
      "sustain_level": 1,
      "release": 1,
      "pan_slide_curve": 0,
      "max_delay_time": 0.125,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "attack_level": 1,
      "pluck_decay": 30,
      "note_slide_curve": 0,
      "sustain": 0,
      "amp_slide": 0,
      "amp": 1,
      "noise_amp": 0.8,
      "pan_slide": 0
    },
    "hiden": false
  },
  "Singer": {
    "name": ":singer",
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "summary": "Singer",
    "opts": {
      "pan_slide_curve": 0,
      "amp_slide": 0,
      "attack": 1,
      "pan": 0,
      "amp_slide_shape": 1,
      "note_slide_shape": 1,
      "note": 52,
      "note_slide": 0,
      "sustain_level": 1,
      "note_slide_curve": 0,
      "decay": 0,
      "sustain": 0,
      "pan_slide_shape": 1,
      "amp": 1,
      "pan_slide": 0,
      "decay_level": 1,
      "attack_level": 1,
      "release": 4.0,
      "env_curve": 2,
      "amp_slide_curve": 0
    },
    "hiden": true
  },
  "ModFM": {
    "name": ":mod_fm",
    "inherit_arg": true,
    "inherit_base": "FM",
    "summary": "Basic FM synthesis with frequency modulation.",
    "opts": {
      "depth_slide_curve": 0,
      "depth_slide_shape": 1,
      "divisor_slide_curve": 0,
      "note_slide": 0,
      "mod_range": 5,
      "attack": 0,
      "mod_phase_offset": 0,
      "depth": 1,
      "cutoff_slide_curve": 0,
      "sustain_level": 1,
      "cutoff": 100,
      "amp_slide_curve": 0,
      "divisor_slide": 0,
      "attack_level": 1,
      "env_curve": 2,
      "divisor": 2,
      "amp": 1,
      "pan_slide": 0,
      "mod_invert_wave": 0,
      "mod_pulse_width": 0.5,
      "amp_slide": 0,
      "mod_wave": 1,
      "divisor_slide_shape": 1,
      "depth_slide": 0,
      "pan": 0,
      "note": 52,
      "decay": 0,
      "note_slide_shape": 1,
      "decay_level": 1,
      "release": 1,
      "pan_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "amp_slide_shape": 1,
      "note_slide_curve": 0,
      "sustain": 0,
      "pan_slide_shape": 1,
      "cutoff_slide": 0,
      "mod_phase": 0.25
    },
    "hiden": true
  },
  "SonicPiSynth": {
    "opts": {},
    "inherit_arg": true,
    "hiden": true,
    "inherit_base": "SynthInfo"
  },
  "Pulse": {
    "name": ":pulse",
    "inherit_arg": true,
    "inherit_base": "Square",
    "summary": "Pulse Wave",
    "opts": {
      "pulse_width_slide_shape": 1,
      "pulse_width": 0.5,
      "amp_slide": 0,
      "pulse_width_slide": 0,
      "pan": 0,
      "note": 52,
      "note_slide": 0,
      "attack": 0,
      "decay": 0,
      "note_slide_shape": 1,
      "sustain_level": 1,
      "cutoff_slide_curve": 0,
      "decay_level": 1,
      "cutoff": 100,
      "release": 1,
      "pan_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "attack_level": 1,
      "note_slide_curve": 0,
      "sustain": 0,
      "pan_slide_shape": 1,
      "amp": 1,
      "pan_slide": 0,
      "cutoff_slide": 0,
      "env_curve": 2
    },
    "hiden": true
  }
}

synth_nodes = {
  ":fx_wobble": "FXWobble",
  ":fx_replace_rlpf": "FXRLPF",
  ":fx_replace_nlpf": "FXNormLPF",
  ":beep": "Beep",
  ":fx_bitcrusher": "FXBitcrusher",
  ":dsaw": "DSaw",
  ":fx_reverb": "FXReverb",
  ":fx_replace_nhpf": "FXNormHPF",
  ":sound_in": "SoundIn",
  ":zawa": "Zawa",
  ":bnoise": "BNoise",
  ":fx_normaliser": "FXNormaliser",
  ":fx_nbpf": "FXNBPF",
  ":fx_band_eq": "FXBandEQ",
  ":noise": "Noise",
  ":mod_dsaw": "ModDSaw",
  ":pretty_bell": "PrettyBell",
  ":fx_pitch_shift": "FXPitchShift",
  ":basic_mono_player": "BasicMonoPlayer",
  ":fm": "FM",
  ":fx_rlpf": "FXRLPF",
  ":sound_in_stereo": "SoundInStereo",
  ":fx_whammy": "FXWhammy",
  ":pnoise": "PNoise",
  ":fx_panslicer": "FXPanSlicer",
  ":fx_replace_ixi_techno": "FXIXITechno",
  ":fx_replace_reverb": "FXReverb",
  ":fx_echo": "FXEcho",
  ":main_mixer": "MainMixer",
  ":dull_bell": "DullBell",
  ":fx_replace_slicer": "FXSlicer",
  ":fx_replace_nrhpf": "FXNormRHPF",
  ":basic_stereo_player": "BasicStereoPlayer",
  ":mod_pulse": "ModPulse",
  ":fx_octaver": "FXOctaver",
  ":hoover": "Hoover",
  ":fx_nrbpf": "FXNRBPF",
  ":chipnoise": "ChipNoise",
  ":fx_level": "FXLevel",
  ":fx_rhpf": "FXRHPF",
  ":fx_ring_mod": "FXRingMod",
  ":fx_slicer": "FXSlicer",
  ":fx_replace_hpf": "FXHPF",
  ":fx_pan": "FXPan",
  ":mod_tri": "ModTri",
  ":basic_mixer": "BasicMixer",
  ":fx_vowel": "FXVowel",
  ":growl": "Growl",
  ":cnoise": "CNoise",
  ":fx_hpf": "FXHPF",
  ":fx_distortion": "FXDistortion",
  ":hollow": "Hollow",
  ":gnoise": "GNoise",
  ":mod_beep": "ModSine",
  ":mod_sine": "ModSine",
  ":chipbass": "ChipBass",
  ":fx_replace_lpf": "FXLPF",
  ":fx_gverb": "FXGVerb",
  ":tri": "Tri",
  ":saw": "Saw",
  ":mod_saw": "ModSaw",
  ":fx_nrlpf": "FXNormRLPF",
  ":fx_compressor": "FXCompressor",
  ":sine": "Beep",
  ":fx_nhpf": "FXNormHPF",
  ":piano": "SynthPiano",
  ":tb303": "TB303",
  ":fx_mono": "FXMono",
  ":tech_saws": "TechSaws",
  ":fx_nlpf": "FXNormLPF",
  ":stereo_player": "StereoPlayer",
  ":mod_fm": "ModFM",
  ":supersaw": "Supersaw",
  ":mono_player": "MonoPlayer",
  ":dpulse": "DPulse",
  ":fx_replace_echo": "FXEcho",
  ":fx_replace_normaliser": "FXNormaliser",
  ":prophet": "Prophet",
  ":fx_rbpf": "FXRBPF",
  ":fx_replace_pan": "FXPan",
  ":fx_bpf": "FXBPF",
  ":fx_replace_wobble": "FXWobble",
  ":pulse": "Pulse",
  ":fx_krush": "FXKrush",
  ":fx_nrhpf": "FXNormRHPF",
  ":pluck": "SynthPluck",
  ":fx_replace_level": "FXLevel",
  ":fx_replace_compressor": "FXCompressor",
  ":blade": "SynthViolin",
  ":fx_replace_nrlpf": "FXNormRLPF",
  ":dtri": "DTri",
  ":fx_replace_distortion": "FXDistortion",
  ":chiplead": "ChipLead",
  ":square": "Square",
  ":fx_tanh": "FXTanh",
  ":fx_ixi_techno": "FXIXITechno",
  ":fx_flanger": "FXFlanger",
  ":subpulse": "SubPulse",
  ":fx_replace_rhpf": "FXRHPF",
  ":fx_lpf": "FXLPF",
  ":dark_ambience": "DarkAmbience"
}

fx = {
  "FXBitcrusher": {
    "name": ":bitcrusher",
    "inherit_arg": true,
    "inherit_base": "FXInfo",
    "summary": "Bitcrusher",
    "opts": {
      "amp_slide_shape": 1,
      "mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_mix": 1,
      "mix_slide": 0,
      "cutoff_slide_shape": 1,
      "bits_slide_curve": 0,
      "pre_amp": 1,
      "bits": 8,
      "cutoff": 0,
      "bits_slide_shape": 1,
      "pre_amp_slide": 0,
      "sample_rate_slide": 0,
      "mix": 1,
      "sample_rate_slide_shape": 1,
      "sample_rate": 10000,
      "cutoff_slide_curve": 0,
      "pre_amp_slide_curve": 0,
      "amp_slide_curve": 0,
      "mix_slide_curve": 0,
      "pre_mix_slide": 0,
      "amp_slide": 0,
      "amp": 1,
      "cutoff_slide": 0,
      "bits_slide": 0,
      "pre_mix_slide_shape": 1,
      "sample_rate_slide_curve": 0,
      "pre_amp_slide_shape": 1
    },
    "hiden": false
  },
  "FXRHPF": {
    "name": ":rhpf",
    "inherit_arg": true,
    "inherit_base": "FXHPF",
    "summary": "Resonant High Pass Filter",
    "opts": {
      "pre_amp_slide_curve": 0,
      "mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_mix": 1,
      "res": 0.5,
      "mix_slide": 0,
      "pre_amp": 1,
      "cutoff_slide_curve": 0,
      "cutoff": 100,
      "res_slide_curve": 0,
      "pre_amp_slide": 0,
      "res_slide": 0,
      "mix": 1,
      "cutoff_slide_shape": 1,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "mix_slide_curve": 0,
      "pre_mix_slide": 0,
      "res_slide_shape": 1,
      "amp_slide": 0,
      "amp": 1,
      "cutoff_slide": 0,
      "pre_mix_slide_shape": 1,
      "pre_amp_slide_shape": 1
    },
    "hiden": true
  },
  "FXWobble": {
    "name": ":wobble",
    "inherit_arg": true,
    "inherit_base": "FXInfo",
    "summary": "Wobble",
    "opts": {
      "smooth_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "smooth_up_slide_curve": 0,
      "mix_slide_shape": 1,
      "pre_mix": 1,
      "res": 0.8,
      "mix_slide": 0,
      "pulse_width_slide": 0,
      "prob_pos_slide": 0,
      "prob_pos_slide_shape": 1,
      "smooth_slide_curve": 0,
      "wave": 0,
      "probability_slide": 0,
      "cutoff_min_slide": 0,
      "res_slide_curve": 0,
      "probability_slide_shape": 1,
      "phase": 0.5,
      "pre_amp_slide": 0,
      "res_slide": 0,
      "cutoff_min": 60,
      "mix": 1,
      "phase_offset": 0,
      "probability_slide_curve": 0,
      "amp_slide_curve": 0,
      "mix_slide_curve": 0,
      "probability": 0,
      "phase_slide_shape": 1,
      "seed": 0,
      "smooth_down_slide_shape": 1,
      "prob_pos_slide_curve": 0,
      "cutoff_max": 120,
      "amp": 1,
      "smooth_down": 0,
      "pre_mix_slide_shape": 1,
      "pre_amp_slide_shape": 1,
      "pulse_width_slide_shape": 1,
      "pulse_width": 0.5,
      "cutoff_min_slide_curve": 0,
      "pre_mix_slide_curve": 0,
      "smooth_down_slide": 0,
      "cutoff_max_slide_curve": 0,
      "cutoff_max_slide_shape": 1,
      "phase_slide": 0,
      "prob_pos": 0,
      "pre_amp": 1,
      "smooth_down_slide_curve": 0,
      "cutoff_min_slide_shape": 1,
      "smooth_up_slide": 0,
      "smooth_slide": 0,
      "filter": 0,
      "cutoff_max_slide": 0,
      "phase_slide_curve": 0,
      "amp_slide_shape": 1,
      "smooth_up_slide_shape": 1,
      "invert_wave": 0,
      "pre_mix_slide": 0,
      "smooth": 0,
      "res_slide_shape": 1,
      "amp_slide": 0,
      "smooth_up": 0,
      "pulse_width_slide_curve": 0
    },
    "hiden": false
  },
  "FXPan": {
    "name": ":pan",
    "inherit_arg": true,
    "inherit_base": "FXInfo",
    "summary": "Pan",
    "opts": {
      "amp_slide_shape": 1,
      "mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_mix": 1,
      "mix_slide": 0,
      "pan": 0,
      "pan_slide_curve": 0,
      "pre_amp": 1,
      "pre_amp_slide": 0,
      "mix": 1,
      "pan_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "amp_slide_curve": 0,
      "mix_slide_curve": 0,
      "pre_mix_slide": 0,
      "amp_slide": 0,
      "amp": 1,
      "pan_slide": 0,
      "pre_mix_slide_shape": 1,
      "pre_amp_slide_shape": 1
    },
    "hiden": false
  },
  "FXOctaver": {
    "name": ":octaver",
    "inherit_arg": true,
    "inherit_base": "FXInfo",
    "summary": "Octaver",
    "opts": {
      "sub_amp_slide_curve": 0,
      "amp_slide_shape": 1,
      "mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_mix": 1,
      "sub_amp_slide_shape": 1,
      "mix_slide": 0,
      "super_amp_slide": 0,
      "subsub_amp_slide_curve": 0,
      "sub_amp": 1,
      "pre_amp": 1,
      "super_amp_slide_shape": 1,
      "subsub_amp_slide_shape": 1,
      "pre_amp_slide": 0,
      "subsub_amp": 1,
      "mix": 1,
      "super_amp": 1,
      "super_amp_slide_curve": 0,
      "pre_amp_slide_curve": 0,
      "amp_slide_curve": 0,
      "mix_slide_curve": 0,
      "sub_amp_slide": 0,
      "pre_mix_slide": 0,
      "amp_slide": 0,
      "amp": 1,
      "subsub_amp_slide": 0,
      "pre_mix_slide_shape": 1,
      "pre_amp_slide_shape": 1
    },
    "hiden": false
  },
  "FXChorus": {
    "name": ":chorus",
    "inherit_arg": true,
    "inherit_base": "FXInfo",
    "summary": "Chorus",
    "opts": {
      "amp_slide_shape": 1,
      "mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_mix": 1,
      "mix_slide": 0,
      "decay_slide_shape": 1,
      "phase_slide": 0,
      "decay": 1e-05,
      "pre_amp": 1,
      "phase": 0.25,
      "pre_amp_slide": 0,
      "max_phase": 1,
      "mix": 1,
      "decay_slide": 0,
      "phase_slide_curve": 0,
      "pre_amp_slide_curve": 0,
      "amp_slide_curve": 0,
      "mix_slide_curve": 0,
      "pre_mix_slide": 0,
      "phase_slide_shape": 1,
      "amp_slide": 0,
      "amp": 1,
      "decay_slide_curve": 0,
      "pre_mix_slide_shape": 1,
      "pre_amp_slide_shape": 1
    },
    "hiden": true
  },
  "FXEcho": {
    "name": ":echo",
    "inherit_arg": true,
    "inherit_base": "FXInfo",
    "summary": "Echo",
    "opts": {
      "amp_slide_shape": 1,
      "mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_mix": 1,
      "mix_slide": 0,
      "decay_slide_shape": 1,
      "phase_slide": 0,
      "decay": 2,
      "pre_amp": 1,
      "phase": 0.25,
      "pre_amp_slide": 0,
      "max_phase": 2,
      "mix": 1,
      "decay_slide": 0,
      "phase_slide_curve": 0,
      "pre_amp_slide_curve": 0,
      "amp_slide_curve": 0,
      "mix_slide_curve": 0,
      "pre_mix_slide": 0,
      "phase_slide_shape": 1,
      "amp_slide": 0,
      "amp": 1,
      "decay_slide_curve": 0,
      "pre_mix_slide_shape": 1,
      "pre_amp_slide_shape": 1
    },
    "hiden": false
  },
  "FXInfo": {
    "opts": {
      "mix": 1,
      "pre_amp_slide_curve": 0,
      "mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_mix": 1,
      "mix_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "mix_slide_curve": 0,
      "pre_mix_slide": 0,
      "amp_slide": 0,
      "amp": 1,
      "pre_amp": 1,
      "pre_mix_slide_shape": 1,
      "pre_amp_slide": 0,
      "pre_amp_slide_shape": 1
    },
    "inherit_arg": false,
    "hiden": true,
    "inherit_base": "BaseInfo"
  },
  "FXRingMod": {
    "name": ":ring_mod",
    "inherit_arg": true,
    "inherit_base": "FXInfo",
    "summary": "Ring Modulator",
    "opts": {
      "freq_slide": 0,
      "amp_slide_shape": 1,
      "mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_mix": 1,
      "mod_amp_slide": 0,
      "mix_slide": 0,
      "mod_amp_slide_shape": 1,
      "pre_amp": 1,
      "freq_slide_curve": 0,
      "pre_amp_slide": 0,
      "mix": 1,
      "mod_amp": 1,
      "pre_amp_slide_curve": 0,
      "amp_slide_curve": 0,
      "mix_slide_curve": 0,
      "pre_mix_slide": 0,
      "freq": 30,
      "freq_slide_shape": 1,
      "amp_slide": 0,
      "amp": 1,
      "pre_mix_slide_shape": 1,
      "mod_amp_slide_curve": 0,
      "pre_amp_slide_shape": 1
    },
    "hiden": false
  },
  "FXPanSlicer": {
    "name": ":panslicer",
    "inherit_arg": true,
    "inherit_base": "FXSlicer",
    "summary": "Pan Slicer",
    "opts": {
      "amp_min_slide_curve": 0,
      "amp_min_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "smooth_up_slide_curve": 0,
      "mix_slide_shape": 1,
      "pan_max_slide_shape": 1,
      "pre_mix": 1,
      "invert_wave": 0,
      "pan_max_slide": 0,
      "mix_slide": 0,
      "pulse_width_slide": 0,
      "prob_pos_slide": 0,
      "mix_slide_curve": 0,
      "pan_max": 1,
      "amp_min": 0,
      "wave": 1,
      "probability_slide": 0,
      "probability_slide_shape": 1,
      "phase": 0.25,
      "pre_amp_slide": 0,
      "amp_slide_shape": 1,
      "smooth": 0,
      "amp_max": 1,
      "pre_mix_slide_curve": 0,
      "amp_max_slide_curve": 0,
      "probability_slide_curve": 0,
      "amp_slide_curve": 0,
      "prob_pos_slide_shape": 1,
      "amp_max_slide_shape": 1,
      "probability": 0,
      "phase_slide_shape": 1,
      "smooth_down_slide_shape": 1,
      "prob_pos_slide_curve": 0,
      "amp": 1,
      "pan_min_slide": 0,
      "pre_mix_slide_shape": 1,
      "pre_amp_slide_shape": 1,
      "pulse_width_slide_shape": 1,
      "smooth_slide_shape": 1,
      "pulse_width": 0.5,
      "amp_max_slide": 0,
      "phase_offset": 0,
      "pan_min_slide_curve": 0,
      "smooth_down_slide": 0,
      "phase_slide": 0,
      "prob_pos": 0,
      "pre_amp": 1,
      "pan_min": -1,
      "smooth_down_slide_curve": 0,
      "pan_min_slide_shape": 1,
      "amp_min_slide": 0,
      "smooth_up_slide": 0,
      "smooth_slide": 0,
      "smooth_slide_curve": 0,
      "smooth_down": 0,
      "phase_slide_curve": 0,
      "smooth_up": 0,
      "pan_max_slide_curve": 0,
      "smooth_up_slide_shape": 1,
      "seed": 0,
      "pre_mix_slide": 0,
      "pulse_width_slide_curve": 0,
      "amp_slide": 0,
      "mix": 1
    },
    "hiden": true
  },
  "FXNormHPF": {
    "name": ":nhpf",
    "inherit_arg": true,
    "inherit_base": "FXHPF",
    "summary": "Normalised High Pass Filter",
    "opts": {
      "pre_amp_slide_curve": 0,
      "mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_mix": 1,
      "mix_slide": 0,
      "pre_amp": 1,
      "cutoff_slide_curve": 0,
      "cutoff": 100,
      "pre_amp_slide": 0,
      "mix": 1,
      "cutoff_slide_shape": 1,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "mix_slide_curve": 0,
      "pre_mix_slide": 0,
      "amp_slide": 0,
      "amp": 1,
      "cutoff_slide": 0,
      "pre_mix_slide_shape": 1,
      "pre_amp_slide_shape": 1
    },
    "hiden": true
  },
  "FXNBPF": {
    "name": ":nbpf",
    "inherit_arg": true,
    "inherit_base": "FXBPF",
    "summary": "Normalised Band Pass Filter",
    "opts": {
      "centre": 100,
      "pre_amp_slide_curve": 0,
      "mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_mix": 1,
      "res": 0.6,
      "centre_slide_shape": 1,
      "mix_slide": 0,
      "pre_amp": 1,
      "res_slide_curve": 0,
      "pre_amp_slide": 0,
      "res_slide": 0,
      "mix": 1,
      "centre_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "mix_slide_curve": 0,
      "pre_mix_slide": 0,
      "res_slide_shape": 1,
      "amp_slide": 0,
      "amp": 1,
      "pre_mix_slide_shape": 1,
      "centre_slide_curve": 0,
      "pre_amp_slide_shape": 1
    },
    "hiden": true
  },
  "FXGVerb": {
    "name": ":gverb",
    "inherit_arg": true,
    "inherit_base": "FXInfo",
    "summary": "GVerb",
    "opts": {
      "dry_slide_curve": 0,
      "amp_slide_shape": 1,
      "mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_mix": 1,
      "tail_level": 0.5,
      "dry": 1,
      "mix_slide": 0,
      "dry_slide_shape": 1,
      "spread_slide": 0,
      "damp": 0.5,
      "spread_slide_shape": 1,
      "spread_slide_curve": 0,
      "pre_damp_slide_curve": 0,
      "dry_slide": 0,
      "pre_amp": 1,
      "pre_damp": 0.5,
      "release": 3,
      "pre_amp_slide": 0,
      "damp_slide": 0,
      "mix": 1,
      "damp_slide_curve": 0,
      "ref_level": 0.7,
      "room": 10,
      "damp_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "amp_slide_curve": 0,
      "mix_slide_curve": 0,
      "pre_damp_slide": 0,
      "pre_mix_slide": 0,
      "amp_slide": 0,
      "amp": 1,
      "spread": 0.5,
      "pre_damp_slide_shape": 1,
      "pre_mix_slide_shape": 1,
      "pre_amp_slide_shape": 1
    },
    "hiden": false
  },
  "FXReverb": {
    "name": ":reverb",
    "inherit_arg": true,
    "inherit_base": "FXInfo",
    "summary": "Reverb",
    "opts": {
      "amp_slide_shape": 1,
      "mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_mix": 1,
      "mix_slide": 0,
      "room_slide": 0,
      "room_slide_curve": 0,
      "damp": 0.5,
      "room_slide_shape": 1,
      "pre_amp": 1,
      "pre_amp_slide": 0,
      "damp_slide": 0,
      "mix": 0.4,
      "damp_slide_curve": 0,
      "room": 0.6,
      "pre_amp_slide_curve": 0,
      "amp_slide_curve": 0,
      "mix_slide_curve": 0,
      "pre_mix_slide": 0,
      "amp_slide": 0,
      "amp": 1,
      "damp_slide_shape": 1,
      "pre_mix_slide_shape": 1,
      "pre_amp_slide_shape": 1
    },
    "hiden": false
  },
  "FXNRBPF": {
    "name": ":nrbpf",
    "inherit_arg": true,
    "inherit_base": "FXRBPF",
    "summary": "Normalised Resonant Band Pass Filter",
    "opts": {
      "centre": 100,
      "amp_slide_shape": 1,
      "mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_mix": 1,
      "res": 0.5,
      "centre_slide_shape": 1,
      "mix_slide": 0,
      "pre_amp": 1,
      "res_slide_curve": 0,
      "pre_amp_slide": 0,
      "res_slide": 0,
      "mix": 1,
      "centre_slide": 0,
      "pre_amp_slide_curve": 0,
      "amp_slide_curve": 0,
      "mix_slide_curve": 0,
      "pre_mix_slide": 0,
      "res_slide_shape": 1,
      "amp_slide": 0,
      "amp": 1,
      "pre_mix_slide_shape": 1,
      "centre_slide_curve": 0,
      "pre_amp_slide_shape": 1
    },
    "hiden": true
  },
  "FXDistortion": {
    "name": ":distortion",
    "inherit_arg": true,
    "inherit_base": "FXInfo",
    "summary": "Distortion",
    "opts": {
      "amp_slide_shape": 1,
      "distort_slide_shape": 1,
      "mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_mix": 1,
      "mix_slide": 0,
      "pre_amp": 1,
      "distort_slide": 0,
      "pre_amp_slide": 0,
      "mix": 1,
      "distort": 0.5,
      "pre_amp_slide_curve": 0,
      "amp_slide_curve": 0,
      "mix_slide_curve": 0,
      "pre_mix_slide": 0,
      "amp_slide": 0,
      "amp": 1,
      "distort_slide_curve": 0,
      "pre_mix_slide_shape": 1,
      "pre_amp_slide_shape": 1
    },
    "hiden": false
  },
  "FXHPF": {
    "name": ":hpf",
    "inherit_arg": true,
    "inherit_base": "FXInfo",
    "summary": "High Pass Filter",
    "opts": {
      "amp_slide_shape": 1,
      "mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_mix": 1,
      "mix_slide": 0,
      "cutoff_slide_curve": 0,
      "pre_amp": 1,
      "cutoff": 100,
      "pre_amp_slide": 0,
      "mix": 1,
      "cutoff_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "amp_slide_curve": 0,
      "mix_slide_curve": 0,
      "pre_mix_slide": 0,
      "amp_slide": 0,
      "amp": 1,
      "cutoff_slide": 0,
      "pre_mix_slide_shape": 1,
      "pre_amp_slide_shape": 1
    },
    "hiden": false
  },
  "FXNormaliser": {
    "name": ":normaliser",
    "inherit_arg": true,
    "inherit_base": "FXInfo",
    "summary": "Normaliser",
    "opts": {
      "amp_slide_shape": 1,
      "mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_mix": 1,
      "mix_slide": 0,
      "level_slide_curve": 0,
      "pre_amp": 1,
      "pre_amp_slide": 0,
      "level_slide_shape": 1,
      "mix": 1,
      "pre_amp_slide_curve": 0,
      "amp_slide_curve": 0,
      "mix_slide_curve": 0,
      "level": 1,
      "pre_mix_slide": 0,
      "level_slide": 0,
      "amp_slide": 0,
      "amp": 1,
      "pre_mix_slide_shape": 1,
      "pre_amp_slide_shape": 1
    },
    "hiden": false
  },
  "FXNormRHPF": {
    "name": ":nrhpf",
    "inherit_arg": true,
    "inherit_base": "FXRHPF",
    "summary": "Normalised Resonant High Pass Filter",
    "opts": {
      "amp_slide_shape": 1,
      "mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_mix": 1,
      "res": 0.5,
      "mix_slide": 0,
      "cutoff_slide_curve": 0,
      "pre_amp": 1,
      "cutoff": 100,
      "res_slide_curve": 0,
      "pre_amp_slide": 0,
      "res_slide": 0,
      "mix": 1,
      "cutoff_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "amp_slide_curve": 0,
      "mix_slide_curve": 0,
      "pre_mix_slide": 0,
      "res_slide_shape": 1,
      "amp_slide": 0,
      "amp": 1,
      "cutoff_slide": 0,
      "pre_mix_slide_shape": 1,
      "pre_amp_slide_shape": 1
    },
    "hiden": true
  },
  "FXIXITechno": {
    "name": ":ixi_techno",
    "inherit_arg": true,
    "inherit_base": "FXInfo",
    "summary": "Techno from IXI Lang",
    "opts": {
      "amp_slide_shape": 1,
      "mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_mix": 1,
      "res": 0.8,
      "mix_slide": 0,
      "cutoff_max_slide_curve": 0,
      "phase_slide": 0,
      "cutoff_max_slide_shape": 1,
      "pre_amp": 1,
      "cutoff_min_slide": 0,
      "res_slide_curve": 0,
      "cutoff_max": 120,
      "phase": 4,
      "pre_amp_slide": 0,
      "res_slide": 0,
      "cutoff_min_slide_shape": 1,
      "cutoff_min": 60,
      "mix": 1,
      "phase_offset": 0,
      "cutoff_min_slide_curve": 0,
      "cutoff_max_slide": 0,
      "phase_slide_curve": 0,
      "pre_amp_slide_curve": 0,
      "amp_slide_curve": 0,
      "mix_slide_curve": 0,
      "pre_mix_slide": 0,
      "phase_slide_shape": 1,
      "res_slide_shape": 1,
      "amp_slide": 0,
      "amp": 1,
      "pre_mix_slide_shape": 1,
      "pre_amp_slide_shape": 1
    },
    "hiden": false
  },
  "FXRBPF": {
    "name": ":rbpf",
    "inherit_arg": true,
    "inherit_base": "FXBPF",
    "summary": "Resonant Band Pass Filter",
    "opts": {
      "centre": 100,
      "pre_amp_slide_curve": 0,
      "mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_mix": 1,
      "res": 0.5,
      "centre_slide_shape": 1,
      "mix_slide": 0,
      "pre_amp": 1,
      "res_slide_curve": 0,
      "pre_amp_slide": 0,
      "res_slide": 0,
      "mix": 1,
      "centre_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "mix_slide_curve": 0,
      "pre_mix_slide": 0,
      "res_slide_shape": 1,
      "amp_slide": 0,
      "amp": 1,
      "pre_mix_slide_shape": 1,
      "centre_slide_curve": 0,
      "pre_amp_slide_shape": 1
    },
    "hiden": true
  },
  "FXWhammy": {
    "name": ":whammy",
    "inherit_arg": true,
    "inherit_base": "FXInfo",
    "summary": "Whammy",
    "opts": {
      "amp_slide_shape": 1,
      "mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_mix": 1,
      "mix_slide": 0,
      "grainsize": 0.075,
      "transpose_slide_curve": 0,
      "pre_amp": 1,
      "transpose_slide": 0,
      "pre_amp_slide": 0,
      "mix": 1,
      "deltime": 0.05,
      "max_delay_time": 1,
      "pre_amp_slide_curve": 0,
      "amp_slide_curve": 0,
      "mix_slide_curve": 0,
      "pre_mix_slide": 0,
      "amp_slide": 0,
      "amp": 1,
      "transpose": 12,
      "transpose_slide_shape": 1,
      "pre_mix_slide_shape": 1,
      "pre_amp_slide_shape": 1
    },
    "hiden": false
  },
  "FXMono": {
    "name": ":mono",
    "inherit_arg": true,
    "inherit_base": "FXInfo",
    "summary": "Mono",
    "opts": {
      "amp_slide_shape": 1,
      "mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_mix": 1,
      "mix_slide": 0,
      "pan": 0,
      "pan_slide_curve": 0,
      "pre_amp": 1,
      "pre_amp_slide": 0,
      "mix": 1,
      "pan_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "amp_slide_curve": 0,
      "mix_slide_curve": 0,
      "pre_mix_slide": 0,
      "amp_slide": 0,
      "amp": 1,
      "pan_slide": 0,
      "pre_mix_slide_shape": 1,
      "pre_amp_slide_shape": 1
    },
    "hiden": false
  },
  "FXLevel": {
    "name": ":level",
    "inherit_arg": false,
    "inherit_base": "FXInfo",
    "summary": "Level Amplifier",
    "opts": {
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "amp_slide": 0,
      "amp": 1
    },
    "hiden": false
  },
  "FXLPF": {
    "name": ":lpf",
    "inherit_arg": true,
    "inherit_base": "FXInfo",
    "summary": "Low Pass Filter",
    "opts": {
      "amp_slide_shape": 1,
      "mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_mix": 1,
      "mix_slide": 0,
      "cutoff_slide_curve": 0,
      "pre_amp": 1,
      "cutoff": 100,
      "pre_amp_slide": 0,
      "mix": 1,
      "cutoff_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "amp_slide_curve": 0,
      "mix_slide_curve": 0,
      "pre_mix_slide": 0,
      "amp_slide": 0,
      "amp": 1,
      "cutoff_slide": 0,
      "pre_mix_slide_shape": 1,
      "pre_amp_slide_shape": 1
    },
    "hiden": false
  },
  "FXSlicer": {
    "name": ":slicer",
    "inherit_arg": true,
    "inherit_base": "FXInfo",
    "summary": "Slicer",
    "opts": {
      "amp_min_slide_curve": 0,
      "amp_min_slide_shape": 1,
      "smooth_up": 0,
      "smooth_up_slide_curve": 0,
      "mix_slide_shape": 1,
      "pre_mix": 1,
      "mix_slide": 0,
      "pulse_width_slide": 0,
      "prob_pos_slide": 0,
      "prob_pos_slide_shape": 1,
      "probability_slide": 0,
      "wave": 1,
      "amp_min": 0,
      "probability_slide_shape": 1,
      "phase": 0.25,
      "pre_amp_slide": 0,
      "pre_mix_slide": 0,
      "amp_max": 1,
      "pre_amp_slide_curve": 0,
      "phase_offset": 0,
      "amp_max_slide_curve": 0,
      "probability_slide_curve": 0,
      "amp_slide_curve": 0,
      "mix_slide_curve": 0,
      "amp_max_slide_shape": 1,
      "probability": 0,
      "phase_slide_shape": 1,
      "seed": 0,
      "smooth_down_slide_shape": 1,
      "prob_pos_slide_curve": 0,
      "amp": 1,
      "pre_mix_slide_shape": 1,
      "pre_amp_slide_shape": 1,
      "pulse_width_slide_shape": 1,
      "smooth_slide_shape": 1,
      "pulse_width": 0.5,
      "amp_max_slide": 0,
      "pre_mix_slide_curve": 0,
      "smooth_down_slide": 0,
      "phase_slide": 0,
      "prob_pos": 0,
      "pre_amp": 1,
      "smooth_down_slide_curve": 0,
      "amp_min_slide": 0,
      "smooth_up_slide": 0,
      "smooth_slide": 0,
      "smooth_slide_curve": 0,
      "smooth_down": 0,
      "phase_slide_curve": 0,
      "amp_slide_shape": 1,
      "smooth_up_slide_shape": 1,
      "invert_wave": 0,
      "smooth": 0,
      "pulse_width_slide_curve": 0,
      "amp_slide": 0,
      "mix": 1
    },
    "hiden": false
  },
  "FXBandEQ": {
    "name": ":band_eq",
    "inherit_arg": true,
    "inherit_base": "FXInfo",
    "summary": "Band EQ Filter",
    "opts": {
      "freq_slide": 0,
      "amp_slide_shape": 1,
      "mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_mix": 1,
      "res": 0.6,
      "mix_slide": 0,
      "db_slide_shape": 1,
      "freq_slide_curve": 0,
      "pre_amp": 1,
      "res_slide_curve": 0,
      "pre_amp_slide": 0,
      "res_slide": 0,
      "mix": 1,
      "freq": 100,
      "res_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "amp_slide_curve": 0,
      "mix_slide_curve": 0,
      "db": 0.6,
      "pre_mix_slide": 0,
      "db_slide_curve": 0,
      "freq_slide_shape": 1,
      "amp_slide": 0,
      "amp": 1,
      "db_slide": 0,
      "pre_mix_slide_shape": 1,
      "pre_amp_slide_shape": 1
    },
    "hiden": false
  },
  "FXTanh": {
    "name": ":tanh",
    "inherit_arg": true,
    "inherit_base": "FXInfo",
    "summary": "Hyperbolic Tangent",
    "opts": {
      "amp_slide_shape": 1,
      "mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_mix": 1,
      "mix_slide": 0,
      "krunch_slide_curve": 0,
      "pre_amp": 1,
      "krunch": 5,
      "pre_amp_slide": 0,
      "mix": 1,
      "pre_amp_slide_curve": 0,
      "amp_slide_curve": 0,
      "mix_slide_curve": 0,
      "krunch_slide_shape": 1,
      "pre_mix_slide": 0,
      "amp_slide": 0,
      "amp": 1,
      "krunch_slide": 0,
      "pre_mix_slide_shape": 1,
      "pre_amp_slide_shape": 1
    },
    "hiden": false
  },
  "FXVowel": {
    "name": ":vowel",
    "inherit_arg": true,
    "inherit_base": "FXInfo",
    "summary": "Vowel",
    "opts": {
      "amp_slide_shape": 1,
      "mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_mix": 1,
      "vowel_sound": 1,
      "mix_slide": 0,
      "voice": 0,
      "pre_amp": 1,
      "pre_amp_slide": 0,
      "mix": 1,
      "pre_amp_slide_curve": 0,
      "amp_slide_curve": 0,
      "mix_slide_curve": 0,
      "pre_mix_slide": 0,
      "amp_slide": 0,
      "amp": 1,
      "pre_mix_slide_shape": 1,
      "pre_amp_slide_shape": 1
    },
    "hiden": false
  },
  "FXNormLPF": {
    "name": ":nlpf",
    "inherit_arg": true,
    "inherit_base": "FXLPF",
    "summary": "Normalised Low Pass Filter.",
    "opts": {
      "pre_amp_slide_curve": 0,
      "mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_mix": 1,
      "mix_slide": 0,
      "pre_amp": 1,
      "cutoff_slide_curve": 0,
      "cutoff": 100,
      "pre_amp_slide": 0,
      "mix": 1,
      "cutoff_slide_shape": 1,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "mix_slide_curve": 0,
      "pre_mix_slide": 0,
      "amp_slide": 0,
      "amp": 1,
      "cutoff_slide": 0,
      "pre_mix_slide_shape": 1,
      "pre_amp_slide_shape": 1
    },
    "hiden": true
  },
  "FXKrush": {
    "name": ":krush",
    "inherit_arg": true,
    "inherit_base": "FXInfo",
    "summary": "krush",
    "opts": {
      "amp_slide_shape": 1,
      "mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_mix": 1,
      "res": 0,
      "mix_slide": 0,
      "gain_slide_shape": 1,
      "cutoff_slide_shape": 1,
      "gain_slide": 0,
      "pre_amp": 1,
      "res_slide_curve": 0,
      "cutoff": 100,
      "pre_amp_slide": 0,
      "res_slide": 0,
      "mix": 1,
      "cutoff_slide_curve": 0,
      "pre_amp_slide_curve": 0,
      "amp_slide_curve": 0,
      "mix_slide_curve": 0,
      "pre_mix_slide": 0,
      "res_slide_shape": 1,
      "amp_slide": 0,
      "amp": 1,
      "gain_slide__curve": 0,
      "cutoff_slide": 0,
      "pre_mix_slide_shape": 1,
      "gain": 5,
      "pre_amp_slide_shape": 1
    },
    "hiden": false
  },
  "FXFlanger": {
    "name": ":flanger",
    "inherit_arg": true,
    "inherit_base": "FXInfo",
    "summary": "Flanger",
    "opts": {
      "invert_flange": 0,
      "amp_slide_shape": 1,
      "depth_slide_curve": 0,
      "mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_mix": 1,
      "mix_slide": 0,
      "depth_slide_shape": 1,
      "phase_slide": 0,
      "max_delay": 20,
      "wave": 4,
      "decay": 2,
      "delay_slide_shape": 1,
      "pre_amp": 1,
      "depth": 5,
      "decay_slide_shape": 1,
      "phase": 4,
      "pre_amp_slide": 0,
      "decay_slide_curve": 0,
      "stereo_invert_wave": 0,
      "feedback_slide_shape": 1,
      "mix": 1,
      "delay_slide_curve": 0,
      "delay": 5,
      "phase_offset": 0,
      "decay_slide": 0,
      "feedback_slide_curve": 0,
      "phase_slide_curve": 0,
      "pre_amp_slide_curve": 0,
      "amp_slide_curve": 0,
      "mix_slide_curve": 0,
      "invert_wave": 0,
      "pre_mix_slide": 0,
      "phase_slide_shape": 1,
      "feedback": 0,
      "amp_slide": 0,
      "amp": 1,
      "delay_slide": 0,
      "pre_mix_slide_shape": 1,
      "depth_slide": 0,
      "feedback_slide": 0,
      "pre_amp_slide_shape": 1
    },
    "hiden": false
  },
  "FXNormRLPF": {
    "name": ":nrlpf",
    "inherit_arg": true,
    "inherit_base": "FXRLPF",
    "summary": "Normalised Resonant Low Pass Filter",
    "opts": {
      "amp_slide_shape": 1,
      "mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_mix": 1,
      "res": 0.5,
      "mix_slide": 0,
      "cutoff_slide_curve": 0,
      "pre_amp": 1,
      "cutoff": 100,
      "res_slide_curve": 0,
      "pre_amp_slide": 0,
      "res_slide": 0,
      "mix": 1,
      "cutoff_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "amp_slide_curve": 0,
      "mix_slide_curve": 0,
      "pre_mix_slide": 0,
      "res_slide_shape": 1,
      "amp_slide": 0,
      "amp": 1,
      "cutoff_slide": 0,
      "pre_mix_slide_shape": 1,
      "pre_amp_slide_shape": 1
    },
    "hiden": true
  },
  "FXRLPF": {
    "name": ":rlpf",
    "inherit_arg": true,
    "inherit_base": "FXLPF",
    "summary": "Resonant Low Pass Filter",
    "opts": {
      "pre_amp_slide_curve": 0,
      "mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_mix": 1,
      "res": 0.5,
      "mix_slide": 0,
      "pre_amp": 1,
      "cutoff_slide_curve": 0,
      "cutoff": 100,
      "res_slide_curve": 0,
      "pre_amp_slide": 0,
      "res_slide": 0,
      "mix": 1,
      "cutoff_slide_shape": 1,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "mix_slide_curve": 0,
      "pre_mix_slide": 0,
      "res_slide_shape": 1,
      "amp_slide": 0,
      "amp": 1,
      "cutoff_slide": 0,
      "pre_mix_slide_shape": 1,
      "pre_amp_slide_shape": 1
    },
    "hiden": true
  },
  "FXPitchShift": {
    "name": ":pitch_shift",
    "inherit_arg": true,
    "inherit_base": "FXInfo",
    "summary": "Pitch shift",
    "opts": {
      "amp_slide_shape": 1,
      "mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_mix": 1,
      "pitch_dis_slide_shape": 1,
      "mix_slide": 0,
      "pitch_slide_curve": 0,
      "time_dis_slide_curve": 0,
      "pitch_dis_slide_curve": 0,
      "pre_amp": 1,
      "pitch_slide": 0,
      "pitch": 0,
      "pre_amp_slide": 0,
      "mix": 1,
      "window_size_slide_shape": 1,
      "time_dis_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "amp_slide_curve": 0,
      "mix_slide_curve": 0,
      "pitch_dis_slide": 0,
      "pre_mix_slide": 0,
      "time_dis_slide": 0,
      "window_size_slide_curve": 0,
      "pitch_dis": 0.0,
      "window_size_slide": 0,
      "amp_slide": 0,
      "amp": 1,
      "time_dis": 0.0,
      "window_size": 0.2,
      "pitch_slide_shape": 1,
      "pre_mix_slide_shape": 1,
      "pre_amp_slide_shape": 1
    },
    "hiden": false
  },
  "FXBPF": {
    "name": ":bpf",
    "inherit_arg": true,
    "inherit_base": "FXInfo",
    "summary": "Band Pass Filter",
    "opts": {
      "centre": 100,
      "amp_slide_shape": 1,
      "mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_mix": 1,
      "res": 0.6,
      "centre_slide_shape": 1,
      "mix_slide": 0,
      "pre_amp": 1,
      "res_slide_curve": 0,
      "pre_amp_slide": 0,
      "res_slide": 0,
      "mix": 1,
      "centre_slide": 0,
      "pre_amp_slide_curve": 0,
      "amp_slide_curve": 0,
      "mix_slide_curve": 0,
      "pre_mix_slide": 0,
      "res_slide_shape": 1,
      "amp_slide": 0,
      "amp": 1,
      "pre_mix_slide_shape": 1,
      "centre_slide_curve": 0,
      "pre_amp_slide_shape": 1
    },
    "hiden": false
  },
  "FXCompressor": {
    "name": ":compressor",
    "inherit_arg": true,
    "inherit_base": "FXInfo",
    "summary": "Compressor",
    "opts": {
      "threshold_slide_curve": 0,
      "amp_slide_shape": 1,
      "mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_mix": 1,
      "clamp_time_slide_curve": 0,
      "mix_slide": 0,
      "clamp_time": 0.01,
      "relax_time_slide": 0,
      "slope_above_slide_shape": 1,
      "clamp_time_slide_shape": 1,
      "relax_time_slide_curve": 0,
      "slope_above_slide": 0,
      "slope_below_slide_shape": 1,
      "pre_amp": 1,
      "relax_time": 0.01,
      "slope_above": 0.5,
      "pre_amp_slide": 0,
      "relax_time_slide_shape": 1,
      "threshold": 0.2,
      "slope_above_slide_curve": 0,
      "mix": 1,
      "slope_below": 1,
      "pre_amp_slide_curve": 0,
      "amp_slide_curve": 0,
      "mix_slide_curve": 0,
      "threshold_slide_shape": 1,
      "pre_mix_slide": 0,
      "slope_below_slide": 0,
      "threshold_slide": 0,
      "clamp_time_slide": 0,
      "amp_slide": 0,
      "amp": 1,
      "slope_below_slide_curve": 0,
      "pre_mix_slide_shape": 1,
      "pre_amp_slide_shape": 1
    },
    "hiden": false
  }
}

samples = {
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
  "Vinyl sounds": [
    ":vinyl_backspin",
    ":vinyl_rewind",
    ":vinyl_scratch",
    ":vinyl_hiss"
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
  "Percussive Sounds": [
    ":perc_bell",
    ":perc_snap",
    ":perc_snap2",
    ":perc_swash",
    ":perc_till"
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
  "Miscellaneous Sounds": [
    ":misc_burp",
    ":misc_crow",
    ":misc_cineboom"
  ],
  "Sounds featuring guitars": [
    ":guit_harmonics",
    ":guit_e_fifths",
    ":guit_e_slide",
    ":guit_em9"
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
  ]
}

synth_args_types_conversion = {}

synth_opts_types_conversion = {}

