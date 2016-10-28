null = None; true = True; false = False;
#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/

lang_core = {
  "wait": {
    "accepts_block": false,
    "args": [
      {
        "beats": ":number"
      }
    ],
    "name": "wait",
    "introduced": "2,0,0",
    "hiden": true,
    "summary": "Wait for duration",
    "signature": {
      "time": null
    },
    "advances_time": true
  },
  "defonce": {
    "accepts_block": true,
    "args": [
      {
        "name": ":symbol"
      }
    ],
    "requires_block": true,
    "opts": {
      "override": false
    },
    "name": "defonce",
    "introduced": "2,0,0",
    "hiden": false,
    "summary": "Define a named value only once",
    "signature": {
      "&block": null,
      "*opts": null,
      "name": null
    }
  },
  "current_bpm": {
    "introduced": "2,0,0",
    "accepts_block": false,
    "hiden": true,
    "summary": "Get current tempo",
    "name": "current_bpm"
  },
  "rt": {
    "accepts_block": false,
    "args": [
      {
        "seconds": ":number"
      }
    ],
    "name": "rt",
    "introduced": "2,0,0",
    "hiden": false,
    "summary": "Real time conversion",
    "signature": {
      "t": null
    },
    "inline": true
  },
  "with_random_seed": {
    "accepts_block": true,
    "args": [
      {
        "seed": ":number"
      }
    ],
    "requires_block": true,
    "name": "with_random_seed",
    "introduced": "2,0,0",
    "hiden": false,
    "summary": "Specify random seed for code block",
    "signature": {
      "seed": null,
      "&block": null
    }
  },
  "on": {
    "accepts_block": true,
    "args": [
      {
        "condition": ":truthy"
      }
    ],
    "requires_block": true,
    "name": "on",
    "introduced": "2,10,0",
    "hiden": false,
    "returns": null,
    "summary": "Optionally evaluate block",
    "signature": {
      "condition": null,
      "&blk": null
    }
  },
  "use_bpm_mul": {
    "accepts_block": false,
    "args": [
      {
        "mul": ":number"
      }
    ],
    "name": "use_bpm_mul",
    "introduced": "2,3,0",
    "hiden": false,
    "summary": "Set new tempo as a multiple of current tempo",
    "signature": {
      "mul": null,
      "&block": null
    }
  },
  "puts": {
    "accepts_block": false,
    "args": [
      {
        "output": ":anything"
      }
    ],
    "name": "puts",
    "introduced": "2,0,0",
    "hiden": true,
    "intro_fn": true,
    "summary": "Display a message in the output pane",
    "signature": {
      "*msgs": null
    }
  },
  "with_bpm": {
    "accepts_block": true,
    "args": [
      {
        "bpm": ":number"
      }
    ],
    "requires_block": true,
    "name": "with_bpm",
    "introduced": "2,0,0",
    "hiden": false,
    "summary": "Set the tempo for the code block",
    "signature": {
      "bpm": null,
      "&block": null
    }
  },
  "use_cue_logging": {
    "accepts_block": false,
    "args": [
      {
        "true_or_false": ":boolean"
      }
    ],
    "name": "use_cue_logging",
    "introduced": "2,6,0",
    "hiden": false,
    "summary": "Enable and disable cue logging",
    "signature": {
      "v": null,
      "&block": null
    }
  },
  "assert_equal": {
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
    ],
    "name": "assert_equal",
    "introduced": "2,8,0",
    "hiden": true,
    "summary": "Ensure args are equal",
    "signature": {
      "msg": "nil",
      "arg1": null,
      "arg2": null
    }
  },
  "rdist": {
    "accepts_block": false,
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
    "name": "rdist",
    "introduced": "2,3,0",
    "hiden": false,
    "summary": "Random number in centred distribution",
    "signature": {
      "*opts": null,
      "centre": 0,
      "width": null
    },
    "inline": true
  },
  "assert": {
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
    ],
    "name": "assert",
    "introduced": "2,8,0",
    "hiden": true,
    "summary": "Ensure arg is valid",
    "signature": {
      "arg": null,
      "msg": "nil"
    }
  },
  "block_duration": {
    "accepts_block": true,
    "args": [],
    "requires_block": true,
    "async_block": false,
    "name": "block_duration",
    "introduced": "2,9,0",
    "hiden": false,
    "summary": "Return block duration",
    "signature": {
      "&block": null
    }
  },
  "print": {
    "accepts_block": false,
    "args": [
      {
        "output": ":anything"
      }
    ],
    "name": "print",
    "introduced": "2,0,0",
    "hiden": true,
    "intro_fn": true,
    "summary": "Display a message in the output pane",
    "signature": {
      "*msgs": null
    }
  },
  "with_tempo": {
    "hiden": true,
    "signature": {
      "*args": null,
      "&block": null
    }
  },
  "use_random_seed": {
    "accepts_block": false,
    "args": [
      {
        "seed": ":number"
      }
    ],
    "name": "use_random_seed",
    "introduced": "2,0,0",
    "hiden": false,
    "summary": "Set random seed generator to known seed",
    "signature": {
      "seed": null,
      "&block": null
    }
  },
  "rand_back": {
    "accepts_block": false,
    "args": [
      {
        "amount": ":number"
      }
    ],
    "name": "rand_back",
    "introduced": "2,7,0",
    "hiden": false,
    "summary": "Roll back random generator",
    "signature": {
      "amount": 1
    }
  },
  "rand_skip": {
    "accepts_block": false,
    "args": [
      {
        "amount": ":number"
      }
    ],
    "name": "rand_skip",
    "introduced": "2,7,0",
    "hiden": false,
    "summary": "Jump forward random generator",
    "signature": {
      "amount": 1
    }
  },
  "sleep": {
    "accepts_block": false,
    "args": [
      {
        "beats": ":number"
      }
    ],
    "name": "sleep",
    "introduced": "2,0,0",
    "hiden": false,
    "summary": "Wait for beat duration",
    "signature": {
      "beats": null
    },
    "advances_time": true
  },
  "reset": {
    "accepts_block": false,
    "args": [],
    "name": "reset",
    "introduced": "2,11,0",
    "hiden": false,
    "returns": null,
    "summary": "Reset all thread locals"
  },
  "look": {
    "accepts_block": false,
    "alt_args": [
      {
        "list": ":array"
      },
      {
        "key": ":symbol"
      }
    ],
    "opts": {
      "offset": 0
    },
    "name": "look",
    "introduced": "2,6,0",
    "hiden": false,
    "returns": ":number",
    "summary": "Obtain value of a tick",
    "signature": {
      "*args": null
    },
    "inline": true
  },
  "ring": {
    "accepts_block": false,
    "args": [
      {
        "list": ":array"
      }
    ],
    "name": "ring",
    "introduced": "2,2,0",
    "hiden": false,
    "returns": ":ring",
    "summary": "Create a ring buffer",
    "signature": {
      "*args": null
    },
    "inline": true
  },
  "sync": {
    "accepts_block": false,
    "args": [
      {
        "cue_id": ":symbol"
      }
    ],
    "opts": {
      "bpm_sync": false
    },
    "name": "sync",
    "introduced": "2,0,0",
    "hiden": false,
    "summary": "Sync with other threads",
    "signature": {
      "cue_ids": null,
      "opts": "{}"
    },
    "advances_time": true
  },
  "inc": {
    "accepts_block": false,
    "args": [
      {
        "n": ":number"
      }
    ],
    "opts": {},
    "name": "inc",
    "introduced": "2, 1, 0",
    "hiden": true,
    "summary": "Increment",
    "signature": {
      "n": null
    }
  },
  "tick": {
    "accepts_block": false,
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
    "opts": {
      "offset": 0,
      "step": 1
    },
    "name": "tick",
    "introduced": "2,6,0",
    "hiden": false,
    "returns": ":number",
    "summary": "Increment a tick and return value",
    "signature": {
      "*args": null
    },
    "inline": true
  },
  "tick_reset": {
    "accepts_block": false,
    "alt_args": [
      {
        "key": ":symbol"
      }
    ],
    "name": "tick_reset",
    "introduced": "2,6,0",
    "hiden": false,
    "returns": ":number",
    "summary": "Reset tick to 0",
    "signature": {
      "*args": null
    }
  },
  "spread": {
    "accepts_block": false,
    "args": [
      {
        "num_accents": ":number"
      },
      {
        "size": ":number"
      }
    ],
    "opts": {
      "rotate": false
    },
    "name": "spread",
    "introduced": "2,4,0",
    "hiden": false,
    "returns": ":ring",
    "summary": "Euclidean distribution for beats",
    "signature": {
      "num_accents": null,
      "size": null,
      "*args": null
    },
    "inline": true
  },
  "factor": {
    "accepts_block": false,
    "args": [
      {
        "val": ":number"
      },
      {
        "factor": ":number"
      }
    ],
    "name": "factor?",
    "introduced": "2,1,0",
    "hiden": false,
    "summary": "Factor test",
    "signature": {
      "val": null,
      "factor": null
    }
  },
  "at": {
    "accepts_block": true,
    "args": [
      {
        "times": ":list"
      },
      {
        "params": ":list"
      }
    ],
    "requires_block": true,
    "async_block": true,
    "name": "at",
    "introduced": "2,1,0",
    "hiden": false,
    "summary": "Asynchronous Time. Run a block at the given time(s)",
    "signature": {
      "times": 0,
      "params": "nil",
      "&block": null
    }
  },
  "rrand_i": {
    "accepts_block": false,
    "args": [
      {
        "min": ":number"
      },
      {
        "max": ":number"
      }
    ],
    "name": "rrand_i",
    "introduced": "2,0,0",
    "hiden": false,
    "summary": "Generate a random whole number between two points inclusively",
    "signature": {
      "min": null,
      "max": null
    },
    "inline": true
  },
  "spark": {
    "accepts_block": false,
    "name": "spark",
    "introduced": "2,5,0",
    "hiden": true,
    "summary": "Print a string representing a list of numeric values as a spark graph/bar chart",
    "signature": {
      "*values": null
    }
  },
  "quantise": {
    "accepts_block": false,
    "args": [
      {
        "n": ":number"
      },
      {
        "step": ":positive_number"
      }
    ],
    "name": "quantise",
    "introduced": "2,1,0",
    "hiden": false,
    "summary": "Quantise a value to resolution",
    "signature": {
      "n": null,
      "step": null
    },
    "inline": true
  },
  "live_loop": {
    "accepts_block": true,
    "args": [
      {
        "name": ":symbol"
      }
    ],
    "requires_block": true,
    "async_block": true,
    "opts": {
      "sync_bpm": ":foo",
      "seed": 0,
      "sync": ":foo",
      "init": "",
      "auto_cue": true,
      "delay": 0
    },
    "name": "live_loop",
    "introduced": "2,1,0",
    "hiden": false,
    "intro_fn": true,
    "summary": "A loop for live coding",
    "signature": {
      "*args": null,
      "&block": null,
      "name": "nil"
    }
  },
  "one_in": {
    "accepts_block": false,
    "args": [
      {
        "num": ":number"
      }
    ],
    "name": "one_in",
    "introduced": "2,0,0",
    "hiden": false,
    "summary": "Random true value with specified probability",
    "signature": {
      "num": null
    },
    "inline": true
  },
  "ramp": {
    "accepts_block": false,
    "args": [
      {
        "list": ":array"
      }
    ],
    "name": "ramp",
    "introduced": "2,6,0",
    "hiden": false,
    "returns": ":ramp",
    "summary": "Create a ramp vector",
    "signature": {
      "*args": null
    },
    "inline": true
  },
  "spark_graph": {
    "accepts_block": false,
    "name": "spark_graph",
    "introduced": "2,5,0",
    "hiden": true,
    "summary": "Returns a string representing a list of numeric values as a spark graph/bar chart",
    "signature": {
      "*values": null
    }
  },
  "define": {
    "accepts_block": true,
    "args": [
      {
        "name": ":symbol"
      }
    ],
    "requires_block": true,
    "name": "define",
    "introduced": "2,0,0",
    "hiden": false,
    "intro_fn": true,
    "summary": "Define a new function",
    "signature": {
      "&block": null,
      "name": null
    }
  },
  "choose": {
    "accepts_block": false,
    "args": [],
    "alt_args": [
      {
        "list": ":array"
      }
    ],
    "name": "choose",
    "introduced": "2,0,0",
    "hiden": false,
    "summary": "Random list selection",
    "signature": {
      "args": null
    },
    "inline": true
  },
  "load_buffer": {
    "accepts_block": false,
    "args": [
      {
        "path": ":string"
      }
    ],
    "name": "load_buffer",
    "introduced": "2,10,0",
    "hiden": false,
    "summary": "Load the contents of a file to the current buffer",
    "signature": {
      "path": null
    }
  },
  "rand_i_look": {
    "accepts_block": false,
    "args": [
      {
        "max": ":number_or_range"
      }
    ],
    "name": "rand_i_look",
    "introduced": "2,11,0",
    "hiden": false,
    "summary": "Generate a random whole number without consuming a rand",
    "signature": {
      "*args": null
    },
    "inline": true
  },
  "shuffle": {
    "accepts_block": false,
    "args": [],
    "alt_args": [
      {
        "list": ":array"
      }
    ],
    "name": "shuffle",
    "introduced": "2,1,0",
    "hiden": false,
    "summary": "Randomise order of a list",
    "signature": {
      "list": null
    },
    "inline": true
  },
  "with_bpm_mul": {
    "accepts_block": true,
    "args": [
      {
        "mul": ":number"
      }
    ],
    "requires_block": true,
    "name": "with_bpm_mul",
    "introduced": "2,3,0",
    "hiden": false,
    "summary": "Set new tempo as a multiple of current tempo for block",
    "signature": {
      "mul": null,
      "&block": null
    }
  },
  "stop": {
    "accepts_block": false,
    "name": "stop",
    "introduced": "2,5,0",
    "hiden": false,
    "returns": null,
    "summary": "Stop current thread or run"
  },
  "vt": {
    "accepts_block": false,
    "name": "vt",
    "introduced": "2,1,0",
    "hiden": false,
    "summary": "Get virtual time",
    "inline": true
  },
  "run_file": {
    "accepts_block": false,
    "args": [
      {
        "filename": ":path"
      }
    ],
    "name": "run_file",
    "introduced": "2,11,0",
    "hiden": false,
    "returns": null,
    "summary": "Evaluate the contents of the file as a new Run",
    "signature": {
      "path": null
    }
  },
  "doubles": {
    "accepts_block": false,
    "args": [
      {
        "start": ":number"
      },
      {
        "num_doubles": ":int"
      }
    ],
    "name": "doubles",
    "memoize": true,
    "introduced": "2,10,0",
    "hiden": false,
    "returns": ":ring",
    "summary": "Create a ring of successive doubles",
    "signature": {
      "num_doubles": 1,
      "start": null
    },
    "inline": true
  },
  "pick": {
    "accepts_block": false,
    "args": [
      {
        "n": ":number_or_nil"
      }
    ],
    "alt_args": [
      {
        "list": ":array"
      }
    ],
    "opts": {
      "skip": 0
    },
    "name": "pick",
    "introduced": "2,10,0",
    "hiden": false,
    "summary": "Randomly pick from list (with duplicates)",
    "signature": {
      "*args": null
    },
    "inline": true
  },
  "load_example": {
    "accepts_block": false,
    "args": [
      {
        "path": ":string"
      }
    ],
    "name": "load_example",
    "introduced": "2,10,0",
    "hiden": true,
    "summary": "Load a built-in example",
    "signature": {
      "example_name": null
    }
  },
  "current_beat_duration": {
    "introduced": "2,6,0",
    "accepts_block": false,
    "hiden": true,
    "summary": "Duration of current beat",
    "name": "current_beat_duration"
  },
  "block_slept": {
    "accepts_block": true,
    "args": [],
    "requires_block": true,
    "async_block": false,
    "name": "block_slept?",
    "introduced": "2,9,0",
    "hiden": false,
    "summary": "Determine if block contains sleep time",
    "signature": {
      "&block": null
    }
  },
  "tick_set": {
    "accepts_block": false,
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
    "name": "tick_set",
    "introduced": "2,6,0",
    "hiden": false,
    "returns": ":number",
    "summary": "Set tick to a specific value",
    "signature": {
      "*args": null
    }
  },
  "clear": {
    "accepts_block": false,
    "args": [],
    "name": "clear",
    "introduced": "2,11,0",
    "hiden": false,
    "returns": null,
    "summary": "Clear all thread locals to defaults"
  },
  "range": {
    "accepts_block": false,
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
    "opts": {
      "step": 1,
      "inclusive": false
    },
    "name": "range",
    "memoize": true,
    "introduced": "2,2,0",
    "hiden": false,
    "returns": ":ring",
    "summary": "Create a ring buffer with the specified start, finish and step size",
    "signature": {
      "*args": null,
      "finish": null,
      "start": null
    },
    "inline": true
  },
  "rand_i": {
    "accepts_block": false,
    "args": [
      {
        "max": ":number_or_range"
      }
    ],
    "name": "rand_i",
    "introduced": "2,0,0",
    "hiden": false,
    "summary": "Generate a random whole number below a value (exclusive)",
    "signature": {
      "max": 2
    },
    "inline": true
  },
  "comment": {
    "accepts_block": true,
    "requires_block": true,
    "name": "comment",
    "introduced": "2,0,0",
    "hiden": true,
    "summary": "Block level commenting",
    "signature": {
      "*args": null,
      "&block": null
    }
  },
  "run_code": {
    "accepts_block": false,
    "args": [
      {
        "code": ":string"
      }
    ],
    "name": "run_code",
    "introduced": "2,11,0",
    "hiden": false,
    "returns": null,
    "summary": "Evaluate the code passed as a String as a new Run",
    "signature": {
      "code": null
    }
  },
  "uncomment": {
    "accepts_block": true,
    "requires_block": true,
    "name": "uncomment",
    "introduced": "2,0,0",
    "hiden": true,
    "summary": "Block level comment ignoring",
    "signature": {
      "*args": null,
      "&block": null
    }
  },
  "with_cue_logging": {
    "accepts_block": true,
    "args": [
      {
        "true_or_false": ":boolean"
      }
    ],
    "requires_block": true,
    "name": "with_cue_logging",
    "introduced": "2,6,0",
    "hiden": false,
    "summary": "Block-level enable and disable cue logging",
    "signature": {
      "v": null,
      "&block": null
    }
  },
  "version": {
    "introduced": "2,0,0",
    "accepts_block": false,
    "hiden": true,
    "summary": "Get current version information",
    "name": "version"
  },
  "rand_reset": {
    "accepts_block": false,
    "args": [],
    "name": "rand_reset",
    "introduced": "2,7,0",
    "hiden": false,
    "summary": "Reset rand generator to last seed"
  },
  "dice": {
    "accepts_block": false,
    "args": [
      {
        "num_sides": ":number"
      }
    ],
    "name": "dice",
    "introduced": "2,0,0",
    "hiden": false,
    "summary": "Random dice throw",
    "signature": {
      "num_sides": 6
    },
    "inline": true
  },
  "halves": {
    "accepts_block": false,
    "args": [
      {
        "start": ":number"
      },
      {
        "num_halves": ":int"
      }
    ],
    "name": "halves",
    "memoize": true,
    "introduced": "2,10,0",
    "hiden": false,
    "returns": ":ring",
    "summary": "Create a ring of successive halves",
    "signature": {
      "num_halves": 1,
      "start": null
    },
    "inline": true
  },
  "in_thread": {
    "accepts_block": true,
    "requires_block": true,
    "async_block": true,
    "opts": {
      "sync": ":foo",
      "sync_bpm": ":foo",
      "name": ":foo",
      "delay": 0
    },
    "name": "in_thread",
    "introduced": "2,0,0",
    "hiden": false,
    "summary": "Run code block at the same time",
    "signature": {
      "&block": null,
      "*opts": null
    }
  },
  "dec": {
    "accepts_block": false,
    "args": [
      {
        "n": ":number"
      }
    ],
    "opts": {},
    "name": "dec",
    "introduced": "2, 1, 0",
    "hiden": true,
    "summary": "Decrement",
    "signature": {
      "n": null
    }
  },
  "time_shift": {
    "accepts_block": true,
    "args": [
      {
        "delta_time": ":number"
      }
    ],
    "requires_block": true,
    "name": "time_shift",
    "introduced": "2,11,0",
    "hiden": false,
    "returns": null,
    "summary": "Slide time forwards or backwards for the given block",
    "signature": {
      "delta": null,
      "&blk": null
    }
  },
  "line": {
    "accepts_block": false,
    "args": [
      {
        "start": ":number"
      },
      {
        "finish": ":number"
      }
    ],
    "opts": {
      "inclusive": false,
      "steps": 1
    },
    "name": "line",
    "memoize": true,
    "introduced": "2,5,0",
    "hiden": false,
    "returns": ":ring",
    "summary": "Create a ring buffer representing a straight line",
    "signature": {
      "*args": null,
      "finish": null,
      "start": null
    },
    "inline": true
  },
  "vector": {
    "accepts_block": false,
    "args": [
      {
        "list": ":array"
      }
    ],
    "name": "vector",
    "introduced": "2,6,0",
    "hiden": false,
    "returns": ":vector",
    "summary": "Create a vector",
    "signature": {
      "*args": null
    },
    "inline": true
  },
  "ndefine": {
    "accepts_block": true,
    "args": [
      {
        "name": ":symbol"
      }
    ],
    "requires_block": true,
    "name": "ndefine",
    "introduced": "2,1,0",
    "hiden": true,
    "summary": "Define a new function",
    "signature": {
      "&block": null,
      "name": null
    }
  },
  "use_bpm": {
    "accepts_block": false,
    "args": [
      {
        "bpm": ":number"
      }
    ],
    "name": "use_bpm",
    "introduced": "2,0,0",
    "hiden": false,
    "intro_fn": true,
    "summary": "Set the tempo",
    "signature": {
      "bpm": null,
      "&block": null
    }
  },
  "osc": {
    "hiden": true,
    "signature": {
      "*args": null,
      "path": null
    }
  },
  "beat": {
    "accepts_block": false,
    "args": [],
    "name": "beat",
    "introduced": "2,10,0",
    "hiden": true,
    "summary": "Get current beat"
  },
  "rrand": {
    "accepts_block": false,
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
    "name": "rrand",
    "introduced": "2,0,0",
    "hiden": false,
    "intro_fn": true,
    "summary": "Generate a random float between two numbers",
    "signature": {
      "min": null,
      "*opts": null,
      "max": null
    },
    "inline": true
  },
  "bools": {
    "accepts_block": false,
    "args": [
      {
        "list": ":array"
      }
    ],
    "name": "bools",
    "introduced": "2,2,0",
    "hiden": false,
    "returns": ":ring",
    "summary": "Create a ring of boolean values",
    "signature": {
      "*args": null
    },
    "inline": true
  },
  "sync_bpm": {
    "accepts_block": false,
    "args": [
      {
        "cue_id": ":symbol"
      }
    ],
    "opts": {},
    "name": "sync_bpm",
    "introduced": "2,10,0",
    "hiden": false,
    "summary": "Sync and inherit BPM from other threads ",
    "signature": {
      "cue_ids": null,
      "opts": "{}"
    },
    "advances_time": true
  },
  "rand": {
    "accepts_block": false,
    "args": [
      {
        "max": ":number_or_range"
      }
    ],
    "name": "rand",
    "introduced": "2,0,0",
    "hiden": false,
    "intro_fn": true,
    "summary": "Generate a random float below a value",
    "signature": {
      "max": 1
    },
    "inline": true
  },
  "knit": {
    "accepts_block": false,
    "args": [
      {
        "value": ":anything"
      },
      {
        "count": ":number"
      }
    ],
    "name": "knit",
    "introduced": "2,2,0",
    "hiden": false,
    "returns": ":ring",
    "summary": "Knit a sequence of repeated values",
    "signature": {
      "*args": null
    },
    "inline": true
  },
  "rand_look": {
    "accepts_block": false,
    "args": [
      {
        "max": ":number_or_range"
      }
    ],
    "name": "rand_look",
    "introduced": "2,11,0",
    "hiden": false,
    "summary": "Generate a random number without consuming a rand",
    "signature": {
      "*args": null
    },
    "inline": true
  },
  "use_osc": {
    "hiden": true,
    "signature": {
      "port": "nil",
      "host_or_port": null
    }
  },
  "current_random_seed": {
    "accepts_block": false,
    "name": "current_random_seed",
    "introduced": "2,10,0",
    "hiden": true,
    "intro_fn": true,
    "summary": "Get current random seed"
  },
  "stretch": {
    "accepts_block": false,
    "args": [
      {
        "count": ":int"
      }
    ],
    "alt_args": [
      {
        "list": ":array"
      }
    ],
    "name": "stretch",
    "introduced": "2,6,0",
    "hiden": false,
    "returns": ":ring",
    "summary": "Stretch a sequence of values",
    "signature": {
      "*args": null
    },
    "inline": true
  },
  "bt": {
    "accepts_block": false,
    "args": [
      {
        "seconds": ":number"
      }
    ],
    "name": "bt",
    "introduced": "2,8,0",
    "hiden": true,
    "summary": "Beat time conversion",
    "signature": {
      "t": null
    }
  },
  "tick_reset_all": {
    "accepts_block": false,
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
    "name": "tick_reset_all",
    "introduced": "2,6,0",
    "hiden": false,
    "returns": null,
    "summary": "Reset all ticks"
  },
  "density": {
    "accepts_block": true,
    "args": [
      {
        "d": ":density"
      }
    ],
    "requires_block": true,
    "async_block": true,
    "name": "density",
    "introduced": "2,3,0",
    "hiden": false,
    "summary": "Squash and repeat time",
    "signature": {
      "d": null,
      "&block": null
    }
  },
  "cue": {
    "accepts_block": false,
    "args": [
      {
        "cue_id": ":symbol"
      }
    ],
    "opts": {
      "another_key": "foo: 64",
      "your_key": ":bar",
      "key": "foo: 64"
    },
    "name": "cue",
    "introduced": "2,0,0",
    "hiden": false,
    "summary": "Cue other threads",
    "signature": {
      "cue_id": null,
      "*opts": null
    }
  }
}

