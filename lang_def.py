null = None; true = True; false = False;
#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/

lang_core = {
  "doubles": {
    "args": [
      {
        "start": ":number"
      },
      {
        "num_doubles": ":int"
      }
    ],
    "inline": true,
    "returns": ":ring",
    "summary": "Create a ring of successive doubles",
    "introduced": "2,10,0",
    "accepts_block": false,
    "signature": {
      "start": null,
      "num_doubles": 1
    },
    "hiden": false,
    "memoize": true
  },
  "comment": {
    "hiden": true,
    "requires_block": true,
    "summary": "Block level commenting",
    "introduced": "2,0,0",
    "accepts_block": true,
    "signature": {
      "*args": null,
      "&block": null
    }
  },
  "use_cue_logging": {
    "args": [
      {
        "true_or_false": ":boolean"
      }
    ],
    "summary": "Enable and disable cue logging",
    "introduced": "2,6,0",
    "accepts_block": false,
    "signature": {
      "&block": null,
      "v": null
    },
    "hiden": false
  },
  "one_in": {
    "args": [
      {
        "num": ":number"
      }
    ],
    "inline": true,
    "summary": "Random true value with specified probability",
    "introduced": "2,0,0",
    "accepts_block": false,
    "signature": {
      "num": null
    },
    "hiden": false
  },
  "uncomment": {
    "hiden": true,
    "requires_block": true,
    "summary": "Block level comment ignoring",
    "introduced": "2,0,0",
    "accepts_block": true,
    "signature": {
      "*args": null,
      "&block": null
    }
  },
  "rrand": {
    "intro_fn": true,
    "args": [
      {
        "min": ":number"
      },
      {
        "max": ":number"
      }
    ],
    "inline": true,
    "opts": {
      "step": 1
    },
    "summary": "Generate a random float between two numbers",
    "introduced": "2,0,0",
    "accepts_block": false,
    "signature": {
      "max": null,
      "*opts": null,
      "min": null
    },
    "hiden": false
  },
  "osc": {
    "hiden": true,
    "signature": {
      "path": null,
      "*args": null
    }
  },
  "dice": {
    "args": [
      {
        "num_sides": ":number"
      }
    ],
    "inline": true,
    "summary": "Random dice throw",
    "introduced": "2,0,0",
    "accepts_block": false,
    "signature": {
      "num_sides": 6
    },
    "hiden": false
  },
  "bt": {
    "args": [
      {
        "seconds": ":number"
      }
    ],
    "summary": "Beat time conversion",
    "introduced": "2,8,0",
    "accepts_block": false,
    "signature": {
      "t": null
    },
    "hiden": true
  },
  "pick": {
    "alt_args": [
      {
        "list": ":array"
      }
    ],
    "args": [
      {
        "n": ":number_or_nil"
      }
    ],
    "inline": true,
    "opts": {
      "skip": 0
    },
    "summary": "Randomly pick from list (with duplicates)",
    "introduced": "2,10,0",
    "accepts_block": false,
    "signature": {
      "*args": null
    },
    "hiden": false
  },
  "sleep": {
    "args": [
      {
        "beats": ":number"
      }
    ],
    "summary": "Wait for beat duration",
    "introduced": "2,0,0",
    "advances_time": true,
    "accepts_block": false,
    "signature": {
      "beats": null
    },
    "hiden": false
  },
  "load_example": {
    "args": [
      {
        "path": ":string"
      }
    ],
    "summary": "Load a built-in example",
    "introduced": "2,10,0",
    "accepts_block": false,
    "signature": {
      "example_name": null
    },
    "hiden": true
  },
  "halves": {
    "args": [
      {
        "start": ":number"
      },
      {
        "num_halves": ":int"
      }
    ],
    "inline": true,
    "returns": ":ring",
    "summary": "Create a ring of successive halves",
    "introduced": "2,10,0",
    "accepts_block": false,
    "signature": {
      "start": null,
      "num_halves": 1
    },
    "hiden": false,
    "memoize": true
  },
  "clear": {
    "args": [],
    "returns": null,
    "summary": "Clear all thread locals to defaults",
    "introduced": "2,11,0",
    "accepts_block": false,
    "hiden": false
  },
  "rt": {
    "args": [
      {
        "seconds": ":number"
      }
    ],
    "inline": true,
    "summary": "Real time conversion",
    "introduced": "2,0,0",
    "accepts_block": false,
    "signature": {
      "t": null
    },
    "hiden": false
  },
  "stop": {
    "hiden": false,
    "accepts_block": false,
    "returns": null,
    "summary": "Stop current thread or run",
    "introduced": "2,5,0"
  },
  "at": {
    "args": [
      {
        "times": ":list"
      },
      {
        "params": ":list"
      }
    ],
    "requires_block": true,
    "summary": "Asynchronous Time. Run a block at the given time(s)",
    "introduced": "2,1,0",
    "accepts_block": true,
    "signature": {
      "times": 0,
      "params": "nil",
      "&block": null
    },
    "async_block": true,
    "hiden": false
  },
  "use_random_seed": {
    "args": [
      {
        "seed": ":number"
      }
    ],
    "summary": "Set random seed generator to known seed",
    "introduced": "2,0,0",
    "accepts_block": false,
    "signature": {
      "seed": null,
      "&block": null
    },
    "hiden": false
  },
  "load_buffer": {
    "args": [
      {
        "path": ":string"
      }
    ],
    "summary": "Load the contents of a file to the current buffer",
    "introduced": "2,10,0",
    "accepts_block": false,
    "signature": {
      "path": null
    },
    "hiden": false
  },
  "spark": {
    "hiden": true,
    "introduced": "2,5,0",
    "accepts_block": false,
    "summary": "Print a string representing a list of numeric values as a spark graph/bar chart",
    "signature": {
      "*values": null
    }
  },
  "live_loop": {
    "intro_fn": true,
    "args": [
      {
        "name": ":symbol"
      }
    ],
    "opts": {
      "sync": ":foo",
      "delay": 0,
      "seed": 0,
      "init": "",
      "auto_cue": true,
      "sync_bpm": ":foo"
    },
    "summary": "A loop for live coding",
    "introduced": "2,1,0",
    "accepts_block": true,
    "signature": {
      "name": "nil",
      "*args": null,
      "&block": null
    },
    "async_block": true,
    "hiden": false,
    "requires_block": true
  },
  "rand_look": {
    "args": [
      {
        "max": ":number_or_range"
      }
    ],
    "inline": true,
    "summary": "Generate a random number without consuming a rand",
    "introduced": "2,11,0",
    "accepts_block": false,
    "signature": {
      "*args": null
    },
    "hiden": false
  },
  "block_slept?": {
    "args": [],
    "requires_block": true,
    "summary": "Determine if block contains sleep time",
    "introduced": "2,9,0",
    "accepts_block": true,
    "signature": {
      "&block": null
    },
    "async_block": false,
    "hiden": false
  },
  "knit": {
    "args": [
      {
        "value": ":anything"
      },
      {
        "count": ":number"
      }
    ],
    "inline": true,
    "returns": ":ring",
    "summary": "Knit a sequence of repeated values",
    "introduced": "2,2,0",
    "accepts_block": false,
    "signature": {
      "*args": null
    },
    "hiden": false
  },
  "tick_reset_all": {
    "args": [
      {
        "value": ":number"
      }
    ],
    "returns": null,
    "summary": "Reset all ticks",
    "alt_args": [
      {
        "key": ":symbol"
      },
      {
        "value": ":number"
      }
    ],
    "accepts_block": false,
    "introduced": "2,6,0",
    "hiden": false
  },
  "with_cue_logging": {
    "args": [
      {
        "true_or_false": ":boolean"
      }
    ],
    "requires_block": true,
    "summary": "Block-level enable and disable cue logging",
    "introduced": "2,6,0",
    "accepts_block": true,
    "signature": {
      "&block": null,
      "v": null
    },
    "hiden": false
  },
  "current_beat_duration": {
    "accepts_block": false,
    "hiden": true,
    "summary": "Duration of current beat",
    "introduced": "2,6,0"
  },
  "line": {
    "inline": true,
    "args": [
      {
        "start": ":number"
      },
      {
        "finish": ":number"
      }
    ],
    "memoize": true,
    "returns": ":ring",
    "summary": "Create a ring buffer representing a straight line",
    "introduced": "2,5,0",
    "accepts_block": false,
    "signature": {
      "*args": null,
      "start": null,
      "finish": null
    },
    "hiden": false,
    "opts": {
      "inclusive": false,
      "steps": 1
    }
  },
  "define": {
    "intro_fn": true,
    "args": [
      {
        "name": ":symbol"
      }
    ],
    "requires_block": true,
    "summary": "Define a new function",
    "introduced": "2,0,0",
    "accepts_block": true,
    "signature": {
      "name": null,
      "&block": null
    },
    "hiden": false
  },
  "ring": {
    "args": [
      {
        "list": ":array"
      }
    ],
    "inline": true,
    "returns": ":ring",
    "summary": "Create a ring buffer",
    "introduced": "2,2,0",
    "accepts_block": false,
    "signature": {
      "*args": null
    },
    "hiden": false
  },
  "spread": {
    "args": [
      {
        "num_accents": ":number"
      },
      {
        "size": ":number"
      }
    ],
    "inline": true,
    "returns": ":ring",
    "summary": "Euclidean distribution for beats",
    "introduced": "2,4,0",
    "accepts_block": false,
    "signature": {
      "*args": null,
      "num_accents": null,
      "size": null
    },
    "hiden": false,
    "opts": {
      "rotate": false
    }
  },
  "spark_graph": {
    "accepts_block": false,
    "introduced": "2,5,0",
    "hiden": true,
    "summary": "Returns a string representing a list of numeric values as a spark graph/bar chart",
    "signature": {
      "*values": null
    }
  },
  "version": {
    "accepts_block": false,
    "hiden": true,
    "summary": "Get current version information",
    "introduced": "2,0,0"
  },
  "in_thread": {
    "hiden": false,
    "opts": {
      "name": ":foo",
      "sync": ":foo",
      "delay": 0,
      "sync_bpm": ":foo"
    },
    "summary": "Run code block at the same time",
    "introduced": "2,0,0",
    "accepts_block": true,
    "signature": {
      "*opts": null,
      "&block": null
    },
    "async_block": true,
    "requires_block": true
  },
  "assert": {
    "signature": {
      "arg": null,
      "msg": "nil"
    },
    "args": [
      {
        "arg": ":anything"
      }
    ],
    "summary": "Ensure arg is valid",
    "alt_args": [
      {
        "arg": ":anything"
      },
      {
        "error_msg": ":string"
      }
    ],
    "accepts_block": false,
    "introduced": "2,8,0",
    "hiden": true
  },
  "dec": {
    "args": [
      {
        "n": ":number"
      }
    ],
    "opts": {},
    "summary": "Decrement",
    "introduced": "2, 1, 0",
    "accepts_block": false,
    "signature": {
      "n": null
    },
    "hiden": true
  },
  "tick_reset": {
    "signature": {
      "*args": null
    },
    "hiden": false,
    "returns": ":number",
    "summary": "Reset tick to 0",
    "alt_args": [
      {
        "key": ":symbol"
      }
    ],
    "accepts_block": false,
    "introduced": "2,6,0"
  },
  "print": {
    "intro_fn": true,
    "args": [
      {
        "output": ":anything"
      }
    ],
    "summary": "Display a message in the output pane",
    "introduced": "2,0,0",
    "accepts_block": false,
    "signature": {
      "*msgs": null
    },
    "hiden": true
  },
  "vt": {
    "accepts_block": false,
    "inline": true,
    "hiden": false,
    "summary": "Get virtual time",
    "introduced": "2,1,0"
  },
  "use_osc": {
    "hiden": true,
    "signature": {
      "port": "nil",
      "host_or_port": null
    }
  },
  "ndefine": {
    "args": [
      {
        "name": ":symbol"
      }
    ],
    "requires_block": true,
    "summary": "Define a new function",
    "introduced": "2,1,0",
    "accepts_block": true,
    "signature": {
      "name": null,
      "&block": null
    },
    "hiden": true
  },
  "shuffle": {
    "alt_args": [
      {
        "list": ":array"
      }
    ],
    "args": [],
    "inline": true,
    "summary": "Randomise order of a list",
    "introduced": "2,1,0",
    "accepts_block": false,
    "signature": {
      "list": null
    },
    "hiden": false
  },
  "current_random_seed": {
    "intro_fn": true,
    "accepts_block": false,
    "hiden": true,
    "summary": "Get current random seed",
    "introduced": "2,10,0"
  },
  "rand_reset": {
    "hiden": false,
    "args": [],
    "accepts_block": false,
    "summary": "Reset rand generator to last seed",
    "introduced": "2,7,0"
  },
  "look": {
    "signature": {
      "*args": null
    },
    "hiden": false,
    "inline": true,
    "returns": ":number",
    "summary": "Obtain value of a tick",
    "alt_args": [
      {
        "list": ":array"
      },
      {
        "key": ":symbol"
      }
    ],
    "accepts_block": false,
    "introduced": "2,6,0",
    "opts": {
      "offset": 0
    }
  },
  "run_code": {
    "args": [
      {
        "code": ":string"
      }
    ],
    "returns": null,
    "summary": "Evaluate the code passed as a String as a new Run",
    "introduced": "2,11,0",
    "accepts_block": false,
    "signature": {
      "code": null
    },
    "hiden": false
  },
  "time_shift": {
    "args": [
      {
        "delta_time": ":number"
      }
    ],
    "returns": null,
    "summary": "Slide time forwards or backwards for the given block",
    "introduced": "2,11,0",
    "accepts_block": true,
    "signature": {
      "&blk": null,
      "delta": null
    },
    "hiden": false,
    "requires_block": true
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
    "inline": true,
    "summary": "Quantise a value to resolution",
    "introduced": "2,1,0",
    "accepts_block": false,
    "signature": {
      "n": null,
      "step": null
    },
    "hiden": false
  },
  "on": {
    "args": [
      {
        "condition": ":truthy"
      }
    ],
    "returns": null,
    "summary": "Optionally evaluate block",
    "introduced": "2,10,0",
    "accepts_block": true,
    "signature": {
      "condition": null,
      "&blk": null
    },
    "hiden": false,
    "requires_block": true
  },
  "rand_i_look": {
    "args": [
      {
        "max": ":number_or_range"
      }
    ],
    "inline": true,
    "summary": "Generate a random whole number without consuming a rand",
    "introduced": "2,11,0",
    "accepts_block": false,
    "signature": {
      "*args": null
    },
    "hiden": false
  },
  "run_file": {
    "args": [
      {
        "filename": ":path"
      }
    ],
    "returns": null,
    "summary": "Evaluate the contents of the file as a new Run",
    "introduced": "2,11,0",
    "accepts_block": false,
    "signature": {
      "path": null
    },
    "hiden": false
  },
  "wait": {
    "args": [
      {
        "beats": ":number"
      }
    ],
    "summary": "Wait for duration",
    "introduced": "2,0,0",
    "advances_time": true,
    "accepts_block": false,
    "signature": {
      "time": null
    },
    "hiden": true
  },
  "choose": {
    "alt_args": [
      {
        "list": ":array"
      }
    ],
    "args": [],
    "inline": true,
    "summary": "Random list selection",
    "introduced": "2,0,0",
    "accepts_block": false,
    "signature": {
      "args": null
    },
    "hiden": false
  },
  "range": {
    "inline": true,
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
    "memoize": true,
    "returns": ":ring",
    "summary": "Create a ring buffer with the specified start, finish and step size",
    "introduced": "2,2,0",
    "accepts_block": false,
    "signature": {
      "*args": null,
      "start": null,
      "finish": null
    },
    "hiden": false,
    "opts": {
      "inclusive": false,
      "step": 1
    }
  },
  "sync": {
    "args": [
      {
        "cue_id": ":symbol"
      }
    ],
    "opts": {
      "bpm_sync": false
    },
    "summary": "Sync with other threads",
    "introduced": "2,0,0",
    "advances_time": true,
    "accepts_block": false,
    "signature": {
      "cue_ids": null,
      "opts": "{}"
    },
    "hiden": false
  },
  "bools": {
    "args": [
      {
        "list": ":array"
      }
    ],
    "inline": true,
    "returns": ":ring",
    "summary": "Create a ring of boolean values",
    "introduced": "2,2,0",
    "accepts_block": false,
    "signature": {
      "*args": null
    },
    "hiden": false
  },
  "cue": {
    "args": [
      {
        "cue_id": ":symbol"
      }
    ],
    "opts": {
      "key": "foo: 64",
      "another_key": "foo: 64",
      "your_key": ":bar"
    },
    "summary": "Cue other threads",
    "introduced": "2,0,0",
    "accepts_block": false,
    "signature": {
      "cue_id": null,
      "*opts": null
    },
    "hiden": false
  },
  "beat": {
    "hiden": true,
    "args": [],
    "accepts_block": false,
    "summary": "Get current beat",
    "introduced": "2,10,0"
  },
  "with_random_seed": {
    "args": [
      {
        "seed": ":number"
      }
    ],
    "requires_block": true,
    "summary": "Specify random seed for code block",
    "introduced": "2,0,0",
    "accepts_block": true,
    "signature": {
      "seed": null,
      "&block": null
    },
    "hiden": false
  },
  "rand_back": {
    "args": [
      {
        "amount": ":number"
      }
    ],
    "summary": "Roll back random generator",
    "introduced": "2,7,0",
    "accepts_block": false,
    "signature": {
      "amount": 1
    },
    "hiden": false
  },
  "assert_equal": {
    "signature": {
      "arg1": null,
      "arg2": null,
      "msg": "nil"
    },
    "args": [
      {
        "arg1": ":anything"
      },
      {
        "arg2": ":anything"
      }
    ],
    "summary": "Ensure args are equal",
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
    "introduced": "2,8,0",
    "hiden": true
  },
  "defonce": {
    "args": [
      {
        "name": ":symbol"
      }
    ],
    "opts": {
      "override": false
    },
    "summary": "Define a named value only once",
    "introduced": "2,0,0",
    "accepts_block": true,
    "signature": {
      "name": null,
      "*opts": null,
      "&block": null
    },
    "hiden": false,
    "requires_block": true
  },
  "rand": {
    "intro_fn": true,
    "args": [
      {
        "max": ":number_or_range"
      }
    ],
    "inline": true,
    "summary": "Generate a random float below a value",
    "introduced": "2,0,0",
    "accepts_block": false,
    "signature": {
      "max": 1
    },
    "hiden": false
  },
  "reset": {
    "args": [],
    "returns": null,
    "summary": "Reset all thread locals",
    "introduced": "2,11,0",
    "accepts_block": false,
    "hiden": false
  },
  "block_duration": {
    "args": [],
    "requires_block": true,
    "summary": "Return block duration",
    "introduced": "2,9,0",
    "accepts_block": true,
    "signature": {
      "&block": null
    },
    "async_block": false,
    "hiden": false
  },
  "current_bpm": {
    "accepts_block": false,
    "hiden": true,
    "summary": "Get current tempo",
    "introduced": "2,0,0"
  },
  "density": {
    "args": [
      {
        "d": ":density"
      }
    ],
    "requires_block": true,
    "summary": "Squash and repeat time",
    "introduced": "2,3,0",
    "accepts_block": true,
    "signature": {
      "d": null,
      "&block": null
    },
    "async_block": true,
    "hiden": false
  },
  "stretch": {
    "alt_args": [
      {
        "list": ":array"
      }
    ],
    "args": [
      {
        "count": ":int"
      }
    ],
    "inline": true,
    "returns": ":ring",
    "summary": "Stretch a sequence of values",
    "introduced": "2,6,0",
    "accepts_block": false,
    "signature": {
      "*args": null
    },
    "hiden": false
  },
  "ramp": {
    "args": [
      {
        "list": ":array"
      }
    ],
    "inline": true,
    "returns": ":ramp",
    "summary": "Create a ramp vector",
    "introduced": "2,6,0",
    "accepts_block": false,
    "signature": {
      "*args": null
    },
    "hiden": false
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
    "summary": "Factor test",
    "introduced": "2,1,0",
    "accepts_block": false,
    "signature": {
      "factor": null,
      "val": null
    },
    "hiden": false
  },
  "rdist": {
    "signature": {
      "centre": 0,
      "*opts": null,
      "width": null
    },
    "args": [
      {
        "width": ":number"
      }
    ],
    "inline": true,
    "opts": {
      "step": 1
    },
    "summary": "Random number in centred distribution",
    "alt_args": [
      {
        "width": ":number"
      },
      {
        "centre": ":number"
      }
    ],
    "accepts_block": false,
    "introduced": "2,3,0",
    "hiden": false
  },
  "rand_i": {
    "args": [
      {
        "max": ":number_or_range"
      }
    ],
    "inline": true,
    "summary": "Generate a random whole number below a value (exclusive)",
    "introduced": "2,0,0",
    "accepts_block": false,
    "signature": {
      "max": 2
    },
    "hiden": false
  },
  "with_bpm_mul": {
    "args": [
      {
        "mul": ":number"
      }
    ],
    "requires_block": true,
    "summary": "Set new tempo as a multiple of current tempo for block",
    "introduced": "2,3,0",
    "accepts_block": true,
    "signature": {
      "mul": null,
      "&block": null
    },
    "hiden": false
  },
  "vector": {
    "args": [
      {
        "list": ":array"
      }
    ],
    "inline": true,
    "returns": ":vector",
    "summary": "Create a vector",
    "introduced": "2,6,0",
    "accepts_block": false,
    "signature": {
      "*args": null
    },
    "hiden": false
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
    "inline": true,
    "summary": "Generate a random whole number between two points inclusively",
    "introduced": "2,0,0",
    "accepts_block": false,
    "signature": {
      "max": null,
      "min": null
    },
    "hiden": false
  },
  "sync_bpm": {
    "args": [
      {
        "cue_id": ":symbol"
      }
    ],
    "opts": {},
    "summary": "Sync and inherit BPM from other threads ",
    "introduced": "2,10,0",
    "advances_time": true,
    "accepts_block": false,
    "signature": {
      "cue_ids": null,
      "opts": "{}"
    },
    "hiden": false
  },
  "inc": {
    "args": [
      {
        "n": ":number"
      }
    ],
    "opts": {},
    "summary": "Increment",
    "introduced": "2, 1, 0",
    "accepts_block": false,
    "signature": {
      "n": null
    },
    "hiden": true
  },
  "use_bpm": {
    "intro_fn": true,
    "args": [
      {
        "bpm": ":number"
      }
    ],
    "summary": "Set the tempo",
    "introduced": "2,0,0",
    "accepts_block": false,
    "signature": {
      "bpm": null,
      "&block": null
    },
    "hiden": false
  },
  "puts": {
    "intro_fn": true,
    "args": [
      {
        "output": ":anything"
      }
    ],
    "summary": "Display a message in the output pane",
    "introduced": "2,0,0",
    "accepts_block": false,
    "signature": {
      "*msgs": null
    },
    "hiden": true
  },
  "rand_skip": {
    "args": [
      {
        "amount": ":number"
      }
    ],
    "summary": "Jump forward random generator",
    "introduced": "2,7,0",
    "accepts_block": false,
    "signature": {
      "amount": 1
    },
    "hiden": false
  },
  "tick_set": {
    "signature": {
      "*args": null
    },
    "args": [
      {
        "value": ":number"
      }
    ],
    "returns": ":number",
    "summary": "Set tick to a specific value",
    "alt_args": [
      {
        "key": ":symbol"
      },
      {
        "value": ":number"
      }
    ],
    "accepts_block": false,
    "introduced": "2,6,0",
    "hiden": false
  },
  "with_tempo": {
    "hiden": true,
    "signature": {
      "*args": null,
      "&block": null
    }
  },
  "tick": {
    "signature": {
      "*args": null
    },
    "args": [],
    "inline": true,
    "returns": ":number",
    "summary": "Increment a tick and return value",
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
    "accepts_block": false,
    "introduced": "2,6,0",
    "hiden": false,
    "opts": {
      "offset": 0,
      "step": 1
    }
  },
  "with_bpm": {
    "args": [
      {
        "bpm": ":number"
      }
    ],
    "requires_block": true,
    "summary": "Set the tempo for the code block",
    "introduced": "2,0,0",
    "accepts_block": true,
    "signature": {
      "bpm": null,
      "&block": null
    },
    "hiden": false
  },
  "use_bpm_mul": {
    "args": [
      {
        "mul": ":number"
      }
    ],
    "summary": "Set new tempo as a multiple of current tempo",
    "introduced": "2,3,0",
    "accepts_block": false,
    "signature": {
      "mul": null,
      "&block": null
    },
    "hiden": false
  }
}

