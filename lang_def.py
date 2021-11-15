null = None; true = True; false = False;
#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/

lang_core = {
  "set": {
    "signature": {
      "k": null,
      "val": null
    },
    "name": "set",
    "introduced": "3,0,0",
    "summary": "Store information in the Time State",
    "args": [
      {
        "time_state_key": ":default"
      },
      {
        "value": ":anything"
      }
    ],
    "accepts_block": false,
    "hidden": false
  },
  "cue": {
    "signature": {
      "k": null,
      "*opts": null
    },
    "name": "cue",
    "introduced": "2,0,0",
    "summary": "Cue other threads",
    "args": [
      {
        "cue_id": ":symbol"
      }
    ],
    "opts": {
      "your_key": ":bar",
      "another_key": "",
      "key": "foo: 64"
    },
    "accepts_block": false,
    "hidden": false
  },
  "__osc_match": {
    "signature": {
      "matcher_path": null,
      "osc_path": null
    },
    "hidden": false
  },
  "get_event": {
    "signature": {
      "*args": null
    },
    "hidden": false
  },
  "get": {
    "signature": {
      "*args": null
    },
    "name": "get",
    "introduced": "3,0,0",
    "summary": "Get information from the Time State",
    "args": [
      {
        "time_state_key": ":default"
      }
    ],
    "accepts_block": false,
    "hidden": false
  },
  "current_beat": {
    "hidden": false
  },
  "with_swing": {
    "signature": {
      "*args": null,
      "&blk": null
    },
    "name": "with_swing",
    "introduced": "3,0,0",
    "summary": "Add swing to successive calls to do/end block",
    "args": [
      {
        "shift": ":beats"
      }
    ],
    "returns": null,
    "opts": {},
    "accepts_block": false,
    "hidden": false,
    "alt_args": [
      {
        "pulse": ":number"
      },
      {
        "tick": ":symbol"
      },
      {
        "offset": ":number"
      }
    ]
  },
  "run_file": {
    "signature": {
      "path": null
    },
    "name": "run_file",
    "introduced": "2,11,0",
    "summary": "Evaluate the contents of the file as a new Run",
    "args": [
      {
        "filename": ":path"
      }
    ],
    "returns": null,
    "accepts_block": false,
    "hidden": false
  },
  "run_code": {
    "signature": {
      "code": null
    },
    "name": "run_code",
    "introduced": "2,11,0",
    "summary": "Evaluate the code passed as a String as a new Run",
    "args": [
      {
        "code": ":string"
      }
    ],
    "returns": null,
    "accepts_block": false,
    "hidden": false
  },
  "eval_file": {
    "signature": {
      "path": null
    },
    "name": "eval_file",
    "introduced": "3,2,0",
    "summary": "Evaluate the contents of the file inline in the current thread like a function.",
    "args": [
      {
        "filename": ":path"
      }
    ],
    "returns": null,
    "accepts_block": false,
    "hidden": false
  },
  "use_osc_logging": {
    "signature": {
      "v": null,
      "&block": null
    },
    "name": "use_osc_logging",
    "introduced": "3,0,0",
    "summary": "Enable and disable OSC logging",
    "args": [
      {
        "true_or_false": ":boolean"
      }
    ],
    "accepts_block": false,
    "hidden": false
  },
  "with_osc_logging": {
    "signature": {
      "v": null,
      "&block": null
    },
    "name": "with_osc_logging",
    "introduced": "3,0,0",
    "summary": "Block-level enable and disable OSC logging",
    "args": [
      {
        "true_or_false": ":boolean"
      }
    ],
    "accepts_block": true,
    "requires_block": true,
    "hidden": false
  },
  "use_osc": {
    "signature": {
      "host": null,
      "port": 4560
    },
    "name": "use_osc",
    "introduced": "3,0,0",
    "summary": "Set the default hostname and port number for outgoing OSC messages.",
    "args": [
      {
        "hostname": ":string"
      },
      {
        "port": ":number"
      }
    ],
    "returns": null,
    "accepts_block": false,
    "hidden": true
  },
  "with_osc": {
    "signature": {
      "host": null,
      "port": 4560,
      "&block": null
    },
    "name": "with_osc",
    "introduced": "3,0,0",
    "summary": "Block-level setting for the default hostname and port number of outgoing OSC messages.",
    "args": [
      {
        "hostname": ":string"
      },
      {
        "port": ":number"
      }
    ],
    "returns": null,
    "accepts_block": true,
    "hidden": false
  },
  "__osc_send_api": {
    "signature": {
      "path": null,
      "*args": null
    },
    "hidden": false
  },
  "__osc_send": {
    "signature": {
      "host": null,
      "port": null,
      "path": null,
      "*args": null
    },
    "hidden": false
  },
  "osc_send": {
    "signature": {
      "host": null,
      "port": null,
      "path": null,
      "*args": null
    },
    "name": "osc_send",
    "introduced": "3,0,0",
    "summary": "Send an OSC message to a specific host and port",
    "args": [
      {
        "hostname": ":string"
      },
      {
        "port": ":number"
      },
      {
        "path": ":osc_path"
      },
      {
        "args": ":list"
      }
    ],
    "returns": null,
    "accepts_block": true,
    "hidden": true
  },
  "osc": {
    "signature": {
      "path": null,
      "*args": null
    },
    "name": "osc",
    "introduced": "3,0,0",
    "summary": "Send an OSC message (Open Sound Control)",
    "args": [
      {
        "path": ":arguments"
      }
    ],
    "returns": null,
    "accepts_block": false,
    "hidden": true
  },
  "reset": {
    "name": "reset",
    "introduced": "2,11,0",
    "summary": "Reset all thread locals",
    "args": [],
    "returns": null,
    "accepts_block": false,
    "hidden": false
  },
  "clear": {
    "name": "clear",
    "introduced": "2,11,0",
    "summary": "Clear all thread locals to defaults",
    "args": [],
    "returns": null,
    "accepts_block": false,
    "hidden": false
  },
  "time_warp": {
    "signature": {
      "times": 0,
      "params": "nil",
      "&block": null
    },
    "name": "time_warp",
    "introduced": "2,11,0",
    "summary": "Shift time forwards or backwards for the given block",
    "args": [
      {
        "delta_time": ":number"
      }
    ],
    "returns": null,
    "accepts_block": true,
    "hidden": false
  },
  "tick_set": {
    "signature": {
      "*args": null
    },
    "name": "tick_set",
    "introduced": "2,6,0",
    "summary": "Set tick to a specific value",
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
    ],
    "returns": ":number",
    "accepts_block": false,
    "hidden": false
  },
  "tick_reset": {
    "signature": {
      "*args": null
    },
    "name": "tick_reset",
    "introduced": "2,6,0",
    "summary": "Reset tick to 0",
    "alt_args": [
      {
        "key": ":symbol"
      }
    ],
    "returns": ":number",
    "accepts_block": false,
    "hidden": false
  },
  "tick_reset_all": {
    "name": "tick_reset_all",
    "introduced": "2,6,0",
    "summary": "Reset all ticks",
    "returns": null,
    "accepts_block": false,
    "hidden": false
  },
  "tick": {
    "signature": {
      "*args": null
    },
    "name": "tick",
    "introduced": "2,6,0",
    "summary": "Increment a tick and return value",
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
    ],
    "returns": ":number",
    "opts": {
      "step": 1,
      "offset": 0
    },
    "accepts_block": false,
    "hidden": false,
    "inline": true
  },
  "look": {
    "signature": {
      "*args": null
    },
    "name": "look",
    "introduced": "2,6,0",
    "summary": "Obtain value of a tick",
    "alt_args": [
      {
        "list": ":array"
      },
      {
        "key": ":symbol"
      }
    ],
    "returns": ":number",
    "opts": {
      "offset": 0
    },
    "accepts_block": false,
    "hidden": false,
    "inline": true
  },
  "stop": {
    "name": "stop",
    "introduced": "2,5,0",
    "summary": "Stop current thread or run",
    "returns": null,
    "accepts_block": false,
    "hidden": false,
    "args": [
      {
        "signal": ":boolean"
      }
    ],
    "alt_args": []
  },
  "on": {
    "signature": {
      "condition": null,
      "&blk": null
    },
    "name": "on",
    "introduced": "2,10,0",
    "summary": "Optionally evaluate block",
    "args": [
      {
        "condition": ":truthy"
      }
    ],
    "returns": null,
    "accepts_block": true,
    "hidden": false,
    "requires_block": true
  },
  "bools": {
    "signature": {
      "*args": null
    },
    "name": "bools",
    "introduced": "2,2,0",
    "summary": "Create a ring of boolean values",
    "args": [
      {
        "list": ":array"
      }
    ],
    "returns": ":ring",
    "accepts_block": false,
    "hidden": false,
    "inline": true
  },
  "stretch": {
    "signature": {
      "*args": null
    },
    "name": "stretch",
    "introduced": "2,6,0",
    "summary": "Stretch a sequence of values",
    "args": [
      {
        "count": ":int"
      }
    ],
    "returns": ":ring",
    "accepts_block": false,
    "hidden": false,
    "inline": true,
    "alt_args": [
      {
        "list": ":array"
      }
    ]
  },
  "knit": {
    "signature": {
      "*args": null
    },
    "name": "knit",
    "introduced": "2,2,0",
    "summary": "Knit a sequence of repeated values",
    "args": [
      {
        "value": ":anything"
      }
    ],
    "returns": ":ring",
    "accepts_block": false,
    "hidden": false,
    "inline": true,
    "alt_args": [
      {
        "count": ":number"
      }
    ]
  },
  "redistribute": {
    "signature": {
      "v1": null,
      "v2": null
    },
    "hidden": false
  },
  "spread": {
    "signature": {
      "num_accents": null,
      "size": null,
      "*args": null
    },
    "name": "spread",
    "introduced": "2,4,0",
    "summary": "Euclidean distribution for beats",
    "args": [
      {
        "num_accents": ":number"
      },
      {
        "size": ":number"
      }
    ],
    "returns": ":ring",
    "opts": {
      "rotate": false
    },
    "accepts_block": false,
    "hidden": false,
    "inline": true
  },
  "range": {
    "signature": {
      "start": null,
      "finish": null,
      "*args": null
    },
    "name": "range",
    "introduced": "2,2,0",
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
    "returns": ":ring",
    "opts": {
      "step": 1,
      "inclusive": false
    },
    "accepts_block": false,
    "memoize": true,
    "hidden": false,
    "inline": true
  },
  "line": {
    "signature": {
      "start": null,
      "finish": null,
      "*args": null
    },
    "name": "line",
    "introduced": "2,5,0",
    "summary": "Create a ring buffer representing a straight line",
    "args": [
      {
        "start": ":number"
      },
      {
        "finish": ":number"
      }
    ],
    "returns": ":ring",
    "opts": {
      "steps": 1,
      "inclusive": false
    },
    "accepts_block": false,
    "memoize": true,
    "hidden": false,
    "inline": true
  },
  "halves": {
    "signature": {
      "start": null,
      "num_halves": 1
    },
    "name": "halves",
    "introduced": "2,10,0",
    "summary": "Create a ring of successive halves",
    "args": [
      {
        "start": ":number"
      },
      {
        "num_halves": ":int"
      }
    ],
    "returns": ":ring",
    "accepts_block": false,
    "memoize": true,
    "hidden": false,
    "inline": true
  },
  "doubles": {
    "signature": {
      "start": null,
      "num_doubles": 1
    },
    "name": "doubles",
    "introduced": "2,10,0",
    "summary": "Create a ring of successive doubles",
    "args": [
      {
        "start": ":number"
      },
      {
        "num_doubles": ":int"
      }
    ],
    "returns": ":ring",
    "accepts_block": false,
    "memoize": true,
    "hidden": false,
    "inline": true
  },
  "vector": {
    "signature": {
      "*args": null
    },
    "name": "vector",
    "introduced": "2,6,0",
    "summary": "Create a vector",
    "args": [
      {
        "list": ":array"
      }
    ],
    "returns": ":vector",
    "accepts_block": false,
    "hidden": false,
    "inline": true
  },
  "ring": {
    "signature": {
      "*args": null
    },
    "name": "ring",
    "introduced": "2,2,0",
    "summary": "Create a ring buffer",
    "args": [
      {
        "list": ":array"
      }
    ],
    "returns": ":ring",
    "accepts_block": false,
    "hidden": false,
    "inline": true
  },
  "map": {
    "signature": {
      "*args": null
    },
    "name": "map",
    "introduced": "2,11,0",
    "summary": "Create an immutable map",
    "args": [
      {
        "list": ":array"
      }
    ],
    "returns": ":map",
    "accepts_block": false,
    "hidden": false
  },
  "ramp": {
    "signature": {
      "*args": null
    },
    "name": "ramp",
    "introduced": "2,6,0",
    "summary": "Create a ramp vector",
    "args": [
      {
        "list": ":array"
      }
    ],
    "returns": ":ramp",
    "accepts_block": false,
    "hidden": false,
    "inline": true
  },
  "choose": {
    "signature": {
      "args": "nil"
    },
    "name": "choose",
    "introduced": "2,0,0",
    "summary": "Random list selection",
    "args": [],
    "accepts_block": false,
    "opts": {
      "skip": 0
    },
    "hidden": false,
    "inline": true,
    "alt_args": [
      {
        "list": ":array"
      }
    ]
  },
  "inc": {
    "signature": {
      "n": null
    },
    "name": "inc",
    "introduced": "2, 1, 0",
    "summary": "Increment",
    "args": [
      {
        "n": ":number"
      }
    ],
    "opts": {},
    "accepts_block": false,
    "hidden": true
  },
  "dec": {
    "signature": {
      "n": null
    },
    "name": "dec",
    "introduced": "2, 1, 0",
    "summary": "Decrement",
    "args": [
      {
        "n": ":number"
      }
    ],
    "opts": {},
    "accepts_block": false,
    "hidden": true
  },
  "loop": {
    "signature": {
      "&block": null
    },
    "name": "loop",
    "introduced": "2,0,0",
    "summary": "Repeat do/end block forever",
    "args": [],
    "accepts_block": true,
    "requires_block": true,
    "async_block": false,
    "hidden": true
  },
  "live_loop": {
    "signature": {
      "name": "nil",
      "*args": null,
      "&block": null
    },
    "name": "live_loop",
    "introduced": "2,1,0",
    "summary": "A loop for live coding",
    "args": [],
    "opts": {
      "init": "",
      "auto_cue": true,
      "delay": 0,
      "sync": ":foo",
      "sync_bpm": ":foo",
      "seed": 0
    },
    "accepts_block": true,
    "requires_block": true,
    "async_block": true,
    "intro_fn": true,
    "hidden": false,
    "alt_args": [
      {
        "name": ":symbol"
      }
    ]
  },
  "block_duration": {
    "signature": {
      "&block": null
    },
    "name": "block_duration",
    "introduced": "2,9,0",
    "summary": "Return block duration",
    "args": [],
    "accepts_block": true,
    "requires_block": true,
    "async_block": false,
    "hidden": false
  },
  "block_slept": {
    "signature": {
      "&block": null
    },
    "name": "block_slept?",
    "introduced": "2,9,0",
    "summary": "Determine if block contains sleep time",
    "args": [],
    "accepts_block": true,
    "requires_block": true,
    "async_block": false,
    "hidden": false
  },
  "at": {
    "signature": {
      "times": 0,
      "params": "nil",
      "&block": null
    },
    "name": "at",
    "introduced": "2,1,0",
    "summary": "Asynchronous Time. Run a block at the given time(s)",
    "args": [
      {
        "times": ":list"
      },
      {
        "params": ":list"
      }
    ],
    "accepts_block": true,
    "requires_block": true,
    "async_block": true,
    "hidden": false
  },
  "version": {
    "name": "version",
    "introduced": "2,0,0",
    "summary": "Get current version information",
    "accepts_block": false,
    "hidden": true
  },
  "spark_graph": {
    "signature": {
      "*values": null
    },
    "name": "spark_graph",
    "introduced": "2,5,0",
    "summary": "Returns a string representing a list of numeric values as a spark graph/bar chart",
    "accepts_block": false,
    "hidden": true
  },
  "spark": {
    "signature": {
      "*values": null
    },
    "name": "spark",
    "hidden": true,
    "introduced": "2,5,0",
    "summary": "Print a string representing a list of numeric values as a spark graph/bar chart",
    "accepts_block": false
  },
  "defonce": {
    "signature": {
      "name": null,
      "*opts": null,
      "&block": null
    },
    "name": "defonce",
    "introduced": "2,0,0",
    "summary": "Define a named value only once",
    "args": [
      {
        "name": ":symbol"
      }
    ],
    "opts": {
      "override": false
    },
    "accepts_block": true,
    "requires_block": true,
    "hidden": false
  },
  "ndefine": {
    "signature": {
      "name": null,
      "&block": null
    },
    "name": "ndefine",
    "introduced": "2,1,0",
    "summary": "Define a new function",
    "args": [
      {
        "name": ":symbol"
      }
    ],
    "accepts_block": true,
    "requires_block": true,
    "hidden": true
  },
  "define": {
    "signature": {
      "name": null,
      "&block": null
    },
    "name": "define",
    "introduced": "2,0,0",
    "summary": "Define a new function",
    "args": [
      {
        "name": ":symbol"
      }
    ],
    "accepts_block": true,
    "requires_block": true,
    "intro_fn": true,
    "hidden": false
  },
  "comment": {
    "signature": {
      "*args": null,
      "&block": null
    },
    "name": "comment",
    "introduced": "2,0,0",
    "summary": "Block level commenting",
    "accepts_block": true,
    "requires_block": true,
    "hidden": true
  },
  "uncomment": {
    "signature": {
      "*args": null,
      "&block": null
    },
    "name": "uncomment",
    "introduced": "2,0,0",
    "summary": "Block level comment ignoring",
    "accepts_block": true,
    "requires_block": true,
    "hidden": true
  },
  "print": {
    "signature": {
      "*msgs": null
    },
    "name": "print",
    "introduced": "2,0,0",
    "summary": "Display a message in the output pane",
    "args": [
      {
        "output": ":anything"
      }
    ],
    "accepts_block": false,
    "intro_fn": true,
    "hidden": true
  },
  "puts": {
    "signature": {
      "*msgs": null
    },
    "name": "puts",
    "introduced": "2,0,0",
    "summary": "Display a message in the output pane",
    "args": [
      {
        "output": ":anything"
      }
    ],
    "accepts_block": false,
    "intro_fn": true,
    "hidden": true
  },
  "vt": {
    "name": "vt",
    "introduced": "2,1,0",
    "summary": "Get virtual time",
    "accepts_block": false,
    "hidden": false,
    "inline": true
  },
  "factor": {
    "signature": {
      "val": null,
      "factor": null
    },
    "name": "factor?",
    "introduced": "2,1,0",
    "summary": "Factor test",
    "args": [
      {
        "val": ":number"
      },
      {
        "factor": ":number"
      }
    ],
    "accepts_block": false,
    "hidden": false
  },
  "quantise": {
    "signature": {
      "n": null,
      "step": null
    },
    "name": "quantise",
    "introduced": "2,1,0",
    "summary": "Quantise a value to resolution",
    "args": [
      {
        "n": ":number"
      },
      {
        "step": ":positive_number"
      }
    ],
    "accepts_block": false,
    "hidden": false,
    "inline": true
  },
  "dice": {
    "signature": {
      "num_sides": 6
    },
    "name": "dice",
    "introduced": "2,0,0",
    "summary": "Random dice throw",
    "args": [
      {
        "num_sides": ":number"
      }
    ],
    "accepts_block": false,
    "hidden": false,
    "inline": true
  },
  "one_in": {
    "signature": {
      "num": null
    },
    "name": "one_in",
    "introduced": "2,0,0",
    "summary": "Random true value with specified probability",
    "args": [
      {
        "num": ":number"
      }
    ],
    "accepts_block": false,
    "hidden": false,
    "inline": true
  },
  "rdist": {
    "signature": {
      "width": null,
      "centre": 0,
      "*opts": null
    },
    "name": "rdist",
    "introduced": "2,3,0",
    "summary": "Random number in centred distribution",
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
    ],
    "opts": {
      "step": 1
    },
    "accepts_block": false,
    "hidden": false,
    "inline": true
  },
  "rrand": {
    "signature": {
      "min": null,
      "max": null,
      "*opts": null
    },
    "name": "rrand",
    "introduced": "2,0,0",
    "summary": "Generate a random float between two numbers",
    "args": [
      {
        "min": ":number"
      },
      {
        "max": ":number"
      }
    ],
    "opts": {
      "step": 1
    },
    "accepts_block": false,
    "intro_fn": true,
    "hidden": false,
    "inline": true
  },
  "rrand_i": {
    "signature": {
      "min": null,
      "max": null
    },
    "name": "rrand_i",
    "introduced": "2,0,0",
    "summary": "Generate a random whole number between two points inclusively",
    "args": [
      {
        "min": ":number"
      },
      {
        "max": ":number"
      }
    ],
    "accepts_block": false,
    "hidden": false,
    "inline": true
  },
  "rand": {
    "signature": {
      "max": 1
    },
    "name": "rand",
    "introduced": "2,0,0",
    "summary": "Generate a random float below a value",
    "args": [
      {
        "max": ":number_or_range"
      }
    ],
    "accepts_block": false,
    "intro_fn": true,
    "hidden": false,
    "inline": true
  },
  "rand_i": {
    "signature": {
      "max": 2
    },
    "name": "rand_i",
    "introduced": "2,0,0",
    "summary": "Generate a random whole number below a value (exclusive)",
    "args": [
      {
        "max": ":number_or_range"
      }
    ],
    "accepts_block": false,
    "hidden": false,
    "inline": true
  },
  "rand_look": {
    "signature": {
      "*args": null
    },
    "name": "rand_look",
    "introduced": "2,11,0",
    "summary": "Generate a random number without consuming a rand",
    "args": [
      {
        "max": ":number_or_range"
      }
    ],
    "accepts_block": false,
    "hidden": false,
    "inline": true
  },
  "rand_i_look": {
    "signature": {
      "*args": null
    },
    "name": "rand_i_look",
    "introduced": "2,11,0",
    "summary": "Generate a random whole number without consuming a rand",
    "args": [
      {
        "max": ":number_or_range"
      }
    ],
    "accepts_block": false,
    "hidden": false,
    "inline": true
  },
  "rand_back": {
    "signature": {
      "amount": 1
    },
    "name": "rand_back",
    "introduced": "2,7,0",
    "summary": "Roll back random generator",
    "args": [
      {
        "amount": ":number"
      }
    ],
    "accepts_block": false,
    "hidden": false
  },
  "rand_skip": {
    "signature": {
      "amount": 1
    },
    "name": "rand_skip",
    "introduced": "2,7,0",
    "summary": "Jump forward random generator",
    "args": [
      {
        "amount": ":number"
      }
    ],
    "accepts_block": false,
    "hidden": false
  },
  "rand_reset": {
    "name": "rand_reset",
    "introduced": "2,7,0",
    "summary": "Reset rand generator to last seed",
    "args": [],
    "accepts_block": false,
    "hidden": false
  },
  "shuffle": {
    "signature": {
      "list": null
    },
    "name": "shuffle",
    "introduced": "2,1,0",
    "summary": "Randomise order of a list",
    "args": [],
    "accepts_block": false,
    "hidden": false,
    "inline": true,
    "alt_args": [
      {
        "list": ":array"
      }
    ]
  },
  "use_random_seed": {
    "signature": {
      "seed": null,
      "&block": null
    },
    "name": "use_random_seed",
    "introduced": "2,0,0",
    "summary": "Set random seed generator to known seed",
    "args": [
      {
        "seed": ":number"
      }
    ],
    "accepts_block": false,
    "hidden": false
  },
  "with_random_seed": {
    "signature": {
      "seed": null,
      "&block": null
    },
    "name": "with_random_seed",
    "introduced": "2,0,0",
    "summary": "Specify random seed for code block",
    "args": [
      {
        "seed": ":number"
      }
    ],
    "accepts_block": true,
    "requires_block": true,
    "hidden": false
  },
  "use_random_source": {
    "signature": {
      "noise_type": null,
      "&block": null
    },
    "name": "use_random_source",
    "introduced": "3,3,0",
    "summary": "Change how random numbers are chosen",
    "args": [
      {
        "noise_type": ":symbol"
      }
    ],
    "accepts_block": false,
    "hidden": false
  },
  "with_random_source": {
    "signature": {
      "noise_type": null,
      "&block": null
    },
    "name": "with_random_source",
    "introduced": "3,3,0",
    "summary": "Specify random distribution for code block",
    "args": [
      {
        "noise_type": ":symbol"
      }
    ],
    "accepts_block": true,
    "requires_block": true,
    "hidden": false
  },
  "with_tempo": {
    "signature": {
      "*args": null,
      "&block": null
    },
    "hidden": true
  },
  "use_cue_logging": {
    "signature": {
      "v": null,
      "&block": null
    },
    "name": "use_cue_logging",
    "introduced": "2,6,0",
    "summary": "Enable and disable cue logging",
    "args": [
      {
        "true_or_false": ":boolean"
      }
    ],
    "accepts_block": false,
    "hidden": false
  },
  "with_cue_logging": {
    "signature": {
      "v": null,
      "&block": null
    },
    "name": "with_cue_logging",
    "introduced": "2,6,0",
    "summary": "Block-level enable and disable cue logging",
    "args": [
      {
        "true_or_false": ":boolean"
      }
    ],
    "accepts_block": true,
    "requires_block": true,
    "hidden": false
  },
  "use_bpm": {
    "signature": {
      "bpm": null,
      "&block": null
    },
    "name": "use_bpm",
    "introduced": "2,0,0",
    "summary": "Set the tempo",
    "args": [
      {
        "bpm": ":number"
      }
    ],
    "accepts_block": false,
    "intro_fn": true,
    "hidden": false
  },
  "with_bpm": {
    "signature": {
      "bpm": null,
      "&block": null
    },
    "name": "with_bpm",
    "introduced": "2,0,0",
    "summary": "Set the tempo for the code block",
    "args": [
      {
        "bpm": ":number"
      }
    ],
    "accepts_block": true,
    "requires_block": true,
    "hidden": false
  },
  "with_bpm_mul": {
    "signature": {
      "mul": null,
      "&block": null
    },
    "name": "with_bpm_mul",
    "introduced": "2,3,0",
    "summary": "Set new tempo as a multiple of current tempo for block",
    "args": [
      {
        "mul": ":number"
      }
    ],
    "accepts_block": true,
    "requires_block": true,
    "hidden": false
  },
  "use_bpm_mul": {
    "signature": {
      "mul": null,
      "&block": null
    },
    "name": "use_bpm_mul",
    "introduced": "2,3,0",
    "summary": "Set new tempo as a multiple of current tempo",
    "args": [
      {
        "mul": ":number"
      }
    ],
    "accepts_block": false,
    "hidden": false
  },
  "density": {
    "signature": {
      "d": null,
      "&block": null
    },
    "name": "density",
    "introduced": "2,3,0",
    "summary": "Squash and repeat time",
    "args": [
      {
        "d": ":density"
      }
    ],
    "accepts_block": true,
    "hidden": false,
    "async_block": true,
    "requires_block": true
  },
  "current_time": {
    "name": "current_time",
    "introduced": "3,0,0",
    "summary": "Get current (logically quantized) time",
    "accepts_block": false,
    "hidden": false
  },
  "current_random_seed": {
    "name": "current_random_seed",
    "introduced": "2,10,0",
    "summary": "Get current random seed",
    "accepts_block": false,
    "hidden": true,
    "intro_fn": true
  },
  "current_bpm": {
    "name": "current_bpm",
    "introduced": "2,0,0",
    "summary": "Get current tempo",
    "accepts_block": false,
    "hidden": true
  },
  "current_beat_duration": {
    "name": "current_beat_duration",
    "introduced": "2,6,0",
    "summary": "Duration of current beat",
    "accepts_block": false,
    "hidden": true
  },
  "beat": {
    "name": "beat",
    "introduced": "2,10,0",
    "summary": "Get current beat",
    "args": [],
    "accepts_block": false,
    "hidden": true
  },
  "rt": {
    "signature": {
      "t": null
    },
    "name": "rt",
    "introduced": "2,0,0",
    "summary": "Real time conversion",
    "args": [
      {
        "seconds": ":number"
      }
    ],
    "accepts_block": false,
    "hidden": false,
    "inline": true
  },
  "bt": {
    "signature": {
      "t": null
    },
    "name": "bt",
    "introduced": "2,8,0",
    "summary": "Beat time conversion",
    "args": [
      {
        "seconds": ":number"
      }
    ],
    "accepts_block": false,
    "hidden": true
  },
  "set_sched_ahead_time": {
    "signature": {
      "sat": null
    },
    "name": "set_sched_ahead_time!",
    "modifies_env": true,
    "introduced": "2,0,0",
    "summary": "Set sched ahead time globally",
    "args": [
      {
        "time": ":number"
      }
    ],
    "accepts_block": false,
    "hidden": false
  },
  "use_sched_ahead_time": {
    "name": "use_sched_ahead_time",
    "introduced": "3,0,0",
    "summary": "Set sched ahead time for the current thread",
    "args": [
      {
        "time": ":number"
      }
    ],
    "modifies_env": true,
    "accepts_block": false,
    "hidden": false
  },
  "use_real_time": {
    "name": "use_real_time",
    "introduced": "3,0,0",
    "summary": "Set sched ahead time to 0 for the current thread",
    "args": [],
    "modifies_env": true,
    "accepts_block": false,
    "hidden": false
  },
  "with_real_time": {
    "signature": {
      "&blk": null
    },
    "name": "with_real_time",
    "introduced": "3,0,0",
    "summary": "Sets sched ahead time to 0 within the block for the current thread",
    "args": [],
    "modifies_env": true,
    "accepts_block": false,
    "hidden": false
  },
  "with_sched_ahead_time": {
    "name": "with_sched_ahead_time",
    "introduced": "3,0,0",
    "summary": "Block-level set sched ahead time for the current thread",
    "args": [
      {
        "time": ":number"
      }
    ],
    "modifies_env": true,
    "accepts_block": false,
    "hidden": false
  },
  "current_sched_ahead_time": {
    "name": "current_sched_ahead_time",
    "introduced": "2,0,0",
    "summary": "Get current sched ahead time",
    "accepts_block": false,
    "hidden": true
  },
  "__change_time": {
    "signature": {
      "new_vt": null
    },
    "hidden": false
  },
  "sleep": {
    "signature": {
      "beats": null
    },
    "name": "sleep",
    "introduced": "2,0,0",
    "summary": "Wait for beat duration",
    "args": [
      {
        "beats": ":number"
      }
    ],
    "accepts_block": false,
    "advances_time": true,
    "hidden": false
  },
  "wait": {
    "signature": {
      "time": null
    },
    "name": "wait",
    "introduced": "2,0,0",
    "summary": "Wait for duration",
    "args": [
      {
        "beats": ":number"
      }
    ],
    "accepts_block": false,
    "advances_time": true,
    "hidden": true
  },
  "__live_loop_cue": {
    "signature": {
      "id": null
    },
    "hidden": false
  },
  "sync_bpm": {
    "signature": {
      "*args": null
    },
    "name": "sync_bpm",
    "introduced": "2,10,0",
    "summary": "Sync and inherit BPM from other threads ",
    "args": [
      {
        "cue_id": ":symbol"
      }
    ],
    "opts": {},
    "accepts_block": false,
    "advances_time": true,
    "hidden": false
  },
  "sync_event": {
    "signature": {
      "*args": null
    },
    "hidden": false
  },
  "sync": {
    "signature": {
      "*args": null
    },
    "name": "sync",
    "introduced": "2,0,0",
    "summary": "Sync with other threads",
    "args": [
      {
        "cue_id": ":symbol"
      }
    ],
    "opts": {
      "bpm_sync": false
    },
    "accepts_block": false,
    "advances_time": true,
    "hidden": false
  },
  "in_thread": {
    "signature": {
      "*opts": null,
      "&block": null
    },
    "name": "in_thread",
    "introduced": "2,0,0",
    "summary": "Run code block at the same time",
    "opts": {
      "name": ":foo",
      "delay": 0,
      "sync": ":foo",
      "sync_bpm": ":foo"
    },
    "accepts_block": true,
    "requires_block": true,
    "async_block": true,
    "hidden": false
  },
  "assert_inherited": {
    "signature": {
      "arg": null,
      "klass": "Object"
    },
    "hidden": false
  },
  "assert_error": {
    "signature": {
      "klass": "Exception",
      "&blk": null
    },
    "name": "assert_error",
    "introduced": "3,0,0",
    "summary": "Ensure block throws an error",
    "args": [
      {
        "class": ":Exception"
      }
    ],
    "accepts_block": true,
    "hidden": false
  },
  "assert_not": {
    "signature": {
      "arg": null,
      "msg": "nil"
    },
    "name": "assert_not",
    "introduced": "3,3,0",
    "summary": "Ensure arg is not valid",
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
    ],
    "accepts_block": false,
    "hidden": false
  },
  "assert": {
    "signature": {
      "arg": null,
      "msg": "nil"
    },
    "name": "assert",
    "introduced": "2,8,0",
    "summary": "Ensure arg is valid",
    "args": [
      {
        "is_true": ":boolean"
      }
    ],
    "alt_args": [],
    "accepts_block": false,
    "hidden": false
  },
  "assert_not_equal": {
    "signature": {
      "arg1": null,
      "arg2": null,
      "msg": "nil"
    },
    "name": "assert_not_equal",
    "introduced": "3,3,0",
    "summary": "Ensure args are not equal",
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
    ],
    "accepts_block": false,
    "hidden": false
  },
  "assert_equal": {
    "signature": {
      "arg1": null,
      "arg2": null,
      "msg": "nil"
    },
    "name": "assert_equal",
    "introduced": "2,8,0",
    "summary": "Ensure args are equal",
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
    ],
    "accepts_block": false,
    "hidden": false
  },
  "assert_similar": {
    "signature": {
      "a": null,
      "b": null,
      "msg": "nil"
    },
    "name": "assert_similar",
    "introduced": "3,0,0",
    "summary": "Ensure args are similar",
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
    ],
    "accepts_block": false,
    "hidden": false
  },
  "load_buffer": {
    "signature": {
      "path": null
    },
    "name": "load_buffer",
    "introduced": "2,10,0",
    "summary": "Load the contents of a file to the current buffer",
    "args": [
      {
        "path": ":string"
      }
    ],
    "accepts_block": false,
    "hidden": false
  },
  "load_example": {
    "signature": {
      "example_name": null
    },
    "name": "load_example",
    "introduced": "2,10,0",
    "summary": "Load a built-in example",
    "args": [
      {
        "path": ":string"
      }
    ],
    "accepts_block": false,
    "hidden": true
  },
  "note_list": {
    "accepts_block": false,
    "summary": "Make a list of notes",
    "opts": {},
    "signature": {},
    "hidden": false,
    "args": [],
    "name": "note_list",
    "introduced": "blend-sonic"
  },
  "time_now": {
    "accepts_block": false,
    "summary": "return a number based on current time",
    "opts": {},
    "signature": {},
    "hidden": false,
    "args": [],
    "name": "time_now",
    "introduced": "blend-sonic"
  }
}