#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/

lang_sound = {
  "note_info": {
    "accepts_block": false,
    "args": [
      {
        "note": ":symbol_or_number"
      }
    ],
    "opts": {
      "octave": 4
    },
    "name": "note_info",
    "introduced": "2,0,0",
    "hiden": true,
    "summary": "Get note info",
    "signature": {
      "n": null,
      "*args": null
    }
  },
  "rest": {
    "accepts_block": false,
    "args": [
      {
        "note_or_args": ":number_symbol_or_map"
      }
    ],
    "name": "rest?",
    "introduced": "2,1,0",
    "hiden": false,
    "summary": "Determine if note or args is a rest",
    "signature": {
      "n": null
    }
  },
  "note": {
    "accepts_block": false,
    "args": [
      {
        "note": ":symbol_or_number"
      }
    ],
    "opts": {
      "octave": 4
    },
    "name": "note",
    "introduced": "2,0,0",
    "hiden": false,
    "summary": "Describe note",
    "signature": {
      "n": null,
      "*args": null
    },
    "inline": true
  },
  "recording_save": {
    "accepts_block": false,
    "args": [
      {
        "path": ":string"
      }
    ],
    "name": "recording_save",
    "introduced": "2,0,0",
    "hiden": true,
    "summary": "Save recording",
    "signature": {
      "filename": null
    }
  },
  "set_control_delta": {
    "accepts_block": false,
    "args": [
      {
        "time": ":number"
      }
    ],
    "name": "set_control_delta!",
    "introduced": "2,1,0",
    "hiden": false,
    "summary": "Set control delta globally",
    "signature": {
      "t": null
    },
    "modifies_env": true
  },
  "reset_mixer": {
    "accepts_block": false,
    "opts": {},
    "name": "reset_mixer!",
    "introduced": "2,9,0",
    "hiden": false,
    "summary": "Reset master mixer",
    "signature": {
      "": null
    },
    "modifies_env": true
  },
  "set_mixer_invert_stereo!": {
    "hiden": false
  },
  "play_chord": {
    "accepts_block": false,
    "args": [
      {
        "notes": ":list"
      }
    ],
    "opts": {
      "pitch": 0,
      "attack": 0,
      "pan": 0,
      "amp_slide": 1,
      "amp": 1,
      "on": 1,
      "release": 0,
      "sustain": 1,
      "env_curve": 1,
      "decay_level": 1,
      "pan_slide": 1,
      "attack_level": 1,
      "sustain_level": 1,
      "slide": 0,
      "decay": 0
    },
    "name": "play_chord",
    "introduced": "2,0,0",
    "hiden": false,
    "summary": "Play notes simultaneously",
    "signature": {
      "notes": null,
      "*args": null
    }
  },
  "chord_degree": {
    "accepts_block": false,
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
    "name": "chord_degree",
    "memoize": true,
    "introduced": "2,1,0",
    "hiden": false,
    "returns": ":ring",
    "summary": "Construct chords of stacked thirds, based on scale degrees",
    "signature": {
      "degree": null,
      "tonic": null,
      "number_of_notes": 4,
      "*opts": null,
      "scale": ":major"
    },
    "inline": true
  },
  "with_transpose": {
    "accepts_block": true,
    "args": [
      {
        "note_shift": ":number"
      }
    ],
    "requires_block": true,
    "name": "with_transpose",
    "introduced": "2,0,0",
    "hiden": false,
    "summary": "Block-level note transposition",
    "signature": {
      "shift": null,
      "&block": null
    }
  },
  "with_arg_bpm_scaling": {
    "accepts_block": true,
    "requires_block": true,
    "name": "with_arg_bpm_scaling",
    "introduced": "2,0,0",
    "hiden": false,
    "summary": "Block-level enable and disable BPM scaling",
    "signature": {
      "&block": null,
      "bool": null
    }
  },
  "load_sample_at_path": {
    "hiden": false,
    "signature": {
      "path": null
    }
  },
  "current_amp": {
    "hiden": true
  },
  "use_synth": {
    "accepts_block": false,
    "args": [
      {
        "synth_name": ":symbol"
      }
    ],
    "name": "use_synth",
    "introduced": "2,0,0",
    "hiden": false,
    "intro_fn": true,
    "summary": "Switch current synth",
    "signature": {
      "*args": null,
      "synth_name": null,
      "&block": null
    }
  },
  "pitch_ratio": {
    "hiden": true,
    "signature": {
      "*args": null
    }
  },
  "current_debug": {
    "introduced": "2,0,0",
    "accepts_block": false,
    "hiden": true,
    "summary": "Get current debug status",
    "name": "current_debug"
  },
  "use_cent_tuning": {
    "accepts_block": false,
    "args": [
      {
        "cent_shift": ":number"
      }
    ],
    "name": "use_cent_tuning",
    "introduced": "2,9,0",
    "hiden": false,
    "intro_fn": true,
    "summary": "Cent tuning",
    "signature": {
      "shift": null,
      "&block": null
    }
  },
  "control": {
    "accepts_block": false,
    "args": [
      {
        "node": ":synth_node"
      }
    ],
    "opts": {},
    "name": "control",
    "introduced": "2,0,0",
    "hiden": false,
    "summary": "Control running synth",
    "signature": {
      "*args": null
    }
  },
  "use_sample_bpm": {
    "accepts_block": false,
    "args": [
      {
        "string_or_number": ":sample_name_or_duration"
      }
    ],
    "opts": {
      "num_beats": 1
    },
    "name": "use_sample_bpm",
    "introduced": "2,1,0",
    "hiden": false,
    "summary": "Sample-duration-based bpm modification",
    "signature": {
      "*args": null,
      "sample_name": null
    }
  },
  "hz_to_midi": {
    "accepts_block": false,
    "args": [
      {
        "freq": ":number"
      }
    ],
    "name": "hz_to_midi",
    "introduced": "2,0,0",
    "hiden": false,
    "summary": "Hz to MIDI conversion",
    "signature": {
      "freq": null
    },
    "inline": true
  },
  "recording_stop": {
    "introduced": "2,0,0",
    "accepts_block": false,
    "hiden": true,
    "summary": "Stop recording",
    "name": "recording_stop"
  },
  "use_octave": {
    "accepts_block": false,
    "args": [
      {
        "octave_shift": ":number"
      }
    ],
    "name": "use_octave",
    "introduced": "2,9,0",
    "hiden": false,
    "intro_fn": true,
    "summary": "Note octave transposition",
    "signature": {
      "shift": null,
      "&block": null
    }
  },
  "set_mixer_mono_mode!": {
    "hiden": false
  },
  "recording_delete": {
    "accepts_block": false,
    "hiden": true,
    "name": "recording_delete"
  },
  "with_merged_sample_defaults": {
    "accepts_block": true,
    "requires_block": true,
    "opts": {},
    "name": "with_merged_sample_defaults",
    "introduced": "2,9,0",
    "hiden": false,
    "summary": "Block-level use merged sample defaults",
    "signature": {
      "*args": null,
      "&block": null
    }
  },
  "current_arg_checks": {
    "introduced": "2,0,0",
    "accepts_block": false,
    "hiden": true,
    "summary": "Get current arg checking status",
    "name": "current_arg_checks"
  },
  "sample_duration": {
    "accepts_block": false,
    "args": [
      {
        "path": ":string"
      }
    ],
    "opts": {
      "sustain": 1,
      "decay": 0,
      "pitch_stretch": 1,
      "start": 0,
      "beat_stretch": 1,
      "rpitch": 0,
      "finish": 1,
      "release": 0,
      "rate": 1,
      "attack": 0
    },
    "name": "sample_duration",
    "introduced": "2,0,0",
    "hiden": true,
    "summary": "Get duration of sample in beats",
    "signature": {
      "*args": null
    }
  },
  "recording_start": {
    "introduced": "2,0,0",
    "accepts_block": false,
    "hiden": true,
    "summary": "Start recording",
    "name": "recording_start"
  },
  "sample_split_filts_and_opts": {
    "hiden": true,
    "signature": {
      "args": null
    }
  },
  "set_mixer_stereo_mode!": {
    "hiden": false
  },
  "with_timing_warnings": {
    "hiden": true,
    "signature": {
      "v": null,
      "&block": null
    }
  },
  "use_external_synths": {
    "hiden": true,
    "signature": {
      "v": null,
      "&block": null
    }
  },
  "play_pattern": {
    "accepts_block": false,
    "args": [
      {
        "notes": ":list"
      }
    ],
    "opts": {},
    "name": "play_pattern",
    "introduced": "2,0,0",
    "hiden": false,
    "summary": "Play pattern of notes",
    "signature": {
      "notes": null,
      "*args": null
    }
  },
  "current_synth": {
    "introduced": "2,0,0",
    "accepts_block": false,
    "hiden": true,
    "summary": "Get current synth",
    "name": "current_synth"
  },
  "sample_buffer": {
    "accepts_block": false,
    "args": [
      {
        "path": ":string"
      }
    ],
    "name": "sample_buffer",
    "introduced": "2,0,0",
    "hiden": true,
    "summary": "Get sample data",
    "signature": {
      "*args": null
    }
  },
  "kill": {
    "accepts_block": false,
    "args": [
      {
        "node": ":synth_node"
      }
    ],
    "opts": {},
    "name": "kill",
    "introduced": "2,0,0",
    "hiden": false,
    "summary": "Kill synth",
    "signature": {
      "node": null
    }
  },
  "use_tuning": {
    "accepts_block": false,
    "args": [
      {
        "tuning": ":symbol"
      },
      {
        "fundamental_note": ":symbol_or_number"
      }
    ],
    "name": "use_tuning",
    "introduced": "2,6,0",
    "hiden": false,
    "summary": "Use alternative tuning systems",
    "signature": {
      "tuning": null,
      "fundamental_note": ":c",
      "&block": null
    }
  },
  "with_octave": {
    "accepts_block": true,
    "args": [
      {
        "octave_shift": ":number"
      }
    ],
    "requires_block": true,
    "name": "with_octave",
    "introduced": "2,9,0",
    "hiden": false,
    "intro_fn": true,
    "summary": "Block level octave transposition",
    "signature": {
      "shift": null,
      "&block": null
    }
  },
  "ratio_to_pitch": {
    "accepts_block": false,
    "args": [
      {
        "ratio": ":number"
      }
    ],
    "name": "ratio_to_pitch",
    "introduced": "2,7,0",
    "hiden": false,
    "summary": "relative frequency ratio to MIDI pitch",
    "signature": {
      "r": null
    },
    "inline": true
  },
  "chord_invert": {
    "accepts_block": false,
    "args": [
      {
        "notes": ":list"
      },
      {
        "shift": ":number"
      }
    ],
    "name": "chord_invert",
    "introduced": "2,6,0",
    "hiden": false,
    "returns": ":ring",
    "summary": "Chord inversion",
    "signature": {
      "notes": null,
      "shift": null
    },
    "inline": true
  },
  "use_merged_synth_defaults": {
    "accepts_block": false,
    "opts": {},
    "name": "use_merged_synth_defaults",
    "introduced": "2,0,0",
    "hiden": false,
    "summary": "Merge synth defaults",
    "signature": {
      "*args": null,
      "&block": null
    }
  },
  "resolve_sample_paths": {
    "hiden": true,
    "signature": {
      "filts_and_sources": null
    }
  },
  "sample_loaded": {
    "accepts_block": false,
    "args": [
      {
        "path": ":string"
      }
    ],
    "name": "sample_loaded?",
    "introduced": "2,2,0",
    "hiden": false,
    "summary": "Test if sample was pre-loaded",
    "signature": {
      "*args": null
    }
  },
  "set_cent_tuning": {
    "accepts_block": false,
    "args": [
      {
        "cent_shift": ":number"
      }
    ],
    "name": "set_cent_tuning!",
    "introduced": "2,10,0",
    "hiden": false,
    "intro_fn": false,
    "summary": "Global Cent tuning",
    "signature": {
      "shift": null
    },
    "modifies_env": true
  },
  "use_transpose": {
    "accepts_block": false,
    "args": [
      {
        "note_shift": ":number"
      }
    ],
    "name": "use_transpose",
    "introduced": "2,0,0",
    "hiden": false,
    "intro_fn": true,
    "summary": "Note transposition",
    "signature": {
      "shift": null,
      "&block": null
    }
  },
  "load_samples": {
    "accepts_block": false,
    "args": [
      {
        "paths": ":list"
      }
    ],
    "name": "load_samples",
    "introduced": "2,0,0",
    "hiden": false,
    "summary": "Pre-load all matching samples",
    "signature": {
      "*args": null
    }
  },
  "note_range": {
    "accepts_block": false,
    "args": [
      {
        "low_note": ":note"
      },
      {
        "high_note": ":note"
      }
    ],
    "opts": {
      "pitches": []
    },
    "name": "note_range",
    "introduced": "2,6,0",
    "hiden": false,
    "returns": ":ring",
    "summary": "Get a range of notes",
    "signature": {
      "high_note": null,
      "*opts": null,
      "low_note": null
    },
    "inline": true
  },
  "current_sched_ahead_time": {
    "introduced": "2,0,0",
    "accepts_block": false,
    "hiden": true,
    "summary": "Get current sched ahead time",
    "name": "current_sched_ahead_time"
  },
  "use_timing_warnings": {
    "hiden": true,
    "signature": {
      "v": null,
      "&block": null
    }
  },
  "current_sample_defaults": {
    "introduced": "2,5,0",
    "accepts_block": false,
    "hiden": true,
    "summary": "Get current sample defaults",
    "name": "current_sample_defaults"
  },
  "with_synth": {
    "accepts_block": true,
    "args": [
      {
        "synth_name": ":symbol"
      }
    ],
    "requires_block": true,
    "name": "with_synth",
    "introduced": "2,0,0",
    "hiden": false,
    "summary": "Block-level synth switching",
    "signature": {
      "*args": null,
      "synth_name": null,
      "&block": null
    }
  },
  "use_arg_checks": {
    "accepts_block": false,
    "args": [
      {
        "true_or_false": ":boolean"
      }
    ],
    "name": "use_arg_checks",
    "introduced": "2,0,0",
    "hiden": false,
    "summary": "Enable and disable arg checks",
    "signature": {
      "v": null,
      "&block": null
    }
  },
  "truthy": {
    "hiden": false,
    "signature": {
      "val": null
    }
  },
  "use_fx": {
    "hiden": true,
    "signature": {
      "*args": null,
      "&block": null
    }
  },
  "sample_info": {
    "accepts_block": false,
    "args": [
      {
        "path": ":string"
      }
    ],
    "name": "sample_info",
    "introduced": "2,0,0",
    "hiden": true,
    "summary": "Get sample information",
    "signature": {
      "*args": null
    }
  },
  "current_volume": {
    "introduced": "2,0,0",
    "accepts_block": false,
    "hiden": true,
    "summary": "Get current volume",
    "name": "current_volume"
  },
  "set_mixer_control": {
    "accepts_block": false,
    "opts": {
      "limiter_bypass": 0,
      "lpf_bypass": 0,
      "leak_dc_bypass": 0,
      "amp": 1,
      "pre_amp": 1,
      "hpf_bypass": 0,
      "hpf": 0,
      "lpf": 131
    },
    "name": "set_mixer_control!",
    "introduced": "2,7,0",
    "hiden": false,
    "summary": "Control master mixer",
    "signature": {
      "opts": null
    },
    "modifies_env": true
  },
  "with_tuning": {
    "accepts_block": true,
    "args": [
      {
        "tuning": ":symbol"
      },
      {
        "fundamental_note": ":symbol_or_number"
      }
    ],
    "requires_block": true,
    "name": "with_tuning",
    "introduced": "2,6,0",
    "hiden": false,
    "summary": "Block-level tuning modification",
    "signature": {
      "tuning": null,
      "fundamental_note": ":c",
      "&block": null
    }
  },
  "current_synth_defaults": {
    "introduced": "2,0,0",
    "accepts_block": false,
    "hiden": true,
    "summary": "Get current synth defaults",
    "name": "current_synth_defaults"
  },
  "sample": {
    "accepts_block": true,
    "args": [
      {
        "name_or_path": ":symbol_or_string"
      }
    ],
    "requires_block": false,
    "async_block": true,
    "opts": {
      "pitch": 0,
      "rpitch": 0,
      "finish": 1,
      "path": "/path/to/file",
      "release": 0,
      "pitch_dis": 0,
      "sustain": 1,
      "lpf_attack_level": 0,
      "hpf": 0,
      "hpf_env_curve": 1,
      "lpf_env_curve": 1,
      "pre_amp": 1,
      "compress": 0,
      "lpf_release_level": 0,
      "lpf_release": 0,
      "relax_time": 0,
      "pitch_stretch": 1,
      "start": 0,
      "pan": 0,
      "hpf_sustain": 0,
      "lpf_decay": 0,
      "hpf_attack": 0,
      "norm": 0,
      "lpf_min": 30,
      "lpf_init_level": 30,
      "hpf_decay_level": 0,
      "beat_stretch": 1,
      "lpf_attack": 0,
      "hpf_sustain_level": 0,
      "amp": 1,
      "window_size": 0,
      "lpf_sustain_level": 0,
      "onset": 0,
      "slide": 0,
      "hpf_attack_level": 0,
      "slope_below": 1,
      "clamp_time": 0,
      "lpf_sustain": 0,
      "attack": 0,
      "lpf_decay_level": 0,
      "hpf_init_level": 130,
      "hpf_decay": 0,
      "hpf_release": 0,
      "hpf_release_level": 0,
      "slope_above": 1,
      "hpf_max": 200,
      "lpf": 131,
      "time_dis": 0,
      "rate": 1,
      "threshold": 0
    },
    "name": "sample",
    "introduced": "2,0,0",
    "hiden": false,
    "intro_fn": true,
    "summary": "Trigger sample",
    "signature": {
      "*args": null,
      "&blk": null
    }
  },
  "load_sample": {
    "accepts_block": false,
    "args": [
      {
        "path": ":string"
      }
    ],
    "name": "load_sample",
    "introduced": "2,0,0",
    "hiden": false,
    "summary": "Pre-load first matching sample",
    "signature": {
      "*args": null
    }
  },
  "scale": {
    "args": [
      {
        "tonic": ":symbol"
      },
      {
        "name": ":symbol"
      }
    ],
    "opts": {
      "num_octaves": 1
    },
    "intro_fn": true,
    "signature": {
      "*opts": null,
      "tonic_or_name": null
    },
    "inline": true,
    "accepts_block": false,
    "memoize": true,
    "name": "scale",
    "introduced": "2,0,0",
    "hiden": false,
    "returns": ":ring",
    "summary": "Create scale"
  },
  "degree": {
    "accepts_block": false,
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
    "name": "degree",
    "introduced": "2,1,0",
    "hiden": false,
    "summary": "Convert a degree into a note",
    "signature": {
      "degree": null,
      "tonic": null,
      "scale": null
    },
    "inline": true
  },
  "with_sample_bpm": {
    "accepts_block": true,
    "args": [
      {
        "string_or_number": ":sample_name_or_duration"
      }
    ],
    "requires_block": true,
    "opts": {
      "num_beats": 1
    },
    "name": "with_sample_bpm",
    "introduced": "2,1,0",
    "hiden": false,
    "summary": "Block-scoped sample-duration-based bpm modification",
    "signature": {
      "*args": null,
      "&block": null,
      "sample_name": null
    }
  },
  "pitch_to_ratio": {
    "accepts_block": false,
    "args": [
      {
        "pitch": ":midi_number"
      }
    ],
    "name": "pitch_to_ratio",
    "introduced": "2,5,0",
    "hiden": false,
    "summary": "relative MIDI pitch to frequency ratio",
    "signature": {
      "m": null
    },
    "inline": true
  },
  "use_timing_guarantees": {
    "accepts_block": false,
    "args": [
      {
        "bool": ":true_or_false"
      }
    ],
    "requires_block": false,
    "name": "use_timing_guarantees",
    "introduced": "2,10,0",
    "hiden": false,
    "summary": "Inhibit synth triggers if too late",
    "signature": {
      "v": null,
      "&block": null
    }
  },
  "invert_chord": {
    "hiden": true,
    "signature": {
      "*args": null
    }
  },
  "sample_groups": {
    "accepts_block": false,
    "memoize": true,
    "name": "sample_groups",
    "introduced": "2,0,0",
    "hiden": true,
    "summary": "Get all sample groups"
  },
  "use_merged_sample_defaults": {
    "accepts_block": false,
    "opts": {},
    "name": "use_merged_sample_defaults",
    "introduced": "2,9,0",
    "hiden": false,
    "summary": "Merge new sample defaults",
    "signature": {
      "*args": null,
      "&block": null
    }
  },
  "sample_free": {
    "accepts_block": false,
    "args": [
      {
        "path": ":string"
      }
    ],
    "name": "sample_free",
    "introduced": "2,9,0",
    "hiden": false,
    "returns": null,
    "summary": "Free a sample on the synth server",
    "signature": {
      "*paths": null
    }
  },
  "should_trigger": {
    "hiden": false,
    "signature": {
      "args_h": null
    }
  },
  "with_fx": {
    "accepts_block": true,
    "args": [
      {
        "fx_name": ":symbol"
      }
    ],
    "requires_block": true,
    "async_block": true,
    "opts": {
      "kill_delay": 1,
      "reps": 1
    },
    "name": "with_fx",
    "introduced": "2,0,0",
    "hiden": false,
    "intro_fn": true,
    "summary": "Use Studio FX",
    "signature": {
      "*args": null,
      "&block": null,
      "fx_name": null
    }
  },
  "sample_free_all": {
    "accepts_block": false,
    "args": [],
    "name": "sample_free_all",
    "introduced": "2,9,0",
    "hiden": false,
    "returns": null,
    "summary": "Free all loaded samples on the synth server"
  },
  "fx_names": {
    "accepts_block": false,
    "memoize": true,
    "name": "fx_names",
    "introduced": "2,10,0",
    "hiden": true,
    "summary": "Get all FX names"
  },
  "scale_names": {
    "accepts_block": false,
    "memoize": true,
    "name": "scale_names",
    "introduced": "2,6,0",
    "hiden": true,
    "summary": "All scale names"
  },
  "all_sample_names": {
    "accepts_block": false,
    "memoize": true,
    "name": "all_sample_names",
    "introduced": "2,0,0",
    "hiden": true,
    "summary": "Get all sample names"
  },
  "with_arg_checks": {
    "accepts_block": true,
    "args": [
      {
        "true_or_false": ":boolean"
      }
    ],
    "requires_block": true,
    "name": "with_arg_checks",
    "introduced": "2,0,0",
    "hiden": false,
    "summary": "Block-level enable and disable arg checks",
    "signature": {
      "v": null,
      "&block": null
    }
  },
  "synth_names": {
    "accepts_block": false,
    "memoize": true,
    "name": "synth_names",
    "introduced": "2,9,0",
    "hiden": true,
    "summary": "Get all synth names"
  },
  "current_octave": {
    "introduced": "2,9,0",
    "accepts_block": false,
    "hiden": true,
    "summary": "Get current octave shift",
    "name": "current_octave"
  },
  "with_debug": {
    "accepts_block": true,
    "args": [
      {
        "true_or_false": ":boolean"
      }
    ],
    "requires_block": true,
    "name": "with_debug",
    "introduced": "2,0,0",
    "hiden": false,
    "summary": "Block-level enable and disable debug",
    "signature": {
      "v": null,
      "&block": null
    }
  },
  "start_amp_monitor": {
    "hiden": true
  },
  "with_sample_defaults": {
    "accepts_block": true,
    "requires_block": true,
    "opts": {},
    "name": "with_sample_defaults",
    "introduced": "2,5,0",
    "hiden": false,
    "summary": "Block-level use new sample defaults",
    "signature": {
      "*args": null,
      "&block": null
    }
  },
  "use_arg_bpm_scaling": {
    "accepts_block": false,
    "args": [
      {
        "bool": ":boolean"
      }
    ],
    "name": "use_arg_bpm_scaling",
    "introduced": "2,0,0",
    "hiden": false,
    "summary": "Enable and disable BPM scaling",
    "signature": {
      "&block": null,
      "bool": null
    }
  },
  "with_timing_guarantees": {
    "accepts_block": true,
    "args": [
      {
        "bool": ":true_or_false"
      }
    ],
    "requires_block": true,
    "name": "with_timing_guarantees",
    "introduced": "2,10,0",
    "hiden": false,
    "summary": "Block-scoped inhibition of synth triggers if too late",
    "signature": {
      "v": null,
      "&block": null
    }
  },
  "set_mixer_standard_stereo!": {
    "hiden": false
  },
  "status": {
    "introduced": "2,0,0",
    "accepts_block": false,
    "hiden": true,
    "summary": "Get server status",
    "name": "status"
  },
  "chord": {
    "args": [
      {
        "tonic": ":symbol"
      },
      {
        "name": ":symbol"
      }
    ],
    "opts": {
      "num_octaves": 1,
      "invert": 0
    },
    "intro_fn": true,
    "signature": {
      "*opts": null,
      "tonic_or_name": null
    },
    "inline": true,
    "accepts_block": false,
    "memoize": true,
    "name": "chord",
    "introduced": "2,0,0",
    "hiden": false,
    "returns": ":ring",
    "summary": "Create chord"
  },
  "current_cent_tuning": {
    "introduced": "2,9,0",
    "accepts_block": false,
    "hiden": true,
    "summary": "Get current cent shift",
    "name": "current_cent_tuning"
  },
  "chord_names": {
    "accepts_block": false,
    "memoize": true,
    "name": "chord_names",
    "introduced": "2,6,0",
    "hiden": true,
    "summary": "All chord names"
  },
  "with_synth_defaults": {
    "accepts_block": true,
    "requires_block": true,
    "opts": {},
    "name": "with_synth_defaults",
    "introduced": "2,0,0",
    "hiden": false,
    "summary": "Block-level use new synth defaults",
    "signature": {
      "*args": null,
      "&block": null
    }
  },
  "resolve_sample_path": {
    "hiden": true,
    "signature": {
      "filts_and_sources": null
    }
  },
  "load_synthdefs": {
    "accepts_block": false,
    "args": [
      {
        "path": ":string"
      }
    ],
    "name": "load_synthdefs",
    "introduced": "2,0,0",
    "hiden": true,
    "summary": "Load external synthdefs",
    "signature": {
      "path": "synthdef_path"
    }
  },
  "midi_to_hz": {
    "accepts_block": false,
    "args": [
      {
        "note": ":symbol_or_number"
      }
    ],
    "name": "midi_to_hz",
    "introduced": "2,0,0",
    "hiden": false,
    "summary": "MIDI to Hz conversion",
    "signature": {
      "n": null
    },
    "inline": true
  },
  "sample_names": {
    "accepts_block": false,
    "args": [
      {
        "group": ":symbol"
      }
    ],
    "name": "sample_names",
    "memoize": true,
    "introduced": "2,0,0",
    "hiden": true,
    "returns": ":ring",
    "summary": "Get sample names",
    "signature": {
      "group": null
    }
  },
  "use_sample_defaults": {
    "accepts_block": false,
    "opts": {},
    "name": "use_sample_defaults",
    "introduced": "2,5,0",
    "hiden": false,
    "summary": "Use new sample defaults",
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
  "synth": {
    "accepts_block": true,
    "args": [
      {
        "synth_name": ":symbol"
      }
    ],
    "requires_block": false,
    "async_block": true,
    "opts": {
      "pitch": 0,
      "attack": 0,
      "pan": 0,
      "amp_slide": 1,
      "amp": 1,
      "on": 1,
      "release": 0,
      "sustain": 1,
      "env_curve": 1,
      "decay_level": 1,
      "pan_slide": 1,
      "attack_level": 1,
      "sustain_level": 1,
      "slide": 0,
      "decay": 0
    },
    "name": "synth",
    "introduced": "2,0,0",
    "hiden": false,
    "intro_fn": true,
    "summary": "Trigger specific synth",
    "signature": {
      "*args": null,
      "synth_name": null,
      "&blk": null
    }
  },
  "set_sched_ahead_time": {
    "accepts_block": false,
    "args": [
      {
        "time": ":number"
      }
    ],
    "name": "set_sched_ahead_time!",
    "introduced": "2,0,0",
    "hiden": false,
    "summary": "Set sched ahead time globally",
    "signature": {
      "t": null
    },
    "modifies_env": true
  },
  "with_cent_tuning": {
    "accepts_block": true,
    "args": [
      {
        "cent_shift": ":number"
      }
    ],
    "requires_block": true,
    "name": "with_cent_tuning",
    "introduced": "2,9,0",
    "hiden": false,
    "summary": "Block-level cent tuning",
    "signature": {
      "shift": null,
      "&block": null
    }
  },
  "current_transpose": {
    "introduced": "2,0,0",
    "accepts_block": false,
    "hiden": true,
    "summary": "Get current transposition",
    "name": "current_transpose"
  },
  "sample_paths": {
    "accepts_block": false,
    "args": [
      {
        "pre_args": ":source_and_filter_types"
      }
    ],
    "name": "sample_paths",
    "introduced": "2,10,0",
    "hiden": true,
    "returns": ":ring",
    "summary": "Sample Pack Filter Resolution",
    "signature": {
      "*args": null
    }
  },
  "use_debug": {
    "accepts_block": false,
    "args": [
      {
        "true_or_false": ":boolean"
      }
    ],
    "name": "use_debug",
    "introduced": "2,0,0",
    "hiden": false,
    "summary": "Enable and disable debug",
    "signature": {
      "v": null,
      "&block": null
    }
  },
  "play": {
    "accepts_block": true,
    "args": [
      {
        "note": ":symbol_or_number"
      }
    ],
    "requires_block": false,
    "async_block": true,
    "opts": {
      "pitch": 0,
      "attack": 0,
      "pan": 0,
      "amp_slide": 1,
      "amp": 1,
      "on": 1,
      "release": 0,
      "sustain": 1,
      "env_curve": 1,
      "decay_level": 1,
      "pan_slide": 1,
      "attack_level": 1,
      "sustain_level": 1,
      "slide": 0,
      "decay": 0
    },
    "name": "play",
    "introduced": "2,0,0",
    "hiden": false,
    "intro_fn": true,
    "summary": "Play current synth",
    "signature": {
      "n": null,
      "*args": null,
      "&blk": null
    }
  },
  "set_volume": {
    "accepts_block": false,
    "args": [
      {
        "vol": ":number"
      }
    ],
    "name": "set_volume!",
    "introduced": "2,0,0",
    "hiden": false,
    "summary": "Set Volume globally",
    "signature": {
      "vol": null
    },
    "modifies_env": true
  },
  "midi_notes": {
    "accepts_block": false,
    "args": [
      {
        "list": ":array"
      }
    ],
    "name": "midi_notes",
    "memoize": true,
    "introduced": "2,7,0",
    "hiden": false,
    "returns": ":ring",
    "summary": "Create a ring buffer of midi note numbers",
    "signature": {
      "*args": null
    },
    "inline": true
  },
  "use_synth_defaults": {
    "accepts_block": false,
    "opts": {},
    "name": "use_synth_defaults",
    "introduced": "2,0,0",
    "hiden": false,
    "summary": "Use new synth defaults",
    "signature": {
      "*args": null,
      "&block": null
    }
  },
  "play_pattern_timed": {
    "accepts_block": false,
    "args": [
      {
        "notes": ":list"
      },
      {
        "times": ":list_or_number"
      }
    ],
    "opts": {
      "pitch": 0,
      "attack": 0,
      "pan": 0,
      "amp_slide": 1,
      "amp": 1,
      "on": 1,
      "release": 0,
      "sustain": 1,
      "env_curve": 1,
      "decay_level": 1,
      "pan_slide": 1,
      "attack_level": 1,
      "sustain_level": 1,
      "slide": 0,
      "decay": 0
    },
    "name": "play_pattern_timed",
    "introduced": "2,0,0",
    "hiden": false,
    "summary": "Play pattern of notes with specific times",
    "signature": {
      "notes": null,
      "times": null,
      "*args": null
    }
  },
  "with_merged_synth_defaults": {
    "accepts_block": true,
    "requires_block": true,
    "opts": {},
    "name": "with_merged_synth_defaults",
    "introduced": "2,0,0",
    "hiden": false,
    "summary": "Block-level merge synth defaults",
    "signature": {
      "*args": null,
      "&block": null
    }
  },
  "octs": {
    "accepts_block": false,
    "args": [
      {
        "start": ":note"
      },
      {
        "num_octaves": ":pos_int"
      }
    ],
    "name": "octs",
    "introduced": "2,8,0",
    "hiden": false,
    "returns": ":ring",
    "summary": "Create a ring of octaves",
    "signature": {
      "num_octs": 1,
      "start": null
    },
    "inline": true
  }
}

sound_args_types_conversion = {}

sound_opts_types_conversion = {}

#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/

synths = {
  "SubPulse": {
    "opts": {
      "cutoff_slide_curve": 0,
      "decay": 0,
      "amp_slide_shape": 1,
      "amp": 1,
      "cutoff_slide_shape": 1,
      "release": 1,
      "sub_amp_slide": 0,
      "sub_detune_slide_shape": 1,
      "sustain": 0,
      "pulse_width_slide": 0,
      "pan_slide_shape": 1,
      "decay_level": 1,
      "note": 52,
      "pan_slide": 0,
      "sub_detune": -12,
      "cutoff_slide": 0,
      "note_slide_shape": 1,
      "sub_amp": 1,
      "pulse_width_slide_shape": 1,
      "attack": 0,
      "pan": 0,
      "cutoff": 100,
      "sub_amp_slide_shape": 1,
      "amp_slide": 0,
      "sub_amp_slide_curve": 0,
      "amp_slide_curve": 0,
      "env_curve": 2,
      "pan_slide_curve": 0,
      "pulse_width": 0.5,
      "attack_level": 1,
      "sustain_level": 1,
      "note_slide": 0,
      "sub_detune_slide": 0,
      "note_slide_curve": 0
    },
    "name": ":subpulse",
    "inherit_arg": true,
    "inherit_base": "Pulse",
    "summary": "Pulse Wave with sub",
    "hiden": true
  },
  "DullBell": {
    "opts": {
      "attack_level": 1,
      "attack": 0,
      "pan": 0,
      "amp_slide_shape": 1,
      "note": 52,
      "pan_slide_curve": 0,
      "decay": 0,
      "release": 1,
      "amp_slide": 0,
      "sustain": 0,
      "amp_slide_curve": 0,
      "pan_slide_shape": 1,
      "decay_level": 1,
      "amp": 1,
      "pan_slide": 0,
      "sustain_level": 1,
      "note_slide_shape": 1,
      "env_curve": 2,
      "note_slide_curve": 0,
      "note_slide": 0
    },
    "name": ":dull_bell",
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "summary": "Dull Bell",
    "hiden": false
  },
  "ChipBass": {
    "opts": {
      "attack_level": 1,
      "attack": 0,
      "pan": 0,
      "amp_slide_shape": 1,
      "amp": 1,
      "pan_slide_curve": 0,
      "note": 60,
      "release": 1,
      "amp_slide": 0,
      "sustain": 0,
      "decay": 0,
      "amp_slide_curve": 0,
      "pan_slide_shape": 1,
      "decay_level": 1,
      "note_resolution": 0.1,
      "pan_slide": 0,
      "sustain_level": 1,
      "note_slide_shape": 1,
      "env_curve": 2,
      "note_slide_curve": 0,
      "note_slide": 0
    },
    "name": ":chipbass",
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "summary": "Chip Bass",
    "hiden": false
  },
  "SynthInfo": {
    "inherit_base": "BaseInfo",
    "hiden": true,
    "opts": {},
    "inherit_arg": true
  },
  "ModTri": {
    "opts": {
      "cutoff_slide_curve": 0,
      "amp": 1,
      "mod_pulse_width_slide_curve": 0,
      "decay": 0,
      "amp_slide_shape": 1,
      "note": 52,
      "cutoff_slide_shape": 1,
      "release": 1,
      "sustain": 0,
      "mod_phase_slide_shape": 1,
      "pan_slide_shape": 1,
      "decay_level": 1,
      "mod_range_slide": 0,
      "pan_slide": 0,
      "mod_pulse_width_slide": 0,
      "mod_wave": 1,
      "cutoff_slide": 0,
      "note_slide_shape": 1,
      "mod_phase_slide": 0,
      "mod_pulse_width_slide_shape": 1,
      "mod_range_slide_shape": 1,
      "mod_phase_offset": 0,
      "attack": 0,
      "pan": 0,
      "cutoff": 100,
      "mod_phase_slide_curve": 0,
      "mod_pulse_width": 0.5,
      "mod_range": 5,
      "amp_slide": 0,
      "mod_phase": 0.25,
      "amp_slide_curve": 0,
      "env_curve": 2,
      "pan_slide_curve": 0,
      "attack_level": 1,
      "sustain_level": 1,
      "note_slide": 0,
      "mod_range_slide_curve": 0,
      "note_slide_curve": 0,
      "mod_invert_wave": 0
    },
    "name": ":mod_tri",
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "summary": "Modulated Triangle Wave",
    "hiden": false
  },
  "Square": {
    "opts": {
      "cutoff_slide_curve": 0,
      "amp": 1,
      "decay": 0,
      "amp_slide_shape": 1,
      "note": 52,
      "cutoff_slide_shape": 1,
      "release": 1,
      "sustain": 0,
      "pan_slide_shape": 1,
      "decay_level": 1,
      "pan_slide": 0,
      "cutoff_slide": 0,
      "note_slide_shape": 1,
      "attack": 0,
      "pan": 0,
      "cutoff": 100,
      "amp_slide": 0,
      "amp_slide_curve": 0,
      "env_curve": 2,
      "pan_slide_curve": 0,
      "attack_level": 1,
      "sustain_level": 1,
      "note_slide": 0,
      "note_slide_curve": 0
    },
    "name": ":square",
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "summary": "Square Wave",
    "hiden": false
  },
  "ChipLead": {
    "opts": {
      "decay": 0,
      "amp_slide_shape": 1,
      "amp": 1,
      "note_resolution": 0.1,
      "note": 60,
      "release": 1,
      "sustain": 0,
      "pan_slide_shape": 1,
      "decay_level": 1,
      "pan_slide": 0,
      "note_slide_shape": 1,
      "width": 0,
      "attack": 0,
      "pan": 0,
      "amp_slide": 0,
      "amp_slide_curve": 0,
      "env_curve": 2,
      "pan_slide_curve": 0,
      "attack_level": 1,
      "sustain_level": 1,
      "note_slide": 0,
      "note_slide_curve": 0
    },
    "name": ":chiplead",
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "summary": "Chip Lead",
    "hiden": false
  },
  "BasicMonoPlayer": {
    "opts": {
      "lpf_slide": 0,
      "hpf_slide": 0,
      "pan": 0,
      "amp_slide_shape": 1,
      "amp": 1,
      "hpf": -1,
      "lpf_slide_curve": 0,
      "amp_slide": 0,
      "hpf_slide_shape": 1,
      "hpf_slide_curve": 0,
      "amp_slide_curve": 0,
      "pan_slide_shape": 1,
      "pan_slide_curve": 0,
      "pan_slide": 0,
      "lpf_slide_shape": 1,
      "rate": 1,
      "lpf": -1
    },
    "name": ":basic_mono_player",
    "inherit_arg": false,
    "inherit_base": "StudioInfo",
    "summary": "Basic Mono Sample Player (no env)",
    "hiden": true
  },
  "SynthViolin": {
    "opts": {
      "cutoff_slide_curve": 0,
      "amp": 1,
      "decay": 0,
      "amp_slide_shape": 1,
      "note": 52,
      "vibrato_depth_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "release": 1,
      "sustain": 0,
      "pan_slide_shape": 1,
      "decay_level": 1,
      "pan_slide": 0,
      "cutoff_slide": 0,
      "vibrato_delay": 0.5,
      "note_slide_shape": 1,
      "vibrato_depth_slide_shape": 1,
      "attack": 0,
      "pan": 0,
      "cutoff": 100,
      "vibrato_rate_slide_shape": 1,
      "vibrato_rate": 6,
      "vibrato_onset": 0.1,
      "amp_slide": 0,
      "amp_slide_curve": 0,
      "env_curve": 2,
      "pan_slide_curve": 0,
      "attack_level": 1,
      "sustain_level": 1,
      "note_slide": 0,
      "vibrato_rate_slide_curve": 0,
      "vibrato_depth": 0.15,
      "note_slide_curve": 0
    },
    "name": ":synth_violin",
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "summary": "Blade Runner style strings",
    "hiden": false
  },
  "StereoPlayer": {
    "opts": {
      "pitch": 0,
      "decay": 0,
      "amp_slide_shape": 1,
      "release": 0,
      "hpf_slide_curve": 0,
      "sustain": -1,
      "pan_slide_shape": 1,
      "decay_level": 1,
      "clamp_time_slide_curve": 0,
      "lpf_env_curve": 2,
      "pre_amp": 1,
      "lpf_slide_shape": 1,
      "hpf_slide": 0,
      "relax_time": 0.01,
      "lpf_min_slide": 0,
      "lpf_decay": 0,
      "hpf_sustain": -1,
      "amp_slide": 0,
      "env_curve": 2,
      "norm": 0,
      "lpf_min": -1,
      "hpf": -1,
      "hpf_decay_level": -1,
      "pre_amp_slide": 0,
      "relax_time_slide_curve": 0,
      "hpf_sustain_level": -1,
      "clamp_time_slide_shape": 1,
      "amp": 1,
      "pre_amp_slide_shape": 1,
      "window_size": 0.2,
      "time_dis_slide_curve": 0,
      "hpf_env_curve": 2,
      "hpf_attack_level": -1,
      "attack": 0,
      "clamp_time": 0.01,
      "time_dis_slide_shape": 1,
      "pan": 0,
      "hpf_release": 0,
      "amp_slide_curve": 0,
      "hpf_max": -1,
      "sustain_level": 1,
      "lpf": -1,
      "time_dis": 0.0,
      "slope_above_slide": 0,
      "pitch_slide": 0,
      "threshold_slide_curve": 0,
      "relax_time_slide_shape": 1,
      "lpf_min_slide_curve": 0,
      "pitch_dis_slide_curve": 0,
      "slope_above_slide_curve": 0,
      "pitch_dis_slide": 0,
      "pitch_dis": 0.0,
      "hpf_slide_shape": 1,
      "pitch_dis_slide_shape": 1,
      "lpf_attack_level": -1,
      "window_size_slide_curve": 0,
      "slope_below_slide": 0,
      "compress": 0,
      "lpf_slide": 0,
      "lpf_release_level": -1,
      "finish": 1,
      "clamp_time_slide": 0,
      "lpf_attack": 0,
      "lpf_slide_curve": 0,
      "threshold_slide_shape": 1,
      "threshold": 0.2,
      "hpf_attack": 0,
      "hpf_max_slide_shape": 1,
      "pan_slide_curve": 0,
      "attack_level": 1,
      "lpf_init_level": -1,
      "hpf_max_slide_curve": 0,
      "window_size_slide_shape": 1,
      "pitch_slide_shape": 1,
      "hpf_max_slide": 0,
      "slope_below_slide_curve": 0,
      "slope_below_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "lpf_release": 0,
      "lpf_sustain_level": -1,
      "pan_slide": 0,
      "hpf_init_level": -1,
      "relax_time_slide": 0,
      "slope_below": 1,
      "lpf_decay_level": -1,
      "threshold_slide": 0,
      "start": 0,
      "hpf_decay": 0,
      "time_dis_slide": 0,
      "lpf_sustain": -1,
      "lpf_min_slide_shape": 1,
      "hpf_release_level": -1,
      "slope_above": 0.5,
      "window_size_slide": 0,
      "pitch_slide_curve": 0,
      "rate": 1,
      "slope_above_slide_shape": 1
    },
    "name": ":stereo_player",
    "inherit_arg": true,
    "inherit_base": "MonoPlayer",
    "summary": "Stereo Sample Player",
    "hiden": true
  },
  "Tri": {
    "opts": {
      "cutoff_slide_curve": 0,
      "decay": 0,
      "amp_slide_shape": 1,
      "amp": 1,
      "cutoff_slide_shape": 1,
      "release": 1,
      "sustain": 0,
      "pulse_width_slide": 0,
      "pan_slide_shape": 1,
      "decay_level": 1,
      "note": 52,
      "pan_slide": 0,
      "cutoff_slide": 0,
      "note_slide_shape": 1,
      "pulse_width_slide_shape": 1,
      "attack": 0,
      "pan": 0,
      "cutoff": 100,
      "amp_slide": 0,
      "amp_slide_curve": 0,
      "env_curve": 2,
      "pan_slide_curve": 0,
      "pulse_width": 0.5,
      "attack_level": 1,
      "sustain_level": 1,
      "note_slide": 0,
      "note_slide_curve": 0
    },
    "name": ":tri",
    "inherit_arg": true,
    "inherit_base": "Pulse",
    "summary": "Triangle Wave",
    "hiden": true
  },
  "DSaw": {
    "opts": {
      "cutoff_slide_curve": 0,
      "amp": 1,
      "decay": 0,
      "amp_slide_shape": 1,
      "note": 52,
      "cutoff_slide_shape": 1,
      "release": 1,
      "detune_slide_curve": 0,
      "sustain": 0,
      "detune": 0.1,
      "pan_slide_shape": 1,
      "decay_level": 1,
      "pan_slide": 0,
      "cutoff_slide": 0,
      "note_slide_shape": 1,
      "attack": 0,
      "pan": 0,
      "cutoff": 100,
      "detune_slide_shape": 1,
      "amp_slide": 0,
      "amp_slide_curve": 0,
      "env_curve": 2,
      "pan_slide_curve": 0,
      "attack_level": 1,
      "sustain_level": 1,
      "note_slide": 0,
      "note_slide_curve": 0,
      "detune_slide": 0
    },
    "name": ":dsaw",
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "summary": "Detuned Saw wave",
    "hiden": false
  },
  "Growl": {
    "opts": {
      "cutoff_slide_curve": 0,
      "amp": 1,
      "decay": 0,
      "amp_slide_shape": 1,
      "note": 52,
      "cutoff_slide_shape": 1,
      "release": 1,
      "sustain": 0,
      "pan_slide_shape": 1,
      "decay_level": 1,
      "res": 0.7,
      "res_slide_curve": 0,
      "pan_slide": 0,
      "res_slide": 0,
      "cutoff_slide": 0,
      "note_slide_shape": 1,
      "attack": 0.1,
      "pan": 0,
      "cutoff": 130,
      "res_slide_shape": 1,
      "amp_slide": 0,
      "amp_slide_curve": 0,
      "env_curve": 2,
      "pan_slide_curve": 0,
      "attack_level": 1,
      "sustain_level": 1,
      "note_slide": 0,
      "note_slide_curve": 0
    },
    "name": ":growl",
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "summary": "Growl",
    "hiden": false
  },
  "ChipNoise": {
    "opts": {
      "freq_band": 0,
      "attack_level": 1,
      "decay": 0,
      "pan": 0,
      "amp_slide_shape": 0,
      "amp": 1,
      "freq_band_slide": 0,
      "freq_band_slide_shape": 1,
      "release": 0,
      "freq_band_slide_curve": 0,
      "amp_slide": 0,
      "sustain": 1,
      "amp_slide_curve": 1,
      "pan_slide_shape": 1,
      "decay_level": 1,
      "pan_slide_curve": 0,
      "pan_slide": 0,
      "sustain_level": 1,
      "env_curve": 0,
      "attack": 0
    },
    "name": ":chipnoise",
    "inherit_arg": false,
    "inherit_base": "Noise",
    "summary": "Chip Noise",
    "hiden": true
  },
  "SoundInStereo": {
    "opts": {
      "decay": 0,
      "amp_slide_shape": 1,
      "amp": 1,
      "release": 0,
      "sustain": 1,
      "pan_slide_shape": 1,
      "decay_level": 1,
      "pan_slide": 0,
      "input": 1,
      "attack": 0,
      "pan": 0,
      "amp_slide": 0,
      "amp_slide_curve": 0,
      "env_curve": 0,
      "pan_slide_curve": 0,
      "attack_level": 1,
      "sustain_level": 1
    },
    "name": ":sound_in_stereo",
    "inherit_arg": true,
    "inherit_base": "SoundIn",
    "summary": "Sound In Stereo",
    "hiden": true
  },
  "DarkSeaHorn": {
    "opts": {
      "attack_level": 1,
      "attack": 1,
      "pan": 0,
      "amp_slide_shape": 1,
      "note": 52,
      "pan_slide_curve": 0,
      "decay": 0,
      "release": 4.0,
      "amp_slide": 0,
      "sustain": 0,
      "amp_slide_curve": 0,
      "pan_slide_shape": 1,
      "decay_level": 1,
      "amp": 1,
      "pan_slide": 0,
      "sustain_level": 1,
      "note_slide_shape": 1,
      "env_curve": 2,
      "note_slide_curve": 0,
      "note_slide": 0
    },
    "name": ":dark_sea_horn",
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "summary": "Dark Sea Horn",
    "hiden": true
  },
  "GNoise": {
    "opts": {
      "cutoff_slide_curve": 0,
      "decay": 0,
      "amp_slide_shape": 1,
      "amp": 1,
      "cutoff_slide_shape": 1,
      "release": 1,
      "sustain": 0,
      "pan_slide_shape": 1,
      "decay_level": 1,
      "res": 0,
      "res_slide_curve": 0,
      "pan_slide": 0,
      "res_slide": 0,
      "cutoff_slide": 0,
      "attack": 0,
      "pan": 0,
      "cutoff": 110,
      "res_slide_shape": 1,
      "amp_slide": 0,
      "amp_slide_curve": 0,
      "env_curve": 2,
      "pan_slide_curve": 0,
      "attack_level": 1,
      "sustain_level": 1
    },
    "name": ":gnoise",
    "inherit_arg": true,
    "inherit_base": "Noise",
    "summary": "Grey Noise",
    "hiden": true
  },
  "TechSaws": {
    "opts": {
      "cutoff_slide_curve": 0,
      "amp": 1,
      "decay": 0,
      "amp_slide_shape": 1,
      "note": 52,
      "cutoff_slide_shape": 1,
      "release": 1,
      "sustain": 0,
      "pan_slide_shape": 1,
      "decay_level": 1,
      "res": 0.7,
      "res_slide_curve": 0,
      "pan_slide": 0,
      "res_slide": 0,
      "cutoff_slide": 0,
      "note_slide_shape": 1,
      "attack": 0,
      "pan": 0,
      "cutoff": 130,
      "res_slide_shape": 1,
      "amp_slide": 0,
      "amp_slide_curve": 0,
      "env_curve": 2,
      "pan_slide_curve": 0,
      "attack_level": 1,
      "sustain_level": 1,
      "note_slide": 0,
      "note_slide_curve": 0
    },
    "name": ":tech_saws",
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "summary": "TechSaws",
    "hiden": false
  },
  "ModSaw": {
    "opts": {
      "cutoff_slide_curve": 0,
      "amp": 1,
      "mod_pulse_width_slide_curve": 0,
      "decay": 0,
      "amp_slide_shape": 1,
      "note": 52,
      "cutoff_slide_shape": 1,
      "release": 1,
      "sustain": 0,
      "mod_phase_slide_shape": 1,
      "pan_slide_shape": 1,
      "decay_level": 1,
      "mod_range_slide": 0,
      "pan_slide": 0,
      "mod_pulse_width_slide": 0,
      "mod_wave": 1,
      "cutoff_slide": 0,
      "note_slide_shape": 1,
      "mod_phase_slide": 0,
      "mod_pulse_width_slide_shape": 1,
      "mod_range_slide_shape": 1,
      "mod_phase_offset": 0,
      "attack": 0,
      "pan": 0,
      "cutoff": 100,
      "mod_phase_slide_curve": 0,
      "mod_pulse_width": 0.5,
      "mod_range": 5,
      "amp_slide": 0,
      "mod_phase": 0.25,
      "amp_slide_curve": 0,
      "env_curve": 2,
      "pan_slide_curve": 0,
      "attack_level": 1,
      "sustain_level": 1,
      "note_slide": 0,
      "mod_range_slide_curve": 0,
      "note_slide_curve": 0,
      "mod_invert_wave": 0
    },
    "name": ":mod_saw",
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "summary": "Modulated Saw Wave",
    "hiden": false
  },
  "DarkAmbience": {
    "opts": {
      "cutoff_slide_curve": 0,
      "detune1_slide_curve": 0,
      "amp": 1,
      "decay": 0,
      "detune2": 24,
      "amp_slide_shape": 1,
      "note": 52,
      "cutoff_slide_shape": 1,
      "release": 1,
      "detune2_slide": 0,
      "noise": 0,
      "sustain": 0,
      "pan_slide_shape": 1,
      "decay_level": 1,
      "res": 0.7,
      "res_slide_curve": 0,
      "pan_slide": 0,
      "detune1_slide_shape": 1,
      "res_slide": 0,
      "cutoff_slide": 0,
      "note_slide_shape": 1,
      "ring": 0.2,
      "reverb_time": 100,
      "detune2_slide_curve": 0,
      "attack": 0,
      "pan": 0,
      "cutoff": 110,
      "detune1_slide": 0,
      "res_slide_shape": 1,
      "amp_slide": 0,
      "detune1": 12,
      "amp_slide_curve": 0,
      "env_curve": 2,
      "pan_slide_curve": 0,
      "attack_level": 1,
      "sustain_level": 1,
      "note_slide": 0,
      "detune2_slide_shape": 1,
      "room": 70,
      "note_slide_curve": 0
    },
    "name": ":dark_ambience",
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "summary": "Dark Ambience",
    "hiden": false
  },
  "Saw": {
    "opts": {
      "amp": 1,
      "decay": 0,
      "amp_slide_shape": 1,
      "note": 52,
      "release": 1,
      "sustain": 0,
      "pan_slide_shape": 1,
      "decay_level": 1,
      "pan_slide": 0,
      "note_slide_shape": 1,
      "attack": 0,
      "pan": 0,
      "amp_slide": 0,
      "amp_slide_curve": 0,
      "env_curve": 2,
      "pan_slide_curve": 0,
      "attack_level": 1,
      "sustain_level": 1,
      "note_slide": 0,
      "note_slide_curve": 0
    },
    "name": ":saw",
    "inherit_arg": true,
    "inherit_base": "Beep",
    "summary": "Saw Wave",
    "hiden": true
  },
  "Pulse": {
    "opts": {
      "cutoff_slide_curve": 0,
      "decay": 0,
      "amp_slide_shape": 1,
      "amp": 1,
      "pan_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "release": 1,
      "sustain": 0,
      "pulse_width_slide": 0,
      "pan_slide_shape": 1,
      "decay_level": 1,
      "pan_slide": 0,
      "cutoff_slide": 0,
      "note_slide_shape": 1,
      "pulse_width_slide_shape": 1,
      "attack": 0,
      "pan": 0,
      "cutoff": 100,
      "amp_slide": 0,
      "amp_slide_curve": 0,
      "env_curve": 2,
      "note": 52,
      "pulse_width": 0.5,
      "attack_level": 1,
      "sustain_level": 1,
      "note_slide": 0,
      "note_slide_curve": 0
    },
    "name": ":pulse",
    "inherit_arg": true,
    "inherit_base": "Square",
    "summary": "Pulse Wave",
    "hiden": true
  },
  "SoundIn": {
    "opts": {
      "attack_level": 1,
      "decay": 0,
      "pan": 0,
      "amp_slide_shape": 1,
      "amp": 1,
      "release": 0,
      "amp_slide": 0,
      "sustain": 1,
      "input": 1,
      "amp_slide_curve": 0,
      "pan_slide_shape": 1,
      "decay_level": 1,
      "pan_slide_curve": 0,
      "pan_slide": 0,
      "sustain_level": 1,
      "env_curve": 0,
      "attack": 0
    },
    "name": ":sound_in",
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "summary": "Sound In",
    "hiden": false
  },
  "SonicPiSynth": {
    "inherit_base": "SynthInfo",
    "hiden": true,
    "opts": {},
    "inherit_arg": true
  },
  "Noise": {
    "opts": {
      "cutoff_slide_curve": 0,
      "decay": 0,
      "amp_slide_shape": 1,
      "amp": 1,
      "pan_slide_curve": 0,
      "release": 1,
      "sustain": 0,
      "pan_slide_shape": 1,
      "decay_level": 1,
      "res": 0,
      "res_slide_curve": 0,
      "pan_slide": 0,
      "res_slide": 0,
      "cutoff_slide": 0,
      "attack": 0,
      "pan": 0,
      "cutoff": 110,
      "res_slide_shape": 1,
      "amp_slide": 0,
      "amp_slide_curve": 0,
      "env_curve": 2,
      "cutoff_slide_shape": 1,
      "attack_level": 1,
      "sustain_level": 1
    },
    "name": ":noise",
    "inherit_arg": false,
    "inherit_base": "Pitchless",
    "summary": "Noise",
    "hiden": false
  },
  "ModFM": {
    "opts": {
      "decay": 0,
      "amp_slide_shape": 1,
      "note": 52,
      "release": 1,
      "sustain": 0,
      "pan_slide_shape": 1,
      "decay_level": 1,
      "divisor_slide_shape": 1,
      "cutoff_slide": 0,
      "mod_phase_offset": 0,
      "depth": 1,
      "cutoff": 100,
      "mod_range": 5,
      "amp_slide": 0,
      "mod_pulse_width": 0.5,
      "env_curve": 2,
      "cutoff_slide_shape": 1,
      "attack_level": 1,
      "note_slide": 0,
      "depth_slide_shape": 1,
      "cutoff_slide_curve": 0,
      "amp": 1,
      "depth_slide_curve": 0,
      "pan_slide_curve": 0,
      "divisor_slide_curve": 0,
      "divisor": 2,
      "pan_slide": 0,
      "depth_slide": 0,
      "mod_wave": 1,
      "note_slide_shape": 1,
      "attack": 0,
      "pan": 0,
      "mod_phase": 0.25,
      "amp_slide_curve": 0,
      "note_slide_curve": 0,
      "sustain_level": 1,
      "mod_invert_wave": 0,
      "divisor_slide": 0
    },
    "name": ":mod_fm",
    "inherit_arg": true,
    "inherit_base": "FM",
    "summary": "Basic FM synthesis with frequency modulation.",
    "hiden": true
  },
  "PNoise": {
    "opts": {
      "cutoff_slide_curve": 0,
      "decay": 0,
      "amp_slide_shape": 1,
      "amp": 1,
      "cutoff_slide_shape": 1,
      "release": 1,
      "sustain": 0,
      "pan_slide_shape": 1,
      "decay_level": 1,
      "res": 0,
      "res_slide_curve": 0,
      "pan_slide": 0,
      "res_slide": 0,
      "cutoff_slide": 0,
      "attack": 0,
      "pan": 0,
      "cutoff": 110,
      "res_slide_shape": 1,
      "amp_slide": 0,
      "amp_slide_curve": 0,
      "env_curve": 2,
      "pan_slide_curve": 0,
      "attack_level": 1,
      "sustain_level": 1
    },
    "name": ":pnoise",
    "inherit_arg": true,
    "inherit_base": "Noise",
    "summary": "Pink Noise",
    "hiden": true
  },
  "SynthPluck": {
    "opts": {
      "amp": 1,
      "decay": 0,
      "amp_slide_shape": 1,
      "note": 52,
      "release": 1,
      "sustain": 0,
      "coef": 0.3,
      "pan_slide_shape": 1,
      "decay_level": 1,
      "pan_slide": 0,
      "noise_amp": 0.8,
      "note_slide_shape": 1,
      "max_delay_time": 0.125,
      "pluck_decay": 30,
      "attack": 0,
      "pan": 0,
      "amp_slide": 0,
      "amp_slide_curve": 0,
      "pan_slide_curve": 0,
      "attack_level": 1,
      "sustain_level": 1,
      "note_slide": 0,
      "note_slide_curve": 0
    },
    "name": ":pluck",
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "summary": "SynthPluck",
    "hiden": false
  },
  "DTri": {
    "opts": {
      "cutoff_slide_curve": 0,
      "detune": 0.1,
      "decay": 0,
      "note_slide_curve": 0,
      "amp_slide_shape": 1,
      "amp": 1,
      "pan_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "release": 1,
      "detune_slide_curve": 0,
      "sustain": 0,
      "detune_slide": 0,
      "pan_slide_shape": 1,
      "decay_level": 1,
      "pan_slide": 0,
      "cutoff_slide": 0,
      "note_slide_shape": 1,
      "attack": 0,
      "pan": 0,
      "cutoff": 100,
      "amp_slide": 0,
      "amp_slide_curve": 0,
      "env_curve": 2,
      "note": 52,
      "attack_level": 1,
      "sustain_level": 1,
      "note_slide": 0,
      "detune_slide_shape": 1
    },
    "name": ":dtri",
    "inherit_arg": true,
    "inherit_base": "DSaw",
    "summary": "Detuned Triangle Wave",
    "hiden": true
  },
  "FM": {
    "opts": {
      "cutoff_slide_curve": 0,
      "amp": 1,
      "decay": 0,
      "amp_slide_shape": 1,
      "note": 52,
      "depth_slide_curve": 0,
      "divisor_slide_shape": 1,
      "cutoff_slide_shape": 1,
      "release": 1,
      "divisor_slide_curve": 0,
      "sustain": 0,
      "pan_slide_shape": 1,
      "decay_level": 1,
      "divisor": 2,
      "pan_slide": 0,
      "depth_slide": 0,
      "cutoff_slide": 0,
      "note_slide_shape": 1,
      "depth": 1,
      "attack": 0,
      "pan": 0,
      "cutoff": 100,
      "depth_slide_shape": 1,
      "amp_slide": 0,
      "amp_slide_curve": 0,
      "env_curve": 2,
      "pan_slide_curve": 0,
      "attack_level": 1,
      "sustain_level": 1,
      "note_slide": 0,
      "note_slide_curve": 0,
      "divisor_slide": 0
    },
    "name": ":fm",
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "summary": "Basic FM synthesis",
    "hiden": false
  },
  "DPulse": {
    "opts": {
      "cutoff_slide_curve": 0,
      "detune": 0.1,
      "pulse_width_slide_curve": 0,
      "decay": 0,
      "note_slide_curve": 0,
      "amp_slide_shape": 1,
      "amp": 1,
      "pan_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "release": 1,
      "dpulse_width_slide": 0,
      "detune_slide_curve": 0,
      "sustain": 0,
      "detune_slide": 0,
      "pan_slide_shape": 1,
      "decay_level": 1,
      "pan_slide": 0,
      "cutoff_slide": 0,
      "note_slide_shape": 1,
      "dpulse_width_slide_shape": 1,
      "dpulse_width": 0,
      "pulse_width_slide_shape": 1,
      "attack": 0,
      "pan": 0,
      "cutoff": 100,
      "amp_slide": 0,
      "pulse_width_slide": 0,
      "amp_slide_curve": 0,
      "env_curve": 2,
      "note": 52,
      "pulse_width": 0.5,
      "attack_level": 1,
      "sustain_level": 1,
      "note_slide": 0,
      "detune_slide_shape": 1
    },
    "name": ":dpulse",
    "inherit_arg": true,
    "inherit_base": "DSaw",
    "summary": "Detuned Pulse Wave",
    "hiden": true
  },
  "Beep": {
    "opts": {
      "attack_level": 1,
      "attack": 0,
      "pan": 0,
      "amp_slide_shape": 1,
      "note": 52,
      "pan_slide_curve": 0,
      "decay": 0,
      "release": 1,
      "amp_slide": 0,
      "sustain": 0,
      "amp_slide_curve": 0,
      "pan_slide_shape": 1,
      "decay_level": 1,
      "amp": 1,
      "pan_slide": 0,
      "sustain_level": 1,
      "note_slide_shape": 1,
      "env_curve": 2,
      "note_slide_curve": 0,
      "note_slide": 0
    },
    "name": ":beep",
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "summary": "Sine Wave",
    "hiden": false
  },
  "TB303": {
    "opts": {
      "cutoff_attack_level": 1,
      "cutoff_min": 30,
      "decay": 0,
      "amp_slide_shape": 1,
      "note": 52,
      "release": 1,
      "cutoff_attack": 0,
      "sustain": 0,
      "pulse_width_slide": 0,
      "pan_slide_shape": 1,
      "decay_level": 1,
      "res": 0.9,
      "res_slide_curve": 0,
      "pulse_width_slide_curve": 0,
      "cutoff_slide": 0,
      "pulse_width_slide_shape": 1,
      "cutoff": 120,
      "cutoff_min_slide_shape": 1,
      "amp_slide": 0,
      "cutoff_release": 1,
      "cutoff_decay": 0,
      "env_curve": 2,
      "cutoff_slide_shape": 1,
      "amp_slide_curve": 0,
      "cutoff_min_slide_curve": 0,
      "note_slide": 0,
      "note_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "amp": 1,
      "pan_slide_curve": 0,
      "cutoff_min_slide": 0,
      "cutoff_sustain": 0,
      "res_slide": 0,
      "cutoff_sustain_level": 1,
      "res_slide_shape": 1,
      "attack_level": 1,
      "pan_slide": 0,
      "note_slide_shape": 1,
      "attack": 0,
      "pan": 0,
      "cutoff_decay_level": 1,
      "wave": 0,
      "pulse_width": 0.5,
      "sustain_level": 1
    },
    "name": ":tb303",
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "summary": "TB-303 Emulation",
    "hiden": false
  },
  "Pitchless": {
    "inherit_base": "SonicPiSynth",
    "hiden": true,
    "opts": {},
    "inherit_arg": true
  },
  "BaseMixer": {
    "inherit_base": "StudioInfo",
    "hiden": true,
    "opts": {},
    "inherit_arg": true
  },
  "MainMixer": {
    "opts": {
      "pre_amp_slide": 0.02,
      "force_mono": 0,
      "invert_stereo": 0,
      "hpf_slide": 0.02,
      "lpf_slide_shape": 1,
      "lpf_slide": 0.02,
      "amp_slide": 0.02,
      "amp": 1,
      "pre_amp_slide_curve": 0,
      "hpf": 0,
      "lpf_bypass": 0,
      "hpf_slide_curve": 0,
      "amp_slide_shape": 1,
      "hpf_slide_shape": 1,
      "lpf_slide_curve": 0,
      "amp_slide_curve": 0,
      "limiter_bypass": 0,
      "pre_amp_slide_shape": 1,
      "pre_amp": 1,
      "hpf_bypass": 0,
      "lpf": 135.5
    },
    "name": ":mixer",
    "inherit_arg": false,
    "inherit_base": "BaseMixer",
    "summary": "Main Mixer",
    "hiden": true
  },
  "StudioInfo": {
    "inherit_base": "SonicPiSynth",
    "hiden": true,
    "opts": {},
    "inherit_arg": true
  },
  "PrettyBell": {
    "opts": {
      "amp": 1,
      "decay": 0,
      "amp_slide_shape": 1,
      "note": 52,
      "release": 1,
      "sustain": 0,
      "pan_slide_shape": 1,
      "decay_level": 1,
      "pan_slide": 0,
      "note_slide_shape": 1,
      "attack": 0,
      "pan": 0,
      "amp_slide": 0,
      "amp_slide_curve": 0,
      "env_curve": 2,
      "pan_slide_curve": 0,
      "attack_level": 1,
      "sustain_level": 1,
      "note_slide": 0,
      "note_slide_curve": 0
    },
    "name": ":pretty_bell",
    "inherit_arg": true,
    "inherit_base": "DullBell",
    "summary": "Pretty Bell",
    "hiden": true
  },
  "ModPulse": {
    "opts": {
      "cutoff_slide_curve": 0,
      "amp": 1,
      "mod_pulse_width_slide_curve": 0,
      "decay": 0,
      "amp_slide_shape": 1,
      "note": 52,
      "cutoff_slide_shape": 1,
      "release": 1,
      "pulse_width_slide_shape": 1,
      "sustain": 0,
      "mod_phase_slide_shape": 1,
      "pan_slide_shape": 1,
      "decay_level": 1,
      "mod_range_slide": 0,
      "pan_slide": 0,
      "mod_pulse_width_slide": 0,
      "mod_wave": 1,
      "cutoff_slide": 0,
      "pulse_width_slide_curve": 0,
      "note_slide_shape": 1,
      "mod_phase_slide": 0,
      "mod_pulse_width_slide_shape": 1,
      "mod_range_slide_shape": 1,
      "mod_phase_offset": 0,
      "attack": 0,
      "pan": 0,
      "cutoff": 100,
      "mod_phase_slide_curve": 0,
      "mod_pulse_width": 0.5,
      "mod_range": 5,
      "amp_slide": 0,
      "mod_phase": 0.25,
      "pulse_width_slide": 0,
      "amp_slide_curve": 0,
      "env_curve": 2,
      "pan_slide_curve": 0,
      "pulse_width": 0.5,
      "attack_level": 1,
      "sustain_level": 1,
      "note_slide": 0,
      "mod_range_slide_curve": 0,
      "note_slide_curve": 0,
      "mod_invert_wave": 0
    },
    "name": ":mod_pulse",
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "summary": "Modulated Pulse",
    "hiden": false
  },
  "Supersaw": {
    "opts": {
      "cutoff_slide_curve": 0,
      "amp": 1,
      "decay": 0,
      "amp_slide_shape": 1,
      "note": 52,
      "cutoff_slide_shape": 1,
      "release": 1,
      "sustain": 0,
      "pan_slide_shape": 1,
      "decay_level": 1,
      "res": 0.7,
      "res_slide_curve": 0,
      "pan_slide": 0,
      "res_slide": 0,
      "cutoff_slide": 0,
      "note_slide_shape": 1,
      "attack": 0,
      "pan": 0,
      "cutoff": 130,
      "res_slide_shape": 1,
      "amp_slide": 0,
      "amp_slide_curve": 0,
      "env_curve": 2,
      "pan_slide_curve": 0,
      "attack_level": 1,
      "sustain_level": 1,
      "note_slide": 0,
      "note_slide_curve": 0
    },
    "name": ":supersaw",
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "summary": "Supersaw",
    "hiden": false
  },
  "BNoise": {
    "opts": {
      "cutoff_slide_curve": 0,
      "decay": 0,
      "amp_slide_shape": 1,
      "amp": 1,
      "cutoff_slide_shape": 1,
      "release": 1,
      "sustain": 0,
      "pan_slide_shape": 1,
      "decay_level": 1,
      "res": 0,
      "res_slide_curve": 0,
      "pan_slide": 0,
      "res_slide": 0,
      "cutoff_slide": 0,
      "attack": 0,
      "pan": 0,
      "cutoff": 110,
      "res_slide_shape": 1,
      "amp_slide": 0,
      "amp_slide_curve": 0,
      "env_curve": 2,
      "pan_slide_curve": 0,
      "attack_level": 1,
      "sustain_level": 1
    },
    "name": ":bnoise",
    "inherit_arg": true,
    "inherit_base": "Noise",
    "summary": "Brown Noise",
    "hiden": true
  },
  "Prophet": {
    "opts": {
      "cutoff_slide_curve": 0,
      "amp": 1,
      "decay": 0,
      "amp_slide_shape": 1,
      "note": 52,
      "cutoff_slide_shape": 1,
      "release": 1,
      "sustain": 0,
      "pan_slide_shape": 1,
      "decay_level": 1,
      "res": 0.7,
      "res_slide_curve": 0,
      "pan_slide": 0,
      "res_slide": 0,
      "cutoff_slide": 0,
      "note_slide_shape": 1,
      "attack": 0,
      "pan": 0,
      "cutoff": 110,
      "res_slide_shape": 1,
      "amp_slide": 0,
      "amp_slide_curve": 0,
      "env_curve": 2,
      "pan_slide_curve": 0,
      "attack_level": 1,
      "sustain_level": 1,
      "note_slide": 0,
      "note_slide_curve": 0
    },
    "name": ":prophet",
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "summary": "The Prophet",
    "hiden": false
  },
  "BasicMixer": {
    "opts": {
      "amp_slide": 0.1,
      "amp": 1,
      "amp_slide_curve": 0,
      "amp_slide_shape": 1
    },
    "name": ":basic_mixer",
    "inherit_arg": false,
    "inherit_base": "BaseMixer",
    "summary": "Basic Mixer",
    "hiden": true
  },
  "BasicStereoPlayer": {
    "opts": {
      "hpf_slide": 0,
      "amp_slide_shape": 1,
      "amp": 1,
      "hpf_slide_curve": 0,
      "hpf_slide_shape": 1,
      "pan_slide_shape": 1,
      "pan_slide": 0,
      "lpf_slide_shape": 1,
      "lpf_slide": 0,
      "pan": 0,
      "hpf": -1,
      "lpf_slide_curve": 0,
      "amp_slide": 0,
      "amp_slide_curve": 0,
      "pan_slide_curve": 0,
      "rate": 1,
      "lpf": -1
    },
    "name": ":basic_stereo_player",
    "inherit_arg": true,
    "inherit_base": "BasicMonoPlayer",
    "summary": "Basic Stereo Sample Player (no env)",
    "hiden": true
  },
  "ModSine": {
    "opts": {
      "cutoff_slide_curve": 0,
      "amp": 1,
      "mod_pulse_width_slide_curve": 0,
      "decay": 0,
      "amp_slide_shape": 1,
      "note": 52,
      "cutoff_slide_shape": 1,
      "release": 1,
      "sustain": 0,
      "mod_phase_slide_shape": 1,
      "pan_slide_shape": 1,
      "decay_level": 1,
      "mod_range_slide": 0,
      "pan_slide": 0,
      "mod_pulse_width_slide": 0,
      "mod_wave": 1,
      "cutoff_slide": 0,
      "note_slide_shape": 1,
      "mod_phase_slide": 0,
      "mod_pulse_width_slide_shape": 1,
      "mod_range_slide_shape": 1,
      "mod_phase_offset": 0,
      "attack": 0,
      "pan": 0,
      "cutoff": 100,
      "mod_phase_slide_curve": 0,
      "mod_pulse_width": 0.5,
      "mod_range": 5,
      "amp_slide": 0,
      "mod_phase": 0.25,
      "amp_slide_curve": 0,
      "env_curve": 2,
      "pan_slide_curve": 0,
      "attack_level": 1,
      "sustain_level": 1,
      "note_slide": 0,
      "mod_range_slide_curve": 0,
      "note_slide_curve": 0,
      "mod_invert_wave": 0
    },
    "name": ":mod_sine",
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "summary": "Modulated Sine Wave",
    "hiden": false
  },
  "SynthPiano": {
    "opts": {
      "amp": 1,
      "decay": 0,
      "amp_slide_shape": 1,
      "note": 52,
      "vel": 0.2,
      "release": 1,
      "amp_slide": 0,
      "sustain": 0,
      "pan_slide_shape": 1,
      "decay_level": 1,
      "pan_slide": 0,
      "note_slide_shape": 1,
      "attack": 0,
      "pan": 0,
      "stereo_width": 0,
      "hard": 0.5,
      "amp_slide_curve": 0,
      "pan_slide_curve": 0,
      "attack_level": 1,
      "sustain_level": 1,
      "note_slide": 0,
      "note_slide_curve": 0
    },
    "name": ":piano",
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "summary": "SynthPiano",
    "hiden": false
  },
  "Hollow": {
    "opts": {
      "cutoff_slide_curve": 0,
      "amp": 1,
      "decay": 0,
      "amp_slide_shape": 1,
      "note": 52,
      "norm": 0,
      "cutoff_slide_shape": 1,
      "release": 1,
      "noise": 1,
      "sustain": 0,
      "pan_slide_shape": 1,
      "decay_level": 1,
      "res": 0.99,
      "res_slide_curve": 0,
      "pan_slide": 0,
      "res_slide": 0,
      "cutoff_slide": 0,
      "note_slide_shape": 1,
      "attack": 0,
      "pan": 0,
      "cutoff": 90,
      "res_slide_shape": 1,
      "amp_slide": 0,
      "amp_slide_curve": 0,
      "env_curve": 2,
      "pan_slide_curve": 0,
      "attack_level": 1,
      "sustain_level": 1,
      "note_slide": 0,
      "note_slide_curve": 0
    },
    "name": ":hollow",
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "summary": "Hollow",
    "hiden": false
  },
  "Hoover": {
    "opts": {
      "cutoff_slide_curve": 0,
      "amp": 1,
      "decay": 0,
      "amp_slide_shape": 1,
      "note": 52,
      "cutoff_slide_shape": 1,
      "release": 1,
      "sustain": 0,
      "pan_slide_shape": 1,
      "decay_level": 1,
      "res": 0.1,
      "res_slide_curve": 0,
      "pan_slide": 0,
      "res_slide": 0,
      "cutoff_slide": 0,
      "note_slide_shape": 1,
      "attack": 0.05,
      "pan": 0,
      "cutoff": 130,
      "res_slide_shape": 1,
      "amp_slide": 0,
      "amp_slide_curve": 0,
      "env_curve": 2,
      "pan_slide_curve": 0,
      "attack_level": 1,
      "sustain_level": 1,
      "note_slide": 0,
      "note_slide_curve": 0
    },
    "name": ":hoover",
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "summary": "Hoover",
    "hiden": false
  },
  "CNoise": {
    "opts": {
      "cutoff_slide_curve": 0,
      "decay": 0,
      "amp_slide_shape": 1,
      "amp": 1,
      "cutoff_slide_shape": 1,
      "release": 1,
      "sustain": 0,
      "pan_slide_shape": 1,
      "decay_level": 1,
      "res": 0,
      "res_slide_curve": 0,
      "pan_slide": 0,
      "res_slide": 0,
      "cutoff_slide": 0,
      "attack": 0,
      "pan": 0,
      "cutoff": 110,
      "res_slide_shape": 1,
      "amp_slide": 0,
      "amp_slide_curve": 0,
      "env_curve": 2,
      "pan_slide_curve": 0,
      "attack_level": 1,
      "sustain_level": 1
    },
    "name": ":cnoise",
    "inherit_arg": true,
    "inherit_base": "Noise",
    "summary": "Clip Noise",
    "hiden": true
  },
  "Zawa": {
    "opts": {
      "cutoff_slide_curve": 0,
      "amp": 1,
      "pulse_width_slide_curve": 0,
      "decay": 0,
      "invert_wave": 0,
      "amp_slide_shape": 1,
      "note": 52,
      "range_slide": 0,
      "cutoff_slide_shape": 1,
      "release": 1,
      "range_slide_shape": 1,
      "sustain": 0,
      "range": 24,
      "pan_slide_shape": 1,
      "decay_level": 1,
      "res": 0.9,
      "res_slide_curve": 0,
      "pan_slide": 0,
      "phase_slide": 0,
      "res_slide": 0,
      "cutoff_slide": 0,
      "note_slide_shape": 1,
      "pulse_width_slide_shape": 1,
      "attack": 0,
      "pan": 0,
      "cutoff": 100,
      "disable_wave": 0,
      "phase": 1,
      "range_slide_curve": 0,
      "phase_slide_shape": 1,
      "phase_offset": 0,
      "res_slide_shape": 1,
      "amp_slide": 0,
      "wave": 3,
      "amp_slide_curve": 0,
      "pulse_width_slide": 0,
      "pan_slide_curve": 0,
      "pulse_width": 0.5,
      "attack_level": 1,
      "sustain_level": 1,
      "note_slide": 0,
      "phase_slide_curve": 0,
      "note_slide_curve": 0
    },
    "name": ":zawa",
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "summary": "Zawa",
    "hiden": false
  },
  "ModDSaw": {
    "opts": {
      "cutoff_slide_curve": 0,
      "amp": 1,
      "mod_pulse_width_slide_curve": 0,
      "decay": 0,
      "amp_slide_shape": 1,
      "note": 52,
      "cutoff_slide_shape": 1,
      "release": 1,
      "detune_slide_curve": 0,
      "sustain": 0,
      "mod_phase_slide_shape": 1,
      "pan_slide_shape": 1,
      "decay_level": 1,
      "mod_range_slide": 0,
      "detune": 0.1,
      "pan_slide": 0,
      "mod_pulse_width_slide": 0,
      "mod_wave": 1,
      "cutoff_slide": 0,
      "note_slide_shape": 1,
      "mod_phase_slide": 0,
      "mod_pulse_width_slide_shape": 1,
      "mod_range_slide_shape": 1,
      "mod_phase_offset": 0,
      "attack": 0,
      "pan": 0,
      "cutoff": 100,
      "detune_slide": 0,
      "mod_phase_slide_curve": 0,
      "mod_pulse_width": 0.5,
      "mod_range": 5,
      "amp_slide": 0,
      "mod_phase": 0.25,
      "amp_slide_curve": 0,
      "env_curve": 2,
      "pan_slide_curve": 0,
      "detune_slide_shape": 1,
      "attack_level": 1,
      "sustain_level": 1,
      "note_slide": 0,
      "mod_range_slide_curve": 0,
      "note_slide_curve": 0,
      "mod_invert_wave": 0
    },
    "name": ":mod_dsaw",
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "summary": "Modulated Detuned Saw Waves",
    "hiden": false
  },
  "MonoPlayer": {
    "opts": {
      "pitch": 0,
      "decay": 0,
      "amp_slide_shape": 1,
      "release": 0,
      "hpf_slide_curve": 0,
      "sustain": -1,
      "pan_slide_shape": 1,
      "decay_level": 1,
      "clamp_time_slide_curve": 0,
      "lpf_env_curve": 2,
      "pre_amp": 1,
      "lpf_slide_shape": 1,
      "hpf_slide": 0,
      "relax_time_slide_curve": 0,
      "relax_time": 0.01,
      "lpf_min_slide": 0,
      "threshold": 0.2,
      "hpf_sustain": -1,
      "amp_slide": 0,
      "env_curve": 2,
      "relax_time_slide_shape": 1,
      "norm": 0,
      "lpf_min": -1,
      "hpf": -1,
      "pre_amp_slide": 0,
      "pitch_dis_slide": 0,
      "hpf_sustain_level": -1,
      "finish": 1,
      "clamp_time_slide_shape": 1,
      "amp": 1,
      "pre_amp_slide_shape": 1,
      "window_size": 0.2,
      "hpf_env_curve": 2,
      "hpf_attack_level": -1,
      "slope_below": 1,
      "clamp_time": 0.01,
      "time_dis_slide_shape": 1,
      "pan": 0,
      "slope_below_slide_shape": 1,
      "hpf_release": 0,
      "amp_slide_curve": 0,
      "hpf_max": -1,
      "sustain_level": 1,
      "hpf_max_slide": 0,
      "time_dis": 0.0,
      "slope_above_slide": 0,
      "pitch_slide": 0,
      "window_size_slide_curve": 0,
      "slope_above_slide_shape": 1,
      "lpf_min_slide_curve": 0,
      "pitch_dis_slide_curve": 0,
      "slope_above_slide_curve": 0,
      "hpf_decay_level": -1,
      "pitch_dis": 0.0,
      "hpf_slide_shape": 1,
      "pitch_dis_slide_shape": 1,
      "lpf_attack_level": -1,
      "threshold_slide_curve": 0,
      "slope_below_slide": 0,
      "compress": 0,
      "lpf_slide": 0,
      "lpf_release_level": -1,
      "lpf_release": 0,
      "clamp_time_slide": 0,
      "time_dis_slide": 0,
      "lpf_slide_curve": 0,
      "threshold_slide_shape": 1,
      "lpf_decay": 0,
      "hpf_attack": 0,
      "hpf_max_slide_shape": 1,
      "pan_slide_curve": 0,
      "attack_level": 1,
      "lpf_init_level": -1,
      "hpf_max_slide_curve": 0,
      "window_size_slide_shape": 1,
      "pitch_slide_shape": 1,
      "lpf": -1,
      "slope_below_slide_curve": 0,
      "lpf_attack": 0,
      "pre_amp_slide_curve": 0,
      "lpf_sustain_level": -1,
      "pan_slide": 0,
      "hpf_init_level": -1,
      "relax_time_slide": 0,
      "attack": 0,
      "lpf_decay_level": -1,
      "threshold_slide": 0,
      "start": 0,
      "hpf_decay": 0,
      "time_dis_slide_curve": 0,
      "lpf_sustain": -1,
      "lpf_min_slide_shape": 1,
      "hpf_release_level": -1,
      "slope_above": 0.5,
      "window_size_slide": 0,
      "pitch_slide_curve": 0,
      "rate": 1
    },
    "name": ":mono_player",
    "inherit_arg": false,
    "inherit_base": "BasicMonoPlayer",
    "summary": "Mono Sample Player",
    "hiden": true
  },
  "Singer": {
    "opts": {
      "attack_level": 1,
      "attack": 1,
      "pan": 0,
      "amp_slide_shape": 1,
      "note": 52,
      "pan_slide_curve": 0,
      "decay": 0,
      "release": 4.0,
      "amp_slide": 0,
      "sustain": 0,
      "amp_slide_curve": 0,
      "pan_slide_shape": 1,
      "decay_level": 1,
      "amp": 1,
      "pan_slide": 0,
      "sustain_level": 1,
      "note_slide_shape": 1,
      "env_curve": 2,
      "note_slide_curve": 0,
      "note_slide": 0
    },
    "name": ":singer",
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "summary": "Singer",
    "hiden": true
  }
}

synth_nodes = {
  ":square": "Square",
  ":fx_replace_ixi_techno": "FXIXITechno",
  ":fx_rhpf": "FXRHPF",
  ":dsaw": "DSaw",
  ":fx_nbpf": "FXNBPF",
  ":fx_rbpf": "FXRBPF",
  ":subpulse": "SubPulse",
  ":noise": "Noise",
  ":growl": "Growl",
  ":saw": "Saw",
  ":pulse": "Pulse",
  ":fx_octaver": "FXOctaver",
  ":fx_reverb": "FXReverb",
  ":fx_replace_echo": "FXEcho",
  ":fx_replace_lpf": "FXLPF",
  ":chiplead": "ChipLead",
  ":fx_replace_compressor": "FXCompressor",
  ":fx_panslicer": "FXPanSlicer",
  ":fx_wobble": "FXWobble",
  ":fx_nrlpf": "FXNormRLPF",
  ":beep": "Beep",
  ":tri": "Tri",
  ":chipbass": "ChipBass",
  ":fx_replace_rlpf": "FXRLPF",
  ":fx_ixi_techno": "FXIXITechno",
  ":fx_ring_mod": "FXRingMod",
  ":hollow": "Hollow",
  ":basic_stereo_player": "BasicStereoPlayer",
  ":fx_level": "FXLevel",
  ":fx_nhpf": "FXNormHPF",
  ":supersaw": "Supersaw",
  ":fx_gverb": "FXGVerb",
  ":pnoise": "PNoise",
  ":fx_tanh": "FXTanh",
  ":sound_in": "SoundIn",
  ":fx_slicer": "FXSlicer",
  ":fx_replace_nlpf": "FXNormLPF",
  ":fx_replace_normaliser": "FXNormaliser",
  ":basic_mixer": "BasicMixer",
  ":fx_mono": "FXMono",
  ":mod_pulse": "ModPulse",
  ":basic_mono_player": "BasicMonoPlayer",
  ":mod_dsaw": "ModDSaw",
  ":piano": "SynthPiano",
  ":pretty_bell": "PrettyBell",
  ":gnoise": "GNoise",
  ":dark_ambience": "DarkAmbience",
  ":fx_normaliser": "FXNormaliser",
  ":fx_pitch_shift": "FXPitchShift",
  ":tb303": "TB303",
  ":fx_replace_nrhpf": "FXNormRHPF",
  ":fx_replace_pan": "FXPan",
  ":dpulse": "DPulse",
  ":fx_nrhpf": "FXNormRHPF",
  ":fx_nrbpf": "FXNRBPF",
  ":fx_replace_slicer": "FXSlicer",
  ":fx_bpf": "FXBPF",
  ":fx_echo": "FXEcho",
  ":main_mixer": "MainMixer",
  ":dtri": "DTri",
  ":fx_distortion": "FXDistortion",
  ":bnoise": "BNoise",
  ":fx_replace_hpf": "FXHPF",
  ":stereo_player": "StereoPlayer",
  ":fx_replace_nrlpf": "FXNormRLPF",
  ":mod_sine": "ModSine",
  ":fx_band_eq": "FXBandEQ",
  ":fx_flanger": "FXFlanger",
  ":fx_compressor": "FXCompressor",
  ":sine": "Beep",
  ":fx_whammy": "FXWhammy",
  ":mono_player": "MonoPlayer",
  ":chipnoise": "ChipNoise",
  ":fx_lpf": "FXLPF",
  ":zawa": "Zawa",
  ":fx_bitcrusher": "FXBitcrusher",
  ":mod_fm": "ModFM",
  ":fm": "FM",
  ":fx_hpf": "FXHPF",
  ":pluck": "SynthPluck",
  ":cnoise": "CNoise",
  ":fx_replace_distortion": "FXDistortion",
  ":fx_nlpf": "FXNormLPF",
  ":dull_bell": "DullBell",
  ":fx_replace_rhpf": "FXRHPF",
  ":tech_saws": "TechSaws",
  ":prophet": "Prophet",
  ":fx_krush": "FXKrush",
  ":hoover": "Hoover",
  ":mod_saw": "ModSaw",
  ":fx_replace_wobble": "FXWobble",
  ":fx_pan": "FXPan",
  ":fx_rlpf": "FXRLPF",
  ":fx_replace_reverb": "FXReverb",
  ":mod_beep": "ModSine",
  ":blade": "SynthViolin",
  ":fx_vowel": "FXVowel",
  ":mod_tri": "ModTri",
  ":fx_replace_nhpf": "FXNormHPF",
  ":sound_in_stereo": "SoundInStereo",
  ":fx_replace_level": "FXLevel"
}

fx = {
  "FXNBPF": {
    "opts": {
      "pre_amp_slide": 0,
      "res_slide": 0,
      "amp_slide_shape": 1,
      "pre_mix": 1,
      "mix_slide_curve": 0,
      "mix": 1,
      "pre_amp_slide_shape": 1,
      "pre_mix_slide": 0,
      "centre_slide": 0,
      "pre_mix_slide_shape": 1,
      "centre": 100,
      "res_slide_shape": 1,
      "res": 0.6,
      "res_slide_curve": 0,
      "pre_amp": 1,
      "centre_slide_curve": 0,
      "centre_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "mix_slide_shape": 1,
      "mix_slide": 0,
      "amp_slide": 0,
      "amp_slide_curve": 0,
      "amp": 1,
      "pre_amp_slide_curve": 0
    },
    "name": ":fx_nbpf",
    "inherit_arg": true,
    "inherit_base": "FXBPF",
    "summary": "Normalised Band Pass Filter",
    "hiden": true
  },
  "FXPitchShift": {
    "opts": {
      "pre_amp_slide": 0,
      "pitch": 0,
      "pitch_dis_slide": 0,
      "amp_slide_shape": 1,
      "pre_mix": 1,
      "mix_slide_curve": 0,
      "pitch_dis_slide_curve": 0,
      "pre_amp_slide_shape": 1,
      "pre_mix_slide": 0,
      "pitch_dis": 0.0,
      "window_size": 0.2,
      "pre_mix_slide_shape": 1,
      "pitch_dis_slide_shape": 1,
      "pitch_slide": 0,
      "window_size_slide_curve": 0,
      "mix": 1,
      "pre_amp": 1,
      "time_dis_slide_curve": 0,
      "time_dis_slide_shape": 1,
      "time_dis": 0.0,
      "pre_mix_slide_curve": 0,
      "mix_slide_shape": 1,
      "mix_slide": 0,
      "time_dis_slide": 0,
      "amp_slide": 0,
      "amp_slide_curve": 0,
      "pitch_slide_curve": 0,
      "amp": 1,
      "window_size_slide": 0,
      "pre_amp_slide_curve": 0,
      "window_size_slide_shape": 1,
      "pitch_slide_shape": 1
    },
    "name": ":fx_pitch_shift",
    "inherit_arg": true,
    "inherit_base": "FXInfo",
    "summary": "Pitch shift",
    "hiden": false
  },
  "FXPanSlicer": {
    "opts": {
      "pan_max": 1,
      "phase_slide_shape": 1,
      "pulse_width_slide_curve": 0,
      "probability_slide_curve": 0,
      "invert_wave": 0,
      "amp_slide_shape": 1,
      "pre_mix": 1,
      "mix_slide_curve": 0,
      "smooth_down": 0,
      "amp_min_slide_curve": 0,
      "amp_min_slide": 0,
      "smooth_up_slide_curve": 0,
      "pre_mix_slide_shape": 1,
      "pulse_width_slide": 0,
      "mix": 1,
      "prob_pos_slide": 0,
      "prob_pos_slide_shape": 1,
      "phase_slide": 0,
      "pre_amp": 1,
      "smooth_slide": 0,
      "amp_max": 1,
      "smooth_up_slide_shape": 1,
      "pulse_width_slide_shape": 1,
      "phase": 0.25,
      "smooth_down_slide_shape": 1,
      "smooth_up_slide": 0,
      "pre_mix_slide_curve": 0,
      "mix_slide_shape": 1,
      "prob_pos": 0,
      "amp_slide": 0,
      "amp_slide_curve": 0,
      "smooth_slide_shape": 1,
      "smooth": 0,
      "phase_offset": 0,
      "pan_max_slide": 0,
      "pre_amp_slide": 0,
      "probability_slide": 0,
      "smooth_slide_curve": 0,
      "probability": 0,
      "amp": 1,
      "pan_min_slide_curve": 0,
      "pan_min_slide": 0,
      "pre_amp_slide_shape": 1,
      "pre_mix_slide": 0,
      "probability_slide_shape": 1,
      "smooth_down_slide_curve": 0,
      "amp_max_slide_shape": 1,
      "pan_min": -1,
      "amp_min": 0,
      "seed": 0,
      "amp_max_slide_curve": 0,
      "pan_max_slide_curve": 0,
      "smooth_down_slide": 0,
      "smooth_up": 0,
      "pan_max_slide_shape": 1,
      "mix_slide": 0,
      "pan_min_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "wave": 1,
      "amp_min_slide_shape": 1,
      "amp_max_slide": 0,
      "pulse_width": 0.5,
      "phase_slide_curve": 0,
      "prob_pos_slide_curve": 0
    },
    "name": ":fx_panslicer",
    "inherit_arg": true,
    "inherit_base": "FXSlicer",
    "summary": "Pan Slicer",
    "hiden": true
  },
  "FXChorus": {
    "opts": {
      "pre_amp_slide": 0,
      "phase_slide_shape": 1,
      "decay": 1e-05,
      "amp_slide_shape": 1,
      "pre_mix": 1,
      "mix_slide_curve": 0,
      "pre_amp_slide_shape": 1,
      "pre_mix_slide": 0,
      "pre_mix_slide_shape": 1,
      "mix": 1,
      "phase_slide": 0,
      "pre_amp": 1,
      "decay_slide": 0,
      "phase_slide_curve": 0,
      "phase": 0.25,
      "decay_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "mix_slide_shape": 1,
      "mix_slide": 0,
      "max_phase": 1,
      "amp_slide": 0,
      "amp_slide_curve": 0,
      "amp": 1,
      "decay_slide_curve": 0,
      "pre_amp_slide_curve": 0
    },
    "name": ":fx_chorus",
    "inherit_arg": true,
    "inherit_base": "FXInfo",
    "summary": "Chorus",
    "hiden": true
  },
  "FXPan": {
    "opts": {
      "pre_amp_slide": 0,
      "amp_slide_shape": 1,
      "pre_mix": 1,
      "mix_slide_curve": 0,
      "pan_slide_curve": 0,
      "pre_amp_slide_shape": 1,
      "pre_mix_slide": 0,
      "pre_mix_slide_shape": 1,
      "pan_slide_shape": 1,
      "mix": 1,
      "pan_slide": 0,
      "pre_amp": 1,
      "pan": 0,
      "pre_mix_slide_curve": 0,
      "mix_slide_shape": 1,
      "mix_slide": 0,
      "amp_slide": 0,
      "amp_slide_curve": 0,
      "amp": 1,
      "pre_amp_slide_curve": 0
    },
    "name": ":fx_pan",
    "inherit_arg": true,
    "inherit_base": "FXInfo",
    "summary": "Pan",
    "hiden": false
  },
  "FXHPF": {
    "opts": {
      "pre_amp_slide": 0,
      "cutoff_slide_curve": 0,
      "amp_slide_shape": 1,
      "pre_mix": 1,
      "mix_slide_curve": 0,
      "pre_amp_slide_shape": 1,
      "pre_mix_slide": 0,
      "pre_mix_slide_shape": 1,
      "mix": 1,
      "pre_amp": 1,
      "cutoff_slide": 0,
      "cutoff": 100,
      "cutoff_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "mix_slide_shape": 1,
      "mix_slide": 0,
      "amp_slide": 0,
      "amp_slide_curve": 0,
      "amp": 1,
      "pre_amp_slide_curve": 0
    },
    "name": ":fx_hpf",
    "inherit_arg": true,
    "inherit_base": "FXInfo",
    "summary": "High Pass Filter",
    "hiden": false
  },
  "FXCompressor": {
    "opts": {
      "pre_amp_slide": 0,
      "slope_below_slide_shape": 1,
      "slope_above_slide_shape": 1,
      "slope_below_slide_curve": 0,
      "amp_slide_shape": 1,
      "pre_mix": 1,
      "mix_slide_curve": 0,
      "clamp_time_slide_curve": 0,
      "pre_amp_slide_shape": 1,
      "pre_mix_slide": 0,
      "threshold_slide": 0,
      "pre_mix_slide_shape": 1,
      "threshold_slide_curve": 0,
      "mix": 1,
      "clamp_time_slide_shape": 1,
      "slope_below_slide": 0,
      "pre_amp": 1,
      "slope_below": 1,
      "relax_time_slide": 0,
      "relax_time": 0.01,
      "clamp_time_slide": 0,
      "threshold_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "mix_slide_shape": 1,
      "mix_slide": 0,
      "relax_time_slide_curve": 0,
      "amp_slide": 0,
      "slope_above_slide_curve": 0,
      "amp_slide_curve": 0,
      "slope_above": 0.5,
      "relax_time_slide_shape": 1,
      "amp": 1,
      "clamp_time": 0.01,
      "pre_amp_slide_curve": 0,
      "slope_above_slide": 0,
      "threshold": 0.2
    },
    "name": ":fx_compressor",
    "inherit_arg": true,
    "inherit_base": "FXInfo",
    "summary": "Compressor",
    "hiden": false
  },
  "FXLPF": {
    "opts": {
      "pre_amp_slide": 0,
      "cutoff_slide_curve": 0,
      "amp_slide_shape": 1,
      "pre_mix": 1,
      "mix_slide_curve": 0,
      "pre_amp_slide_shape": 1,
      "pre_mix_slide": 0,
      "pre_mix_slide_shape": 1,
      "mix": 1,
      "pre_amp": 1,
      "cutoff_slide": 0,
      "cutoff": 100,
      "cutoff_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "mix_slide_shape": 1,
      "mix_slide": 0,
      "amp_slide": 0,
      "amp_slide_curve": 0,
      "amp": 1,
      "pre_amp_slide_curve": 0
    },
    "name": ":fx_lpf",
    "inherit_arg": true,
    "inherit_base": "FXInfo",
    "summary": "Low Pass Filter",
    "hiden": false
  },
  "FXRLPF": {
    "opts": {
      "pre_amp_slide": 0,
      "res_slide_shape": 1,
      "cutoff_slide_curve": 0,
      "amp_slide_shape": 1,
      "pre_mix": 1,
      "mix_slide_curve": 0,
      "res": 0.5,
      "pre_amp_slide_shape": 1,
      "pre_mix_slide": 0,
      "pre_mix_slide_shape": 1,
      "amp": 1,
      "mix": 1,
      "res_slide_curve": 0,
      "pre_amp": 1,
      "res_slide": 0,
      "cutoff_slide": 0,
      "cutoff": 100,
      "pre_mix_slide_curve": 0,
      "mix_slide_shape": 1,
      "mix_slide": 0,
      "amp_slide": 0,
      "amp_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "pre_amp_slide_curve": 0
    },
    "name": ":fx_rlpf",
    "inherit_arg": true,
    "inherit_base": "FXLPF",
    "summary": "Resonant Low Pass Filter",
    "hiden": true
  },
  "FXEcho": {
    "opts": {
      "pre_amp_slide": 0,
      "phase_slide_shape": 1,
      "decay": 2,
      "amp_slide_shape": 1,
      "pre_mix": 1,
      "mix_slide_curve": 0,
      "pre_amp_slide_shape": 1,
      "pre_mix_slide": 0,
      "pre_mix_slide_shape": 1,
      "mix": 1,
      "phase_slide": 0,
      "pre_amp": 1,
      "decay_slide": 0,
      "phase_slide_curve": 0,
      "phase": 0.25,
      "decay_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "mix_slide_shape": 1,
      "mix_slide": 0,
      "max_phase": 2,
      "amp_slide": 0,
      "amp_slide_curve": 0,
      "amp": 1,
      "decay_slide_curve": 0,
      "pre_amp_slide_curve": 0
    },
    "name": ":fx_echo",
    "inherit_arg": true,
    "inherit_base": "FXInfo",
    "summary": "Echo",
    "hiden": false
  },
  "FXReverb": {
    "opts": {
      "pre_amp_slide": 0,
      "damp": 0.5,
      "amp_slide_shape": 1,
      "pre_mix": 1,
      "mix_slide_curve": 0,
      "pre_amp_slide_shape": 1,
      "pre_mix_slide": 0,
      "room": 0.6,
      "pre_mix_slide_shape": 1,
      "mix": 0.4,
      "room_slide_curve": 0,
      "pre_amp": 1,
      "room_slide_shape": 1,
      "damp_slide": 0,
      "damp_slide_curve": 0,
      "pre_mix_slide_curve": 0,
      "mix_slide_shape": 1,
      "mix_slide": 0,
      "amp_slide": 0,
      "amp_slide_curve": 0,
      "amp": 1,
      "damp_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "room_slide": 0
    },
    "name": ":fx_reverb",
    "inherit_arg": true,
    "inherit_base": "FXInfo",
    "summary": "Reverb",
    "hiden": false
  },
  "FXWhammy": {
    "opts": {
      "pre_amp_slide": 0,
      "amp_slide_shape": 1,
      "pre_mix": 1,
      "mix_slide_curve": 0,
      "pre_amp_slide_shape": 1,
      "pre_mix_slide": 0,
      "transpose_slide_shape": 1,
      "pre_mix_slide_shape": 1,
      "deltime": 0.05,
      "mix": 1,
      "pre_amp": 1,
      "max_delay_time": 1,
      "transpose_slide": 0,
      "pre_mix_slide_curve": 0,
      "mix_slide_shape": 1,
      "mix_slide": 0,
      "amp_slide": 0,
      "grainsize": 0.075,
      "amp_slide_curve": 0,
      "amp": 1,
      "transpose": 12,
      "pre_amp_slide_curve": 0,
      "transpose_slide_curve": 0
    },
    "name": ":fx_whammy",
    "inherit_arg": true,
    "inherit_base": "FXInfo",
    "summary": "Whammy",
    "hiden": false
  },
  "FXFlanger": {
    "opts": {
      "pre_amp_slide": 0,
      "decay_slide_shape": 1,
      "decay": 2,
      "invert_wave": 0,
      "phase_slide_curve": 0,
      "amp_slide_shape": 1,
      "pre_mix": 1,
      "mix_slide_curve": 0,
      "pre_amp_slide_shape": 1,
      "pre_mix_slide": 0,
      "feedback_slide_curve": 0,
      "feedback_slide": 0,
      "pre_mix_slide_shape": 1,
      "mix": 1,
      "depth": 5,
      "decay_slide": 0,
      "pre_amp": 1,
      "phase_slide": 0,
      "delay": 5,
      "stereo_invert_wave": 0,
      "depth_slide": 0,
      "feedback": 0,
      "feedback_slide_shape": 1,
      "depth_slide_curve": 0,
      "phase": 4,
      "max_delay": 20,
      "phase_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "mix_slide_shape": 1,
      "mix_slide": 0,
      "phase_offset": 0,
      "amp_slide": 0,
      "delay_slide_curve": 0,
      "amp_slide_curve": 0,
      "amp": 1,
      "decay_slide_curve": 0,
      "wave": 4,
      "delay_slide_shape": 1,
      "invert_flange": 0,
      "pre_amp_slide_curve": 0,
      "delay_slide": 0,
      "depth_slide_shape": 1
    },
    "name": ":fx_flanger",
    "inherit_arg": true,
    "inherit_base": "FXInfo",
    "summary": "Flanger",
    "hiden": false
  },
  "FXRingMod": {
    "opts": {
      "pre_amp_slide": 0,
      "freq_slide": 0,
      "mod_amp_slide_curve": 0,
      "amp_slide_shape": 1,
      "pre_mix": 1,
      "mix_slide_curve": 0,
      "freq_slide_curve": 0,
      "pre_amp_slide_shape": 1,
      "pre_mix_slide": 0,
      "pre_mix_slide_shape": 1,
      "mix": 1,
      "mod_amp_slide_shape": 1,
      "mod_amp_slide": 0,
      "pre_amp": 1,
      "mod_amp": 1,
      "pre_mix_slide_curve": 0,
      "mix_slide_shape": 1,
      "mix_slide": 0,
      "amp_slide": 0,
      "amp_slide_curve": 0,
      "amp": 1,
      "freq_slide_shape": 1,
      "pre_amp_slide_curve": 0,
      "freq": 30
    },
    "name": ":fx_ring_mod",
    "inherit_arg": true,
    "inherit_base": "FXInfo",
    "summary": "Ring Modulator",
    "hiden": false
  },
  "FXBandEQ": {
    "opts": {
      "pre_amp_slide": 0,
      "freq_slide": 0,
      "res_slide_shape": 1,
      "amp_slide_shape": 1,
      "pre_mix": 1,
      "mix_slide_curve": 0,
      "freq_slide_curve": 0,
      "pre_amp_slide_shape": 1,
      "pre_mix_slide": 0,
      "pre_mix_slide_shape": 1,
      "db": 0.6,
      "res_slide": 0,
      "mix": 1,
      "res_slide_curve": 0,
      "pre_amp": 1,
      "res": 0.6,
      "db_slide_shape": 1,
      "db_slide_curve": 0,
      "pre_mix_slide_curve": 0,
      "mix_slide_shape": 1,
      "mix_slide": 0,
      "amp_slide": 0,
      "amp_slide_curve": 0,
      "amp": 1,
      "freq_slide_shape": 1,
      "db_slide": 0,
      "pre_amp_slide_curve": 0,
      "freq": 100
    },
    "name": ":fx_band_eq",
    "inherit_arg": true,
    "inherit_base": "FXInfo",
    "summary": "Band EQ Filter",
    "hiden": false
  },
  "FXNormHPF": {
    "opts": {
      "pre_amp_slide": 0,
      "cutoff_slide_curve": 0,
      "amp_slide_shape": 1,
      "pre_mix": 1,
      "mix_slide_curve": 0,
      "pre_amp_slide_shape": 1,
      "pre_mix_slide": 0,
      "pre_mix_slide_shape": 1,
      "amp": 1,
      "mix": 1,
      "pre_amp": 1,
      "cutoff_slide": 0,
      "cutoff": 100,
      "pre_mix_slide_curve": 0,
      "mix_slide_shape": 1,
      "mix_slide": 0,
      "amp_slide": 0,
      "amp_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "pre_amp_slide_curve": 0
    },
    "name": ":fx_nhpf",
    "inherit_arg": true,
    "inherit_base": "FXHPF",
    "summary": "Normalised High Pass Filter",
    "hiden": true
  },
  "FXVowel": {
    "opts": {
      "pre_amp_slide": 0,
      "amp_slide_shape": 1,
      "pre_mix": 1,
      "mix_slide_curve": 0,
      "pre_amp_slide_shape": 1,
      "pre_mix_slide": 0,
      "pre_mix_slide_shape": 1,
      "mix": 1,
      "pre_amp": 1,
      "vowel_sound": 1,
      "voice": 0,
      "pre_mix_slide_curve": 0,
      "mix_slide_shape": 1,
      "mix_slide": 0,
      "amp_slide": 0,
      "amp_slide_curve": 0,
      "amp": 1,
      "pre_amp_slide_curve": 0
    },
    "name": ":fx_vowel",
    "inherit_arg": true,
    "inherit_base": "FXInfo",
    "summary": "Vowel",
    "hiden": false
  },
  "FXNormRLPF": {
    "opts": {
      "pre_amp_slide": 0,
      "res_slide": 0,
      "cutoff_slide_curve": 0,
      "amp_slide_shape": 1,
      "pre_mix": 1,
      "mix_slide_curve": 0,
      "mix": 1,
      "pre_amp_slide_shape": 1,
      "pre_mix_slide": 0,
      "pre_mix_slide_shape": 1,
      "res_slide_shape": 1,
      "res": 0.5,
      "res_slide_curve": 0,
      "pre_amp": 1,
      "cutoff_slide": 0,
      "cutoff": 100,
      "cutoff_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "mix_slide_shape": 1,
      "mix_slide": 0,
      "amp_slide": 0,
      "amp_slide_curve": 0,
      "amp": 1,
      "pre_amp_slide_curve": 0
    },
    "name": ":fx_nrlpf",
    "inherit_arg": true,
    "inherit_base": "FXRLPF",
    "summary": "Normalised Resonant Low Pass Filter",
    "hiden": true
  },
  "FXDistortion": {
    "opts": {
      "pre_amp_slide": 0,
      "amp_slide_shape": 1,
      "pre_mix": 1,
      "mix_slide_curve": 0,
      "pre_amp_slide_shape": 1,
      "pre_mix_slide": 0,
      "pre_mix_slide_shape": 1,
      "mix": 1,
      "pre_amp": 1,
      "distort_slide": 0,
      "distort": 0.5,
      "pre_mix_slide_curve": 0,
      "mix_slide_shape": 1,
      "mix_slide": 0,
      "distort_slide_shape": 1,
      "amp_slide": 0,
      "amp_slide_curve": 0,
      "distort_slide_curve": 0,
      "amp": 1,
      "pre_amp_slide_curve": 0
    },
    "name": ":fx_distortion",
    "inherit_arg": true,
    "inherit_base": "FXInfo",
    "summary": "Distortion",
    "hiden": false
  },
  "FXNRBPF": {
    "opts": {
      "pre_amp_slide": 0,
      "res_slide_shape": 1,
      "amp_slide_shape": 1,
      "pre_mix": 1,
      "mix_slide_curve": 0,
      "res": 0.5,
      "pre_amp_slide_shape": 1,
      "pre_mix_slide": 0,
      "centre_slide": 0,
      "pre_mix_slide_shape": 1,
      "centre": 100,
      "res_slide": 0,
      "mix": 1,
      "res_slide_curve": 0,
      "pre_amp": 1,
      "centre_slide_curve": 0,
      "centre_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "mix_slide_shape": 1,
      "mix_slide": 0,
      "amp_slide": 0,
      "amp_slide_curve": 0,
      "amp": 1,
      "pre_amp_slide_curve": 0
    },
    "name": ":fx_nrbpf",
    "inherit_arg": true,
    "inherit_base": "FXRBPF",
    "summary": "Normalised Resonant Band Pass Filter",
    "hiden": true
  },
  "FXWobble": {
    "opts": {
      "cutoff_max_slide_shape": 1,
      "smooth_up_slide": 0,
      "cutoff_min": 60,
      "probability_slide_curve": 0,
      "invert_wave": 0,
      "amp_slide_shape": 1,
      "pre_mix": 1,
      "mix_slide_curve": 0,
      "smooth_down": 0,
      "prob_pos_slide": 0,
      "pre_mix_slide_shape": 1,
      "pulse_width_slide": 0,
      "res_slide": 0,
      "mix": 1,
      "res_slide_curve": 0,
      "pulse_width_slide_curve": 0,
      "phase_slide": 0,
      "pre_amp": 1,
      "res": 0.8,
      "smooth_slide": 0,
      "cutoff_max": 120,
      "prob_pos": 0,
      "smooth_up_slide_shape": 1,
      "pulse_width_slide_shape": 1,
      "cutoff_min_slide_shape": 1,
      "smooth_slide_curve": 0,
      "phase_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "mix_slide_shape": 1,
      "phase_offset": 0,
      "amp_slide": 0,
      "smooth_down_slide": 0,
      "wave": 0,
      "cutoff_min_slide_curve": 0,
      "smooth_slide_shape": 1,
      "smooth": 0,
      "pre_amp_slide": 0,
      "probability_slide": 0,
      "probability": 0,
      "amp": 1,
      "pre_amp_slide_shape": 1,
      "pre_mix_slide": 0,
      "cutoff_min_slide": 0,
      "cutoff_max_slide_curve": 0,
      "smooth_down_slide_curve": 0,
      "res_slide_shape": 1,
      "probability_slide_shape": 1,
      "seed": 0,
      "smooth_up_slide_curve": 0,
      "phase_slide_curve": 0,
      "smooth_up": 0,
      "filter": 0,
      "mix_slide": 0,
      "prob_pos_slide_curve": 0,
      "prob_pos_slide_shape": 1,
      "amp_slide_curve": 0,
      "cutoff_max_slide": 0,
      "phase": 0.5,
      "pulse_width": 0.5,
      "pre_amp_slide_curve": 0,
      "smooth_down_slide_shape": 1
    },
    "name": ":fx_wobble",
    "inherit_arg": true,
    "inherit_base": "FXInfo",
    "summary": "Wobble",
    "hiden": false
  },
  "FXIXITechno": {
    "opts": {
      "pre_amp_slide": 0,
      "cutoff_max_slide_shape": 1,
      "cutoff_min": 60,
      "res_slide": 0,
      "amp_slide_shape": 1,
      "pre_mix": 1,
      "mix_slide_curve": 0,
      "res": 0.8,
      "pre_amp_slide_shape": 1,
      "pre_mix_slide": 0,
      "cutoff_min_slide": 0,
      "cutoff_max_slide_curve": 0,
      "pre_mix_slide_shape": 1,
      "res_slide_shape": 1,
      "mix": 1,
      "res_slide_curve": 0,
      "phase_slide": 0,
      "pre_amp": 1,
      "cutoff_max": 120,
      "phase_slide_curve": 0,
      "cutoff_min_slide_shape": 1,
      "phase_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "mix_slide_shape": 1,
      "mix_slide": 0,
      "phase_offset": 0,
      "amp_slide": 0,
      "amp_slide_curve": 0,
      "cutoff_max_slide": 0,
      "amp": 1,
      "cutoff_min_slide_curve": 0,
      "phase": 4,
      "pre_amp_slide_curve": 0
    },
    "name": ":fx_ixi_techno",
    "inherit_arg": true,
    "inherit_base": "FXInfo",
    "summary": "Techno from IXI Lang",
    "hiden": false
  },
  "FXNormRHPF": {
    "opts": {
      "pre_amp_slide": 0,
      "res_slide": 0,
      "cutoff_slide_curve": 0,
      "amp_slide_shape": 1,
      "pre_mix": 1,
      "mix_slide_curve": 0,
      "mix": 1,
      "pre_amp_slide_shape": 1,
      "pre_mix_slide": 0,
      "pre_mix_slide_shape": 1,
      "res_slide_shape": 1,
      "res": 0.5,
      "res_slide_curve": 0,
      "pre_amp": 1,
      "cutoff_slide": 0,
      "cutoff": 100,
      "cutoff_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "mix_slide_shape": 1,
      "mix_slide": 0,
      "amp_slide": 0,
      "amp_slide_curve": 0,
      "amp": 1,
      "pre_amp_slide_curve": 0
    },
    "name": ":fx_nrhpf",
    "inherit_arg": true,
    "inherit_base": "FXRHPF",
    "summary": "Normalised Resonant High Pass Filter",
    "hiden": true
  },
  "FXBitcrusher": {
    "opts": {
      "pre_amp_slide": 0,
      "cutoff_slide_curve": 0,
      "amp_slide_shape": 1,
      "pre_mix": 1,
      "mix_slide_curve": 0,
      "pre_amp_slide_shape": 1,
      "pre_mix_slide": 0,
      "sample_rate_slide_shape": 1,
      "pre_mix_slide_shape": 1,
      "bits_slide": 0,
      "sample_rate": 10000,
      "sample_rate_slide": 0,
      "mix": 1,
      "pre_amp": 1,
      "cutoff_slide": 0,
      "sample_rate_slide_curve": 0,
      "cutoff": 0,
      "cutoff_slide_shape": 1,
      "bits_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "mix_slide_shape": 1,
      "mix_slide": 0,
      "bits_slide_curve": 0,
      "amp_slide": 0,
      "bits": 8,
      "amp_slide_curve": 0,
      "amp": 1,
      "pre_amp_slide_curve": 0
    },
    "name": ":fx_bitcrusher",
    "inherit_arg": true,
    "inherit_base": "FXInfo",
    "summary": "Bitcrusher",
    "hiden": false
  },
  "FXLevel": {
    "opts": {
      "amp_slide": 0,
      "amp": 1,
      "amp_slide_curve": 0,
      "amp_slide_shape": 1
    },
    "name": ":fx_level",
    "inherit_arg": false,
    "inherit_base": "FXInfo",
    "summary": "Level Amplifier",
    "hiden": false
  },
  "FXOctaver": {
    "opts": {
      "pre_amp_slide": 0,
      "amp_slide_shape": 1,
      "pre_mix": 1,
      "mix_slide_curve": 0,
      "pre_amp_slide_shape": 1,
      "pre_mix_slide": 0,
      "super_amp_slide": 0,
      "sub_amp_slide": 0,
      "subsub_amp_slide": 0,
      "pre_mix_slide_shape": 1,
      "super_amp_slide_curve": 0,
      "subsub_amp": 1,
      "mix": 1,
      "super_amp": 1,
      "pre_amp": 1,
      "super_amp_slide_shape": 1,
      "sub_amp": 1,
      "sub_amp_slide_shape": 1,
      "subsub_amp_slide_curve": 0,
      "pre_mix_slide_curve": 0,
      "mix_slide_shape": 1,
      "mix_slide": 0,
      "amp_slide": 0,
      "sub_amp_slide_curve": 0,
      "amp_slide_curve": 0,
      "amp": 1,
      "pre_amp_slide_curve": 0,
      "subsub_amp_slide_shape": 1
    },
    "name": ":fx_octaver",
    "inherit_arg": true,
    "inherit_base": "FXInfo",
    "summary": "Octaver",
    "hiden": false
  },
  "FXMono": {
    "opts": {
      "pre_amp_slide": 0,
      "amp_slide_shape": 1,
      "pre_mix": 1,
      "mix_slide_curve": 0,
      "pan_slide_curve": 0,
      "pre_amp_slide_shape": 1,
      "pre_mix_slide": 0,
      "pre_mix_slide_shape": 1,
      "pan_slide_shape": 1,
      "mix": 1,
      "pan_slide": 0,
      "pre_amp": 1,
      "pan": 0,
      "pre_mix_slide_curve": 0,
      "mix_slide_shape": 1,
      "mix_slide": 0,
      "amp_slide": 0,
      "amp_slide_curve": 0,
      "amp": 1,
      "pre_amp_slide_curve": 0
    },
    "name": ":fx_mono",
    "inherit_arg": true,
    "inherit_base": "FXInfo",
    "summary": "Mono",
    "hiden": false
  },
  "FXInfo": {
    "inherit_base": "BaseInfo",
    "hiden": true,
    "opts": {
      "pre_amp_slide": 0,
      "amp_slide_shape": 1,
      "pre_mix": 1,
      "mix_slide_curve": 0,
      "pre_mix_slide_curve": 0,
      "mix_slide_shape": 1,
      "mix_slide": 0,
      "pre_mix_slide": 0,
      "amp_slide": 0,
      "pre_mix_slide_shape": 1,
      "amp_slide_curve": 0,
      "amp": 1,
      "mix": 1,
      "pre_amp_slide_shape": 1,
      "pre_amp": 1,
      "pre_amp_slide_curve": 0
    },
    "inherit_arg": false
  },
  "FXNormaliser": {
    "opts": {
      "level_slide_curve": 0,
      "pre_amp_slide": 0,
      "amp_slide_shape": 1,
      "pre_mix": 1,
      "mix_slide_curve": 0,
      "pre_amp_slide_shape": 1,
      "pre_mix_slide": 0,
      "pre_mix_slide_shape": 1,
      "mix": 1,
      "level": 1,
      "pre_amp": 1,
      "level_slide": 0,
      "pre_mix_slide_curve": 0,
      "mix_slide_shape": 1,
      "mix_slide": 0,
      "amp_slide": 0,
      "amp_slide_curve": 0,
      "amp": 1,
      "pre_amp_slide_curve": 0,
      "level_slide_shape": 1
    },
    "name": ":fx_normaliser",
    "inherit_arg": true,
    "inherit_base": "FXInfo",
    "summary": "Normaliser",
    "hiden": false
  },
  "FXTanh": {
    "opts": {
      "pre_amp_slide": 0,
      "krunch_slide_curve": 0,
      "krunch": 5,
      "krunch_slide": 0,
      "amp_slide_shape": 1,
      "pre_mix": 1,
      "mix_slide_curve": 0,
      "pre_amp_slide_shape": 1,
      "pre_mix_slide": 0,
      "pre_mix_slide_shape": 1,
      "mix": 1,
      "krunch_slide_shape": 1,
      "pre_amp": 1,
      "pre_mix_slide_curve": 0,
      "mix_slide_shape": 1,
      "mix_slide": 0,
      "amp_slide": 0,
      "amp_slide_curve": 0,
      "amp": 1,
      "pre_amp_slide_curve": 0
    },
    "name": ":fx_tanh",
    "inherit_arg": true,
    "inherit_base": "FXInfo",
    "summary": "Hyperbolic Tangent",
    "hiden": false
  },
  "FXRBPF": {
    "opts": {
      "pre_amp_slide": 0,
      "res_slide": 0,
      "amp_slide_shape": 1,
      "pre_mix": 1,
      "mix_slide_curve": 0,
      "mix": 1,
      "pre_amp_slide_shape": 1,
      "pre_mix_slide": 0,
      "centre_slide": 0,
      "pre_mix_slide_shape": 1,
      "centre": 100,
      "res_slide_shape": 1,
      "res": 0.5,
      "res_slide_curve": 0,
      "pre_amp": 1,
      "centre_slide_curve": 0,
      "centre_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "mix_slide_shape": 1,
      "mix_slide": 0,
      "amp_slide": 0,
      "amp_slide_curve": 0,
      "amp": 1,
      "pre_amp_slide_curve": 0
    },
    "name": ":fx_rbpf",
    "inherit_arg": true,
    "inherit_base": "FXBPF",
    "summary": "Resonant Band Pass Filter",
    "hiden": true
  },
  "FXKrush": {
    "opts": {
      "pre_amp_slide": 0,
      "res_slide_shape": 1,
      "cutoff_slide_curve": 0,
      "amp_slide_shape": 1,
      "pre_mix": 1,
      "mix_slide_curve": 0,
      "res": 0,
      "pre_amp_slide_shape": 1,
      "pre_mix_slide": 0,
      "pre_mix_slide_shape": 1,
      "gain": 5,
      "mix": 1,
      "res_slide_curve": 0,
      "pre_amp": 1,
      "res_slide": 0,
      "cutoff_slide": 0,
      "gain_slide__curve": 0,
      "cutoff": 100,
      "gain_slide": 0,
      "cutoff_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "mix_slide_shape": 1,
      "mix_slide": 0,
      "amp_slide": 0,
      "amp_slide_curve": 0,
      "amp": 1,
      "gain_slide_shape": 1,
      "pre_amp_slide_curve": 0
    },
    "name": ":fx_krush",
    "inherit_arg": true,
    "inherit_base": "FXInfo",
    "summary": "krush",
    "hiden": false
  },
  "FXRHPF": {
    "opts": {
      "pre_amp_slide": 0,
      "res_slide_shape": 1,
      "cutoff_slide_curve": 0,
      "amp_slide_shape": 1,
      "pre_mix": 1,
      "mix_slide_curve": 0,
      "res": 0.5,
      "pre_amp_slide_shape": 1,
      "pre_mix_slide": 0,
      "pre_mix_slide_shape": 1,
      "amp": 1,
      "mix": 1,
      "res_slide_curve": 0,
      "pre_amp": 1,
      "res_slide": 0,
      "cutoff_slide": 0,
      "cutoff": 100,
      "pre_mix_slide_curve": 0,
      "mix_slide_shape": 1,
      "mix_slide": 0,
      "amp_slide": 0,
      "amp_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "pre_amp_slide_curve": 0
    },
    "name": ":fx_rhpf",
    "inherit_arg": true,
    "inherit_base": "FXHPF",
    "summary": "Resonant High Pass Filter",
    "hiden": true
  },
  "FXNormLPF": {
    "opts": {
      "pre_amp_slide": 0,
      "cutoff_slide_curve": 0,
      "amp_slide_shape": 1,
      "pre_mix": 1,
      "mix_slide_curve": 0,
      "pre_amp_slide_shape": 1,
      "pre_mix_slide": 0,
      "pre_mix_slide_shape": 1,
      "amp": 1,
      "mix": 1,
      "pre_amp": 1,
      "cutoff_slide": 0,
      "cutoff": 100,
      "pre_mix_slide_curve": 0,
      "mix_slide_shape": 1,
      "mix_slide": 0,
      "amp_slide": 0,
      "amp_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "pre_amp_slide_curve": 0
    },
    "name": ":fx_nlpf",
    "inherit_arg": true,
    "inherit_base": "FXLPF",
    "summary": "Normalised Low Pass Filter.",
    "hiden": true
  },
  "FXBPF": {
    "opts": {
      "pre_amp_slide": 0,
      "res_slide_shape": 1,
      "amp_slide_shape": 1,
      "pre_mix": 1,
      "mix_slide_curve": 0,
      "res": 0.6,
      "pre_amp_slide_shape": 1,
      "pre_mix_slide": 0,
      "centre_slide": 0,
      "pre_mix_slide_shape": 1,
      "centre": 100,
      "res_slide": 0,
      "mix": 1,
      "res_slide_curve": 0,
      "pre_amp": 1,
      "centre_slide_curve": 0,
      "centre_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "mix_slide_shape": 1,
      "mix_slide": 0,
      "amp_slide": 0,
      "amp_slide_curve": 0,
      "amp": 1,
      "pre_amp_slide_curve": 0
    },
    "name": ":fx_bpf",
    "inherit_arg": true,
    "inherit_base": "FXInfo",
    "summary": "Band Pass Filter",
    "hiden": false
  },
  "FXGVerb": {
    "opts": {
      "pre_amp_slide": 0,
      "pre_damp_slide_shape": 1,
      "damp": 0.5,
      "tail_level": 0.5,
      "amp_slide_shape": 1,
      "pre_mix": 1,
      "mix_slide_curve": 0,
      "pre_amp_slide_shape": 1,
      "pre_mix_slide": 0,
      "room": 10,
      "release": 3,
      "dry_slide_shape": 1,
      "pre_mix_slide_shape": 1,
      "dry_slide": 0,
      "spread_slide": 0,
      "mix": 1,
      "pre_amp": 1,
      "spread_slide_shape": 1,
      "dry_slide_curve": 0,
      "pre_damp_slide_curve": 0,
      "spread_slide_curve": 0,
      "ref_level": 0.7,
      "pre_damp_slide": 0,
      "damp_slide": 0,
      "damp_slide_curve": 0,
      "spread": 0.5,
      "pre_mix_slide_curve": 0,
      "mix_slide_shape": 1,
      "mix_slide": 0,
      "amp_slide": 0,
      "amp_slide_curve": 0,
      "amp": 1,
      "damp_slide_shape": 1,
      "dry": 1,
      "pre_amp_slide_curve": 0,
      "pre_damp": 0.5
    },
    "name": ":fx_gverb",
    "inherit_arg": true,
    "inherit_base": "FXInfo",
    "summary": "GVerb",
    "hiden": false
  },
  "FXSlicer": {
    "opts": {
      "smooth_up_slide": 0,
      "pulse_width_slide_curve": 0,
      "probability_slide_curve": 0,
      "invert_wave": 0,
      "amp_slide_shape": 1,
      "pre_mix": 1,
      "mix_slide_curve": 0,
      "smooth_down": 0,
      "probability_slide": 0,
      "amp_min_slide": 0,
      "smooth_up_slide_curve": 0,
      "pre_mix_slide_shape": 1,
      "pulse_width_slide": 0,
      "mix": 1,
      "prob_pos_slide": 0,
      "prob_pos_slide_shape": 1,
      "phase_slide": 0,
      "pre_amp": 1,
      "smooth_slide": 0,
      "amp_max": 1,
      "smooth_up_slide_shape": 1,
      "pulse_width_slide_shape": 1,
      "phase": 0.25,
      "smooth_down_slide_shape": 1,
      "phase_slide_shape": 1,
      "pre_mix_slide_curve": 0,
      "mix_slide_shape": 1,
      "prob_pos": 0,
      "amp_slide": 0,
      "wave": 1,
      "smooth_slide_shape": 1,
      "smooth": 0,
      "phase_offset": 0,
      "pre_amp_slide": 0,
      "amp_min_slide_curve": 0,
      "probability": 0,
      "amp": 1,
      "pre_amp_slide_shape": 1,
      "pre_mix_slide": 0,
      "probability_slide_shape": 1,
      "smooth_down_slide_curve": 0,
      "amp_max_slide_shape": 1,
      "amp_min": 0,
      "seed": 0,
      "amp_max_slide_curve": 0,
      "phase_slide_curve": 0,
      "smooth_up": 0,
      "mix_slide": 0,
      "prob_pos_slide_curve": 0,
      "pre_amp_slide_curve": 0,
      "amp_slide_curve": 0,
      "amp_min_slide_shape": 1,
      "amp_max_slide": 0,
      "pulse_width": 0.5,
      "smooth_down_slide": 0,
      "smooth_slide_curve": 0
    },
    "name": ":fx_slicer",
    "inherit_arg": true,
    "inherit_base": "FXInfo",
    "summary": "Slicer",
    "hiden": false
  }
}

samples = {
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
  "Miscellaneous Sounds": [
    ":misc_burp",
    ":misc_crow",
    ":misc_cineboom"
  ]
}