#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/

lang_sound = {
  "truthy?": {
    "hiden": false,
    "signature": {
      "val": null
    }
  },
  "set_mixer_standard_stereo!": {
    "hiden": false
  },
  "use_debug": {
    "args": [
      {
        "true_or_false": ":boolean"
      }
    ],
    "summary": "Enable and disable debug",
    "introduced": "2,0,0",
    "accepts_block": false,
    "signature": {
      "&block": null,
      "v": null
    },
    "hiden": false
  },
  "use_synth_defaults": {
    "hiden": false,
    "opts": {},
    "summary": "Use new synth defaults",
    "introduced": "2,0,0",
    "accepts_block": false,
    "signature": {
      "*args": null,
      "&block": null
    }
  },
  "recording_save": {
    "args": [
      {
        "path": ":string"
      }
    ],
    "summary": "Save recording",
    "introduced": "2,0,0",
    "accepts_block": false,
    "signature": {
      "filename": null
    },
    "hiden": true
  },
  "set_volume!": {
    "args": [
      {
        "vol": ":number"
      }
    ],
    "modifies_env": true,
    "summary": "Set Volume globally",
    "introduced": "2,0,0",
    "accepts_block": false,
    "signature": {
      "vol": null
    },
    "hiden": false
  },
  "use_merged_synth_defaults": {
    "hiden": false,
    "opts": {},
    "summary": "Merge synth defaults",
    "introduced": "2,0,0",
    "accepts_block": false,
    "signature": {
      "*args": null,
      "&block": null
    }
  },
  "chord": {
    "intro_fn": true,
    "args": [
      {
        "tonic": ":symbol"
      },
      {
        "name": ":symbol"
      }
    ],
    "memoize": true,
    "returns": ":ring",
    "summary": "Create chord",
    "introduced": "2,0,0",
    "inline": true,
    "accepts_block": false,
    "signature": {
      "*opts": null,
      "tonic_or_name": null
    },
    "hiden": false,
    "opts": {
      "invert": 0,
      "num_octaves": 1
    }
  },
  "use_timing_warnings": {
    "hiden": true,
    "signature": {
      "&block": null,
      "v": null
    }
  },
  "use_sample_defaults": {
    "hiden": false,
    "opts": {},
    "summary": "Use new sample defaults",
    "introduced": "2,5,0",
    "accepts_block": false,
    "signature": {
      "*args": null,
      "&block": null
    }
  },
  "with_afx": {
    "hiden": true,
    "signature": {
      "*args": null,
      "&block": null,
      "fx_name": null
    }
  },
  "pitch_to_ratio": {
    "args": [
      {
        "pitch": ":midi_number"
      }
    ],
    "inline": true,
    "summary": "relative MIDI pitch to frequency ratio",
    "introduced": "2,5,0",
    "accepts_block": false,
    "signature": {
      "m": null
    },
    "hiden": false
  },
  "chord_names": {
    "hiden": true,
    "accepts_block": false,
    "memoize": true,
    "summary": "All chord names",
    "introduced": "2,6,0"
  },
  "with_timing_warnings": {
    "hiden": true,
    "signature": {
      "&block": null,
      "v": null
    }
  },
  "with_sample_defaults": {
    "hiden": false,
    "opts": {},
    "summary": "Block-level use new sample defaults",
    "introduced": "2,5,0",
    "accepts_block": true,
    "signature": {
      "*args": null,
      "&block": null
    },
    "requires_block": true
  },
  "set_control_delta!": {
    "args": [
      {
        "time": ":number"
      }
    ],
    "modifies_env": true,
    "summary": "Set control delta globally",
    "introduced": "2,1,0",
    "accepts_block": false,
    "signature": {
      "t": null
    },
    "hiden": false
  },
  "with_timing_guarantees": {
    "args": [
      {
        "bool": ":true_or_false"
      }
    ],
    "requires_block": true,
    "summary": "Block-scoped inhibition of synth triggers if too late",
    "introduced": "2,10,0",
    "accepts_block": true,
    "signature": {
      "&block": null,
      "v": null
    },
    "hiden": false
  },
  "use_cent_tuning": {
    "intro_fn": true,
    "args": [
      {
        "cent_shift": ":number"
      }
    ],
    "summary": "Cent tuning",
    "introduced": "2,9,0",
    "accepts_block": false,
    "signature": {
      "shift": null,
      "&block": null
    },
    "hiden": false
  },
  "play": {
    "intro_fn": true,
    "args": [
      {
        "note": ":symbol_or_number"
      }
    ],
    "opts": {
      "decay_level": 1,
      "sustain": 1,
      "env_curve": 1,
      "release": 0,
      "decay": 0,
      "pitch": 0,
      "slide": 0,
      "amp_slide": 1,
      "sustain_level": 1,
      "pan_slide": 1,
      "attack_level": 1,
      "amp": 1,
      "on": 1,
      "attack": 0,
      "pan": 0
    },
    "summary": "Play current synth",
    "introduced": "2,0,0",
    "accepts_block": true,
    "signature": {
      "*args": null,
      "n": null,
      "&blk": null
    },
    "async_block": true,
    "hiden": false,
    "requires_block": false
  },
  "use_external_synths": {
    "hiden": true,
    "signature": {
      "&block": null,
      "v": null
    }
  },
  "status": {
    "accepts_block": false,
    "hiden": true,
    "summary": "Get server status",
    "introduced": "2,0,0"
  },
  "use_arg_checks": {
    "args": [
      {
        "true_or_false": ":boolean"
      }
    ],
    "summary": "Enable and disable arg checks",
    "introduced": "2,0,0",
    "accepts_block": false,
    "signature": {
      "&block": null,
      "v": null
    },
    "hiden": false
  },
  "use_merged_sample_defaults": {
    "hiden": false,
    "opts": {},
    "summary": "Merge new sample defaults",
    "introduced": "2,9,0",
    "accepts_block": false,
    "signature": {
      "*args": null,
      "&block": null
    }
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
    "inline": true,
    "summary": "Convert a degree into a note",
    "introduced": "2,1,0",
    "accepts_block": false,
    "signature": {
      "tonic": null,
      "degree": null,
      "scale": null
    },
    "hiden": false
  },
  "chord_invert": {
    "args": [
      {
        "notes": ":list"
      },
      {
        "shift": ":number"
      }
    ],
    "inline": true,
    "returns": ":ring",
    "summary": "Chord inversion",
    "introduced": "2,6,0",
    "accepts_block": false,
    "signature": {
      "shift": null,
      "notes": null
    },
    "hiden": false
  },
  "kill": {
    "args": [
      {
        "node": ":synth_node"
      }
    ],
    "opts": {},
    "summary": "Kill synth",
    "introduced": "2,0,0",
    "accepts_block": false,
    "signature": {
      "node": null
    },
    "hiden": false
  },
  "note": {
    "args": [
      {
        "note": ":symbol_or_number"
      }
    ],
    "inline": true,
    "opts": {
      "octave": 4
    },
    "summary": "Describe note",
    "introduced": "2,0,0",
    "accepts_block": false,
    "signature": {
      "*args": null,
      "n": null
    },
    "hiden": false
  },
  "play_chord": {
    "args": [
      {
        "notes": ":list"
      }
    ],
    "opts": {
      "decay_level": 1,
      "sustain": 1,
      "env_curve": 1,
      "release": 0,
      "decay": 0,
      "pitch": 0,
      "slide": 0,
      "amp_slide": 1,
      "sustain_level": 1,
      "pan_slide": 1,
      "attack_level": 1,
      "amp": 1,
      "on": 1,
      "attack": 0,
      "pan": 0
    },
    "summary": "Play notes simultaneously",
    "introduced": "2,0,0",
    "accepts_block": false,
    "signature": {
      "*args": null,
      "notes": null
    },
    "hiden": false
  },
  "note_info": {
    "args": [
      {
        "note": ":symbol_or_number"
      }
    ],
    "opts": {
      "octave": 4
    },
    "summary": "Get note info",
    "introduced": "2,0,0",
    "accepts_block": false,
    "signature": {
      "*args": null,
      "n": null
    },
    "hiden": true
  },
  "sample_loaded?": {
    "args": [
      {
        "path": ":string"
      }
    ],
    "summary": "Test if sample was pre-loaded",
    "introduced": "2,2,0",
    "accepts_block": false,
    "signature": {
      "*args": null
    },
    "hiden": false
  },
  "scale_names": {
    "hiden": true,
    "accepts_block": false,
    "memoize": true,
    "summary": "All scale names",
    "introduced": "2,6,0"
  },
  "sample_free_all": {
    "args": [],
    "returns": null,
    "summary": "Free all loaded samples on the synth server",
    "introduced": "2,9,0",
    "accepts_block": false,
    "hiden": false
  },
  "use_sample_bpm": {
    "args": [
      {
        "string_or_number": ":sample_name_or_duration"
      }
    ],
    "opts": {
      "num_beats": 1
    },
    "summary": "Sample-duration-based bpm modification",
    "introduced": "2,1,0",
    "accepts_block": false,
    "signature": {
      "*args": null,
      "sample_name": null
    },
    "hiden": false
  },
  "use_transpose": {
    "intro_fn": true,
    "args": [
      {
        "note_shift": ":number"
      }
    ],
    "summary": "Note transposition",
    "introduced": "2,0,0",
    "accepts_block": false,
    "signature": {
      "shift": null,
      "&block": null
    },
    "hiden": false
  },
  "with_synth_defaults": {
    "hiden": false,
    "opts": {},
    "summary": "Block-level use new synth defaults",
    "introduced": "2,0,0",
    "accepts_block": true,
    "signature": {
      "*args": null,
      "&block": null
    },
    "requires_block": true
  },
  "with_synth": {
    "args": [
      {
        "synth_name": ":symbol"
      }
    ],
    "requires_block": true,
    "summary": "Block-level synth switching",
    "introduced": "2,0,0",
    "accepts_block": true,
    "signature": {
      "synth_name": null,
      "*args": null,
      "&block": null
    },
    "hiden": false
  },
  "sample_groups": {
    "hiden": true,
    "accepts_block": false,
    "memoize": true,
    "summary": "Get all sample groups",
    "introduced": "2,0,0"
  },
  "sample_info": {
    "args": [
      {
        "path": ":string"
      }
    ],
    "summary": "Get sample information",
    "introduced": "2,0,0",
    "accepts_block": false,
    "signature": {
      "*args": null
    },
    "hiden": true
  },
  "set_mixer_stereo_mode!": {
    "hiden": false
  },
  "set_mixer_invert_stereo!": {
    "hiden": false
  },
  "with_merged_sample_defaults": {
    "hiden": false,
    "opts": {},
    "summary": "Block-level use merged sample defaults",
    "introduced": "2,9,0",
    "accepts_block": true,
    "signature": {
      "*args": null,
      "&block": null
    },
    "requires_block": true
  },
  "sample_paths": {
    "args": [
      {
        "pre_args": ":source_and_filter_types"
      }
    ],
    "returns": ":ring",
    "summary": "Sample Pack Filter Resolution",
    "introduced": "2,10,0",
    "accepts_block": false,
    "signature": {
      "*args": null
    },
    "hiden": true
  },
  "use_fx": {
    "hiden": true,
    "signature": {
      "*args": null,
      "&block": null
    }
  },
  "current_transpose": {
    "accepts_block": false,
    "hiden": true,
    "summary": "Get current transposition",
    "introduced": "2,0,0"
  },
  "set_cent_tuning!": {
    "intro_fn": false,
    "args": [
      {
        "cent_shift": ":number"
      }
    ],
    "summary": "Global Cent tuning",
    "introduced": "2,10,0",
    "accepts_block": false,
    "signature": {
      "shift": null
    },
    "hiden": false
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
    "requires_block": true,
    "summary": "Block-level tuning modification",
    "introduced": "2,6,0",
    "accepts_block": true,
    "signature": {
      "tuning": null,
      "fundamental_note": ":c",
      "&block": null
    },
    "hiden": false
  },
  "load_samples": {
    "args": [
      {
        "paths": ":list"
      }
    ],
    "summary": "Pre-load all matching samples",
    "introduced": "2,0,0",
    "accepts_block": false,
    "signature": {
      "*args": null
    },
    "hiden": false
  },
  "sample_free": {
    "args": [
      {
        "path": ":string"
      }
    ],
    "returns": null,
    "summary": "Free a sample on the synth server",
    "introduced": "2,9,0",
    "accepts_block": false,
    "signature": {
      "*paths": null
    },
    "hiden": false
  },
  "fx_names": {
    "hiden": true,
    "accepts_block": false,
    "memoize": true,
    "summary": "Get all FX names",
    "introduced": "2,10,0"
  },
  "sample_duration": {
    "args": [
      {
        "path": ":string"
      }
    ],
    "opts": {
      "decay": 0,
      "finish": 1,
      "release": 0,
      "beat_stretch": 1,
      "sustain": 1,
      "rpitch": 0,
      "start": 0,
      "attack": 0,
      "pitch_stretch": 1,
      "rate": 1
    },
    "summary": "Get duration of sample in beats",
    "introduced": "2,0,0",
    "accepts_block": false,
    "signature": {
      "*args": null
    },
    "hiden": true
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
    "summary": "Use alternative tuning systems",
    "introduced": "2,6,0",
    "accepts_block": false,
    "signature": {
      "tuning": null,
      "fundamental_note": ":c",
      "&block": null
    },
    "hiden": false
  },
  "recording_start": {
    "accepts_block": false,
    "hiden": true,
    "summary": "Start recording",
    "introduced": "2,0,0"
  },
  "sample_split_filts_and_opts": {
    "hiden": true,
    "signature": {
      "args": null
    }
  },
  "load_sample_at_path": {
    "hiden": false,
    "signature": {
      "path": null
    }
  },
  "current_cent_tuning": {
    "accepts_block": false,
    "hiden": true,
    "summary": "Get current cent shift",
    "introduced": "2,9,0"
  },
  "set_mixer_control!": {
    "hiden": false,
    "opts": {
      "limiter_bypass": 0,
      "hpf_bypass": 0,
      "amp": 1,
      "leak_dc_bypass": 0,
      "lpf_bypass": 0,
      "pre_amp": 1,
      "lpf": 131,
      "hpf": 0
    },
    "summary": "Control master mixer",
    "introduced": "2,7,0",
    "accepts_block": false,
    "signature": {
      "opts": null
    }
  },
  "scale": {
    "intro_fn": true,
    "args": [
      {
        "tonic": ":symbol"
      },
      {
        "name": ":symbol"
      }
    ],
    "memoize": true,
    "returns": ":ring",
    "summary": "Create scale",
    "introduced": "2,0,0",
    "inline": true,
    "accepts_block": false,
    "signature": {
      "*opts": null,
      "tonic_or_name": null
    },
    "hiden": false,
    "opts": {
      "num_octaves": 1
    }
  },
  "sample_names": {
    "args": [
      {
        "group": ":symbol"
      }
    ],
    "returns": ":ring",
    "summary": "Get sample names",
    "introduced": "2,0,0",
    "accepts_block": false,
    "signature": {
      "group": null
    },
    "hiden": true,
    "memoize": true
  },
  "use_octave": {
    "intro_fn": true,
    "args": [
      {
        "octave_shift": ":number"
      }
    ],
    "summary": "Note octave transposition",
    "introduced": "2,9,0",
    "accepts_block": false,
    "signature": {
      "shift": null,
      "&block": null
    },
    "hiden": false
  },
  "recording_stop": {
    "accepts_block": false,
    "hiden": true,
    "summary": "Stop recording",
    "introduced": "2,0,0"
  },
  "load_sample": {
    "args": [
      {
        "path": ":string"
      }
    ],
    "summary": "Pre-load first matching sample",
    "introduced": "2,0,0",
    "accepts_block": false,
    "signature": {
      "*args": null
    },
    "hiden": false
  },
  "invert_chord": {
    "hiden": true,
    "signature": {
      "*args": null
    }
  },
  "recording_delete": {
    "accepts_block": false,
    "hiden": true
  },
  "sample": {
    "intro_fn": true,
    "args": [
      {
        "name_or_path": ":symbol_or_string"
      }
    ],
    "opts": {
      "hpf_sustain": 0,
      "hpf_decay": 0,
      "release": 0,
      "beat_stretch": 1,
      "hpf_env_curve": 1,
      "pitch": 0,
      "slope_above": 1,
      "hpf_max": 200,
      "lpf_release": 0,
      "relax_time": 0,
      "lpf_decay_level": 0,
      "lpf_init_level": 30,
      "hpf_attack_level": 0,
      "hpf_sustain_level": 0,
      "lpf": 131,
      "lpf_min": 30,
      "slope_below": 1,
      "hpf_release": 0,
      "rate": 1,
      "window_size": 0,
      "pitch_stretch": 1,
      "pitch_dis": 0,
      "attack": 0,
      "time_dis": 0,
      "path": "/path/to/file",
      "lpf_decay": 0,
      "start": 0,
      "slide": 0,
      "hpf_attack": 0,
      "hpf_init_level": 130,
      "amp": 1,
      "onset": 0,
      "rpitch": 0,
      "compress": 0,
      "pre_amp": 1,
      "lpf_attack": 0,
      "sustain": 1,
      "lpf_env_curve": 1,
      "lpf_sustain": 0,
      "lpf_sustain_level": 0,
      "hpf_decay_level": 0,
      "threshold": 0,
      "hpf": 0,
      "lpf_attack_level": 0,
      "finish": 1,
      "lpf_release_level": 0,
      "clamp_time": 0,
      "hpf_release_level": 0,
      "pan": 0,
      "norm": 0
    },
    "summary": "Trigger sample",
    "introduced": "2,0,0",
    "accepts_block": true,
    "signature": {
      "*args": null,
      "&blk": null
    },
    "async_block": true,
    "hiden": false,
    "requires_block": false
  },
  "start_amp_monitor": {
    "hiden": true
  },
  "sample_buffer": {
    "args": [
      {
        "path": ":string"
      }
    ],
    "summary": "Get sample data",
    "introduced": "2,0,0",
    "accepts_block": false,
    "signature": {
      "*args": null
    },
    "hiden": true
  },
  "midi_to_hz": {
    "args": [
      {
        "note": ":symbol_or_number"
      }
    ],
    "inline": true,
    "summary": "MIDI to Hz conversion",
    "introduced": "2,0,0",
    "accepts_block": false,
    "signature": {
      "n": null
    },
    "hiden": false
  },
  "with_transpose": {
    "args": [
      {
        "note_shift": ":number"
      }
    ],
    "requires_block": true,
    "summary": "Block-level note transposition",
    "introduced": "2,0,0",
    "accepts_block": true,
    "signature": {
      "shift": null,
      "&block": null
    },
    "hiden": false
  },
  "with_cent_tuning": {
    "args": [
      {
        "cent_shift": ":number"
      }
    ],
    "requires_block": true,
    "summary": "Block-level cent tuning",
    "introduced": "2,9,0",
    "accepts_block": true,
    "signature": {
      "shift": null,
      "&block": null
    },
    "hiden": false
  },
  "note_range": {
    "args": [
      {
        "low_note": ":note"
      },
      {
        "high_note": ":note"
      }
    ],
    "inline": true,
    "returns": ":ring",
    "summary": "Get a range of notes",
    "introduced": "2,6,0",
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
  },
  "use_synth": {
    "intro_fn": true,
    "args": [
      {
        "synth_name": ":symbol"
      }
    ],
    "summary": "Switch current synth",
    "introduced": "2,0,0",
    "accepts_block": false,
    "signature": {
      "synth_name": null,
      "*args": null,
      "&block": null
    },
    "hiden": false
  },
  "midi_notes": {
    "args": [
      {
        "list": ":array"
      }
    ],
    "inline": true,
    "returns": ":ring",
    "summary": "Create a ring buffer of midi note numbers",
    "introduced": "2,7,0",
    "accepts_block": false,
    "signature": {
      "*args": null
    },
    "hiden": false,
    "memoize": true
  },
  "rest?": {
    "args": [
      {
        "note_or_args": ":number_symbol_or_map"
      }
    ],
    "summary": "Determine if note or args is a rest",
    "introduced": "2,1,0",
    "accepts_block": false,
    "signature": {
      "n": null
    },
    "hiden": false
  },
  "current_synth_defaults": {
    "accepts_block": false,
    "hiden": true,
    "summary": "Get current synth defaults",
    "introduced": "2,0,0"
  },
  "with_arg_checks": {
    "args": [
      {
        "true_or_false": ":boolean"
      }
    ],
    "requires_block": true,
    "summary": "Block-level enable and disable arg checks",
    "introduced": "2,0,0",
    "accepts_block": true,
    "signature": {
      "&block": null,
      "v": null
    },
    "hiden": false
  },
  "ratio_to_pitch": {
    "args": [
      {
        "ratio": ":number"
      }
    ],
    "inline": true,
    "summary": "relative frequency ratio to MIDI pitch",
    "introduced": "2,7,0",
    "accepts_block": false,
    "signature": {
      "r": null
    },
    "hiden": false
  },
  "set_sched_ahead_time!": {
    "args": [
      {
        "time": ":number"
      }
    ],
    "modifies_env": true,
    "summary": "Set sched ahead time globally",
    "introduced": "2,0,0",
    "accepts_block": false,
    "signature": {
      "t": null
    },
    "hiden": false
  },
  "chord_degree": {
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
    "inline": true,
    "returns": ":ring",
    "summary": "Construct chords of stacked thirds, based on scale degrees",
    "introduced": "2,1,0",
    "accepts_block": false,
    "signature": {
      "*opts": null,
      "tonic": null,
      "degree": null,
      "number_of_notes": 4,
      "scale": ":major"
    },
    "hiden": false,
    "memoize": true
  },
  "current_synth": {
    "accepts_block": false,
    "hiden": true,
    "summary": "Get current synth",
    "introduced": "2,0,0"
  },
  "control": {
    "args": [
      {
        "node": ":synth_node"
      }
    ],
    "opts": {},
    "summary": "Control running synth",
    "introduced": "2,0,0",
    "accepts_block": false,
    "signature": {
      "*args": null
    },
    "hiden": false
  },
  "set_mixer_mono_mode!": {
    "hiden": false
  },
  "resolve_sample_path": {
    "hiden": true,
    "signature": {
      "filts_and_sources": null
    }
  },
  "current_volume": {
    "accepts_block": false,
    "hiden": true,
    "summary": "Get current volume",
    "introduced": "2,0,0"
  },
  "hz_to_midi": {
    "args": [
      {
        "freq": ":number"
      }
    ],
    "inline": true,
    "summary": "Hz to MIDI conversion",
    "introduced": "2,0,0",
    "accepts_block": false,
    "signature": {
      "freq": null
    },
    "hiden": false
  },
  "current_arg_checks": {
    "accepts_block": false,
    "hiden": true,
    "summary": "Get current arg checking status",
    "introduced": "2,0,0"
  },
  "with_arg_bpm_scaling": {
    "hiden": false,
    "requires_block": true,
    "summary": "Block-level enable and disable BPM scaling",
    "introduced": "2,0,0",
    "accepts_block": true,
    "signature": {
      "bool": null,
      "&block": null
    }
  },
  "should_trigger?": {
    "hiden": false,
    "signature": {
      "args_h": null
    }
  },
  "play_pattern_timed": {
    "args": [
      {
        "notes": ":list"
      },
      {
        "times": ":list_or_number"
      }
    ],
    "opts": {
      "decay_level": 1,
      "sustain": 1,
      "env_curve": 1,
      "release": 0,
      "decay": 0,
      "pitch": 0,
      "slide": 0,
      "amp_slide": 1,
      "sustain_level": 1,
      "pan_slide": 1,
      "attack_level": 1,
      "amp": 1,
      "on": 1,
      "attack": 0,
      "pan": 0
    },
    "summary": "Play pattern of notes with specific times",
    "introduced": "2,0,0",
    "accepts_block": false,
    "signature": {
      "*args": null,
      "times": null,
      "notes": null
    },
    "hiden": false
  },
  "with_octave": {
    "intro_fn": true,
    "args": [
      {
        "octave_shift": ":number"
      }
    ],
    "requires_block": true,
    "summary": "Block level octave transposition",
    "introduced": "2,9,0",
    "accepts_block": true,
    "signature": {
      "shift": null,
      "&block": null
    },
    "hiden": false
  },
  "load_synthdefs": {
    "args": [
      {
        "path": ":string"
      }
    ],
    "summary": "Load external synthdefs",
    "introduced": "2,0,0",
    "accepts_block": false,
    "signature": {
      "path": "synthdef_path"
    },
    "hiden": true
  },
  "with_fx": {
    "intro_fn": true,
    "args": [
      {
        "fx_name": ":symbol"
      }
    ],
    "opts": {
      "kill_delay": 1,
      "reps": 1
    },
    "summary": "Use Studio FX",
    "introduced": "2,0,0",
    "accepts_block": true,
    "signature": {
      "*args": null,
      "&block": null,
      "fx_name": null
    },
    "async_block": true,
    "hiden": false,
    "requires_block": true
  },
  "reset_mixer!": {
    "hiden": false,
    "opts": {},
    "summary": "Reset master mixer",
    "introduced": "2,9,0",
    "accepts_block": false,
    "signature": {
      "": null
    }
  },
  "with_debug": {
    "args": [
      {
        "true_or_false": ":boolean"
      }
    ],
    "requires_block": true,
    "summary": "Block-level enable and disable debug",
    "introduced": "2,0,0",
    "accepts_block": true,
    "signature": {
      "&block": null,
      "v": null
    },
    "hiden": false
  },
  "current_sched_ahead_time": {
    "accepts_block": false,
    "hiden": true,
    "summary": "Get current sched ahead time",
    "introduced": "2,0,0"
  },
  "with_merged_synth_defaults": {
    "hiden": false,
    "opts": {},
    "summary": "Block-level merge synth defaults",
    "introduced": "2,0,0",
    "accepts_block": true,
    "signature": {
      "*args": null,
      "&block": null
    },
    "requires_block": true
  },
  "play_pattern": {
    "args": [
      {
        "notes": ":list"
      }
    ],
    "opts": {},
    "summary": "Play pattern of notes",
    "introduced": "2,0,0",
    "accepts_block": false,
    "signature": {
      "*args": null,
      "notes": null
    },
    "hiden": false
  },
  "current_octave": {
    "accepts_block": false,
    "hiden": true,
    "summary": "Get current octave shift",
    "introduced": "2,9,0"
  },
  "use_timing_guarantees": {
    "args": [
      {
        "bool": ":true_or_false"
      }
    ],
    "requires_block": false,
    "summary": "Inhibit synth triggers if too late",
    "introduced": "2,10,0",
    "accepts_block": false,
    "signature": {
      "&block": null,
      "v": null
    },
    "hiden": false
  },
  "synth_names": {
    "hiden": true,
    "accepts_block": false,
    "memoize": true,
    "summary": "Get all synth names",
    "introduced": "2,9,0"
  },
  "octs": {
    "args": [
      {
        "start": ":note"
      },
      {
        "num_octaves": ":pos_int"
      }
    ],
    "inline": true,
    "returns": ":ring",
    "summary": "Create a ring of octaves",
    "introduced": "2,8,0",
    "accepts_block": false,
    "signature": {
      "start": null,
      "num_octs": 1
    },
    "hiden": false
  },
  "pitch_ratio": {
    "hiden": true,
    "signature": {
      "*args": null
    }
  },
  "resolve_sample_paths": {
    "hiden": true,
    "signature": {
      "filts_and_sources": null
    }
  },
  "current_debug": {
    "accepts_block": false,
    "hiden": true,
    "summary": "Get current debug status",
    "introduced": "2,0,0"
  },
  "all_sample_names": {
    "hiden": true,
    "accepts_block": false,
    "memoize": true,
    "summary": "Get all sample names",
    "introduced": "2,0,0"
  },
  "current_amp": {
    "hiden": true
  },
  "synth": {
    "intro_fn": true,
    "args": [
      {
        "synth_name": ":symbol"
      }
    ],
    "opts": {
      "decay_level": 1,
      "sustain": 1,
      "env_curve": 1,
      "release": 0,
      "decay": 0,
      "pitch": 0,
      "slide": 0,
      "amp_slide": 1,
      "sustain_level": 1,
      "pan_slide": 1,
      "attack_level": 1,
      "amp": 1,
      "on": 1,
      "attack": 0,
      "pan": 0
    },
    "summary": "Trigger specific synth",
    "introduced": "2,0,0",
    "accepts_block": true,
    "signature": {
      "synth_name": null,
      "*args": null,
      "&blk": null
    },
    "async_block": true,
    "hiden": false,
    "requires_block": false
  },
  "current_sample_defaults": {
    "accepts_block": false,
    "hiden": true,
    "summary": "Get current sample defaults",
    "introduced": "2,5,0"
  },
  "use_arg_bpm_scaling": {
    "args": [
      {
        "bool": ":boolean"
      }
    ],
    "summary": "Enable and disable BPM scaling",
    "introduced": "2,0,0",
    "accepts_block": false,
    "signature": {
      "bool": null,
      "&block": null
    },
    "hiden": false
  },
  "with_sample_bpm": {
    "args": [
      {
        "string_or_number": ":sample_name_or_duration"
      }
    ],
    "opts": {
      "num_beats": 1
    },
    "summary": "Block-scoped sample-duration-based bpm modification",
    "introduced": "2,1,0",
    "accepts_block": true,
    "signature": {
      "*args": null,
      "sample_name": null,
      "&block": null
    },
    "hiden": false,
    "requires_block": true
  }
}