#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/

lang_sound = {
  "use_timing_guarantees": {
    "signature": {
      "v": null,
      "&block": null
    },
    "name": "use_timing_guarantees",
    "introduced": "2,10,0",
    "summary": "Inhibit synth triggers if too late",
    "args": [
      {
        "bool": ":true_or_false"
      }
    ],
    "accepts_block": false,
    "hidden": false,
    "requires_block": false
  },
  "with_timing_guarantees": {
    "signature": {
      "v": null,
      "&block": null
    },
    "name": "with_timing_guarantees",
    "introduced": "2,10,0",
    "summary": "Block-scoped inhibition of synth triggers if too late",
    "args": [
      {
        "bool": ":true_or_false"
      }
    ],
    "accepts_block": true,
    "hidden": false,
    "requires_block": true
  },
  "use_external_synths": {
    "signature": {
      "v": null,
      "&block": null
    },
    "hidden": true
  },
  "use_timing_warnings": {
    "signature": {
      "v": null,
      "&block": null
    },
    "hidden": true
  },
  "with_timing_warnings": {
    "signature": {
      "v": null,
      "&block": null
    },
    "hidden": true
  },
  "use_sample_bpm": {
    "signature": {
      "sample_name": null,
      "*args": null
    },
    "name": "use_sample_bpm",
    "introduced": "2,1,0",
    "summary": "Sample-duration-based bpm modification",
    "args": [],
    "opts": {
      "num_beats": 1
    },
    "accepts_block": false,
    "hidden": false,
    "alt_args": [
      {
        "string_or_number": ":sample_name_or_duration"
      }
    ]
  },
  "with_sample_bpm": {
    "signature": {
      "sample_name": null,
      "*args": null,
      "&block": null
    },
    "name": "with_sample_bpm",
    "introduced": "2,1,0",
    "summary": "Block-scoped sample-duration-based bpm modification",
    "args": [
      {
        "string_or_number": ":sample_name_or_duration"
      }
    ],
    "opts": {
      "num_beats": 1
    },
    "accepts_block": true,
    "requires_block": true,
    "hidden": false
  },
  "use_arg_bpm_scaling": {
    "signature": {
      "bool": null,
      "&block": null
    },
    "name": "use_arg_bpm_scaling",
    "introduced": "2,0,0",
    "summary": "Enable and disable BPM scaling",
    "args": [
      {
        "bool": ":boolean"
      }
    ],
    "accepts_block": false,
    "hidden": false
  },
  "with_arg_bpm_scaling": {
    "signature": {
      "bool": null,
      "&block": null
    },
    "name": "with_arg_bpm_scaling",
    "introduced": "2,0,0",
    "summary": "Block-level enable and disable BPM scaling",
    "accepts_block": true,
    "requires_block": true,
    "hidden": false
  },
  "set_audio_latency": {
    "signature": {
      "delta_ms": null
    },
    "name": "set_audio_latency!",
    "modifies_env": true,
    "introduced": "3,1,0",
    "summary": "Globally modify audio latency",
    "args": [
      {
        "milliseconds": ":number"
      }
    ],
    "accepts_block": false,
    "hidden": false
  },
  "set_recording_bit_depth": {
    "signature": {
      "d": null
    },
    "name": "set_recording_bit_depth!",
    "modifies_env": true,
    "introduced": "2,11,0",
    "summary": "Set the bit depth for recording wav files",
    "args": [
      {
        "bit_depth": ":number"
      }
    ],
    "accepts_block": false,
    "hidden": false
  },
  "set_control_delta": {
    "signature": {
      "t": null
    },
    "name": "set_control_delta!",
    "modifies_env": true,
    "introduced": "2,1,0",
    "summary": "Set control delta globally",
    "args": [
      {
        "time": ":number"
      }
    ],
    "accepts_block": false,
    "hidden": false
  },
  "use_debug": {
    "signature": {
      "v": null,
      "&block": null
    },
    "name": "use_debug",
    "introduced": "2,0,0",
    "summary": "Enable and disable debug",
    "args": [
      {
        "true_or_false": ":boolean"
      }
    ],
    "accepts_block": false,
    "hidden": false
  },
  "with_debug": {
    "signature": {
      "v": null,
      "&block": null
    },
    "name": "with_debug",
    "introduced": "2,0,0",
    "summary": "Block-level enable and disable debug",
    "args": [
      {
        "true_or_false": ":boolean"
      }
    ],
    "accepts_block": true,
    "requires_block": true,
    "hidden": true
  },
  "use_arg_checks": {
    "signature": {
      "v": null,
      "&block": null
    },
    "name": "use_arg_checks",
    "introduced": "2,0,0",
    "summary": "Enable and disable arg checks",
    "args": [
      {
        "true_or_false": ":boolean"
      }
    ],
    "accepts_block": false,
    "hidden": false
  },
  "with_arg_checks": {
    "signature": {
      "v": null,
      "&block": null
    },
    "name": "with_arg_checks",
    "introduced": "2,0,0",
    "summary": "Block-level enable and disable arg checks",
    "args": [
      {
        "true_or_false": ":boolean"
      }
    ],
    "accepts_block": true,
    "requires_block": true,
    "hidden": false
  },
  "use_synth": {
    "signature": {
      "synth_name": null,
      "*args": null,
      "&block": null
    },
    "name": "use_synth",
    "introduced": "2,0,0",
    "summary": "Switch current synth",
    "args": [],
    "accepts_block": false,
    "intro_fn": true,
    "hidden": false,
    "alt_args": [
      {
        "synth_name": ":symbol"
      }
    ]
  },
  "with_synth": {
    "signature": {
      "synth_name": null,
      "*args": null,
      "&block": null
    },
    "name": "with_synth",
    "introduced": "2,0,0",
    "summary": "Block-level synth switching",
    "args": [
      {
        "synth_name": ":symbol"
      }
    ],
    "accepts_block": true,
    "requires_block": true,
    "hidden": true
  },
  "recording_start": {
    "name": "recording_start",
    "introduced": "2,0,0",
    "summary": "Start recording",
    "accepts_block": false,
    "hidden": true
  },
  "recording_stop": {
    "name": "recording_stop",
    "introduced": "2,0,0",
    "summary": "Stop recording",
    "accepts_block": false,
    "hidden": true
  },
  "recording_save": {
    "signature": {
      "filename": null
    },
    "name": "recording_save",
    "introduced": "2,0,0",
    "summary": "Save recording",
    "args": [
      {
        "path": ":string"
      }
    ],
    "accepts_block": false,
    "hidden": true
  },
  "recording_delete": {
    "name": "recording_delete",
    "accepts_block": false,
    "hidden": true
  },
  "reset_mixer": {
    "signature": {
      "": null
    },
    "name": "reset_mixer!",
    "modifies_env": true,
    "introduced": "2,9,0",
    "summary": "Reset main mixer",
    "opts": {},
    "accepts_block": false,
    "hidden": false
  },
  "set_mixer_control": {
    "signature": {
      "opts": null
    },
    "name": "set_mixer_control!",
    "modifies_env": true,
    "introduced": "2,7,0",
    "summary": "Control main mixer",
    "opts": {
      "pre_amp": 1,
      "amp": 1,
      "hpf": 0,
      "lpf": 131,
      "hpf_bypass": 0,
      "lpf_bypass": 0,
      "limiter_bypass": 0,
      "leak_dc_bypass": 0
    },
    "accepts_block": false,
    "hidden": false
  },
  "set_mixer_invert_stereo!": {
    "hidden": false
  },
  "set_mixer_standard_stereo!": {
    "hidden": false
  },
  "set_mixer_stereo_mode!": {
    "hidden": false
  },
  "set_mixer_mono_mode!": {
    "hidden": false
  },
  "synth": {
    "signature": {
      "synth_name": null,
      "*args": null,
      "&blk": null
    },
    "name": "synth",
    "introduced": "2,0,0",
    "summary": "Trigger specific synth",
    "args": [],
    "opts": {
      "note": ":e1",
      "note_num": 77,
      "cutoff": 0,
      "wave": 0,
      "phase": 0,
      "amp": 1,
      "amp_slide": 1,
      "pan": 0,
      "pan_slide": 1,
      "attack": 0,
      "decay": 0,
      "sustain": 1,
      "release": 0,
      "attack_level": 1,
      "decay_level": 1,
      "sustain_level": 1,
      "env_curve": 1,
      "slide": 0,
      "pitch": 0,
      "on": 1
    },
    "accepts_block": true,
    "hidden": false,
    "async_block": true,
    "intro_fn": true,
    "requires_block": false,
    "alt_args": [
      {
        "synth_name": ":symbol"
      }
    ]
  },
  "play": {
    "signature": {
      "n": null,
      "*args": null,
      "&blk": null
    },
    "name": "play",
    "introduced": "2,0,0",
    "summary": "Play current synth",
    "args": [
      {
        "note": ":symbol_or_number"
      }
    ],
    "opts": {
      "amp": 1,
      "amp_slide": 1,
      "pan": 0,
      "pan_slide": 1,
      "attack": 0,
      "decay": 0,
      "sustain": 1,
      "release": 0,
      "attack_level": 1,
      "decay_level": 1,
      "sustain_level": 1,
      "env_curve": 1,
      "slide": 0,
      "pitch": 0,
      "on": 1
    },
    "accepts_block": true,
    "intro_fn": true,
    "hidden": false,
    "async_block": true,
    "requires_block": false
  },
  "play_pattern": {
    "signature": {
      "notes": null,
      "*args": null
    },
    "name": "play_pattern",
    "introduced": "2,0,0",
    "summary": "Play pattern of notes",
    "args": [
      {
        "notes": ":list"
      }
    ],
    "opts": {},
    "accepts_block": false,
    "hidden": false
  },
  "play_pattern_timed": {
    "signature": {
      "notes": null,
      "times": null,
      "*args": null
    },
    "name": "play_pattern_timed",
    "introduced": "2,0,0",
    "summary": "Play pattern of notes with specific times",
    "args": [
      {
        "notes": ":list"
      },
      {
        "times": ":list_or_number"
      }
    ],
    "opts": {
      "amp": 1,
      "amp_slide": 1,
      "pan": 0,
      "pan_slide": 1,
      "attack": 0,
      "decay": 0,
      "sustain": 1,
      "release": 0,
      "attack_level": 1,
      "decay_level": 1,
      "sustain_level": 1,
      "env_curve": 1,
      "slide": 0,
      "pitch": 0,
      "on": 1
    },
    "accepts_block": false,
    "hidden": false
  },
  "play_chord": {
    "signature": {
      "notes": null,
      "*args": null
    },
    "name": "play_chord",
    "introduced": "2,0,0",
    "summary": "Play notes simultaneously",
    "args": [
      {
        "notes": ":list"
      }
    ],
    "opts": {
      "amp": 1,
      "amp_slide": 1,
      "pan": 0,
      "pan_slide": 1,
      "attack": 0,
      "decay": 0,
      "sustain": 1,
      "release": 0,
      "attack_level": 1,
      "decay_level": 1,
      "sustain_level": 1,
      "env_curve": 1,
      "slide": 0,
      "pitch": 0,
      "on": 1
    },
    "accepts_block": false,
    "hidden": false
  },
  "use_merged_synth_defaults": {
    "signature": {
      "*args": null,
      "&block": null
    },
    "name": "use_merged_synth_defaults",
    "introduced": "2,0,0",
    "summary": "Merge synth defaults",
    "opts": {},
    "accepts_block": false,
    "hidden": false
  },
  "with_merged_synth_defaults": {
    "signature": {
      "*args": null,
      "&block": null
    },
    "name": "with_merged_synth_defaults",
    "introduced": "2,0,0",
    "summary": "Block-level merge synth defaults",
    "opts": {},
    "accepts_block": true,
    "requires_block": true,
    "hidden": true
  },
  "use_synth_defaults": {
    "signature": {
      "*args": null,
      "&block": null
    },
    "name": "use_synth_defaults",
    "introduced": "2,0,0",
    "summary": "Use new synth defaults",
    "opts": {},
    "accepts_block": false,
    "hidden": true
  },
  "use_sample_defaults": {
    "signature": {
      "*args": null,
      "&block": null
    },
    "name": "use_sample_defaults",
    "introduced": "2,5,0",
    "summary": "Use new sample defaults",
    "opts": {
      "rate": 1,
      "beat_stretch": 1,
      "pitch_stretch": 1,
      "attack": 0,
      "sustain": 1,
      "release": 0,
      "start": 0,
      "finish": 1,
      "pan": 0,
      "amp": 1,
      "pre_amp": 1,
      "onset": 0,
      "on": 1,
      "slice": 16,
      "num_slices": 16,
      "norm": 0,
      "lpf": 131,
      "lpf_init_level": 30,
      "lpf_attack_level": 0,
      "lpf_decay_level": 0,
      "lpf_sustain_level": 0,
      "lpf_release_level": 0,
      "lpf_attack": 0,
      "lpf_decay": 0,
      "lpf_sustain": 0,
      "lpf_release": 0,
      "lpf_min": 30,
      "lpf_env_curve": 1,
      "hpf": 0,
      "hpf_init_level": 130,
      "hpf_attack_level": 0,
      "hpf_decay_level": 0,
      "hpf_sustain_level": 0,
      "hpf_release_level": 0,
      "hpf_attack": 0,
      "hpf_decay": 0,
      "hpf_sustain": 0,
      "hpf_release": 0,
      "hpf_env_curve": 1,
      "hpf_max": 200,
      "rpitch": 0,
      "pitch": 0,
      "window_size": 0,
      "pitch_dis": 0,
      "time_dis": 0,
      "compress": 0,
      "threshold": 0,
      "slope_below": 1,
      "slope_above": 1,
      "clamp_time": 0,
      "relax_time": 0,
      "slide": 0,
      "path": "/path/to/file"
    },
    "accepts_block": false,
    "hidden": false
  },
  "use_merged_sample_defaults": {
    "signature": {
      "*args": null,
      "&block": null
    },
    "name": "use_merged_sample_defaults",
    "introduced": "2,9,0",
    "summary": "Merge new sample defaults",
    "opts": {},
    "accepts_block": false,
    "hidden": false
  },
  "with_sample_defaults": {
    "signature": {
      "*args": null,
      "&block": null
    },
    "name": "with_sample_defaults",
    "introduced": "2,5,0",
    "summary": "Block-level use new sample defaults",
    "opts": {},
    "accepts_block": true,
    "requires_block": true,
    "hidden": false
  },
  "with_merged_sample_defaults": {
    "signature": {
      "*args": null,
      "&block": null
    },
    "name": "with_merged_sample_defaults",
    "introduced": "2,9,0",
    "summary": "Block-level use merged sample defaults",
    "opts": {},
    "accepts_block": true,
    "requires_block": true,
    "hidden": false
  },
  "with_synth_defaults": {
    "signature": {
      "*args": null,
      "&block": null
    },
    "name": "with_synth_defaults",
    "introduced": "2,0,0",
    "summary": "Block-level use new synth defaults",
    "opts": {},
    "accepts_block": true,
    "requires_block": true,
    "hidden": true
  },
  "use_fx": {
    "signature": {
      "*args": null,
      "&block": null
    },
    "hidden": true
  },
  "with_afx": {
    "signature": {
      "fx_name": null,
      "*args": null,
      "&block": null
    },
    "hidden": true
  },
  "with_fx": {
    "signature": {
      "fx_name": null,
      "*args": null,
      "&block": null
    },
    "name": "with_fx",
    "introduced": "2,0,0",
    "summary": "Use Studio FX",
    "args": [],
    "opts": {
      "reps": 1,
      "kill_delay": 1
    },
    "accepts_block": true,
    "requires_block": true,
    "intro_fn": true,
    "hidden": true,
    "async_block": true,
    "alt_args": [
      {
        "fx_name": ":symbol"
      }
    ]
  },
  "current_synth": {
    "name": "current_synth",
    "introduced": "2,0,0",
    "summary": "Get current synth",
    "accepts_block": false,
    "hidden": true
  },
  "current_synth_defaults": {
    "name": "current_synth_defaults",
    "introduced": "2,0,0",
    "summary": "Get current synth defaults",
    "accepts_block": false,
    "hidden": true
  },
  "current_sample_defaults": {
    "name": "current_sample_defaults",
    "introduced": "2,5,0",
    "summary": "Get current sample defaults",
    "accepts_block": false,
    "hidden": true
  },
  "current_volume": {
    "name": "current_volume",
    "introduced": "2,0,0",
    "summary": "Get current volume",
    "accepts_block": false,
    "hidden": true
  },
  "current_debug": {
    "name": "current_debug",
    "introduced": "2,0,0",
    "summary": "Get current debug status",
    "accepts_block": false,
    "hidden": true
  },
  "current_arg_checks": {
    "name": "current_arg_checks",
    "introduced": "2,0,0",
    "summary": "Get current arg checking status",
    "accepts_block": false,
    "hidden": true
  },
  "set_volume": {
    "signature": {
      "vol": null,
      "now": "false",
      "silent": "false"
    },
    "name": "set_volume!",
    "modifies_env": true,
    "introduced": "2,0,0",
    "summary": "Set Volume globally",
    "args": [
      {
        "vol": ":number"
      }
    ],
    "accepts_block": false,
    "hidden": false
  },
  "sample_loaded": {
    "signature": {
      "*args": null
    },
    "name": "sample_loaded?",
    "introduced": "2,2,0",
    "summary": "Test if sample was pre-loaded",
    "args": [
      {
        "path": ":string"
      }
    ],
    "accepts_block": false,
    "hidden": false
  },
  "load_sample": {
    "signature": {
      "*args": null
    },
    "name": "load_sample",
    "introduced": "2,0,0",
    "summary": "Pre-load first matching sample",
    "args": [
      {
        "path": ":string"
      }
    ],
    "accepts_block": false,
    "hidden": true
  },
  "load_samples": {
    "signature": {
      "*args": null
    },
    "name": "load_samples",
    "introduced": "2,0,0",
    "summary": "Pre-load all matching samples",
    "args": [
      {
        "paths": ":list"
      }
    ],
    "accepts_block": false,
    "hidden": false
  },
  "load_sample_at_path": {
    "signature": {
      "path": null
    },
    "hidden": true
  },
  "sample_info": {
    "signature": {
      "*args": null
    },
    "name": "sample_info",
    "introduced": "2,0,0",
    "summary": "Get sample information",
    "args": [
      {
        "path": ":string"
      }
    ],
    "accepts_block": false,
    "hidden": true
  },
  "sample_buffer": {
    "signature": {
      "*args": null
    },
    "name": "sample_buffer",
    "introduced": "2,0,0",
    "summary": "Get sample data",
    "args": [
      {
        "path": ":string"
      }
    ],
    "accepts_block": false,
    "hidden": true
  },
  "sample_duration": {
    "signature": {
      "*args": null
    },
    "name": "sample_duration",
    "introduced": "2,0,0",
    "summary": "Get duration of sample in beats",
    "args": [
      {
        "path": ":string"
      }
    ],
    "opts": {
      "rate": 1,
      "start": 0,
      "finish": 1,
      "attack": 0,
      "decay": 0,
      "sustain": 1,
      "release": 0,
      "beat_stretch": 1,
      "pitch_stretch": 1,
      "rpitch": 0
    },
    "accepts_block": false,
    "hidden": true
  },
  "sample_split_filts_and_opts": {
    "signature": {
      "args": null
    },
    "hidden": true
  },
  "resolve_sample_paths": {
    "signature": {
      "filts_and_sources": null
    },
    "hidden": true
  },
  "resolve_sample_path": {
    "signature": {
      "filts_and_sources": null
    },
    "hidden": true
  },
  "sample_paths": {
    "signature": {
      "*args": null
    },
    "name": "sample_paths",
    "introduced": "2,10,0",
    "summary": "Sample Pack Filter Resolution",
    "args": [
      {
        "pre_args": ":source_and_filter_types"
      }
    ],
    "returns": ":ring",
    "accepts_block": false,
    "hidden": true
  },
  "sample": {
    "signature": {
      "*args": null,
      "&blk": null
    },
    "name": "sample",
    "introduced": "2,0,0",
    "summary": "Trigger sample",
    "args": [],
    "opts": {
      "rate": 1,
      "beat_stretch": 1,
      "pitch_stretch": 1,
      "attack": 0,
      "sustain": 1,
      "release": 0,
      "start": 0,
      "finish": 1,
      "pan": 0,
      "amp": 1,
      "pre_amp": 1,
      "onset": 0,
      "on": 1,
      "slice": 16,
      "num_slices": 16,
      "norm": 0,
      "lpf": 131,
      "lpf_init_level": 30,
      "lpf_attack_level": 0,
      "lpf_decay_level": 0,
      "lpf_sustain_level": 0,
      "lpf_release_level": 0,
      "lpf_attack": 0,
      "lpf_decay": 0,
      "lpf_sustain": 0,
      "lpf_release": 0,
      "lpf_min": 30,
      "lpf_env_curve": 1,
      "hpf": 0,
      "hpf_init_level": 130,
      "hpf_attack_level": 0,
      "hpf_decay_level": 0,
      "hpf_sustain_level": 0,
      "hpf_release_level": 0,
      "hpf_attack": 0,
      "hpf_decay": 0,
      "hpf_sustain": 0,
      "hpf_release": 0,
      "hpf_env_curve": 1,
      "hpf_max": 200,
      "rpitch": 0,
      "pitch": 0,
      "window_size": 0,
      "pitch_dis": 0,
      "time_dis": 0,
      "compress": 0,
      "threshold": 0,
      "slope_below": 1,
      "slope_above": 1,
      "clamp_time": 0,
      "relax_time": 0,
      "slide": 0,
      "path": "/path/to/file"
    },
    "accepts_block": true,
    "intro_fn": true,
    "hidden": false,
    "async_block": true,
    "requires_block": false,
    "alt_args": [
      {
        "name_or_path": ":symbol_or_string"
      }
    ]
  },
  "status": {
    "name": "status",
    "introduced": "2,0,0",
    "summary": "Get server status",
    "accepts_block": false,
    "hidden": true
  },
  "control": {
    "signature": {
      "*args": null
    },
    "name": "control",
    "introduced": "2,0,0",
    "summary": "Control running synth",
    "args": [
      {
        "node": ":synth_node"
      }
    ],
    "opts": {},
    "accepts_block": false,
    "hidden": false
  },
  "kill": {
    "signature": {
      "node": null
    },
    "name": "kill",
    "introduced": "2,0,0",
    "summary": "Kill synth",
    "args": [
      {
        "node": ":synth_node"
      }
    ],
    "opts": {},
    "accepts_block": false,
    "hidden": false
  },
  "sample_names": {
    "signature": {
      "group": null
    },
    "name": "sample_names",
    "introduced": "2,0,0",
    "summary": "Get sample names",
    "args": [
      {
        "group": ":symbol"
      }
    ],
    "returns": ":ring",
    "accepts_block": false,
    "memoize": true,
    "hidden": true
  },
  "all_sample_names": {
    "name": "all_sample_names",
    "introduced": "2,0,0",
    "summary": "Get all sample names",
    "accepts_block": false,
    "memoize": true,
    "hidden": true
  },
  "sample_groups": {
    "name": "sample_groups",
    "introduced": "2,0,0",
    "summary": "Get all sample groups",
    "accepts_block": false,
    "memoize": true,
    "hidden": true
  },
  "synth_names": {
    "name": "synth_names",
    "introduced": "2,9,0",
    "summary": "Get all synth names",
    "accepts_block": false,
    "memoize": true,
    "hidden": true
  },
  "fx_names": {
    "name": "fx_names",
    "introduced": "2,10,0",
    "summary": "Get all FX names",
    "accepts_block": false,
    "memoize": true,
    "hidden": true
  },
  "load_synthdefs": {
    "signature": {
      "path": "synthdef_path"
    },
    "name": "load_synthdefs",
    "introduced": "2,0,0",
    "summary": "Load external synthdefs",
    "args": [
      {
        "path": ":string"
      }
    ],
    "accepts_block": false,
    "hidden": true
  },
  "note_list": {
    "accepts_block": false,
    "summary": "Make a list of notes",
    "opts": {},
    "signature": {},
    "hidden": false,
    "args": [],
    "name": "note_list",
    "introduced": "blend-sonic"
  },
  "time_now": {
    "accepts_block": false,
    "summary": "return a number based on current time",
    "opts": {},
    "signature": {},
    "hidden": false,
    "args": [],
    "name": "time_now",
    "introduced": "blend-sonic"
  }
}

