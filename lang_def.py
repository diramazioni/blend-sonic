null = None; true = True; false = False;
#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/

lang_core = {
  "range": {
    "introduced": "2,2,0",
    "returns": ":ring",
    "inline": true,
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
    "name": "range",
    "accepts_block": false,
    "memoize": true,
    "signature": {
      "start": null,
      "*args": null,
      "finish": null
    },
    "hiden": false,
    "opts": {
      "inclusive": false,
      "step": 1
    }
  },
  "bools": {
    "introduced": "2,2,0",
    "returns": ":ring",
    "inline": true,
    "summary": "Create a ring of boolean values",
    "args": [
      {
        "list": ":array"
      }
    ],
    "name": "bools",
    "accepts_block": false,
    "signature": {
      "*args": null
    },
    "hiden": false
  },
  "print": {
    "introduced": "2,0,0",
    "accepts_block": false,
    "summary": "Display a message in the output pane",
    "args": [
      {
        "output": ":anything"
      }
    ],
    "name": "print",
    "signature": {
      "*msgs": null
    },
    "hiden": true,
    "intro_fn": true
  },
  "tick_reset": {
    "introduced": "2,6,0",
    "returns": ":number",
    "alt_args": [
      {
        "key": ":symbol"
      }
    ],
    "summary": "Reset tick to 0",
    "name": "tick_reset",
    "accepts_block": false,
    "signature": {
      "*args": null
    },
    "hiden": false
  },
  "spark_graph": {
    "introduced": "2,5,0",
    "accepts_block": false,
    "summary": "Returns a string representing a list of numeric values as a spark graph/bar chart",
    "name": "spark_graph",
    "signature": {
      "*values": null
    },
    "hiden": true
  },
  "with_bpm_mul": {
    "introduced": "2,3,0",
    "accepts_block": true,
    "summary": "Set new tempo as a multiple of current tempo for block",
    "args": [
      {
        "mul": ":number"
      }
    ],
    "name": "with_bpm_mul",
    "signature": {
      "&block": null,
      "mul": null
    },
    "hiden": false,
    "requires_block": true
  },
  "vector": {
    "introduced": "2,6,0",
    "returns": ":vector",
    "inline": true,
    "summary": "Create a vector",
    "args": [
      {
        "list": ":array"
      }
    ],
    "name": "vector",
    "accepts_block": false,
    "signature": {
      "*args": null
    },
    "hiden": false
  },
  "on": {
    "introduced": "2,10,0",
    "returns": null,
    "summary": "Optionally evaluate block",
    "args": [
      {
        "condition": ":truthy"
      }
    ],
    "name": "on",
    "accepts_block": true,
    "signature": {
      "condition": null,
      "&blk": null
    },
    "hiden": false,
    "requires_block": true
  },
  "rrand": {
    "introduced": "2,0,0",
    "accepts_block": false,
    "inline": true,
    "summary": "Generate a random float between two numbers",
    "args": [
      {
        "min": ":number"
      },
      {
        "max": ":number"
      }
    ],
    "name": "rrand",
    "signature": {
      "max": null,
      "*opts": null,
      "min": null
    },
    "hiden": false,
    "intro_fn": true,
    "opts": {
      "step": 1
    }
  },
  "current_random_seed": {
    "introduced": "2,10,0",
    "accepts_block": false,
    "summary": "Get current random seed",
    "name": "current_random_seed",
    "hiden": true,
    "intro_fn": true
  },
  "use_bpm": {
    "introduced": "2,0,0",
    "accepts_block": false,
    "summary": "Set the tempo",
    "args": [
      {
        "bpm": ":number"
      }
    ],
    "name": "use_bpm",
    "signature": {
      "&block": null,
      "bpm": null
    },
    "hiden": false,
    "intro_fn": true
  },
  "look": {
    "introduced": "2,6,0",
    "returns": ":number",
    "alt_args": [
      {
        "list": ":array"
      },
      {
        "key": ":symbol"
      }
    ],
    "summary": "Obtain value of a tick",
    "name": "look",
    "accepts_block": false,
    "signature": {
      "*args": null
    },
    "hiden": false,
    "inline": true,
    "opts": {
      "offset": 0
    }
  },
  "block_slept": {
    "introduced": "2,9,0",
    "accepts_block": true,
    "summary": "Determine if block contains sleep time",
    "args": [],
    "name": "block_slept?",
    "async_block": false,
    "signature": {
      "&block": null
    },
    "hiden": false,
    "requires_block": true
  },
  "comment": {
    "introduced": "2,0,0",
    "accepts_block": true,
    "summary": "Block level commenting",
    "name": "comment",
    "signature": {
      "*args": null,
      "&block": null
    },
    "hiden": true,
    "requires_block": true
  },
  "factor": {
    "introduced": "2,1,0",
    "accepts_block": false,
    "summary": "Factor test",
    "args": [
      {
        "val": ":number"
      },
      {
        "factor": ":number"
      }
    ],
    "name": "factor?",
    "signature": {
      "factor": null,
      "val": null
    },
    "hiden": false
  },
  "knit": {
    "introduced": "2,2,0",
    "returns": ":ring",
    "inline": true,
    "summary": "Knit a sequence of repeated values",
    "args": [
      {
        "value": ":anything"
      },
      {
        "count": ":number"
      }
    ],
    "name": "knit",
    "accepts_block": false,
    "signature": {
      "*args": null
    },
    "hiden": false
  },
  "rand_reset": {
    "introduced": "2,7,0",
    "accepts_block": false,
    "summary": "Reset rand generator to last seed",
    "args": [],
    "name": "rand_reset",
    "hiden": false
  },
  "stretch": {
    "introduced": "2,6,0",
    "returns": ":ring",
    "inline": true,
    "summary": "Stretch a sequence of values",
    "args": [
      {
        "count": ":int"
      }
    ],
    "name": "stretch",
    "accepts_block": false,
    "signature": {
      "*args": null
    },
    "hiden": false,
    "alt_args": [
      {
        "list": ":array"
      }
    ]
  },
  "block_duration": {
    "introduced": "2,9,0",
    "accepts_block": true,
    "summary": "Return block duration",
    "args": [],
    "name": "block_duration",
    "async_block": false,
    "signature": {
      "&block": null
    },
    "hiden": false,
    "requires_block": true
  },
  "at": {
    "introduced": "2,1,0",
    "accepts_block": true,
    "summary": "Asynchronous Time. Run a block at the given time(s)",
    "args": [
      {
        "times": ":list"
      },
      {
        "params": ":list"
      }
    ],
    "name": "at",
    "async_block": true,
    "signature": {
      "times": 0,
      "&block": null,
      "params": "nil"
    },
    "hiden": false,
    "requires_block": true
  },
  "use_osc": {
    "signature": {
      "host_or_port": null,
      "port": "nil"
    },
    "hiden": true
  },
  "ring": {
    "introduced": "2,2,0",
    "returns": ":ring",
    "inline": true,
    "summary": "Create a ring buffer",
    "args": [
      {
        "list": ":array"
      }
    ],
    "name": "ring",
    "accepts_block": false,
    "signature": {
      "*args": null
    },
    "hiden": false
  },
  "with_cue_logging": {
    "introduced": "2,6,0",
    "accepts_block": true,
    "summary": "Block-level enable and disable cue logging",
    "args": [
      {
        "true_or_false": ":boolean"
      }
    ],
    "name": "with_cue_logging",
    "signature": {
      "&block": null,
      "v": null
    },
    "hiden": false,
    "requires_block": true
  },
  "tick_set": {
    "introduced": "2,6,0",
    "returns": ":number",
    "alt_args": [
      {
        "key": ":symbol"
      },
      {
        "value": ":number"
      }
    ],
    "summary": "Set tick to a specific value",
    "args": [
      {
        "value": ":number"
      }
    ],
    "name": "tick_set",
    "accepts_block": false,
    "signature": {
      "*args": null
    },
    "hiden": false
  },
  "ramp": {
    "introduced": "2,6,0",
    "returns": ":ramp",
    "inline": true,
    "summary": "Create a ramp vector",
    "args": [
      {
        "list": ":array"
      }
    ],
    "name": "ramp",
    "accepts_block": false,
    "signature": {
      "*args": null
    },
    "hiden": false
  },
  "defonce": {
    "introduced": "2,0,0",
    "accepts_block": true,
    "summary": "Define a named value only once",
    "args": [
      {
        "name": ":symbol"
      }
    ],
    "name": "defonce",
    "signature": {
      "*opts": null,
      "&block": null,
      "name": null
    },
    "hiden": false,
    "requires_block": true,
    "opts": {
      "override": false
    }
  },
  "beat": {
    "introduced": "2,10,0",
    "accepts_block": false,
    "summary": "Get current beat",
    "args": [],
    "name": "beat",
    "hiden": true
  },
  "sync": {
    "introduced": "2,0,0",
    "accepts_block": false,
    "summary": "Sync with other threads",
    "args": [
      {
        "cue_id": ":symbol"
      }
    ],
    "name": "sync",
    "advances_time": true,
    "signature": {
      "opts": "{}",
      "cue_ids": null
    },
    "hiden": false,
    "opts": {
      "bpm_sync": false
    }
  },
  "run_code": {
    "introduced": "2,11,0",
    "returns": null,
    "summary": "Evaluate the code passed as a String as a new Run",
    "args": [
      {
        "code": ":string"
      }
    ],
    "name": "run_code",
    "accepts_block": false,
    "signature": {
      "code": null
    },
    "hiden": false
  },
  "reset": {
    "introduced": "2,11,0",
    "returns": null,
    "summary": "Reset all thread locals",
    "args": [],
    "name": "reset",
    "accepts_block": false,
    "hiden": false
  },
  "use_cue_logging": {
    "introduced": "2,6,0",
    "accepts_block": false,
    "summary": "Enable and disable cue logging",
    "args": [
      {
        "true_or_false": ":boolean"
      }
    ],
    "name": "use_cue_logging",
    "signature": {
      "&block": null,
      "v": null
    },
    "hiden": false
  },
  "spark": {
    "introduced": "2,5,0",
    "accepts_block": false,
    "summary": "Print a string representing a list of numeric values as a spark graph/bar chart",
    "name": "spark",
    "signature": {
      "*values": null
    },
    "hiden": true
  },
  "puts": {
    "introduced": "2,0,0",
    "accepts_block": false,
    "summary": "Display a message in the output pane",
    "args": [
      {
        "output": ":anything"
      }
    ],
    "name": "puts",
    "signature": {
      "*msgs": null
    },
    "hiden": true,
    "intro_fn": true
  },
  "run_file": {
    "introduced": "2,11,0",
    "returns": null,
    "summary": "Evaluate the contents of the file as a new Run",
    "args": [
      {
        "filename": ":path"
      }
    ],
    "name": "run_file",
    "accepts_block": false,
    "signature": {
      "path": null
    },
    "hiden": false
  },
  "osc": {
    "signature": {
      "path": null,
      "*args": null
    },
    "hiden": true
  },
  "doubles": {
    "introduced": "2,10,0",
    "returns": ":ring",
    "inline": true,
    "summary": "Create a ring of successive doubles",
    "args": [
      {
        "start": ":number"
      },
      {
        "num_doubles": ":int"
      }
    ],
    "name": "doubles",
    "accepts_block": false,
    "memoize": true,
    "signature": {
      "start": null,
      "num_doubles": 1
    },
    "hiden": false
  },
  "choose": {
    "introduced": "2,0,0",
    "accepts_block": false,
    "inline": true,
    "summary": "Random list selection",
    "args": [],
    "name": "choose",
    "signature": {
      "args": null
    },
    "hiden": false,
    "alt_args": [
      {
        "list": ":array"
      }
    ]
  },
  "pick": {
    "introduced": "2,10,0",
    "accepts_block": false,
    "inline": true,
    "summary": "Randomly pick from list (with duplicates)",
    "args": [
      {
        "n": ":number_or_nil"
      }
    ],
    "name": "pick",
    "signature": {
      "*args": null
    },
    "hiden": false,
    "alt_args": [
      {
        "list": ":array"
      }
    ],
    "opts": {
      "skip": 0
    }
  },
  "clear": {
    "introduced": "2,11,0",
    "returns": null,
    "summary": "Clear all thread locals to defaults",
    "args": [],
    "name": "clear",
    "accepts_block": false,
    "hiden": false
  },
  "load_buffer": {
    "introduced": "2,10,0",
    "accepts_block": false,
    "summary": "Load the contents of a file to the current buffer",
    "args": [
      {
        "path": ":string"
      }
    ],
    "name": "load_buffer",
    "signature": {
      "path": null
    },
    "hiden": false
  },
  "wait": {
    "introduced": "2,0,0",
    "accepts_block": false,
    "summary": "Wait for duration",
    "args": [
      {
        "beats": ":number"
      }
    ],
    "name": "wait",
    "advances_time": true,
    "signature": {
      "time": null
    },
    "hiden": true
  },
  "halves": {
    "introduced": "2,10,0",
    "returns": ":ring",
    "inline": true,
    "summary": "Create a ring of successive halves",
    "args": [
      {
        "start": ":number"
      },
      {
        "num_halves": ":int"
      }
    ],
    "name": "halves",
    "accepts_block": false,
    "memoize": true,
    "signature": {
      "num_halves": 1,
      "start": null
    },
    "hiden": false
  },
  "uncomment": {
    "introduced": "2,0,0",
    "accepts_block": true,
    "summary": "Block level comment ignoring",
    "name": "uncomment",
    "signature": {
      "*args": null,
      "&block": null
    },
    "hiden": true,
    "requires_block": true
  },
  "current_beat_duration": {
    "introduced": "2,6,0",
    "accepts_block": false,
    "summary": "Duration of current beat",
    "hiden": true,
    "name": "current_beat_duration"
  },
  "inc": {
    "introduced": "2, 1, 0",
    "accepts_block": false,
    "summary": "Increment",
    "args": [
      {
        "n": ":number"
      }
    ],
    "name": "inc",
    "signature": {
      "n": null
    },
    "hiden": true,
    "opts": {}
  },
  "rdist": {
    "introduced": "2,3,0",
    "accepts_block": false,
    "alt_args": [
      {
        "width": ":number"
      },
      {
        "centre": ":number"
      }
    ],
    "summary": "Random number in centred distribution",
    "args": [
      {
        "width": ":number"
      }
    ],
    "name": "rdist",
    "signature": {
      "width": null,
      "*opts": null,
      "centre": 0
    },
    "hiden": false,
    "inline": true,
    "opts": {
      "step": 1
    }
  },
  "tick": {
    "introduced": "2,6,0",
    "returns": ":number",
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
    "summary": "Increment a tick and return value",
    "args": [],
    "name": "tick",
    "accepts_block": false,
    "signature": {
      "*args": null
    },
    "hiden": false,
    "inline": true,
    "opts": {
      "offset": 0,
      "step": 1
    }
  },
  "tick_reset_all": {
    "introduced": "2,6,0",
    "returns": null,
    "alt_args": [
      {
        "key": ":symbol"
      },
      {
        "value": ":number"
      }
    ],
    "summary": "Reset all ticks",
    "args": [
      {
        "value": ":number"
      }
    ],
    "name": "tick_reset_all",
    "accepts_block": false,
    "hiden": false
  },
  "stop": {
    "introduced": "2,5,0",
    "returns": null,
    "alt_args": [],
    "summary": "Stop current thread or run",
    "args": [
      {
        "signal": ":boolean"
      }
    ],
    "name": "stop",
    "accepts_block": false,
    "hiden": false
  },
  "rand_i": {
    "introduced": "2,0,0",
    "accepts_block": false,
    "inline": true,
    "summary": "Generate a random whole number below a value (exclusive)",
    "args": [
      {
        "max": ":number_or_range"
      }
    ],
    "name": "rand_i",
    "signature": {
      "max": 2
    },
    "hiden": false
  },
  "density": {
    "introduced": "2,3,0",
    "accepts_block": true,
    "summary": "Squash and repeat time",
    "args": [
      {
        "d": ":density"
      }
    ],
    "name": "density",
    "async_block": true,
    "signature": {
      "&block": null,
      "d": null
    },
    "hiden": false,
    "requires_block": true
  },
  "time_now": {
    "introduced": "blend-sonic",
    "accepts_block": false,
    "summary": "return a number based on current time",
    "args": [],
    "name": "time_now",
    "signature": {},
    "hiden": false,
    "opts": {}
  },
  "dice": {
    "introduced": "2,0,0",
    "accepts_block": false,
    "inline": true,
    "summary": "Random dice throw",
    "args": [
      {
        "num_sides": ":number"
      }
    ],
    "name": "dice",
    "signature": {
      "num_sides": 6
    },
    "hiden": false
  },
  "rt": {
    "introduced": "2,0,0",
    "accepts_block": false,
    "inline": true,
    "summary": "Real time conversion",
    "args": [
      {
        "seconds": ":number"
      }
    ],
    "name": "rt",
    "signature": {
      "t": null
    },
    "hiden": false
  },
  "live_loop": {
    "introduced": "2,1,0",
    "accepts_block": true,
    "summary": "A loop for live coding",
    "args": [
      {
        "name": ":symbol"
      }
    ],
    "name": "live_loop",
    "intro_fn": true,
    "async_block": true,
    "signature": {
      "*args": null,
      "&block": null,
      "name": "nil"
    },
    "hiden": false,
    "requires_block": true,
    "opts": {
      "init": "",
      "seed": 0,
      "sync": ":foo",
      "sync_bpm": ":foo",
      "delay": 0,
      "auto_cue": true
    }
  },
  "define": {
    "introduced": "2,0,0",
    "accepts_block": true,
    "summary": "Define a new function",
    "args": [
      {
        "name": ":symbol"
      }
    ],
    "name": "define",
    "signature": {
      "&block": null,
      "name": null
    },
    "hiden": false,
    "requires_block": true,
    "intro_fn": true
  },
  "shuffle": {
    "introduced": "2,1,0",
    "accepts_block": false,
    "inline": true,
    "summary": "Randomise order of a list",
    "args": [],
    "name": "shuffle",
    "signature": {
      "list": null
    },
    "hiden": false,
    "alt_args": [
      {
        "list": ":array"
      }
    ]
  },
  "dec": {
    "introduced": "2, 1, 0",
    "accepts_block": false,
    "summary": "Decrement",
    "args": [
      {
        "n": ":number"
      }
    ],
    "name": "dec",
    "signature": {
      "n": null
    },
    "hiden": true,
    "opts": {}
  },
  "use_bpm_mul": {
    "introduced": "2,3,0",
    "accepts_block": false,
    "summary": "Set new tempo as a multiple of current tempo",
    "args": [
      {
        "mul": ":number"
      }
    ],
    "name": "use_bpm_mul",
    "signature": {
      "&block": null,
      "mul": null
    },
    "hiden": false
  },
  "with_random_seed": {
    "introduced": "2,0,0",
    "accepts_block": true,
    "summary": "Specify random seed for code block",
    "args": [
      {
        "seed": ":number"
      }
    ],
    "name": "with_random_seed",
    "signature": {
      "&block": null,
      "seed": null
    },
    "hiden": false,
    "requires_block": true
  },
  "one_in": {
    "introduced": "2,0,0",
    "accepts_block": false,
    "inline": true,
    "summary": "Random true value with specified probability",
    "args": [
      {
        "num": ":number"
      }
    ],
    "name": "one_in",
    "signature": {
      "num": null
    },
    "hiden": false
  },
  "rand_i_look": {
    "introduced": "2,11,0",
    "accepts_block": false,
    "inline": true,
    "summary": "Generate a random whole number without consuming a rand",
    "args": [
      {
        "max": ":number_or_range"
      }
    ],
    "name": "rand_i_look",
    "signature": {
      "*args": null
    },
    "hiden": false
  },
  "ndefine": {
    "introduced": "2,1,0",
    "accepts_block": true,
    "summary": "Define a new function",
    "args": [
      {
        "name": ":symbol"
      }
    ],
    "name": "ndefine",
    "signature": {
      "&block": null,
      "name": null
    },
    "hiden": true,
    "requires_block": true
  },
  "with_tempo": {
    "signature": {
      "*args": null,
      "&block": null
    },
    "hiden": true
  },
  "rrand_i": {
    "introduced": "2,0,0",
    "accepts_block": false,
    "inline": true,
    "summary": "Generate a random whole number between two points inclusively",
    "args": [
      {
        "min": ":number"
      },
      {
        "max": ":number"
      }
    ],
    "name": "rrand_i",
    "signature": {
      "max": null,
      "min": null
    },
    "hiden": false
  },
  "current_bpm": {
    "introduced": "2,0,0",
    "accepts_block": false,
    "summary": "Get current tempo",
    "hiden": true,
    "name": "current_bpm"
  },
  "with_bpm": {
    "introduced": "2,0,0",
    "accepts_block": true,
    "summary": "Set the tempo for the code block",
    "args": [
      {
        "bpm": ":number"
      }
    ],
    "name": "with_bpm",
    "signature": {
      "&block": null,
      "bpm": null
    },
    "hiden": false,
    "requires_block": true
  },
  "bt": {
    "introduced": "2,8,0",
    "accepts_block": false,
    "summary": "Beat time conversion",
    "args": [
      {
        "seconds": ":number"
      }
    ],
    "name": "bt",
    "signature": {
      "t": null
    },
    "hiden": true
  },
  "cue": {
    "introduced": "2,0,0",
    "accepts_block": false,
    "summary": "Cue other threads",
    "args": [
      {
        "cue_id": ":symbol"
      }
    ],
    "name": "cue",
    "signature": {
      "cue_id": null,
      "*opts": null
    },
    "hiden": false,
    "opts": {
      "another_key": "foo: 64",
      "key": "foo: 64",
      "your_key": ":bar"
    }
  },
  "sleep": {
    "introduced": "2,0,0",
    "accepts_block": false,
    "alt_args": [
      {
        "beats": ":number"
      }
    ],
    "summary": "Wait for beat duration",
    "args": [],
    "name": "sleep",
    "advances_time": true,
    "signature": {
      "beats": null
    },
    "hiden": false
  },
  "sync_bpm": {
    "introduced": "2,10,0",
    "accepts_block": false,
    "summary": "Sync and inherit BPM from other threads ",
    "args": [
      {
        "cue_id": ":symbol"
      }
    ],
    "name": "sync_bpm",
    "advances_time": true,
    "signature": {
      "opts": "{}",
      "cue_ids": null
    },
    "hiden": false,
    "opts": {}
  },
  "spread": {
    "introduced": "2,4,0",
    "returns": ":ring",
    "inline": true,
    "summary": "Euclidean distribution for beats",
    "args": [
      {
        "num_accents": ":number"
      },
      {
        "size": ":number"
      }
    ],
    "name": "spread",
    "accepts_block": false,
    "signature": {
      "size": null,
      "num_accents": null,
      "*args": null
    },
    "hiden": false,
    "opts": {
      "rotate": false
    }
  },
  "quantise": {
    "introduced": "2,1,0",
    "accepts_block": false,
    "inline": true,
    "summary": "Quantise a value to resolution",
    "args": [
      {
        "n": ":number"
      },
      {
        "step": ":positive_number"
      }
    ],
    "name": "quantise",
    "signature": {
      "step": null,
      "n": null
    },
    "hiden": false
  },
  "use_random_seed": {
    "introduced": "2,0,0",
    "accepts_block": false,
    "summary": "Set random seed generator to known seed",
    "args": [
      {
        "seed": ":number"
      }
    ],
    "name": "use_random_seed",
    "signature": {
      "&block": null,
      "seed": null
    },
    "hiden": false
  },
  "version": {
    "introduced": "2,0,0",
    "accepts_block": false,
    "summary": "Get current version information",
    "hiden": true,
    "name": "version"
  },
  "rand_skip": {
    "introduced": "2,7,0",
    "accepts_block": false,
    "summary": "Jump forward random generator",
    "args": [
      {
        "amount": ":number"
      }
    ],
    "name": "rand_skip",
    "signature": {
      "amount": 1
    },
    "hiden": false
  },
  "rand_look": {
    "introduced": "2,11,0",
    "accepts_block": false,
    "inline": true,
    "summary": "Generate a random number without consuming a rand",
    "args": [
      {
        "max": ":number_or_range"
      }
    ],
    "name": "rand_look",
    "signature": {
      "*args": null
    },
    "hiden": false
  },
  "vt": {
    "introduced": "2,1,0",
    "accepts_block": false,
    "inline": true,
    "summary": "Get virtual time",
    "name": "vt",
    "hiden": false
  },
  "assert": {
    "introduced": "2,8,0",
    "accepts_block": false,
    "alt_args": [],
    "summary": "Ensure arg is valid",
    "args": [
      {
        "is_true": ":boolean"
      }
    ],
    "name": "assert",
    "signature": {
      "arg": null,
      "msg": "nil"
    },
    "hiden": false
  },
  "load_example": {
    "introduced": "2,10,0",
    "accepts_block": false,
    "summary": "Load a built-in example",
    "args": [
      {
        "path": ":string"
      }
    ],
    "name": "load_example",
    "signature": {
      "example_name": null
    },
    "hiden": true
  },
  "line": {
    "introduced": "2,5,0",
    "returns": ":ring",
    "inline": true,
    "summary": "Create a ring buffer representing a straight line",
    "args": [
      {
        "start": ":number"
      },
      {
        "finish": ":number"
      }
    ],
    "name": "line",
    "accepts_block": false,
    "memoize": true,
    "signature": {
      "start": null,
      "*args": null,
      "finish": null
    },
    "hiden": false,
    "opts": {
      "inclusive": false,
      "steps": 1
    }
  },
  "note_list": {
    "introduced": "blend-sonic",
    "accepts_block": false,
    "summary": "Make a list of notes",
    "args": [],
    "name": "note_list",
    "signature": {},
    "hiden": false,
    "opts": {}
  },
  "rand_back": {
    "introduced": "2,7,0",
    "accepts_block": false,
    "summary": "Roll back random generator",
    "args": [
      {
        "amount": ":number"
      }
    ],
    "name": "rand_back",
    "signature": {
      "amount": 1
    },
    "hiden": false
  },
  "assert_equal": {
    "introduced": "2,8,0",
    "accepts_block": false,
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
    "summary": "Ensure args are equal",
    "args": [
      {
        "arg1": ":anything"
      },
      {
        "arg2": ":anything"
      }
    ],
    "name": "assert_equal",
    "signature": {
      "msg": "nil",
      "arg2": null,
      "arg1": null
    },
    "hiden": false
  },
  "rand": {
    "introduced": "2,0,0",
    "accepts_block": false,
    "inline": true,
    "summary": "Generate a random float below a value",
    "args": [
      {
        "max": ":number_or_range"
      }
    ],
    "name": "rand",
    "signature": {
      "max": 1
    },
    "hiden": false,
    "intro_fn": true
  },
  "in_thread": {
    "introduced": "2,0,0",
    "accepts_block": true,
    "summary": "Run code block at the same time",
    "name": "in_thread",
    "async_block": true,
    "signature": {
      "*opts": null,
      "&block": null
    },
    "hiden": false,
    "requires_block": true,
    "opts": {
      "delay": 0,
      "sync": ":foo",
      "sync_bpm": ":foo",
      "name": ":foo"
    }
  },
  "time_shift": {
    "introduced": "2,11,0",
    "returns": null,
    "summary": "Slide time forwards or backwards for the given block",
    "args": [
      {
        "delta_time": ":number"
      }
    ],
    "name": "time_shift",
    "accepts_block": true,
    "signature": {
      "&blk": null,
      "delta": null
    },
    "hiden": false,
    "requires_block": true
  }
}