sound_args_types_conversion = {}

sound_opts_types_conversion = {}

#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/

synths = {
  "ModPulse": {
    "name": ":mod_pulse",
    "hiden": false,
    "opts": {
      "mod_phase_offset": 0,
      "mod_phase_slide_curve": 0,
      "note_slide_curve": 0,
      "release": 1,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "pulse_width_slide": 0,
      "cutoff_slide_shape": 1,
      "amp_slide_shape": 1,
      "mod_pulse_width": 0.5,
      "mod_range": 5,
      "decay": 0,
      "pulse_width": 0.5,
      "mod_phase": 0.25,
      "amp": 1,
      "mod_pulse_width_slide_shape": 1,
      "attack_level": 1,
      "pan_slide_curve": 0,
      "decay_level": 1,
      "env_curve": 2,
      "mod_phase_slide_shape": 1,
      "mod_invert_wave": 0,
      "sustain": 0,
      "note_slide": 0,
      "pan_slide_shape": 1,
      "mod_pulse_width_slide": 0,
      "mod_range_slide_curve": 0,
      "cutoff_slide": 0,
      "mod_phase_slide": 0,
      "cutoff": 100,
      "mod_range_slide_shape": 1,
      "pan": 0,
      "pulse_width_slide_shape": 1,
      "amp_slide": 0,
      "pulse_width_slide_curve": 0,
      "sustain_level": 1,
      "pan_slide": 0,
      "mod_pulse_width_slide_curve": 0,
      "mod_wave": 1,
      "mod_range_slide": 0,
      "attack": 0,
      "note": 52,
      "note_slide_shape": 1
    },
    "summary": "Modulated Pulse",
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false
  },
  "DTri": {
    "name": ":dtri",
    "hiden": true,
    "opts": {
      "note_slide_curve": 0,
      "release": 1,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "amp_slide_shape": 1,
      "pan_slide_shape": 1,
      "decay": 0,
      "note_slide_shape": 1,
      "amp": 1,
      "attack_level": 1,
      "decay_level": 1,
      "env_curve": 2,
      "detune_slide_curve": 0,
      "sustain": 0,
      "note_slide": 0,
      "pan_slide_curve": 0,
      "detune_slide": 0,
      "cutoff_slide": 0,
      "cutoff": 100,
      "amp_slide": 0,
      "sustain_level": 1,
      "pan_slide": 0,
      "detune": 0.1,
      "detune_slide_shape": 1,
      "attack": 0,
      "note": 52,
      "pan": 0
    },
    "summary": "Detuned Triangle Wave",
    "inherit_base": "DSaw",
    "inherit_arg": true
  },
  "BasicMixer": {
    "name": ":basic_mixer",
    "hiden": true,
    "opts": {
      "amp_slide": 0.1,
      "amp_slide_shape": 1,
      "amp": 1,
      "amp_slide_curve": 0
    },
    "summary": "Basic Mixer",
    "inherit_base": "BaseMixer",
    "inherit_arg": false
  },
  "SynthViolin": {
    "name": ":synth_violin",
    "hiden": false,
    "opts": {
      "note_slide_curve": 0,
      "release": 1,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "amp_slide_shape": 1,
      "decay": 0,
      "amp": 1,
      "vibrato_delay": 0.5,
      "attack_level": 1,
      "pan_slide_curve": 0,
      "decay_level": 1,
      "env_curve": 2,
      "vibrato_rate": 6,
      "vibrato_rate_slide_curve": 0,
      "sustain": 0,
      "vibrato_rate_slide_shape": 1,
      "note_slide": 0,
      "vibrato_depth_slide_curve": 0,
      "pan_slide_shape": 1,
      "cutoff_slide": 0,
      "vibrato_depth_slide_shape": 1,
      "vibrato_onset": 0.1,
      "cutoff": 100,
      "pan": 0,
      "amp_slide": 0,
      "sustain_level": 1,
      "pan_slide": 0,
      "attack": 0,
      "note": 52,
      "note_slide_shape": 1,
      "vibrato_depth": 0.15
    },
    "summary": "Blade Runner style strings",
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false
  },
  "DullBell": {
    "name": ":dull_bell",
    "hiden": false,
    "opts": {
      "decay_level": 1,
      "sustain": 0,
      "note_slide": 0,
      "amp_slide_curve": 0,
      "pan_slide_shape": 1,
      "decay": 0,
      "amp_slide_shape": 1,
      "sustain_level": 1,
      "note_slide_curve": 0,
      "amp_slide": 0,
      "note_slide_shape": 1,
      "amp": 1,
      "attack_level": 1,
      "pan_slide_curve": 0,
      "pan_slide": 0,
      "env_curve": 2,
      "attack": 0,
      "note": 52,
      "pan": 0,
      "release": 1
    },
    "summary": "Dull Bell",
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false
  },
  "FM": {
    "name": ":fm",
    "hiden": false,
    "opts": {
      "note_slide_curve": 0,
      "release": 1,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "depth_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "amp_slide_shape": 1,
      "depth_slide": 0,
      "decay": 0,
      "divisor": 2,
      "amp": 1,
      "attack_level": 1,
      "pan_slide_curve": 0,
      "decay_level": 1,
      "divisor_slide_shape": 1,
      "env_curve": 2,
      "depth_slide_shape": 1,
      "sustain": 0,
      "divisor_slide_curve": 0,
      "note_slide": 0,
      "pan_slide_shape": 1,
      "cutoff_slide": 0,
      "depth": 1,
      "cutoff": 100,
      "pan": 0,
      "amp_slide": 0,
      "divisor_slide": 0,
      "sustain_level": 1,
      "pan_slide": 0,
      "attack": 0,
      "note": 52,
      "note_slide_shape": 1
    },
    "summary": "Basic FM synthesis",
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false
  },
  "SynthInfo": {
    "hiden": true,
    "opts": {},
    "inherit_arg": true,
    "inherit_base": "BaseInfo"
  },
  "Saw": {
    "name": ":saw",
    "hiden": true,
    "opts": {
      "note_slide_curve": 0,
      "release": 1,
      "amp_slide_curve": 0,
      "amp_slide_shape": 1,
      "decay": 0,
      "amp": 1,
      "attack_level": 1,
      "pan_slide_curve": 0,
      "decay_level": 1,
      "env_curve": 2,
      "sustain": 0,
      "note_slide": 0,
      "pan_slide_shape": 1,
      "pan": 0,
      "amp_slide": 0,
      "sustain_level": 1,
      "pan_slide": 0,
      "attack": 0,
      "note": 52,
      "note_slide_shape": 1
    },
    "summary": "Saw Wave",
    "inherit_base": "Beep",
    "inherit_arg": true
  },
  "ChipNoise": {
    "name": ":chipnoise",
    "hiden": true,
    "opts": {
      "decay_level": 1,
      "sustain": 1,
      "env_curve": 0,
      "freq_band_slide_shape": 1,
      "amp_slide_curve": 1,
      "pan_slide_shape": 1,
      "decay": 0,
      "freq_band_slide": 0,
      "amp_slide_shape": 0,
      "freq_band": 0,
      "freq_band_slide_curve": 0,
      "amp_slide": 0,
      "sustain_level": 1,
      "amp": 1,
      "attack_level": 1,
      "pan_slide_curve": 0,
      "pan_slide": 0,
      "attack": 0,
      "pan": 0,
      "release": 0
    },
    "summary": "Chip Noise",
    "inherit_base": "Noise",
    "inherit_arg": false
  },
  "ModTri": {
    "name": ":mod_tri",
    "hiden": false,
    "opts": {
      "mod_phase_offset": 0,
      "mod_phase_slide_curve": 0,
      "note_slide_curve": 0,
      "release": 1,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "amp_slide_shape": 1,
      "mod_pulse_width": 0.5,
      "mod_range": 5,
      "decay": 0,
      "mod_phase": 0.25,
      "amp": 1,
      "mod_pulse_width_slide_shape": 1,
      "attack_level": 1,
      "pan_slide_curve": 0,
      "decay_level": 1,
      "env_curve": 2,
      "mod_phase_slide_shape": 1,
      "mod_invert_wave": 0,
      "sustain": 0,
      "note_slide": 0,
      "pan_slide_shape": 1,
      "mod_pulse_width_slide": 0,
      "mod_range_slide_curve": 0,
      "cutoff_slide": 0,
      "mod_phase_slide": 0,
      "cutoff": 100,
      "mod_range_slide_shape": 1,
      "pan": 0,
      "amp_slide": 0,
      "sustain_level": 1,
      "pan_slide": 0,
      "mod_pulse_width_slide_curve": 0,
      "mod_wave": 1,
      "mod_range_slide": 0,
      "attack": 0,
      "note": 52,
      "note_slide_shape": 1
    },
    "summary": "Modulated Triangle Wave",
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false
  },
  "Pulse": {
    "name": ":pulse",
    "hiden": true,
    "opts": {
      "note_slide_curve": 0,
      "release": 1,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "pulse_width_slide": 0,
      "cutoff_slide_shape": 1,
      "amp_slide_shape": 1,
      "pan_slide_shape": 1,
      "decay": 0,
      "note_slide_shape": 1,
      "amp": 1,
      "attack_level": 1,
      "decay_level": 1,
      "env_curve": 2,
      "sustain": 0,
      "note_slide": 0,
      "pan_slide_curve": 0,
      "cutoff_slide": 0,
      "cutoff": 100,
      "pulse_width_slide_shape": 1,
      "amp_slide": 0,
      "sustain_level": 1,
      "pan_slide": 0,
      "pulse_width": 0.5,
      "attack": 0,
      "note": 52,
      "pan": 0
    },
    "summary": "Pulse Wave",
    "inherit_base": "Square",
    "inherit_arg": true
  },
  "DSaw": {
    "name": ":dsaw",
    "hiden": false,
    "opts": {
      "note_slide_curve": 0,
      "release": 1,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "amp_slide_shape": 1,
      "decay": 0,
      "amp": 1,
      "attack_level": 1,
      "pan_slide_curve": 0,
      "decay_level": 1,
      "env_curve": 2,
      "detune_slide_curve": 0,
      "sustain": 0,
      "note_slide": 0,
      "pan_slide_shape": 1,
      "detune_slide": 0,
      "cutoff_slide": 0,
      "cutoff": 100,
      "pan": 0,
      "amp_slide": 0,
      "sustain_level": 1,
      "pan_slide": 0,
      "detune": 0.1,
      "detune_slide_shape": 1,
      "attack": 0,
      "note": 52,
      "note_slide_shape": 1
    },
    "summary": "Detuned Saw wave",
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false
  },
  "Hoover": {
    "name": ":hoover",
    "hiden": false,
    "opts": {
      "note_slide_curve": 0,
      "res_slide_shape": 1,
      "release": 1,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "amp_slide_shape": 1,
      "res": 0.1,
      "decay": 0,
      "amp": 1,
      "attack_level": 1,
      "pan_slide_curve": 0,
      "decay_level": 1,
      "env_curve": 2,
      "res_slide": 0,
      "sustain": 0,
      "note_slide": 0,
      "pan_slide_shape": 1,
      "cutoff_slide": 0,
      "res_slide_curve": 0,
      "cutoff": 130,
      "pan": 0,
      "amp_slide": 0,
      "sustain_level": 1,
      "pan_slide": 0,
      "attack": 0.05,
      "note": 52,
      "note_slide_shape": 1
    },
    "summary": "Hoover",
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false
  },
  "StereoPlayer": {
    "name": ":stereo_player",
    "hiden": true,
    "opts": {
      "slope_below_slide_shape": 1,
      "hpf_sustain": -1,
      "release": 0,
      "hpf_slide_curve": 0,
      "pitch": 0,
      "lpf_release": 0,
      "pitch_slide_curve": 0,
      "relax_time": 0.01,
      "threshold_slide_curve": 0,
      "hpf_attack_level": -1,
      "hpf_sustain_level": -1,
      "lpf": -1,
      "threshold_slide_shape": 1,
      "hpf_release": 0,
      "slope_below_slide_curve": 0,
      "pitch_dis_slide_shape": 1,
      "amp_slide": 0,
      "window_size": 0.2,
      "time_dis_slide": 0,
      "attack": 0,
      "time_dis": 0.0,
      "pitch_dis_slide_curve": 0,
      "lpf_slide_curve": 0,
      "pan_slide_shape": 1,
      "start": 0,
      "lpf_min_slide_shape": 1,
      "hpf_init_level": -1,
      "time_dis_slide_shape": 1,
      "hpf_slide_shape": 1,
      "env_curve": 2,
      "pre_amp": 1,
      "lpf_attack": 0,
      "time_dis_slide_curve": 0,
      "lpf_min_slide": 0,
      "threshold": 0.2,
      "hpf": -1,
      "lpf_slide_shape": 1,
      "hpf_slide": 0,
      "relax_time_slide_curve": 0,
      "norm": 0,
      "clamp_time_slide": 0,
      "hpf_env_curve": 2,
      "relax_time_slide": 0,
      "hpf_decay": 0,
      "attack_level": 1,
      "hpf_max": -1,
      "hpf_max_slide": 0,
      "pitch_slide_shape": 1,
      "lpf_decay_level": -1,
      "lpf_init_level": -1,
      "slope_below": 1,
      "lpf_min": -1,
      "pan_slide_curve": 0,
      "window_size_slide": 0,
      "window_size_slide_curve": 0,
      "lpf_slide": 0,
      "slope_above_slide": 0,
      "sustain_level": 1,
      "pan_slide": 0,
      "clamp_time_slide_curve": 0,
      "pitch_slide": 0,
      "pitch_dis": 0.0,
      "threshold_slide": 0,
      "hpf_max_slide_shape": 1,
      "decay_level": 1,
      "hpf_max_slide_curve": 0,
      "lpf_min_slide_curve": 0,
      "amp_slide_curve": 0,
      "lpf_decay": 0,
      "amp_slide_shape": 1,
      "pre_amp_slide_shape": 1,
      "hpf_attack": 0,
      "slope_above_slide_curve": 0,
      "decay": 0,
      "amp": 1,
      "hpf_release_level": -1,
      "relax_time_slide_shape": 1,
      "compress": 0,
      "slope_below_slide": 0,
      "pre_amp_slide": 0,
      "sustain": -1,
      "pre_amp_slide_curve": 0,
      "lpf_env_curve": 2,
      "window_size_slide_shape": 1,
      "lpf_sustain": -1,
      "lpf_sustain_level": -1,
      "hpf_decay_level": -1,
      "rate": 1,
      "lpf_attack_level": -1,
      "slope_above_slide_shape": 1,
      "finish": 1,
      "lpf_release_level": -1,
      "pitch_dis_slide": 0,
      "clamp_time": 0.01,
      "slope_above": 0.5,
      "clamp_time_slide_shape": 1,
      "pan": 0
    },
    "summary": "Stereo Sample Player",
    "inherit_base": "MonoPlayer",
    "inherit_arg": true
  },
  "PNoise": {
    "name": ":pnoise",
    "hiden": true,
    "opts": {
      "res_slide_shape": 1,
      "release": 1,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "amp_slide_shape": 1,
      "pan_slide_shape": 1,
      "res": 0,
      "decay": 0,
      "amp": 1,
      "attack_level": 1,
      "decay_level": 1,
      "env_curve": 2,
      "res_slide": 0,
      "sustain": 0,
      "pan_slide_curve": 0,
      "cutoff_slide": 0,
      "res_slide_curve": 0,
      "cutoff": 110,
      "amp_slide": 0,
      "sustain_level": 1,
      "pan_slide": 0,
      "attack": 0,
      "pan": 0
    },
    "summary": "Pink Noise",
    "inherit_base": "Noise",
    "inherit_arg": true
  },
  "ChipLead": {
    "name": ":chiplead",
    "hiden": false,
    "opts": {
      "note_slide_curve": 0,
      "release": 1,
      "pan_slide_shape": 1,
      "amp_slide_shape": 1,
      "decay": 0,
      "amp": 1,
      "attack_level": 1,
      "pan_slide_curve": 0,
      "decay_level": 1,
      "width": 0,
      "env_curve": 2,
      "sustain": 0,
      "note_slide": 0,
      "amp_slide_curve": 0,
      "note": 60,
      "pan": 0,
      "amp_slide": 0,
      "sustain_level": 1,
      "pan_slide": 0,
      "attack": 0,
      "note_resolution": 0.1,
      "note_slide_shape": 1
    },
    "summary": "Chip Lead",
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false
  },
  "SynthPluck": {
    "name": ":pluck",
    "hiden": false,
    "opts": {
      "note_slide_curve": 0,
      "release": 1,
      "amp_slide_curve": 0,
      "amp_slide_shape": 1,
      "decay": 0,
      "amp": 1,
      "attack_level": 1,
      "pan_slide_curve": 0,
      "decay_level": 1,
      "coef": 0.3,
      "sustain": 0,
      "note_slide": 0,
      "pan_slide_shape": 1,
      "max_delay_time": 0.125,
      "noise_amp": 0.8,
      "pan": 0,
      "amp_slide": 0,
      "pluck_decay": 30,
      "sustain_level": 1,
      "pan_slide": 0,
      "attack": 0,
      "note": 52,
      "note_slide_shape": 1
    },
    "summary": "SynthPluck",
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false
  },
  "ModFM": {
    "name": ":mod_fm",
    "hiden": true,
    "opts": {
      "mod_phase": 0.25,
      "release": 1,
      "depth": 1,
      "cutoff": 100,
      "mod_invert_wave": 0,
      "pan_slide_shape": 1,
      "mod_pulse_width": 0.5,
      "depth_slide": 0,
      "divisor": 2,
      "attack_level": 1,
      "decay_level": 1,
      "divisor_slide_shape": 1,
      "divisor_slide_curve": 0,
      "pan_slide_curve": 0,
      "mod_range": 5,
      "depth_slide_curve": 0,
      "amp_slide": 0,
      "sustain_level": 1,
      "pan_slide": 0,
      "mod_wave": 1,
      "attack": 0,
      "note": 52,
      "note_slide_shape": 1,
      "mod_phase_offset": 0,
      "note_slide_curve": 0,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "amp_slide_shape": 1,
      "decay": 0,
      "amp": 1,
      "env_curve": 2,
      "depth_slide_shape": 1,
      "sustain": 0,
      "note_slide": 0,
      "cutoff_slide": 0,
      "divisor_slide": 0,
      "pan": 0
    },
    "summary": "Basic FM synthesis with frequency modulation.",
    "inherit_base": "FM",
    "inherit_arg": true
  },
  "BNoise": {
    "name": ":bnoise",
    "hiden": true,
    "opts": {
      "res_slide_shape": 1,
      "release": 1,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "amp_slide_shape": 1,
      "pan_slide_shape": 1,
      "res": 0,
      "decay": 0,
      "amp": 1,
      "attack_level": 1,
      "decay_level": 1,
      "env_curve": 2,
      "res_slide": 0,
      "sustain": 0,
      "pan_slide_curve": 0,
      "cutoff_slide": 0,
      "res_slide_curve": 0,
      "cutoff": 110,
      "amp_slide": 0,
      "sustain_level": 1,
      "pan_slide": 0,
      "attack": 0,
      "pan": 0
    },
    "summary": "Brown Noise",
    "inherit_base": "Noise",
    "inherit_arg": true
  },
  "Singer": {
    "name": ":singer",
    "hiden": true,
    "opts": {
      "decay_level": 1,
      "sustain": 0,
      "note_slide": 0,
      "amp_slide_curve": 0,
      "pan_slide_shape": 1,
      "decay": 0,
      "amp_slide_shape": 1,
      "sustain_level": 1,
      "note_slide_curve": 0,
      "amp_slide": 0,
      "note_slide_shape": 1,
      "amp": 1,
      "attack_level": 1,
      "pan_slide_curve": 0,
      "pan_slide": 0,
      "env_curve": 2,
      "attack": 1,
      "note": 52,
      "pan": 0,
      "release": 4.0
    },
    "summary": "Singer",
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false
  },
  "ChipBass": {
    "name": ":chipbass",
    "hiden": false,
    "opts": {
      "decay_level": 1,
      "sustain": 0,
      "note_slide": 0,
      "pan_slide_shape": 1,
      "amp_slide_curve": 0,
      "decay": 0,
      "note_resolution": 0.1,
      "amp_slide_shape": 1,
      "sustain_level": 1,
      "note_slide_curve": 0,
      "amp_slide": 0,
      "note_slide_shape": 1,
      "amp": 1,
      "attack_level": 1,
      "pan_slide_curve": 0,
      "pan_slide": 0,
      "env_curve": 2,
      "attack": 0,
      "note": 60,
      "pan": 0,
      "release": 1
    },
    "summary": "Chip Bass",
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false
  },
  "BasicMonoPlayer": {
    "name": ":basic_mono_player",
    "hiden": true,
    "opts": {
      "lpf_slide_curve": 0,
      "amp_slide_curve": 0,
      "pan_slide_shape": 1,
      "hpf_slide": 0,
      "hpf_slide_curve": 0,
      "amp_slide_shape": 1,
      "lpf_slide": 0,
      "rate": 1,
      "lpf_slide_shape": 1,
      "amp_slide": 0,
      "amp": 1,
      "pan_slide_curve": 0,
      "pan_slide": 0,
      "hpf_slide_shape": 1,
      "hpf": -1,
      "pan": 0,
      "lpf": -1
    },
    "summary": "Basic Mono Sample Player (no env)",
    "inherit_base": "StudioInfo",
    "inherit_arg": false
  },
  "GNoise": {
    "name": ":gnoise",
    "hiden": true,
    "opts": {
      "res_slide_shape": 1,
      "release": 1,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "amp_slide_shape": 1,
      "pan_slide_shape": 1,
      "res": 0,
      "decay": 0,
      "amp": 1,
      "attack_level": 1,
      "decay_level": 1,
      "env_curve": 2,
      "res_slide": 0,
      "sustain": 0,
      "pan_slide_curve": 0,
      "cutoff_slide": 0,
      "res_slide_curve": 0,
      "cutoff": 110,
      "amp_slide": 0,
      "sustain_level": 1,
      "pan_slide": 0,
      "attack": 0,
      "pan": 0
    },
    "summary": "Grey Noise",
    "inherit_base": "Noise",
    "inherit_arg": true
  },
  "ModSine": {
    "name": ":mod_sine",
    "hiden": false,
    "opts": {
      "mod_phase_offset": 0,
      "mod_phase_slide_curve": 0,
      "note_slide_curve": 0,
      "release": 1,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "amp_slide_shape": 1,
      "mod_pulse_width": 0.5,
      "mod_range": 5,
      "decay": 0,
      "mod_phase": 0.25,
      "amp": 1,
      "mod_pulse_width_slide_shape": 1,
      "attack_level": 1,
      "pan_slide_curve": 0,
      "decay_level": 1,
      "env_curve": 2,
      "mod_phase_slide_shape": 1,
      "mod_invert_wave": 0,
      "sustain": 0,
      "note_slide": 0,
      "pan_slide_shape": 1,
      "mod_pulse_width_slide": 0,
      "mod_range_slide_curve": 0,
      "cutoff_slide": 0,
      "mod_phase_slide": 0,
      "cutoff": 100,
      "mod_range_slide_shape": 1,
      "pan": 0,
      "amp_slide": 0,
      "sustain_level": 1,
      "pan_slide": 0,
      "mod_pulse_width_slide_curve": 0,
      "mod_wave": 1,
      "mod_range_slide": 0,
      "attack": 0,
      "note": 52,
      "note_slide_shape": 1
    },
    "summary": "Modulated Sine Wave",
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false
  },
  "SoundInStereo": {
    "name": ":sound_in_stereo",
    "hiden": true,
    "opts": {
      "release": 0,
      "amp_slide_curve": 0,
      "amp_slide_shape": 1,
      "decay": 0,
      "amp": 1,
      "attack_level": 1,
      "pan_slide_curve": 0,
      "decay_level": 1,
      "env_curve": 0,
      "sustain": 1,
      "pan_slide_shape": 1,
      "amp_slide": 0,
      "sustain_level": 1,
      "pan_slide": 0,
      "attack": 0,
      "input": 1,
      "pan": 0
    },
    "summary": "Sound In Stereo",
    "inherit_base": "SoundIn",
    "inherit_arg": true
  },
  "PrettyBell": {
    "name": ":pretty_bell",
    "hiden": true,
    "opts": {
      "note_slide_curve": 0,
      "release": 1,
      "amp_slide_curve": 0,
      "amp_slide_shape": 1,
      "decay": 0,
      "amp": 1,
      "attack_level": 1,
      "pan_slide_curve": 0,
      "decay_level": 1,
      "env_curve": 2,
      "sustain": 0,
      "note_slide": 0,
      "pan_slide_shape": 1,
      "pan": 0,
      "amp_slide": 0,
      "sustain_level": 1,
      "pan_slide": 0,
      "attack": 0,
      "note": 52,
      "note_slide_shape": 1
    },
    "summary": "Pretty Bell",
    "inherit_base": "DullBell",
    "inherit_arg": true
  },
  "StudioInfo": {
    "hiden": true,
    "opts": {},
    "inherit_arg": true,
    "inherit_base": "SonicPiSynth"
  },
  "MonoPlayer": {
    "name": ":mono_player",
    "hiden": true,
    "opts": {
      "slope_below_slide_shape": 1,
      "hpf_sustain": -1,
      "release": 0,
      "hpf_slide_curve": 0,
      "pitch": 0,
      "lpf_release": 0,
      "pitch_slide_curve": 0,
      "relax_time": 0.01,
      "lpf_slide": 0,
      "slope_above_slide": 0,
      "hpf_sustain_level": -1,
      "lpf": -1,
      "threshold_slide_shape": 1,
      "hpf_release": 0,
      "slope_below_slide_curve": 0,
      "pitch_dis_slide_shape": 1,
      "amp_slide": 0,
      "window_size": 0.2,
      "pan_slide": 0,
      "attack": 0,
      "time_dis": 0.0,
      "pitch_dis_slide_curve": 0,
      "lpf_slide_curve": 0,
      "pan_slide_shape": 1,
      "start": 0,
      "lpf_min_slide_shape": 1,
      "hpf_init_level": -1,
      "time_dis_slide_shape": 1,
      "hpf_slide_shape": 1,
      "env_curve": 2,
      "pre_amp": 1,
      "lpf_attack": 0,
      "time_dis_slide_curve": 0,
      "lpf_min_slide": 0,
      "threshold_slide": 0,
      "threshold": 0.2,
      "hpf": -1,
      "lpf_slide_shape": 1,
      "hpf_slide": 0,
      "relax_time_slide_curve": 0,
      "lpf_sustain_level": -1,
      "clamp_time_slide": 0,
      "hpf_env_curve": 2,
      "relax_time_slide": 0,
      "hpf_decay": 0,
      "lpf_init_level": -1,
      "lpf_decay_level": -1,
      "hpf_max": -1,
      "pitch_slide_shape": 1,
      "attack_level": 1,
      "decay_level": 1,
      "slope_below": 1,
      "lpf_min": -1,
      "amp_slide_curve": 0,
      "window_size_slide": 0,
      "window_size_slide_curve": 0,
      "threshold_slide_curve": 0,
      "hpf_attack_level": -1,
      "sustain_level": 1,
      "time_dis_slide": 0,
      "clamp_time_slide_curve": 0,
      "pitch_slide": 0,
      "finish": 1,
      "rate": 1,
      "hpf_max_slide_shape": 1,
      "lpf_release_level": -1,
      "lpf_min_slide_curve": 0,
      "pan_slide_curve": 0,
      "lpf_decay": 0,
      "amp_slide_shape": 1,
      "pre_amp_slide_shape": 1,
      "hpf_attack": 0,
      "slope_above_slide_curve": 0,
      "decay": 0,
      "amp": 1,
      "slope_above": 0.5,
      "relax_time_slide_shape": 1,
      "compress": 0,
      "slope_below_slide": 0,
      "pre_amp_slide": 0,
      "sustain": -1,
      "pre_amp_slide_curve": 0,
      "lpf_env_curve": 2,
      "window_size_slide_shape": 1,
      "lpf_sustain": -1,
      "norm": 0,
      "hpf_decay_level": -1,
      "hpf_max_slide": 0,
      "lpf_attack_level": -1,
      "slope_above_slide_shape": 1,
      "pitch_dis": 0.0,
      "hpf_max_slide_curve": 0,
      "pitch_dis_slide": 0,
      "clamp_time": 0.01,
      "hpf_release_level": -1,
      "clamp_time_slide_shape": 1,
      "pan": 0
    },
    "summary": "Mono Sample Player",
    "inherit_base": "BasicMonoPlayer",
    "inherit_arg": false
  },
  "Square": {
    "name": ":square",
    "hiden": false,
    "opts": {
      "note_slide_curve": 0,
      "release": 1,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "amp_slide_shape": 1,
      "decay": 0,
      "amp": 1,
      "attack_level": 1,
      "pan_slide_curve": 0,
      "decay_level": 1,
      "env_curve": 2,
      "sustain": 0,
      "note_slide": 0,
      "pan_slide_shape": 1,
      "cutoff_slide": 0,
      "cutoff": 100,
      "pan": 0,
      "amp_slide": 0,
      "sustain_level": 1,
      "pan_slide": 0,
      "attack": 0,
      "note": 52,
      "note_slide_shape": 1
    },
    "summary": "Square Wave",
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false
  },
  "DPulse": {
    "name": ":dpulse",
    "hiden": true,
    "opts": {
      "note_slide_curve": 0,
      "release": 1,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "pulse_width_slide": 0,
      "cutoff_slide_shape": 1,
      "amp_slide_shape": 1,
      "pan_slide_shape": 1,
      "decay": 0,
      "pulse_width": 0.5,
      "note_slide_shape": 1,
      "amp": 1,
      "attack_level": 1,
      "decay_level": 1,
      "env_curve": 2,
      "dpulse_width_slide_shape": 1,
      "dpulse_width": 0,
      "detune_slide_curve": 0,
      "sustain": 0,
      "note_slide": 0,
      "pan_slide_curve": 0,
      "detune_slide": 0,
      "dpulse_width_slide": 0,
      "cutoff_slide": 0,
      "cutoff": 100,
      "pulse_width_slide_shape": 1,
      "amp_slide": 0,
      "pulse_width_slide_curve": 0,
      "sustain_level": 1,
      "pan_slide": 0,
      "detune": 0.1,
      "detune_slide_shape": 1,
      "attack": 0,
      "note": 52,
      "pan": 0
    },
    "summary": "Detuned Pulse Wave",
    "inherit_base": "DSaw",
    "inherit_arg": true
  },
  "Noise": {
    "name": ":noise",
    "hiden": false,
    "opts": {
      "res_slide_shape": 1,
      "release": 1,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "amp_slide_shape": 1,
      "res": 0,
      "decay": 0,
      "amp": 1,
      "attack_level": 1,
      "pan_slide_curve": 0,
      "decay_level": 1,
      "env_curve": 2,
      "res_slide": 0,
      "sustain": 0,
      "pan_slide_shape": 1,
      "cutoff_slide": 0,
      "res_slide_curve": 0,
      "cutoff": 110,
      "amp_slide": 0,
      "sustain_level": 1,
      "pan_slide": 0,
      "attack": 0,
      "pan": 0
    },
    "summary": "Noise",
    "inherit_base": "Pitchless",
    "inherit_arg": false
  },
  "BasicStereoPlayer": {
    "name": ":basic_stereo_player",
    "hiden": true,
    "opts": {
      "lpf_slide_curve": 0,
      "amp_slide_curve": 0,
      "hpf_slide_curve": 0,
      "amp_slide_shape": 1,
      "amp": 1,
      "pan_slide_curve": 0,
      "hpf_slide_shape": 1,
      "rate": 1,
      "lpf": -1,
      "pan_slide_shape": 1,
      "amp_slide": 0,
      "lpf_slide": 0,
      "hpf": -1,
      "lpf_slide_shape": 1,
      "hpf_slide": 0,
      "pan_slide": 0,
      "pan": 0
    },
    "summary": "Basic Stereo Sample Player (no env)",
    "inherit_base": "BasicMonoPlayer",
    "inherit_arg": true
  },
  "CNoise": {
    "name": ":cnoise",
    "hiden": true,
    "opts": {
      "res_slide_shape": 1,
      "release": 1,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "amp_slide_shape": 1,
      "pan_slide_shape": 1,
      "res": 0,
      "decay": 0,
      "amp": 1,
      "attack_level": 1,
      "decay_level": 1,
      "env_curve": 2,
      "res_slide": 0,
      "sustain": 0,
      "pan_slide_curve": 0,
      "cutoff_slide": 0,
      "res_slide_curve": 0,
      "cutoff": 110,
      "amp_slide": 0,
      "sustain_level": 1,
      "pan_slide": 0,
      "attack": 0,
      "pan": 0
    },
    "summary": "Clip Noise",
    "inherit_base": "Noise",
    "inherit_arg": true
  },
  "TB303": {
    "name": ":tb303",
    "hiden": false,
    "opts": {
      "res_slide_shape": 1,
      "release": 1,
      "pulse_width_slide": 0,
      "pan_slide_shape": 1,
      "cutoff_decay_level": 1,
      "cutoff_attack": 0,
      "cutoff_min": 30,
      "attack_level": 1,
      "decay_level": 1,
      "res_slide": 0,
      "pan_slide_curve": 0,
      "cutoff_release": 1,
      "cutoff": 120,
      "amp_slide": 0,
      "pulse_width_slide_curve": 0,
      "sustain_level": 1,
      "pan_slide": 0,
      "cutoff_decay": 0,
      "cutoff_attack_level": 1,
      "pulse_width": 0.5,
      "cutoff_sustain": 0,
      "note": 52,
      "note_slide_shape": 1,
      "attack": 0,
      "cutoff_min_slide_curve": 0,
      "wave": 0,
      "note_slide_curve": 0,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "amp_slide_shape": 1,
      "res": 0.9,
      "decay": 0,
      "amp": 1,
      "cutoff_sustain_level": 1,
      "cutoff_min_slide_shape": 1,
      "env_curve": 2,
      "sustain": 0,
      "note_slide": 0,
      "cutoff_slide": 0,
      "res_slide_curve": 0,
      "pulse_width_slide_shape": 1,
      "cutoff_min_slide": 0,
      "pan": 0
    },
    "summary": "TB-303 Emulation",
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false
  },
  "Supersaw": {
    "name": ":supersaw",
    "hiden": false,
    "opts": {
      "note_slide_curve": 0,
      "res_slide_shape": 1,
      "release": 1,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "amp_slide_shape": 1,
      "res": 0.7,
      "decay": 0,
      "amp": 1,
      "attack_level": 1,
      "pan_slide_curve": 0,
      "decay_level": 1,
      "env_curve": 2,
      "res_slide": 0,
      "sustain": 0,
      "note_slide": 0,
      "pan_slide_shape": 1,
      "cutoff_slide": 0,
      "res_slide_curve": 0,
      "cutoff": 130,
      "pan": 0,
      "amp_slide": 0,
      "sustain_level": 1,
      "pan_slide": 0,
      "attack": 0,
      "note": 52,
      "note_slide_shape": 1
    },
    "summary": "Supersaw",
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false
  },
  "BaseMixer": {
    "hiden": true,
    "opts": {},
    "inherit_arg": true,
    "inherit_base": "StudioInfo"
  },
  "Beep": {
    "name": ":beep",
    "hiden": false,
    "opts": {
      "decay_level": 1,
      "sustain": 0,
      "note_slide": 0,
      "amp_slide_curve": 0,
      "pan_slide_shape": 1,
      "decay": 0,
      "amp_slide_shape": 1,
      "sustain_level": 1,
      "note_slide_curve": 0,
      "amp_slide": 0,
      "note_slide_shape": 1,
      "amp": 1,
      "attack_level": 1,
      "pan_slide_curve": 0,
      "pan_slide": 0,
      "env_curve": 2,
      "attack": 0,
      "note": 52,
      "pan": 0,
      "release": 1
    },
    "summary": "Sine Wave",
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false
  },
  "SoundIn": {
    "name": ":sound_in",
    "hiden": false,
    "opts": {
      "decay_level": 1,
      "sustain": 1,
      "env_curve": 0,
      "amp_slide_curve": 0,
      "pan_slide_shape": 1,
      "decay": 0,
      "amp_slide_shape": 1,
      "amp_slide": 0,
      "sustain_level": 1,
      "amp": 1,
      "attack_level": 1,
      "pan_slide_curve": 0,
      "pan_slide": 0,
      "attack": 0,
      "input": 1,
      "pan": 0,
      "release": 0
    },
    "summary": "Sound In",
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false
  },
  "ModSaw": {
    "name": ":mod_saw",
    "hiden": false,
    "opts": {
      "mod_phase_offset": 0,
      "mod_phase_slide_curve": 0,
      "note_slide_curve": 0,
      "release": 1,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "amp_slide_shape": 1,
      "mod_pulse_width": 0.5,
      "mod_range": 5,
      "decay": 0,
      "mod_phase": 0.25,
      "amp": 1,
      "mod_pulse_width_slide_shape": 1,
      "attack_level": 1,
      "pan_slide_curve": 0,
      "decay_level": 1,
      "env_curve": 2,
      "mod_phase_slide_shape": 1,
      "mod_invert_wave": 0,
      "sustain": 0,
      "note_slide": 0,
      "pan_slide_shape": 1,
      "mod_pulse_width_slide": 0,
      "mod_range_slide_curve": 0,
      "cutoff_slide": 0,
      "mod_phase_slide": 0,
      "cutoff": 100,
      "mod_range_slide_shape": 1,
      "pan": 0,
      "amp_slide": 0,
      "sustain_level": 1,
      "pan_slide": 0,
      "mod_pulse_width_slide_curve": 0,
      "mod_wave": 1,
      "mod_range_slide": 0,
      "attack": 0,
      "note": 52,
      "note_slide_shape": 1
    },
    "summary": "Modulated Saw Wave",
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false
  },
  "Zawa": {
    "name": ":zawa",
    "hiden": false,
    "opts": {
      "wave": 3,
      "note_slide_curve": 0,
      "res_slide_shape": 1,
      "release": 1,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "disable_wave": 0,
      "cutoff_slide_shape": 1,
      "amp_slide_shape": 1,
      "phase": 1,
      "res": 0.9,
      "decay": 0,
      "phase_offset": 0,
      "phase_slide_shape": 1,
      "amp": 1,
      "attack_level": 1,
      "pan_slide_curve": 0,
      "decay_level": 1,
      "phase_slide_curve": 0,
      "res_slide": 0,
      "pulse_width_slide": 0,
      "sustain": 0,
      "phase_slide": 0,
      "note_slide": 0,
      "range": 24,
      "pan_slide_shape": 1,
      "cutoff_slide": 0,
      "res_slide_curve": 0,
      "cutoff": 100,
      "invert_wave": 0,
      "pan": 0,
      "range_slide_shape": 1,
      "amp_slide": 0,
      "pulse_width_slide_curve": 0,
      "sustain_level": 1,
      "pan_slide": 0,
      "pulse_width_slide_shape": 1,
      "pulse_width": 0.5,
      "range_slide": 0,
      "attack": 0,
      "note": 52,
      "note_slide_shape": 1,
      "range_slide_curve": 0
    },
    "summary": "Zawa",
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false
  },
  "Growl": {
    "name": ":growl",
    "hiden": false,
    "opts": {
      "note_slide_curve": 0,
      "res_slide_shape": 1,
      "release": 1,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "amp_slide_shape": 1,
      "res": 0.7,
      "decay": 0,
      "amp": 1,
      "attack_level": 1,
      "pan_slide_curve": 0,
      "decay_level": 1,
      "env_curve": 2,
      "res_slide": 0,
      "sustain": 0,
      "note_slide": 0,
      "pan_slide_shape": 1,
      "cutoff_slide": 0,
      "res_slide_curve": 0,
      "cutoff": 130,
      "pan": 0,
      "amp_slide": 0,
      "sustain_level": 1,
      "pan_slide": 0,
      "attack": 0.1,
      "note": 52,
      "note_slide_shape": 1
    },
    "summary": "Growl",
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false
  },
  "Hollow": {
    "name": ":hollow",
    "hiden": false,
    "opts": {
      "noise": 1,
      "note_slide_curve": 0,
      "res_slide_shape": 1,
      "release": 1,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "norm": 0,
      "cutoff_slide_shape": 1,
      "amp_slide_shape": 1,
      "res": 0.99,
      "decay": 0,
      "amp": 1,
      "attack_level": 1,
      "pan_slide_curve": 0,
      "decay_level": 1,
      "env_curve": 2,
      "res_slide": 0,
      "sustain": 0,
      "note_slide": 0,
      "pan_slide_shape": 1,
      "cutoff_slide": 0,
      "res_slide_curve": 0,
      "cutoff": 90,
      "pan": 0,
      "amp_slide": 0,
      "sustain_level": 1,
      "pan_slide": 0,
      "attack": 0,
      "note": 52,
      "note_slide_shape": 1
    },
    "summary": "Hollow",
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false
  },
  "SubPulse": {
    "name": ":subpulse",
    "hiden": true,
    "opts": {
      "sub_detune": -12,
      "note_slide_curve": 0,
      "release": 1,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "pulse_width_slide": 0,
      "cutoff_slide_shape": 1,
      "amp_slide_shape": 1,
      "decay": 0,
      "amp": 1,
      "sub_amp_slide_shape": 1,
      "attack_level": 1,
      "pan_slide_curve": 0,
      "decay_level": 1,
      "sub_amp_slide": 0,
      "env_curve": 2,
      "sub_amp_slide_curve": 0,
      "sub_amp": 1,
      "sub_detune_slide_shape": 1,
      "sustain": 0,
      "note_slide": 0,
      "pan_slide_shape": 1,
      "cutoff_slide": 0,
      "cutoff": 100,
      "sustain_level": 1,
      "pulse_width_slide_shape": 1,
      "amp_slide": 0,
      "note_slide_shape": 1,
      "pan_slide": 0,
      "sub_detune_slide": 0,
      "pulse_width": 0.5,
      "attack": 0,
      "note": 52,
      "pan": 0
    },
    "summary": "Pulse Wave with sub",
    "inherit_base": "Pulse",
    "inherit_arg": true
  },
  "SynthPiano": {
    "name": ":piano",
    "hiden": false,
    "opts": {
      "note_slide_curve": 0,
      "release": 1,
      "amp_slide_curve": 0,
      "amp_slide_shape": 1,
      "decay": 0,
      "hard": 0.5,
      "amp": 1,
      "attack_level": 1,
      "pan_slide_curve": 0,
      "decay_level": 1,
      "sustain": 0,
      "note_slide": 0,
      "pan_slide_shape": 1,
      "stereo_width": 0,
      "pan": 0,
      "amp_slide": 0,
      "sustain_level": 1,
      "pan_slide": 0,
      "attack": 0,
      "note": 52,
      "note_slide_shape": 1,
      "vel": 0.2
    },
    "summary": "SynthPiano",
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false
  },
  "Prophet": {
    "name": ":prophet",
    "hiden": false,
    "opts": {
      "note_slide_curve": 0,
      "res_slide_shape": 1,
      "release": 1,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "amp_slide_shape": 1,
      "res": 0.7,
      "decay": 0,
      "amp": 1,
      "attack_level": 1,
      "pan_slide_curve": 0,
      "decay_level": 1,
      "env_curve": 2,
      "res_slide": 0,
      "sustain": 0,
      "note_slide": 0,
      "pan_slide_shape": 1,
      "cutoff_slide": 0,
      "res_slide_curve": 0,
      "cutoff": 110,
      "pan": 0,
      "amp_slide": 0,
      "sustain_level": 1,
      "pan_slide": 0,
      "attack": 0,
      "note": 52,
      "note_slide_shape": 1
    },
    "summary": "The Prophet",
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false
  },
  "Tri": {
    "name": ":tri",
    "hiden": true,
    "opts": {
      "note_slide_curve": 0,
      "release": 1,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "pulse_width_slide": 0,
      "cutoff_slide_shape": 1,
      "amp_slide_shape": 1,
      "decay": 0,
      "amp": 1,
      "attack_level": 1,
      "pan_slide_curve": 0,
      "decay_level": 1,
      "env_curve": 2,
      "sustain": 0,
      "note_slide": 0,
      "pan_slide_shape": 1,
      "cutoff_slide": 0,
      "cutoff": 100,
      "sustain_level": 1,
      "pulse_width_slide_shape": 1,
      "amp_slide": 0,
      "note_slide_shape": 1,
      "pan_slide": 0,
      "pulse_width": 0.5,
      "attack": 0,
      "note": 52,
      "pan": 0
    },
    "summary": "Triangle Wave",
    "inherit_base": "Pulse",
    "inherit_arg": true
  },
  "DarkSeaHorn": {
    "name": ":dark_sea_horn",
    "hiden": true,
    "opts": {
      "decay_level": 1,
      "sustain": 0,
      "note_slide": 0,
      "amp_slide_curve": 0,
      "pan_slide_shape": 1,
      "decay": 0,
      "amp_slide_shape": 1,
      "sustain_level": 1,
      "note_slide_curve": 0,
      "amp_slide": 0,
      "note_slide_shape": 1,
      "amp": 1,
      "attack_level": 1,
      "pan_slide_curve": 0,
      "pan_slide": 0,
      "env_curve": 2,
      "attack": 1,
      "note": 52,
      "pan": 0,
      "release": 4.0
    },
    "summary": "Dark Sea Horn",
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false
  },
  "ModDSaw": {
    "name": ":mod_dsaw",
    "hiden": false,
    "opts": {
      "mod_phase_offset": 0,
      "mod_phase_slide_curve": 0,
      "detune_slide_shape": 1,
      "note_slide_curve": 0,
      "release": 1,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "amp_slide_shape": 1,
      "mod_pulse_width": 0.5,
      "mod_range": 5,
      "decay": 0,
      "mod_phase": 0.25,
      "amp": 1,
      "mod_pulse_width_slide_shape": 1,
      "attack_level": 1,
      "pan_slide_curve": 0,
      "decay_level": 1,
      "env_curve": 2,
      "mod_phase_slide_shape": 1,
      "mod_invert_wave": 0,
      "detune_slide_curve": 0,
      "sustain": 0,
      "note_slide": 0,
      "pan_slide_shape": 1,
      "mod_pulse_width_slide": 0,
      "mod_range_slide_curve": 0,
      "cutoff_slide": 0,
      "mod_phase_slide": 0,
      "detune": 0.1,
      "cutoff": 100,
      "mod_range_slide_shape": 1,
      "pan": 0,
      "amp_slide": 0,
      "sustain_level": 1,
      "pan_slide": 0,
      "detune_slide": 0,
      "mod_pulse_width_slide_curve": 0,
      "mod_wave": 1,
      "mod_range_slide": 0,
      "attack": 0,
      "note": 52,
      "note_slide_shape": 1
    },
    "summary": "Modulated Detuned Saw Waves",
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false
  },
  "TechSaws": {
    "name": ":tech_saws",
    "hiden": false,
    "opts": {
      "note_slide_curve": 0,
      "res_slide_shape": 1,
      "release": 1,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "amp_slide_shape": 1,
      "res": 0.7,
      "decay": 0,
      "amp": 1,
      "attack_level": 1,
      "pan_slide_curve": 0,
      "decay_level": 1,
      "env_curve": 2,
      "res_slide": 0,
      "sustain": 0,
      "note_slide": 0,
      "pan_slide_shape": 1,
      "cutoff_slide": 0,
      "res_slide_curve": 0,
      "cutoff": 130,
      "pan": 0,
      "amp_slide": 0,
      "sustain_level": 1,
      "pan_slide": 0,
      "attack": 0,
      "note": 52,
      "note_slide_shape": 1
    },
    "summary": "TechSaws",
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false
  },
  "DarkAmbience": {
    "name": ":dark_ambience",
    "hiden": false,
    "opts": {
      "room": 70,
      "noise": 0,
      "note_slide_curve": 0,
      "res_slide_shape": 1,
      "release": 1,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "amp_slide_shape": 1,
      "detune2_slide": 0,
      "res": 0.7,
      "detune1_slide_curve": 0,
      "decay": 0,
      "detune1_slide_shape": 1,
      "amp": 1,
      "attack_level": 1,
      "pan_slide_curve": 0,
      "decay_level": 1,
      "env_curve": 2,
      "res_slide": 0,
      "detune1_slide": 0,
      "sustain": 0,
      "detune1": 12,
      "note_slide": 0,
      "pan_slide_shape": 1,
      "detune2_slide_shape": 1,
      "cutoff_slide": 0,
      "res_slide_curve": 0,
      "detune2_slide_curve": 0,
      "cutoff": 110,
      "pan": 0,
      "amp_slide": 0,
      "sustain_level": 1,
      "pan_slide": 0,
      "reverb_time": 100,
      "detune2": 24,
      "attack": 0,
      "note": 52,
      "note_slide_shape": 1,
      "ring": 0.2
    },
    "summary": "Dark Ambience",
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false
  },
  "MainMixer": {
    "name": ":mixer",
    "hiden": true,
    "opts": {
      "lpf_slide_curve": 0,
      "pre_amp_slide_curve": 0,
      "hpf_bypass": 0,
      "force_mono": 0,
      "pre_amp_slide": 0.02,
      "amp_slide_curve": 0,
      "hpf_slide": 0.02,
      "hpf_slide_curve": 0,
      "amp_slide_shape": 1,
      "pre_amp_slide_shape": 1,
      "hpf": 0,
      "lpf_slide_shape": 1,
      "amp_slide": 0.02,
      "limiter_bypass": 0,
      "amp": 1,
      "lpf_slide": 0.02,
      "hpf_slide_shape": 1,
      "lpf_bypass": 0,
      "pre_amp": 1,
      "lpf": 135.5,
      "invert_stereo": 0
    },
    "summary": "Main Mixer",
    "inherit_base": "BaseMixer",
    "inherit_arg": false
  },
  "Pitchless": {
    "hiden": true,
    "opts": {},
    "inherit_arg": true,
    "inherit_base": "SonicPiSynth"
  },
  "SonicPiSynth": {
    "hiden": true,
    "opts": {},
    "inherit_arg": true,
    "inherit_base": "SynthInfo"
  }
}