sound_args_types_conversion = {}

sound_opts_types_conversion = {}

#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/

synths = {
  "SynthInfo": {
    "opts": {},
    "inherit_base": "BaseInfo",
    "inherit_arg": true,
    "hidden": true
  },
  "SonicPiSynth": {
    "opts": {},
    "inherit_base": "SynthInfo",
    "inherit_arg": true,
    "hidden": true
  },
  "SoundIn": {
    "opts": {
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "pan": 0,
      "pan_slide": 0,
      "pan_slide_shape": 1,
      "pan_slide_curve": 0,
      "attack": 0,
      "decay": 0,
      "sustain": 1,
      "release": 0,
      "attack_level": 1,
      "decay_level": 1,
      "sustain_level": 1,
      "env_curve": 0,
      "input": 1
    },
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false,
    "name": ":sound_in",
    "summary": "Sound In",
    "hidden": false
  },
  "SoundInStereo": {
    "opts": {
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "pan": 0,
      "pan_slide": 0,
      "pan_slide_shape": 1,
      "pan_slide_curve": 0,
      "attack": 0,
      "decay": 0,
      "sustain": 1,
      "release": 0,
      "attack_level": 1,
      "decay_level": 1,
      "sustain_level": 1,
      "env_curve": 0,
      "input": 1
    },
    "inherit_base": "SoundIn",
    "inherit_arg": true,
    "name": ":sound_in_stereo",
    "summary": "Sound In Stereo",
    "hidden": true
  },
  "DullBell": {
    "opts": {
      "note": 52,
      "note_slide": 0,
      "note_slide_shape": 1,
      "note_slide_curve": 0,
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "pan": 0,
      "pan_slide": 0,
      "pan_slide_shape": 1,
      "pan_slide_curve": 0,
      "attack": 0,
      "decay": 0,
      "sustain": 0,
      "release": 1,
      "attack_level": 1,
      "decay_level": 1,
      "sustain_level": 1,
      "env_curve": 2
    },
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false,
    "name": ":dull_bell",
    "summary": "Dull Bell",
    "hidden": false
  },
  "PrettyBell": {
    "opts": {
      "note": 52,
      "note_slide": 0,
      "note_slide_shape": 1,
      "note_slide_curve": 0,
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "pan": 0,
      "pan_slide": 0,
      "pan_slide_shape": 1,
      "pan_slide_curve": 0,
      "attack": 0,
      "decay": 0,
      "sustain": 0,
      "release": 1,
      "attack_level": 1,
      "decay_level": 1,
      "sustain_level": 1,
      "env_curve": 2
    },
    "inherit_base": "DullBell",
    "inherit_arg": true,
    "name": ":pretty_bell",
    "summary": "Pretty Bell",
    "hidden": true
  },
  "Beep": {
    "opts": {
      "note": 52,
      "note_slide": 0,
      "note_slide_shape": 1,
      "note_slide_curve": 0,
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "pan": 0,
      "pan_slide": 0,
      "pan_slide_shape": 1,
      "pan_slide_curve": 0,
      "attack": 0,
      "decay": 0,
      "sustain": 0,
      "release": 1,
      "attack_level": 1,
      "decay_level": 1,
      "sustain_level": 1,
      "env_curve": 2
    },
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false,
    "name": ":beep",
    "summary": "Sine Wave",
    "hidden": false
  },
  "Saw": {
    "opts": {
      "note": 52,
      "note_slide": 0,
      "note_slide_shape": 1,
      "note_slide_curve": 0,
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "pan": 0,
      "pan_slide": 0,
      "pan_slide_shape": 1,
      "pan_slide_curve": 0,
      "attack": 0,
      "decay": 0,
      "sustain": 0,
      "release": 1,
      "attack_level": 1,
      "decay_level": 1,
      "sustain_level": 1,
      "env_curve": 2,
      "cutoff": 100,
      "cutoff_slide": 0,
      "cutoff_slide_shape": 1,
      "cutoff_slide_curve": 0
    },
    "inherit_base": "Beep",
    "inherit_arg": true,
    "name": ":saw",
    "summary": "Saw Wave",
    "hidden": true
  },
  "Square": {
    "opts": {
      "note": 52,
      "note_slide": 0,
      "note_slide_shape": 1,
      "note_slide_curve": 0,
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "pan": 0,
      "pan_slide": 0,
      "pan_slide_shape": 1,
      "pan_slide_curve": 0,
      "attack": 0,
      "decay": 0,
      "sustain": 0,
      "release": 1,
      "attack_level": 1,
      "decay_level": 1,
      "sustain_level": 1,
      "env_curve": 2,
      "cutoff": 100,
      "cutoff_slide": 0,
      "cutoff_slide_shape": 1,
      "cutoff_slide_curve": 0
    },
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false,
    "name": ":square",
    "summary": "Square Wave",
    "hidden": false
  },
  "Pulse": {
    "opts": {
      "note": 52,
      "note_slide": 0,
      "note_slide_shape": 1,
      "note_slide_curve": 0,
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "pan": 0,
      "pan_slide": 0,
      "pan_slide_shape": 1,
      "pan_slide_curve": 0,
      "attack": 0,
      "decay": 0,
      "sustain": 0,
      "release": 1,
      "attack_level": 1,
      "decay_level": 1,
      "sustain_level": 1,
      "env_curve": 2,
      "cutoff": 100,
      "cutoff_slide": 0,
      "cutoff_slide_shape": 1,
      "cutoff_slide_curve": 0,
      "pulse_width": 0.5,
      "pulse_width_slide": 0,
      "pulse_width_slide_shape": 1
    },
    "inherit_base": "Square",
    "inherit_arg": true,
    "name": ":pulse",
    "summary": "Pulse Wave",
    "hidden": true
  },
  "SubPulse": {
    "opts": {
      "note": 52,
      "note_slide": 0,
      "note_slide_shape": 1,
      "note_slide_curve": 0,
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "pan": 0,
      "pan_slide": 0,
      "pan_slide_shape": 1,
      "pan_slide_curve": 0,
      "attack": 0,
      "decay": 0,
      "sustain": 0,
      "release": 1,
      "attack_level": 1,
      "decay_level": 1,
      "sustain_level": 1,
      "env_curve": 2,
      "cutoff": 100,
      "cutoff_slide": 0,
      "cutoff_slide_shape": 1,
      "cutoff_slide_curve": 0,
      "pulse_width": 0.5,
      "pulse_width_slide": 0,
      "pulse_width_slide_shape": 1,
      "sub_amp": 1,
      "sub_amp_slide": 0,
      "sub_amp_slide_shape": 1,
      "sub_amp_slide_curve": 0,
      "sub_detune": -12,
      "sub_detune_slide": 0,
      "sub_detune_slide_shape": 1
    },
    "inherit_base": "Pulse",
    "inherit_arg": true,
    "name": ":subpulse",
    "summary": "Pulse Wave with sub",
    "hidden": true
  },
  "Tri": {
    "opts": {
      "note": 52,
      "note_slide": 0,
      "note_slide_shape": 1,
      "note_slide_curve": 0,
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "pan": 0,
      "pan_slide": 0,
      "pan_slide_shape": 1,
      "pan_slide_curve": 0,
      "attack": 0,
      "decay": 0,
      "sustain": 0,
      "release": 1,
      "attack_level": 1,
      "decay_level": 1,
      "sustain_level": 1,
      "env_curve": 2,
      "cutoff": 100,
      "cutoff_slide": 0,
      "cutoff_slide_shape": 1,
      "cutoff_slide_curve": 0,
      "pulse_width": 0.5,
      "pulse_width_slide": 0,
      "pulse_width_slide_shape": 1
    },
    "inherit_base": "Pulse",
    "inherit_arg": true,
    "name": ":tri",
    "summary": "Triangle Wave",
    "hidden": true
  },
  "DSaw": {
    "opts": {
      "note": 52,
      "note_slide": 0,
      "note_slide_shape": 1,
      "note_slide_curve": 0,
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "pan": 0,
      "pan_slide": 0,
      "pan_slide_shape": 1,
      "pan_slide_curve": 0,
      "attack": 0,
      "decay": 0,
      "sustain": 0,
      "release": 1,
      "attack_level": 1,
      "decay_level": 1,
      "sustain_level": 1,
      "env_curve": 2,
      "cutoff": 100,
      "cutoff_slide": 0,
      "cutoff_slide_shape": 1,
      "cutoff_slide_curve": 0,
      "detune": 0.1,
      "detune_slide": 0,
      "detune_slide_shape": 1,
      "detune_slide_curve": 0
    },
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false,
    "name": ":dsaw",
    "summary": "Detuned Saw wave",
    "hidden": false
  },
  "DTri": {
    "opts": {
      "note": 52,
      "note_slide": 0,
      "note_slide_shape": 1,
      "note_slide_curve": 0,
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "pan": 0,
      "pan_slide": 0,
      "pan_slide_shape": 1,
      "pan_slide_curve": 0,
      "attack": 0,
      "decay": 0,
      "sustain": 0,
      "release": 1,
      "attack_level": 1,
      "decay_level": 1,
      "sustain_level": 1,
      "env_curve": 2,
      "cutoff": 100,
      "cutoff_slide": 0,
      "cutoff_slide_shape": 1,
      "cutoff_slide_curve": 0,
      "detune": 0.1,
      "detune_slide": 0,
      "detune_slide_shape": 1,
      "detune_slide_curve": 0
    },
    "inherit_base": "DSaw",
    "inherit_arg": true,
    "name": ":dtri",
    "summary": "Detuned Triangle Wave",
    "hidden": true
  },
  "DPulse": {
    "opts": {
      "note": 52,
      "note_slide": 0,
      "note_slide_shape": 1,
      "note_slide_curve": 0,
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "pan": 0,
      "pan_slide": 0,
      "pan_slide_shape": 1,
      "pan_slide_curve": 0,
      "attack": 0,
      "decay": 0,
      "sustain": 0,
      "release": 1,
      "attack_level": 1,
      "decay_level": 1,
      "sustain_level": 1,
      "env_curve": 2,
      "cutoff": 100,
      "cutoff_slide": 0,
      "cutoff_slide_shape": 1,
      "cutoff_slide_curve": 0,
      "detune": 0.1,
      "detune_slide": 0,
      "detune_slide_shape": 1,
      "detune_slide_curve": 0,
      "pulse_width": 0.5,
      "pulse_width_slide": 0,
      "pulse_width_slide_shape": 1,
      "pulse_width_slide_curve": 0,
      "dpulse_width": 0,
      "dpulse_width_slide": 0,
      "dpulse_width_slide_shape": 1
    },
    "inherit_base": "DSaw",
    "inherit_arg": true,
    "name": ":dpulse",
    "summary": "Detuned Pulse Wave",
    "hidden": true
  },
  "FM": {
    "opts": {
      "note": 52,
      "note_slide": 0,
      "note_slide_shape": 1,
      "note_slide_curve": 0,
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "pan": 0,
      "pan_slide": 0,
      "pan_slide_shape": 1,
      "pan_slide_curve": 0,
      "attack": 0,
      "decay": 0,
      "sustain": 0,
      "release": 1,
      "attack_level": 1,
      "decay_level": 1,
      "sustain_level": 1,
      "env_curve": 2,
      "cutoff": 100,
      "cutoff_slide": 0,
      "cutoff_slide_shape": 1,
      "cutoff_slide_curve": 0,
      "divisor": 2,
      "divisor_slide": 0,
      "divisor_slide_shape": 1,
      "divisor_slide_curve": 0,
      "depth": 1,
      "depth_slide": 0,
      "depth_slide_shape": 1,
      "depth_slide_curve": 0
    },
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false,
    "name": ":fm",
    "summary": "Basic FM synthesis",
    "hidden": false
  },
  "ModFM": {
    "opts": {
      "note": 52,
      "note_slide": 0,
      "note_slide_shape": 1,
      "note_slide_curve": 0,
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "pan": 0,
      "pan_slide": 0,
      "pan_slide_shape": 1,
      "pan_slide_curve": 0,
      "attack": 0,
      "decay": 0,
      "sustain": 0,
      "release": 1,
      "attack_level": 1,
      "decay_level": 1,
      "sustain_level": 1,
      "env_curve": 2,
      "cutoff": 100,
      "cutoff_slide": 0,
      "cutoff_slide_shape": 1,
      "cutoff_slide_curve": 0,
      "divisor": 2,
      "divisor_slide": 0,
      "divisor_slide_shape": 1,
      "divisor_slide_curve": 0,
      "depth": 1,
      "depth_slide": 0,
      "depth_slide_shape": 1,
      "depth_slide_curve": 0,
      "mod_phase": 0.25,
      "mod_range": 5,
      "mod_pulse_width": 0.5,
      "mod_phase_offset": 0,
      "mod_invert_wave": 0,
      "mod_wave": 1
    },
    "inherit_base": "FM",
    "inherit_arg": true,
    "name": ":mod_fm",
    "summary": "Basic FM synthesis with frequency modulation.",
    "hidden": true
  },
  "ModSaw": {
    "opts": {
      "note": 52,
      "note_slide": 0,
      "note_slide_shape": 1,
      "note_slide_curve": 0,
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "pan": 0,
      "pan_slide": 0,
      "pan_slide_shape": 1,
      "pan_slide_curve": 0,
      "attack": 0,
      "decay": 0,
      "sustain": 0,
      "release": 1,
      "attack_level": 1,
      "decay_level": 1,
      "sustain_level": 1,
      "env_curve": 2,
      "cutoff": 100,
      "cutoff_slide": 0,
      "cutoff_slide_shape": 1,
      "cutoff_slide_curve": 0,
      "mod_phase": 0.25,
      "mod_phase_slide": 0,
      "mod_phase_slide_shape": 1,
      "mod_phase_slide_curve": 0,
      "mod_range": 5,
      "mod_range_slide": 0,
      "mod_range_slide_shape": 1,
      "mod_range_slide_curve": 0,
      "mod_pulse_width": 0.5,
      "mod_pulse_width_slide": 0,
      "mod_pulse_width_slide_shape": 1,
      "mod_pulse_width_slide_curve": 0,
      "mod_phase_offset": 0,
      "mod_invert_wave": 0,
      "mod_wave": 1
    },
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false,
    "name": ":mod_saw",
    "summary": "Modulated Saw Wave",
    "hidden": false
  },
  "ModDSaw": {
    "opts": {
      "note": 52,
      "note_slide": 0,
      "note_slide_shape": 1,
      "note_slide_curve": 0,
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "pan": 0,
      "pan_slide": 0,
      "pan_slide_shape": 1,
      "pan_slide_curve": 0,
      "attack": 0,
      "decay": 0,
      "sustain": 0,
      "release": 1,
      "attack_level": 1,
      "decay_level": 1,
      "sustain_level": 1,
      "env_curve": 2,
      "cutoff": 100,
      "cutoff_slide": 0,
      "cutoff_slide_shape": 1,
      "cutoff_slide_curve": 0,
      "mod_phase": 0.25,
      "mod_phase_slide": 0,
      "mod_phase_slide_shape": 1,
      "mod_phase_slide_curve": 0,
      "mod_range": 5,
      "mod_range_slide": 0,
      "mod_range_slide_shape": 1,
      "mod_range_slide_curve": 0,
      "mod_pulse_width": 0.5,
      "mod_pulse_width_slide": 0,
      "mod_pulse_width_slide_shape": 1,
      "mod_pulse_width_slide_curve": 0,
      "mod_phase_offset": 0,
      "mod_invert_wave": 0,
      "mod_wave": 1,
      "detune": 0.1,
      "detune_slide": 0,
      "detune_slide_shape": 1,
      "detune_slide_curve": 0
    },
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false,
    "name": ":mod_dsaw",
    "summary": "Modulated Detuned Saw Waves",
    "hidden": false
  },
  "ModSine": {
    "opts": {
      "note": 52,
      "note_slide": 0,
      "note_slide_shape": 1,
      "note_slide_curve": 0,
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "pan": 0,
      "pan_slide": 0,
      "pan_slide_shape": 1,
      "pan_slide_curve": 0,
      "attack": 0,
      "decay": 0,
      "sustain": 0,
      "release": 1,
      "attack_level": 1,
      "decay_level": 1,
      "sustain_level": 1,
      "env_curve": 2,
      "cutoff": 100,
      "cutoff_slide": 0,
      "cutoff_slide_shape": 1,
      "cutoff_slide_curve": 0,
      "mod_phase": 0.25,
      "mod_phase_slide": 0,
      "mod_phase_slide_shape": 1,
      "mod_phase_slide_curve": 0,
      "mod_range": 5,
      "mod_range_slide": 0,
      "mod_range_slide_shape": 1,
      "mod_range_slide_curve": 0,
      "mod_pulse_width": 0.5,
      "mod_pulse_width_slide": 0,
      "mod_pulse_width_slide_shape": 1,
      "mod_pulse_width_slide_curve": 0,
      "mod_phase_offset": 0,
      "mod_invert_wave": 0,
      "mod_wave": 1
    },
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false,
    "name": ":mod_sine",
    "summary": "Modulated Sine Wave",
    "hidden": false
  },
  "ModTri": {
    "opts": {
      "note": 52,
      "note_slide": 0,
      "note_slide_shape": 1,
      "note_slide_curve": 0,
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "pan": 0,
      "pan_slide": 0,
      "pan_slide_shape": 1,
      "pan_slide_curve": 0,
      "attack": 0,
      "decay": 0,
      "sustain": 0,
      "release": 1,
      "attack_level": 1,
      "decay_level": 1,
      "sustain_level": 1,
      "env_curve": 2,
      "cutoff": 100,
      "cutoff_slide": 0,
      "cutoff_slide_shape": 1,
      "cutoff_slide_curve": 0,
      "mod_phase": 0.25,
      "mod_phase_slide": 0,
      "mod_phase_slide_shape": 1,
      "mod_phase_slide_curve": 0,
      "mod_range": 5,
      "mod_range_slide": 0,
      "mod_range_slide_shape": 1,
      "mod_range_slide_curve": 0,
      "mod_pulse_width": 0.5,
      "mod_pulse_width_slide": 0,
      "mod_pulse_width_slide_shape": 1,
      "mod_pulse_width_slide_curve": 0,
      "mod_phase_offset": 0,
      "mod_invert_wave": 0,
      "mod_wave": 1
    },
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false,
    "name": ":mod_tri",
    "summary": "Modulated Triangle Wave",
    "hidden": false
  },
  "ModPulse": {
    "opts": {
      "note": 52,
      "note_slide": 0,
      "note_slide_shape": 1,
      "note_slide_curve": 0,
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "pan": 0,
      "pan_slide": 0,
      "pan_slide_shape": 1,
      "pan_slide_curve": 0,
      "attack": 0,
      "decay": 0,
      "sustain": 0,
      "release": 1,
      "attack_level": 1,
      "decay_level": 1,
      "sustain_level": 1,
      "env_curve": 2,
      "cutoff": 100,
      "cutoff_slide": 0,
      "cutoff_slide_shape": 1,
      "cutoff_slide_curve": 0,
      "mod_phase": 0.25,
      "mod_phase_slide": 0,
      "mod_phase_slide_shape": 1,
      "mod_phase_slide_curve": 0,
      "mod_range": 5,
      "mod_range_slide": 0,
      "mod_range_slide_shape": 1,
      "mod_range_slide_curve": 0,
      "mod_pulse_width": 0.5,
      "mod_pulse_width_slide": 0,
      "mod_pulse_width_slide_shape": 1,
      "mod_pulse_width_slide_curve": 0,
      "mod_phase_offset": 0,
      "mod_invert_wave": 0,
      "mod_wave": 1,
      "pulse_width": 0.5,
      "pulse_width_slide": 0,
      "pulse_width_slide_shape": 1,
      "pulse_width_slide_curve": 0
    },
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false,
    "name": ":mod_pulse",
    "summary": "Modulated Pulse",
    "hidden": false
  },
  "TB303": {
    "opts": {
      "note": 52,
      "note_slide": 0,
      "note_slide_shape": 1,
      "note_slide_curve": 0,
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "pan": 0,
      "pan_slide": 0,
      "pan_slide_shape": 1,
      "pan_slide_curve": 0,
      "attack": 0,
      "decay": 0,
      "sustain": 0,
      "release": 1,
      "attack_level": 1,
      "decay_level": 1,
      "sustain_level": 1,
      "env_curve": 2,
      "cutoff": 120,
      "cutoff_slide": 0,
      "cutoff_slide_shape": 1,
      "cutoff_slide_curve": 0,
      "cutoff_min": 30,
      "cutoff_min_slide": 0,
      "cutoff_min_slide_shape": 1,
      "cutoff_min_slide_curve": 0,
      "cutoff_attack": 0,
      "cutoff_decay": 0,
      "cutoff_sustain": 0,
      "cutoff_release": 1,
      "cutoff_attack_level": 1,
      "cutoff_decay_level": 1,
      "cutoff_sustain_level": 1,
      "res": 0.9,
      "res_slide": 0,
      "res_slide_shape": 1,
      "res_slide_curve": 0,
      "wave": 0,
      "pulse_width": 0.5,
      "pulse_width_slide": 0,
      "pulse_width_slide_shape": 1,
      "pulse_width_slide_curve": 0
    },
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false,
    "name": ":tb303",
    "summary": "TB-303 Emulation",
    "hidden": false
  },
  "Supersaw": {
    "opts": {
      "note": 52,
      "note_slide": 0,
      "note_slide_shape": 1,
      "note_slide_curve": 0,
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "pan": 0,
      "pan_slide": 0,
      "pan_slide_shape": 1,
      "pan_slide_curve": 0,
      "attack": 0,
      "decay": 0,
      "sustain": 0,
      "release": 1,
      "attack_level": 1,
      "decay_level": 1,
      "sustain_level": 1,
      "env_curve": 2,
      "cutoff": 130,
      "cutoff_slide": 0,
      "cutoff_slide_shape": 1,
      "cutoff_slide_curve": 0,
      "res": 0.7,
      "res_slide": 0,
      "res_slide_shape": 1,
      "res_slide_curve": 0
    },
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false,
    "name": ":supersaw",
    "summary": "Supersaw",
    "hidden": false
  },
  "Hoover": {
    "opts": {
      "note": 52,
      "note_slide": 0,
      "note_slide_shape": 1,
      "note_slide_curve": 0,
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "pan": 0,
      "pan_slide": 0,
      "pan_slide_shape": 1,
      "pan_slide_curve": 0,
      "attack": 0.05,
      "decay": 0,
      "sustain": 0,
      "release": 1,
      "attack_level": 1,
      "decay_level": 1,
      "sustain_level": 1,
      "env_curve": 2,
      "cutoff": 130,
      "cutoff_slide": 0,
      "cutoff_slide_shape": 1,
      "cutoff_slide_curve": 0,
      "res": 0.1,
      "res_slide": 0,
      "res_slide_shape": 1,
      "res_slide_curve": 0
    },
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false,
    "name": ":hoover",
    "summary": "Hoover",
    "hidden": false
  },
  "SynthViolin": {
    "opts": {
      "note": 52,
      "note_slide": 0,
      "note_slide_shape": 1,
      "note_slide_curve": 0,
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "pan": 0,
      "pan_slide": 0,
      "pan_slide_shape": 1,
      "pan_slide_curve": 0,
      "attack": 0,
      "decay": 0,
      "sustain": 0,
      "release": 1,
      "attack_level": 1,
      "decay_level": 1,
      "sustain_level": 1,
      "env_curve": 2,
      "cutoff": 100,
      "cutoff_slide": 0,
      "cutoff_slide_shape": 1,
      "cutoff_slide_curve": 0,
      "vibrato_rate": 6,
      "vibrato_rate_slide_shape": 1,
      "vibrato_rate_slide_curve": 0,
      "vibrato_depth": 0.15,
      "vibrato_depth_slide_shape": 1,
      "vibrato_depth_slide_curve": 0,
      "vibrato_delay": 0.5,
      "vibrato_onset": 0.1
    },
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false,
    "name": ":blade",
    "summary": "Blade Runner style strings",
    "hidden": false
  },
  "SynthPluck": {
    "opts": {
      "note": 52,
      "note_slide": 0,
      "note_slide_shape": 1,
      "note_slide_curve": 0,
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "pan": 0,
      "pan_slide": 0,
      "pan_slide_shape": 1,
      "pan_slide_curve": 0,
      "attack": 0,
      "sustain": 0,
      "release": 1,
      "attack_level": 1,
      "decay": 0,
      "decay_level": 1,
      "sustain_level": 1,
      "noise_amp": 0.8,
      "max_delay_time": 0.125,
      "pluck_decay": 30,
      "coef": 0.3
    },
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false,
    "name": ":pluck",
    "summary": "SynthPluck",
    "hidden": false
  },
  "SynthKalimba": {
    "opts": {
      "note": 52,
      "note_slide": 0,
      "note_slide_shape": 1,
      "note_slide_curve": 0,
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "pan": 0,
      "pan_slide": 0,
      "pan_slide_shape": 1,
      "pan_slide_curve": 0,
      "attack": 0,
      "decay": 0,
      "sustain": 4,
      "release": 1,
      "attack_level": 1,
      "decay_level": 1,
      "sustain_level": 1,
      "clickiness": 0.1
    },
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false,
    "name": ":kalimba",
    "summary": "SynthKalimba",
    "hidden": false
  },
  "SynthRodeo": {
    "opts": {
      "note": 52,
      "note_slide": 0,
      "note_slide_shape": 1,
      "note_slide_curve": 0,
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "pan": 0,
      "pan_slide": 0,
      "pan_slide_shape": 1,
      "pan_slide_curve": 0,
      "attack": 0,
      "decay": 1,
      "sustain": 0.8,
      "release": 1,
      "attack_level": 1,
      "decay_level": 1,
      "sustain_level": 1,
      "use_chorus": 1,
      "use_compressor": 1,
      "cutoff": 72,
      "cutoff_slide": 0,
      "cutoff_slide_shape": 1,
      "cutoff_slide_curve": 0
    },
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false,
    "name": ":rodeo",
    "summary": "SynthRodeo",
    "hidden": false
  },
  "SynthPiano": {
    "opts": {
      "note": 52,
      "note_slide": 0,
      "note_slide_shape": 1,
      "note_slide_curve": 0,
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "pan": 0,
      "pan_slide": 0,
      "pan_slide_shape": 1,
      "pan_slide_curve": 0,
      "vel": 0.2,
      "attack": 0,
      "decay": 0,
      "sustain": 0,
      "release": 1,
      "attack_level": 1,
      "decay_level": 1,
      "sustain_level": 1,
      "hard": 0.5,
      "stereo_width": 0
    },
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false,
    "name": ":piano",
    "summary": "SynthPiano",
    "hidden": false
  },
  "Growl": {
    "opts": {
      "note": 52,
      "note_slide": 0,
      "note_slide_shape": 1,
      "note_slide_curve": 0,
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "pan": 0,
      "pan_slide": 0,
      "pan_slide_shape": 1,
      "pan_slide_curve": 0,
      "attack": 0.1,
      "decay": 0,
      "sustain": 0,
      "release": 1,
      "attack_level": 1,
      "decay_level": 1,
      "sustain_level": 1,
      "env_curve": 2,
      "cutoff": 130,
      "cutoff_slide": 0,
      "cutoff_slide_shape": 1,
      "cutoff_slide_curve": 0,
      "res": 0.7,
      "res_slide": 0,
      "res_slide_shape": 1,
      "res_slide_curve": 0
    },
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false,
    "name": ":growl",
    "summary": "Growl",
    "hidden": false
  },
  "DarkAmbience": {
    "opts": {
      "note": 52,
      "note_slide": 0,
      "note_slide_shape": 1,
      "note_slide_curve": 0,
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "pan": 0,
      "pan_slide": 0,
      "pan_slide_shape": 1,
      "pan_slide_curve": 0,
      "attack": 0,
      "decay": 0,
      "sustain": 0,
      "release": 1,
      "attack_level": 1,
      "decay_level": 1,
      "sustain_level": 1,
      "env_curve": 2,
      "cutoff": 110,
      "cutoff_slide": 0,
      "cutoff_slide_shape": 1,
      "cutoff_slide_curve": 0,
      "res": 0.7,
      "res_slide": 0,
      "res_slide_shape": 1,
      "res_slide_curve": 0,
      "detune1": 12,
      "detune1_slide": 0,
      "detune1_slide_shape": 1,
      "detune1_slide_curve": 0,
      "detune2": 24,
      "detune2_slide": 0,
      "detune2_slide_shape": 1,
      "detune2_slide_curve": 0,
      "noise": 0,
      "ring": 0.2,
      "room": 70,
      "reverb_time": 100
    },
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false,
    "name": ":dark_ambience",
    "summary": "Dark Ambience",
    "hidden": false
  },
  "DarkSeaHorn": {
    "opts": {
      "note": 52,
      "note_slide": 0,
      "note_slide_shape": 1,
      "note_slide_curve": 0,
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "pan": 0,
      "pan_slide": 0,
      "pan_slide_shape": 1,
      "pan_slide_curve": 0,
      "attack": 1,
      "decay": 0,
      "sustain": 0,
      "release": 4.0,
      "attack_level": 1,
      "decay_level": 1,
      "sustain_level": 1,
      "env_curve": 2
    },
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false,
    "name": ":dark_sea_horn",
    "summary": "Dark Sea Horn",
    "hidden": true
  },
  "Singer": {
    "opts": {
      "note": 52,
      "note_slide": 0,
      "note_slide_shape": 1,
      "note_slide_curve": 0,
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "pan": 0,
      "pan_slide": 0,
      "pan_slide_shape": 1,
      "pan_slide_curve": 0,
      "attack": 1,
      "decay": 0,
      "sustain": 0,
      "release": 4.0,
      "attack_level": 1,
      "decay_level": 1,
      "sustain_level": 1,
      "env_curve": 2
    },
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false,
    "name": ":singer",
    "summary": "Singer",
    "hidden": true
  },
  "Hollow": {
    "opts": {
      "note": 52,
      "note_slide": 0,
      "note_slide_shape": 1,
      "note_slide_curve": 0,
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "pan": 0,
      "pan_slide": 0,
      "pan_slide_shape": 1,
      "pan_slide_curve": 0,
      "attack": 0,
      "decay": 0,
      "sustain": 0,
      "release": 1,
      "attack_level": 1,
      "decay_level": 1,
      "sustain_level": 1,
      "env_curve": 2,
      "cutoff": 90,
      "cutoff_slide": 0,
      "cutoff_slide_shape": 1,
      "cutoff_slide_curve": 0,
      "res": 0.99,
      "res_slide": 0,
      "res_slide_shape": 1,
      "res_slide_curve": 0,
      "noise": 1,
      "norm": 0
    },
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false,
    "name": ":hollow",
    "summary": "Hollow",
    "hidden": false
  },
  "Zawa": {
    "opts": {
      "note": 52,
      "note_slide": 0,
      "note_slide_shape": 1,
      "note_slide_curve": 0,
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "pan": 0,
      "pan_slide": 0,
      "pan_slide_shape": 1,
      "pan_slide_curve": 0,
      "attack": 0,
      "decay": 0,
      "sustain": 0,
      "release": 1,
      "attack_level": 1,
      "decay_level": 1,
      "sustain_level": 1,
      "cutoff": 100,
      "cutoff_slide": 0,
      "cutoff_slide_shape": 1,
      "cutoff_slide_curve": 0,
      "res": 0.9,
      "res_slide": 0,
      "res_slide_shape": 1,
      "res_slide_curve": 0,
      "phase": 1,
      "phase_slide": 0,
      "phase_slide_shape": 1,
      "phase_slide_curve": 0,
      "phase_offset": 0,
      "wave": 3,
      "invert_wave": 0,
      "range": 24,
      "range_slide": 0,
      "range_slide_shape": 1,
      "range_slide_curve": 0,
      "disable_wave": 0,
      "pulse_width": 0.5,
      "pulse_width_slide": 0,
      "pulse_width_slide_shape": 1,
      "pulse_width_slide_curve": 0
    },
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false,
    "name": ":zawa",
    "summary": "Zawa",
    "hidden": false
  },
  "Prophet": {
    "opts": {
      "note": 52,
      "note_slide": 0,
      "note_slide_shape": 1,
      "note_slide_curve": 0,
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "pan": 0,
      "pan_slide": 0,
      "pan_slide_shape": 1,
      "pan_slide_curve": 0,
      "attack": 0,
      "decay": 0,
      "sustain": 0,
      "release": 1,
      "attack_level": 1,
      "decay_level": 1,
      "sustain_level": 1,
      "env_curve": 2,
      "cutoff": 110,
      "cutoff_slide": 0,
      "cutoff_slide_shape": 1,
      "cutoff_slide_curve": 0,
      "res": 0.7,
      "res_slide": 0,
      "res_slide_shape": 1,
      "res_slide_curve": 0
    },
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false,
    "name": ":prophet",
    "summary": "The Prophet",
    "hidden": false
  },
  "ChipLead": {
    "opts": {
      "note": 60,
      "note_slide": 0,
      "note_slide_shape": 1,
      "note_slide_curve": 0,
      "note_resolution": 0.1,
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "pan": 0,
      "pan_slide": 0,
      "pan_slide_shape": 1,
      "pan_slide_curve": 0,
      "attack": 0,
      "decay": 0,
      "sustain": 0,
      "release": 1,
      "attack_level": 1,
      "decay_level": 1,
      "sustain_level": 1,
      "env_curve": 2,
      "width": 0
    },
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false,
    "name": ":chiplead",
    "summary": "Chip Lead",
    "hidden": false
  },
  "ChipBass": {
    "opts": {
      "note": 60,
      "note_slide": 0,
      "note_slide_shape": 1,
      "note_slide_curve": 0,
      "note_resolution": 0.1,
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "pan": 0,
      "pan_slide": 0,
      "pan_slide_shape": 1,
      "pan_slide_curve": 0,
      "attack": 0,
      "decay": 0,
      "sustain": 0,
      "release": 1,
      "attack_level": 1,
      "decay_level": 1,
      "sustain_level": 1,
      "env_curve": 2
    },
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false,
    "name": ":chipbass",
    "summary": "Chip Bass",
    "hidden": false
  },
  "Pitchless": {
    "opts": {},
    "inherit_base": "SonicPiSynth",
    "inherit_arg": true,
    "hidden": true
  },
  "Noise": {
    "opts": {
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "pan": 0,
      "pan_slide": 0,
      "pan_slide_shape": 1,
      "pan_slide_curve": 0,
      "attack": 0,
      "decay": 0,
      "sustain": 0,
      "release": 1,
      "attack_level": 1,
      "decay_level": 1,
      "sustain_level": 1,
      "env_curve": 2,
      "cutoff": 110,
      "cutoff_slide": 0,
      "cutoff_slide_shape": 1,
      "cutoff_slide_curve": 0,
      "res": 0,
      "res_slide": 0,
      "res_slide_shape": 1,
      "res_slide_curve": 0
    },
    "inherit_base": "Pitchless",
    "inherit_arg": false,
    "name": ":noise",
    "summary": "Noise",
    "hidden": false
  },
  "GNoise": {
    "opts": {
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "pan": 0,
      "pan_slide": 0,
      "pan_slide_shape": 1,
      "pan_slide_curve": 0,
      "attack": 0,
      "decay": 0,
      "sustain": 0,
      "release": 1,
      "attack_level": 1,
      "decay_level": 1,
      "sustain_level": 1,
      "env_curve": 2,
      "cutoff": 110,
      "cutoff_slide": 0,
      "cutoff_slide_shape": 1,
      "cutoff_slide_curve": 0,
      "res": 0,
      "res_slide": 0,
      "res_slide_shape": 1,
      "res_slide_curve": 0
    },
    "inherit_base": "Noise",
    "inherit_arg": true,
    "name": ":gnoise",
    "summary": "Grey Noise",
    "hidden": true
  },
  "BNoise": {
    "opts": {
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "pan": 0,
      "pan_slide": 0,
      "pan_slide_shape": 1,
      "pan_slide_curve": 0,
      "attack": 0,
      "decay": 0,
      "sustain": 0,
      "release": 1,
      "attack_level": 1,
      "decay_level": 1,
      "sustain_level": 1,
      "env_curve": 2,
      "cutoff": 110,
      "cutoff_slide": 0,
      "cutoff_slide_shape": 1,
      "cutoff_slide_curve": 0,
      "res": 0,
      "res_slide": 0,
      "res_slide_shape": 1,
      "res_slide_curve": 0
    },
    "inherit_base": "Noise",
    "inherit_arg": true,
    "name": ":bnoise",
    "summary": "Brown Noise",
    "hidden": true
  },
  "PNoise": {
    "opts": {
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "pan": 0,
      "pan_slide": 0,
      "pan_slide_shape": 1,
      "pan_slide_curve": 0,
      "attack": 0,
      "decay": 0,
      "sustain": 0,
      "release": 1,
      "attack_level": 1,
      "decay_level": 1,
      "sustain_level": 1,
      "env_curve": 2,
      "cutoff": 110,
      "cutoff_slide": 0,
      "cutoff_slide_shape": 1,
      "cutoff_slide_curve": 0,
      "res": 0,
      "res_slide": 0,
      "res_slide_shape": 1,
      "res_slide_curve": 0
    },
    "inherit_base": "Noise",
    "inherit_arg": true,
    "name": ":pnoise",
    "summary": "Pink Noise",
    "hidden": true
  },
  "CNoise": {
    "opts": {
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "pan": 0,
      "pan_slide": 0,
      "pan_slide_shape": 1,
      "pan_slide_curve": 0,
      "attack": 0,
      "decay": 0,
      "sustain": 0,
      "release": 1,
      "attack_level": 1,
      "decay_level": 1,
      "sustain_level": 1,
      "env_curve": 2,
      "cutoff": 110,
      "cutoff_slide": 0,
      "cutoff_slide_shape": 1,
      "cutoff_slide_curve": 0,
      "res": 0,
      "res_slide": 0,
      "res_slide_shape": 1,
      "res_slide_curve": 0
    },
    "inherit_base": "Noise",
    "inherit_arg": true,
    "name": ":cnoise",
    "summary": "Clip Noise",
    "hidden": true
  },
  "ChipNoise": {
    "opts": {
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 0,
      "amp_slide_curve": 1,
      "pan": 0,
      "pan_slide": 0,
      "pan_slide_shape": 1,
      "pan_slide_curve": 0,
      "attack": 0,
      "decay": 0,
      "sustain": 0,
      "release": 1,
      "attack_level": 1,
      "decay_level": 1,
      "sustain_level": 1,
      "env_curve": 0,
      "freq_band": 0,
      "freq_band_slide": 0,
      "freq_band_slide_shape": 1,
      "freq_band_slide_curve": 0
    },
    "inherit_base": "Noise",
    "inherit_arg": false,
    "name": ":chipnoise",
    "summary": "Chip Noise",
    "hidden": true
  },
  "TechSaws": {
    "opts": {
      "note": 52,
      "note_slide": 0,
      "note_slide_shape": 1,
      "note_slide_curve": 0,
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "pan": 0,
      "pan_slide": 0,
      "pan_slide_shape": 1,
      "pan_slide_curve": 0,
      "attack": 0,
      "decay": 0,
      "sustain": 0,
      "release": 1,
      "attack_level": 1,
      "decay_level": 1,
      "sustain_level": 1,
      "env_curve": 2,
      "cutoff": 130,
      "cutoff_slide": 0,
      "cutoff_slide_shape": 1,
      "cutoff_slide_curve": 0,
      "res": 0.7,
      "res_slide": 0,
      "res_slide_shape": 1,
      "res_slide_curve": 0
    },
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false,
    "name": ":tech_saws",
    "summary": "TechSaws",
    "hidden": false
  },
  "StudioInfo": {
    "opts": {},
    "inherit_base": "SonicPiSynth",
    "inherit_arg": true,
    "hidden": true
  },
  "BasicMonoPlayer": {
    "opts": {
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "pan": 0,
      "pan_slide": 0,
      "pan_slide_shape": 1,
      "pan_slide_curve": 0,
      "rate": 1,
      "lpf": -1,
      "lpf_slide": 0,
      "lpf_slide_shape": 1,
      "lpf_slide_curve": 0,
      "hpf": -1,
      "hpf_slide": 0,
      "hpf_slide_shape": 1,
      "hpf_slide_curve": 0
    },
    "inherit_base": "StudioInfo",
    "inherit_arg": false,
    "name": ":basic_mono_player",
    "summary": "Basic Mono Sample Player (no env)",
    "hidden": true
  },
  "BasicStereoPlayer": {
    "opts": {
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "pan": 0,
      "pan_slide": 0,
      "pan_slide_shape": 1,
      "pan_slide_curve": 0,
      "rate": 1,
      "lpf": -1,
      "lpf_slide": 0,
      "lpf_slide_shape": 1,
      "lpf_slide_curve": 0,
      "hpf": -1,
      "hpf_slide": 0,
      "hpf_slide_shape": 1,
      "hpf_slide_curve": 0
    },
    "inherit_base": "BasicMonoPlayer",
    "inherit_arg": true,
    "name": ":basic_stereo_player",
    "summary": "Basic Stereo Sample Player (no env)",
    "hidden": true
  },
  "MonoPlayer": {
    "opts": {
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "pre_amp": 1,
      "pre_amp_slide": 0,
      "pre_amp_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "pan": 0,
      "pan_slide": 0,
      "pan_slide_shape": 1,
      "pan_slide_curve": 0,
      "attack": 0,
      "decay": 0,
      "sustain": -1,
      "release": 0,
      "lpf": -1,
      "lpf_slide": 0,
      "lpf_slide_shape": 1,
      "lpf_slide_curve": 0,
      "lpf_attack": 0,
      "lpf_decay": 0,
      "lpf_sustain": -1,
      "lpf_release": 0,
      "lpf_init_level": -1,
      "lpf_attack_level": -1,
      "lpf_decay_level": -1,
      "lpf_sustain_level": -1,
      "lpf_release_level": -1,
      "lpf_env_curve": 2,
      "lpf_min": -1,
      "lpf_min_slide": 0,
      "lpf_min_slide_shape": 1,
      "lpf_min_slide_curve": 0,
      "hpf": -1,
      "hpf_slide": 0,
      "hpf_slide_shape": 1,
      "hpf_slide_curve": 0,
      "hpf_attack": 0,
      "hpf_sustain": -1,
      "hpf_decay": 0,
      "hpf_release": 0,
      "hpf_init_level": -1,
      "hpf_attack_level": -1,
      "hpf_decay_level": -1,
      "hpf_sustain_level": -1,
      "hpf_release_level": -1,
      "hpf_env_curve": 2,
      "hpf_max": -1,
      "hpf_max_slide": 0,
      "hpf_max_slide_shape": 1,
      "hpf_max_slide_curve": 0,
      "attack_level": 1,
      "decay_level": 1,
      "sustain_level": 1,
      "env_curve": 2,
      "rate": 1,
      "start": 0,
      "finish": 1,
      "norm": 0,
      "pitch": 0,
      "pitch_slide": 0,
      "pitch_slide_shape": 1,
      "pitch_slide_curve": 0,
      "window_size": 0.2,
      "window_size_slide": 0,
      "window_size_slide_shape": 1,
      "window_size_slide_curve": 0,
      "pitch_dis": 0.0,
      "pitch_dis_slide": 0,
      "pitch_dis_slide_shape": 1,
      "pitch_dis_slide_curve": 0,
      "time_dis": 0.0,
      "time_dis_slide": 0,
      "time_dis_slide_shape": 1,
      "time_dis_slide_curve": 0,
      "compress": 0,
      "threshold": 0.2,
      "threshold_slide": 0,
      "threshold_slide_shape": 1,
      "threshold_slide_curve": 0,
      "clamp_time": 0.01,
      "clamp_time_slide": 0,
      "clamp_time_slide_shape": 1,
      "clamp_time_slide_curve": 0,
      "slope_above": 0.5,
      "slope_above_slide": 0,
      "slope_above_slide_shape": 1,
      "slope_above_slide_curve": 0,
      "slope_below": 1,
      "slope_below_slide": 0,
      "slope_below_slide_shape": 1,
      "slope_below_slide_curve": 0,
      "relax_time": 0.01,
      "relax_time_slide": 0,
      "relax_time_slide_shape": 1,
      "relax_time_slide_curve": 0
    },
    "inherit_base": "BasicMonoPlayer",
    "inherit_arg": false,
    "name": ":mono_player",
    "summary": "Mono Sample Player",
    "hidden": true
  },
  "StereoPlayer": {
    "opts": {
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "pre_amp": 1,
      "pre_amp_slide": 0,
      "pre_amp_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "pan": 0,
      "pan_slide": 0,
      "pan_slide_shape": 1,
      "pan_slide_curve": 0,
      "attack": 0,
      "decay": 0,
      "sustain": -1,
      "release": 0,
      "lpf": -1,
      "lpf_slide": 0,
      "lpf_slide_shape": 1,
      "lpf_slide_curve": 0,
      "lpf_attack": 0,
      "lpf_decay": 0,
      "lpf_sustain": -1,
      "lpf_release": 0,
      "lpf_init_level": -1,
      "lpf_attack_level": -1,
      "lpf_decay_level": -1,
      "lpf_sustain_level": -1,
      "lpf_release_level": -1,
      "lpf_env_curve": 2,
      "lpf_min": -1,
      "lpf_min_slide": 0,
      "lpf_min_slide_shape": 1,
      "lpf_min_slide_curve": 0,
      "hpf": -1,
      "hpf_slide": 0,
      "hpf_slide_shape": 1,
      "hpf_slide_curve": 0,
      "hpf_attack": 0,
      "hpf_sustain": -1,
      "hpf_decay": 0,
      "hpf_release": 0,
      "hpf_init_level": -1,
      "hpf_attack_level": -1,
      "hpf_decay_level": -1,
      "hpf_sustain_level": -1,
      "hpf_release_level": -1,
      "hpf_env_curve": 2,
      "hpf_max": -1,
      "hpf_max_slide": 0,
      "hpf_max_slide_shape": 1,
      "hpf_max_slide_curve": 0,
      "attack_level": 1,
      "decay_level": 1,
      "sustain_level": 1,
      "env_curve": 2,
      "rate": 1,
      "start": 0,
      "finish": 1,
      "norm": 0,
      "pitch": 0,
      "pitch_slide": 0,
      "pitch_slide_shape": 1,
      "pitch_slide_curve": 0,
      "window_size": 0.2,
      "window_size_slide": 0,
      "window_size_slide_shape": 1,
      "window_size_slide_curve": 0,
      "pitch_dis": 0.0,
      "pitch_dis_slide": 0,
      "pitch_dis_slide_shape": 1,
      "pitch_dis_slide_curve": 0,
      "time_dis": 0.0,
      "time_dis_slide": 0,
      "time_dis_slide_shape": 1,
      "time_dis_slide_curve": 0,
      "compress": 0,
      "threshold": 0.2,
      "threshold_slide": 0,
      "threshold_slide_shape": 1,
      "threshold_slide_curve": 0,
      "clamp_time": 0.01,
      "clamp_time_slide": 0,
      "clamp_time_slide_shape": 1,
      "clamp_time_slide_curve": 0,
      "slope_above": 0.5,
      "slope_above_slide": 0,
      "slope_above_slide_shape": 1,
      "slope_above_slide_curve": 0,
      "slope_below": 1,
      "slope_below_slide": 0,
      "slope_below_slide_shape": 1,
      "slope_below_slide_curve": 0,
      "relax_time": 0.01,
      "relax_time_slide": 0,
      "relax_time_slide_shape": 1,
      "relax_time_slide_curve": 0
    },
    "inherit_base": "MonoPlayer",
    "inherit_arg": true,
    "name": ":stereo_player",
    "summary": "Stereo Sample Player",
    "hidden": true
  },
  "BaseMixer": {
    "opts": {},
    "inherit_base": "StudioInfo",
    "inherit_arg": true,
    "hidden": true
  },
  "BasicMixer": {
    "opts": {
      "amp": 1,
      "amp_slide": 0.1,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0
    },
    "inherit_base": "BaseMixer",
    "inherit_arg": false,
    "name": ":basic_mixer",
    "summary": "Basic Mixer",
    "hidden": true
  },
  "MainMixer": {
    "opts": {
      "amp_slide": 0.02,
      "pre_amp_slide": 0.02,
      "hpf_slide": 0.02,
      "lpf_slide": 0.02,
      "pre_amp": 1,
      "pre_amp_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "amp": 1,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "hpf": 0,
      "hpf_bypass": 0,
      "hpf_slide_shape": 1,
      "hpf_slide_curve": 0,
      "lpf": 135.5,
      "lpf_bypass": 0,
      "lpf_slide_shape": 1,
      "lpf_slide_curve": 0,
      "force_mono": 0,
      "invert_stereo": 0,
      "limiter_bypass": 0
    },
    "inherit_base": "BaseMixer",
    "inherit_arg": false,
    "name": ":mixer",
    "summary": "Main Mixer",
    "hidden": true
  }
}