#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/

lang_sound = {
  "use_sample_bpm": {
    "introduced": "2,1,0",
    "accepts_block": false,
    "alt_args": [
      {
        "string_or_number": ":sample_name_or_duration"
      }
    ],
    "summary": "Sample-duration-based bpm modification",
    "args": [],
    "name": "use_sample_bpm",
    "signature": {
      "sample_name": null,
      "*args": null
    },
    "hiden": false,
    "opts": {
      "num_beats": 1
    }
  },
  "current_octave": {
    "introduced": "2,9,0",
    "accepts_block": false,
    "summary": "Get current octave shift",
    "hiden": true,
    "name": "current_octave"
  },
  "sample": {
    "introduced": "2,0,0",
    "accepts_block": true,
    "alt_args": [
      {
        "name_or_path": ":symbol_or_string"
      }
    ],
    "summary": "Trigger sample",
    "signature": {
      "*args": null,
      "&blk": null
    },
    "opts": {
      "hpf_max": 200,
      "sustain": 1,
      "lpf_sustain_level": 0,
      "onset": 0,
      "relax_time": 0,
      "lpf_attack_level": 0,
      "finish": 1,
      "rpitch": 0,
      "hpf": 0,
      "amp": 1,
      "threshold": 0,
      "pitch_stretch": 1,
      "hpf_attack": 0,
      "lpf_attack": 0,
      "lpf_release": 0,
      "window_size": 0,
      "time_dis": 0,
      "lpf_release_level": 0,
      "hpf_sustain_level": 0,
      "lpf_sustain": 0,
      "start": 0,
      "lpf_decay": 0,
      "slide": 0,
      "slope_above": 1,
      "hpf_env_curve": 1,
      "hpf_release": 0,
      "hpf_sustain": 0,
      "lpf": 131,
      "hpf_decay_level": 0,
      "norm": 0,
      "clamp_time": 0,
      "lpf_decay_level": 0,
      "hpf_init_level": 130,
      "slope_below": 1,
      "lpf_init_level": 30,
      "rate": 1,
      "pitch": 0,
      "pre_amp": 1,
      "attack": 0,
      "hpf_decay": 0,
      "path": "/path/to/file",
      "hpf_release_level": 0,
      "pitch_dis": 0,
      "beat_stretch": 1,
      "pan": 0,
      "release": 0,
      "hpf_attack_level": 0,
      "compress": 0,
      "lpf_min": 30,
      "lpf_env_curve": 1
    },
    "args": [],
    "name": "sample",
    "async_block": true,
    "requires_block": false,
    "hiden": false,
    "intro_fn": true
  },
  "with_debug": {
    "introduced": "2,0,0",
    "accepts_block": true,
    "summary": "Block-level enable and disable debug",
    "args": [
      {
        "true_or_false": ":boolean"
      }
    ],
    "name": "with_debug",
    "signature": {
      "&block": null,
      "v": null
    },
    "hiden": false,
    "requires_block": true
  },
  "use_cent_tuning": {
    "introduced": "2,9,0",
    "accepts_block": false,
    "summary": "Cent tuning",
    "args": [
      {
        "cent_shift": ":number"
      }
    ],
    "name": "use_cent_tuning",
    "signature": {
      "&block": null,
      "shift": null
    },
    "hiden": false,
    "intro_fn": true
  },
  "recording_start": {
    "introduced": "2,0,0",
    "accepts_block": false,
    "summary": "Start recording",
    "hiden": true,
    "name": "recording_start"
  },
  "kill": {
    "introduced": "2,0,0",
    "accepts_block": false,
    "summary": "Kill synth",
    "args": [
      {
        "node": ":synth_node"
      }
    ],
    "name": "kill",
    "signature": {
      "node": null
    },
    "hiden": false,
    "opts": {}
  },
  "with_transpose": {
    "introduced": "2,0,0",
    "accepts_block": true,
    "summary": "Block-level note transposition",
    "args": [
      {
        "note_shift": ":number"
      }
    ],
    "name": "with_transpose",
    "signature": {
      "&block": null,
      "shift": null
    },
    "hiden": false,
    "requires_block": true
  },
  "should_trigger": {
    "signature": {
      "args_h": null
    },
    "hiden": false
  },
  "with_fx": {
    "introduced": "2,0,0",
    "accepts_block": true,
    "alt_args": [
      {
        "fx_name": ":symbol"
      }
    ],
    "summary": "Use Studio FX",
    "signature": {
      "fx_name": null,
      "*args": null,
      "&block": null
    },
    "opts": {
      "reps": 1,
      "kill_delay": 1
    },
    "args": [],
    "name": "with_fx",
    "async_block": true,
    "requires_block": true,
    "hiden": true,
    "intro_fn": true
  },
  "use_timing_warnings": {
    "signature": {
      "&block": null,
      "v": null
    },
    "hiden": true
  },
  "with_octave": {
    "introduced": "2,9,0",
    "accepts_block": true,
    "summary": "Block level octave transposition",
    "args": [
      {
        "octave_shift": ":number"
      }
    ],
    "name": "with_octave",
    "signature": {
      "&block": null,
      "shift": null
    },
    "hiden": false,
    "intro_fn": true,
    "requires_block": true
  },
  "scale": {
    "introduced": "2,0,0",
    "returns": ":ring",
    "inline": true,
    "summary": "Create scale",
    "accepts_block": false,
    "signature": {
      "tonic_or_name": null,
      "*opts": null
    },
    "alt_args": [
      {
        "tonic": ":symbol"
      },
      {
        "scale": ":symbol"
      }
    ],
    "opts": {
      "num_octaves": 1
    },
    "memoize": true,
    "args": [],
    "name": "scale",
    "hiden": false,
    "intro_fn": true
  },
  "current_sched_ahead_time": {
    "introduced": "2,0,0",
    "accepts_block": false,
    "summary": "Get current sched ahead time",
    "hiden": true,
    "name": "current_sched_ahead_time"
  },
  "status": {
    "introduced": "2,0,0",
    "accepts_block": false,
    "summary": "Get server status",
    "hiden": true,
    "name": "status"
  },
  "set_mixer_control": {
    "introduced": "2,7,0",
    "accepts_block": false,
    "summary": "Control master mixer",
    "name": "set_mixer_control!",
    "signature": {
      "opts": null
    },
    "hiden": false,
    "modifies_env": true,
    "opts": {
      "leak_dc_bypass": 0,
      "pre_amp": 1,
      "lpf": 131,
      "limiter_bypass": 0,
      "amp": 1,
      "lpf_bypass": 0,
      "hpf_bypass": 0,
      "hpf": 0
    }
  },
  "use_fx": {
    "signature": {
      "*args": null,
      "&block": null
    },
    "hiden": true
  },
  "current_arg_checks": {
    "introduced": "2,0,0",
    "accepts_block": false,
    "summary": "Get current arg checking status",
    "hiden": true,
    "name": "current_arg_checks"
  },
  "use_merged_sample_defaults": {
    "introduced": "2,9,0",
    "accepts_block": false,
    "summary": "Merge new sample defaults",
    "name": "use_merged_sample_defaults",
    "signature": {
      "*args": null,
      "&block": null
    },
    "hiden": false,
    "opts": {}
  },
  "with_cent_tuning": {
    "introduced": "2,9,0",
    "accepts_block": true,
    "summary": "Block-level cent tuning",
    "args": [
      {
        "cent_shift": ":number"
      }
    ],
    "name": "with_cent_tuning",
    "signature": {
      "&block": null,
      "shift": null
    },
    "hiden": false,
    "requires_block": true
  },
  "midi_to_hz": {
    "introduced": "2,0,0",
    "accepts_block": false,
    "inline": true,
    "summary": "MIDI to Hz conversion",
    "args": [
      {
        "note": ":symbol_or_number"
      }
    ],
    "name": "midi_to_hz",
    "signature": {
      "n": null
    },
    "hiden": false
  },
  "use_synth": {
    "introduced": "2,0,0",
    "accepts_block": false,
    "summary": "Switch current synth",
    "args": [
      {
        "synth_name": ":symbol"
      }
    ],
    "name": "use_synth",
    "signature": {
      "*args": null,
      "&block": null,
      "synth_name": null
    },
    "hiden": true,
    "intro_fn": true
  },
  "with_merged_sample_defaults": {
    "introduced": "2,9,0",
    "accepts_block": true,
    "summary": "Block-level use merged sample defaults",
    "name": "with_merged_sample_defaults",
    "signature": {
      "*args": null,
      "&block": null
    },
    "hiden": false,
    "requires_block": true,
    "opts": {}
  },
  "invert_chord": {
    "signature": {
      "*args": null
    },
    "hiden": true
  },
  "control": {
    "introduced": "2,0,0",
    "accepts_block": false,
    "summary": "Control running synth",
    "args": [
      {
        "node": ":synth_node"
      }
    ],
    "name": "control",
    "signature": {
      "*args": null
    },
    "hiden": false,
    "opts": {}
  },
  "with_timing_warnings": {
    "signature": {
      "&block": null,
      "v": null
    },
    "hiden": true
  },
  "set_mixer_stereo_mode!": {
    "hiden": false
  },
  "current_synth_defaults": {
    "introduced": "2,0,0",
    "accepts_block": false,
    "summary": "Get current synth defaults",
    "hiden": true,
    "name": "current_synth_defaults"
  },
  "with_afx": {
    "signature": {
      "fx_name": null,
      "*args": null,
      "&block": null
    },
    "hiden": true
  },
  "pitch_ratio": {
    "signature": {
      "*args": null
    },
    "hiden": true
  },
  "start_amp_monitor": {
    "hiden": true
  },
  "fx_names": {
    "introduced": "2,10,0",
    "accepts_block": false,
    "memoize": true,
    "name": "fx_names",
    "summary": "Get all FX names",
    "hiden": true
  },
  "midi_notes": {
    "introduced": "2,7,0",
    "returns": ":ring",
    "inline": true,
    "summary": "Create a ring buffer of midi note numbers",
    "args": [
      {
        "list": ":array"
      }
    ],
    "name": "midi_notes",
    "accepts_block": false,
    "memoize": true,
    "signature": {
      "*args": null
    },
    "hiden": false
  },
  "pitch_to_ratio": {
    "introduced": "2,5,0",
    "accepts_block": false,
    "inline": true,
    "summary": "relative MIDI pitch to frequency ratio",
    "args": [
      {
        "pitch": ":midi_number"
      }
    ],
    "name": "pitch_to_ratio",
    "signature": {
      "m": null
    },
    "hiden": false
  },
  "sample_duration": {
    "introduced": "2,0,0",
    "accepts_block": false,
    "summary": "Get duration of sample in beats",
    "args": [
      {
        "path": ":string"
      }
    ],
    "name": "sample_duration",
    "signature": {
      "*args": null
    },
    "hiden": true,
    "opts": {
      "start": 0,
      "attack": 0,
      "sustain": 1,
      "beat_stretch": 1,
      "pitch_stretch": 1,
      "decay": 0,
      "release": 0,
      "finish": 1,
      "rpitch": 0,
      "rate": 1
    }
  },
  "octs": {
    "introduced": "2,8,0",
    "returns": ":ring",
    "inline": true,
    "summary": "Create a ring of octaves",
    "args": [
      {
        "start": ":note"
      },
      {
        "num_octaves": ":pos_int"
      }
    ],
    "name": "octs",
    "accepts_block": false,
    "signature": {
      "start": null,
      "num_octs": 1
    },
    "hiden": false
  },
  "set_cent_tuning": {
    "introduced": "2,10,0",
    "accepts_block": false,
    "summary": "Global Cent tuning",
    "args": [
      {
        "cent_shift": ":number"
      }
    ],
    "name": "set_cent_tuning!",
    "signature": {
      "shift": null
    },
    "hiden": false,
    "modifies_env": true,
    "intro_fn": false
  },
  "load_sample": {
    "introduced": "2,0,0",
    "accepts_block": false,
    "summary": "Pre-load first matching sample",
    "args": [
      {
        "path": ":string"
      }
    ],
    "name": "load_sample",
    "signature": {
      "*args": null
    },
    "hiden": true
  },
  "chord_degree": {
    "introduced": "2,1,0",
    "returns": ":ring",
    "inline": true,
    "summary": "Construct chords of stacked thirds, based on scale degrees",
    "args": [
      {
        "number_of_notes": ":int"
      }
    ],
    "name": "chord_degree",
    "accepts_block": false,
    "memoize": true,
    "signature": {
      "degree": null,
      "tonic": null,
      "number_of_notes": 4,
      "scale": ":major",
      "*opts": null
    },
    "hiden": false,
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
  "use_merged_synth_defaults": {
    "introduced": "2,0,0",
    "accepts_block": false,
    "summary": "Merge synth defaults",
    "name": "use_merged_synth_defaults",
    "signature": {
      "*args": null,
      "&block": null
    },
    "hiden": false,
    "opts": {}
  },
  "sample_buffer": {
    "introduced": "2,0,0",
    "accepts_block": false,
    "summary": "Get sample data",
    "args": [
      {
        "path": ":string"
      }
    ],
    "name": "sample_buffer",
    "signature": {
      "*args": null
    },
    "hiden": true
  },
  "with_merged_synth_defaults": {
    "introduced": "2,0,0",
    "accepts_block": true,
    "summary": "Block-level merge synth defaults",
    "name": "with_merged_synth_defaults",
    "signature": {
      "*args": null,
      "&block": null
    },
    "hiden": true,
    "requires_block": true,
    "opts": {}
  },
  "use_octave": {
    "introduced": "2,9,0",
    "accepts_block": false,
    "summary": "Note octave transposition",
    "args": [
      {
        "octave_shift": ":number"
      }
    ],
    "name": "use_octave",
    "signature": {
      "&block": null,
      "shift": null
    },
    "hiden": false,
    "intro_fn": true
  },
  "load_sample_at_path": {
    "signature": {
      "path": null
    },
    "hiden": true
  },
  "current_volume": {
    "introduced": "2,0,0",
    "accepts_block": false,
    "summary": "Get current volume",
    "hiden": true,
    "name": "current_volume"
  },
  "with_tuning": {
    "introduced": "2,6,0",
    "accepts_block": true,
    "summary": "Block-level tuning modification",
    "args": [
      {
        "tuning": ":symbol"
      },
      {
        "fundamental_note": ":symbol_or_number"
      }
    ],
    "name": "with_tuning",
    "signature": {
      "fundamental_note": ":c",
      "tuning": null,
      "&block": null
    },
    "hiden": false,
    "requires_block": true
  },
  "recording_delete": {
    "accepts_block": false,
    "hiden": true,
    "name": "recording_delete"
  },
  "sample_info": {
    "introduced": "2,0,0",
    "accepts_block": false,
    "summary": "Get sample information",
    "args": [
      {
        "path": ":string"
      }
    ],
    "name": "sample_info",
    "signature": {
      "*args": null
    },
    "hiden": true
  },
  "all_sample_names": {
    "introduced": "2,0,0",
    "accepts_block": false,
    "memoize": true,
    "name": "all_sample_names",
    "summary": "Get all sample names",
    "hiden": true
  },
  "recording_stop": {
    "introduced": "2,0,0",
    "accepts_block": false,
    "summary": "Stop recording",
    "hiden": true,
    "name": "recording_stop"
  },
  "sample_paths": {
    "introduced": "2,10,0",
    "returns": ":ring",
    "summary": "Sample Pack Filter Resolution",
    "args": [
      {
        "pre_args": ":source_and_filter_types"
      }
    ],
    "name": "sample_paths",
    "accepts_block": false,
    "signature": {
      "*args": null
    },
    "hiden": true
  },
  "use_arg_checks": {
    "introduced": "2,0,0",
    "accepts_block": false,
    "summary": "Enable and disable arg checks",
    "args": [
      {
        "true_or_false": ":boolean"
      }
    ],
    "name": "use_arg_checks",
    "signature": {
      "&block": null,
      "v": null
    },
    "hiden": false
  },
  "current_sample_defaults": {
    "introduced": "2,5,0",
    "accepts_block": false,
    "summary": "Get current sample defaults",
    "hiden": true,
    "name": "current_sample_defaults"
  },
  "use_timing_guarantees": {
    "introduced": "2,10,0",
    "accepts_block": false,
    "summary": "Inhibit synth triggers if too late",
    "args": [
      {
        "bool": ":true_or_false"
      }
    ],
    "name": "use_timing_guarantees",
    "signature": {
      "&block": null,
      "v": null
    },
    "hiden": false,
    "requires_block": false
  },
  "truthy": {
    "signature": {
      "val": null
    },
    "hiden": false
  },
  "hz_to_midi": {
    "introduced": "2,0,0",
    "accepts_block": false,
    "inline": true,
    "summary": "Hz to MIDI conversion",
    "args": [
      {
        "freq": ":number"
      }
    ],
    "name": "hz_to_midi",
    "signature": {
      "freq": null
    },
    "hiden": false
  },
  "current_transpose": {
    "introduced": "2,0,0",
    "accepts_block": false,
    "summary": "Get current transposition",
    "hiden": true,
    "name": "current_transpose"
  },
  "current_amp": {
    "hiden": true
  },
  "load_synthdefs": {
    "introduced": "2,0,0",
    "accepts_block": false,
    "summary": "Load external synthdefs",
    "args": [
      {
        "path": ":string"
      }
    ],
    "name": "load_synthdefs",
    "signature": {
      "path": "synthdef_path"
    },
    "hiden": true
  },
  "current_cent_tuning": {
    "introduced": "2,9,0",
    "accepts_block": false,
    "summary": "Get current cent shift",
    "hiden": true,
    "name": "current_cent_tuning"
  },
  "sample_split_filts_and_opts": {
    "signature": {
      "args": null
    },
    "hiden": true
  },
  "play_pattern_timed": {
    "introduced": "2,0,0",
    "accepts_block": false,
    "summary": "Play pattern of notes with specific times",
    "args": [
      {
        "notes": ":list"
      },
      {
        "times": ":list_or_number"
      }
    ],
    "name": "play_pattern_timed",
    "signature": {
      "times": null,
      "notes": null,
      "*args": null
    },
    "hiden": false,
    "opts": {
      "attack": 0,
      "sustain": 1,
      "decay": 0,
      "amp_slide": 1,
      "decay_level": 1,
      "sustain_level": 1,
      "amp": 1,
      "on": 1,
      "env_curve": 1,
      "pan": 0,
      "release": 0,
      "pitch": 0,
      "pan_slide": 1,
      "attack_level": 1,
      "slide": 0
    }
  },
  "with_arg_bpm_scaling": {
    "introduced": "2,0,0",
    "accepts_block": true,
    "summary": "Block-level enable and disable BPM scaling",
    "name": "with_arg_bpm_scaling",
    "signature": {
      "&block": null,
      "bool": null
    },
    "hiden": false,
    "requires_block": true
  },
  "use_external_synths": {
    "signature": {
      "&block": null,
      "v": null
    },
    "hiden": true
  },
  "use_synth_defaults": {
    "introduced": "2,0,0",
    "accepts_block": false,
    "summary": "Use new synth defaults",
    "name": "use_synth_defaults",
    "signature": {
      "*args": null,
      "&block": null
    },
    "hiden": true,
    "opts": {}
  },
  "play_pattern": {
    "introduced": "2,0,0",
    "accepts_block": false,
    "summary": "Play pattern of notes",
    "args": [
      {
        "notes": ":list"
      }
    ],
    "name": "play_pattern",
    "signature": {
      "*args": null,
      "notes": null
    },
    "hiden": false,
    "opts": {}
  },
  "rest": {
    "introduced": "2,1,0",
    "accepts_block": false,
    "summary": "Determine if note or args is a rest",
    "args": [
      {
        "note_or_args": ":number_symbol_or_map"
      }
    ],
    "name": "rest?",
    "signature": {
      "n": null
    },
    "hiden": false
  },
  "ratio_to_pitch": {
    "introduced": "2,7,0",
    "accepts_block": false,
    "inline": true,
    "summary": "relative frequency ratio to MIDI pitch",
    "args": [
      {
        "ratio": ":number"
      }
    ],
    "name": "ratio_to_pitch",
    "signature": {
      "r": null
    },
    "hiden": false
  },
  "play": {
    "introduced": "2,0,0",
    "accepts_block": true,
    "summary": "Play current synth",
    "args": [
      {
        "note": ":symbol_or_number"
      }
    ],
    "name": "play",
    "requires_block": false,
    "async_block": true,
    "signature": {
      "*args": null,
      "&blk": null,
      "n": null
    },
    "hiden": false,
    "intro_fn": true,
    "opts": {
      "attack": 0,
      "sustain": 1,
      "decay": 0,
      "amp_slide": 1,
      "decay_level": 1,
      "sustain_level": 1,
      "amp": 1,
      "on": 1,
      "env_curve": 1,
      "pan": 0,
      "release": 0,
      "pitch": 0,
      "pan_slide": 1,
      "attack_level": 1,
      "slide": 0
    }
  },
  "play_chord": {
    "introduced": "2,0,0",
    "accepts_block": false,
    "summary": "Play notes simultaneously",
    "args": [
      {
        "notes": ":list"
      }
    ],
    "name": "play_chord",
    "signature": {
      "*args": null,
      "notes": null
    },
    "hiden": false,
    "opts": {
      "attack": 0,
      "sustain": 1,
      "decay": 0,
      "amp_slide": 1,
      "decay_level": 1,
      "sustain_level": 1,
      "amp": 1,
      "on": 1,
      "env_curve": 1,
      "pan": 0,
      "release": 0,
      "pitch": 0,
      "pan_slide": 1,
      "attack_level": 1,
      "slide": 0
    }
  },
  "chord_invert": {
    "introduced": "2,6,0",
    "returns": ":ring",
    "inline": true,
    "summary": "Chord inversion",
    "args": [
      {
        "notes": ":list"
      },
      {
        "shift": ":number"
      }
    ],
    "name": "chord_invert",
    "accepts_block": false,
    "signature": {
      "shift": null,
      "notes": null
    },
    "hiden": false
  },
  "with_synth": {
    "introduced": "2,0,0",
    "accepts_block": true,
    "summary": "Block-level synth switching",
    "args": [
      {
        "synth_name": ":symbol"
      }
    ],
    "name": "with_synth",
    "signature": {
      "*args": null,
      "&block": null,
      "synth_name": null
    },
    "hiden": true,
    "requires_block": true
  },
  "with_arg_checks": {
    "introduced": "2,0,0",
    "accepts_block": true,
    "summary": "Block-level enable and disable arg checks",
    "args": [
      {
        "true_or_false": ":boolean"
      }
    ],
    "name": "with_arg_checks",
    "signature": {
      "&block": null,
      "v": null
    },
    "hiden": false,
    "requires_block": true
  },
  "with_sample_bpm": {
    "introduced": "2,1,0",
    "accepts_block": true,
    "summary": "Block-scoped sample-duration-based bpm modification",
    "args": [
      {
        "string_or_number": ":sample_name_or_duration"
      }
    ],
    "name": "with_sample_bpm",
    "signature": {
      "sample_name": null,
      "*args": null,
      "&block": null
    },
    "hiden": false,
    "requires_block": true,
    "opts": {
      "num_beats": 1
    }
  },
  "current_synth": {
    "introduced": "2,0,0",
    "accepts_block": false,
    "summary": "Get current synth",
    "hiden": true,
    "name": "current_synth"
  },
  "use_sample_defaults": {
    "introduced": "2,5,0",
    "accepts_block": false,
    "summary": "Use new sample defaults",
    "name": "use_sample_defaults",
    "signature": {
      "*args": null,
      "&block": null
    },
    "hiden": false,
    "opts": {
      "hpf_max": 200,
      "sustain": 1,
      "lpf_sustain_level": 0,
      "onset": 0,
      "relax_time": 0,
      "lpf_attack_level": 0,
      "finish": 1,
      "rpitch": 0,
      "hpf": 0,
      "amp": 1,
      "threshold": 0,
      "pitch_stretch": 1,
      "hpf_attack": 0,
      "lpf_attack": 0,
      "lpf_release": 0,
      "window_size": 0,
      "time_dis": 0,
      "lpf_release_level": 0,
      "hpf_sustain_level": 0,
      "lpf_sustain": 0,
      "start": 0,
      "lpf_decay": 0,
      "slide": 0,
      "slope_above": 1,
      "hpf_env_curve": 1,
      "hpf_release": 0,
      "hpf_sustain": 0,
      "lpf": 131,
      "hpf_decay_level": 0,
      "norm": 0,
      "clamp_time": 0,
      "lpf_decay_level": 0,
      "hpf_init_level": 130,
      "slope_below": 1,
      "lpf_init_level": 30,
      "rate": 1,
      "pitch": 0,
      "pre_amp": 1,
      "attack": 0,
      "hpf_decay": 0,
      "path": "/path/to/file",
      "hpf_release_level": 0,
      "pitch_dis": 0,
      "beat_stretch": 1,
      "pan": 0,
      "release": 0,
      "hpf_attack_level": 0,
      "compress": 0,
      "lpf_min": 30,
      "lpf_env_curve": 1
    }
  },
  "chord_names": {
    "introduced": "2,6,0",
    "accepts_block": false,
    "memoize": true,
    "name": "chord_names",
    "summary": "All chord names",
    "hiden": true
  },
  "chord": {
    "introduced": "2,0,0",
    "returns": ":ring",
    "inline": true,
    "summary": "Create chord",
    "accepts_block": false,
    "signature": {
      "tonic_or_name": null,
      "*opts": null
    },
    "alt_args": [
      {
        "tonic": ":symbol"
      },
      {
        "chord": ":symbol"
      }
    ],
    "opts": {
      "num_octaves": 1,
      "invert": 0
    },
    "memoize": true,
    "args": [],
    "name": "chord",
    "hiden": false,
    "intro_fn": true
  },
  "sample_loaded": {
    "introduced": "2,2,0",
    "accepts_block": false,
    "summary": "Test if sample was pre-loaded",
    "args": [
      {
        "path": ":string"
      }
    ],
    "name": "sample_loaded?",
    "signature": {
      "*args": null
    },
    "hiden": false
  },
  "note": {
    "introduced": "2,0,0",
    "accepts_block": false,
    "alt_args": [
      {
        "note": ":symbol"
      }
    ],
    "summary": "Describe note",
    "args": [],
    "name": "note",
    "signature": {
      "*args": null,
      "n": null
    },
    "hiden": false,
    "opts": {}
  },
  "set_sched_ahead_time": {
    "introduced": "2,0,0",
    "accepts_block": false,
    "summary": "Set sched ahead time globally",
    "args": [
      {
        "time": ":number"
      }
    ],
    "name": "set_sched_ahead_time!",
    "signature": {
      "t": null
    },
    "hiden": false,
    "modifies_env": true
  },
  "set_mixer_mono_mode!": {
    "hiden": false
  },
  "note_info": {
    "introduced": "2,0,0",
    "accepts_block": false,
    "summary": "Get note info",
    "args": [
      {
        "note": ":symbol_or_number"
      }
    ],
    "name": "note_info",
    "signature": {
      "*args": null,
      "n": null
    },
    "hiden": true,
    "opts": {
      "octave": 4
    }
  },
  "resolve_sample_paths": {
    "signature": {
      "filts_and_sources": null
    },
    "hiden": true
  },
  "with_synth_defaults": {
    "introduced": "2,0,0",
    "accepts_block": true,
    "summary": "Block-level use new synth defaults",
    "name": "with_synth_defaults",
    "signature": {
      "*args": null,
      "&block": null
    },
    "hiden": true,
    "requires_block": true,
    "opts": {}
  },
  "degree": {
    "introduced": "2,1,0",
    "accepts_block": false,
    "inline": true,
    "summary": "Convert a degree into a note",
    "args": [],
    "name": "degree",
    "signature": {
      "degree": null,
      "tonic": null,
      "scale": null
    },
    "hiden": false,
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
  "sample_free": {
    "introduced": "2,9,0",
    "returns": null,
    "summary": "Free a sample on the synth server",
    "args": [
      {
        "path": ":string"
      }
    ],
    "name": "sample_free",
    "accepts_block": false,
    "signature": {
      "*paths": null
    },
    "hiden": false
  },
  "current_debug": {
    "introduced": "2,0,0",
    "accepts_block": false,
    "summary": "Get current debug status",
    "hiden": true,
    "name": "current_debug"
  },
  "use_transpose": {
    "introduced": "2,0,0",
    "accepts_block": false,
    "summary": "Note transposition",
    "args": [
      {
        "note_shift": ":number"
      }
    ],
    "name": "use_transpose",
    "signature": {
      "&block": null,
      "shift": null
    },
    "hiden": false,
    "intro_fn": true
  },
  "time_now": {
    "introduced": "blend-sonic",
    "accepts_block": false,
    "summary": "return a number based on current time",
    "args": [],
    "name": "time_now",
    "signature": {},
    "hiden": false,
    "opts": {}
  },
  "set_mixer_invert_stereo!": {
    "hiden": false
  },
  "reset_mixer": {
    "introduced": "2,9,0",
    "accepts_block": false,
    "summary": "Reset master mixer",
    "name": "reset_mixer!",
    "signature": {
      "": null
    },
    "hiden": false,
    "modifies_env": true,
    "opts": {}
  },
  "scale_names": {
    "introduced": "2,6,0",
    "accepts_block": false,
    "memoize": true,
    "name": "scale_names",
    "summary": "All scale names",
    "hiden": true
  },
  "use_tuning": {
    "introduced": "2,6,0",
    "accepts_block": false,
    "summary": "Use alternative tuning systems",
    "args": [
      {
        "tuning": ":symbol"
      },
      {
        "fundamental_note": ":symbol_or_number"
      }
    ],
    "name": "use_tuning",
    "signature": {
      "fundamental_note": ":c",
      "tuning": null,
      "&block": null
    },
    "hiden": false
  },
  "use_arg_bpm_scaling": {
    "introduced": "2,0,0",
    "accepts_block": false,
    "summary": "Enable and disable BPM scaling",
    "args": [
      {
        "bool": ":boolean"
      }
    ],
    "name": "use_arg_bpm_scaling",
    "signature": {
      "&block": null,
      "bool": null
    },
    "hiden": false
  },
  "synth_names": {
    "introduced": "2,9,0",
    "accepts_block": false,
    "memoize": true,
    "name": "synth_names",
    "summary": "Get all synth names",
    "hiden": true
  },
  "sample_names": {
    "introduced": "2,0,0",
    "returns": ":ring",
    "summary": "Get sample names",
    "args": [
      {
        "group": ":symbol"
      }
    ],
    "name": "sample_names",
    "accepts_block": false,
    "memoize": true,
    "signature": {
      "group": null
    },
    "hiden": true
  },
  "sample_groups": {
    "introduced": "2,0,0",
    "accepts_block": false,
    "memoize": true,
    "name": "sample_groups",
    "summary": "Get all sample groups",
    "hiden": true
  },
  "with_timing_guarantees": {
    "introduced": "2,10,0",
    "accepts_block": true,
    "summary": "Block-scoped inhibition of synth triggers if too late",
    "args": [
      {
        "bool": ":true_or_false"
      }
    ],
    "name": "with_timing_guarantees",
    "signature": {
      "&block": null,
      "v": null
    },
    "hiden": false,
    "requires_block": true
  },
  "load_samples": {
    "introduced": "2,0,0",
    "accepts_block": false,
    "summary": "Pre-load all matching samples",
    "args": [
      {
        "paths": ":list"
      }
    ],
    "name": "load_samples",
    "signature": {
      "*args": null
    },
    "hiden": false
  },
  "sample_free_all": {
    "introduced": "2,9,0",
    "returns": null,
    "summary": "Free all loaded samples on the synth server",
    "args": [],
    "name": "sample_free_all",
    "accepts_block": false,
    "hiden": false
  },
  "note_list": {
    "introduced": "blend-sonic",
    "accepts_block": false,
    "summary": "Make a list of notes",
    "args": [],
    "name": "note_list",
    "signature": {},
    "hiden": false,
    "opts": {}
  },
  "resolve_sample_path": {
    "signature": {
      "filts_and_sources": null
    },
    "hiden": true
  },
  "set_mixer_standard_stereo!": {
    "hiden": false
  },
  "synth": {
    "introduced": "2,0,0",
    "accepts_block": true,
    "summary": "Trigger specific synth",
    "args": [
      {
        "synth_name": ":symbol"
      }
    ],
    "name": "synth",
    "requires_block": false,
    "async_block": true,
    "signature": {
      "*args": null,
      "synth_name": null,
      "&blk": null
    },
    "hiden": true,
    "intro_fn": true,
    "opts": {
      "attack": 0,
      "sustain": 1,
      "decay": 0,
      "amp_slide": 1,
      "decay_level": 1,
      "sustain_level": 1,
      "amp": 1,
      "on": 1,
      "env_curve": 1,
      "pan": 0,
      "release": 0,
      "pitch": 0,
      "pan_slide": 1,
      "attack_level": 1,
      "slide": 0
    }
  },
  "set_volume": {
    "introduced": "2,0,0",
    "accepts_block": false,
    "summary": "Set Volume globally",
    "args": [
      {
        "vol": ":number"
      }
    ],
    "name": "set_volume!",
    "signature": {
      "vol": null
    },
    "hiden": false,
    "modifies_env": true
  },
  "recording_save": {
    "introduced": "2,0,0",
    "accepts_block": false,
    "summary": "Save recording",
    "args": [
      {
        "path": ":string"
      }
    ],
    "name": "recording_save",
    "signature": {
      "filename": null
    },
    "hiden": true
  },
  "use_debug": {
    "introduced": "2,0,0",
    "accepts_block": false,
    "summary": "Enable and disable debug",
    "args": [
      {
        "true_or_false": ":boolean"
      }
    ],
    "name": "use_debug",
    "signature": {
      "&block": null,
      "v": null
    },
    "hiden": false
  },
  "set_control_delta": {
    "introduced": "2,1,0",
    "accepts_block": false,
    "summary": "Set control delta globally",
    "args": [
      {
        "time": ":number"
      }
    ],
    "name": "set_control_delta!",
    "signature": {
      "t": null
    },
    "hiden": false,
    "modifies_env": true
  },
  "with_sample_defaults": {
    "introduced": "2,5,0",
    "accepts_block": true,
    "summary": "Block-level use new sample defaults",
    "name": "with_sample_defaults",
    "signature": {
      "*args": null,
      "&block": null
    },
    "hiden": false,
    "requires_block": true,
    "opts": {}
  },
  "note_range": {
    "introduced": "2,6,0",
    "returns": ":ring",
    "inline": true,
    "summary": "Get a range of notes",
    "args": [
      {
        "low_note": ":note"
      },
      {
        "high_note": ":note"
      }
    ],
    "name": "note_range",
    "accepts_block": false,
    "signature": {
      "low_note": null,
      "high_note": null,
      "*opts": null
    },
    "hiden": false,
    "opts": {
      "pitches": []
    }
  }
}

sound_args_types_conversion = {}

sound_opts_types_conversion = {}

#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/

synths = {
  "BasicMonoPlayer": {
    "summary": "Basic Mono Sample Player (no env)",
    "name": ":basic_mono_player",
    "inherit_arg": false,
    "opts": {
      "amp_slide_shape": 1,
      "lpf_slide_curve": 0,
      "lpf": -1,
      "hpf_slide": 0,
      "amp_slide": 0,
      "pan_slide_shape": 1,
      "hpf_slide_curve": 0,
      "hpf": -1,
      "lpf_slide": 0,
      "amp": 1,
      "lpf_slide_shape": 1,
      "hpf_slide_shape": 1,
      "pan": 0,
      "pan_slide_curve": 0,
      "pan_slide": 0,
      "amp_slide_curve": 0,
      "rate": 1
    },
    "hiden": true,
    "inherit_base": "StudioInfo"
  },
  "Beep": {
    "summary": "Sine Wave",
    "name": ":beep",
    "inherit_arg": false,
    "opts": {
      "note": 52,
      "amp_slide_shape": 1,
      "sustain": 0,
      "attack_level": 1,
      "note_slide": 0,
      "decay": 0,
      "attack": 0,
      "amp_slide": 0,
      "note_slide_shape": 1,
      "pan_slide_shape": 1,
      "sustain_level": 1,
      "decay_level": 1,
      "amp": 1,
      "env_curve": 2,
      "pan": 0,
      "release": 1,
      "amp_slide_curve": 0,
      "pan_slide": 0,
      "pan_slide_curve": 0,
      "note_slide_curve": 0
    },
    "hiden": false,
    "inherit_base": "SonicPiSynth"
  },
  "SoundIn": {
    "summary": "Sound In",
    "name": ":sound_in",
    "inherit_arg": false,
    "opts": {
      "amp_slide_shape": 1,
      "sustain": 1,
      "attack_level": 1,
      "decay": 0,
      "attack": 0,
      "amp_slide": 0,
      "pan_slide_shape": 1,
      "sustain_level": 1,
      "decay_level": 1,
      "amp": 1,
      "env_curve": 0,
      "input": 1,
      "pan": 0,
      "release": 0,
      "pan_slide_curve": 0,
      "pan_slide": 0,
      "amp_slide_curve": 0
    },
    "hiden": false,
    "inherit_base": "SonicPiSynth"
  },
  "ModDSaw": {
    "summary": "Modulated Detuned Saw Waves",
    "name": ":mod_dsaw",
    "inherit_arg": false,
    "opts": {
      "amp_slide_shape": 1,
      "sustain": 0,
      "note_slide": 0,
      "mod_pulse_width_slide_shape": 1,
      "decay": 0,
      "mod_phase": 0.25,
      "attack_level": 1,
      "pan_slide_shape": 1,
      "detune": 0.1,
      "decay_level": 1,
      "amp": 1,
      "detune_slide_curve": 0,
      "detune_slide_shape": 1,
      "env_curve": 2,
      "mod_wave": 1,
      "amp_slide_curve": 0,
      "pan_slide_curve": 0,
      "mod_phase_slide": 0,
      "note": 52,
      "attack": 0,
      "mod_range_slide": 0,
      "mod_pulse_width_slide_curve": 0,
      "note_slide_curve": 0,
      "mod_range_slide_shape": 1,
      "mod_range": 5,
      "mod_range_slide_curve": 0,
      "mod_phase_offset": 0,
      "mod_pulse_width": 0.5,
      "note_slide_shape": 1,
      "mod_invert_wave": 0,
      "sustain_level": 1,
      "cutoff_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "mod_pulse_width_slide": 0,
      "mod_phase_slide_curve": 0,
      "pan": 0,
      "mod_phase_slide_shape": 1,
      "release": 1,
      "cutoff_slide": 0,
      "pan_slide": 0,
      "amp_slide": 0,
      "cutoff": 100,
      "detune_slide": 0
    },
    "hiden": false,
    "inherit_base": "SonicPiSynth"
  },
  "Supersaw": {
    "summary": "Supersaw",
    "name": ":supersaw",
    "inherit_arg": false,
    "opts": {
      "amp_slide_shape": 1,
      "sustain": 0,
      "note_slide": 0,
      "decay": 0,
      "attack_level": 1,
      "pan_slide_shape": 1,
      "decay_level": 1,
      "amp": 1,
      "env_curve": 2,
      "amp_slide_curve": 0,
      "pan_slide_curve": 0,
      "res": 0.7,
      "note": 52,
      "attack": 0,
      "note_slide_curve": 0,
      "res_slide": 0,
      "note_slide_shape": 1,
      "sustain_level": 1,
      "cutoff_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "res_slide_shape": 1,
      "res_slide_curve": 0,
      "pan": 0,
      "release": 1,
      "cutoff_slide": 0,
      "pan_slide": 0,
      "amp_slide": 0,
      "cutoff": 130
    },
    "hiden": false,
    "inherit_base": "SonicPiSynth"
  },
  "TechSaws": {
    "summary": "TechSaws",
    "name": ":tech_saws",
    "inherit_arg": false,
    "opts": {
      "amp_slide_shape": 1,
      "sustain": 0,
      "note_slide": 0,
      "decay": 0,
      "attack_level": 1,
      "pan_slide_shape": 1,
      "decay_level": 1,
      "amp": 1,
      "env_curve": 2,
      "amp_slide_curve": 0,
      "pan_slide_curve": 0,
      "res": 0.7,
      "note": 52,
      "attack": 0,
      "note_slide_curve": 0,
      "res_slide": 0,
      "note_slide_shape": 1,
      "sustain_level": 1,
      "cutoff_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "res_slide_shape": 1,
      "res_slide_curve": 0,
      "pan": 0,
      "release": 1,
      "cutoff_slide": 0,
      "pan_slide": 0,
      "amp_slide": 0,
      "cutoff": 130
    },
    "hiden": false,
    "inherit_base": "SonicPiSynth"
  },
  "SynthPiano": {
    "summary": "SynthPiano",
    "name": ":piano",
    "inherit_arg": false,
    "opts": {
      "amp_slide_shape": 1,
      "sustain": 0,
      "stereo_width": 0,
      "note_slide": 0,
      "decay": 0,
      "amp_slide": 0,
      "pan_slide_shape": 1,
      "decay_level": 1,
      "amp": 1,
      "amp_slide_curve": 0,
      "pan_slide_curve": 0,
      "note": 52,
      "attack": 0,
      "vel": 0.2,
      "note_slide_curve": 0,
      "note_slide_shape": 1,
      "sustain_level": 1,
      "hard": 0.5,
      "pan": 0,
      "release": 1,
      "pan_slide": 0,
      "attack_level": 1
    },
    "hiden": false,
    "inherit_base": "SonicPiSynth"
  },
  "PrettyBell": {
    "summary": "Pretty Bell",
    "name": ":pretty_bell",
    "inherit_arg": true,
    "opts": {
      "amp_slide_shape": 1,
      "sustain": 0,
      "note_slide": 0,
      "decay": 0,
      "attack_level": 1,
      "pan_slide_shape": 1,
      "decay_level": 1,
      "amp": 1,
      "env_curve": 2,
      "amp_slide_curve": 0,
      "pan_slide_curve": 0,
      "note": 52,
      "attack": 0,
      "note_slide_curve": 0,
      "note_slide_shape": 1,
      "sustain_level": 1,
      "pan": 0,
      "release": 1,
      "pan_slide": 0,
      "amp_slide": 0
    },
    "hiden": true,
    "inherit_base": "DullBell"
  },
  "StudioInfo": {
    "inherit_arg": true,
    "hiden": true,
    "inherit_base": "SonicPiSynth",
    "opts": {}
  },
  "Tri": {
    "summary": "Triangle Wave",
    "name": ":tri",
    "inherit_arg": true,
    "opts": {
      "amp_slide_shape": 1,
      "sustain": 0,
      "note_slide": 0,
      "decay": 0,
      "attack_level": 1,
      "pan_slide_shape": 1,
      "decay_level": 1,
      "amp": 1,
      "pulse_width_slide_shape": 1,
      "env_curve": 2,
      "amp_slide_curve": 0,
      "pan_slide_curve": 0,
      "pulse_width_slide": 0,
      "note": 52,
      "attack": 0,
      "note_slide_curve": 0,
      "note_slide_shape": 1,
      "sustain_level": 1,
      "cutoff_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "pulse_width": 0.5,
      "pan": 0,
      "release": 1,
      "cutoff_slide": 0,
      "pan_slide": 0,
      "amp_slide": 0,
      "cutoff": 100
    },
    "hiden": true,
    "inherit_base": "Pulse"
  },
  "DSaw": {
    "summary": "Detuned Saw wave",
    "name": ":dsaw",
    "inherit_arg": false,
    "opts": {
      "amp_slide_shape": 1,
      "sustain": 0,
      "note_slide": 0,
      "decay": 0,
      "attack_level": 1,
      "pan_slide_shape": 1,
      "detune": 0.1,
      "decay_level": 1,
      "amp": 1,
      "env_curve": 2,
      "amp_slide_curve": 0,
      "pan_slide_curve": 0,
      "note": 52,
      "attack": 0,
      "detune_slide_curve": 0,
      "note_slide_curve": 0,
      "detune_slide": 0,
      "note_slide_shape": 1,
      "sustain_level": 1,
      "cutoff_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "pan": 0,
      "release": 1,
      "cutoff_slide": 0,
      "pan_slide": 0,
      "amp_slide": 0,
      "cutoff": 100,
      "detune_slide_shape": 1
    },
    "hiden": false,
    "inherit_base": "SonicPiSynth"
  },
  "DullBell": {
    "summary": "Dull Bell",
    "name": ":dull_bell",
    "inherit_arg": false,
    "opts": {
      "note": 52,
      "amp_slide_shape": 1,
      "sustain": 0,
      "attack_level": 1,
      "note_slide": 0,
      "decay": 0,
      "attack": 0,
      "amp_slide": 0,
      "note_slide_shape": 1,
      "pan_slide_shape": 1,
      "sustain_level": 1,
      "decay_level": 1,
      "amp": 1,
      "env_curve": 2,
      "pan": 0,
      "release": 1,
      "amp_slide_curve": 0,
      "pan_slide": 0,
      "pan_slide_curve": 0,
      "note_slide_curve": 0
    },
    "hiden": false,
    "inherit_base": "SonicPiSynth"
  },
  "GNoise": {
    "summary": "Grey Noise",
    "name": ":gnoise",
    "inherit_arg": true,
    "opts": {
      "amp_slide_shape": 1,
      "sustain": 0,
      "res": 0,
      "decay": 0,
      "attack_level": 1,
      "pan_slide_shape": 1,
      "decay_level": 1,
      "amp": 1,
      "env_curve": 2,
      "amp_slide_curve": 0,
      "pan_slide_curve": 0,
      "res_slide": 0,
      "attack": 0,
      "pan_slide": 0,
      "sustain_level": 1,
      "cutoff_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "cutoff": 110,
      "pan": 0,
      "release": 1,
      "cutoff_slide": 0,
      "res_slide_shape": 1,
      "amp_slide": 0,
      "res_slide_curve": 0
    },
    "hiden": true,
    "inherit_base": "Noise"
  },
  "Zawa": {
    "summary": "Zawa",
    "name": ":zawa",
    "inherit_arg": false,
    "opts": {
      "range": 24,
      "amp_slide_shape": 1,
      "sustain": 0,
      "note_slide": 0,
      "phase": 1,
      "decay": 0,
      "pulse_width_slide_shape": 1,
      "attack_level": 1,
      "range_slide_shape": 1,
      "pan_slide_shape": 1,
      "decay_level": 1,
      "amp": 1,
      "phase_slide": 0,
      "disable_wave": 0,
      "pulse_width_slide": 0,
      "amp_slide_curve": 0,
      "phase_slide_curve": 0,
      "pan_slide_curve": 0,
      "res": 0.9,
      "note": 52,
      "attack": 0,
      "note_slide_curve": 0,
      "wave": 3,
      "res_slide": 0,
      "pulse_width_slide_curve": 0,
      "note_slide_shape": 1,
      "sustain_level": 1,
      "cutoff_slide_curve": 0,
      "invert_wave": 0,
      "cutoff_slide_shape": 1,
      "range_slide": 0,
      "res_slide_shape": 1,
      "range_slide_curve": 0,
      "res_slide_curve": 0,
      "pan": 0,
      "phase_offset": 0,
      "release": 1,
      "pulse_width": 0.5,
      "cutoff_slide": 0,
      "pan_slide": 0,
      "amp_slide": 0,
      "cutoff": 100,
      "phase_slide_shape": 1
    },
    "hiden": false,
    "inherit_base": "SonicPiSynth"
  },
  "DTri": {
    "summary": "Detuned Triangle Wave",
    "name": ":dtri",
    "inherit_arg": true,
    "opts": {
      "amp_slide_shape": 1,
      "sustain": 0,
      "note_slide": 0,
      "decay": 0,
      "attack_level": 1,
      "pan_slide_shape": 1,
      "detune": 0.1,
      "decay_level": 1,
      "amp": 1,
      "env_curve": 2,
      "amp_slide_curve": 0,
      "pan_slide_curve": 0,
      "note": 52,
      "attack": 0,
      "cutoff_slide": 0,
      "note_slide_curve": 0,
      "detune_slide": 0,
      "note_slide_shape": 1,
      "sustain_level": 1,
      "cutoff_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "pan": 0,
      "release": 1,
      "detune_slide_curve": 0,
      "pan_slide": 0,
      "amp_slide": 0,
      "cutoff": 100,
      "detune_slide_shape": 1
    },
    "hiden": true,
    "inherit_base": "DSaw"
  },
  "SonicPiSynth": {
    "inherit_arg": true,
    "hiden": true,
    "inherit_base": "SynthInfo",
    "opts": {}
  },
  "ChipBass": {
    "summary": "Chip Bass",
    "name": ":chipbass",
    "inherit_arg": false,
    "opts": {
      "note": 60,
      "amp_slide_shape": 1,
      "sustain": 0,
      "attack_level": 1,
      "note_slide": 0,
      "decay": 0,
      "note_resolution": 0.1,
      "amp_slide": 0,
      "note_slide_shape": 1,
      "pan_slide_shape": 1,
      "sustain_level": 1,
      "decay_level": 1,
      "amp": 1,
      "env_curve": 2,
      "pan": 0,
      "attack": 0,
      "release": 1,
      "amp_slide_curve": 0,
      "pan_slide": 0,
      "pan_slide_curve": 0,
      "note_slide_curve": 0
    },
    "hiden": false,
    "inherit_base": "SonicPiSynth"
  },
  "SoundInStereo": {
    "summary": "Sound In Stereo",
    "name": ":sound_in_stereo",
    "inherit_arg": true,
    "opts": {
      "amp_slide_shape": 1,
      "sustain": 1,
      "decay": 0,
      "attack_level": 1,
      "pan_slide_shape": 1,
      "input": 1,
      "decay_level": 1,
      "amp": 1,
      "env_curve": 0,
      "pan_slide_curve": 0,
      "amp_slide_curve": 0,
      "attack": 0,
      "sustain_level": 1,
      "pan": 0,
      "release": 0,
      "pan_slide": 0,
      "amp_slide": 0
    },
    "hiden": true,
    "inherit_base": "SoundIn"
  },
  "ModTri": {
    "summary": "Modulated Triangle Wave",
    "name": ":mod_tri",
    "inherit_arg": false,
    "opts": {
      "amp_slide_shape": 1,
      "sustain": 0,
      "note_slide": 0,
      "mod_pulse_width_slide_shape": 1,
      "decay": 0,
      "mod_phase": 0.25,
      "attack_level": 1,
      "pan_slide_shape": 1,
      "decay_level": 1,
      "amp": 1,
      "env_curve": 2,
      "mod_wave": 1,
      "amp_slide_curve": 0,
      "pan_slide_curve": 0,
      "mod_phase_slide": 0,
      "note": 52,
      "attack": 0,
      "mod_range_slide": 0,
      "mod_pulse_width_slide_curve": 0,
      "note_slide_curve": 0,
      "mod_range_slide_shape": 1,
      "mod_range": 5,
      "mod_range_slide_curve": 0,
      "mod_phase_offset": 0,
      "mod_pulse_width": 0.5,
      "note_slide_shape": 1,
      "mod_invert_wave": 0,
      "sustain_level": 1,
      "cutoff_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "mod_pulse_width_slide": 0,
      "mod_phase_slide_curve": 0,
      "pan": 0,
      "mod_phase_slide_shape": 1,
      "release": 1,
      "cutoff_slide": 0,
      "pan_slide": 0,
      "amp_slide": 0,
      "cutoff": 100
    },
    "hiden": false,
    "inherit_base": "SonicPiSynth"
  },
  "FM": {
    "summary": "Basic FM synthesis",
    "name": ":fm",
    "inherit_arg": false,
    "opts": {
      "amp_slide_shape": 1,
      "sustain": 0,
      "note_slide": 0,
      "decay": 0,
      "depth_slide": 0,
      "attack_level": 1,
      "pan_slide_shape": 1,
      "decay_level": 1,
      "amp": 1,
      "divisor_slide_curve": 0,
      "env_curve": 2,
      "depth_slide_shape": 1,
      "amp_slide_curve": 0,
      "pan_slide_curve": 0,
      "depth": 1,
      "divisor_slide": 0,
      "note": 52,
      "attack": 0,
      "note_slide_curve": 0,
      "note_slide_shape": 1,
      "sustain_level": 1,
      "cutoff_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "pan": 0,
      "release": 1,
      "divisor": 2,
      "divisor_slide_shape": 1,
      "cutoff_slide": 0,
      "pan_slide": 0,
      "amp_slide": 0,
      "cutoff": 100,
      "depth_slide_curve": 0
    },
    "hiden": false,
    "inherit_base": "SonicPiSynth"
  },
  "SynthPluck": {
    "summary": "SynthPluck",
    "name": ":pluck",
    "inherit_arg": false,
    "opts": {
      "amp_slide_shape": 1,
      "sustain": 0,
      "note_slide": 0,
      "decay": 0,
      "attack_level": 1,
      "pan_slide_shape": 1,
      "decay_level": 1,
      "amp": 1,
      "max_delay_time": 0.125,
      "amp_slide_curve": 0,
      "pluck_decay": 30,
      "pan_slide_curve": 0,
      "note": 52,
      "attack": 0,
      "note_slide_curve": 0,
      "note_slide_shape": 1,
      "sustain_level": 1,
      "noise_amp": 0.8,
      "pan": 0,
      "release": 1,
      "coef": 0.3,
      "pan_slide": 0,
      "amp_slide": 0
    },
    "hiden": false,
    "inherit_base": "SonicPiSynth"
  },
  "Noise": {
    "summary": "Noise",
    "name": ":noise",
    "inherit_arg": false,
    "opts": {
      "amp_slide_shape": 1,
      "sustain": 0,
      "res": 0,
      "decay": 0,
      "attack_level": 1,
      "pan_slide_shape": 1,
      "decay_level": 1,
      "amp": 1,
      "env_curve": 2,
      "amp_slide_curve": 0,
      "pan_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "res_slide": 0,
      "attack": 0,
      "res_slide_shape": 1,
      "sustain_level": 1,
      "cutoff_slide_shape": 1,
      "res_slide_curve": 0,
      "pan": 0,
      "release": 1,
      "cutoff_slide": 0,
      "pan_slide": 0,
      "amp_slide": 0,
      "cutoff": 110
    },
    "hiden": false,
    "inherit_base": "Pitchless"
  },
  "ChipNoise": {
    "summary": "Chip Noise",
    "name": ":chipnoise",
    "inherit_arg": false,
    "opts": {
      "freq_band_slide_shape": 1,
      "amp_slide_shape": 0,
      "sustain": 1,
      "attack_level": 1,
      "decay": 0,
      "attack": 0,
      "amp_slide": 0,
      "freq_band": 0,
      "pan_slide_shape": 1,
      "sustain_level": 1,
      "decay_level": 1,
      "amp": 1,
      "env_curve": 0,
      "pan": 0,
      "release": 0,
      "pan_slide_curve": 0,
      "freq_band_slide_curve": 0,
      "pan_slide": 0,
      "amp_slide_curve": 1,
      "freq_band_slide": 0
    },
    "hiden": true,
    "inherit_base": "Noise"
  },
  "ChipLead": {
    "summary": "Chip Lead",
    "name": ":chiplead",
    "inherit_arg": false,
    "opts": {
      "amp_slide_shape": 1,
      "sustain": 0,
      "note_slide": 0,
      "decay": 0,
      "note_slide_shape": 1,
      "attack_level": 1,
      "pan_slide_shape": 1,
      "decay_level": 1,
      "width": 0,
      "amp": 1,
      "env_curve": 2,
      "amp_slide_curve": 0,
      "pan_slide_curve": 0,
      "note": 60,
      "attack": 0,
      "note_slide_curve": 0,
      "note_resolution": 0.1,
      "sustain_level": 1,
      "pan": 0,
      "release": 1,
      "pan_slide": 0,
      "amp_slide": 0
    },
    "hiden": false,
    "inherit_base": "SonicPiSynth"
  },
  "MainMixer": {
    "summary": "Main Mixer",
    "name": ":mixer",
    "inherit_arg": false,
    "opts": {
      "pre_amp": 1,
      "amp_slide_shape": 1,
      "lpf_slide_curve": 0,
      "lpf": 135.5,
      "hpf_slide": 0.02,
      "invert_stereo": 0,
      "amp_slide": 0.02,
      "hpf_bypass": 0,
      "hpf": 0,
      "lpf_slide": 0.02,
      "amp": 1,
      "force_mono": 0,
      "lpf_slide_shape": 1,
      "hpf_slide_curve": 0,
      "limiter_bypass": 0,
      "pre_amp_slide_curve": 0,
      "amp_slide_curve": 0,
      "lpf_bypass": 0,
      "pre_amp_slide_shape": 1,
      "hpf_slide_shape": 1,
      "pre_amp_slide": 0.02
    },
    "hiden": true,
    "inherit_base": "BaseMixer"
  },
  "DarkSeaHorn": {
    "summary": "Dark Sea Horn",
    "name": ":dark_sea_horn",
    "inherit_arg": false,
    "opts": {
      "note": 52,
      "amp_slide_shape": 1,
      "sustain": 0,
      "attack_level": 1,
      "note_slide": 0,
      "decay": 0,
      "attack": 1,
      "amp_slide": 0,
      "note_slide_shape": 1,
      "pan_slide_shape": 1,
      "sustain_level": 1,
      "decay_level": 1,
      "amp": 1,
      "env_curve": 2,
      "pan": 0,
      "release": 4.0,
      "amp_slide_curve": 0,
      "pan_slide": 0,
      "pan_slide_curve": 0,
      "note_slide_curve": 0
    },
    "hiden": true,
    "inherit_base": "SonicPiSynth"
  },
  "PNoise": {
    "summary": "Pink Noise",
    "name": ":pnoise",
    "inherit_arg": true,
    "opts": {
      "amp_slide_shape": 1,
      "sustain": 0,
      "res": 0,
      "decay": 0,
      "attack_level": 1,
      "pan_slide_shape": 1,
      "decay_level": 1,
      "amp": 1,
      "env_curve": 2,
      "amp_slide_curve": 0,
      "pan_slide_curve": 0,
      "res_slide": 0,
      "attack": 0,
      "pan_slide": 0,
      "sustain_level": 1,
      "cutoff_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "cutoff": 110,
      "pan": 0,
      "release": 1,
      "cutoff_slide": 0,
      "res_slide_shape": 1,
      "amp_slide": 0,
      "res_slide_curve": 0
    },
    "hiden": true,
    "inherit_base": "Noise"
  },
  "ModSine": {
    "summary": "Modulated Sine Wave",
    "name": ":mod_sine",
    "inherit_arg": false,
    "opts": {
      "amp_slide_shape": 1,
      "sustain": 0,
      "note_slide": 0,
      "mod_pulse_width_slide_shape": 1,
      "decay": 0,
      "mod_phase": 0.25,
      "attack_level": 1,
      "pan_slide_shape": 1,
      "decay_level": 1,
      "amp": 1,
      "env_curve": 2,
      "mod_wave": 1,
      "amp_slide_curve": 0,
      "pan_slide_curve": 0,
      "mod_phase_slide": 0,
      "note": 52,
      "attack": 0,
      "mod_range_slide": 0,
      "mod_pulse_width_slide_curve": 0,
      "note_slide_curve": 0,
      "mod_range_slide_shape": 1,
      "mod_range": 5,
      "mod_range_slide_curve": 0,
      "mod_phase_offset": 0,
      "mod_pulse_width": 0.5,
      "note_slide_shape": 1,
      "mod_invert_wave": 0,
      "sustain_level": 1,
      "cutoff_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "mod_pulse_width_slide": 0,
      "mod_phase_slide_curve": 0,
      "pan": 0,
      "mod_phase_slide_shape": 1,
      "release": 1,
      "cutoff_slide": 0,
      "pan_slide": 0,
      "amp_slide": 0,
      "cutoff": 100
    },
    "hiden": false,
    "inherit_base": "SonicPiSynth"
  },
  "Hoover": {
    "summary": "Hoover",
    "name": ":hoover",
    "inherit_arg": false,
    "opts": {
      "amp_slide_shape": 1,
      "sustain": 0,
      "note_slide": 0,
      "decay": 0,
      "attack_level": 1,
      "pan_slide_shape": 1,
      "decay_level": 1,
      "amp": 1,
      "env_curve": 2,
      "amp_slide_curve": 0,
      "pan_slide_curve": 0,
      "res": 0.1,
      "note": 52,
      "attack": 0.05,
      "note_slide_curve": 0,
      "res_slide": 0,
      "note_slide_shape": 1,
      "sustain_level": 1,
      "cutoff_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "res_slide_shape": 1,
      "res_slide_curve": 0,
      "pan": 0,
      "release": 1,
      "cutoff_slide": 0,
      "pan_slide": 0,
      "amp_slide": 0,
      "cutoff": 130
    },
    "hiden": false,
    "inherit_base": "SonicPiSynth"
  },
  "BaseMixer": {
    "inherit_arg": true,
    "hiden": true,
    "inherit_base": "StudioInfo",
    "opts": {}
  },
  "ModSaw": {
    "summary": "Modulated Saw Wave",
    "name": ":mod_saw",
    "inherit_arg": false,
    "opts": {
      "amp_slide_shape": 1,
      "sustain": 0,
      "note_slide": 0,
      "mod_pulse_width_slide_shape": 1,
      "decay": 0,
      "mod_phase": 0.25,
      "attack_level": 1,
      "pan_slide_shape": 1,
      "decay_level": 1,
      "amp": 1,
      "env_curve": 2,
      "mod_wave": 1,
      "amp_slide_curve": 0,
      "pan_slide_curve": 0,
      "mod_phase_slide": 0,
      "note": 52,
      "attack": 0,
      "mod_range_slide": 0,
      "mod_pulse_width_slide_curve": 0,
      "note_slide_curve": 0,
      "mod_range_slide_shape": 1,
      "mod_range": 5,
      "mod_range_slide_curve": 0,
      "mod_phase_offset": 0,
      "mod_pulse_width": 0.5,
      "note_slide_shape": 1,
      "mod_invert_wave": 0,
      "sustain_level": 1,
      "cutoff_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "mod_pulse_width_slide": 0,
      "mod_phase_slide_curve": 0,
      "pan": 0,
      "mod_phase_slide_shape": 1,
      "release": 1,
      "cutoff_slide": 0,
      "pan_slide": 0,
      "amp_slide": 0,
      "cutoff": 100
    },
    "hiden": false,
    "inherit_base": "SonicPiSynth"
  },
  "BasicStereoPlayer": {
    "summary": "Basic Stereo Sample Player (no env)",
    "name": ":basic_stereo_player",
    "inherit_arg": true,
    "opts": {
      "amp_slide_shape": 1,
      "lpf_slide_curve": 0,
      "lpf": -1,
      "amp_slide": 0,
      "pan_slide_shape": 1,
      "hpf": -1,
      "lpf_slide": 0,
      "amp": 1,
      "lpf_slide_shape": 1,
      "pan_slide_curve": 0,
      "amp_slide_curve": 0,
      "rate": 1,
      "hpf_slide": 0,
      "hpf_slide_curve": 0,
      "pan": 0,
      "pan_slide": 0,
      "hpf_slide_shape": 1
    },
    "hiden": true,
    "inherit_base": "BasicMonoPlayer"
  },
  "Pulse": {
    "summary": "Pulse Wave",
    "name": ":pulse",
    "inherit_arg": true,
    "opts": {
      "amp_slide_shape": 1,
      "sustain": 0,
      "note_slide": 0,
      "decay": 0,
      "attack_level": 1,
      "pan_slide_shape": 1,
      "decay_level": 1,
      "amp": 1,
      "pulse_width_slide_shape": 1,
      "env_curve": 2,
      "amp_slide_curve": 0,
      "pan_slide_curve": 0,
      "pulse_width_slide": 0,
      "note": 52,
      "attack": 0,
      "note_slide_curve": 0,
      "note_slide_shape": 1,
      "sustain_level": 1,
      "cutoff_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "pulse_width": 0.5,
      "pan": 0,
      "release": 1,
      "cutoff_slide": 0,
      "pan_slide": 0,
      "amp_slide": 0,
      "cutoff": 100
    },
    "hiden": true,
    "inherit_base": "Square"
  },
  "BNoise": {
    "summary": "Brown Noise",
    "name": ":bnoise",
    "inherit_arg": true,
    "opts": {
      "amp_slide_shape": 1,
      "sustain": 0,
      "res": 0,
      "decay": 0,
      "attack_level": 1,
      "pan_slide_shape": 1,
      "decay_level": 1,
      "amp": 1,
      "env_curve": 2,
      "amp_slide_curve": 0,
      "pan_slide_curve": 0,
      "res_slide": 0,
      "attack": 0,
      "pan_slide": 0,
      "sustain_level": 1,
      "cutoff_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "cutoff": 110,
      "pan": 0,
      "release": 1,
      "cutoff_slide": 0,
      "res_slide_shape": 1,
      "amp_slide": 0,
      "res_slide_curve": 0
    },
    "hiden": true,
    "inherit_base": "Noise"
  },
  "Hollow": {
    "summary": "Hollow",
    "name": ":hollow",
    "inherit_arg": false,
    "opts": {
      "amp_slide_shape": 1,
      "sustain": 0,
      "note_slide": 0,
      "decay": 0,
      "attack_level": 1,
      "pan_slide_shape": 1,
      "decay_level": 1,
      "norm": 0,
      "amp": 1,
      "noise": 1,
      "env_curve": 2,
      "amp_slide_curve": 0,
      "pan_slide_curve": 0,
      "res": 0.99,
      "note": 52,
      "attack": 0,
      "note_slide_curve": 0,
      "res_slide": 0,
      "note_slide_shape": 1,
      "sustain_level": 1,
      "cutoff_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "res_slide_shape": 1,
      "res_slide_curve": 0,
      "pan": 0,
      "release": 1,
      "cutoff_slide": 0,
      "pan_slide": 0,
      "amp_slide": 0,
      "cutoff": 90
    },
    "hiden": false,
    "inherit_base": "SonicPiSynth"
  },
  "SubPulse": {
    "summary": "Pulse Wave with sub",
    "name": ":subpulse",
    "inherit_arg": true,
    "opts": {
      "amp_slide_shape": 1,
      "sustain": 0,
      "note_slide": 0,
      "decay": 0,
      "attack_level": 1,
      "pan_slide_shape": 1,
      "decay_level": 1,
      "amp": 1,
      "pulse_width_slide_shape": 1,
      "env_curve": 2,
      "sub_detune_slide": 0,
      "amp_slide_curve": 0,
      "pan_slide_curve": 0,
      "sub_amp_slide_shape": 1,
      "pulse_width_slide": 0,
      "note": 52,
      "attack": 0,
      "note_slide_curve": 0,
      "sub_amp_slide_curve": 0,
      "sub_detune": -12,
      "note_slide_shape": 1,
      "sustain_level": 1,
      "cutoff_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "pulse_width": 0.5,
      "pan": 0,
      "sub_detune_slide_shape": 1,
      "release": 1,
      "sub_amp": 1,
      "sub_amp_slide": 0,
      "cutoff_slide": 0,
      "pan_slide": 0,
      "amp_slide": 0,
      "cutoff": 100
    },
    "hiden": true,
    "inherit_base": "Pulse"
  },
  "ModPulse": {
    "summary": "Modulated Pulse",
    "name": ":mod_pulse",
    "inherit_arg": false,
    "opts": {
      "amp_slide_shape": 1,
      "sustain": 0,
      "note_slide": 0,
      "mod_pulse_width_slide_shape": 1,
      "decay": 0,
      "mod_phase": 0.25,
      "attack_level": 1,
      "pan_slide_shape": 1,
      "decay_level": 1,
      "amp": 1,
      "pulse_width_slide_shape": 1,
      "env_curve": 2,
      "mod_wave": 1,
      "amp_slide_curve": 0,
      "pan_slide_curve": 0,
      "mod_phase_slide": 0,
      "pulse_width_slide": 0,
      "note": 52,
      "attack": 0,
      "mod_range_slide": 0,
      "mod_pulse_width_slide_curve": 0,
      "note_slide_curve": 0,
      "mod_range_slide_shape": 1,
      "mod_range": 5,
      "mod_range_slide_curve": 0,
      "mod_phase_offset": 0,
      "mod_pulse_width": 0.5,
      "note_slide_shape": 1,
      "mod_invert_wave": 0,
      "sustain_level": 1,
      "cutoff_slide_curve": 0,
      "pulse_width_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "mod_pulse_width_slide": 0,
      "pulse_width": 0.5,
      "mod_phase_slide_curve": 0,
      "pan": 0,
      "mod_phase_slide_shape": 1,
      "release": 1,
      "cutoff_slide": 0,
      "pan_slide": 0,
      "amp_slide": 0,
      "cutoff": 100
    },
    "hiden": false,
    "inherit_base": "SonicPiSynth"
  },
  "DarkAmbience": {
    "summary": "Dark Ambience",
    "name": ":dark_ambience",
    "inherit_arg": false,
    "opts": {
      "amp_slide_shape": 1,
      "sustain": 0,
      "detune1_slide_curve": 0,
      "note_slide": 0,
      "decay": 0,
      "detune2": 24,
      "attack_level": 1,
      "detune2_slide_curve": 0,
      "pan_slide_shape": 1,
      "decay_level": 1,
      "detune2_slide": 0,
      "amp": 1,
      "noise": 0,
      "env_curve": 2,
      "amp_slide_curve": 0,
      "detune1_slide_shape": 1,
      "pan_slide_curve": 0,
      "res": 0.7,
      "room": 70,
      "note": 52,
      "attack": 0,
      "detune1": 12,
      "note_slide_curve": 0,
      "ring": 0.2,
      "res_slide": 0,
      "reverb_time": 100,
      "note_slide_shape": 1,
      "sustain_level": 1,
      "cutoff_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "res_slide_shape": 1,
      "res_slide_curve": 0,
      "pan": 0,
      "release": 1,
      "detune1_slide": 0,
      "cutoff_slide": 0,
      "pan_slide": 0,
      "amp_slide": 0,
      "cutoff": 110,
      "detune2_slide_shape": 1
    },
    "hiden": false,
    "inherit_base": "SonicPiSynth"
  },
  "Prophet": {
    "summary": "The Prophet",
    "name": ":prophet",
    "inherit_arg": false,
    "opts": {
      "amp_slide_shape": 1,
      "sustain": 0,
      "note_slide": 0,
      "decay": 0,
      "attack_level": 1,
      "pan_slide_shape": 1,
      "decay_level": 1,
      "amp": 1,
      "env_curve": 2,
      "amp_slide_curve": 0,
      "pan_slide_curve": 0,
      "res": 0.7,
      "note": 52,
      "attack": 0,
      "note_slide_curve": 0,
      "res_slide": 0,
      "note_slide_shape": 1,
      "sustain_level": 1,
      "cutoff_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "res_slide_shape": 1,
      "res_slide_curve": 0,
      "pan": 0,
      "release": 1,
      "cutoff_slide": 0,
      "pan_slide": 0,
      "amp_slide": 0,
      "cutoff": 110
    },
    "hiden": false,
    "inherit_base": "SonicPiSynth"
  },
  "SynthInfo": {
    "inherit_arg": true,
    "hiden": true,
    "inherit_base": "BaseInfo",
    "opts": {}
  },
  "ModFM": {
    "summary": "Basic FM synthesis with frequency modulation.",
    "name": ":mod_fm",
    "inherit_arg": true,
    "opts": {
      "pan_slide_shape": 1,
      "sustain": 0,
      "depth_slide": 0,
      "decay_level": 1,
      "amp": 1,
      "env_curve": 2,
      "amp_slide_curve": 0,
      "pan_slide_curve": 0,
      "depth": 1,
      "divisor_slide_curve": 0,
      "note_slide_curve": 0,
      "mod_range": 5,
      "mod_pulse_width": 0.5,
      "mod_phase": 0.25,
      "sustain_level": 1,
      "cutoff_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "divisor": 2,
      "divisor_slide_shape": 1,
      "cutoff_slide": 0,
      "pan_slide": 0,
      "amp_slide": 0,
      "cutoff": 100,
      "amp_slide_shape": 1,
      "note_slide": 0,
      "decay": 0,
      "attack_level": 1,
      "depth_slide_shape": 1,
      "mod_wave": 1,
      "divisor_slide": 0,
      "note": 52,
      "attack": 0,
      "note_slide_shape": 1,
      "mod_invert_wave": 0,
      "pan": 0,
      "release": 1,
      "depth_slide_curve": 0,
      "mod_phase_offset": 0
    },
    "hiden": true,
    "inherit_base": "FM"
  },
  "CNoise": {
    "summary": "Clip Noise",
    "name": ":cnoise",
    "inherit_arg": true,
    "opts": {
      "amp_slide_shape": 1,
      "sustain": 0,
      "res": 0,
      "decay": 0,
      "attack_level": 1,
      "pan_slide_shape": 1,
      "decay_level": 1,
      "amp": 1,
      "env_curve": 2,
      "amp_slide_curve": 0,
      "pan_slide_curve": 0,
      "res_slide": 0,
      "attack": 0,
      "pan_slide": 0,
      "sustain_level": 1,
      "cutoff_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "cutoff": 110,
      "pan": 0,
      "release": 1,
      "cutoff_slide": 0,
      "res_slide_shape": 1,
      "amp_slide": 0,
      "res_slide_curve": 0
    },
    "hiden": true,
    "inherit_base": "Noise"
  },
  "StereoPlayer": {
    "summary": "Stereo Sample Player",
    "name": ":stereo_player",
    "inherit_arg": true,
    "opts": {
      "lpf_sustain_level": -1,
      "lpf_release": 0,
      "relax_time": 0.01,
      "finish": 1,
      "decay_level": 1,
      "env_curve": 2,
      "lpf_sustain": -1,
      "pitch_slide_curve": 0,
      "amp_slide_curve": 0,
      "pitch_slide_shape": 1,
      "window_size": 0.2,
      "window_size_slide": 0,
      "pitch_dis_slide": 0,
      "hpf_sustain_level": -1,
      "sustain_level": 1,
      "threshold_slide": 0,
      "threshold_slide_shape": 1,
      "rate": 1,
      "pre_amp_slide_shape": 1,
      "pitch_dis_slide_curve": 0,
      "hpf_max_slide": 0,
      "hpf_max": -1,
      "hpf_sustain": -1,
      "pitch_dis_slide_shape": 1,
      "lpf_slide_curve": 0,
      "decay": 0,
      "hpf_decay_level": -1,
      "attack_level": 1,
      "lpf_slide": 0,
      "lpf_min_slide": 0,
      "lpf_slide_shape": 1,
      "hpf_slide": 0,
      "hpf_max_slide_curve": 0,
      "pitch": 0,
      "pre_amp": 1,
      "clamp_time": 0.01,
      "hpf_decay": 0,
      "relax_time_slide_curve": 0,
      "pitch_slide": 0,
      "hpf_release_level": -1,
      "slope_above_slide_shape": 1,
      "hpf_slide_curve": 0,
      "pre_amp_slide_curve": 0,
      "lpf_min_slide_curve": 0,
      "release": 0,
      "time_dis_slide": 0,
      "hpf_attack_level": -1,
      "lpf_min": -1,
      "hpf_release": 0,
      "pan_slide_shape": 1,
      "sustain": -1,
      "slope_below_slide_curve": 0,
      "lpf_attack_level": -1,
      "hpf": -1,
      "amp": 1,
      "threshold": 0.2,
      "clamp_time_slide": 0,
      "hpf_attack": 0,
      "pan_slide_curve": 0,
      "lpf_attack": 0,
      "time_dis_slide_curve": 0,
      "lpf_release_level": -1,
      "slope_below_slide": 0,
      "lpf_env_curve": 2,
      "slope_above_slide": 0,
      "lpf_min_slide_shape": 1,
      "lpf_decay": 0,
      "clamp_time_slide_curve": 0,
      "pan_slide": 0,
      "norm": 0,
      "hpf_env_curve": 2,
      "amp_slide_shape": 1,
      "lpf": -1,
      "hpf_max_slide_shape": 1,
      "amp_slide": 0,
      "lpf_decay_level": -1,
      "time_dis": 0.0,
      "hpf_init_level": -1,
      "relax_time_slide_shape": 1,
      "threshold_slide_curve": 0,
      "window_size_slide_curve": 0,
      "slope_above_slide_curve": 0,
      "slope_below": 1,
      "pre_amp_slide": 0,
      "attack": 0,
      "compress": 0,
      "pitch_dis": 0.0,
      "slope_above": 0.5,
      "time_dis_slide_shape": 1,
      "clamp_time_slide_shape": 1,
      "slope_below_slide_shape": 1,
      "window_size_slide_shape": 1,
      "pan": 0,
      "start": 0,
      "relax_time_slide": 0,
      "lpf_init_level": -1,
      "hpf_slide_shape": 1
    },
    "hiden": true,
    "inherit_base": "MonoPlayer"
  },
  "BasicMixer": {
    "summary": "Basic Mixer",
    "name": ":basic_mixer",
    "inherit_arg": false,
    "opts": {
      "amp": 1,
      "amp_slide": 0.1,
      "amp_slide_curve": 0,
      "amp_slide_shape": 1
    },
    "hiden": true,
    "inherit_base": "BaseMixer"
  },
  "DPulse": {
    "summary": "Detuned Pulse Wave",
    "name": ":dpulse",
    "inherit_arg": true,
    "opts": {
      "amp_slide_shape": 1,
      "sustain": 0,
      "note_slide": 0,
      "decay": 0,
      "attack_level": 1,
      "pan_slide_shape": 1,
      "detune": 0.1,
      "decay_level": 1,
      "amp": 1,
      "dpulse_width": 0.5,
      "env_curve": 2,
      "dpulse_width_slide_shape": 1,
      "amp_slide_curve": 0,
      "pan_slide_curve": 0,
      "pulse_width_slide": 0,
      "note": 52,
      "attack": 0,
      "cutoff_slide": 0,
      "dpulse_width_slide": 0,
      "note_slide_curve": 0,
      "detune_slide": 0,
      "note_slide_shape": 1,
      "sustain_level": 1,
      "cutoff_slide_curve": 0,
      "pulse_width_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "pulse_width_slide_shape": 1,
      "pulse_width": 0.5,
      "pan": 0,
      "release": 1,
      "detune_slide_curve": 0,
      "pan_slide": 0,
      "amp_slide": 0,
      "cutoff": 100,
      "detune_slide_shape": 1
    },
    "hiden": true,
    "inherit_base": "DSaw"
  },
  "TB303": {
    "summary": "TB-303 Emulation",
    "name": ":tb303",
    "inherit_arg": false,
    "opts": {
      "pan_slide_shape": 1,
      "sustain": 0,
      "decay_level": 1,
      "amp": 1,
      "cutoff_min": 30,
      "env_curve": 2,
      "amp_slide_curve": 0,
      "cutoff_sustain": 0,
      "pan_slide_curve": 0,
      "res": 0.9,
      "res_slide": 0,
      "note_slide_curve": 0,
      "wave": 0,
      "cutoff_sustain_level": 1,
      "sustain_level": 1,
      "cutoff_slide_curve": 0,
      "pulse_width_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "cutoff_min_slide_curve": 0,
      "cutoff_release": 1,
      "cutoff_slide": 0,
      "res_slide_shape": 1,
      "amp_slide": 0,
      "res_slide_curve": 0,
      "amp_slide_shape": 1,
      "cutoff_decay": 0,
      "note_slide": 0,
      "decay": 0,
      "attack_level": 1,
      "cutoff_attack_level": 1,
      "pulse_width_slide_shape": 1,
      "cutoff_attack": 0,
      "cutoff_min_slide_shape": 1,
      "pulse_width_slide": 0,
      "note": 52,
      "attack": 0,
      "cutoff_decay_level": 1,
      "pan_slide": 0,
      "note_slide_shape": 1,
      "pulse_width": 0.5,
      "cutoff_min_slide": 0,
      "pan": 0,
      "release": 1,
      "cutoff": 120
    },
    "hiden": false,
    "inherit_base": "SonicPiSynth"
  },
  "MonoPlayer": {
    "summary": "Mono Sample Player",
    "name": ":mono_player",
    "inherit_arg": false,
    "opts": {
      "lpf_sustain_level": -1,
      "lpf_release": 0,
      "relax_time": 0.01,
      "finish": 1,
      "decay_level": 1,
      "env_curve": 2,
      "sustain_level": 1,
      "pitch_slide_curve": 0,
      "amp_slide_curve": 0,
      "pitch_slide_shape": 1,
      "window_size": 0.2,
      "window_size_slide": 0,
      "pitch_dis_slide": 0,
      "hpf_sustain_level": -1,
      "lpf_sustain": -1,
      "pre_amp": 1,
      "threshold_slide": 0,
      "threshold_slide_shape": 1,
      "hpf_max_slide_curve": 0,
      "pre_amp_slide_shape": 1,
      "pitch_dis_slide_curve": 0,
      "hpf_max_slide": 0,
      "hpf_max": -1,
      "hpf_sustain": -1,
      "pitch_dis": 0.0,
      "lpf_slide_curve": 0,
      "decay": 0,
      "hpf_decay_level": -1,
      "attack_level": 1,
      "relax_time_slide_curve": 0,
      "lpf_slide": 0,
      "lpf_min_slide": 0,
      "time_dis": 0.0,
      "rate": 1,
      "pitch": 0,
      "lpf_min_slide_shape": 1,
      "clamp_time": 0.01,
      "hpf_decay": 0,
      "hpf_slide": 0,
      "pitch_slide": 0,
      "hpf_release_level": -1,
      "hpf_slide_curve": 0,
      "lpf_min_slide_curve": 0,
      "release": 0,
      "time_dis_slide": 0,
      "clamp_time_slide": 0,
      "lpf_min": -1,
      "hpf_release": 0,
      "pan_slide_shape": 1,
      "sustain": -1,
      "slope_below_slide_curve": 0,
      "lpf_attack_level": -1,
      "hpf": -1,
      "amp": 1,
      "threshold": 0.2,
      "lpf_slide_shape": 1,
      "hpf_attack": 0,
      "pan_slide_curve": 0,
      "lpf_attack": 0,
      "time_dis_slide_curve": 0,
      "lpf_release_level": -1,
      "slope_below_slide": 0,
      "lpf_env_curve": 2,
      "slope_above_slide": 0,
      "start": 0,
      "lpf_decay": 0,
      "clamp_time_slide_curve": 0,
      "pan_slide": 0,
      "amp_slide": 0,
      "hpf_env_curve": 2,
      "amp_slide_shape": 1,
      "lpf": -1,
      "hpf_max_slide_shape": 1,
      "norm": 0,
      "lpf_decay_level": -1,
      "clamp_time_slide_shape": 1,
      "hpf_init_level": -1,
      "relax_time_slide_shape": 1,
      "threshold_slide_curve": 0,
      "relax_time_slide": 0,
      "window_size_slide_curve": 0,
      "slope_above_slide_curve": 0,
      "slope_below": 1,
      "hpf_attack_level": -1,
      "pre_amp_slide": 0,
      "attack": 0,
      "lpf_init_level": -1,
      "pitch_dis_slide_shape": 1,
      "slope_above": 0.5,
      "time_dis_slide_shape": 1,
      "slope_below_slide_shape": 1,
      "hpf_slide_shape": 1,
      "pan": 0,
      "pre_amp_slide_curve": 0,
      "slope_above_slide_shape": 1,
      "compress": 0,
      "window_size_slide_shape": 1
    },
    "hiden": true,
    "inherit_base": "BasicMonoPlayer"
  },
  "Singer": {
    "summary": "Singer",
    "name": ":singer",
    "inherit_arg": false,
    "opts": {
      "note": 52,
      "amp_slide_shape": 1,
      "sustain": 0,
      "attack_level": 1,
      "note_slide": 0,
      "decay": 0,
      "attack": 1,
      "amp_slide": 0,
      "note_slide_shape": 1,
      "pan_slide_shape": 1,
      "sustain_level": 1,
      "decay_level": 1,
      "amp": 1,
      "env_curve": 2,
      "pan": 0,
      "release": 4.0,
      "amp_slide_curve": 0,
      "pan_slide": 0,
      "pan_slide_curve": 0,
      "note_slide_curve": 0
    },
    "hiden": true,
    "inherit_base": "SonicPiSynth"
  },
  "Saw": {
    "summary": "Saw Wave",
    "name": ":saw",
    "inherit_arg": true,
    "opts": {
      "amp_slide_shape": 1,
      "sustain": 0,
      "note_slide": 0,
      "decay": 0,
      "attack_level": 1,
      "pan_slide_shape": 1,
      "decay_level": 1,
      "amp": 1,
      "env_curve": 2,
      "amp_slide_curve": 0,
      "pan_slide_curve": 0,
      "note": 52,
      "attack": 0,
      "note_slide_curve": 0,
      "note_slide_shape": 1,
      "sustain_level": 1,
      "pan": 0,
      "release": 1,
      "pan_slide": 0,
      "amp_slide": 0
    },
    "hiden": true,
    "inherit_base": "Beep"
  },
  "Pitchless": {
    "inherit_arg": true,
    "hiden": true,
    "inherit_base": "SonicPiSynth",
    "opts": {}
  },
  "Square": {
    "summary": "Square Wave",
    "name": ":square",
    "inherit_arg": false,
    "opts": {
      "amp_slide_shape": 1,
      "sustain": 0,
      "note_slide": 0,
      "decay": 0,
      "attack_level": 1,
      "pan_slide_shape": 1,
      "decay_level": 1,
      "amp": 1,
      "env_curve": 2,
      "amp_slide_curve": 0,
      "pan_slide_curve": 0,
      "note": 52,
      "attack": 0,
      "note_slide_curve": 0,
      "note_slide_shape": 1,
      "sustain_level": 1,
      "cutoff_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "pan": 0,
      "release": 1,
      "cutoff_slide": 0,
      "pan_slide": 0,
      "amp_slide": 0,
      "cutoff": 100
    },
    "hiden": false,
    "inherit_base": "SonicPiSynth"
  },
  "Growl": {
    "summary": "Growl",
    "name": ":growl",
    "inherit_arg": false,
    "opts": {
      "amp_slide_shape": 1,
      "sustain": 0,
      "note_slide": 0,
      "decay": 0,
      "attack_level": 1,
      "pan_slide_shape": 1,
      "decay_level": 1,
      "amp": 1,
      "env_curve": 2,
      "amp_slide_curve": 0,
      "pan_slide_curve": 0,
      "res": 0.7,
      "note": 52,
      "attack": 0.1,
      "note_slide_curve": 0,
      "res_slide": 0,
      "note_slide_shape": 1,
      "sustain_level": 1,
      "cutoff_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "res_slide_shape": 1,
      "res_slide_curve": 0,
      "pan": 0,
      "release": 1,
      "cutoff_slide": 0,
      "pan_slide": 0,
      "amp_slide": 0,
      "cutoff": 130
    },
    "hiden": false,
    "inherit_base": "SonicPiSynth"
  },
  "SynthViolin": {
    "summary": "Blade Runner style strings",
    "name": ":synth_violin",
    "inherit_arg": false,
    "opts": {
      "vibrato_onset": 0.1,
      "amp_slide_shape": 1,
      "sustain": 0,
      "note_slide": 0,
      "decay": 0,
      "vibrato_rate": 6,
      "attack_level": 1,
      "pan_slide_shape": 1,
      "decay_level": 1,
      "amp": 1,
      "env_curve": 2,
      "vibrato_depth_slide_curve": 0,
      "vibrato_rate_slide_shape": 1,
      "amp_slide_curve": 0,
      "pan_slide_curve": 0,
      "vibrato_depth": 0.15,
      "note": 52,
      "attack": 0,
      "note_slide_curve": 0,
      "vibrato_depth_slide_shape": 1,
      "vibrato_delay": 0.5,
      "note_slide_shape": 1,
      "sustain_level": 1,
      "cutoff_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "pan": 0,
      "release": 1,
      "vibrato_rate_slide_curve": 0,
      "cutoff_slide": 0,
      "pan_slide": 0,
      "amp_slide": 0,
      "cutoff": 100
    },
    "hiden": false,
    "inherit_base": "SonicPiSynth"
  }
}

synth_nodes = {
  ":mod_tri": "ModTri",
  ":piano": "SynthPiano",
  ":fm": "FM",
  ":fx_ring_mod": "FXRingMod",
  ":fx_octaver": "FXOctaver",
  ":beep": "Beep",
  ":fx_replace_nrlpf": "FXNormRLPF",
  ":hoover": "Hoover",
  ":mod_sine": "ModSine",
  ":fx_tanh": "FXTanh",
  ":subpulse": "SubPulse",
  ":chipbass": "ChipBass",
  ":growl": "Growl",
  ":fx_replace_nrhpf": "FXNormRHPF",
  ":mod_saw": "ModSaw",
  ":fx_ixi_techno": "FXIXITechno",
  ":fx_replace_pan": "FXPan",
  ":dsaw": "DSaw",
  ":pulse": "Pulse",
  ":gnoise": "GNoise",
  ":fx_bitcrusher": "FXBitcrusher",
  ":fx_rhpf": "FXRHPF",
  ":fx_pitch_shift": "FXPitchShift",
  ":chiplead": "ChipLead",
  ":fx_flanger": "FXFlanger",
  ":fx_hpf": "FXHPF",
  ":tri": "Tri",
  ":fx_replace_level": "FXLevel",
  ":supersaw": "Supersaw",
  ":fx_nrbpf": "FXNRBPF",
  ":fx_nbpf": "FXNBPF",
  ":fx_replace_reverb": "FXReverb",
  ":mod_dsaw": "ModDSaw",
  ":fx_replace_rlpf": "FXRLPF",
  ":fx_distortion": "FXDistortion",
  ":stereo_player": "StereoPlayer",
  ":mono_player": "MonoPlayer",
  ":mod_pulse": "ModPulse",
  ":fx_bpf": "FXBPF",
  ":fx_vowel": "FXVowel",
  ":fx_wobble": "FXWobble",
  ":fx_normaliser": "FXNormaliser",
  ":fx_compressor": "FXCompressor",
  ":pluck": "SynthPluck",
  ":fx_nhpf": "FXNormHPF",
  ":fx_slicer": "FXSlicer",
  ":fx_pan": "FXPan",
  ":fx_replace_compressor": "FXCompressor",
  ":dull_bell": "DullBell",
  ":hollow": "Hollow",
  ":cnoise": "CNoise",
  ":mod_fm": "ModFM",
  ":fx_replace_nlpf": "FXNormLPF",
  ":basic_stereo_player": "BasicStereoPlayer",
  ":fx_replace_hpf": "FXHPF",
  ":zawa": "Zawa",
  ":dpulse": "DPulse",
  ":fx_reverb": "FXReverb",
  ":fx_rbpf": "FXRBPF",
  ":fx_nlpf": "FXNormLPF",
  ":fx_replace_normaliser": "FXNormaliser",
  ":bnoise": "BNoise",
  ":fx_replace_echo": "FXEcho",
  ":dtri": "DTri",
  ":fx_whammy": "FXWhammy",
  ":basic_mixer": "BasicMixer",
  ":prophet": "Prophet",
  ":main_mixer": "MainMixer",
  ":mod_beep": "ModSine",
  ":fx_replace_ixi_techno": "FXIXITechno",
  ":fx_lpf": "FXLPF",
  ":fx_replace_lpf": "FXLPF",
  ":fx_krush": "FXKrush",
  ":sound_in": "SoundIn",
  ":fx_gverb": "FXGVerb",
  ":fx_replace_distortion": "FXDistortion",
  ":blade": "SynthViolin",
  ":fx_panslicer": "FXPanSlicer",
  ":fx_nrhpf": "FXNormRHPF",
  ":saw": "Saw",
  ":tb303": "TB303",
  ":fx_replace_slicer": "FXSlicer",
  ":noise": "Noise",
  ":fx_replace_rhpf": "FXRHPF",
  ":fx_echo": "FXEcho",
  ":dark_ambience": "DarkAmbience",
  ":chipnoise": "ChipNoise",
  ":fx_level": "FXLevel",
  ":fx_nrlpf": "FXNormRLPF",
  ":fx_replace_nhpf": "FXNormHPF",
  ":fx_replace_wobble": "FXWobble",
  ":pnoise": "PNoise",
  ":pretty_bell": "PrettyBell",
  ":basic_mono_player": "BasicMonoPlayer",
  ":sine": "Beep",
  ":fx_rlpf": "FXRLPF",
  ":tech_saws": "TechSaws",
  ":fx_mono": "FXMono",
  ":sound_in_stereo": "SoundInStereo",
  ":square": "Square",
  ":fx_band_eq": "FXBandEQ"
}

fx = {
  "FXOctaver": {
    "summary": "Octaver",
    "name": ":octaver",
    "inherit_arg": true,
    "opts": {
      "amp_slide_shape": 1,
      "super_amp_slide_shape": 1,
      "amp_slide": 0,
      "subsub_amp_slide_curve": 0,
      "amp": 1,
      "mix": 1,
      "pre_mix_slide_shape": 1,
      "super_amp": 1,
      "pre_mix_slide": 0,
      "amp_slide_curve": 0,
      "subsub_amp_slide_shape": 1,
      "sub_amp_slide": 0,
      "sub_amp_slide_shape": 1,
      "pre_amp_slide": 0,
      "subsub_amp_slide": 0,
      "pre_amp": 1,
      "subsub_amp": 1,
      "mix_slide": 0,
      "sub_amp_slide_curve": 0,
      "super_amp_slide": 0,
      "pre_mix_slide_curve": 0,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "super_amp_slide_curve": 0,
      "mix_slide_shape": 1,
      "sub_amp": 1,
      "pre_amp_slide_curve": 0,
      "pre_amp_slide_shape": 1
    },
    "hiden": false,
    "inherit_base": "FXInfo"
  },
  "FXVowel": {
    "summary": "Vowel",
    "name": ":vowel",
    "inherit_arg": true,
    "opts": {
      "amp_slide_shape": 1,
      "amp_slide": 0,
      "vowel_sound": 1,
      "amp": 1,
      "mix": 1,
      "pre_mix_slide_shape": 1,
      "pre_mix_slide": 0,
      "amp_slide_curve": 0,
      "pre_amp_slide": 0,
      "pre_amp": 1,
      "mix_slide": 0,
      "pre_mix_slide_curve": 0,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "mix_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "pre_amp_slide_shape": 1,
      "voice": 0
    },
    "hiden": false,
    "inherit_base": "FXInfo"
  },
  "FXSlicer": {
    "summary": "Slicer",
    "name": ":slicer",
    "inherit_arg": true,
    "opts": {
      "smooth_slide": 0,
      "smooth_up_slide": 0,
      "smooth_down_slide_curve": 0,
      "amp_max_slide_curve": 0,
      "smooth_up": 0,
      "smooth_down": 0,
      "mix": 1,
      "pre_mix_slide_shape": 1,
      "amp_max_slide_shape": 1,
      "smooth_up_slide_shape": 1,
      "prob_pos": 0,
      "amp_slide_curve": 0,
      "amp_min_slide_curve": 0,
      "amp_max": 1,
      "smooth_up_slide_curve": 0,
      "smooth_down_slide_shape": 1,
      "amp_min": 0,
      "mix_slide_shape": 1,
      "pulse_width_slide_curve": 0,
      "probability_slide": 0,
      "smooth_down_slide": 0,
      "smooth_slide_shape": 1,
      "pre_amp_slide_shape": 1,
      "invert_wave": 0,
      "amp_slide_shape": 1,
      "phase_slide": 0,
      "prob_pos_slide": 0,
      "pre_amp": 1,
      "amp_slide": 0,
      "phase_slide_curve": 0,
      "smooth_slide_curve": 0,
      "pulse_width_slide_shape": 1,
      "probability": 0,
      "smooth": 0,
      "probability_slide_shape": 1,
      "pre_mix_slide": 0,
      "phase": 0.25,
      "prob_pos_slide_shape": 1,
      "pre_amp_slide": 0,
      "amp_min_slide_shape": 1,
      "probability_slide_curve": 0,
      "wave": 1,
      "amp_min_slide": 0,
      "amp": 1,
      "pre_mix_slide_curve": 0,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "amp_max_slide": 0,
      "mix_slide": 0,
      "pulse_width": 0.5,
      "phase_offset": 0,
      "seed": 0,
      "pre_amp_slide_curve": 0,
      "prob_pos_slide_curve": 0,
      "pulse_width_slide": 0,
      "phase_slide_shape": 1
    },
    "hiden": false,
    "inherit_base": "FXInfo"
  },
  "FXNormLPF": {
    "summary": "Normalised Low Pass Filter.",
    "name": ":nlpf",
    "inherit_arg": true,
    "opts": {
      "amp_slide_shape": 1,
      "mix_slide_shape": 1,
      "amp_slide": 0,
      "amp": 1,
      "mix": 1,
      "pre_mix_slide_shape": 1,
      "pre_mix_slide": 0,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "pre_amp_slide": 0,
      "pre_amp": 1,
      "mix_slide": 0,
      "pre_mix_slide_curve": 0,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "cutoff_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "pre_amp_slide_shape": 1,
      "cutoff_slide": 0,
      "cutoff": 100
    },
    "hiden": true,
    "inherit_base": "FXLPF"
  },
  "FXLPF": {
    "summary": "Low Pass Filter",
    "name": ":lpf",
    "inherit_arg": true,
    "opts": {
      "amp_slide_shape": 1,
      "amp_slide": 0,
      "amp": 1,
      "mix": 1,
      "pre_mix_slide_shape": 1,
      "pre_mix_slide": 0,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "pre_amp_slide": 0,
      "cutoff_slide_shape": 1,
      "pre_amp": 1,
      "mix_slide": 0,
      "pre_mix_slide_curve": 0,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "mix_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "pre_amp_slide_shape": 1,
      "cutoff_slide": 0,
      "cutoff": 100
    },
    "hiden": false,
    "inherit_base": "FXInfo"
  },
  "FXDistortion": {
    "summary": "Distortion",
    "name": ":distortion",
    "inherit_arg": true,
    "opts": {
      "amp_slide_shape": 1,
      "distort_slide": 0,
      "amp_slide": 0,
      "amp": 1,
      "mix": 1,
      "pre_mix_slide_shape": 1,
      "pre_mix_slide": 0,
      "amp_slide_curve": 0,
      "pre_amp_slide": 0,
      "pre_amp": 1,
      "mix_slide": 0,
      "distort_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "distort_slide_curve": 0,
      "mix_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "pre_amp_slide_shape": 1,
      "distort": 0.5
    },
    "hiden": false,
    "inherit_base": "FXInfo"
  },
  "FXFlanger": {
    "summary": "Flanger",
    "name": ":flanger",
    "inherit_arg": true,
    "opts": {
      "phase_slide_shape": 1,
      "amp_slide_shape": 1,
      "phase_slide": 0,
      "delay_slide_curve": 0,
      "decay": 2,
      "depth_slide": 0,
      "amp_slide": 0,
      "feedback_slide": 0,
      "phase_slide_curve": 0,
      "stereo_invert_wave": 0,
      "amp": 1,
      "delay_slide": 0,
      "mix": 1,
      "pre_mix_slide_shape": 1,
      "max_delay": 20,
      "depth_slide_shape": 1,
      "feedback": 0,
      "pre_mix_slide": 0,
      "amp_slide_curve": 0,
      "phase": 4,
      "depth": 5,
      "pre_amp_slide": 0,
      "pre_amp": 1,
      "delay_slide_shape": 1,
      "wave": 4,
      "mix_slide": 0,
      "feedback_slide_curve": 0,
      "feedback_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "decay_slide_shape": 1,
      "mix_slide_shape": 1,
      "invert_flange": 0,
      "decay_slide_curve": 0,
      "phase_offset": 0,
      "pre_amp_slide_curve": 0,
      "pre_amp_slide_shape": 1,
      "invert_wave": 0,
      "decay_slide": 0,
      "delay": 5,
      "depth_slide_curve": 0
    },
    "hiden": false,
    "inherit_base": "FXInfo"
  },
  "FXWobble": {
    "summary": "Wobble",
    "name": ":wobble",
    "inherit_arg": true,
    "opts": {
      "cutoff_min_slide_shape": 1,
      "smooth_slide": 0,
      "smooth_down_slide_curve": 0,
      "cutoff_max_slide_shape": 1,
      "filter": 0,
      "amp": 1,
      "cutoff_min": 60,
      "mix": 1,
      "pre_mix_slide_shape": 1,
      "smooth_up_slide_shape": 1,
      "prob_pos": 0,
      "amp_slide_curve": 0,
      "res_slide": 0,
      "smooth_up_slide_curve": 0,
      "phase_slide": 0,
      "wave": 0,
      "mix_slide_shape": 1,
      "cutoff_max_slide_curve": 0,
      "cutoff_max": 120,
      "phase": 0.5,
      "pulse_width_slide_curve": 0,
      "prob_pos_slide": 0,
      "prob_pos_slide_shape": 1,
      "smooth_down_slide": 0,
      "cutoff_min_slide_curve": 0,
      "pulse_width": 0.5,
      "pre_amp_slide_shape": 1,
      "invert_wave": 0,
      "res_slide_shape": 1,
      "res_slide_curve": 0,
      "cutoff_min_slide": 0,
      "amp_slide_shape": 1,
      "prob_pos_slide_curve": 0,
      "res": 0.8,
      "smooth_down_slide_shape": 1,
      "amp_slide": 0,
      "phase_slide_curve": 0,
      "smooth_slide_curve": 0,
      "pulse_width_slide_shape": 1,
      "probability": 0,
      "smooth": 0,
      "probability_slide_shape": 1,
      "pre_mix_slide": 0,
      "smooth_up_slide": 0,
      "probability_slide": 0,
      "pre_amp_slide": 0,
      "pre_amp": 1,
      "cutoff_max_slide": 0,
      "probability_slide_curve": 0,
      "smooth_up": 0,
      "pre_mix_slide_curve": 0,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "mix_slide": 0,
      "smooth_slide_shape": 1,
      "phase_offset": 0,
      "seed": 0,
      "pre_amp_slide_curve": 0,
      "smooth_down": 0,
      "pulse_width_slide": 0,
      "phase_slide_shape": 1
    },
    "hiden": false,
    "inherit_base": "FXInfo"
  },
  "FXIXITechno": {
    "summary": "Techno from IXI Lang",
    "name": ":ixi_techno",
    "inherit_arg": true,
    "opts": {
      "amp_slide_shape": 1,
      "phase_slide": 0,
      "res": 0.8,
      "res_slide": 0,
      "cutoff_min_slide_curve": 0,
      "amp_slide": 0,
      "cutoff_min_slide": 0,
      "cutoff_max_slide_shape": 1,
      "phase_slide_curve": 0,
      "amp": 1,
      "cutoff_min": 60,
      "mix": 1,
      "pre_mix_slide_shape": 1,
      "cutoff_max": 120,
      "cutoff_min_slide_shape": 1,
      "pre_mix_slide": 0,
      "amp_slide_curve": 0,
      "phase": 4,
      "pre_amp_slide": 0,
      "pre_amp": 1,
      "cutoff_max_slide": 0,
      "mix_slide": 0,
      "cutoff_max_slide_curve": 0,
      "pre_mix_slide_curve": 0,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "mix_slide_shape": 1,
      "phase_offset": 0,
      "pre_amp_slide_curve": 0,
      "pre_amp_slide_shape": 1,
      "res_slide_shape": 1,
      "res_slide_curve": 0,
      "phase_slide_shape": 1
    },
    "hiden": false,
    "inherit_base": "FXInfo"
  },
  "FXWhammy": {
    "summary": "Whammy",
    "name": ":whammy",
    "inherit_arg": true,
    "opts": {
      "deltime": 0.05,
      "amp_slide_shape": 1,
      "max_delay_time": 1,
      "amp_slide": 0,
      "transpose_slide_shape": 1,
      "amp": 1,
      "mix": 1,
      "pre_mix_slide_shape": 1,
      "pre_mix_slide": 0,
      "amp_slide_curve": 0,
      "grainsize": 0.075,
      "transpose_slide_curve": 0,
      "pre_amp_slide": 0,
      "pre_amp": 1,
      "transpose_slide": 0,
      "transpose": 12,
      "mix_slide": 0,
      "pre_mix_slide_curve": 0,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "mix_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "pre_amp_slide_shape": 1
    },
    "hiden": false,
    "inherit_base": "FXInfo"
  },
  "FXEcho": {
    "summary": "Echo",
    "name": ":echo",
    "inherit_arg": true,
    "opts": {
      "amp_slide_shape": 1,
      "phase_slide": 0,
      "decay": 2,
      "amp_slide": 0,
      "phase_slide_curve": 0,
      "amp": 1,
      "mix": 1,
      "pre_mix_slide_shape": 1,
      "pre_mix_slide": 0,
      "amp_slide_curve": 0,
      "phase": 0.25,
      "pre_amp_slide": 0,
      "pre_amp": 1,
      "mix_slide": 0,
      "pre_mix_slide_curve": 0,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "decay_slide_shape": 1,
      "mix_slide_shape": 1,
      "decay_slide_curve": 0,
      "pre_amp_slide_curve": 0,
      "max_phase": 2,
      "pre_amp_slide_shape": 1,
      "decay_slide": 0,
      "phase_slide_shape": 1
    },
    "hiden": false,
    "inherit_base": "FXInfo"
  },
  "FXLevel": {
    "summary": "Level Amplifier",
    "name": ":level",
    "inherit_arg": false,
    "opts": {
      "amp": 1,
      "amp_slide": 0,
      "amp_slide_curve": 0,
      "amp_slide_shape": 1
    },
    "hiden": false,
    "inherit_base": "FXInfo"
  },
  "FXGVerb": {
    "summary": "GVerb",
    "name": ":gverb",
    "inherit_arg": true,
    "opts": {
      "amp_slide_shape": 1,
      "damp_slide": 0,
      "dry_slide_shape": 1,
      "ref_level": 0.7,
      "amp_slide": 0,
      "spread_slide_curve": 0,
      "damp_slide_shape": 1,
      "damp": 0.5,
      "amp": 1,
      "spread": 0.5,
      "mix": 1,
      "pre_mix_slide_shape": 1,
      "spread_slide_shape": 1,
      "dry_slide_curve": 0,
      "pre_damp": 0.5,
      "pre_mix_slide": 0,
      "amp_slide_curve": 0,
      "pre_damp_slide": 0,
      "dry": 1,
      "pre_amp_slide": 0,
      "room": 10,
      "pre_amp": 1,
      "tail_level": 0.5,
      "spread_slide": 0,
      "mix_slide": 0,
      "pre_damp_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "mix_slide_shape": 1,
      "damp_slide_curve": 0,
      "dry_slide": 0,
      "pre_amp_slide_curve": 0,
      "release": 3,
      "pre_amp_slide_shape": 1,
      "pre_damp_slide_curve": 0
    },
    "hiden": false,
    "inherit_base": "FXInfo"
  },
  "FXNormHPF": {
    "summary": "Normalised High Pass Filter",
    "name": ":nhpf",
    "inherit_arg": true,
    "opts": {
      "amp_slide_shape": 1,
      "mix_slide_shape": 1,
      "amp_slide": 0,
      "amp": 1,
      "mix": 1,
      "pre_mix_slide_shape": 1,
      "pre_mix_slide": 0,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "pre_amp_slide": 0,
      "pre_amp": 1,
      "mix_slide": 0,
      "pre_mix_slide_curve": 0,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "cutoff_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "pre_amp_slide_shape": 1,
      "cutoff_slide": 0,
      "cutoff": 100
    },
    "hiden": true,
    "inherit_base": "FXHPF"
  },
  "FXRLPF": {
    "summary": "Resonant Low Pass Filter",
    "name": ":rlpf",
    "inherit_arg": true,
    "opts": {
      "amp_slide_shape": 1,
      "mix_slide_shape": 1,
      "res": 0.5,
      "res_slide": 0,
      "amp_slide": 0,
      "amp": 1,
      "mix": 1,
      "pre_mix_slide_shape": 1,
      "pre_mix_slide": 0,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "pre_amp_slide": 0,
      "pre_amp": 1,
      "mix_slide": 0,
      "pre_mix_slide_curve": 0,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "cutoff_slide_shape": 1,
      "res_slide_curve": 0,
      "pre_amp_slide_curve": 0,
      "pre_amp_slide_shape": 1,
      "cutoff_slide": 0,
      "res_slide_shape": 1,
      "cutoff": 100
    },
    "hiden": true,
    "inherit_base": "FXLPF"
  },
  "FXPanSlicer": {
    "summary": "Pan Slicer",
    "name": ":panslicer",
    "inherit_arg": true,
    "opts": {
      "smooth_slide": 0,
      "pan_max_slide": 0,
      "smooth_down_slide_curve": 0,
      "amp_slide_shape": 1,
      "smooth_up": 0,
      "smooth_down": 0,
      "mix": 1,
      "pre_mix_slide_shape": 1,
      "mix_slide_curve": 0,
      "smooth_up_slide_shape": 1,
      "prob_pos": 0,
      "amp_slide_curve": 0,
      "pan_min": -1,
      "pan_min_slide": 0,
      "amp_min_slide_curve": 0,
      "amp_max": 1,
      "pan_min_slide_curve": 0,
      "smooth_up_slide_curve": 0,
      "prob_pos_slide": 0,
      "amp_min": 0,
      "mix_slide": 0,
      "phase": 0.25,
      "pulse_width_slide_curve": 0,
      "prob_pos_slide_shape": 1,
      "smooth_down_slide": 0,
      "pulse_width": 0.5,
      "smooth_up_slide": 0,
      "pre_amp_slide": 0,
      "amp_max_slide_curve": 0,
      "phase_slide": 0,
      "pan_max": 1,
      "smooth_down_slide_shape": 1,
      "amp_min_slide_shape": 1,
      "pan_min_slide_shape": 1,
      "amp_slide": 0,
      "phase_slide_curve": 0,
      "smooth_slide_curve": 0,
      "pulse_width_slide_shape": 1,
      "probability": 0,
      "smooth": 0,
      "probability_slide_shape": 1,
      "pre_mix_slide": 0,
      "pre_amp_slide_shape": 1,
      "probability_slide": 0,
      "invert_wave": 0,
      "pre_amp": 1,
      "probability_slide_curve": 0,
      "wave": 1,
      "amp_min_slide": 0,
      "amp": 1,
      "pre_mix_slide_curve": 0,
      "amp_max_slide_shape": 1,
      "pre_mix": 1,
      "amp_max_slide": 0,
      "mix_slide_shape": 1,
      "smooth_slide_shape": 1,
      "phase_offset": 0,
      "seed": 0,
      "pre_amp_slide_curve": 0,
      "pulse_width_slide": 0,
      "pan_max_slide_shape": 1,
      "pan_max_slide_curve": 0,
      "prob_pos_slide_curve": 0,
      "phase_slide_shape": 1
    },
    "hiden": true,
    "inherit_base": "FXSlicer"
  },
  "FXTanh": {
    "summary": "Hyperbolic Tangent",
    "name": ":tanh",
    "inherit_arg": true,
    "opts": {
      "amp_slide_shape": 1,
      "amp_slide": 0,
      "krunch": 5,
      "amp": 1,
      "mix": 1,
      "pre_mix_slide_shape": 1,
      "pre_mix_slide": 0,
      "amp_slide_curve": 0,
      "krunch_slide_shape": 1,
      "pre_amp_slide": 0,
      "pre_amp": 1,
      "krunch_slide": 0,
      "mix_slide": 0,
      "pre_mix_slide_curve": 0,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "mix_slide_shape": 1,
      "krunch_slide_curve": 0,
      "pre_amp_slide_curve": 0,
      "pre_amp_slide_shape": 1
    },
    "hiden": false,
    "inherit_base": "FXInfo"
  },
  "FXNormRHPF": {
    "summary": "Normalised Resonant High Pass Filter",
    "name": ":nrhpf",
    "inherit_arg": true,
    "opts": {
      "amp_slide_shape": 1,
      "res": 0.5,
      "pre_amp": 1,
      "amp_slide": 0,
      "amp": 1,
      "mix": 1,
      "pre_mix_slide_shape": 1,
      "pre_mix_slide": 0,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "pre_amp_slide": 0,
      "cutoff_slide_shape": 1,
      "res_slide": 0,
      "mix_slide": 0,
      "pre_mix_slide_curve": 0,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "mix_slide_shape": 1,
      "cutoff": 100,
      "pre_amp_slide_curve": 0,
      "pre_amp_slide_shape": 1,
      "cutoff_slide": 0,
      "res_slide_shape": 1,
      "res_slide_curve": 0
    },
    "hiden": true,
    "inherit_base": "FXRHPF"
  },
  "FXBandEQ": {
    "summary": "Band EQ Filter",
    "name": ":band_eq",
    "inherit_arg": true,
    "opts": {
      "freq_slide": 0,
      "amp_slide_shape": 1,
      "db": 0.6,
      "res": 0.6,
      "res_slide": 0,
      "amp_slide": 0,
      "amp": 1,
      "db_slide": 0,
      "mix": 1,
      "pre_mix_slide_shape": 1,
      "freq": 100,
      "freq_slide_shape": 1,
      "pre_mix_slide": 0,
      "amp_slide_curve": 0,
      "pre_amp_slide": 0,
      "pre_amp": 1,
      "mix_slide": 0,
      "db_slide_curve": 0,
      "res_slide_shape": 1,
      "db_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "mix_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "pre_amp_slide_shape": 1,
      "freq_slide_curve": 0,
      "res_slide_curve": 0
    },
    "hiden": false,
    "inherit_base": "FXInfo"
  },
  "FXInfo": {
    "inherit_arg": false,
    "hiden": true,
    "inherit_base": "BaseInfo",
    "opts": {
      "pre_amp": 1,
      "amp_slide_shape": 1,
      "mix_slide_shape": 1,
      "mix_slide": 0,
      "amp_slide": 0,
      "pre_mix_slide_curve": 0,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "amp": 1,
      "mix": 1,
      "pre_mix_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "pre_mix_slide": 0,
      "amp_slide_curve": 0,
      "pre_amp_slide_shape": 1,
      "pre_amp_slide": 0
    }
  },
  "FXReverb": {
    "summary": "Reverb",
    "name": ":reverb",
    "inherit_arg": true,
    "opts": {
      "amp_slide_shape": 1,
      "damp_slide": 0,
      "room_slide_shape": 1,
      "amp_slide": 0,
      "damp_slide_shape": 1,
      "damp": 0.5,
      "amp": 1,
      "mix": 0.4,
      "pre_mix_slide_shape": 1,
      "pre_mix_slide": 0,
      "amp_slide_curve": 0,
      "room": 0.6,
      "room_slide_curve": 0,
      "pre_amp_slide": 0,
      "pre_amp": 1,
      "mix_slide": 0,
      "pre_mix_slide_curve": 0,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "mix_slide_shape": 1,
      "damp_slide_curve": 0,
      "pre_amp_slide_curve": 0,
      "room_slide": 0,
      "pre_amp_slide_shape": 1
    },
    "hiden": false,
    "inherit_base": "FXInfo"
  },
  "FXRingMod": {
    "summary": "Ring Modulator",
    "name": ":ring_mod",
    "inherit_arg": true,
    "opts": {
      "freq_slide": 0,
      "amp_slide_shape": 1,
      "amp_slide": 0,
      "amp": 1,
      "mix": 1,
      "pre_mix_slide_shape": 1,
      "freq": 30,
      "freq_slide_shape": 1,
      "pre_mix_slide": 0,
      "amp_slide_curve": 0,
      "mod_amp_slide_curve": 0,
      "pre_amp_slide": 0,
      "pre_amp": 1,
      "mod_amp_slide": 0,
      "mix_slide": 0,
      "pre_mix_slide_curve": 0,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "mix_slide_shape": 1,
      "mod_amp_slide_shape": 1,
      "mod_amp": 1,
      "pre_amp_slide_curve": 0,
      "pre_amp_slide_shape": 1,
      "freq_slide_curve": 0
    },
    "hiden": false,
    "inherit_base": "FXInfo"
  },
  "FXHPF": {
    "summary": "High Pass Filter",
    "name": ":hpf",
    "inherit_arg": true,
    "opts": {
      "amp_slide_shape": 1,
      "amp_slide": 0,
      "amp": 1,
      "mix": 1,
      "pre_mix_slide_shape": 1,
      "pre_mix_slide": 0,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "pre_amp_slide": 0,
      "cutoff_slide_shape": 1,
      "pre_amp": 1,
      "mix_slide": 0,
      "pre_mix_slide_curve": 0,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "mix_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "pre_amp_slide_shape": 1,
      "cutoff_slide": 0,
      "cutoff": 100
    },
    "hiden": false,
    "inherit_base": "FXInfo"
  },
  "FXRBPF": {
    "summary": "Resonant Band Pass Filter",
    "name": ":rbpf",
    "inherit_arg": true,
    "opts": {
      "amp_slide_shape": 1,
      "res": 0.5,
      "centre_slide_curve": 0,
      "pre_amp": 1,
      "amp_slide": 0,
      "pre_mix_slide_curve": 0,
      "amp": 1,
      "mix": 1,
      "pre_mix_slide_shape": 1,
      "centre_slide_shape": 1,
      "pre_mix_slide": 0,
      "amp_slide_curve": 0,
      "centre_slide": 0,
      "pre_amp_slide": 0,
      "res_slide": 0,
      "mix_slide_shape": 1,
      "centre": 100,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "mix_slide": 0,
      "pre_amp_slide_curve": 0,
      "pre_amp_slide_shape": 1,
      "res_slide_shape": 1,
      "res_slide_curve": 0
    },
    "hiden": true,
    "inherit_base": "FXBPF"
  },
  "FXKrush": {
    "summary": "krush",
    "name": ":krush",
    "inherit_arg": true,
    "opts": {
      "amp_slide_shape": 1,
      "gain_slide_shape": 1,
      "res": 0,
      "res_slide": 0,
      "amp_slide": 0,
      "gain_slide__curve": 0,
      "amp": 1,
      "mix": 1,
      "pre_mix_slide_shape": 1,
      "pre_mix_slide": 0,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "pre_amp_slide": 0,
      "cutoff_slide_shape": 1,
      "pre_amp": 1,
      "mix_slide": 0,
      "gain": 5,
      "pre_mix_slide_curve": 0,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "mix_slide_shape": 1,
      "gain_slide": 0,
      "cutoff": 100,
      "pre_amp_slide_curve": 0,
      "pre_amp_slide_shape": 1,
      "cutoff_slide": 0,
      "res_slide_shape": 1,
      "res_slide_curve": 0
    },
    "hiden": false,
    "inherit_base": "FXInfo"
  },
  "FXBitcrusher": {
    "summary": "Bitcrusher",
    "name": ":bitcrusher",
    "inherit_arg": true,
    "opts": {
      "bits_slide": 0,
      "amp_slide_shape": 1,
      "sample_rate": 10000,
      "amp_slide": 0,
      "sample_rate_slide_shape": 1,
      "amp": 1,
      "mix": 1,
      "pre_mix_slide_shape": 1,
      "sample_rate_slide_curve": 0,
      "pre_mix_slide": 0,
      "amp_slide_curve": 0,
      "sample_rate_slide": 0,
      "cutoff_slide_curve": 0,
      "pre_amp_slide": 0,
      "cutoff_slide_shape": 1,
      "pre_amp": 1,
      "bits_slide_shape": 1,
      "mix_slide": 0,
      "pre_mix_slide_curve": 0,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "bits": 8,
      "mix_slide_shape": 1,
      "bits_slide_curve": 0,
      "pre_amp_slide_curve": 0,
      "pre_amp_slide_shape": 1,
      "cutoff_slide": 0,
      "cutoff": 0
    },
    "hiden": false,
    "inherit_base": "FXInfo"
  },
  "FXCompressor": {
    "summary": "Compressor",
    "name": ":compressor",
    "inherit_arg": true,
    "opts": {
      "amp_slide_shape": 1,
      "relax_time": 0.01,
      "amp_slide": 0,
      "clamp_time_slide_shape": 1,
      "amp": 1,
      "clamp_time_slide": 0,
      "mix": 1,
      "pre_mix_slide_shape": 1,
      "relax_time_slide_shape": 1,
      "threshold_slide_curve": 0,
      "pre_mix_slide": 0,
      "amp_slide_curve": 0,
      "slope_above_slide": 0,
      "slope_below": 1,
      "pre_amp_slide": 0,
      "pre_amp": 1,
      "clamp_time": 0.01,
      "slope_above_slide_curve": 0,
      "slope_below_slide": 0,
      "relax_time_slide_curve": 0,
      "mix_slide": 0,
      "slope_above_slide_shape": 1,
      "threshold_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "threshold_slide": 0,
      "mix_slide_shape": 1,
      "threshold": 0.2,
      "slope_below_slide_shape": 1,
      "clamp_time_slide_curve": 0,
      "pre_amp_slide_curve": 0,
      "slope_below_slide_curve": 0,
      "pre_amp_slide_shape": 1,
      "relax_time_slide": 0,
      "slope_above": 0.5
    },
    "hiden": false,
    "inherit_base": "FXInfo"
  },
  "FXBPF": {
    "summary": "Band Pass Filter",
    "name": ":bpf",
    "inherit_arg": true,
    "opts": {
      "amp_slide_shape": 1,
      "res": 0.6,
      "centre_slide_curve": 0,
      "res_slide": 0,
      "amp_slide": 0,
      "centre": 100,
      "amp": 1,
      "mix": 1,
      "pre_mix_slide_shape": 1,
      "centre_slide_shape": 1,
      "pre_mix_slide": 0,
      "amp_slide_curve": 0,
      "centre_slide": 0,
      "pre_amp_slide": 0,
      "pre_amp": 1,
      "mix_slide": 0,
      "pre_mix_slide_curve": 0,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "mix_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "pre_amp_slide_shape": 1,
      "res_slide_shape": 1,
      "res_slide_curve": 0
    },
    "hiden": false,
    "inherit_base": "FXInfo"
  },
  "FXChorus": {
    "summary": "Chorus",
    "name": ":chorus",
    "inherit_arg": true,
    "opts": {
      "amp_slide_shape": 1,
      "phase_slide": 0,
      "decay": 1e-05,
      "amp_slide": 0,
      "phase_slide_curve": 0,
      "amp": 1,
      "mix": 1,
      "pre_mix_slide_shape": 1,
      "pre_mix_slide": 0,
      "amp_slide_curve": 0,
      "phase": 0.25,
      "pre_amp_slide": 0,
      "pre_amp": 1,
      "mix_slide": 0,
      "pre_mix_slide_curve": 0,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "decay_slide_shape": 1,
      "mix_slide_shape": 1,
      "decay_slide_curve": 0,
      "pre_amp_slide_curve": 0,
      "max_phase": 1,
      "pre_amp_slide_shape": 1,
      "decay_slide": 0,
      "phase_slide_shape": 1
    },
    "hiden": true,
    "inherit_base": "FXInfo"
  },
  "FXNBPF": {
    "summary": "Normalised Band Pass Filter",
    "name": ":nbpf",
    "inherit_arg": true,
    "opts": {
      "amp_slide_shape": 1,
      "res": 0.6,
      "centre_slide_curve": 0,
      "pre_amp": 1,
      "amp_slide": 0,
      "pre_mix_slide_curve": 0,
      "amp": 1,
      "mix": 1,
      "pre_mix_slide_shape": 1,
      "centre_slide_shape": 1,
      "pre_mix_slide": 0,
      "amp_slide_curve": 0,
      "centre_slide": 0,
      "pre_amp_slide": 0,
      "res_slide": 0,
      "mix_slide_shape": 1,
      "centre": 100,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "mix_slide": 0,
      "pre_amp_slide_curve": 0,
      "pre_amp_slide_shape": 1,
      "res_slide_shape": 1,
      "res_slide_curve": 0
    },
    "hiden": true,
    "inherit_base": "FXBPF"
  },
  "FXMono": {
    "summary": "Mono",
    "name": ":mono",
    "inherit_arg": true,
    "opts": {
      "amp_slide_shape": 1,
      "amp_slide": 0,
      "pan_slide_shape": 1,
      "amp": 1,
      "mix": 1,
      "pre_mix_slide_shape": 1,
      "pre_mix_slide": 0,
      "amp_slide_curve": 0,
      "pan_slide_curve": 0,
      "pre_amp_slide": 0,
      "pre_amp": 1,
      "mix_slide": 0,
      "pre_mix_slide_curve": 0,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "mix_slide_shape": 1,
      "pan": 0,
      "pre_amp_slide_curve": 0,
      "pre_amp_slide_shape": 1,
      "pan_slide": 0
    },
    "hiden": false,
    "inherit_base": "FXInfo"
  },
  "FXNormaliser": {
    "summary": "Normaliser",
    "name": ":normaliser",
    "inherit_arg": true,
    "opts": {
      "amp_slide_shape": 1,
      "level_slide_shape": 1,
      "level_slide": 0,
      "level_slide_curve": 0,
      "amp_slide": 0,
      "amp": 1,
      "mix": 1,
      "pre_mix_slide_shape": 1,
      "pre_mix_slide": 0,
      "amp_slide_curve": 0,
      "pre_amp_slide": 0,
      "pre_amp": 1,
      "mix_slide": 0,
      "level": 1,
      "pre_mix_slide_curve": 0,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "mix_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "pre_amp_slide_shape": 1
    },
    "hiden": false,
    "inherit_base": "FXInfo"
  },
  "FXNRBPF": {
    "summary": "Normalised Resonant Band Pass Filter",
    "name": ":nrbpf",
    "inherit_arg": true,
    "opts": {
      "amp_slide_shape": 1,
      "res": 0.5,
      "centre_slide_curve": 0,
      "res_slide": 0,
      "amp_slide": 0,
      "centre": 100,
      "amp": 1,
      "mix": 1,
      "pre_mix_slide_shape": 1,
      "centre_slide_shape": 1,
      "pre_mix_slide": 0,
      "amp_slide_curve": 0,
      "centre_slide": 0,
      "pre_amp_slide": 0,
      "pre_amp": 1,
      "mix_slide": 0,
      "pre_mix_slide_curve": 0,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "mix_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "pre_amp_slide_shape": 1,
      "res_slide_shape": 1,
      "res_slide_curve": 0
    },
    "hiden": true,
    "inherit_base": "FXRBPF"
  },
  "FXPan": {
    "summary": "Pan",
    "name": ":pan",
    "inherit_arg": true,
    "opts": {
      "amp_slide_shape": 1,
      "amp_slide": 0,
      "pan_slide_shape": 1,
      "amp": 1,
      "mix": 1,
      "pre_mix_slide_shape": 1,
      "pre_mix_slide": 0,
      "amp_slide_curve": 0,
      "pan_slide_curve": 0,
      "pre_amp_slide": 0,
      "pre_amp": 1,
      "mix_slide": 0,
      "pre_mix_slide_curve": 0,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "mix_slide_shape": 1,
      "pan": 0,
      "pre_amp_slide_curve": 0,
      "pre_amp_slide_shape": 1,
      "pan_slide": 0
    },
    "hiden": false,
    "inherit_base": "FXInfo"
  },
  "FXNormRLPF": {
    "summary": "Normalised Resonant Low Pass Filter",
    "name": ":nrlpf",
    "inherit_arg": true,
    "opts": {
      "amp_slide_shape": 1,
      "res": 0.5,
      "pre_amp": 1,
      "amp_slide": 0,
      "amp": 1,
      "mix": 1,
      "pre_mix_slide_shape": 1,
      "pre_mix_slide": 0,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "pre_amp_slide": 0,
      "cutoff_slide_shape": 1,
      "res_slide": 0,
      "mix_slide": 0,
      "pre_mix_slide_curve": 0,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "mix_slide_shape": 1,
      "cutoff": 100,
      "pre_amp_slide_curve": 0,
      "pre_amp_slide_shape": 1,
      "cutoff_slide": 0,
      "res_slide_shape": 1,
      "res_slide_curve": 0
    },
    "hiden": true,
    "inherit_base": "FXRLPF"
  },
  "FXRHPF": {
    "summary": "Resonant High Pass Filter",
    "name": ":rhpf",
    "inherit_arg": true,
    "opts": {
      "amp_slide_shape": 1,
      "mix_slide_shape": 1,
      "res": 0.5,
      "res_slide": 0,
      "amp_slide": 0,
      "amp": 1,
      "mix": 1,
      "pre_mix_slide_shape": 1,
      "pre_mix_slide": 0,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "pre_amp_slide": 0,
      "pre_amp": 1,
      "mix_slide": 0,
      "pre_mix_slide_curve": 0,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "cutoff_slide_shape": 1,
      "res_slide_curve": 0,
      "pre_amp_slide_curve": 0,
      "pre_amp_slide_shape": 1,
      "cutoff_slide": 0,
      "res_slide_shape": 1,
      "cutoff": 100
    },
    "hiden": true,
    "inherit_base": "FXHPF"
  },
  "FXPitchShift": {
    "summary": "Pitch shift",
    "name": ":pitch_shift",
    "inherit_arg": true,
    "opts": {
      "amp_slide_shape": 1,
      "pitch_dis": 0.0,
      "pitch_slide_curve": 0,
      "amp_slide": 0,
      "time_dis_slide_curve": 0,
      "pitch_dis_slide_shape": 1,
      "amp": 1,
      "mix": 1,
      "pre_mix_slide_shape": 1,
      "pre_mix_slide": 0,
      "amp_slide_curve": 0,
      "window_size_slide_curve": 0,
      "pre_amp_slide": 0,
      "pitch_slide_shape": 1,
      "pre_amp": 1,
      "window_size": 0.2,
      "window_size_slide": 0,
      "pitch_dis_slide": 0,
      "mix_slide": 0,
      "pitch_slide": 0,
      "time_dis_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "mix_slide_curve": 0,
      "pre_mix": 1,
      "mix_slide_shape": 1,
      "pitch": 0,
      "time_dis": 0.0,
      "pre_amp_slide_curve": 0,
      "time_dis_slide": 0,
      "pre_amp_slide_shape": 1,
      "pitch_dis_slide_curve": 0,
      "window_size_slide_shape": 1
    },
    "hiden": false,
    "inherit_base": "FXInfo"
  }
}

samples = {
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
  "Sounds featuring guitars": [
    ":guit_harmonics",
    ":guit_e_fifths",
    ":guit_e_slide",
    ":guit_em9"
  ],
  "Vinyl sounds": [
    ":vinyl_backspin",
    ":vinyl_rewind",
    ":vinyl_scratch",
    ":vinyl_hiss"
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
  ]
}

synth_args_types_conversion = {}

synth_opts_types_conversion = {}