synth_nodes = {
  ":dsaw": "DSaw",
  ":mod_dsaw": "ModDSaw",
  ":fx_rlpf": "FXRLPF",
  ":fx_rhpf": "FXRHPF",
  ":fx_replace_nrlpf": "FXNormRLPF",
  ":fx_slicer": "FXSlicer",
  ":fx_nbpf": "FXNBPF",
  ":mod_fm": "ModFM",
  ":mono_player": "MonoPlayer",
  ":fx_replace_reverb": "FXReverb",
  ":beep": "Beep",
  ":cnoise": "CNoise",
  ":gnoise": "GNoise",
  ":fx_replace_nlpf": "FXNormLPF",
  ":dull_bell": "DullBell",
  ":chipnoise": "ChipNoise",
  ":bnoise": "BNoise",
  ":saw": "Saw",
  ":stereo_player": "StereoPlayer",
  ":dtri": "DTri",
  ":fx_bpf": "FXBPF",
  ":fx_nrlpf": "FXNormRLPF",
  ":fx_reverb": "FXReverb",
  ":fx_ring_mod": "FXRingMod",
  ":fx_replace_lpf": "FXLPF",
  ":pnoise": "PNoise",
  ":fx_band_eq": "FXBandEQ",
  ":fx_level": "FXLevel",
  ":chipbass": "ChipBass",
  ":fx_replace_ixi_techno": "FXIXITechno",
  ":noise": "Noise",
  ":fx_replace_pan": "FXPan",
  ":fx_replace_rhpf": "FXRHPF",
  ":fx_nlpf": "FXNormLPF",
  ":hollow": "Hollow",
  ":prophet": "Prophet",
  ":fx_replace_compressor": "FXCompressor",
  ":dark_ambience": "DarkAmbience",
  ":tb303": "TB303",
  ":pulse": "Pulse",
  ":fx_nrbpf": "FXNRBPF",
  ":mod_beep": "ModSine",
  ":fx_replace_nhpf": "FXNormHPF",
  ":fx_rbpf": "FXRBPF",
  ":tech_saws": "TechSaws",
  ":main_mixer": "MainMixer",
  ":basic_stereo_player": "BasicStereoPlayer",
  ":dpulse": "DPulse",
  ":pretty_bell": "PrettyBell",
  ":mod_pulse": "ModPulse",
  ":chiplead": "ChipLead",
  ":growl": "Growl",
  ":fx_normaliser": "FXNormaliser",
  ":fm": "FM",
  ":fx_gverb": "FXGVerb",
  ":sound_in": "SoundIn",
  ":fx_replace_nrhpf": "FXNormRHPF",
  ":fx_flanger": "FXFlanger",
  ":fx_bitcrusher": "FXBitcrusher",
  ":zawa": "Zawa",
  ":mod_sine": "ModSine",
  ":fx_mono": "FXMono",
  ":fx_krush": "FXKrush",
  ":fx_wobble": "FXWobble",
  ":fx_compressor": "FXCompressor",
  ":piano": "SynthPiano",
  ":fx_whammy": "FXWhammy",
  ":supersaw": "Supersaw",
  ":fx_replace_echo": "FXEcho",
  ":fx_echo": "FXEcho",
  ":fx_panslicer": "FXPanSlicer",
  ":fx_replace_level": "FXLevel",
  ":fx_nhpf": "FXNormHPF",
  ":fx_nrhpf": "FXNormRHPF",
  ":fx_replace_rlpf": "FXRLPF",
  ":blade": "SynthViolin",
  ":fx_octaver": "FXOctaver",
  ":square": "Square",
  ":mod_saw": "ModSaw",
  ":basic_mixer": "BasicMixer",
  ":fx_hpf": "FXHPF",
  ":sine": "Beep",
  ":pluck": "SynthPluck",
  ":hoover": "Hoover",
  ":fx_lpf": "FXLPF",
  ":sound_in_stereo": "SoundInStereo",
  ":fx_distortion": "FXDistortion",
  ":basic_mono_player": "BasicMonoPlayer",
  ":subpulse": "SubPulse",
  ":fx_replace_wobble": "FXWobble",
  ":fx_pitch_shift": "FXPitchShift",
  ":fx_replace_normaliser": "FXNormaliser",
  ":tri": "Tri",
  ":mod_tri": "ModTri",
  ":fx_pan": "FXPan",
  ":fx_vowel": "FXVowel",
  ":fx_replace_distortion": "FXDistortion",
  ":fx_replace_slicer": "FXSlicer",
  ":fx_ixi_techno": "FXIXITechno",
  ":fx_tanh": "FXTanh",
  ":fx_replace_hpf": "FXHPF"
}