synth_nodes = {
  ":dull_bell": "DullBell",
  ":pretty_bell": "PrettyBell",
  ":beep": "Beep",
  ":sine": "Beep",
  ":saw": "Saw",
  ":pulse": "Pulse",
  ":subpulse": "SubPulse",
  ":square": "Square",
  ":tri": "Tri",
  ":dsaw": "DSaw",
  ":dpulse": "DPulse",
  ":dtri": "DTri",
  ":fm": "FM",
  ":mod_fm": "ModFM",
  ":mod_saw": "ModSaw",
  ":mod_dsaw": "ModDSaw",
  ":mod_sine": "ModSine",
  ":mod_beep": "ModSine",
  ":mod_tri": "ModTri",
  ":mod_pulse": "ModPulse",
  ":chiplead": "ChipLead",
  ":chipbass": "ChipBass",
  ":tb303": "TB303",
  ":supersaw": "Supersaw",
  ":hoover": "Hoover",
  ":prophet": "Prophet",
  ":zawa": "Zawa",
  ":dark_ambience": "DarkAmbience",
  ":growl": "Growl",
  ":hollow": "Hollow",
  ":mono_player": "MonoPlayer",
  ":stereo_player": "StereoPlayer",
  ":blade": "SynthViolin",
  ":piano": "SynthPiano",
  ":rodeo": "SynthRodeo",
  ":kalimba": "SynthKalimba",
  ":pluck": "SynthPluck",
  ":tech_saws": "TechSaws",
  ":sound_in": "SoundIn",
  ":sound_in_stereo": "SoundInStereo",
  ":noise": "Noise",
  ":pnoise": "PNoise",
  ":bnoise": "BNoise",
  ":gnoise": "GNoise",
  ":cnoise": "CNoise",
  ":chipnoise": "ChipNoise",
  ":basic_mono_player": "BasicMonoPlayer",
  ":basic_stereo_player": "BasicStereoPlayer",
  ":basic_mixer": "BasicMixer",
  ":main_mixer": "MainMixer",
  ":fx_bitcrusher": "FXBitcrusher",
  ":fx_krush": "FXKrush",
  ":fx_reverb": "FXReverb",
  ":fx_gverb": "FXGVerb",
  ":fx_replace_reverb": "FXReverb",
  ":fx_level": "FXLevel",
  ":fx_mono": "FXMono",
  ":fx_autotuner": "FXAutotuner",
  ":fx_replace_level": "FXLevel",
  ":fx_echo": "FXEcho",
  ":fx_replace_echo": "FXEcho",
  ":fx_slicer": "FXSlicer",
  ":fx_panslicer": "FXPanSlicer",
  ":fx_replace_slicer": "FXSlicer",
  ":fx_wobble": "FXWobble",
  ":fx_replace_wobble": "FXWobble",
  ":fx_ixi_techno": "FXIXITechno",
  ":fx_replace_ixi_techno": "FXIXITechno",
  ":fx_compressor": "FXCompressor",
  ":fx_whammy": "FXWhammy",
  ":fx_replace_compressor": "FXCompressor",
  ":fx_rlpf": "FXRLPF",
  ":fx_replace_rlpf": "FXRLPF",
  ":fx_nrlpf": "FXNormRLPF",
  ":fx_replace_nrlpf": "FXNormRLPF",
  ":fx_rhpf": "FXRHPF",
  ":fx_replace_rhpf": "FXRHPF",
  ":fx_nrhpf": "FXNormRHPF",
  ":fx_replace_nrhpf": "FXNormRHPF",
  ":fx_hpf": "FXHPF",
  ":fx_replace_hpf": "FXHPF",
  ":fx_nhpf": "FXNormHPF",
  ":fx_replace_nhpf": "FXNormHPF",
  ":fx_lpf": "FXLPF",
  ":fx_replace_lpf": "FXLPF",
  ":fx_nlpf": "FXNormLPF",
  ":fx_replace_nlpf": "FXNormLPF",
  ":fx_normaliser": "FXNormaliser",
  ":fx_replace_normaliser": "FXNormaliser",
  ":fx_distortion": "FXDistortion",
  ":fx_replace_distortion": "FXDistortion",
  ":fx_pan": "FXPan",
  ":fx_replace_pan": "FXPan",
  ":fx_bpf": "FXBPF",
  ":fx_nbpf": "FXNBPF",
  ":fx_rbpf": "FXRBPF",
  ":fx_nrbpf": "FXNRBPF",
  ":fx_band_eq": "FXBandEQ",
  ":fx_tanh": "FXTanh",
  ":fx_pitch_shift": "FXPitchShift",
  ":fx_ring_mod": "FXRingMod",
  ":fx_octaver": "FXOctaver",
  ":fx_vowel": "FXVowel",
  ":fx_flanger": "FXFlanger",
  ":fx_eq": "FXEQ",
  ":fx_tremolo": "FXTremolo",
  ":fx_record": "FXRecord",
  ":fx_sound_out": "FXSoundOut",
  ":fx_sound_out_stereo": "FXSoundOutStereo",
  ":fx_ping_pong": "FXPingPong"
}

fx = {
  "FXInfo": {
    "opts": {
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "mix": 1,
      "mix_slide": 0,
      "mix_slide_shape": 1,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "pre_mix_slide": 0,
      "pre_mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_amp": 1,
      "pre_amp_slide": 0,
      "pre_amp_slide_shape": 1,
      "pre_amp_slide_curve": 0
    },
    "inherit_base": "BaseInfo",
    "inherit_arg": false,
    "hidden": true
  },
  "FXRecord": {
    "opts": {
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "mix": 1,
      "mix_slide": 0,
      "mix_slide_shape": 1,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "pre_mix_slide": 0,
      "pre_mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_amp": 1,
      "pre_amp_slide": 0,
      "pre_amp_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "buffer": "nil"
    },
    "inherit_base": "FXInfo",
    "inherit_arg": false,
    "name": ":record",
    "summary": "Record",
    "hidden": false
  },
  "FXSoundOut": {
    "opts": {
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "mix": 1,
      "mix_slide": 0,
      "mix_slide_shape": 1,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "pre_mix_slide": 0,
      "pre_mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_amp": 1,
      "pre_amp_slide": 0,
      "pre_amp_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "output": 1,
      "mode": 0
    },
    "inherit_base": "FXInfo",
    "inherit_arg": true,
    "name": ":sound_out",
    "summary": "Sound Out",
    "hidden": false
  },
  "FXSoundOutStereo": {
    "opts": {
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "mix": 1,
      "mix_slide": 0,
      "mix_slide_shape": 1,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "pre_mix_slide": 0,
      "pre_mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_amp": 1,
      "pre_amp_slide": 0,
      "pre_amp_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "output": 1,
      "mode": 0
    },
    "inherit_base": "FXInfo",
    "inherit_arg": true,
    "name": ":sound_out_stereo",
    "summary": "Sound Out Stereo",
    "hidden": false
  },
  "FXEQ": {
    "opts": {
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "mix": 1,
      "mix_slide": 0,
      "mix_slide_shape": 1,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "pre_mix_slide": 0,
      "pre_mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_amp": 1,
      "pre_amp_slide": 0,
      "pre_amp_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "low_shelf": 0,
      "low_shelf_slide": 0,
      "low_shelf_slide_shape": 1,
      "low_shelf_slide_curve": 0,
      "low_shelf_note": 43.349957,
      "low_shelf_note_slide": 0,
      "low_shelf_note_slide_shape": 1,
      "low_shelf_note_slide_curve": 0,
      "low_shelf_slope": 1,
      "low_shelf_slope_slide": 0,
      "low_shelf_slope_slide_shape": 1,
      "low_shelf_slope_slide_curve": 0,
      "low": 0,
      "low_slide": 0,
      "low_slide_shape": 1,
      "low_slide_curve": 0,
      "low_note": 59.2130948,
      "low_note_slide": 0,
      "low_note_slide_shape": 1,
      "low_note_slide_curve": 0,
      "low_q": 0.6,
      "low_q_slide": 0,
      "low_q_slide_shape": 1,
      "low_q_slide_curve": 0,
      "mid": 0,
      "mid_slide": 0,
      "mid_slide_shape": 1,
      "mid_slide_curve": 0,
      "mid_note": 83.2130948,
      "mid_note_slide": 0,
      "mid_note_slide_shape": 1,
      "mid_note_slide_curve": 0,
      "mid_q": 0.6,
      "mid_q_slide": 0,
      "mid_q_slide_shape": 1,
      "mid_q_slide_curve": 0,
      "high": 0,
      "high_slide": 0,
      "high_slide_shape": 1,
      "high_slide_curve": 0,
      "high_note": 104.9013539,
      "high_note_slide": 0,
      "high_note_slide_shape": 1,
      "high_note_slide_curve": 0,
      "high_q": 0.6,
      "high_q_slide": 0,
      "high_q_slide_shape": 1,
      "high_q_slide_curve": 0,
      "high_shelf": 0,
      "high_shelf_slide": 0,
      "high_shelf_slide_shape": 1,
      "high_shelf_slide_curve": 0,
      "high_shelf_note": 114.2326448,
      "high_shelf_note_slide": 0,
      "high_shelf_note_slide_shape": 1,
      "high_shelf_note_slide_curve": 0,
      "high_shelf_slope": 1,
      "high_shelf_slope_slide": 0,
      "high_shelf_slope_slide_shape": 1,
      "high_shelf_slope_slide_curve": 0
    },
    "inherit_base": "FXInfo",
    "inherit_arg": true,
    "name": ":eq",
    "summary": "EQ",
    "hidden": false
  },
  "FXGVerb": {
    "opts": {
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "mix": 1,
      "mix_slide": 0,
      "mix_slide_shape": 1,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "pre_mix_slide": 0,
      "pre_mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_amp": 1,
      "pre_amp_slide": 0,
      "pre_amp_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "spread": 0.5,
      "spread_slide": 0,
      "spread_slide_shape": 1,
      "spread_slide_curve": 0,
      "damp": 0.5,
      "damp_slide": 0,
      "damp_slide_shape": 1,
      "damp_slide_curve": 0,
      "pre_damp": 0.5,
      "pre_damp_slide": 0,
      "pre_damp_slide_shape": 1,
      "pre_damp_slide_curve": 0,
      "dry": 1,
      "dry_slide": 0,
      "dry_slide_shape": 1,
      "dry_slide_curve": 0,
      "room": 10,
      "release": 3,
      "ref_level": 0.7,
      "tail_level": 0.5
    },
    "inherit_base": "FXInfo",
    "inherit_arg": true,
    "name": ":gverb",
    "summary": "GVerb",
    "hidden": false
  },
  "FXReverb": {
    "opts": {
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "mix": 0.4,
      "mix_slide": 0,
      "mix_slide_shape": 1,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "pre_mix_slide": 0,
      "pre_mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_amp": 1,
      "pre_amp_slide": 0,
      "pre_amp_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "room": 0.6,
      "room_slide": 0,
      "room_slide_shape": 1,
      "room_slide_curve": 0,
      "damp": 0.5,
      "damp_slide": 0,
      "damp_slide_shape": 1,
      "damp_slide_curve": 0
    },
    "inherit_base": "FXInfo",
    "inherit_arg": true,
    "name": ":reverb",
    "summary": "Reverb",
    "hidden": false
  },
  "FXKrush": {
    "opts": {
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "mix": 1,
      "mix_slide": 0,
      "mix_slide_shape": 1,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "pre_mix_slide": 0,
      "pre_mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_amp": 1,
      "pre_amp_slide": 0,
      "pre_amp_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "gain": 5,
      "gain_slide": 0,
      "gain_slide_shape": 1,
      "gain_slide__curve": 0,
      "cutoff": 100,
      "cutoff_slide": 0,
      "cutoff_slide_shape": 1,
      "cutoff_slide_curve": 0,
      "res": 0,
      "res_slide": 0,
      "res_slide_shape": 1,
      "res_slide_curve": 0
    },
    "inherit_base": "FXInfo",
    "inherit_arg": true,
    "name": ":krush",
    "summary": "krush",
    "hidden": false
  },
  "FXBitcrusher": {
    "opts": {
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "mix": 1,
      "mix_slide": 0,
      "mix_slide_shape": 1,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "pre_mix_slide": 0,
      "pre_mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_amp": 1,
      "pre_amp_slide": 0,
      "pre_amp_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "sample_rate": 10000,
      "sample_rate_slide": 0,
      "sample_rate_slide_shape": 1,
      "sample_rate_slide_curve": 0,
      "bits": 8,
      "bits_slide": 0,
      "bits_slide_shape": 1,
      "bits_slide_curve": 0,
      "cutoff": 0,
      "cutoff_slide": 0,
      "cutoff_slide_shape": 1,
      "cutoff_slide_curve": 0
    },
    "inherit_base": "FXInfo",
    "inherit_arg": true,
    "name": ":bitcrusher",
    "summary": "Bitcrusher",
    "hidden": false
  },
  "FXLevel": {
    "opts": {
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0
    },
    "inherit_base": "FXInfo",
    "inherit_arg": false,
    "name": ":level",
    "summary": "Level Amplifier",
    "hidden": false
  },
  "FXAutotuner": {
    "opts": {
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "mix": 1,
      "mix_slide": 0,
      "mix_slide_shape": 1,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "pre_mix_slide": 0,
      "pre_mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_amp": 1,
      "pre_amp_slide": 0,
      "pre_amp_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "note": 0,
      "note_slide": 0,
      "note_slide_shape": 1,
      "note_slide_curve": 0,
      "formant_ratio": 1.0,
      "formant_ratio_slide": 0,
      "formant_ratio_slide_shape": 1,
      "formant_ratio_slide_curve": 0
    },
    "inherit_base": "FXInfo",
    "inherit_arg": true,
    "name": ":autotuner",
    "summary": "Autotuner",
    "hidden": false
  },
  "FXMono": {
    "opts": {
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "mix": 1,
      "mix_slide": 0,
      "mix_slide_shape": 1,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "pre_mix_slide": 0,
      "pre_mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_amp": 1,
      "pre_amp_slide": 0,
      "pre_amp_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "pan": 0,
      "pan_slide": 0,
      "pan_slide_shape": 1,
      "pan_slide_curve": 0
    },
    "inherit_base": "FXInfo",
    "inherit_arg": true,
    "name": ":mono",
    "summary": "Mono",
    "hidden": false
  },
  "FXEcho": {
    "opts": {
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "mix": 1,
      "mix_slide": 0,
      "mix_slide_shape": 1,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "pre_mix_slide": 0,
      "pre_mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_amp": 1,
      "pre_amp_slide": 0,
      "pre_amp_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "phase": 0.25,
      "phase_slide": 0,
      "phase_slide_shape": 1,
      "phase_slide_curve": 0,
      "decay": 2,
      "decay_slide": 0,
      "decay_slide_shape": 1,
      "decay_slide_curve": 0,
      "max_phase": 2
    },
    "inherit_base": "FXInfo",
    "inherit_arg": true,
    "name": ":echo",
    "summary": "Echo",
    "hidden": false
  },
  "FXSlicer": {
    "opts": {
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "mix": 1,
      "mix_slide": 0,
      "mix_slide_shape": 1,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "pre_mix_slide": 0,
      "pre_mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_amp": 1,
      "pre_amp_slide": 0,
      "pre_amp_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "phase": 0.25,
      "phase_slide": 0,
      "phase_slide_shape": 1,
      "phase_slide_curve": 0,
      "amp_min": 0,
      "amp_min_slide": 0,
      "amp_min_slide_shape": 1,
      "amp_min_slide_curve": 0,
      "amp_max": 1,
      "amp_max_slide": 0,
      "amp_max_slide_shape": 1,
      "amp_max_slide_curve": 0,
      "pulse_width": 0.5,
      "pulse_width_slide": 0,
      "pulse_width_slide_shape": 1,
      "pulse_width_slide_curve": 0,
      "phase_offset": 0,
      "wave": 1,
      "invert_wave": 0,
      "probability": 0,
      "probability_slide": 0,
      "probability_slide_shape": 1,
      "probability_slide_curve": 0,
      "prob_pos": 0,
      "prob_pos_slide": 0,
      "prob_pos_slide_shape": 1,
      "prob_pos_slide_curve": 0,
      "seed": 0,
      "smooth": 0,
      "smooth_slide": 0,
      "smooth_slide_shape": 1,
      "smooth_slide_curve": 0,
      "smooth_up": 0,
      "smooth_up_slide": 0,
      "smooth_up_slide_shape": 1,
      "smooth_up_slide_curve": 0,
      "smooth_down": 0,
      "smooth_down_slide": 0,
      "smooth_down_slide_shape": 1,
      "smooth_down_slide_curve": 0
    },
    "inherit_base": "FXInfo",
    "inherit_arg": true,
    "name": ":slicer",
    "summary": "Slicer",
    "hidden": false
  },
  "FXWobble": {
    "opts": {
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "mix": 1,
      "mix_slide": 0,
      "mix_slide_shape": 1,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "pre_mix_slide": 0,
      "pre_mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_amp": 1,
      "pre_amp_slide": 0,
      "pre_amp_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "phase": 0.5,
      "phase_slide": 0,
      "phase_slide_shape": 1,
      "phase_slide_curve": 0,
      "cutoff_min": 60,
      "cutoff_min_slide": 0,
      "cutoff_min_slide_shape": 1,
      "cutoff_min_slide_curve": 0,
      "cutoff_max": 120,
      "cutoff_max_slide": 0,
      "cutoff_max_slide_shape": 1,
      "cutoff_max_slide_curve": 0,
      "res": 0.8,
      "res_slide": 0,
      "res_slide_shape": 1,
      "res_slide_curve": 0,
      "phase_offset": 0,
      "wave": 0,
      "invert_wave": 0,
      "pulse_width": 0.5,
      "pulse_width_slide": 0,
      "pulse_width_slide_shape": 1,
      "pulse_width_slide_curve": 0,
      "filter": 0,
      "probability": 0,
      "probability_slide": 0,
      "probability_slide_shape": 1,
      "probability_slide_curve": 0,
      "prob_pos": 0,
      "prob_pos_slide": 0,
      "prob_pos_slide_shape": 1,
      "prob_pos_slide_curve": 0,
      "seed": 0,
      "smooth": 0,
      "smooth_slide": 0,
      "smooth_slide_shape": 1,
      "smooth_slide_curve": 0,
      "smooth_up": 0,
      "smooth_up_slide": 0,
      "smooth_up_slide_shape": 1,
      "smooth_up_slide_curve": 0,
      "smooth_down": 0,
      "smooth_down_slide": 0,
      "smooth_down_slide_shape": 1,
      "smooth_down_slide_curve": 0
    },
    "inherit_base": "FXInfo",
    "inherit_arg": true,
    "name": ":wobble",
    "summary": "Wobble",
    "hidden": false
  },
  "FXPanSlicer": {
    "opts": {
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "mix": 1,
      "mix_slide": 0,
      "mix_slide_shape": 1,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "pre_mix_slide": 0,
      "pre_mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_amp": 1,
      "pre_amp_slide": 0,
      "pre_amp_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "phase": 0.25,
      "phase_slide": 0,
      "phase_slide_shape": 1,
      "phase_slide_curve": 0,
      "amp_min": 0,
      "amp_min_slide": 0,
      "amp_min_slide_shape": 1,
      "amp_min_slide_curve": 0,
      "amp_max": 1,
      "amp_max_slide": 0,
      "amp_max_slide_shape": 1,
      "amp_max_slide_curve": 0,
      "pulse_width": 0.5,
      "pulse_width_slide": 0,
      "pulse_width_slide_shape": 1,
      "pulse_width_slide_curve": 0,
      "phase_offset": 0,
      "wave": 1,
      "invert_wave": 0,
      "probability": 0,
      "probability_slide": 0,
      "probability_slide_shape": 1,
      "probability_slide_curve": 0,
      "prob_pos": 0,
      "prob_pos_slide": 0,
      "prob_pos_slide_shape": 1,
      "prob_pos_slide_curve": 0,
      "seed": 0,
      "smooth": 0,
      "smooth_slide": 0,
      "smooth_slide_shape": 1,
      "smooth_slide_curve": 0,
      "smooth_up": 0,
      "smooth_up_slide": 0,
      "smooth_up_slide_shape": 1,
      "smooth_up_slide_curve": 0,
      "smooth_down": 0,
      "smooth_down_slide": 0,
      "smooth_down_slide_shape": 1,
      "smooth_down_slide_curve": 0,
      "pan_min": -1,
      "pan_min_slide": 0,
      "pan_min_slide_shape": 1,
      "pan_min_slide_curve": 0,
      "pan_max": 1,
      "pan_max_slide": 0,
      "pan_max_slide_shape": 1,
      "pan_max_slide_curve": 0
    },
    "inherit_base": "FXSlicer",
    "inherit_arg": true,
    "name": ":panslicer",
    "summary": "Pan Slicer",
    "hidden": true
  },
  "FXIXITechno": {
    "opts": {
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "mix": 1,
      "mix_slide": 0,
      "mix_slide_shape": 1,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "pre_mix_slide": 0,
      "pre_mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_amp": 1,
      "pre_amp_slide": 0,
      "pre_amp_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "phase": 4,
      "phase_slide": 0,
      "phase_slide_shape": 1,
      "phase_slide_curve": 0,
      "phase_offset": 0,
      "cutoff_min": 60,
      "cutoff_min_slide": 0,
      "cutoff_min_slide_shape": 1,
      "cutoff_min_slide_curve": 0,
      "cutoff_max": 120,
      "cutoff_max_slide": 0,
      "cutoff_max_slide_shape": 1,
      "cutoff_max_slide_curve": 0,
      "res": 0.8,
      "res_slide": 0,
      "res_slide_shape": 1,
      "res_slide_curve": 0
    },
    "inherit_base": "FXInfo",
    "inherit_arg": true,
    "name": ":ixi_techno",
    "summary": "Techno from IXI Lang",
    "hidden": false
  },
  "FXWhammy": {
    "opts": {
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "mix": 1,
      "mix_slide": 0,
      "mix_slide_shape": 1,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "pre_mix_slide": 0,
      "pre_mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_amp": 1,
      "pre_amp_slide": 0,
      "pre_amp_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "transpose": 12,
      "transpose_slide": 0,
      "transpose_slide_shape": 1,
      "transpose_slide_curve": 0,
      "max_delay_time": 1,
      "deltime": 0.05,
      "grainsize": 0.075
    },
    "inherit_base": "FXInfo",
    "inherit_arg": true,
    "name": ":whammy",
    "summary": "Whammy",
    "hidden": false
  },
  "FXCompressor": {
    "opts": {
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "mix": 1,
      "mix_slide": 0,
      "mix_slide_shape": 1,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "pre_mix_slide": 0,
      "pre_mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_amp": 1,
      "pre_amp_slide": 0,
      "pre_amp_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "threshold": 0.2,
      "threshold_slide": 0,
      "threshold_slide_shape": 1,
      "threshold_slide_curve": 0,
      "clamp_time": 0.01,
      "clamp_time_slide": 0,
      "clamp_time_slide_shape": 1,
      "clamp_time_slide_curve": 0,
      "slope_above": 0.5,
      "slope_above_slide": 0,
      "slope_above_slide_shape": 1,
      "slope_above_slide_curve": 0,
      "slope_below": 1,
      "slope_below_slide": 0,
      "slope_below_slide_shape": 1,
      "slope_below_slide_curve": 0,
      "relax_time": 0.01,
      "relax_time_slide": 0,
      "relax_time_slide_shape": 1,
      "relax_time_slide_curve": 0
    },
    "inherit_base": "FXInfo",
    "inherit_arg": true,
    "name": ":compressor",
    "summary": "Compressor",
    "hidden": false
  },
  "FXVowel": {
    "opts": {
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "mix": 1,
      "mix_slide": 0,
      "mix_slide_shape": 1,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "pre_mix_slide": 0,
      "pre_mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_amp": 1,
      "pre_amp_slide": 0,
      "pre_amp_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "vowel_sound": 1,
      "voice": 0
    },
    "inherit_base": "FXInfo",
    "inherit_arg": true,
    "name": ":vowel",
    "summary": "Vowel",
    "hidden": false
  },
  "FXOctaver": {
    "opts": {
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "mix": 1,
      "mix_slide": 0,
      "mix_slide_shape": 1,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "pre_mix_slide": 0,
      "pre_mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_amp": 1,
      "pre_amp_slide": 0,
      "pre_amp_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "super_amp": 1,
      "super_amp_slide": 0,
      "super_amp_slide_shape": 1,
      "super_amp_slide_curve": 0,
      "sub_amp": 1,
      "sub_amp_slide": 0,
      "sub_amp_slide_shape": 1,
      "sub_amp_slide_curve": 0,
      "subsub_amp": 1,
      "subsub_amp_slide": 0,
      "subsub_amp_slide_shape": 1,
      "subsub_amp_slide_curve": 0
    },
    "inherit_base": "FXInfo",
    "inherit_arg": true,
    "name": ":octaver",
    "summary": "Octaver",
    "hidden": false
  },
  "FXChorus": {
    "opts": {
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "mix": 1,
      "mix_slide": 0,
      "mix_slide_shape": 1,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "pre_mix_slide": 0,
      "pre_mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_amp": 1,
      "pre_amp_slide": 0,
      "pre_amp_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "phase": 0.25,
      "phase_slide": 0,
      "phase_slide_shape": 1,
      "phase_slide_curve": 0,
      "decay": 1e-05,
      "decay_slide": 0,
      "decay_slide_shape": 1,
      "decay_slide_curve": 0,
      "max_phase": 1
    },
    "inherit_base": "FXInfo",
    "inherit_arg": true,
    "name": ":chorus",
    "summary": "Chorus",
    "hidden": true
  },
  "FXRingMod": {
    "opts": {
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "mix": 1,
      "mix_slide": 0,
      "mix_slide_shape": 1,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "pre_mix_slide": 0,
      "pre_mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_amp": 1,
      "pre_amp_slide": 0,
      "pre_amp_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "freq": 30,
      "freq_slide": 0,
      "freq_slide_shape": 1,
      "freq_slide_curve": 0,
      "mod_amp": 1,
      "mod_amp_slide": 0,
      "mod_amp_slide_shape": 1,
      "mod_amp_slide_curve": 0
    },
    "inherit_base": "FXInfo",
    "inherit_arg": true,
    "name": ":ring_mod",
    "summary": "Ring Modulator",
    "hidden": false
  },
  "FXBPF": {
    "opts": {
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "mix": 1,
      "mix_slide": 0,
      "mix_slide_shape": 1,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "pre_mix_slide": 0,
      "pre_mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_amp": 1,
      "pre_amp_slide": 0,
      "pre_amp_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "centre": 100,
      "centre_slide": 0,
      "centre_slide_shape": 1,
      "centre_slide_curve": 0,
      "res": 0.6,
      "res_slide": 0,
      "res_slide_shape": 1,
      "res_slide_curve": 0
    },
    "inherit_base": "FXInfo",
    "inherit_arg": true,
    "name": ":bpf",
    "summary": "Band Pass Filter",
    "hidden": false
  },
  "FXRBPF": {
    "opts": {
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "mix": 1,
      "mix_slide": 0,
      "mix_slide_shape": 1,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "pre_mix_slide": 0,
      "pre_mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_amp": 1,
      "pre_amp_slide": 0,
      "pre_amp_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "centre": 100,
      "centre_slide": 0,
      "centre_slide_shape": 1,
      "centre_slide_curve": 0,
      "res": 0.5,
      "res_slide": 0,
      "res_slide_shape": 1,
      "res_slide_curve": 0
    },
    "inherit_base": "FXBPF",
    "inherit_arg": true,
    "name": ":rbpf",
    "summary": "Resonant Band Pass Filter",
    "hidden": true
  },
  "FXNBPF": {
    "opts": {
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "mix": 1,
      "mix_slide": 0,
      "mix_slide_shape": 1,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "pre_mix_slide": 0,
      "pre_mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_amp": 1,
      "pre_amp_slide": 0,
      "pre_amp_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "centre": 100,
      "centre_slide": 0,
      "centre_slide_shape": 1,
      "centre_slide_curve": 0,
      "res": 0.6,
      "res_slide": 0,
      "res_slide_shape": 1,
      "res_slide_curve": 0
    },
    "inherit_base": "FXBPF",
    "inherit_arg": true,
    "name": ":nbpf",
    "summary": "Normalised Band Pass Filter",
    "hidden": true
  },
  "FXNRBPF": {
    "opts": {
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "mix": 1,
      "mix_slide": 0,
      "mix_slide_shape": 1,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "pre_mix_slide": 0,
      "pre_mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_amp": 1,
      "pre_amp_slide": 0,
      "pre_amp_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "centre": 100,
      "centre_slide": 0,
      "centre_slide_shape": 1,
      "centre_slide_curve": 0,
      "res": 0.5,
      "res_slide": 0,
      "res_slide_shape": 1,
      "res_slide_curve": 0
    },
    "inherit_base": "FXRBPF",
    "inherit_arg": true,
    "name": ":nrbpf",
    "summary": "Normalised Resonant Band Pass Filter",
    "hidden": true
  },
  "FXLPF": {
    "opts": {
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "mix": 1,
      "mix_slide": 0,
      "mix_slide_shape": 1,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "pre_mix_slide": 0,
      "pre_mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_amp": 1,
      "pre_amp_slide": 0,
      "pre_amp_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "cutoff": 100,
      "cutoff_slide": 0,
      "cutoff_slide_shape": 1,
      "cutoff_slide_curve": 0
    },
    "inherit_base": "FXInfo",
    "inherit_arg": true,
    "name": ":lpf",
    "summary": "Low Pass Filter",
    "hidden": false
  },
  "FXRLPF": {
    "opts": {
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "mix": 1,
      "mix_slide": 0,
      "mix_slide_shape": 1,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "pre_mix_slide": 0,
      "pre_mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_amp": 1,
      "pre_amp_slide": 0,
      "pre_amp_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "cutoff": 100,
      "cutoff_slide": 0,
      "cutoff_slide_shape": 1,
      "cutoff_slide_curve": 0,
      "res": 0.5,
      "res_slide": 0,
      "res_slide_shape": 1,
      "res_slide_curve": 0
    },
    "inherit_base": "FXLPF",
    "inherit_arg": true,
    "name": ":rlpf",
    "summary": "Resonant Low Pass Filter",
    "hidden": true
  },
  "FXNormRLPF": {
    "opts": {
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "mix": 1,
      "mix_slide": 0,
      "mix_slide_shape": 1,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "pre_mix_slide": 0,
      "pre_mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_amp": 1,
      "pre_amp_slide": 0,
      "pre_amp_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "cutoff": 100,
      "cutoff_slide": 0,
      "cutoff_slide_shape": 1,
      "cutoff_slide_curve": 0,
      "res": 0.5,
      "res_slide": 0,
      "res_slide_shape": 1,
      "res_slide_curve": 0
    },
    "inherit_base": "FXRLPF",
    "inherit_arg": true,
    "name": ":nrlpf",
    "summary": "Normalised Resonant Low Pass Filter",
    "hidden": true
  },
  "FXHPF": {
    "opts": {
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "mix": 1,
      "mix_slide": 0,
      "mix_slide_shape": 1,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "pre_mix_slide": 0,
      "pre_mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_amp": 1,
      "pre_amp_slide": 0,
      "pre_amp_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "cutoff": 100,
      "cutoff_slide": 0,
      "cutoff_slide_shape": 1,
      "cutoff_slide_curve": 0
    },
    "inherit_base": "FXInfo",
    "inherit_arg": true,
    "name": ":hpf",
    "summary": "High Pass Filter",
    "hidden": false
  },
  "FXRHPF": {
    "opts": {
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "mix": 1,
      "mix_slide": 0,
      "mix_slide_shape": 1,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "pre_mix_slide": 0,
      "pre_mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_amp": 1,
      "pre_amp_slide": 0,
      "pre_amp_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "cutoff": 100,
      "cutoff_slide": 0,
      "cutoff_slide_shape": 1,
      "cutoff_slide_curve": 0,
      "res": 0.5,
      "res_slide": 0,
      "res_slide_shape": 1,
      "res_slide_curve": 0
    },
    "inherit_base": "FXHPF",
    "inherit_arg": true,
    "name": ":rhpf",
    "summary": "Resonant High Pass Filter",
    "hidden": true
  },
  "FXNormRHPF": {
    "opts": {
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "mix": 1,
      "mix_slide": 0,
      "mix_slide_shape": 1,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "pre_mix_slide": 0,
      "pre_mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_amp": 1,
      "pre_amp_slide": 0,
      "pre_amp_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "cutoff": 100,
      "cutoff_slide": 0,
      "cutoff_slide_shape": 1,
      "cutoff_slide_curve": 0,
      "res": 0.5,
      "res_slide": 0,
      "res_slide_shape": 1,
      "res_slide_curve": 0
    },
    "inherit_base": "FXRHPF",
    "inherit_arg": true,
    "name": ":nrhpf",
    "summary": "Normalised Resonant High Pass Filter",
    "hidden": true
  },
  "FXBandEQ": {
    "opts": {
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "mix": 1,
      "mix_slide": 0,
      "mix_slide_shape": 1,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "pre_mix_slide": 0,
      "pre_mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_amp": 1,
      "pre_amp_slide": 0,
      "pre_amp_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "freq": 100,
      "freq_slide": 0,
      "freq_slide_shape": 1,
      "freq_slide_curve": 0,
      "res": 0.6,
      "res_slide": 0,
      "res_slide_shape": 1,
      "res_slide_curve": 0,
      "db": 0.6,
      "db_slide": 0,
      "db_slide_shape": 1,
      "db_slide_curve": 0
    },
    "inherit_base": "FXInfo",
    "inherit_arg": true,
    "name": ":band_eq",
    "summary": "Band EQ Filter",
    "hidden": false
  },
  "FXNormLPF": {
    "opts": {
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "mix": 1,
      "mix_slide": 0,
      "mix_slide_shape": 1,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "pre_mix_slide": 0,
      "pre_mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_amp": 1,
      "pre_amp_slide": 0,
      "pre_amp_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "cutoff": 100,
      "cutoff_slide": 0,
      "cutoff_slide_shape": 1,
      "cutoff_slide_curve": 0
    },
    "inherit_base": "FXLPF",
    "inherit_arg": true,
    "name": ":nlpf",
    "summary": "Normalised Low Pass Filter.",
    "hidden": true
  },
  "FXNormHPF": {
    "opts": {
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "mix": 1,
      "mix_slide": 0,
      "mix_slide_shape": 1,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "pre_mix_slide": 0,
      "pre_mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_amp": 1,
      "pre_amp_slide": 0,
      "pre_amp_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "cutoff": 100,
      "cutoff_slide": 0,
      "cutoff_slide_shape": 1,
      "cutoff_slide_curve": 0
    },
    "inherit_base": "FXHPF",
    "inherit_arg": true,
    "name": ":nhpf",
    "summary": "Normalised High Pass Filter",
    "hidden": true
  },
  "FXNormaliser": {
    "opts": {
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "mix": 1,
      "mix_slide": 0,
      "mix_slide_shape": 1,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "pre_mix_slide": 0,
      "pre_mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_amp": 1,
      "pre_amp_slide": 0,
      "pre_amp_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "level": 1,
      "level_slide": 0,
      "level_slide_shape": 1,
      "level_slide_curve": 0
    },
    "inherit_base": "FXInfo",
    "inherit_arg": true,
    "name": ":normaliser",
    "summary": "Normaliser",
    "hidden": false
  },
  "FXTanh": {
    "opts": {
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "mix": 1,
      "mix_slide": 0,
      "mix_slide_shape": 1,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "pre_mix_slide": 0,
      "pre_mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_amp": 1,
      "pre_amp_slide": 0,
      "pre_amp_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "krunch": 5,
      "krunch_slide": 0,
      "krunch_slide_shape": 1,
      "krunch_slide_curve": 0
    },
    "inherit_base": "FXInfo",
    "inherit_arg": true,
    "name": ":tanh",
    "summary": "Hyperbolic Tangent",
    "hidden": false
  },
  "FXPitchShift": {
    "opts": {
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "mix": 1,
      "mix_slide": 0,
      "mix_slide_shape": 1,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "pre_mix_slide": 0,
      "pre_mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_amp": 1,
      "pre_amp_slide": 0,
      "pre_amp_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "window_size": 0.2,
      "window_size_slide": 0,
      "window_size_slide_shape": 1,
      "window_size_slide_curve": 0,
      "pitch": 0,
      "pitch_slide": 0,
      "pitch_slide_shape": 1,
      "pitch_slide_curve": 0,
      "pitch_dis": 0.0,
      "pitch_dis_slide": 0,
      "pitch_dis_slide_shape": 1,
      "pitch_dis_slide_curve": 0,
      "time_dis": 0.0,
      "time_dis_slide": 0,
      "time_dis_slide_shape": 1,
      "time_dis_slide_curve": 0
    },
    "inherit_base": "FXInfo",
    "inherit_arg": true,
    "name": ":pitch_shift",
    "summary": "Pitch shift",
    "hidden": false
  },
  "FXDistortion": {
    "opts": {
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "mix": 1,
      "mix_slide": 0,
      "mix_slide_shape": 1,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "pre_mix_slide": 0,
      "pre_mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_amp": 1,
      "pre_amp_slide": 0,
      "pre_amp_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "distort": 0.5,
      "distort_slide": 0,
      "distort_slide_shape": 1,
      "distort_slide_curve": 0
    },
    "inherit_base": "FXInfo",
    "inherit_arg": true,
    "name": ":distortion",
    "summary": "Distortion",
    "hidden": false
  },
  "FXPan": {
    "opts": {
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "mix": 1,
      "mix_slide": 0,
      "mix_slide_shape": 1,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "pre_mix_slide": 0,
      "pre_mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_amp": 1,
      "pre_amp_slide": 0,
      "pre_amp_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "pan": 0,
      "pan_slide": 0,
      "pan_slide_shape": 1,
      "pan_slide_curve": 0
    },
    "inherit_base": "FXInfo",
    "inherit_arg": true,
    "name": ":pan",
    "summary": "Pan",
    "hidden": false
  },
  "FXFlanger": {
    "opts": {
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "mix": 1,
      "mix_slide": 0,
      "mix_slide_shape": 1,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "pre_mix_slide": 0,
      "pre_mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_amp": 1,
      "pre_amp_slide": 0,
      "pre_amp_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "phase": 4,
      "phase_slide": 0,
      "phase_slide_shape": 1,
      "phase_slide_curve": 0,
      "phase_offset": 0,
      "wave": 4,
      "invert_wave": 0,
      "stereo_invert_wave": 0,
      "delay": 5,
      "delay_slide": 0,
      "delay_slide_shape": 1,
      "delay_slide_curve": 0,
      "max_delay": 20,
      "depth": 5,
      "depth_slide": 0,
      "depth_slide_shape": 1,
      "depth_slide_curve": 0,
      "decay": 2,
      "decay_slide": 0,
      "decay_slide_shape": 1,
      "decay_slide_curve": 0,
      "feedback": 0,
      "feedback_slide": 0,
      "feedback_slide_shape": 1,
      "feedback_slide_curve": 0,
      "invert_flange": 0
    },
    "inherit_base": "FXInfo",
    "inherit_arg": true,
    "name": ":flanger",
    "summary": "Flanger",
    "hidden": false
  },
  "FXTremolo": {
    "opts": {
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "mix": 1,
      "mix_slide": 0,
      "mix_slide_shape": 1,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "pre_mix_slide": 0,
      "pre_mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_amp": 1,
      "pre_amp_slide": 0,
      "pre_amp_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "phase": 4,
      "phase_slide": 0,
      "phase_slide_shape": 1,
      "phase_slide_curve": 0,
      "phase_offset": 0,
      "wave": 2,
      "invert_wave": 0,
      "depth": 0.5,
      "depth_slide": 0,
      "depth_slide_shape": 1,
      "depth_slide_curve": 0
    },
    "inherit_base": "FXInfo",
    "inherit_arg": true,
    "name": ":tremolo",
    "summary": "Tremolo",
    "hidden": false
  },
  "FXPingPong": {
    "opts": {
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "mix": 1,
      "mix_slide": 0,
      "mix_slide_shape": 1,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "pre_mix_slide": 0,
      "pre_mix_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "pre_amp": 1,
      "pre_amp_slide": 0,
      "pre_amp_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "phase": 0.25,
      "phase_slide": 0,
      "phase_slide_shape": 1,
      "phase_slide_curve": 0,
      "feedback": 0.5,
      "feedback_slide": 0,
      "feedback_slide_shape": 1,
      "feedback_slide_curve": 0,
      "max_phase": 1,
      "pan_start": 1
    },
    "inherit_base": "FXInfo",
    "inherit_arg": true,
    "name": ":ping_pong",
    "summary": "Ping Pong Echo",
    "hidden": false
  }
}