fx = {
  "FXRLPF": {
    "name": ":fx_rlpf",
    "hiden": true,
    "opts": {
      "mix_slide": 0,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "amp_slide_shape": 1,
      "pre_amp_slide_shape": 1,
      "res": 0.5,
      "amp": 1,
      "pre_mix_slide_curve": 0,
      "res_slide_shape": 1,
      "pre_amp": 1,
      "mix_slide_shape": 1,
      "pre_mix": 1,
      "pre_amp_slide_curve": 0,
      "pre_amp_slide": 0,
      "cutoff_slide": 0,
      "res_slide_curve": 0,
      "cutoff": 100,
      "res_slide": 0,
      "amp_slide": 0,
      "pre_mix_slide_shape": 1,
      "mix": 1,
      "pre_mix_slide": 0,
      "mix_slide_curve": 0
    },
    "summary": "Resonant Low Pass Filter",
    "inherit_base": "FXLPF",
    "inherit_arg": true
  },
  "FXNRBPF": {
    "name": ":fx_nrbpf",
    "hiden": true,
    "opts": {
      "mix_slide": 0,
      "amp_slide_curve": 0,
      "amp_slide_shape": 1,
      "pre_amp_slide_shape": 1,
      "res": 0.5,
      "amp": 1,
      "pre_mix_slide_curve": 0,
      "res_slide_shape": 1,
      "centre": 100,
      "pre_amp": 1,
      "mix_slide_shape": 1,
      "pre_mix": 1,
      "pre_amp_slide_curve": 0,
      "centre_slide_shape": 1,
      "pre_amp_slide": 0,
      "res_slide_curve": 0,
      "res_slide": 0,
      "amp_slide": 0,
      "pre_mix_slide_shape": 1,
      "centre_slide": 0,
      "mix": 1,
      "pre_mix_slide": 0,
      "centre_slide_curve": 0,
      "mix_slide_curve": 0
    },
    "summary": "Normalised Resonant Band Pass Filter",
    "inherit_base": "FXRBPF",
    "inherit_arg": true
  },
  "FXNormRLPF": {
    "name": ":fx_nrlpf",
    "hiden": true,
    "opts": {
      "mix_slide": 0,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "amp_slide_shape": 1,
      "pre_amp_slide_shape": 1,
      "res": 0.5,
      "amp": 1,
      "pre_mix_slide_curve": 0,
      "res_slide_shape": 1,
      "pre_amp": 1,
      "mix_slide_shape": 1,
      "pre_mix": 1,
      "pre_amp_slide_curve": 0,
      "pre_amp_slide": 0,
      "cutoff_slide": 0,
      "res_slide_curve": 0,
      "cutoff": 100,
      "res_slide": 0,
      "amp_slide": 0,
      "pre_mix_slide_shape": 1,
      "mix": 1,
      "pre_mix_slide": 0,
      "mix_slide_curve": 0
    },
    "summary": "Normalised Resonant Low Pass Filter",
    "inherit_base": "FXRLPF",
    "inherit_arg": true
  },
  "FXPanSlicer": {
    "name": ":fx_panslicer",
    "hiden": true,
    "opts": {
      "smooth_slide": 0,
      "mix_slide": 0,
      "prob_pos_slide_shape": 1,
      "seed": 0,
      "pulse_width_slide": 0,
      "pre_mix_slide_curve": 0,
      "pan_max_slide_curve": 0,
      "smooth_down": 0,
      "smooth_down_slide": 0,
      "phase_slide_shape": 1,
      "amp_min": 0,
      "amp_min_slide": 0,
      "amp_max_slide_shape": 1,
      "probability_slide": 0,
      "mix_slide_shape": 1,
      "smooth_up": 0,
      "probability": 0,
      "pan_max_slide_shape": 1,
      "prob_pos": 0,
      "amp_slide_curve": 0,
      "pan_min_slide_shape": 1,
      "probability_slide_curve": 0,
      "smooth_up_slide_curve": 0,
      "smooth_up_slide": 0,
      "amp_max_slide_curve": 0,
      "amp_slide": 0,
      "pulse_width_slide_curve": 0,
      "smooth_up_slide_shape": 1,
      "pan_max": 1,
      "pulse_width": 0.5,
      "mix": 1,
      "prob_pos_slide_curve": 0,
      "pre_mix": 1,
      "probability_slide_shape": 1,
      "wave": 1,
      "smooth_down_slide_curve": 0,
      "smooth_slide_shape": 1,
      "amp_max": 1,
      "amp_slide_shape": 1,
      "phase": 0.25,
      "phase_slide": 0,
      "pre_amp_slide_shape": 1,
      "pan_min_slide": 0,
      "phase_offset": 0,
      "smooth_down_slide_shape": 1,
      "amp": 1,
      "mix_slide_curve": 0,
      "smooth": 0,
      "smooth_slide_curve": 0,
      "phase_slide_curve": 0,
      "pre_amp": 1,
      "pre_amp_slide": 0,
      "pre_amp_slide_curve": 0,
      "pan_min": -1,
      "pan_min_slide_curve": 0,
      "pan_max_slide": 0,
      "invert_wave": 0,
      "amp_min_slide_shape": 1,
      "pulse_width_slide_shape": 1,
      "pre_mix_slide_shape": 1,
      "amp_max_slide": 0,
      "amp_min_slide_curve": 0,
      "pre_mix_slide": 0,
      "prob_pos_slide": 0
    },
    "summary": "Pan Slicer",
    "inherit_base": "FXSlicer",
    "inherit_arg": true
  },
  "FXPan": {
    "name": ":fx_pan",
    "hiden": false,
    "opts": {
      "mix_slide": 0,
      "amp_slide_curve": 0,
      "amp_slide_shape": 1,
      "pan_slide_shape": 1,
      "pre_amp_slide_shape": 1,
      "amp": 1,
      "pre_mix_slide_curve": 0,
      "pan_slide_curve": 0,
      "pre_amp": 1,
      "mix_slide_shape": 1,
      "pre_mix": 1,
      "pre_amp_slide_curve": 0,
      "pre_amp_slide": 0,
      "amp_slide": 0,
      "pre_mix_slide_shape": 1,
      "pan_slide": 0,
      "mix": 1,
      "pre_mix_slide": 0,
      "pan": 0,
      "mix_slide_curve": 0
    },
    "summary": "Pan",
    "inherit_base": "FXInfo",
    "inherit_arg": true
  },
  "FXInfo": {
    "hiden": true,
    "opts": {
      "pre_amp_slide_curve": 0,
      "mix_slide": 0,
      "pre_amp_slide": 0,
      "amp_slide_curve": 0,
      "pre_amp_slide_shape": 1,
      "amp_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "amp_slide": 0,
      "pre_mix_slide_shape": 1,
      "amp": 1,
      "mix_slide_curve": 0,
      "mix": 1,
      "pre_mix_slide": 0,
      "pre_amp": 1,
      "mix_slide_shape": 1,
      "pre_mix": 1
    },
    "inherit_arg": false,
    "inherit_base": "BaseInfo"
  },
  "FXBitcrusher": {
    "name": ":fx_bitcrusher",
    "hiden": false,
    "opts": {
      "bits_slide_shape": 1,
      "mix_slide": 0,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "amp_slide_shape": 1,
      "bits_slide": 0,
      "pre_amp_slide_shape": 1,
      "bits_slide_curve": 0,
      "amp": 1,
      "pre_mix_slide_curve": 0,
      "sample_rate_slide_curve": 0,
      "pre_amp": 1,
      "mix_slide_shape": 1,
      "pre_mix": 1,
      "pre_amp_slide_curve": 0,
      "pre_amp_slide": 0,
      "sample_rate_slide": 0,
      "cutoff_slide": 0,
      "cutoff": 0,
      "amp_slide": 0,
      "sample_rate_slide_shape": 1,
      "pre_mix_slide_shape": 1,
      "bits": 8,
      "mix": 1,
      "pre_mix_slide": 0,
      "sample_rate": 10000,
      "mix_slide_curve": 0
    },
    "summary": "Bitcrusher",
    "inherit_base": "FXInfo",
    "inherit_arg": true
  },
  "FXNormHPF": {
    "name": ":fx_nhpf",
    "hiden": true,
    "opts": {
      "mix_slide": 0,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "amp_slide_shape": 1,
      "pre_amp_slide_shape": 1,
      "amp": 1,
      "pre_mix_slide_curve": 0,
      "pre_amp": 1,
      "mix_slide_shape": 1,
      "pre_mix": 1,
      "pre_amp_slide_curve": 0,
      "pre_amp_slide": 0,
      "cutoff_slide": 0,
      "cutoff": 100,
      "amp_slide": 0,
      "pre_mix_slide_shape": 1,
      "mix": 1,
      "pre_mix_slide": 0,
      "mix_slide_curve": 0
    },
    "summary": "Normalised High Pass Filter",
    "inherit_base": "FXHPF",
    "inherit_arg": true
  },
  "FXKrush": {
    "name": ":fx_krush",
    "hiden": false,
    "opts": {
      "gain_slide_shape": 1,
      "mix_slide": 0,
      "amp_slide_curve": 0,
      "gain": 5,
      "cutoff_slide_shape": 1,
      "amp_slide_shape": 1,
      "pre_amp_slide_shape": 1,
      "res": 0,
      "gain_slide__curve": 0,
      "amp": 1,
      "pre_mix_slide_curve": 0,
      "res_slide_shape": 1,
      "pre_amp": 1,
      "mix_slide_shape": 1,
      "pre_mix": 1,
      "gain_slide": 0,
      "pre_amp_slide_curve": 0,
      "pre_amp_slide": 0,
      "cutoff_slide": 0,
      "res_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "cutoff": 100,
      "res_slide": 0,
      "amp_slide": 0,
      "pre_mix_slide_shape": 1,
      "mix": 1,
      "pre_mix_slide": 0,
      "mix_slide_curve": 0
    },
    "summary": "krush",
    "inherit_base": "FXInfo",
    "inherit_arg": true
  },
  "FXDistortion": {
    "name": ":fx_distortion",
    "hiden": false,
    "opts": {
      "mix_slide": 0,
      "amp_slide_curve": 0,
      "amp_slide_shape": 1,
      "pre_amp_slide_shape": 1,
      "distort_slide_curve": 0,
      "amp": 1,
      "pre_mix_slide_curve": 0,
      "distort_slide": 0,
      "pre_amp": 1,
      "mix_slide_shape": 1,
      "pre_mix": 1,
      "pre_amp_slide_curve": 0,
      "distort_slide_shape": 1,
      "pre_amp_slide": 0,
      "distort": 0.5,
      "amp_slide": 0,
      "pre_mix_slide_shape": 1,
      "mix": 1,
      "pre_mix_slide": 0,
      "mix_slide_curve": 0
    },
    "summary": "Distortion",
    "inherit_base": "FXInfo",
    "inherit_arg": true
  },
  "FXOctaver": {
    "name": ":fx_octaver",
    "hiden": false,
    "opts": {
      "subsub_amp_slide_curve": 0,
      "mix_slide": 0,
      "sub_amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "amp_slide_shape": 1,
      "super_amp": 1,
      "pre_amp_slide_shape": 1,
      "amp": 1,
      "pre_mix_slide_curve": 0,
      "super_amp_slide": 0,
      "sub_amp_slide": 0,
      "pre_amp": 1,
      "mix_slide_shape": 1,
      "pre_mix": 1,
      "pre_amp_slide_curve": 0,
      "subsub_amp": 1,
      "pre_amp_slide": 0,
      "sub_amp_slide_curve": 0,
      "amp_slide": 0,
      "pre_mix_slide_shape": 1,
      "sub_amp": 1,
      "subsub_amp_slide_shape": 1,
      "mix": 1,
      "subsub_amp_slide": 0,
      "pre_mix_slide": 0,
      "super_amp_slide_shape": 1,
      "super_amp_slide_curve": 0,
      "mix_slide_curve": 0
    },
    "summary": "Octaver",
    "inherit_base": "FXInfo",
    "inherit_arg": true
  },
  "FXVowel": {
    "name": ":fx_vowel",
    "hiden": false,
    "opts": {
      "mix_slide": 0,
      "amp_slide_curve": 0,
      "amp_slide_shape": 1,
      "pre_amp_slide_shape": 1,
      "amp": 1,
      "pre_mix_slide_curve": 0,
      "pre_amp": 1,
      "mix_slide_shape": 1,
      "pre_mix": 1,
      "pre_amp_slide_curve": 0,
      "voice": 0,
      "pre_amp_slide": 0,
      "amp_slide": 0,
      "pre_mix_slide_shape": 1,
      "mix": 1,
      "vowel_sound": 1,
      "pre_mix_slide": 0,
      "mix_slide_curve": 0
    },
    "summary": "Vowel",
    "inherit_base": "FXInfo",
    "inherit_arg": true
  },
  "FXCompressor": {
    "name": ":fx_compressor",
    "hiden": false,
    "opts": {
      "clamp_time_slide": 0,
      "slope_below_slide_shape": 1,
      "relax_time_slide": 0,
      "mix_slide": 0,
      "amp_slide_curve": 0,
      "slope_below_slide_curve": 0,
      "amp_slide_shape": 1,
      "pre_amp_slide_shape": 1,
      "slope_above_slide_shape": 1,
      "slope_above_slide_curve": 0,
      "relax_time": 0.01,
      "amp": 1,
      "pre_mix_slide_curve": 0,
      "slope_above": 0.5,
      "relax_time_slide_shape": 1,
      "slope_below": 1,
      "pre_amp": 1,
      "mix_slide_shape": 1,
      "pre_mix": 1,
      "threshold_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "pre_amp_slide": 0,
      "slope_below_slide": 0,
      "threshold_slide_curve": 0,
      "clamp_time": 0.01,
      "threshold": 0.2,
      "slope_above_slide": 0,
      "amp_slide": 0,
      "pre_mix_slide_shape": 1,
      "relax_time_slide_curve": 0,
      "clamp_time_slide_curve": 0,
      "mix": 1,
      "clamp_time_slide_shape": 1,
      "pre_mix_slide": 0,
      "threshold_slide": 0,
      "mix_slide_curve": 0
    },
    "summary": "Compressor",
    "inherit_base": "FXInfo",
    "inherit_arg": true
  },
  "FXEcho": {
    "name": ":fx_echo",
    "hiden": false,
    "opts": {
      "mix_slide": 0,
      "amp_slide_curve": 0,
      "amp_slide_shape": 1,
      "phase": 0.25,
      "phase_slide": 0,
      "pre_amp_slide_shape": 1,
      "decay_slide_curve": 0,
      "decay": 2,
      "phase_slide_shape": 1,
      "amp": 1,
      "pre_mix_slide_curve": 0,
      "decay_slide_shape": 1,
      "phase_slide_curve": 0,
      "pre_amp": 1,
      "mix_slide_shape": 1,
      "pre_mix": 1,
      "pre_amp_slide_curve": 0,
      "pre_amp_slide": 0,
      "decay_slide": 0,
      "amp_slide": 0,
      "pre_mix_slide_shape": 1,
      "max_phase": 2,
      "mix": 1,
      "pre_mix_slide": 0,
      "mix_slide_curve": 0
    },
    "summary": "Echo",
    "inherit_base": "FXInfo",
    "inherit_arg": true
  },
  "FXNormaliser": {
    "name": ":fx_normaliser",
    "hiden": false,
    "opts": {
      "mix_slide": 0,
      "amp_slide_curve": 0,
      "amp_slide_shape": 1,
      "level_slide": 0,
      "pre_amp_slide_shape": 1,
      "level_slide_curve": 0,
      "amp": 1,
      "pre_mix_slide_curve": 0,
      "pre_amp": 1,
      "mix_slide_shape": 1,
      "pre_mix": 1,
      "pre_amp_slide_curve": 0,
      "pre_amp_slide": 0,
      "level_slide_shape": 1,
      "level": 1,
      "amp_slide": 0,
      "pre_mix_slide_shape": 1,
      "mix": 1,
      "pre_mix_slide": 0,
      "mix_slide_curve": 0
    },
    "summary": "Normaliser",
    "inherit_base": "FXInfo",
    "inherit_arg": true
  },
  "FXWhammy": {
    "name": ":fx_whammy",
    "hiden": false,
    "opts": {
      "mix_slide": 0,
      "amp_slide_curve": 0,
      "amp_slide_shape": 1,
      "transpose_slide": 0,
      "pre_amp_slide_shape": 1,
      "transpose_slide_shape": 1,
      "amp": 1,
      "pre_mix_slide_curve": 0,
      "grainsize": 0.075,
      "pre_amp": 1,
      "mix_slide_shape": 1,
      "pre_mix": 1,
      "transpose_slide_curve": 0,
      "pre_amp_slide_curve": 0,
      "pre_amp_slide": 0,
      "max_delay_time": 1,
      "amp_slide": 0,
      "pre_mix_slide_shape": 1,
      "transpose": 12,
      "mix": 1,
      "pre_mix_slide": 0,
      "deltime": 0.05,
      "mix_slide_curve": 0
    },
    "summary": "Whammy",
    "inherit_base": "FXInfo",
    "inherit_arg": true
  },
  "FXRBPF": {
    "name": ":fx_rbpf",
    "hiden": true,
    "opts": {
      "mix_slide": 0,
      "amp_slide_curve": 0,
      "amp_slide_shape": 1,
      "pre_amp_slide_shape": 1,
      "res": 0.5,
      "amp": 1,
      "pre_mix_slide_curve": 0,
      "res_slide_shape": 1,
      "centre": 100,
      "pre_amp": 1,
      "mix_slide_shape": 1,
      "pre_mix": 1,
      "pre_amp_slide_curve": 0,
      "centre_slide_shape": 1,
      "pre_amp_slide": 0,
      "res_slide_curve": 0,
      "res_slide": 0,
      "amp_slide": 0,
      "pre_mix_slide_shape": 1,
      "centre_slide": 0,
      "mix": 1,
      "pre_mix_slide": 0,
      "centre_slide_curve": 0,
      "mix_slide_curve": 0
    },
    "summary": "Resonant Band Pass Filter",
    "inherit_base": "FXBPF",
    "inherit_arg": true
  },
  "FXNormRHPF": {
    "name": ":fx_nrhpf",
    "hiden": true,
    "opts": {
      "mix_slide": 0,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "amp_slide_shape": 1,
      "pre_amp_slide_shape": 1,
      "res": 0.5,
      "amp": 1,
      "pre_mix_slide_curve": 0,
      "res_slide_shape": 1,
      "pre_amp": 1,
      "mix_slide_shape": 1,
      "pre_mix": 1,
      "pre_amp_slide_curve": 0,
      "pre_amp_slide": 0,
      "cutoff_slide": 0,
      "res_slide_curve": 0,
      "cutoff": 100,
      "res_slide": 0,
      "amp_slide": 0,
      "pre_mix_slide_shape": 1,
      "mix": 1,
      "pre_mix_slide": 0,
      "mix_slide_curve": 0
    },
    "summary": "Normalised Resonant High Pass Filter",
    "inherit_base": "FXRHPF",
    "inherit_arg": true
  },
  "FXNormLPF": {
    "name": ":fx_nlpf",
    "hiden": true,
    "opts": {
      "mix_slide": 0,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "amp_slide_shape": 1,
      "pre_amp_slide_shape": 1,
      "amp": 1,
      "pre_mix_slide_curve": 0,
      "pre_amp": 1,
      "mix_slide_shape": 1,
      "pre_mix": 1,
      "pre_amp_slide_curve": 0,
      "pre_amp_slide": 0,
      "cutoff_slide": 0,
      "cutoff": 100,
      "amp_slide": 0,
      "pre_mix_slide_shape": 1,
      "mix": 1,
      "pre_mix_slide": 0,
      "mix_slide_curve": 0
    },
    "summary": "Normalised Low Pass Filter.",
    "inherit_base": "FXLPF",
    "inherit_arg": true
  },
  "FXMono": {
    "name": ":fx_mono",
    "hiden": false,
    "opts": {
      "mix_slide": 0,
      "amp_slide_curve": 0,
      "amp_slide_shape": 1,
      "pan_slide_shape": 1,
      "pre_amp_slide_shape": 1,
      "amp": 1,
      "pre_mix_slide_curve": 0,
      "pan_slide_curve": 0,
      "pre_amp": 1,
      "mix_slide_shape": 1,
      "pre_mix": 1,
      "pre_amp_slide_curve": 0,
      "pre_amp_slide": 0,
      "amp_slide": 0,
      "pre_mix_slide_shape": 1,
      "pan_slide": 0,
      "mix": 1,
      "pre_mix_slide": 0,
      "pan": 0,
      "mix_slide_curve": 0
    },
    "summary": "Mono",
    "inherit_base": "FXInfo",
    "inherit_arg": true
  },
  "FXSlicer": {
    "name": ":fx_slicer",
    "hiden": false,
    "opts": {
      "smooth_slide": 0,
      "mix_slide": 0,
      "smooth": 0,
      "seed": 0,
      "pulse_width_slide": 0,
      "pre_mix_slide_curve": 0,
      "smooth_down": 0,
      "smooth_down_slide": 0,
      "phase_slide_shape": 1,
      "amp_min": 0,
      "amp_min_slide": 0,
      "amp_max_slide_shape": 1,
      "probability_slide": 0,
      "mix_slide_shape": 1,
      "smooth_up": 0,
      "probability": 0,
      "prob_pos": 0,
      "smooth_slide_shape": 1,
      "probability_slide_curve": 0,
      "amp_max": 1,
      "smooth_up_slide": 0,
      "amp_max_slide_curve": 0,
      "amp_slide": 0,
      "pulse_width_slide_curve": 0,
      "smooth_up_slide_shape": 1,
      "pulse_width": 0.5,
      "mix": 1,
      "prob_pos_slide_curve": 0,
      "pre_mix": 1,
      "probability_slide_shape": 1,
      "wave": 1,
      "smooth_down_slide_curve": 0,
      "amp_slide_curve": 0,
      "smooth_up_slide_curve": 0,
      "amp_slide_shape": 1,
      "phase": 0.25,
      "pre_amp_slide_curve": 0,
      "pre_amp_slide_shape": 1,
      "phase_offset": 0,
      "smooth_down_slide_shape": 1,
      "amp": 1,
      "mix_slide_curve": 0,
      "prob_pos_slide_shape": 1,
      "smooth_slide_curve": 0,
      "phase_slide_curve": 0,
      "pre_amp": 1,
      "pre_amp_slide": 0,
      "phase_slide": 0,
      "invert_wave": 0,
      "amp_min_slide_shape": 1,
      "pulse_width_slide_shape": 1,
      "pre_mix_slide_shape": 1,
      "amp_max_slide": 0,
      "amp_min_slide_curve": 0,
      "pre_mix_slide": 0,
      "prob_pos_slide": 0
    },
    "summary": "Slicer",
    "inherit_base": "FXInfo",
    "inherit_arg": true
  },
  "FXHPF": {
    "name": ":fx_hpf",
    "hiden": false,
    "opts": {
      "mix_slide": 0,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "amp_slide_shape": 1,
      "pre_amp_slide_shape": 1,
      "amp": 1,
      "pre_mix_slide_curve": 0,
      "pre_amp": 1,
      "mix_slide_shape": 1,
      "pre_mix": 1,
      "pre_amp_slide_curve": 0,
      "pre_amp_slide": 0,
      "cutoff_slide": 0,
      "cutoff": 100,
      "amp_slide": 0,
      "pre_mix_slide_shape": 1,
      "mix": 1,
      "pre_mix_slide": 0,
      "mix_slide_curve": 0
    },
    "summary": "High Pass Filter",
    "inherit_base": "FXInfo",
    "inherit_arg": true
  },
  "FXPitchShift": {
    "name": ":fx_pitch_shift",
    "hiden": false,
    "opts": {
      "mix_slide": 0,
      "pitch_dis_slide_curve": 0,
      "amp_slide_curve": 0,
      "time_dis_slide": 0,
      "pitch": 0,
      "amp_slide_shape": 1,
      "pre_amp_slide_shape": 1,
      "pitch_slide_curve": 0,
      "pitch_slide_shape": 1,
      "amp": 1,
      "pre_mix_slide_curve": 0,
      "time_dis_slide_shape": 1,
      "pre_amp": 1,
      "mix_slide_shape": 1,
      "pre_mix": 1,
      "pre_amp_slide_curve": 0,
      "pre_amp_slide": 0,
      "window_size_slide_shape": 1,
      "time_dis_slide_curve": 0,
      "window_size_slide_curve": 0,
      "pitch_dis_slide_shape": 1,
      "window_size_slide": 0,
      "amp_slide": 0,
      "pre_mix_slide_shape": 1,
      "pitch_dis": 0.0,
      "window_size": 0.2,
      "pitch_dis_slide": 0,
      "pitch_slide": 0,
      "mix": 1,
      "pre_mix_slide": 0,
      "time_dis": 0.0,
      "mix_slide_curve": 0
    },
    "summary": "Pitch shift",
    "inherit_base": "FXInfo",
    "inherit_arg": true
  },
  "FXRingMod": {
    "name": ":fx_ring_mod",
    "hiden": false,
    "opts": {
      "mix_slide": 0,
      "amp_slide_curve": 0,
      "amp_slide_shape": 1,
      "pre_amp_slide_shape": 1,
      "mod_amp": 1,
      "amp": 1,
      "pre_mix_slide_curve": 0,
      "pre_amp": 1,
      "mix_slide_shape": 1,
      "pre_mix": 1,
      "mod_amp_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "pre_amp_slide": 0,
      "freq_slide_curve": 0,
      "mod_amp_slide": 0,
      "freq": 30,
      "amp_slide": 0,
      "pre_mix_slide_shape": 1,
      "mod_amp_slide_curve": 0,
      "mix": 1,
      "freq_slide": 0,
      "pre_mix_slide": 0,
      "freq_slide_shape": 1,
      "mix_slide_curve": 0
    },
    "summary": "Ring Modulator",
    "inherit_base": "FXInfo",
    "inherit_arg": true
  },
  "FXGVerb": {
    "name": ":fx_gverb",
    "hiden": false,
    "opts": {
      "dry_slide_shape": 1,
      "damp_slide": 0,
      "mix_slide": 0,
      "release": 3,
      "amp_slide_curve": 0,
      "amp_slide_shape": 1,
      "pre_amp_slide_shape": 1,
      "spread_slide_shape": 1,
      "amp": 1,
      "pre_mix_slide_curve": 0,
      "spread_slide": 0,
      "dry": 1,
      "spread_slide_curve": 0,
      "damp_slide_shape": 1,
      "pre_amp": 1,
      "mix_slide_shape": 1,
      "pre_mix": 1,
      "dry_slide_curve": 0,
      "pre_damp_slide": 0,
      "pre_amp_slide_curve": 0,
      "pre_amp_slide": 0,
      "ref_level": 0.7,
      "spread": 0.5,
      "room": 10,
      "pre_damp_slide_curve": 0,
      "damp_slide_curve": 0,
      "amp_slide": 0,
      "dry_slide": 0,
      "pre_mix_slide_shape": 1,
      "damp": 0.5,
      "pre_damp_slide_shape": 1,
      "pre_damp": 0.5,
      "mix": 1,
      "tail_level": 0.5,
      "pre_mix_slide": 0,
      "mix_slide_curve": 0
    },
    "summary": "GVerb",
    "inherit_base": "FXInfo",
    "inherit_arg": true
  },
  "FXIXITechno": {
    "name": ":fx_ixi_techno",
    "hiden": false,
    "opts": {
      "cutoff_min_slide_curve": 0,
      "cutoff_max_slide_curve": 0,
      "mix_slide": 0,
      "amp_slide_curve": 0,
      "amp_slide_shape": 1,
      "phase": 4,
      "phase_slide": 0,
      "pre_amp_slide_shape": 1,
      "res": 0.8,
      "phase_offset": 0,
      "phase_slide_shape": 1,
      "amp": 1,
      "pre_mix_slide_curve": 0,
      "cutoff_min": 60,
      "res_slide_shape": 1,
      "cutoff_min_slide_shape": 1,
      "cutoff_max": 120,
      "pre_amp": 1,
      "mix_slide_shape": 1,
      "pre_mix": 1,
      "pre_amp_slide_curve": 0,
      "phase_slide_curve": 0,
      "pre_amp_slide": 0,
      "res_slide_curve": 0,
      "cutoff_max_slide_shape": 1,
      "res_slide": 0,
      "amp_slide": 0,
      "pre_mix_slide_shape": 1,
      "cutoff_max_slide": 0,
      "mix": 1,
      "cutoff_min_slide": 0,
      "pre_mix_slide": 0,
      "mix_slide_curve": 0
    },
    "summary": "Techno from IXI Lang",
    "inherit_base": "FXInfo",
    "inherit_arg": true
  },
  "FXNBPF": {
    "name": ":fx_nbpf",
    "hiden": true,
    "opts": {
      "mix_slide": 0,
      "amp_slide_curve": 0,
      "amp_slide_shape": 1,
      "pre_amp_slide_shape": 1,
      "res": 0.6,
      "amp": 1,
      "pre_mix_slide_curve": 0,
      "res_slide_shape": 1,
      "centre": 100,
      "pre_amp": 1,
      "mix_slide_shape": 1,
      "pre_mix": 1,
      "pre_amp_slide_curve": 0,
      "centre_slide_shape": 1,
      "pre_amp_slide": 0,
      "res_slide_curve": 0,
      "res_slide": 0,
      "amp_slide": 0,
      "pre_mix_slide_shape": 1,
      "centre_slide": 0,
      "mix": 1,
      "pre_mix_slide": 0,
      "centre_slide_curve": 0,
      "mix_slide_curve": 0
    },
    "summary": "Normalised Band Pass Filter",
    "inherit_base": "FXBPF",
    "inherit_arg": true
  },
  "FXFlanger": {
    "name": ":fx_flanger",
    "hiden": false,
    "opts": {
      "feedback_slide_shape": 1,
      "wave": 4,
      "decay_slide": 0,
      "mix_slide": 0,
      "amp_slide_curve": 0,
      "delay_slide": 0,
      "phase": 4,
      "amp_slide_shape": 1,
      "delay_slide_shape": 1,
      "phase_slide": 0,
      "pre_amp_slide_shape": 1,
      "max_delay": 20,
      "depth_slide": 0,
      "decay": 2,
      "phase_offset": 0,
      "phase_slide_shape": 1,
      "amp": 1,
      "pre_mix_slide_curve": 0,
      "decay_slide_shape": 1,
      "feedback_slide": 0,
      "phase_slide_curve": 0,
      "pre_amp": 1,
      "mix_slide_shape": 1,
      "pre_mix": 1,
      "decay_slide_curve": 0,
      "pre_amp_slide_curve": 0,
      "pre_amp_slide": 0,
      "feedback": 0,
      "depth": 5,
      "depth_slide_curve": 0,
      "invert_wave": 0,
      "feedback_slide_curve": 0,
      "amp_slide": 0,
      "depth_slide_shape": 1,
      "pre_mix_slide_shape": 1,
      "delay": 5,
      "stereo_invert_wave": 0,
      "mix": 1,
      "pre_mix_slide": 0,
      "invert_flange": 0,
      "delay_slide_curve": 0,
      "mix_slide_curve": 0
    },
    "summary": "Flanger",
    "inherit_base": "FXInfo",
    "inherit_arg": true
  },
  "FXChorus": {
    "name": ":fx_chorus",
    "hiden": true,
    "opts": {
      "mix_slide": 0,
      "amp_slide_curve": 0,
      "amp_slide_shape": 1,
      "phase": 0.25,
      "phase_slide": 0,
      "pre_amp_slide_shape": 1,
      "decay_slide_curve": 0,
      "decay": 1e-05,
      "phase_slide_shape": 1,
      "amp": 1,
      "pre_mix_slide_curve": 0,
      "decay_slide_shape": 1,
      "phase_slide_curve": 0,
      "pre_amp": 1,
      "mix_slide_shape": 1,
      "pre_mix": 1,
      "pre_amp_slide_curve": 0,
      "pre_amp_slide": 0,
      "decay_slide": 0,
      "amp_slide": 0,
      "pre_mix_slide_shape": 1,
      "max_phase": 1,
      "mix": 1,
      "pre_mix_slide": 0,
      "mix_slide_curve": 0
    },
    "summary": "Chorus",
    "inherit_base": "FXInfo",
    "inherit_arg": true
  },
  "FXWobble": {
    "name": ":fx_wobble",
    "hiden": false,
    "opts": {
      "smooth_slide": 0,
      "mix_slide": 0,
      "prob_pos_slide_shape": 1,
      "filter": 0,
      "pulse_width_slide": 0,
      "pre_mix_slide_curve": 0,
      "smooth_down": 0,
      "smooth_down_slide": 0,
      "phase_slide_shape": 1,
      "cutoff_max_slide": 0,
      "cutoff_min": 60,
      "res_slide_shape": 1,
      "res_slide": 0,
      "mix_slide_shape": 1,
      "pre_mix": 1,
      "probability": 0,
      "prob_pos": 0,
      "pre_amp_slide": 0,
      "probability_slide_curve": 0,
      "smooth_up_slide": 0,
      "probability_slide": 0,
      "amp_slide": 0,
      "pulse_width_slide_curve": 0,
      "smooth_up_slide_shape": 1,
      "pulse_width": 0.5,
      "mix": 1,
      "prob_pos_slide_curve": 0,
      "smooth_up": 0,
      "probability_slide_shape": 1,
      "cutoff_min_slide_curve": 0,
      "wave": 0,
      "smooth_down_slide_curve": 0,
      "cutoff_max_slide_curve": 0,
      "amp_slide_curve": 0,
      "smooth_up_slide_curve": 0,
      "amp_slide_shape": 1,
      "phase": 0.5,
      "phase_slide": 0,
      "pre_amp_slide_shape": 1,
      "res": 0.8,
      "invert_wave": 0,
      "smooth_down_slide_shape": 1,
      "amp": 1,
      "mix_slide_curve": 0,
      "smooth": 0,
      "seed": 0,
      "cutoff_min_slide_shape": 1,
      "phase_slide_curve": 0,
      "pre_amp": 1,
      "smooth_slide_curve": 0,
      "pre_amp_slide_curve": 0,
      "res_slide_curve": 0,
      "phase_offset": 0,
      "cutoff_max_slide_shape": 1,
      "cutoff_max": 120,
      "pulse_width_slide_shape": 1,
      "pre_mix_slide_shape": 1,
      "smooth_slide_shape": 1,
      "cutoff_min_slide": 0,
      "pre_mix_slide": 0,
      "prob_pos_slide": 0
    },
    "summary": "Wobble",
    "inherit_base": "FXInfo",
    "inherit_arg": true
  },
  "FXLPF": {
    "name": ":fx_lpf",
    "hiden": false,
    "opts": {
      "mix_slide": 0,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "amp_slide_shape": 1,
      "pre_amp_slide_shape": 1,
      "amp": 1,
      "pre_mix_slide_curve": 0,
      "pre_amp": 1,
      "mix_slide_shape": 1,
      "pre_mix": 1,
      "pre_amp_slide_curve": 0,
      "pre_amp_slide": 0,
      "cutoff_slide": 0,
      "cutoff": 100,
      "amp_slide": 0,
      "pre_mix_slide_shape": 1,
      "mix": 1,
      "pre_mix_slide": 0,
      "mix_slide_curve": 0
    },
    "summary": "Low Pass Filter",
    "inherit_base": "FXInfo",
    "inherit_arg": true
  },
  "FXTanh": {
    "name": ":fx_tanh",
    "hiden": false,
    "opts": {
      "mix_slide": 0,
      "amp_slide_curve": 0,
      "krunch": 5,
      "amp_slide_shape": 1,
      "pre_amp_slide_shape": 1,
      "amp": 1,
      "pre_mix_slide_curve": 0,
      "krunch_slide": 0,
      "pre_amp": 1,
      "mix_slide_shape": 1,
      "pre_mix": 1,
      "pre_amp_slide_curve": 0,
      "pre_amp_slide": 0,
      "krunch_slide_curve": 0,
      "krunch_slide_shape": 1,
      "amp_slide": 0,
      "pre_mix_slide_shape": 1,
      "mix": 1,
      "pre_mix_slide": 0,
      "mix_slide_curve": 0
    },
    "summary": "Hyperbolic Tangent",
    "inherit_base": "FXInfo",
    "inherit_arg": true
  },
  "FXRHPF": {
    "name": ":fx_rhpf",
    "hiden": true,
    "opts": {
      "mix_slide": 0,
      "amp_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "amp_slide_shape": 1,
      "pre_amp_slide_shape": 1,
      "res": 0.5,
      "amp": 1,
      "pre_mix_slide_curve": 0,
      "res_slide_shape": 1,
      "pre_amp": 1,
      "mix_slide_shape": 1,
      "pre_mix": 1,
      "pre_amp_slide_curve": 0,
      "pre_amp_slide": 0,
      "cutoff_slide": 0,
      "res_slide_curve": 0,
      "cutoff": 100,
      "res_slide": 0,
      "amp_slide": 0,
      "pre_mix_slide_shape": 1,
      "mix": 1,
      "pre_mix_slide": 0,
      "mix_slide_curve": 0
    },
    "summary": "Resonant High Pass Filter",
    "inherit_base": "FXHPF",
    "inherit_arg": true
  },
  "FXReverb": {
    "name": ":fx_reverb",
    "hiden": false,
    "opts": {
      "damp_slide": 0,
      "mix_slide": 0,
      "amp_slide_curve": 0,
      "amp_slide_shape": 1,
      "room_slide_curve": 0,
      "pre_amp_slide_shape": 1,
      "room_slide_shape": 1,
      "amp": 1,
      "pre_mix_slide_curve": 0,
      "damp_slide_shape": 1,
      "pre_amp": 1,
      "mix_slide_shape": 1,
      "pre_mix": 1,
      "pre_amp_slide_curve": 0,
      "pre_amp_slide": 0,
      "room": 0.6,
      "damp_slide_curve": 0,
      "amp_slide": 0,
      "pre_mix_slide_shape": 1,
      "damp": 0.5,
      "mix": 0.4,
      "room_slide": 0,
      "pre_mix_slide": 0,
      "mix_slide_curve": 0
    },
    "summary": "Reverb",
    "inherit_base": "FXInfo",
    "inherit_arg": true
  },
  "FXBandEQ": {
    "name": ":fx_band_eq",
    "hiden": false,
    "opts": {
      "db_slide": 0,
      "mix_slide": 0,
      "amp_slide_curve": 0,
      "db": 0.6,
      "amp_slide_shape": 1,
      "pre_amp_slide_shape": 1,
      "res": 0.6,
      "amp": 1,
      "pre_mix_slide_curve": 0,
      "db_slide_shape": 1,
      "res_slide_shape": 1,
      "pre_amp": 1,
      "mix_slide_shape": 1,
      "pre_mix": 1,
      "db_slide_curve": 0,
      "pre_amp_slide_curve": 0,
      "pre_amp_slide": 0,
      "freq_slide_curve": 0,
      "res_slide_curve": 0,
      "freq": 100,
      "amp_slide": 0,
      "pre_mix_slide_shape": 1,
      "res_slide": 0,
      "mix": 1,
      "freq_slide": 0,
      "pre_mix_slide": 0,
      "freq_slide_shape": 1,
      "mix_slide_curve": 0
    },
    "summary": "Band EQ Filter",
    "inherit_base": "FXInfo",
    "inherit_arg": true
  },
  "FXLevel": {
    "name": ":fx_level",
    "hiden": false,
    "opts": {
      "amp_slide": 0,
      "amp_slide_shape": 1,
      "amp": 1,
      "amp_slide_curve": 0
    },
    "summary": "Level Amplifier",
    "inherit_base": "FXInfo",
    "inherit_arg": false
  },
  "FXBPF": {
    "name": ":fx_bpf",
    "hiden": false,
    "opts": {
      "mix_slide": 0,
      "amp_slide_curve": 0,
      "amp_slide_shape": 1,
      "pre_amp_slide_shape": 1,
      "res": 0.6,
      "amp": 1,
      "pre_mix_slide_curve": 0,
      "res_slide_shape": 1,
      "centre": 100,
      "pre_amp": 1,
      "mix_slide_shape": 1,
      "pre_mix": 1,
      "pre_amp_slide_curve": 0,
      "centre_slide_shape": 1,
      "pre_amp_slide": 0,
      "res_slide_curve": 0,
      "res_slide": 0,
      "amp_slide": 0,
      "pre_mix_slide_shape": 1,
      "centre_slide": 0,
      "mix": 1,
      "pre_mix_slide": 0,
      "centre_slide_curve": 0,
      "mix_slide_curve": 0
    },
    "summary": "Band Pass Filter",
    "inherit_base": "FXInfo",
    "inherit_arg": true
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
  "Percussive Sounds": [
    ":perc_bell",
    ":perc_snap",
    ":perc_snap2",
    ":perc_swash",
    ":perc_till"
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
  "Sounds featuring guitars": [
    ":guit_harmonics",
    ":guit_e_fifths",
    ":guit_e_slide",
    ":guit_em9"
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
  "Snare Drums": [
    ":sn_dub",
    ":sn_dolf",
    ":sn_zome"
  ]
}