samples = {
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
  "Sounds featuring guitars": [
    ":guit_harmonics",
    ":guit_e_fifths",
    ":guit_e_slide",
    ":guit_em9"
  ],
  "Miscellaneous Sounds": [
    ":misc_burp",
    ":misc_crow",
    ":misc_cineboom"
  ],
  "Percussive Sounds": [
    ":perc_bell",
    ":perc_bell2",
    ":perc_snap",
    ":perc_snap2",
    ":perc_swash",
    ":perc_till",
    ":perc_door",
    ":perc_impact1",
    ":perc_impact2",
    ":perc_swoosh"
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
    ":ambi_choir",
    ":ambi_sauna"
  ],
  "Bass Sounds": [
    ":bass_hit_c",
    ":bass_hard_c",
    ":bass_thick_c",
    ":bass_drop_c",
    ":bass_woodsy_c",
    ":bass_voxy_c",
    ":bass_voxy_hit_c",
    ":bass_dnb_f",
    ":bass_trance_c"
  ],
  "Snare Drums": [
    ":sn_dub",
    ":sn_dolf",
    ":sn_zome",
    ":sn_generic"
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
    ":bd_tek",
    ":bd_mehackit"
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
    ":loop_tabla",
    ":loop_3d_printer",
    ":loop_drone_g_97",
    ":loop_electric",
    ":loop_mehackit1",
    ":loop_mehackit2",
    ":loop_perc1",
    ":loop_perc2",
    ":loop_weirdo",
    ""
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
  "Glitchy Sounds": [
    ":glitch_bass_g",
    ":glitch_perc1",
    ":glitch_perc2",
    ":glitch_perc3",
    ":glitch_perc4",
    ":glitch_perc5",
    ":glitch_robot1",
    ":glitch_robot2"
  ],
  "Vinyl sounds": [
    ":vinyl_backspin",
    ":vinyl_rewind",
    ":vinyl_scratch",
    ":vinyl_hiss"
  ],
  "Mehackit Sounds": [
    ":mehackit_phone1",
    ":mehackit_phone2",
    ":mehackit_phone3",
    ":mehackit_phone4",
    ":mehackit_robot1",
    ":mehackit_robot2",
    ":mehackit_robot3",
    ":mehackit_robot4",
    ":mehackit_robot5",
    ":mehackit_robot6",
    ":mehackit_robot7",
    ""
  ]
}

synth_args_types_conversion = {}

synth_opts_types_conversion = {}

