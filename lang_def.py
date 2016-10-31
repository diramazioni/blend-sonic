null = None; true = True; false = False;
#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/

lang_core = {
  "range": {
    "name": "range",
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
      "inclusive": false,
      "step": 1
    },
    "memoize": true,
    "returns": ":ring",
    "inline": true,
    "summary": "Create a ring buffer with the specified start, finish and step size",
    "accepts_block": false,
    "introduced": "2,2,0",
    "signature": {
      "start": null,
      "finish": null,
      "*args": null
    },
    "hiden": false
  },
  "spread": {
    "name": "spread",
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
    "inline": true,
    "returns": ":ring",
    "summary": "Euclidean distribution for beats",
    "accepts_block": false,
    "introduced": "2,4,0",
    "signature": {
      "size": null,
      "num_accents": null,
      "*args": null
    },
    "hiden": false
  },
  "rand_skip": {
    "name": "rand_skip",
    "args": [
      {
        "amount": ":number"
      }
    ],
    "accepts_block": false,
    "summary": "Jump forward random generator",
    "introduced": "2,7,0",
    "signature": {
      "amount": 1
    },
    "hiden": false
  },
  "inc": {
    "name": "inc",
    "args": [
      {
        "n": ":number"
      }
    ],
    "opts": {},
    "summary": "Increment",
    "accepts_block": false,
    "introduced": "2, 1, 0",
    "signature": {
      "n": null
    },
    "hiden": true
  },
  "one_in": {
    "name": "one_in",
    "args": [
      {
        "num": ":number"
      }
    ],
    "accepts_block": false,
    "inline": true,
    "summary": "Random true value with specified probability",
    "introduced": "2,0,0",
    "signature": {
      "num": null
    },
    "hiden": false
  },
  "dice": {
    "name": "dice",
    "args": [
      {
        "num_sides": ":number"
      }
    ],
    "accepts_block": false,
    "inline": true,
    "summary": "Random dice throw",
    "introduced": "2,0,0",
    "signature": {
      "num_sides": 6
    },
    "hiden": false
  },
  "tick": {
    "name": "tick",
    "args": [],
    "opts": {
      "step": 1,
      "offset": 0
    },
    "inline": true,
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
    "accepts_block": false,
    "introduced": "2,6,0",
    "signature": {
      "*args": null
    },
    "hiden": false
  },
  "print": {
    "name": "print",
    "args": [
      {
        "output": ":anything"
      }
    ],
    "intro_fn": true,
    "accepts_block": false,
    "summary": "Display a message in the output pane",
    "introduced": "2,0,0",
    "signature": {
      "*msgs": null
    },
    "hiden": true
  },
  "density": {
    "name": "density",
    "args": [
      {
        "d": ":density"
      }
    ],
    "accepts_block": true,
    "requires_block": true,
    "summary": "Squash and repeat time",
    "introduced": "2,3,0",
    "async_block": true,
    "signature": {
      "d": null,
      "&block": null
    },
    "hiden": false
  },
  "current_bpm": {
    "name": "current_bpm",
    "introduced": "2,0,0",
    "accepts_block": false,
    "summary": "Get current tempo",
    "hiden": true
  },
  "rrand_i": {
    "name": "rrand_i",
    "args": [
      {
        "min": ":number"
      },
      {
        "max": ":number"
      }
    ],
    "accepts_block": false,
    "inline": true,
    "summary": "Generate a random whole number between two points inclusively",
    "introduced": "2,0,0",
    "signature": {
      "min": null,
      "max": null
    },
    "hiden": false
  },
  "use_osc": {
    "signature": {
      "host_or_port": null,
      "port": "nil"
    },
    "hiden": true
  },
  "with_bpm": {
    "name": "with_bpm",
    "args": [
      {
        "bpm": ":number"
      }
    ],
    "accepts_block": true,
    "requires_block": true,
    "summary": "Set the tempo for the code block",
    "introduced": "2,0,0",
    "signature": {
      "&block": null,
      "bpm": null
    },
    "hiden": false
  },
  "use_random_seed": {
    "name": "use_random_seed",
    "args": [
      {
        "seed": ":number"
      }
    ],
    "accepts_block": false,
    "summary": "Set random seed generator to known seed",
    "introduced": "2,0,0",
    "signature": {
      "&block": null,
      "seed": null
    },
    "hiden": false
  },
  "with_bpm_mul": {
    "name": "with_bpm_mul",
    "args": [
      {
        "mul": ":number"
      }
    ],
    "accepts_block": true,
    "requires_block": true,
    "summary": "Set new tempo as a multiple of current tempo for block",
    "introduced": "2,3,0",
    "signature": {
      "mul": null,
      "&block": null
    },
    "hiden": false
  },
  "pick": {
    "name": "pick",
    "args": [
      {
        "n": ":number_or_nil"
      }
    ],
    "opts": {
      "skip": 0
    },
    "inline": true,
    "alt_args": [
      {
        "list": ":array"
      }
    ],
    "summary": "Randomly pick from list (with duplicates)",
    "accepts_block": false,
    "introduced": "2,10,0",
    "signature": {
      "*args": null
    },
    "hiden": false
  },
  "load_buffer": {
    "name": "load_buffer",
    "args": [
      {
        "path": ":string"
      }
    ],
    "accepts_block": false,
    "summary": "Load the contents of a file to the current buffer",
    "introduced": "2,10,0",
    "signature": {
      "path": null
    },
    "hiden": false
  },
  "look": {
    "name": "look",
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
    "inline": true,
    "returns": ":number",
    "summary": "Obtain value of a tick",
    "accepts_block": false,
    "introduced": "2,6,0",
    "signature": {
      "*args": null
    },
    "hiden": false
  },
  "version": {
    "name": "version",
    "introduced": "2,0,0",
    "accepts_block": false,
    "summary": "Get current version information",
    "hiden": true
  },
  "at": {
    "name": "at",
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
    "summary": "Asynchronous Time. Run a block at the given time(s)",
    "introduced": "2,1,0",
    "async_block": true,
    "signature": {
      "params": "nil",
      "times": 0,
      "&block": null
    },
    "hiden": false
  },
  "rand_back": {
    "name": "rand_back",
    "args": [
      {
        "amount": ":number"
      }
    ],
    "accepts_block": false,
    "summary": "Roll back random generator",
    "introduced": "2,7,0",
    "signature": {
      "amount": 1
    },
    "hiden": false
  },
  "vt": {
    "name": "vt",
    "accepts_block": false,
    "inline": true,
    "introduced": "2,1,0",
    "summary": "Get virtual time",
    "hiden": false
  },
  "current_beat_duration": {
    "name": "current_beat_duration",
    "introduced": "2,6,0",
    "accepts_block": false,
    "summary": "Duration of current beat",
    "hiden": true
  },
  "vector": {
    "name": "vector",
    "args": [
      {
        "list": ":array"
      }
    ],
    "accepts_block": false,
    "inline": true,
    "returns": ":vector",
    "summary": "Create a vector",
    "introduced": "2,6,0",
    "signature": {
      "*args": null
    },
    "hiden": false
  },
  "bt": {
    "name": "bt",
    "args": [
      {
        "seconds": ":number"
      }
    ],
    "accepts_block": false,
    "summary": "Beat time conversion",
    "introduced": "2,8,0",
    "signature": {
      "t": null
    },
    "hiden": true
  },
  "quantise": {
    "name": "quantise",
    "args": [
      {
        "n": ":number"
      },
      {
        "step": ":positive_number"
      }
    ],
    "accepts_block": false,
    "inline": true,
    "summary": "Quantise a value to resolution",
    "introduced": "2,1,0",
    "signature": {
      "step": null,
      "n": null
    },
    "hiden": false
  },
  "note_list": {
    "args": [],
    "name": "note_list",
    "accepts_block": false,
    "opts": {},
    "summary": "Make a list of notes",
    "signature": {},
    "hiden": false,
    "introduced": "blend-sonic"
  },
  "rand_i_look": {
    "name": "rand_i_look",
    "args": [
      {
        "max": ":number_or_range"
      }
    ],
    "accepts_block": false,
    "inline": true,
    "summary": "Generate a random whole number without consuming a rand",
    "introduced": "2,11,0",
    "signature": {
      "*args": null
    },
    "hiden": false
  },
  "wait": {
    "name": "wait",
    "args": [
      {
        "beats": ":number"
      }
    ],
    "advances_time": true,
    "accepts_block": false,
    "summary": "Wait for duration",
    "introduced": "2,0,0",
    "signature": {
      "time": null
    },
    "hiden": true
  },
  "assert_equal": {
    "name": "assert_equal",
    "args": [
      {
        "arg1": ":anything"
      },
      {
        "arg2": ":anything"
      }
    ],
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
    "introduced": "2,8,0",
    "signature": {
      "arg1": null,
      "msg": "nil",
      "arg2": null
    },
    "hiden": false
  },
  "rrand": {
    "name": "rrand",
    "args": [
      {
        "min": ":number"
      },
      {
        "max": ":number"
      }
    ],
    "intro_fn": true,
    "opts": {
      "step": 1
    },
    "inline": true,
    "summary": "Generate a random float between two numbers",
    "accepts_block": false,
    "introduced": "2,0,0",
    "signature": {
      "*opts": null,
      "min": null,
      "max": null
    },
    "hiden": false
  },
  "assert": {
    "name": "assert",
    "args": [
      {
        "is_true": ":boolean"
      }
    ],
    "accepts_block": false,
    "alt_args": [],
    "summary": "Ensure arg is valid",
    "introduced": "2,8,0",
    "signature": {
      "msg": "nil",
      "arg": null
    },
    "hiden": false
  },
  "cue": {
    "name": "cue",
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
    "summary": "Cue other threads",
    "accepts_block": false,
    "introduced": "2,0,0",
    "signature": {
      "*opts": null,
      "cue_id": null
    },
    "hiden": false
  },
  "ndefine": {
    "name": "ndefine",
    "args": [
      {
        "name": ":symbol"
      }
    ],
    "accepts_block": true,
    "requires_block": true,
    "summary": "Define a new function",
    "introduced": "2,1,0",
    "signature": {
      "name": null,
      "&block": null
    },
    "hiden": true
  },
  "ring": {
    "name": "ring",
    "args": [
      {
        "list": ":array"
      }
    ],
    "accepts_block": false,
    "inline": true,
    "returns": ":ring",
    "summary": "Create a ring buffer",
    "introduced": "2,2,0",
    "signature": {
      "*args": null
    },
    "hiden": false
  },
  "rdist": {
    "name": "rdist",
    "args": [
      {
        "width": ":number"
      }
    ],
    "opts": {
      "step": 1
    },
    "inline": true,
    "alt_args": [
      {
        "width": ":number"
      },
      {
        "centre": ":number"
      }
    ],
    "summary": "Random number in centred distribution",
    "accepts_block": false,
    "introduced": "2,3,0",
    "signature": {
      "centre": 0,
      "*opts": null,
      "width": null
    },
    "hiden": false
  },
  "rand_reset": {
    "name": "rand_reset",
    "args": [],
    "accepts_block": false,
    "introduced": "2,7,0",
    "summary": "Reset rand generator to last seed",
    "hiden": false
  },
  "current_random_seed": {
    "name": "current_random_seed",
    "accepts_block": false,
    "intro_fn": true,
    "introduced": "2,10,0",
    "summary": "Get current random seed",
    "hiden": true
  },
  "clear": {
    "name": "clear",
    "args": [],
    "accepts_block": false,
    "returns": null,
    "introduced": "2,11,0",
    "summary": "Clear all thread locals to defaults",
    "hiden": false
  },
  "tick_set": {
    "name": "tick_set",
    "args": [
      {
        "value": ":number"
      }
    ],
    "accepts_block": false,
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
    "introduced": "2,6,0",
    "signature": {
      "*args": null
    },
    "hiden": false
  },
  "factor": {
    "name": "factor?",
    "args": [
      {
        "val": ":number"
      },
      {
        "factor": ":number"
      }
    ],
    "accepts_block": false,
    "summary": "Factor test",
    "introduced": "2,1,0",
    "signature": {
      "factor": null,
      "val": null
    },
    "hiden": false
  },
  "rt": {
    "name": "rt",
    "args": [
      {
        "seconds": ":number"
      }
    ],
    "accepts_block": false,
    "inline": true,
    "summary": "Real time conversion",
    "introduced": "2,0,0",
    "signature": {
      "t": null
    },
    "hiden": false
  },
  "with_tempo": {
    "signature": {
      "&block": null,
      "*args": null
    },
    "hiden": true
  },
  "load_example": {
    "name": "load_example",
    "args": [
      {
        "path": ":string"
      }
    ],
    "accepts_block": false,
    "summary": "Load a built-in example",
    "introduced": "2,10,0",
    "signature": {
      "example_name": null
    },
    "hiden": true
  },
  "beat": {
    "name": "beat",
    "args": [],
    "accepts_block": false,
    "introduced": "2,10,0",
    "summary": "Get current beat",
    "hiden": true
  },
  "use_bpm": {
    "name": "use_bpm",
    "args": [
      {
        "bpm": ":number"
      }
    ],
    "intro_fn": true,
    "accepts_block": false,
    "summary": "Set the tempo",
    "introduced": "2,0,0",
    "signature": {
      "&block": null,
      "bpm": null
    },
    "hiden": false
  },
  "choose": {
    "name": "choose",
    "args": [],
    "accepts_block": false,
    "inline": true,
    "alt_args": [
      {
        "list": ":array"
      }
    ],
    "summary": "Random list selection",
    "introduced": "2,0,0",
    "signature": {
      "args": null
    },
    "hiden": false
  },
  "line": {
    "name": "line",
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
    "memoize": true,
    "returns": ":ring",
    "inline": true,
    "summary": "Create a ring buffer representing a straight line",
    "accepts_block": false,
    "introduced": "2,5,0",
    "signature": {
      "start": null,
      "finish": null,
      "*args": null
    },
    "hiden": false
  },
  "with_cue_logging": {
    "name": "with_cue_logging",
    "args": [
      {
        "true_or_false": ":boolean"
      }
    ],
    "accepts_block": true,
    "requires_block": true,
    "summary": "Block-level enable and disable cue logging",
    "introduced": "2,6,0",
    "signature": {
      "v": null,
      "&block": null
    },
    "hiden": false
  },
  "stretch": {
    "name": "stretch",
    "args": [
      {
        "count": ":int"
      }
    ],
    "accepts_block": false,
    "inline": true,
    "returns": ":ring",
    "alt_args": [
      {
        "list": ":array"
      }
    ],
    "summary": "Stretch a sequence of values",
    "introduced": "2,6,0",
    "signature": {
      "*args": null
    },
    "hiden": false
  },
  "use_bpm_mul": {
    "name": "use_bpm_mul",
    "args": [
      {
        "mul": ":number"
      }
    ],
    "accepts_block": false,
    "summary": "Set new tempo as a multiple of current tempo",
    "introduced": "2,3,0",
    "signature": {
      "mul": null,
      "&block": null
    },
    "hiden": false
  },
  "sleep": {
    "name": "sleep",
    "args": [
      {
        "beats": ":number"
      }
    ],
    "advances_time": true,
    "accepts_block": false,
    "summary": "Wait for beat duration",
    "introduced": "2,0,0",
    "signature": {
      "beats": null
    },
    "hiden": false
  },
  "puts": {
    "name": "puts",
    "args": [
      {
        "output": ":anything"
      }
    ],
    "intro_fn": true,
    "accepts_block": false,
    "summary": "Display a message in the output pane",
    "introduced": "2,0,0",
    "signature": {
      "*msgs": null
    },
    "hiden": true
  },
  "shuffle": {
    "name": "shuffle",
    "args": [],
    "accepts_block": false,
    "inline": true,
    "alt_args": [
      {
        "list": ":array"
      }
    ],
    "summary": "Randomise order of a list",
    "introduced": "2,1,0",
    "signature": {
      "list": null
    },
    "hiden": false
  },
  "on": {
    "name": "on",
    "args": [
      {
        "condition": ":truthy"
      }
    ],
    "accepts_block": true,
    "returns": null,
    "requires_block": true,
    "summary": "Optionally evaluate block",
    "introduced": "2,10,0",
    "signature": {
      "&blk": null,
      "condition": null
    },
    "hiden": false
  },
  "block_duration": {
    "name": "block_duration",
    "args": [],
    "accepts_block": true,
    "requires_block": true,
    "summary": "Return block duration",
    "introduced": "2,9,0",
    "async_block": false,
    "signature": {
      "&block": null
    },
    "hiden": false
  },
  "tick_reset_all": {
    "name": "tick_reset_all",
    "args": [
      {
        "value": ":number"
      }
    ],
    "accepts_block": false,
    "alt_args": [
      {
        "key": ":symbol"
      },
      {
        "value": ":number"
      }
    ],
    "returns": null,
    "introduced": "2,6,0",
    "summary": "Reset all ticks",
    "hiden": false
  },
  "time_shift": {
    "name": "time_shift",
    "args": [
      {
        "delta_time": ":number"
      }
    ],
    "accepts_block": true,
    "returns": null,
    "requires_block": true,
    "summary": "Slide time forwards or backwards for the given block",
    "introduced": "2,11,0",
    "signature": {
      "&blk": null,
      "delta": null
    },
    "hiden": false
  },
  "defonce": {
    "name": "defonce",
    "args": [
      {
        "name": ":symbol"
      }
    ],
    "opts": {
      "override": false
    },
    "requires_block": true,
    "summary": "Define a named value only once",
    "accepts_block": true,
    "introduced": "2,0,0",
    "signature": {
      "name": null,
      "*opts": null,
      "&block": null
    },
    "hiden": false
  },
  "halves": {
    "name": "halves",
    "args": [
      {
        "start": ":number"
      },
      {
        "num_halves": ":int"
      }
    ],
    "accepts_block": false,
    "memoize": true,
    "returns": ":ring",
    "inline": true,
    "summary": "Create a ring of successive halves",
    "introduced": "2,10,0",
    "signature": {
      "start": null,
      "num_halves": 1
    },
    "hiden": false
  },
  "uncomment": {
    "name": "uncomment",
    "accepts_block": true,
    "requires_block": true,
    "summary": "Block level comment ignoring",
    "introduced": "2,0,0",
    "signature": {
      "&block": null,
      "*args": null
    },
    "hiden": true
  },
  "dec": {
    "name": "dec",
    "args": [
      {
        "n": ":number"
      }
    ],
    "opts": {},
    "summary": "Decrement",
    "accepts_block": false,
    "introduced": "2, 1, 0",
    "signature": {
      "n": null
    },
    "hiden": true
  },
  "run_code": {
    "name": "run_code",
    "args": [
      {
        "code": ":string"
      }
    ],
    "accepts_block": false,
    "returns": null,
    "summary": "Evaluate the code passed as a String as a new Run",
    "introduced": "2,11,0",
    "signature": {
      "code": null
    },
    "hiden": false
  },
  "stop": {
    "name": "stop",
    "args": [
      {
        "true_stops": ":boolean"
      }
    ],
    "accepts_block": false,
    "alt_args": [],
    "returns": null,
    "introduced": "2,5,0",
    "summary": "Stop current thread or run",
    "hiden": false
  },
  "spark": {
    "name": "spark",
    "accepts_block": false,
    "introduced": "2,5,0",
    "summary": "Print a string representing a list of numeric values as a spark graph/bar chart",
    "hiden": true,
    "signature": {
      "*values": null
    }
  },
  "rand": {
    "name": "rand",
    "args": [
      {
        "max": ":number_or_range"
      }
    ],
    "intro_fn": true,
    "accepts_block": false,
    "inline": true,
    "summary": "Generate a random float below a value",
    "introduced": "2,0,0",
    "signature": {
      "max": 1
    },
    "hiden": false
  },
  "block_slept": {
    "name": "block_slept?",
    "args": [],
    "accepts_block": true,
    "requires_block": true,
    "summary": "Determine if block contains sleep time",
    "introduced": "2,9,0",
    "async_block": false,
    "signature": {
      "&block": null
    },
    "hiden": false
  },
  "live_loop": {
    "name": "live_loop",
    "args": [
      {
        "name": ":symbol"
      }
    ],
    "intro_fn": true,
    "opts": {
      "auto_cue": true,
      "sync_bpm": ":foo",
      "delay": 0,
      "sync": ":foo",
      "init": "",
      "seed": 0
    },
    "requires_block": true,
    "summary": "A loop for live coding",
    "accepts_block": true,
    "introduced": "2,1,0",
    "async_block": true,
    "signature": {
      "name": "nil",
      "&block": null,
      "*args": null
    },
    "hiden": false
  },
  "ramp": {
    "name": "ramp",
    "args": [
      {
        "list": ":array"
      }
    ],
    "accepts_block": false,
    "inline": true,
    "returns": ":ramp",
    "summary": "Create a ramp vector",
    "introduced": "2,6,0",
    "signature": {
      "*args": null
    },
    "hiden": false
  },
  "sync": {
    "name": "sync",
    "args": [
      {
        "cue_id": ":symbol"
      }
    ],
    "advances_time": true,
    "opts": {
      "bpm_sync": false
    },
    "summary": "Sync with other threads",
    "accepts_block": false,
    "introduced": "2,0,0",
    "signature": {
      "cue_ids": null,
      "opts": "{}"
    },
    "hiden": false
  },
  "in_thread": {
    "name": "in_thread",
    "opts": {
      "name": ":foo",
      "sync_bpm": ":foo",
      "delay": 0,
      "sync": ":foo"
    },
    "requires_block": true,
    "summary": "Run code block at the same time",
    "accepts_block": true,
    "introduced": "2,0,0",
    "async_block": true,
    "signature": {
      "*opts": null,
      "&block": null
    },
    "hiden": false
  },
  "with_random_seed": {
    "name": "with_random_seed",
    "args": [
      {
        "seed": ":number"
      }
    ],
    "accepts_block": true,
    "requires_block": true,
    "summary": "Specify random seed for code block",
    "introduced": "2,0,0",
    "signature": {
      "&block": null,
      "seed": null
    },
    "hiden": false
  },
  "rand_i": {
    "name": "rand_i",
    "args": [
      {
        "max": ":number_or_range"
      }
    ],
    "accepts_block": false,
    "inline": true,
    "summary": "Generate a random whole number below a value (exclusive)",
    "introduced": "2,0,0",
    "signature": {
      "max": 2
    },
    "hiden": false
  },
  "doubles": {
    "name": "doubles",
    "args": [
      {
        "start": ":number"
      },
      {
        "num_doubles": ":int"
      }
    ],
    "accepts_block": false,
    "memoize": true,
    "returns": ":ring",
    "inline": true,
    "summary": "Create a ring of successive doubles",
    "introduced": "2,10,0",
    "signature": {
      "start": null,
      "num_doubles": 1
    },
    "hiden": false
  },
  "use_cue_logging": {
    "name": "use_cue_logging",
    "args": [
      {
        "true_or_false": ":boolean"
      }
    ],
    "accepts_block": false,
    "summary": "Enable and disable cue logging",
    "introduced": "2,6,0",
    "signature": {
      "v": null,
      "&block": null
    },
    "hiden": false
  },
  "tick_reset": {
    "name": "tick_reset",
    "alt_args": [
      {
        "key": ":symbol"
      }
    ],
    "accepts_block": false,
    "returns": ":number",
    "summary": "Reset tick to 0",
    "introduced": "2,6,0",
    "signature": {
      "*args": null
    },
    "hiden": false
  },
  "spark_graph": {
    "name": "spark_graph",
    "accepts_block": false,
    "summary": "Returns a string representing a list of numeric values as a spark graph/bar chart",
    "introduced": "2,5,0",
    "signature": {
      "*values": null
    },
    "hiden": true
  },
  "comment": {
    "name": "comment",
    "accepts_block": true,
    "requires_block": true,
    "summary": "Block level commenting",
    "introduced": "2,0,0",
    "signature": {
      "&block": null,
      "*args": null
    },
    "hiden": true
  },
  "reset": {
    "name": "reset",
    "args": [],
    "accepts_block": false,
    "returns": null,
    "introduced": "2,11,0",
    "summary": "Reset all thread locals",
    "hiden": false
  },
  "bools": {
    "name": "bools",
    "args": [
      {
        "list": ":array"
      }
    ],
    "accepts_block": false,
    "inline": true,
    "returns": ":ring",
    "summary": "Create a ring of boolean values",
    "introduced": "2,2,0",
    "signature": {
      "*args": null
    },
    "hiden": false
  },
  "define": {
    "name": "define",
    "args": [
      {
        "name": ":symbol"
      }
    ],
    "intro_fn": true,
    "accepts_block": true,
    "requires_block": true,
    "summary": "Define a new function",
    "introduced": "2,0,0",
    "signature": {
      "name": null,
      "&block": null
    },
    "hiden": false
  },
  "run_file": {
    "name": "run_file",
    "args": [
      {
        "filename": ":path"
      }
    ],
    "accepts_block": false,
    "returns": null,
    "summary": "Evaluate the contents of the file as a new Run",
    "introduced": "2,11,0",
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
  "sync_bpm": {
    "name": "sync_bpm",
    "args": [
      {
        "cue_id": ":symbol"
      }
    ],
    "advances_time": true,
    "opts": {},
    "summary": "Sync and inherit BPM from other threads ",
    "accepts_block": false,
    "introduced": "2,10,0",
    "signature": {
      "cue_ids": null,
      "opts": "{}"
    },
    "hiden": false
  },
  "knit": {
    "name": "knit",
    "args": [
      {
        "value": ":anything"
      },
      {
        "count": ":number"
      }
    ],
    "accepts_block": false,
    "inline": true,
    "returns": ":ring",
    "summary": "Knit a sequence of repeated values",
    "introduced": "2,2,0",
    "signature": {
      "*args": null
    },
    "hiden": false
  },
  "rand_look": {
    "name": "rand_look",
    "args": [
      {
        "max": ":number_or_range"
      }
    ],
    "accepts_block": false,
    "inline": true,
    "summary": "Generate a random number without consuming a rand",
    "introduced": "2,11,0",
    "signature": {
      "*args": null
    },
    "hiden": false
  }
}

#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/

lang_sound = {
  "fx_names": {
    "name": "fx_names",
    "accepts_block": false,
    "memoize": true,
    "introduced": "2,10,0",
    "summary": "Get all FX names",
    "hiden": true
  },
  "truthy": {
    "signature": {
      "val": null
    },
    "hiden": false
  },
  "use_arg_bpm_scaling": {
    "name": "use_arg_bpm_scaling",
    "args": [
      {
        "bool": ":boolean"
      }
    ],
    "accepts_block": false,
    "summary": "Enable and disable BPM scaling",
    "introduced": "2,0,0",
    "signature": {
      "&block": null,
      "bool": null
    },
    "hiden": false
  },
  "current_amp": {
    "hiden": true
  },
  "midi_notes": {
    "name": "midi_notes",
    "args": [
      {
        "list": ":array"
      }
    ],
    "accepts_block": false,
    "memoize": true,
    "returns": ":ring",
    "inline": true,
    "summary": "Create a ring buffer of midi note numbers",
    "introduced": "2,7,0",
    "signature": {
      "*args": null
    },
    "hiden": false
  },
  "load_sample_at_path": {
    "signature": {
      "path": null
    },
    "hiden": false
  },
  "use_sample_defaults": {
    "name": "use_sample_defaults",
    "opts": {},
    "summary": "Use new sample defaults",
    "accepts_block": false,
    "introduced": "2,5,0",
    "signature": {
      "&block": null,
      "*args": null
    },
    "hiden": false
  },
  "synth": {
    "name": "synth",
    "args": [
      {
        "synth_name": ":symbol"
      }
    ],
    "intro_fn": true,
    "opts": {
      "decay": 0,
      "amp": 1,
      "attack_level": 1,
      "on": 1,
      "pan_slide": 1,
      "pitch": 0,
      "sustain": 1,
      "pan": 0,
      "amp_slide": 1,
      "release": 0,
      "decay_level": 1,
      "sustain_level": 1,
      "slide": 0,
      "env_curve": 1,
      "attack": 0
    },
    "requires_block": false,
    "summary": "Trigger specific synth",
    "accepts_block": true,
    "introduced": "2,0,0",
    "async_block": true,
    "signature": {
      "&blk": null,
      "synth_name": null,
      "*args": null
    },
    "hiden": false
  },
  "use_tuning": {
    "name": "use_tuning",
    "args": [
      {
        "tuning": ":symbol"
      },
      {
        "fundamental_note": ":symbol_or_number"
      }
    ],
    "accepts_block": false,
    "summary": "Use alternative tuning systems",
    "introduced": "2,6,0",
    "signature": {
      "fundamental_note": ":c",
      "&block": null,
      "tuning": null
    },
    "hiden": false
  },
  "sample_paths": {
    "name": "sample_paths",
    "args": [
      {
        "pre_args": ":source_and_filter_types"
      }
    ],
    "accepts_block": false,
    "returns": ":ring",
    "summary": "Sample Pack Filter Resolution",
    "introduced": "2,10,0",
    "signature": {
      "*args": null
    },
    "hiden": true
  },
  "set_volume": {
    "name": "set_volume!",
    "args": [
      {
        "vol": ":number"
      }
    ],
    "accepts_block": false,
    "summary": "Set Volume globally",
    "introduced": "2,0,0",
    "signature": {
      "vol": null
    },
    "hiden": false,
    "modifies_env": true
  },
  "current_transpose": {
    "name": "current_transpose",
    "introduced": "2,0,0",
    "accepts_block": false,
    "summary": "Get current transposition",
    "hiden": true
  },
  "recording_save": {
    "name": "recording_save",
    "args": [
      {
        "path": ":string"
      }
    ],
    "accepts_block": false,
    "summary": "Save recording",
    "introduced": "2,0,0",
    "signature": {
      "filename": null
    },
    "hiden": true
  },
  "play_pattern_timed": {
    "name": "play_pattern_timed",
    "args": [
      {
        "notes": ":list"
      },
      {
        "times": ":list_or_number"
      }
    ],
    "opts": {
      "decay": 0,
      "amp": 1,
      "attack_level": 1,
      "on": 1,
      "pan_slide": 1,
      "pitch": 0,
      "sustain": 1,
      "pan": 0,
      "amp_slide": 1,
      "release": 0,
      "decay_level": 1,
      "sustain_level": 1,
      "slide": 0,
      "env_curve": 1,
      "attack": 0
    },
    "summary": "Play pattern of notes with specific times",
    "accepts_block": false,
    "introduced": "2,0,0",
    "signature": {
      "times": null,
      "notes": null,
      "*args": null
    },
    "hiden": false
  },
  "sample": {
    "name": "sample",
    "args": [
      {
        "name_or_path": ":symbol_or_string"
      }
    ],
    "intro_fn": true,
    "opts": {
      "clamp_time": 0,
      "hpf_attack": 0,
      "sustain": 1,
      "lpf_min": 30,
      "pan": 0,
      "rpitch": 0,
      "lpf_release_level": 0,
      "hpf_max": 200,
      "compress": 0,
      "hpf_sustain_level": 0,
      "hpf_decay_level": 0,
      "beat_stretch": 1,
      "onset": 0,
      "window_size": 0,
      "path": "/path/to/file",
      "lpf_env_curve": 1,
      "hpf_attack_level": 0,
      "hpf_env_curve": 1,
      "slope_above": 1,
      "lpf_init_level": 30,
      "slide": 0,
      "hpf_release": 0,
      "lpf_decay_level": 0,
      "pre_amp": 1,
      "amp": 1,
      "threshold": 0,
      "norm": 0,
      "hpf_release_level": 0,
      "rate": 1,
      "time_dis": 0,
      "hpf_init_level": 130,
      "lpf_sustain_level": 0,
      "lpf": 131,
      "hpf": 0,
      "pitch_dis": 0,
      "lpf_attack": 0,
      "start": 0,
      "lpf_release": 0,
      "release": 0,
      "hpf_sustain": 0,
      "hpf_decay": 0,
      "finish": 1,
      "slope_below": 1,
      "lpf_decay": 0,
      "lpf_sustain": 0,
      "relax_time": 0,
      "lpf_attack_level": 0,
      "pitch_stretch": 1,
      "pitch": 0,
      "attack": 0
    },
    "requires_block": false,
    "summary": "Trigger sample",
    "accepts_block": true,
    "introduced": "2,0,0",
    "async_block": true,
    "signature": {
      "&blk": null,
      "*args": null
    },
    "hiden": false
  },
  "degree": {
    "name": "degree",
    "args": [],
    "accepts_block": false,
    "inline": true,
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
    "summary": "Convert a degree into a note",
    "introduced": "2,1,0",
    "signature": {
      "degree": null,
      "tonic": null,
      "scale": null
    },
    "hiden": false
  },
  "resolve_sample_paths": {
    "signature": {
      "filts_and_sources": null
    },
    "hiden": true
  },
  "load_sample": {
    "name": "load_sample",
    "args": [
      {
        "path": ":string"
      }
    ],
    "accepts_block": false,
    "summary": "Pre-load first matching sample",
    "introduced": "2,0,0",
    "signature": {
      "*args": null
    },
    "hiden": false
  },
  "current_synth": {
    "name": "current_synth",
    "introduced": "2,0,0",
    "accepts_block": false,
    "summary": "Get current synth",
    "hiden": true
  },
  "hz_to_midi": {
    "name": "hz_to_midi",
    "args": [
      {
        "freq": ":number"
      }
    ],
    "accepts_block": false,
    "inline": true,
    "summary": "Hz to MIDI conversion",
    "introduced": "2,0,0",
    "signature": {
      "freq": null
    },
    "hiden": false
  },
  "note": {
    "name": "note",
    "args": [],
    "opts": {},
    "alt_args": [
      {
        "note": ":symbol"
      }
    ],
    "summary": "Describe note",
    "accepts_block": false,
    "introduced": "2,0,0",
    "signature": {
      "*args": null,
      "n": null
    },
    "hiden": false
  },
  "current_volume": {
    "name": "current_volume",
    "introduced": "2,0,0",
    "accepts_block": false,
    "summary": "Get current volume",
    "hiden": true
  },
  "set_mixer_control": {
    "name": "set_mixer_control!",
    "opts": {
      "pre_amp": 1,
      "hpf": 0,
      "lpf": 131,
      "lpf_bypass": 0,
      "hpf_bypass": 0,
      "amp": 1,
      "limiter_bypass": 0,
      "leak_dc_bypass": 0
    },
    "summary": "Control master mixer",
    "accepts_block": false,
    "introduced": "2,7,0",
    "signature": {
      "opts": null
    },
    "hiden": false,
    "modifies_env": true
  },
  "midi_to_hz": {
    "name": "midi_to_hz",
    "args": [
      {
        "note": ":symbol_or_number"
      }
    ],
    "accepts_block": false,
    "inline": true,
    "summary": "MIDI to Hz conversion",
    "introduced": "2,0,0",
    "signature": {
      "n": null
    },
    "hiden": false
  },
  "current_cent_tuning": {
    "name": "current_cent_tuning",
    "introduced": "2,9,0",
    "accepts_block": false,
    "summary": "Get current cent shift",
    "hiden": true
  },
  "use_external_synths": {
    "signature": {
      "v": null,
      "&block": null
    },
    "hiden": true
  },
  "scale_names": {
    "name": "scale_names",
    "accepts_block": false,
    "memoize": true,
    "introduced": "2,6,0",
    "summary": "All scale names",
    "hiden": true
  },
  "pitch_to_ratio": {
    "name": "pitch_to_ratio",
    "args": [
      {
        "pitch": ":midi_number"
      }
    ],
    "accepts_block": false,
    "inline": true,
    "summary": "relative MIDI pitch to frequency ratio",
    "introduced": "2,5,0",
    "signature": {
      "m": null
    },
    "hiden": false
  },
  "octs": {
    "name": "octs",
    "args": [
      {
        "start": ":note"
      },
      {
        "num_octaves": ":pos_int"
      }
    ],
    "accepts_block": false,
    "inline": true,
    "returns": ":ring",
    "summary": "Create a ring of octaves",
    "introduced": "2,8,0",
    "signature": {
      "start": null,
      "num_octs": 1
    },
    "hiden": false
  },
  "resolve_sample_path": {
    "signature": {
      "filts_and_sources": null
    },
    "hiden": true
  },
  "with_merged_synth_defaults": {
    "name": "with_merged_synth_defaults",
    "opts": {},
    "requires_block": true,
    "summary": "Block-level merge synth defaults",
    "accepts_block": true,
    "introduced": "2,0,0",
    "signature": {
      "&block": null,
      "*args": null
    },
    "hiden": false
  },
  "use_merged_synth_defaults": {
    "name": "use_merged_synth_defaults",
    "opts": {},
    "summary": "Merge synth defaults",
    "accepts_block": false,
    "introduced": "2,0,0",
    "signature": {
      "&block": null,
      "*args": null
    },
    "hiden": false
  },
  "sample_free_all": {
    "name": "sample_free_all",
    "args": [],
    "accepts_block": false,
    "returns": null,
    "introduced": "2,9,0",
    "summary": "Free all loaded samples on the synth server",
    "hiden": false
  },
  "with_timing_warnings": {
    "signature": {
      "v": null,
      "&block": null
    },
    "hiden": true
  },
  "recording_stop": {
    "name": "recording_stop",
    "introduced": "2,0,0",
    "accepts_block": false,
    "summary": "Stop recording",
    "hiden": true
  },
  "use_timing_guarantees": {
    "name": "use_timing_guarantees",
    "args": [
      {
        "bool": ":true_or_false"
      }
    ],
    "accepts_block": false,
    "requires_block": false,
    "summary": "Inhibit synth triggers if too late",
    "introduced": "2,10,0",
    "signature": {
      "v": null,
      "&block": null
    },
    "hiden": false
  },
  "current_arg_checks": {
    "name": "current_arg_checks",
    "introduced": "2,0,0",
    "accepts_block": false,
    "summary": "Get current arg checking status",
    "hiden": true
  },
  "with_synth": {
    "name": "with_synth",
    "args": [
      {
        "synth_name": ":symbol"
      }
    ],
    "accepts_block": true,
    "requires_block": true,
    "summary": "Block-level synth switching",
    "introduced": "2,0,0",
    "signature": {
      "synth_name": null,
      "&block": null,
      "*args": null
    },
    "hiden": false
  },
  "play_pattern": {
    "name": "play_pattern",
    "args": [
      {
        "notes": ":list"
      }
    ],
    "opts": {},
    "summary": "Play pattern of notes",
    "accepts_block": false,
    "introduced": "2,0,0",
    "signature": {
      "notes": null,
      "*args": null
    },
    "hiden": false
  },
  "with_synth_defaults": {
    "name": "with_synth_defaults",
    "opts": {},
    "requires_block": true,
    "summary": "Block-level use new synth defaults",
    "accepts_block": true,
    "introduced": "2,0,0",
    "signature": {
      "&block": null,
      "*args": null
    },
    "hiden": false
  },
  "kill": {
    "name": "kill",
    "args": [
      {
        "node": ":synth_node"
      }
    ],
    "opts": {},
    "summary": "Kill synth",
    "accepts_block": false,
    "introduced": "2,0,0",
    "signature": {
      "node": null
    },
    "hiden": false
  },
  "sample_info": {
    "name": "sample_info",
    "args": [
      {
        "path": ":string"
      }
    ],
    "accepts_block": false,
    "summary": "Get sample information",
    "introduced": "2,0,0",
    "signature": {
      "*args": null
    },
    "hiden": true
  },
  "current_synth_defaults": {
    "name": "current_synth_defaults",
    "introduced": "2,0,0",
    "accepts_block": false,
    "summary": "Get current synth defaults",
    "hiden": true
  },
  "reset_mixer": {
    "name": "reset_mixer!",
    "opts": {},
    "summary": "Reset master mixer",
    "accepts_block": false,
    "introduced": "2,9,0",
    "signature": {
      "": null
    },
    "hiden": false,
    "modifies_env": true
  },
  "set_mixer_invert_stereo!": {
    "hiden": false
  },
  "sample_split_filts_and_opts": {
    "signature": {
      "args": null
    },
    "hiden": true
  },
  "status": {
    "name": "status",
    "introduced": "2,0,0",
    "accepts_block": false,
    "summary": "Get server status",
    "hiden": true
  },
  "scale": {
    "args": [],
    "memoize": true,
    "returns": ":ring",
    "summary": "Create scale",
    "signature": {
      "*opts": null,
      "tonic_or_name": null
    },
    "name": "scale",
    "opts": {
      "num_octaves": 1
    },
    "inline": true,
    "alt_args": [
      {
        "tonic": ":symbol"
      },
      {
        "scale": ":symbol"
      }
    ],
    "intro_fn": true,
    "accepts_block": false,
    "introduced": "2,0,0",
    "hiden": false
  },
  "chord_degree": {
    "name": "chord_degree",
    "args": [
      {
        "number_of_notes": ":int"
      }
    ],
    "accepts_block": false,
    "memoize": true,
    "returns": ":ring",
    "inline": true,
    "summary": "Construct chords of stacked thirds, based on scale degrees",
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
    "introduced": "2,1,0",
    "signature": {
      "degree": null,
      "number_of_notes": 4,
      "*opts": null,
      "tonic": null,
      "scale": ":major"
    },
    "hiden": false
  },
  "invert_chord": {
    "signature": {
      "*args": null
    },
    "hiden": true
  },
  "use_transpose": {
    "name": "use_transpose",
    "args": [
      {
        "note_shift": ":number"
      }
    ],
    "intro_fn": true,
    "accepts_block": false,
    "summary": "Note transposition",
    "introduced": "2,0,0",
    "signature": {
      "shift": null,
      "&block": null
    },
    "hiden": false
  },
  "rest": {
    "name": "rest?",
    "args": [
      {
        "note_or_args": ":number_symbol_or_map"
      }
    ],
    "accepts_block": false,
    "summary": "Determine if note or args is a rest",
    "introduced": "2,1,0",
    "signature": {
      "n": null
    },
    "hiden": false
  },
  "use_synth_defaults": {
    "name": "use_synth_defaults",
    "opts": {},
    "summary": "Use new synth defaults",
    "accepts_block": false,
    "introduced": "2,0,0",
    "signature": {
      "&block": null,
      "*args": null
    },
    "hiden": false
  },
  "synth_names": {
    "name": "synth_names",
    "accepts_block": false,
    "memoize": true,
    "introduced": "2,9,0",
    "summary": "Get all synth names",
    "hiden": true
  },
  "with_arg_checks": {
    "name": "with_arg_checks",
    "args": [
      {
        "true_or_false": ":boolean"
      }
    ],
    "accepts_block": true,
    "requires_block": true,
    "summary": "Block-level enable and disable arg checks",
    "introduced": "2,0,0",
    "signature": {
      "v": null,
      "&block": null
    },
    "hiden": false
  },
  "sample_free": {
    "name": "sample_free",
    "args": [
      {
        "path": ":string"
      }
    ],
    "accepts_block": false,
    "returns": null,
    "summary": "Free a sample on the synth server",
    "introduced": "2,9,0",
    "signature": {
      "*paths": null
    },
    "hiden": false
  },
  "with_debug": {
    "name": "with_debug",
    "args": [
      {
        "true_or_false": ":boolean"
      }
    ],
    "accepts_block": true,
    "requires_block": true,
    "summary": "Block-level enable and disable debug",
    "introduced": "2,0,0",
    "signature": {
      "v": null,
      "&block": null
    },
    "hiden": false
  },
  "current_octave": {
    "name": "current_octave",
    "introduced": "2,9,0",
    "accepts_block": false,
    "summary": "Get current octave shift",
    "hiden": true
  },
  "pitch_ratio": {
    "signature": {
      "*args": null
    },
    "hiden": true
  },
  "with_sample_defaults": {
    "name": "with_sample_defaults",
    "opts": {},
    "requires_block": true,
    "summary": "Block-level use new sample defaults",
    "accepts_block": true,
    "introduced": "2,5,0",
    "signature": {
      "&block": null,
      "*args": null
    },
    "hiden": false
  },
  "current_debug": {
    "name": "current_debug",
    "introduced": "2,0,0",
    "accepts_block": false,
    "summary": "Get current debug status",
    "hiden": true
  },
  "use_timing_warnings": {
    "signature": {
      "v": null,
      "&block": null
    },
    "hiden": true
  },
  "sample_duration": {
    "name": "sample_duration",
    "args": [
      {
        "path": ":string"
      }
    ],
    "opts": {
      "decay": 0,
      "rate": 1,
      "sustain": 1,
      "beat_stretch": 1,
      "start": 0,
      "pitch_stretch": 1,
      "finish": 1,
      "release": 0,
      "attack": 0,
      "rpitch": 0
    },
    "summary": "Get duration of sample in beats",
    "accepts_block": false,
    "introduced": "2,0,0",
    "signature": {
      "*args": null
    },
    "hiden": true
  },
  "load_samples": {
    "name": "load_samples",
    "args": [
      {
        "paths": ":list"
      }
    ],
    "accepts_block": false,
    "summary": "Pre-load all matching samples",
    "introduced": "2,0,0",
    "signature": {
      "*args": null
    },
    "hiden": false
  },
  "recording_start": {
    "name": "recording_start",
    "introduced": "2,0,0",
    "accepts_block": false,
    "summary": "Start recording",
    "hiden": true
  },
  "use_cent_tuning": {
    "name": "use_cent_tuning",
    "args": [
      {
        "cent_shift": ":number"
      }
    ],
    "intro_fn": true,
    "accepts_block": false,
    "summary": "Cent tuning",
    "introduced": "2,9,0",
    "signature": {
      "shift": null,
      "&block": null
    },
    "hiden": false
  },
  "with_fx": {
    "name": "with_fx",
    "args": [
      {
        "fx_name": ":symbol"
      }
    ],
    "intro_fn": true,
    "opts": {
      "reps": 1,
      "kill_delay": 1
    },
    "requires_block": true,
    "summary": "Use Studio FX",
    "accepts_block": true,
    "introduced": "2,0,0",
    "async_block": true,
    "signature": {
      "fx_name": null,
      "&block": null,
      "*args": null
    },
    "hiden": false
  },
  "play_chord": {
    "name": "play_chord",
    "args": [
      {
        "notes": ":list"
      }
    ],
    "opts": {
      "decay": 0,
      "amp": 1,
      "attack_level": 1,
      "on": 1,
      "pan_slide": 1,
      "pitch": 0,
      "sustain": 1,
      "pan": 0,
      "amp_slide": 1,
      "release": 0,
      "decay_level": 1,
      "sustain_level": 1,
      "slide": 0,
      "env_curve": 1,
      "attack": 0
    },
    "summary": "Play notes simultaneously",
    "accepts_block": false,
    "introduced": "2,0,0",
    "signature": {
      "notes": null,
      "*args": null
    },
    "hiden": false
  },
  "sample_groups": {
    "name": "sample_groups",
    "accepts_block": false,
    "memoize": true,
    "introduced": "2,0,0",
    "summary": "Get all sample groups",
    "hiden": true
  },
  "sample_loaded": {
    "name": "sample_loaded?",
    "args": [
      {
        "path": ":string"
      }
    ],
    "accepts_block": false,
    "summary": "Test if sample was pre-loaded",
    "introduced": "2,2,0",
    "signature": {
      "*args": null
    },
    "hiden": false
  },
  "with_arg_bpm_scaling": {
    "name": "with_arg_bpm_scaling",
    "accepts_block": true,
    "requires_block": true,
    "summary": "Block-level enable and disable BPM scaling",
    "introduced": "2,0,0",
    "signature": {
      "&block": null,
      "bool": null
    },
    "hiden": false
  },
  "load_synthdefs": {
    "name": "load_synthdefs",
    "args": [
      {
        "path": ":string"
      }
    ],
    "accepts_block": false,
    "summary": "Load external synthdefs",
    "introduced": "2,0,0",
    "signature": {
      "path": "synthdef_path"
    },
    "hiden": true
  },
  "use_arg_checks": {
    "name": "use_arg_checks",
    "args": [
      {
        "true_or_false": ":boolean"
      }
    ],
    "accepts_block": false,
    "summary": "Enable and disable arg checks",
    "introduced": "2,0,0",
    "signature": {
      "v": null,
      "&block": null
    },
    "hiden": false
  },
  "start_amp_monitor": {
    "hiden": true
  },
  "with_afx": {
    "signature": {
      "fx_name": null,
      "&block": null,
      "*args": null
    },
    "hiden": true
  },
  "use_debug": {
    "name": "use_debug",
    "args": [
      {
        "true_or_false": ":boolean"
      }
    ],
    "accepts_block": false,
    "summary": "Enable and disable debug",
    "introduced": "2,0,0",
    "signature": {
      "v": null,
      "&block": null
    },
    "hiden": false
  },
  "set_sched_ahead_time": {
    "name": "set_sched_ahead_time!",
    "args": [
      {
        "time": ":number"
      }
    ],
    "accepts_block": false,
    "summary": "Set sched ahead time globally",
    "introduced": "2,0,0",
    "signature": {
      "t": null
    },
    "hiden": false,
    "modifies_env": true
  },
  "set_control_delta": {
    "name": "set_control_delta!",
    "args": [
      {
        "time": ":number"
      }
    ],
    "accepts_block": false,
    "summary": "Set control delta globally",
    "introduced": "2,1,0",
    "signature": {
      "t": null
    },
    "hiden": false,
    "modifies_env": true
  },
  "should_trigger": {
    "signature": {
      "args_h": null
    },
    "hiden": false
  },
  "note_list": {
    "args": [],
    "name": "note_list",
    "accepts_block": false,
    "opts": {},
    "summary": "Make a list of notes",
    "signature": {},
    "hiden": false,
    "introduced": "blend-sonic"
  },
  "all_sample_names": {
    "name": "all_sample_names",
    "accepts_block": false,
    "memoize": true,
    "introduced": "2,0,0",
    "summary": "Get all sample names",
    "hiden": true
  },
  "use_fx": {
    "signature": {
      "&block": null,
      "*args": null
    },
    "hiden": true
  },
  "use_octave": {
    "name": "use_octave",
    "args": [
      {
        "octave_shift": ":number"
      }
    ],
    "intro_fn": true,
    "accepts_block": false,
    "summary": "Note octave transposition",
    "introduced": "2,9,0",
    "signature": {
      "shift": null,
      "&block": null
    },
    "hiden": false
  },
  "recording_delete": {
    "name": "recording_delete",
    "accepts_block": false,
    "hiden": true
  },
  "use_sample_bpm": {
    "name": "use_sample_bpm",
    "args": [
      {
        "string_or_number": ":sample_name_or_duration"
      }
    ],
    "opts": {
      "num_beats": 1
    },
    "summary": "Sample-duration-based bpm modification",
    "accepts_block": false,
    "introduced": "2,1,0",
    "signature": {
      "*args": null,
      "sample_name": null
    },
    "hiden": false
  },
  "with_tuning": {
    "name": "with_tuning",
    "args": [
      {
        "tuning": ":symbol"
      },
      {
        "fundamental_note": ":symbol_or_number"
      }
    ],
    "accepts_block": true,
    "requires_block": true,
    "summary": "Block-level tuning modification",
    "introduced": "2,6,0",
    "signature": {
      "fundamental_note": ":c",
      "&block": null,
      "tuning": null
    },
    "hiden": false
  },
  "set_cent_tuning": {
    "name": "set_cent_tuning!",
    "args": [
      {
        "cent_shift": ":number"
      }
    ],
    "intro_fn": false,
    "accepts_block": false,
    "summary": "Global Cent tuning",
    "introduced": "2,10,0",
    "signature": {
      "shift": null
    },
    "hiden": false,
    "modifies_env": true
  },
  "with_timing_guarantees": {
    "name": "with_timing_guarantees",
    "args": [
      {
        "bool": ":true_or_false"
      }
    ],
    "accepts_block": true,
    "requires_block": true,
    "summary": "Block-scoped inhibition of synth triggers if too late",
    "introduced": "2,10,0",
    "signature": {
      "v": null,
      "&block": null
    },
    "hiden": false
  },
  "note_info": {
    "name": "note_info",
    "args": [
      {
        "note": ":symbol_or_number"
      }
    ],
    "opts": {
      "octave": 4
    },
    "summary": "Get note info",
    "accepts_block": false,
    "introduced": "2,0,0",
    "signature": {
      "*args": null,
      "n": null
    },
    "hiden": true
  },
  "sample_names": {
    "name": "sample_names",
    "args": [
      {
        "group": ":symbol"
      }
    ],
    "accepts_block": false,
    "memoize": true,
    "returns": ":ring",
    "summary": "Get sample names",
    "introduced": "2,0,0",
    "signature": {
      "group": null
    },
    "hiden": true
  },
  "chord": {
    "args": [],
    "memoize": true,
    "returns": ":ring",
    "summary": "Create chord",
    "signature": {
      "*opts": null,
      "tonic_or_name": null
    },
    "name": "chord",
    "opts": {
      "invert": 0,
      "num_octaves": 1
    },
    "inline": true,
    "alt_args": [
      {
        "tonic": ":symbol"
      },
      {
        "chord": ":symbol"
      }
    ],
    "intro_fn": true,
    "accepts_block": false,
    "introduced": "2,0,0",
    "hiden": false
  },
  "chord_names": {
    "name": "chord_names",
    "accepts_block": false,
    "memoize": true,
    "introduced": "2,6,0",
    "summary": "All chord names",
    "hiden": true
  },
  "with_transpose": {
    "name": "with_transpose",
    "args": [
      {
        "note_shift": ":number"
      }
    ],
    "accepts_block": true,
    "requires_block": true,
    "summary": "Block-level note transposition",
    "introduced": "2,0,0",
    "signature": {
      "shift": null,
      "&block": null
    },
    "hiden": false
  },
  "with_merged_sample_defaults": {
    "name": "with_merged_sample_defaults",
    "opts": {},
    "requires_block": true,
    "summary": "Block-level use merged sample defaults",
    "accepts_block": true,
    "introduced": "2,9,0",
    "signature": {
      "&block": null,
      "*args": null
    },
    "hiden": false
  },
  "control": {
    "name": "control",
    "args": [
      {
        "node": ":synth_node"
      }
    ],
    "opts": {},
    "summary": "Control running synth",
    "accepts_block": false,
    "introduced": "2,0,0",
    "signature": {
      "*args": null
    },
    "hiden": false
  },
  "set_mixer_standard_stereo!": {
    "hiden": false
  },
  "with_cent_tuning": {
    "name": "with_cent_tuning",
    "args": [
      {
        "cent_shift": ":number"
      }
    ],
    "accepts_block": true,
    "requires_block": true,
    "summary": "Block-level cent tuning",
    "introduced": "2,9,0",
    "signature": {
      "shift": null,
      "&block": null
    },
    "hiden": false
  },
  "play": {
    "name": "play",
    "args": [
      {
        "note": ":symbol_or_number"
      }
    ],
    "intro_fn": true,
    "opts": {
      "decay": 0,
      "amp": 1,
      "attack_level": 1,
      "on": 1,
      "pan_slide": 1,
      "pitch": 0,
      "sustain": 1,
      "pan": 0,
      "amp_slide": 1,
      "release": 0,
      "decay_level": 1,
      "sustain_level": 1,
      "slide": 0,
      "env_curve": 1,
      "attack": 0
    },
    "requires_block": false,
    "summary": "Play current synth",
    "accepts_block": true,
    "introduced": "2,0,0",
    "async_block": true,
    "signature": {
      "&blk": null,
      "*args": null,
      "n": null
    },
    "hiden": false
  },
  "with_octave": {
    "name": "with_octave",
    "args": [
      {
        "octave_shift": ":number"
      }
    ],
    "intro_fn": true,
    "accepts_block": true,
    "requires_block": true,
    "summary": "Block level octave transposition",
    "introduced": "2,9,0",
    "signature": {
      "shift": null,
      "&block": null
    },
    "hiden": false
  },
  "chord_invert": {
    "name": "chord_invert",
    "args": [
      {
        "notes": ":list"
      },
      {
        "shift": ":number"
      }
    ],
    "accepts_block": false,
    "inline": true,
    "returns": ":ring",
    "summary": "Chord inversion",
    "introduced": "2,6,0",
    "signature": {
      "shift": null,
      "notes": null
    },
    "hiden": false
  },
  "ratio_to_pitch": {
    "name": "ratio_to_pitch",
    "args": [
      {
        "ratio": ":number"
      }
    ],
    "accepts_block": false,
    "inline": true,
    "summary": "relative frequency ratio to MIDI pitch",
    "introduced": "2,7,0",
    "signature": {
      "r": null
    },
    "hiden": false
  },
  "sample_buffer": {
    "name": "sample_buffer",
    "args": [
      {
        "path": ":string"
      }
    ],
    "accepts_block": false,
    "summary": "Get sample data",
    "introduced": "2,0,0",
    "signature": {
      "*args": null
    },
    "hiden": true
  },
  "note_range": {
    "name": "note_range",
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
    "inline": true,
    "returns": ":ring",
    "summary": "Get a range of notes",
    "accepts_block": false,
    "introduced": "2,6,0",
    "signature": {
      "low_note": null,
      "*opts": null,
      "high_note": null
    },
    "hiden": false
  },
  "current_sample_defaults": {
    "name": "current_sample_defaults",
    "introduced": "2,5,0",
    "accepts_block": false,
    "summary": "Get current sample defaults",
    "hiden": true
  },
  "current_sched_ahead_time": {
    "name": "current_sched_ahead_time",
    "introduced": "2,0,0",
    "accepts_block": false,
    "summary": "Get current sched ahead time",
    "hiden": true
  },
  "use_synth": {
    "name": "use_synth",
    "args": [
      {
        "synth_name": ":symbol"
      }
    ],
    "intro_fn": true,
    "accepts_block": false,
    "summary": "Switch current synth",
    "introduced": "2,0,0",
    "signature": {
      "synth_name": null,
      "&block": null,
      "*args": null
    },
    "hiden": false
  },
  "with_sample_bpm": {
    "name": "with_sample_bpm",
    "args": [
      {
        "string_or_number": ":sample_name_or_duration"
      }
    ],
    "opts": {
      "num_beats": 1
    },
    "requires_block": true,
    "summary": "Block-scoped sample-duration-based bpm modification",
    "accepts_block": true,
    "introduced": "2,1,0",
    "signature": {
      "*args": null,
      "&block": null,
      "sample_name": null
    },
    "hiden": false
  },
  "use_merged_sample_defaults": {
    "name": "use_merged_sample_defaults",
    "opts": {},
    "summary": "Merge new sample defaults",
    "accepts_block": false,
    "introduced": "2,9,0",
    "signature": {
      "&block": null,
      "*args": null
    },
    "hiden": false
  },
  "set_mixer_mono_mode!": {
    "hiden": false
  },
  "set_mixer_stereo_mode!": {
    "hiden": false
  }
}

sound_args_types_conversion = {}

sound_opts_types_conversion = {}

#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/

synths = {
  "DarkSeaHorn": {
    "name": ":dark_sea_horn",
    "opts": {
      "decay": 0,
      "note_slide_curve": 0,
      "pan_slide_curve": 0,
      "note_slide": 0,
      "pan_slide": 0,
      "amp_slide_shape": 1,
      "note": 52,
      "sustain": 0,
      "amp": 1,
      "pan": 0,
      "attack": 1,
      "env_curve": 2,
      "pan_slide_shape": 1,
      "note_slide_shape": 1,
      "decay_level": 1,
      "sustain_level": 1,
      "attack_level": 1,
      "release": 4.0,
      "amp_slide_curve": 0,
      "amp_slide": 0
    },
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false,
    "summary": "Dark Sea Horn",
    "hiden": true
  },
  "TB303": {
    "name": ":tb303",
    "opts": {
      "note_slide_curve": 0,
      "pan_slide_curve": 0,
      "note_slide": 0,
      "cutoff": 120,
      "res": 0.9,
      "cutoff_decay": 0,
      "note": 52,
      "sustain": 0,
      "cutoff_attack": 0,
      "pan": 0,
      "pulse_width": 0.5,
      "pan_slide_shape": 1,
      "note_slide_shape": 1,
      "pulse_width_slide_shape": 1,
      "attack_level": 1,
      "cutoff_release": 1,
      "cutoff_min_slide_curve": 0,
      "cutoff_slide_shape": 1,
      "cutoff_slide_curve": 0,
      "env_curve": 2,
      "attack": 0,
      "decay_level": 1,
      "pulse_width_slide": 0,
      "decay": 0,
      "amp": 1,
      "res_slide_shape": 1,
      "pan_slide": 0,
      "amp_slide_shape": 1,
      "pulse_width_slide_curve": 0,
      "cutoff_min_slide": 0,
      "cutoff_min_slide_shape": 1,
      "release": 1,
      "sustain_level": 1,
      "cutoff_decay_level": 1,
      "cutoff_slide": 0,
      "cutoff_sustain": 0,
      "wave": 0,
      "res_slide": 0,
      "cutoff_attack_level": 1,
      "cutoff_sustain_level": 1,
      "amp_slide_curve": 0,
      "amp_slide": 0,
      "res_slide_curve": 0,
      "cutoff_min": 30
    },
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false,
    "summary": "TB-303 Emulation",
    "hiden": false
  },
  "DTri": {
    "name": ":dtri",
    "opts": {
      "decay": 0,
      "note_slide_curve": 0,
      "pan_slide_curve": 0,
      "note_slide": 0,
      "detune_slide_curve": 0,
      "cutoff": 100,
      "pan_slide": 0,
      "amp_slide_shape": 1,
      "note": 52,
      "sustain": 0,
      "pan": 0,
      "pan_slide_shape": 1,
      "note_slide_shape": 1,
      "sustain_level": 1,
      "amp_slide_curve": 0,
      "attack_level": 1,
      "release": 1,
      "amp": 1,
      "cutoff_slide": 0,
      "cutoff_slide_shape": 1,
      "cutoff_slide_curve": 0,
      "env_curve": 2,
      "detune_slide": 0,
      "detune_slide_shape": 1,
      "attack": 0,
      "decay_level": 1,
      "detune": 0.1,
      "amp_slide": 0
    },
    "inherit_base": "DSaw",
    "inherit_arg": true,
    "summary": "Detuned Triangle Wave",
    "hiden": true
  },
  "Pulse": {
    "name": ":pulse",
    "opts": {
      "decay": 0,
      "note_slide_curve": 0,
      "pan_slide_curve": 0,
      "note_slide": 0,
      "cutoff": 100,
      "pan_slide": 0,
      "amp_slide_shape": 1,
      "note": 52,
      "sustain": 0,
      "pan": 0,
      "pulse_width": 0.5,
      "pan_slide_shape": 1,
      "note_slide_shape": 1,
      "pulse_width_slide_shape": 1,
      "sustain_level": 1,
      "attack_level": 1,
      "release": 1,
      "amp": 1,
      "cutoff_slide": 0,
      "cutoff_slide_shape": 1,
      "cutoff_slide_curve": 0,
      "env_curve": 2,
      "attack": 0,
      "decay_level": 1,
      "amp_slide_curve": 0,
      "amp_slide": 0,
      "pulse_width_slide": 0
    },
    "inherit_base": "Square",
    "inherit_arg": true,
    "summary": "Pulse Wave",
    "hiden": true
  },
  "StereoPlayer": {
    "name": ":stereo_player",
    "opts": {
      "hpf_max_slide_shape": 1,
      "hpf_attack": 0,
      "hpf_sustain_level": -1,
      "pan": 0,
      "lpf_slide_curve": 0,
      "lpf_release_level": -1,
      "pan_slide_shape": 1,
      "hpf_max": -1,
      "decay_level": 1,
      "attack_level": 1,
      "threshold_slide": 0,
      "compress": 0,
      "lpf_slide": 0,
      "hpf_decay_level": -1,
      "clamp_time_slide_curve": 0,
      "pre_amp_slide_shape": 1,
      "clamp_time_slide_shape": 1,
      "time_dis_slide": 0,
      "hpf_attack_level": -1,
      "hpf_env_curve": 2,
      "slope_above": 0.5,
      "pitch": 0,
      "lpf_decay_level": -1,
      "pre_amp": 1,
      "amp": 1,
      "hpf_slide_curve": 0,
      "hpf_release_level": -1,
      "threshold_slide_curve": 0,
      "slope_above_slide": 0,
      "time_dis": 0.0,
      "pre_amp_slide": 0,
      "pitch_dis_slide": 0,
      "pitch_dis_slide_shape": 1,
      "sustain": -1,
      "relax_time_slide_shape": 1,
      "rate": 1,
      "release": 0,
      "pitch_slide": 0,
      "hpf_sustain": -1,
      "clamp_time": 0.01,
      "hpf_max_slide_curve": 0,
      "hpf_release": 0,
      "lpf_sustain": -1,
      "slope_above_slide_shape": 1,
      "lpf_attack_level": -1,
      "pitch_dis_slide_curve": 0,
      "finish": 1,
      "hpf_max_slide": 0,
      "env_curve": 2,
      "lpf_min_slide": 0,
      "lpf_min": -1,
      "pitch_slide_shape": 1,
      "hpf_slide_shape": 1,
      "clamp_time_slide": 0,
      "slope_below_slide": 0,
      "window_size": 0.2,
      "lpf_env_curve": 2,
      "lpf_min_slide_shape": 1,
      "hpf_slide": 0,
      "norm": 0,
      "window_size_slide_shape": 1,
      "lpf_init_level": -1,
      "lpf_decay": 0,
      "slope_below_slide_shape": 1,
      "decay": 0,
      "lpf_slide_shape": 1,
      "slope_above_slide_curve": 0,
      "pre_amp_slide_curve": 0,
      "threshold": 0.2,
      "pan_slide": 0,
      "amp_slide_shape": 1,
      "hpf_init_level": -1,
      "lpf_sustain_level": -1,
      "pitch_slide_curve": 0,
      "relax_time_slide_curve": 0,
      "lpf": -1,
      "sustain_level": 1,
      "hpf": -1,
      "pitch_dis": 0.0,
      "lpf_attack": 0,
      "threshold_slide_shape": 1,
      "start": 0,
      "lpf_release": 0,
      "time_dis_slide_curve": 0,
      "window_size_slide": 0,
      "lpf_min_slide_curve": 0,
      "amp_slide_curve": 0,
      "window_size_slide_curve": 0,
      "slope_below": 1,
      "slope_below_slide_curve": 0,
      "attack": 0,
      "relax_time": 0.01,
      "pan_slide_curve": 0,
      "relax_time_slide": 0,
      "hpf_decay": 0,
      "amp_slide": 0,
      "time_dis_slide_shape": 1
    },
    "inherit_base": "MonoPlayer",
    "inherit_arg": true,
    "summary": "Stereo Sample Player",
    "hiden": true
  },
  "ModFM": {
    "name": ":mod_fm",
    "opts": {
      "note_slide_curve": 0,
      "pan_slide_curve": 0,
      "note_slide": 0,
      "cutoff": 100,
      "env_curve": 2,
      "note": 52,
      "mod_wave": 1,
      "sustain": 0,
      "pan": 0,
      "depth_slide_curve": 0,
      "divisor_slide_shape": 1,
      "pan_slide_shape": 1,
      "note_slide_shape": 1,
      "attack_level": 1,
      "mod_invert_wave": 0,
      "divisor_slide_curve": 0,
      "depth_slide_shape": 1,
      "divisor_slide": 0,
      "cutoff_slide_shape": 1,
      "cutoff_slide_curve": 0,
      "mod_pulse_width": 0.5,
      "mod_range": 5,
      "decay_level": 1,
      "decay": 0,
      "depth_slide": 0,
      "amp": 1,
      "pan_slide": 0,
      "amp_slide_shape": 1,
      "depth": 1,
      "sustain_level": 1,
      "divisor": 2,
      "release": 1,
      "cutoff_slide": 0,
      "mod_phase_offset": 0,
      "attack": 0,
      "mod_phase": 0.25,
      "amp_slide_curve": 0,
      "amp_slide": 0
    },
    "inherit_base": "FM",
    "inherit_arg": true,
    "summary": "Basic FM synthesis with frequency modulation.",
    "hiden": true
  },
  "SubPulse": {
    "name": ":subpulse",
    "opts": {
      "decay": 0,
      "note_slide_curve": 0,
      "sub_amp": 1,
      "pan_slide_curve": 0,
      "note_slide": 0,
      "sub_detune_slide_shape": 1,
      "cutoff": 100,
      "pan_slide": 0,
      "amp_slide_shape": 1,
      "note": 52,
      "sub_detune_slide": 0,
      "sustain": 0,
      "sub_amp_slide_curve": 0,
      "pan": 0,
      "pulse_width": 0.5,
      "pan_slide_shape": 1,
      "note_slide_shape": 1,
      "sustain_level": 1,
      "pulse_width_slide_shape": 1,
      "attack_level": 1,
      "sub_detune": -12,
      "release": 1,
      "amp": 1,
      "cutoff_slide": 0,
      "cutoff_slide_shape": 1,
      "cutoff_slide_curve": 0,
      "env_curve": 2,
      "amp_slide": 0,
      "decay_level": 1,
      "sub_amp_slide": 0,
      "sub_amp_slide_shape": 1,
      "amp_slide_curve": 0,
      "attack": 0,
      "pulse_width_slide": 0
    },
    "inherit_base": "Pulse",
    "inherit_arg": true,
    "summary": "Pulse Wave with sub",
    "hiden": true
  },
  "ModDSaw": {
    "name": ":mod_dsaw",
    "opts": {
      "decay": 0,
      "note_slide_curve": 0,
      "pan_slide_curve": 0,
      "note_slide": 0,
      "detune_slide_curve": 0,
      "cutoff": 100,
      "pan_slide": 0,
      "amp_slide_shape": 1,
      "note": 52,
      "mod_range_slide": 0,
      "sustain": 0,
      "mod_range_slide_shape": 1,
      "pan": 0,
      "pan_slide_shape": 1,
      "note_slide_shape": 1,
      "mod_pulse_width_slide_curve": 0,
      "mod_phase_slide_shape": 1,
      "detune_slide": 0,
      "sustain_level": 1,
      "mod_invert_wave": 0,
      "attack_level": 1,
      "mod_wave": 1,
      "detune_slide_shape": 1,
      "release": 1,
      "amp": 1,
      "cutoff_slide": 0,
      "mod_phase_offset": 0,
      "cutoff_slide_shape": 1,
      "cutoff_slide_curve": 0,
      "mod_pulse_width": 0.5,
      "env_curve": 2,
      "mod_pulse_width_slide_shape": 1,
      "mod_range_slide_curve": 0,
      "amp_slide": 0,
      "mod_phase_slide_curve": 0,
      "mod_range": 5,
      "mod_phase": 0.25,
      "decay_level": 1,
      "mod_phase_slide": 0,
      "detune": 0.1,
      "amp_slide_curve": 0,
      "attack": 0,
      "mod_pulse_width_slide": 0
    },
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false,
    "summary": "Modulated Detuned Saw Waves",
    "hiden": false
  },
  "ChipBass": {
    "name": ":chipbass",
    "opts": {
      "decay": 0,
      "note_slide_curve": 0,
      "pan_slide_curve": 0,
      "note_slide": 0,
      "attack": 0,
      "pan_slide": 0,
      "amp_slide_shape": 1,
      "note": 60,
      "sustain": 0,
      "amp": 1,
      "pan": 0,
      "amp_slide": 0,
      "env_curve": 2,
      "pan_slide_shape": 1,
      "note_slide_shape": 1,
      "decay_level": 1,
      "sustain_level": 1,
      "attack_level": 1,
      "release": 1,
      "amp_slide_curve": 0,
      "note_resolution": 0.1
    },
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false,
    "summary": "Chip Bass",
    "hiden": false
  },
  "Noise": {
    "name": ":noise",
    "opts": {
      "decay": 0,
      "res": 0,
      "pan_slide_curve": 0,
      "attack_level": 1,
      "cutoff": 110,
      "pan_slide": 0,
      "amp_slide_shape": 1,
      "amp": 1,
      "pan": 0,
      "pan_slide_shape": 1,
      "sustain_level": 1,
      "res_slide_shape": 1,
      "res_slide": 0,
      "sustain": 0,
      "release": 1,
      "cutoff_slide": 0,
      "cutoff_slide_shape": 1,
      "cutoff_slide_curve": 0,
      "env_curve": 2,
      "amp_slide": 0,
      "decay_level": 1,
      "amp_slide_curve": 0,
      "attack": 0,
      "res_slide_curve": 0
    },
    "inherit_base": "Pitchless",
    "inherit_arg": false,
    "summary": "Noise",
    "hiden": false
  },
  "ModPulse": {
    "name": ":mod_pulse",
    "opts": {
      "decay": 0,
      "note_slide_curve": 0,
      "pan_slide_curve": 0,
      "note_slide": 0,
      "cutoff": 100,
      "pan_slide": 0,
      "amp_slide_shape": 1,
      "note": 52,
      "mod_range_slide": 0,
      "sustain": 0,
      "mod_range_slide_shape": 1,
      "pan": 0,
      "pulse_width": 0.5,
      "pan_slide_shape": 1,
      "note_slide_shape": 1,
      "mod_pulse_width_slide_curve": 0,
      "mod_phase_slide_shape": 1,
      "pulse_width_slide_shape": 1,
      "sustain_level": 1,
      "pulse_width_slide_curve": 0,
      "mod_invert_wave": 0,
      "attack_level": 1,
      "mod_wave": 1,
      "release": 1,
      "amp": 1,
      "cutoff_slide": 0,
      "mod_phase_offset": 0,
      "cutoff_slide_shape": 1,
      "cutoff_slide_curve": 0,
      "mod_pulse_width": 0.5,
      "env_curve": 2,
      "mod_pulse_width_slide_shape": 1,
      "mod_range_slide_curve": 0,
      "amp_slide": 0,
      "mod_phase_slide_curve": 0,
      "mod_range": 5,
      "mod_phase": 0.25,
      "decay_level": 1,
      "mod_phase_slide": 0,
      "amp_slide_curve": 0,
      "attack": 0,
      "mod_pulse_width_slide": 0,
      "pulse_width_slide": 0
    },
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false,
    "summary": "Modulated Pulse",
    "hiden": false
  },
  "SynthPiano": {
    "name": ":piano",
    "opts": {
      "decay": 0,
      "note_slide_curve": 0,
      "pan_slide_curve": 0,
      "note_slide": 0,
      "pan_slide": 0,
      "amp_slide_shape": 1,
      "note": 52,
      "sustain": 0,
      "pan": 0,
      "pan_slide_shape": 1,
      "note_slide_shape": 1,
      "sustain_level": 1,
      "vel": 0.2,
      "attack_level": 1,
      "release": 1,
      "amp": 1,
      "amp_slide": 0,
      "stereo_width": 0,
      "decay_level": 1,
      "amp_slide_curve": 0,
      "attack": 0,
      "hard": 0.5
    },
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false,
    "summary": "SynthPiano",
    "hiden": false
  },
  "ModTri": {
    "name": ":mod_tri",
    "opts": {
      "decay": 0,
      "note_slide_curve": 0,
      "pan_slide_curve": 0,
      "note_slide": 0,
      "cutoff": 100,
      "pan_slide": 0,
      "amp_slide_shape": 1,
      "note": 52,
      "mod_range_slide": 0,
      "sustain": 0,
      "mod_range_slide_shape": 1,
      "pan": 0,
      "pan_slide_shape": 1,
      "note_slide_shape": 1,
      "mod_pulse_width_slide_curve": 0,
      "mod_phase_slide_shape": 1,
      "sustain_level": 1,
      "mod_invert_wave": 0,
      "attack_level": 1,
      "mod_wave": 1,
      "release": 1,
      "amp": 1,
      "cutoff_slide": 0,
      "mod_phase_offset": 0,
      "cutoff_slide_shape": 1,
      "cutoff_slide_curve": 0,
      "mod_pulse_width": 0.5,
      "env_curve": 2,
      "mod_pulse_width_slide_shape": 1,
      "mod_range_slide_curve": 0,
      "amp_slide": 0,
      "mod_phase_slide_curve": 0,
      "mod_range": 5,
      "mod_phase": 0.25,
      "decay_level": 1,
      "mod_phase_slide": 0,
      "amp_slide_curve": 0,
      "attack": 0,
      "mod_pulse_width_slide": 0
    },
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false,
    "summary": "Modulated Triangle Wave",
    "hiden": false
  },
  "ChipNoise": {
    "name": ":chipnoise",
    "opts": {
      "decay": 0,
      "freq_band_slide": 0,
      "pan_slide_curve": 0,
      "amp": 1,
      "freq_band_slide_shape": 1,
      "pan_slide": 0,
      "amp_slide_shape": 0,
      "sustain": 1,
      "freq_band": 0,
      "pan": 0,
      "attack": 0,
      "env_curve": 0,
      "pan_slide_shape": 1,
      "decay_level": 1,
      "sustain_level": 1,
      "attack_level": 1,
      "release": 0,
      "amp_slide_curve": 1,
      "amp_slide": 0,
      "freq_band_slide_curve": 0
    },
    "inherit_base": "Noise",
    "inherit_arg": false,
    "summary": "Chip Noise",
    "hiden": true
  },
  "MainMixer": {
    "name": ":mixer",
    "opts": {
      "lpf_slide_shape": 1,
      "pre_amp": 1,
      "pre_amp_slide_curve": 0,
      "hpf_slide_curve": 0,
      "amp_slide_shape": 1,
      "pre_amp_slide_shape": 1,
      "invert_stereo": 0,
      "amp": 1,
      "pre_amp_slide": 0.02,
      "amp_slide": 0.02,
      "lpf_slide_curve": 0,
      "lpf_bypass": 0,
      "hpf_slide": 0.02,
      "limiter_bypass": 0,
      "lpf": 135.5,
      "hpf_slide_shape": 1,
      "hpf_bypass": 0,
      "force_mono": 0,
      "hpf": 0,
      "amp_slide_curve": 0,
      "lpf_slide": 0.02
    },
    "inherit_base": "BaseMixer",
    "inherit_arg": false,
    "summary": "Main Mixer",
    "hiden": true
  },
  "Prophet": {
    "name": ":prophet",
    "opts": {
      "decay": 0,
      "note_slide_curve": 0,
      "pan_slide_curve": 0,
      "note_slide": 0,
      "cutoff": 110,
      "pan_slide": 0,
      "amp_slide_shape": 1,
      "note": 52,
      "sustain": 0,
      "pan": 0,
      "res": 0.7,
      "pan_slide_shape": 1,
      "note_slide_shape": 1,
      "sustain_level": 1,
      "res_slide": 0,
      "res_slide_shape": 1,
      "attack_level": 1,
      "release": 1,
      "amp": 1,
      "cutoff_slide": 0,
      "cutoff_slide_shape": 1,
      "cutoff_slide_curve": 0,
      "env_curve": 2,
      "amp_slide": 0,
      "decay_level": 1,
      "amp_slide_curve": 0,
      "attack": 0,
      "res_slide_curve": 0
    },
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false,
    "summary": "The Prophet",
    "hiden": false
  },
  "PrettyBell": {
    "name": ":pretty_bell",
    "opts": {
      "decay": 0,
      "note_slide_curve": 0,
      "pan_slide_curve": 0,
      "note_slide": 0,
      "pan_slide": 0,
      "amp_slide_shape": 1,
      "note": 52,
      "sustain": 0,
      "pan": 0,
      "pan_slide_shape": 1,
      "note_slide_shape": 1,
      "sustain_level": 1,
      "attack_level": 1,
      "release": 1,
      "amp": 1,
      "env_curve": 2,
      "amp_slide": 0,
      "decay_level": 1,
      "amp_slide_curve": 0,
      "attack": 0
    },
    "inherit_base": "DullBell",
    "inherit_arg": true,
    "summary": "Pretty Bell",
    "hiden": true
  },
  "BasicMonoPlayer": {
    "name": ":basic_mono_player",
    "opts": {
      "rate": 1,
      "pan_slide_curve": 0,
      "hpf_slide_curve": 0,
      "pan_slide": 0,
      "amp_slide_shape": 1,
      "amp": 1,
      "pan": 0,
      "lpf_slide": 0,
      "lpf_slide_curve": 0,
      "hpf_slide": 0,
      "pan_slide_shape": 1,
      "lpf": -1,
      "hpf_slide_shape": 1,
      "lpf_slide_shape": 1,
      "hpf": -1,
      "amp_slide_curve": 0,
      "amp_slide": 0
    },
    "inherit_base": "StudioInfo",
    "inherit_arg": false,
    "summary": "Basic Mono Sample Player (no env)",
    "hiden": true
  },
  "Zawa": {
    "name": ":zawa",
    "opts": {
      "decay": 0,
      "note_slide_curve": 0,
      "pan_slide_curve": 0,
      "note_slide": 0,
      "range_slide": 0,
      "cutoff": 100,
      "pan_slide": 0,
      "amp_slide_shape": 1,
      "note": 52,
      "phase_slide_shape": 1,
      "sustain": 0,
      "range_slide_curve": 0,
      "pan": 0,
      "res": 0.9,
      "pulse_width": 0.5,
      "invert_wave": 0,
      "pan_slide_shape": 1,
      "note_slide_shape": 1,
      "phase": 1,
      "disable_wave": 0,
      "sustain_level": 1,
      "res_slide": 0,
      "res_slide_shape": 1,
      "attack_level": 1,
      "pulse_width_slide_shape": 1,
      "release": 1,
      "amp": 1,
      "cutoff_slide": 0,
      "cutoff_slide_shape": 1,
      "cutoff_slide_curve": 0,
      "wave": 3,
      "phase_slide_curve": 0,
      "range": 24,
      "amp_slide": 0,
      "phase_slide": 0,
      "phase_offset": 0,
      "decay_level": 1,
      "pulse_width_slide_curve": 0,
      "range_slide_shape": 1,
      "amp_slide_curve": 0,
      "attack": 0,
      "res_slide_curve": 0,
      "pulse_width_slide": 0
    },
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false,
    "summary": "Zawa",
    "hiden": false
  },
  "Tri": {
    "name": ":tri",
    "opts": {
      "decay": 0,
      "note_slide_curve": 0,
      "pan_slide_curve": 0,
      "note_slide": 0,
      "cutoff": 100,
      "pan_slide": 0,
      "amp_slide_shape": 1,
      "note": 52,
      "sustain": 0,
      "pan": 0,
      "pulse_width": 0.5,
      "pan_slide_shape": 1,
      "note_slide_shape": 1,
      "sustain_level": 1,
      "pulse_width_slide_shape": 1,
      "attack_level": 1,
      "release": 1,
      "amp": 1,
      "cutoff_slide": 0,
      "cutoff_slide_shape": 1,
      "cutoff_slide_curve": 0,
      "env_curve": 2,
      "amp_slide": 0,
      "decay_level": 1,
      "amp_slide_curve": 0,
      "attack": 0,
      "pulse_width_slide": 0
    },
    "inherit_base": "Pulse",
    "inherit_arg": true,
    "summary": "Triangle Wave",
    "hiden": true
  },
  "Growl": {
    "name": ":growl",
    "opts": {
      "decay": 0,
      "note_slide_curve": 0,
      "pan_slide_curve": 0,
      "note_slide": 0,
      "cutoff": 130,
      "pan_slide": 0,
      "amp_slide_shape": 1,
      "note": 52,
      "sustain": 0,
      "pan": 0,
      "res": 0.7,
      "pan_slide_shape": 1,
      "note_slide_shape": 1,
      "sustain_level": 1,
      "res_slide": 0,
      "res_slide_shape": 1,
      "attack_level": 1,
      "release": 1,
      "amp": 1,
      "cutoff_slide": 0,
      "cutoff_slide_shape": 1,
      "cutoff_slide_curve": 0,
      "env_curve": 2,
      "amp_slide": 0,
      "decay_level": 1,
      "amp_slide_curve": 0,
      "attack": 0.1,
      "res_slide_curve": 0
    },
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false,
    "summary": "Growl",
    "hiden": false
  },
  "Saw": {
    "name": ":saw",
    "opts": {
      "decay": 0,
      "note_slide_curve": 0,
      "pan_slide_curve": 0,
      "note_slide": 0,
      "pan_slide": 0,
      "amp_slide_shape": 1,
      "note": 52,
      "sustain": 0,
      "pan": 0,
      "pan_slide_shape": 1,
      "note_slide_shape": 1,
      "sustain_level": 1,
      "attack_level": 1,
      "release": 1,
      "amp": 1,
      "env_curve": 2,
      "amp_slide": 0,
      "decay_level": 1,
      "amp_slide_curve": 0,
      "attack": 0
    },
    "inherit_base": "Beep",
    "inherit_arg": true,
    "summary": "Saw Wave",
    "hiden": true
  },
  "SynthPluck": {
    "name": ":pluck",
    "opts": {
      "decay": 0,
      "note_slide_curve": 0,
      "pan_slide_curve": 0,
      "note_slide": 0,
      "pan_slide": 0,
      "amp_slide_shape": 1,
      "note": 52,
      "sustain": 0,
      "noise_amp": 0.8,
      "pan": 0,
      "pan_slide_shape": 1,
      "note_slide_shape": 1,
      "max_delay_time": 0.125,
      "sustain_level": 1,
      "attack_level": 1,
      "coef": 0.3,
      "release": 1,
      "amp": 1,
      "amp_slide": 0,
      "decay_level": 1,
      "pluck_decay": 30,
      "amp_slide_curve": 0,
      "attack": 0
    },
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false,
    "summary": "SynthPluck",
    "hiden": false
  },
  "SynthInfo": {
    "inherit_arg": true,
    "opts": {},
    "hiden": true,
    "inherit_base": "BaseInfo"
  },
  "MonoPlayer": {
    "name": ":mono_player",
    "opts": {
      "hpf_max_slide_shape": 1,
      "hpf_attack": 0,
      "hpf_sustain_level": -1,
      "pan": 0,
      "lpf_slide_curve": 0,
      "lpf_release_level": -1,
      "pan_slide_shape": 1,
      "hpf_max": -1,
      "lpf_min_slide_curve": 0,
      "attack_level": 1,
      "threshold_slide": 0,
      "compress": 0,
      "lpf_slide": 0,
      "hpf_decay_level": -1,
      "time_dis_slide": 0,
      "pre_amp_slide_shape": 1,
      "clamp_time_slide_shape": 1,
      "clamp_time_slide_curve": 0,
      "hpf_attack_level": -1,
      "hpf_env_curve": 2,
      "slope_above": 0.5,
      "lpf_decay_level": -1,
      "pre_amp": 1,
      "lpf_min_slide": 0,
      "norm": 0,
      "hpf_release_level": -1,
      "threshold_slide_curve": 0,
      "slope_above_slide": 0,
      "time_dis": 0.0,
      "pre_amp_slide": 0,
      "pitch_dis_slide_shape": 1,
      "relax_time_slide_shape": 1,
      "rate": 1,
      "release": 0,
      "pitch_slide": 0,
      "hpf_sustain": -1,
      "clamp_time": 0.01,
      "hpf_max_slide_curve": 0,
      "lpf_decay": 0,
      "lpf_sustain": -1,
      "slope_above_slide_shape": 1,
      "finish": 1,
      "pitch_dis_slide_curve": 0,
      "amp": 1,
      "pan_slide_curve": 0,
      "hpf_max_slide": 0,
      "env_curve": 2,
      "sustain": -1,
      "slope_above_slide_curve": 0,
      "pitch_slide_shape": 1,
      "hpf_slide_shape": 1,
      "clamp_time_slide": 0,
      "hpf_slide_curve": 0,
      "slope_below_slide": 0,
      "window_size": 0.2,
      "pan_slide": 0,
      "lpf_min_slide_shape": 1,
      "hpf_slide": 0,
      "lpf_attack_level": -1,
      "decay_level": 1,
      "window_size_slide_shape": 1,
      "lpf_init_level": -1,
      "hpf_release": 0,
      "slope_below_slide_shape": 1,
      "decay": 0,
      "lpf_slide_shape": 1,
      "lpf_min": -1,
      "pre_amp_slide_curve": 0,
      "threshold": 0.2,
      "lpf_env_curve": 2,
      "amp_slide_shape": 1,
      "hpf_init_level": -1,
      "lpf_sustain_level": -1,
      "pitch_slide_curve": 0,
      "relax_time_slide_curve": 0,
      "lpf": -1,
      "sustain_level": 1,
      "hpf": -1,
      "pitch_dis": 0.0,
      "hpf_decay": 0,
      "lpf_attack": 0,
      "threshold_slide_shape": 1,
      "start": 0,
      "lpf_release": 0,
      "time_dis_slide_curve": 0,
      "window_size_slide": 0,
      "pitch_dis_slide": 0,
      "amp_slide_curve": 0,
      "window_size_slide_curve": 0,
      "slope_below": 1,
      "slope_below_slide_curve": 0,
      "amp_slide": 0,
      "relax_time": 0.01,
      "relax_time_slide": 0,
      "pitch": 0,
      "attack": 0,
      "time_dis_slide_shape": 1
    },
    "inherit_base": "BasicMonoPlayer",
    "inherit_arg": false,
    "summary": "Mono Sample Player",
    "hiden": true
  },
  "ChipLead": {
    "name": ":chiplead",
    "opts": {
      "decay": 0,
      "note_slide_curve": 0,
      "pan_slide_curve": 0,
      "note_slide": 0,
      "pan_slide": 0,
      "amp_slide_shape": 1,
      "note": 60,
      "sustain": 0,
      "pan": 0,
      "pan_slide_shape": 1,
      "note_slide_shape": 1,
      "sustain_level": 1,
      "note_resolution": 0.1,
      "attack_level": 1,
      "release": 1,
      "amp": 1,
      "env_curve": 2,
      "width": 0,
      "amp_slide": 0,
      "decay_level": 1,
      "amp_slide_curve": 0,
      "attack": 0
    },
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false,
    "summary": "Chip Lead",
    "hiden": false
  },
  "ModSaw": {
    "name": ":mod_saw",
    "opts": {
      "decay": 0,
      "note_slide_curve": 0,
      "pan_slide_curve": 0,
      "note_slide": 0,
      "cutoff": 100,
      "pan_slide": 0,
      "amp_slide_shape": 1,
      "note": 52,
      "mod_range_slide": 0,
      "sustain": 0,
      "mod_range_slide_shape": 1,
      "pan": 0,
      "pan_slide_shape": 1,
      "note_slide_shape": 1,
      "mod_pulse_width_slide_curve": 0,
      "mod_phase_slide_shape": 1,
      "sustain_level": 1,
      "mod_invert_wave": 0,
      "attack_level": 1,
      "mod_wave": 1,
      "release": 1,
      "amp": 1,
      "cutoff_slide": 0,
      "mod_phase_offset": 0,
      "cutoff_slide_shape": 1,
      "cutoff_slide_curve": 0,
      "mod_pulse_width": 0.5,
      "env_curve": 2,
      "mod_pulse_width_slide_shape": 1,
      "mod_range_slide_curve": 0,
      "amp_slide": 0,
      "mod_phase_slide_curve": 0,
      "mod_range": 5,
      "mod_phase": 0.25,
      "decay_level": 1,
      "mod_phase_slide": 0,
      "amp_slide_curve": 0,
      "attack": 0,
      "mod_pulse_width_slide": 0
    },
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false,
    "summary": "Modulated Saw Wave",
    "hiden": false
  },
  "Supersaw": {
    "name": ":supersaw",
    "opts": {
      "decay": 0,
      "note_slide_curve": 0,
      "pan_slide_curve": 0,
      "note_slide": 0,
      "cutoff": 130,
      "pan_slide": 0,
      "amp_slide_shape": 1,
      "note": 52,
      "sustain": 0,
      "pan": 0,
      "res": 0.7,
      "pan_slide_shape": 1,
      "note_slide_shape": 1,
      "sustain_level": 1,
      "res_slide": 0,
      "res_slide_shape": 1,
      "attack_level": 1,
      "release": 1,
      "amp": 1,
      "cutoff_slide": 0,
      "cutoff_slide_shape": 1,
      "cutoff_slide_curve": 0,
      "env_curve": 2,
      "amp_slide": 0,
      "decay_level": 1,
      "amp_slide_curve": 0,
      "attack": 0,
      "res_slide_curve": 0
    },
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false,
    "summary": "Supersaw",
    "hiden": false
  },
  "DPulse": {
    "name": ":dpulse",
    "opts": {
      "decay": 0,
      "note_slide_curve": 0,
      "pan_slide_curve": 0,
      "note_slide": 0,
      "detune_slide_curve": 0,
      "cutoff": 100,
      "pan_slide": 0,
      "amp_slide_shape": 1,
      "note": 52,
      "sustain": 0,
      "pan": 0,
      "pulse_width": 0.5,
      "pan_slide_shape": 1,
      "note_slide_shape": 1,
      "dpulse_width_slide_shape": 1,
      "pulse_width_slide_shape": 1,
      "sustain_level": 1,
      "amp_slide_curve": 0,
      "attack_level": 1,
      "release": 1,
      "amp": 1,
      "cutoff_slide": 0,
      "cutoff_slide_shape": 1,
      "cutoff_slide_curve": 0,
      "env_curve": 2,
      "detune_slide": 0,
      "dpulse_width_slide": 0,
      "detune_slide_shape": 1,
      "attack": 0,
      "decay_level": 1,
      "pulse_width_slide_curve": 0,
      "dpulse_width": 0,
      "detune": 0.1,
      "amp_slide": 0,
      "pulse_width_slide": 0
    },
    "inherit_base": "DSaw",
    "inherit_arg": true,
    "summary": "Detuned Pulse Wave",
    "hiden": true
  },
  "TechSaws": {
    "name": ":tech_saws",
    "opts": {
      "decay": 0,
      "note_slide_curve": 0,
      "pan_slide_curve": 0,
      "note_slide": 0,
      "cutoff": 130,
      "pan_slide": 0,
      "amp_slide_shape": 1,
      "note": 52,
      "sustain": 0,
      "pan": 0,
      "res": 0.7,
      "pan_slide_shape": 1,
      "note_slide_shape": 1,
      "sustain_level": 1,
      "res_slide": 0,
      "res_slide_shape": 1,
      "attack_level": 1,
      "release": 1,
      "amp": 1,
      "cutoff_slide": 0,
      "cutoff_slide_shape": 1,
      "cutoff_slide_curve": 0,
      "env_curve": 2,
      "amp_slide": 0,
      "decay_level": 1,
      "amp_slide_curve": 0,
      "attack": 0,
      "res_slide_curve": 0
    },
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false,
    "summary": "TechSaws",
    "hiden": false
  },
  "Hollow": {
    "name": ":hollow",
    "opts": {
      "decay": 0,
      "note_slide_curve": 0,
      "pan_slide_curve": 0,
      "note_slide": 0,
      "norm": 0,
      "cutoff": 90,
      "pan_slide": 0,
      "amp_slide_shape": 1,
      "note": 52,
      "sustain": 0,
      "pan": 0,
      "res": 0.99,
      "pan_slide_shape": 1,
      "note_slide_shape": 1,
      "sustain_level": 1,
      "res_slide": 0,
      "res_slide_shape": 1,
      "attack_level": 1,
      "noise": 1,
      "release": 1,
      "amp": 1,
      "cutoff_slide": 0,
      "cutoff_slide_shape": 1,
      "cutoff_slide_curve": 0,
      "env_curve": 2,
      "amp_slide": 0,
      "decay_level": 1,
      "amp_slide_curve": 0,
      "attack": 0,
      "res_slide_curve": 0
    },
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false,
    "summary": "Hollow",
    "hiden": false
  },
  "BasicMixer": {
    "name": ":basic_mixer",
    "opts": {
      "amp_slide_shape": 1,
      "amp": 1,
      "amp_slide_curve": 0,
      "amp_slide": 0.1
    },
    "inherit_base": "BaseMixer",
    "inherit_arg": false,
    "summary": "Basic Mixer",
    "hiden": true
  },
  "SoundIn": {
    "name": ":sound_in",
    "opts": {
      "decay": 0,
      "pan_slide_curve": 0,
      "amp": 1,
      "pan_slide": 0,
      "amp_slide_shape": 1,
      "sustain": 1,
      "pan": 0,
      "attack": 0,
      "input": 1,
      "env_curve": 0,
      "pan_slide_shape": 1,
      "decay_level": 1,
      "sustain_level": 1,
      "attack_level": 1,
      "release": 0,
      "amp_slide_curve": 0,
      "amp_slide": 0
    },
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false,
    "summary": "Sound In",
    "hiden": false
  },
  "DarkAmbience": {
    "name": ":dark_ambience",
    "opts": {
      "decay": 0,
      "note_slide_curve": 0,
      "detune1_slide": 0,
      "pan_slide_curve": 0,
      "note_slide": 0,
      "cutoff": 110,
      "pan_slide": 0,
      "amp_slide_shape": 1,
      "note": 52,
      "detune1_slide_curve": 0,
      "sustain": 0,
      "noise": 0,
      "pan": 0,
      "res": 0.7,
      "ring": 0.2,
      "pan_slide_shape": 1,
      "note_slide_shape": 1,
      "detune2_slide_shape": 1,
      "sustain_level": 1,
      "res_slide": 0,
      "res_slide_shape": 1,
      "attack_level": 1,
      "detune1_slide_shape": 1,
      "reverb_time": 100,
      "detune1": 12,
      "release": 1,
      "amp": 1,
      "cutoff_slide": 0,
      "cutoff_slide_shape": 1,
      "cutoff_slide_curve": 0,
      "env_curve": 2,
      "amp_slide": 0,
      "decay_level": 1,
      "detune2_slide_curve": 0,
      "detune2_slide": 0,
      "room": 70,
      "amp_slide_curve": 0,
      "attack": 0,
      "res_slide_curve": 0,
      "detune2": 24
    },
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false,
    "summary": "Dark Ambience",
    "hiden": false
  },
  "Singer": {
    "name": ":singer",
    "opts": {
      "decay": 0,
      "note_slide_curve": 0,
      "pan_slide_curve": 0,
      "note_slide": 0,
      "pan_slide": 0,
      "amp_slide_shape": 1,
      "note": 52,
      "sustain": 0,
      "amp": 1,
      "pan": 0,
      "attack": 1,
      "env_curve": 2,
      "pan_slide_shape": 1,
      "note_slide_shape": 1,
      "decay_level": 1,
      "sustain_level": 1,
      "attack_level": 1,
      "release": 4.0,
      "amp_slide_curve": 0,
      "amp_slide": 0
    },
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false,
    "summary": "Singer",
    "hiden": true
  },
  "BaseMixer": {
    "inherit_arg": true,
    "opts": {},
    "hiden": true,
    "inherit_base": "StudioInfo"
  },
  "GNoise": {
    "name": ":gnoise",
    "opts": {
      "decay": 0,
      "res": 0,
      "pan_slide_curve": 0,
      "attack_level": 1,
      "cutoff": 110,
      "pan_slide": 0,
      "amp_slide_shape": 1,
      "amp": 1,
      "pan": 0,
      "pan_slide_shape": 1,
      "sustain_level": 1,
      "sustain": 0,
      "cutoff_slide": 0,
      "release": 1,
      "res_slide_shape": 1,
      "cutoff_slide_shape": 1,
      "cutoff_slide_curve": 0,
      "env_curve": 2,
      "res_slide": 0,
      "attack": 0,
      "decay_level": 1,
      "amp_slide_curve": 0,
      "amp_slide": 0,
      "res_slide_curve": 0
    },
    "inherit_base": "Noise",
    "inherit_arg": true,
    "summary": "Grey Noise",
    "hiden": true
  },
  "FM": {
    "name": ":fm",
    "opts": {
      "decay": 0,
      "note_slide_curve": 0,
      "pan_slide_curve": 0,
      "note_slide": 0,
      "cutoff": 100,
      "pan_slide": 0,
      "amp_slide_shape": 1,
      "note": 52,
      "sustain": 0,
      "pan": 0,
      "depth_slide_curve": 0,
      "divisor_slide_shape": 1,
      "pan_slide_shape": 1,
      "note_slide_shape": 1,
      "depth": 1,
      "sustain_level": 1,
      "divisor_slide": 0,
      "depth_slide_shape": 1,
      "attack_level": 1,
      "divisor": 2,
      "divisor_slide_curve": 0,
      "release": 1,
      "amp": 1,
      "cutoff_slide": 0,
      "cutoff_slide_shape": 1,
      "cutoff_slide_curve": 0,
      "env_curve": 2,
      "amp_slide": 0,
      "depth_slide": 0,
      "decay_level": 1,
      "amp_slide_curve": 0,
      "attack": 0
    },
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false,
    "summary": "Basic FM synthesis",
    "hiden": false
  },
  "DullBell": {
    "name": ":dull_bell",
    "opts": {
      "decay": 0,
      "note_slide_curve": 0,
      "pan_slide_curve": 0,
      "note_slide": 0,
      "pan_slide": 0,
      "amp_slide_shape": 1,
      "note": 52,
      "sustain": 0,
      "amp": 1,
      "pan": 0,
      "attack": 0,
      "env_curve": 2,
      "pan_slide_shape": 1,
      "note_slide_shape": 1,
      "decay_level": 1,
      "sustain_level": 1,
      "attack_level": 1,
      "release": 1,
      "amp_slide_curve": 0,
      "amp_slide": 0
    },
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false,
    "summary": "Dull Bell",
    "hiden": false
  },
  "SonicPiSynth": {
    "inherit_arg": true,
    "opts": {},
    "hiden": true,
    "inherit_base": "SynthInfo"
  },
  "StudioInfo": {
    "inherit_arg": true,
    "opts": {},
    "hiden": true,
    "inherit_base": "SonicPiSynth"
  },
  "DSaw": {
    "name": ":dsaw",
    "opts": {
      "decay": 0,
      "note_slide_curve": 0,
      "pan_slide_curve": 0,
      "note_slide": 0,
      "detune_slide_curve": 0,
      "cutoff": 100,
      "pan_slide": 0,
      "amp_slide_shape": 1,
      "note": 52,
      "sustain": 0,
      "pan": 0,
      "pan_slide_shape": 1,
      "note_slide_shape": 1,
      "sustain_level": 1,
      "attack_level": 1,
      "release": 1,
      "amp": 1,
      "cutoff_slide": 0,
      "cutoff_slide_shape": 1,
      "cutoff_slide_curve": 0,
      "env_curve": 2,
      "detune_slide": 0,
      "amp_slide": 0,
      "detune_slide_shape": 1,
      "decay_level": 1,
      "detune": 0.1,
      "amp_slide_curve": 0,
      "attack": 0
    },
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false,
    "summary": "Detuned Saw wave",
    "hiden": false
  },
  "Beep": {
    "name": ":beep",
    "opts": {
      "decay": 0,
      "note_slide_curve": 0,
      "pan_slide_curve": 0,
      "note_slide": 0,
      "pan_slide": 0,
      "amp_slide_shape": 1,
      "note": 52,
      "sustain": 0,
      "amp": 1,
      "pan": 0,
      "attack": 0,
      "env_curve": 2,
      "pan_slide_shape": 1,
      "note_slide_shape": 1,
      "decay_level": 1,
      "sustain_level": 1,
      "attack_level": 1,
      "release": 1,
      "amp_slide_curve": 0,
      "amp_slide": 0
    },
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false,
    "summary": "Sine Wave",
    "hiden": false
  },
  "BNoise": {
    "name": ":bnoise",
    "opts": {
      "decay": 0,
      "res": 0,
      "pan_slide_curve": 0,
      "attack_level": 1,
      "cutoff": 110,
      "pan_slide": 0,
      "amp_slide_shape": 1,
      "amp": 1,
      "pan": 0,
      "pan_slide_shape": 1,
      "sustain_level": 1,
      "sustain": 0,
      "cutoff_slide": 0,
      "release": 1,
      "res_slide_shape": 1,
      "cutoff_slide_shape": 1,
      "cutoff_slide_curve": 0,
      "env_curve": 2,
      "res_slide": 0,
      "attack": 0,
      "decay_level": 1,
      "amp_slide_curve": 0,
      "amp_slide": 0,
      "res_slide_curve": 0
    },
    "inherit_base": "Noise",
    "inherit_arg": true,
    "summary": "Brown Noise",
    "hiden": true
  },
  "PNoise": {
    "name": ":pnoise",
    "opts": {
      "decay": 0,
      "res": 0,
      "pan_slide_curve": 0,
      "attack_level": 1,
      "cutoff": 110,
      "pan_slide": 0,
      "amp_slide_shape": 1,
      "amp": 1,
      "pan": 0,
      "pan_slide_shape": 1,
      "sustain_level": 1,
      "sustain": 0,
      "cutoff_slide": 0,
      "release": 1,
      "res_slide_shape": 1,
      "cutoff_slide_shape": 1,
      "cutoff_slide_curve": 0,
      "env_curve": 2,
      "res_slide": 0,
      "attack": 0,
      "decay_level": 1,
      "amp_slide_curve": 0,
      "amp_slide": 0,
      "res_slide_curve": 0
    },
    "inherit_base": "Noise",
    "inherit_arg": true,
    "summary": "Pink Noise",
    "hiden": true
  },
  "SoundInStereo": {
    "name": ":sound_in_stereo",
    "opts": {
      "decay": 0,
      "pan_slide_curve": 0,
      "attack_level": 1,
      "pan_slide": 0,
      "amp_slide_shape": 1,
      "amp": 1,
      "pan": 0,
      "pan_slide_shape": 1,
      "sustain_level": 1,
      "sustain": 1,
      "release": 0,
      "input": 1,
      "env_curve": 0,
      "amp_slide": 0,
      "decay_level": 1,
      "amp_slide_curve": 0,
      "attack": 0
    },
    "inherit_base": "SoundIn",
    "inherit_arg": true,
    "summary": "Sound In Stereo",
    "hiden": true
  },
  "Pitchless": {
    "inherit_arg": true,
    "opts": {},
    "hiden": true,
    "inherit_base": "SonicPiSynth"
  },
  "BasicStereoPlayer": {
    "name": ":basic_stereo_player",
    "opts": {
      "lpf_slide_shape": 1,
      "pan_slide_curve": 0,
      "hpf_slide_curve": 0,
      "pan_slide": 0,
      "amp_slide_shape": 1,
      "amp": 1,
      "pan": 0,
      "lpf_slide_curve": 0,
      "pan_slide_shape": 1,
      "lpf": -1,
      "hpf_slide_shape": 1,
      "hpf": -1,
      "lpf_slide": 0,
      "rate": 1,
      "hpf_slide": 0,
      "amp_slide_curve": 0,
      "amp_slide": 0
    },
    "inherit_base": "BasicMonoPlayer",
    "inherit_arg": true,
    "summary": "Basic Stereo Sample Player (no env)",
    "hiden": true
  },
  "SynthViolin": {
    "name": ":synth_violin",
    "opts": {
      "decay": 0,
      "note_slide_curve": 0,
      "pan_slide_curve": 0,
      "note_slide": 0,
      "vibrato_depth_slide_curve": 0,
      "cutoff": 100,
      "pan_slide": 0,
      "amp_slide_shape": 1,
      "note": 52,
      "sustain": 0,
      "pan": 0,
      "pan_slide_shape": 1,
      "note_slide_shape": 1,
      "vibrato_rate_slide_shape": 1,
      "vibrato_onset": 0.1,
      "sustain_level": 1,
      "vibrato_rate": 6,
      "attack_level": 1,
      "vibrato_depth": 0.15,
      "release": 1,
      "amp": 1,
      "cutoff_slide": 0,
      "cutoff_slide_shape": 1,
      "cutoff_slide_curve": 0,
      "env_curve": 2,
      "amp_slide": 0,
      "vibrato_rate_slide_curve": 0,
      "vibrato_delay": 0.5,
      "decay_level": 1,
      "vibrato_depth_slide_shape": 1,
      "amp_slide_curve": 0,
      "attack": 0
    },
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false,
    "summary": "Blade Runner style strings",
    "hiden": false
  },
  "Hoover": {
    "name": ":hoover",
    "opts": {
      "decay": 0,
      "note_slide_curve": 0,
      "pan_slide_curve": 0,
      "note_slide": 0,
      "cutoff": 130,
      "pan_slide": 0,
      "amp_slide_shape": 1,
      "note": 52,
      "sustain": 0,
      "pan": 0,
      "res": 0.1,
      "pan_slide_shape": 1,
      "note_slide_shape": 1,
      "sustain_level": 1,
      "res_slide": 0,
      "res_slide_shape": 1,
      "attack_level": 1,
      "release": 1,
      "amp": 1,
      "cutoff_slide": 0,
      "cutoff_slide_shape": 1,
      "cutoff_slide_curve": 0,
      "env_curve": 2,
      "amp_slide": 0,
      "decay_level": 1,
      "amp_slide_curve": 0,
      "attack": 0.05,
      "res_slide_curve": 0
    },
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false,
    "summary": "Hoover",
    "hiden": false
  },
  "ModSine": {
    "name": ":mod_sine",
    "opts": {
      "decay": 0,
      "note_slide_curve": 0,
      "pan_slide_curve": 0,
      "note_slide": 0,
      "cutoff": 100,
      "pan_slide": 0,
      "amp_slide_shape": 1,
      "note": 52,
      "mod_range_slide": 0,
      "sustain": 0,
      "mod_range_slide_shape": 1,
      "pan": 0,
      "pan_slide_shape": 1,
      "note_slide_shape": 1,
      "mod_pulse_width_slide_curve": 0,
      "mod_phase_slide_shape": 1,
      "sustain_level": 1,
      "mod_invert_wave": 0,
      "attack_level": 1,
      "mod_wave": 1,
      "release": 1,
      "amp": 1,
      "cutoff_slide": 0,
      "mod_phase_offset": 0,
      "cutoff_slide_shape": 1,
      "cutoff_slide_curve": 0,
      "mod_pulse_width": 0.5,
      "env_curve": 2,
      "mod_pulse_width_slide_shape": 1,
      "mod_range_slide_curve": 0,
      "amp_slide": 0,
      "mod_phase_slide_curve": 0,
      "mod_range": 5,
      "mod_phase": 0.25,
      "decay_level": 1,
      "mod_phase_slide": 0,
      "amp_slide_curve": 0,
      "attack": 0,
      "mod_pulse_width_slide": 0
    },
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false,
    "summary": "Modulated Sine Wave",
    "hiden": false
  },
  "Square": {
    "name": ":square",
    "opts": {
      "decay": 0,
      "note_slide_curve": 0,
      "pan_slide_curve": 0,
      "note_slide": 0,
      "cutoff": 100,
      "pan_slide": 0,
      "amp_slide_shape": 1,
      "note": 52,
      "sustain": 0,
      "pan": 0,
      "pan_slide_shape": 1,
      "note_slide_shape": 1,
      "sustain_level": 1,
      "attack_level": 1,
      "release": 1,
      "amp": 1,
      "cutoff_slide": 0,
      "cutoff_slide_shape": 1,
      "cutoff_slide_curve": 0,
      "env_curve": 2,
      "amp_slide": 0,
      "decay_level": 1,
      "amp_slide_curve": 0,
      "attack": 0
    },
    "inherit_base": "SonicPiSynth",
    "inherit_arg": false,
    "summary": "Square Wave",
    "hiden": false
  },
  "CNoise": {
    "name": ":cnoise",
    "opts": {
      "decay": 0,
      "res": 0,
      "pan_slide_curve": 0,
      "attack_level": 1,
      "cutoff": 110,
      "pan_slide": 0,
      "amp_slide_shape": 1,
      "amp": 1,
      "pan": 0,
      "pan_slide_shape": 1,
      "sustain_level": 1,
      "sustain": 0,
      "cutoff_slide": 0,
      "release": 1,
      "res_slide_shape": 1,
      "cutoff_slide_shape": 1,
      "cutoff_slide_curve": 0,
      "env_curve": 2,
      "res_slide": 0,
      "attack": 0,
      "decay_level": 1,
      "amp_slide_curve": 0,
      "amp_slide": 0,
      "res_slide_curve": 0
    },
    "inherit_base": "Noise",
    "inherit_arg": true,
    "summary": "Clip Noise",
    "hiden": true
  }
}

synth_nodes = {
  ":fx_replace_nhpf": "FXNormHPF",
  ":subpulse": "SubPulse",
  ":mod_beep": "ModSine",
  ":growl": "Growl",
  ":fx_whammy": "FXWhammy",
  ":fx_band_eq": "FXBandEQ",
  ":fx_level": "FXLevel",
  ":fm": "FM",
  ":chipnoise": "ChipNoise",
  ":pretty_bell": "PrettyBell",
  ":dsaw": "DSaw",
  ":sine": "Beep",
  ":prophet": "Prophet",
  ":fx_replace_rlpf": "FXRLPF",
  ":fx_gverb": "FXGVerb",
  ":fx_replace_distortion": "FXDistortion",
  ":dull_bell": "DullBell",
  ":chipbass": "ChipBass",
  ":fx_nrhpf": "FXNormRHPF",
  ":cnoise": "CNoise",
  ":fx_pan": "FXPan",
  ":fx_hpf": "FXHPF",
  ":blade": "SynthViolin",
  ":beep": "Beep",
  ":fx_replace_echo": "FXEcho",
  ":fx_ixi_techno": "FXIXITechno",
  ":piano": "SynthPiano",
  ":tri": "Tri",
  ":fx_normaliser": "FXNormaliser",
  ":fx_replace_nrhpf": "FXNormRHPF",
  ":fx_panslicer": "FXPanSlicer",
  ":fx_replace_reverb": "FXReverb",
  ":fx_distortion": "FXDistortion",
  ":fx_compressor": "FXCompressor",
  ":fx_replace_lpf": "FXLPF",
  ":dtri": "DTri",
  ":fx_lpf": "FXLPF",
  ":basic_stereo_player": "BasicStereoPlayer",
  ":fx_flanger": "FXFlanger",
  ":fx_rbpf": "FXRBPF",
  ":fx_nhpf": "FXNormHPF",
  ":basic_mono_player": "BasicMonoPlayer",
  ":fx_rhpf": "FXRHPF",
  ":fx_nlpf": "FXNormLPF",
  ":fx_bitcrusher": "FXBitcrusher",
  ":fx_replace_compressor": "FXCompressor",
  ":hollow": "Hollow",
  ":fx_replace_nrlpf": "FXNormRLPF",
  ":basic_mixer": "BasicMixer",
  ":chiplead": "ChipLead",
  ":fx_vowel": "FXVowel",
  ":tb303": "TB303",
  ":fx_replace_level": "FXLevel",
  ":fx_replace_rhpf": "FXRHPF",
  ":stereo_player": "StereoPlayer",
  ":fx_wobble": "FXWobble",
  ":mono_player": "MonoPlayer",
  ":fx_replace_ixi_techno": "FXIXITechno",
  ":mod_fm": "ModFM",
  ":square": "Square",
  ":fx_replace_slicer": "FXSlicer",
  ":supersaw": "Supersaw",
  ":gnoise": "GNoise",
  ":mod_pulse": "ModPulse",
  ":fx_rlpf": "FXRLPF",
  ":pnoise": "PNoise",
  ":fx_replace_wobble": "FXWobble",
  ":fx_octaver": "FXOctaver",
  ":fx_replace_hpf": "FXHPF",
  ":dark_ambience": "DarkAmbience",
  ":pulse": "Pulse",
  ":mod_tri": "ModTri",
  ":bnoise": "BNoise",
  ":hoover": "Hoover",
  ":fx_bpf": "FXBPF",
  ":mod_sine": "ModSine",
  ":fx_krush": "FXKrush",
  ":fx_replace_pan": "FXPan",
  ":fx_nrlpf": "FXNormRLPF",
  ":main_mixer": "MainMixer",
  ":dpulse": "DPulse",
  ":saw": "Saw",
  ":fx_replace_normaliser": "FXNormaliser",
  ":noise": "Noise",
  ":pluck": "SynthPluck",
  ":fx_tanh": "FXTanh",
  ":sound_in": "SoundIn",
  ":mod_saw": "ModSaw",
  ":fx_slicer": "FXSlicer",
  ":fx_mono": "FXMono",
  ":tech_saws": "TechSaws",
  ":zawa": "Zawa",
  ":fx_echo": "FXEcho",
  ":fx_nbpf": "FXNBPF",
  ":fx_replace_nlpf": "FXNormLPF",
  ":sound_in_stereo": "SoundInStereo",
  ":fx_pitch_shift": "FXPitchShift",
  ":fx_reverb": "FXReverb",
  ":fx_ring_mod": "FXRingMod",
  ":mod_dsaw": "ModDSaw",
  ":fx_nrbpf": "FXNRBPF"
}

fx = {
  "FXIXITechno": {
    "name": ":fx_ixi_techno",
    "opts": {
      "res": 0.8,
      "pre_amp": 1,
      "pre_amp_slide_curve": 0,
      "res_slide_shape": 1,
      "cutoff_max_slide_curve": 0,
      "mix_slide_shape": 1,
      "mix_slide_curve": 0,
      "amp": 1,
      "pre_mix": 1,
      "pre_amp_slide": 0,
      "pre_mix_slide_shape": 1,
      "mix": 1,
      "cutoff_min_slide_shape": 1,
      "cutoff_max": 120,
      "res_slide": 0,
      "phase_offset": 0,
      "cutoff_max_slide_shape": 1,
      "cutoff_max_slide": 0,
      "cutoff_min_slide_curve": 0,
      "mix_slide": 0,
      "pre_amp_slide_shape": 1,
      "phase_slide_curve": 0,
      "phase_slide": 0,
      "amp_slide_shape": 1,
      "pre_mix_slide": 0,
      "res_slide_curve": 0,
      "cutoff_min_slide": 0,
      "phase_slide_shape": 1,
      "cutoff_min": 60,
      "amp_slide_curve": 0,
      "amp_slide": 0,
      "pre_mix_slide_curve": 0,
      "phase": 4
    },
    "inherit_base": "FXInfo",
    "inherit_arg": true,
    "summary": "Techno from IXI Lang",
    "hiden": false
  },
  "FXNBPF": {
    "name": ":fx_nbpf",
    "opts": {
      "res": 0.6,
      "pre_amp": 1,
      "pre_amp_slide_curve": 0,
      "res_slide_shape": 1,
      "mix_slide_shape": 1,
      "mix_slide_curve": 0,
      "amp": 1,
      "pre_mix": 1,
      "pre_amp_slide": 0,
      "centre_slide_curve": 0,
      "pre_mix_slide_shape": 1,
      "mix": 1,
      "centre_slide": 0,
      "mix_slide": 0,
      "pre_amp_slide_shape": 1,
      "centre_slide_shape": 1,
      "res_slide": 0,
      "amp_slide_shape": 1,
      "centre": 100,
      "pre_mix_slide": 0,
      "pre_mix_slide_curve": 0,
      "amp_slide_curve": 0,
      "amp_slide": 0,
      "res_slide_curve": 0
    },
    "inherit_base": "FXBPF",
    "inherit_arg": true,
    "summary": "Normalised Band Pass Filter",
    "hiden": true
  },
  "FXNormaliser": {
    "name": ":fx_normaliser",
    "opts": {
      "pre_amp": 1,
      "pre_amp_slide_curve": 0,
      "mix_slide_shape": 1,
      "mix_slide_curve": 0,
      "amp": 1,
      "pre_mix": 1,
      "pre_amp_slide": 0,
      "pre_mix_slide_shape": 1,
      "mix": 1,
      "mix_slide": 0,
      "level_slide_curve": 0,
      "pre_amp_slide_shape": 1,
      "amp_slide_shape": 1,
      "pre_mix_slide": 0,
      "level_slide": 0,
      "level_slide_shape": 1,
      "level": 1,
      "amp_slide_curve": 0,
      "amp_slide": 0,
      "pre_mix_slide_curve": 0
    },
    "inherit_base": "FXInfo",
    "inherit_arg": true,
    "summary": "Normaliser",
    "hiden": false
  },
  "FXPanSlicer": {
    "name": ":fx_panslicer",
    "opts": {
      "smooth_down_slide_shape": 1,
      "smooth_up": 0,
      "pan_max": 1,
      "mix_slide_shape": 1,
      "mix_slide_curve": 0,
      "amp": 1,
      "pre_amp_slide": 0,
      "pan_min_slide": 0,
      "pulse_width": 0.5,
      "phase": 0.25,
      "prob_pos_slide_shape": 1,
      "pulse_width_slide_shape": 1,
      "seed": 0,
      "prob_pos": 0,
      "pan_min_slide_curve": 0,
      "smooth_up_slide": 0,
      "pre_amp_slide_shape": 1,
      "amp_min_slide_curve": 0,
      "probability_slide_shape": 1,
      "phase_slide": 0,
      "pan_min": -1,
      "pan_max_slide_curve": 0,
      "pre_mix_slide": 0,
      "phase_offset": 0,
      "amp_min_slide_shape": 1,
      "smooth_down": 0,
      "smooth": 0,
      "pre_mix_slide_curve": 0,
      "pulse_width_slide": 0,
      "smooth_up_slide_shape": 1,
      "pre_amp": 1,
      "pre_amp_slide_curve": 0,
      "pan_max_slide": 0,
      "amp_slide_shape": 1,
      "pulse_width_slide_curve": 0,
      "phase_slide_shape": 1,
      "pre_mix": 1,
      "amp_max_slide_shape": 1,
      "pre_mix_slide_shape": 1,
      "amp_min_slide": 0,
      "probability_slide": 0,
      "probability_slide_curve": 0,
      "probability": 0,
      "pan_max_slide_shape": 1,
      "amp_max": 1,
      "smooth_down_slide": 0,
      "mix_slide": 0,
      "smooth_slide_shape": 1,
      "smooth_up_slide_curve": 0,
      "smooth_slide": 0,
      "amp_min": 0,
      "wave": 1,
      "phase_slide_curve": 0,
      "invert_wave": 0,
      "prob_pos_slide": 0,
      "amp_max_slide": 0,
      "smooth_slide_curve": 0,
      "pan_min_slide_shape": 1,
      "smooth_down_slide_curve": 0,
      "amp_max_slide_curve": 0,
      "amp_slide_curve": 0,
      "amp_slide": 0,
      "prob_pos_slide_curve": 0,
      "mix": 1
    },
    "inherit_base": "FXSlicer",
    "inherit_arg": true,
    "summary": "Pan Slicer",
    "hiden": true
  },
  "FXNormRHPF": {
    "name": ":fx_nrhpf",
    "opts": {
      "res": 0.5,
      "pre_amp": 1,
      "pre_amp_slide_curve": 0,
      "cutoff": 100,
      "mix_slide_shape": 1,
      "mix_slide_curve": 0,
      "amp": 1,
      "pre_mix": 1,
      "pre_amp_slide": 0,
      "pre_mix_slide_shape": 1,
      "mix": 1,
      "cutoff_slide": 0,
      "res_slide_shape": 1,
      "mix_slide": 0,
      "cutoff_slide_shape": 1,
      "pre_amp_slide_shape": 1,
      "res_slide": 0,
      "amp_slide_shape": 1,
      "pre_mix_slide": 0,
      "pre_mix_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "amp_slide_curve": 0,
      "amp_slide": 0,
      "res_slide_curve": 0
    },
    "inherit_base": "FXRHPF",
    "inherit_arg": true,
    "summary": "Normalised Resonant High Pass Filter",
    "hiden": true
  },
  "FXFlanger": {
    "name": ":fx_flanger",
    "opts": {
      "decay": 2,
      "pre_amp": 1,
      "pre_amp_slide_curve": 0,
      "feedback_slide_shape": 1,
      "stereo_invert_wave": 0,
      "wave": 4,
      "mix_slide_shape": 1,
      "phase_slide_curve": 0,
      "mix_slide_curve": 0,
      "amp": 1,
      "pre_mix": 1,
      "pre_amp_slide": 0,
      "depth_slide_curve": 0,
      "pre_mix_slide_shape": 1,
      "decay_slide_curve": 0,
      "mix": 1,
      "feedback": 0,
      "depth": 5,
      "phase_offset": 0,
      "depth_slide": 0,
      "decay_slide": 0,
      "depth_slide_shape": 1,
      "invert_flange": 0,
      "mix_slide": 0,
      "max_delay": 20,
      "pre_amp_slide_shape": 1,
      "delay_slide_shape": 1,
      "decay_slide_shape": 1,
      "feedback_slide_curve": 0,
      "invert_wave": 0,
      "delay_slide_curve": 0,
      "phase_slide": 0,
      "amp_slide_shape": 1,
      "delay": 5,
      "pre_mix_slide": 0,
      "delay_slide": 0,
      "phase_slide_shape": 1,
      "feedback_slide": 0,
      "amp_slide_curve": 0,
      "amp_slide": 0,
      "pre_mix_slide_curve": 0,
      "phase": 4
    },
    "inherit_base": "FXInfo",
    "inherit_arg": true,
    "summary": "Flanger",
    "hiden": false
  },
  "FXHPF": {
    "name": ":fx_hpf",
    "opts": {
      "pre_amp": 1,
      "pre_amp_slide_curve": 0,
      "cutoff": 100,
      "mix_slide_shape": 1,
      "mix_slide_curve": 0,
      "amp": 1,
      "pre_mix": 1,
      "pre_amp_slide": 0,
      "pre_mix_slide_shape": 1,
      "mix": 1,
      "cutoff_slide": 0,
      "mix_slide": 0,
      "cutoff_slide_shape": 1,
      "pre_amp_slide_shape": 1,
      "amp_slide_shape": 1,
      "pre_mix_slide": 0,
      "cutoff_slide_curve": 0,
      "amp_slide_curve": 0,
      "amp_slide": 0,
      "pre_mix_slide_curve": 0
    },
    "inherit_base": "FXInfo",
    "inherit_arg": true,
    "summary": "High Pass Filter",
    "hiden": false
  },
  "FXBandEQ": {
    "name": ":fx_band_eq",
    "opts": {
      "freq_slide_shape": 1,
      "res": 0.6,
      "pre_amp": 1,
      "pre_amp_slide_curve": 0,
      "res_slide_shape": 1,
      "mix_slide_shape": 1,
      "db": 0.6,
      "mix_slide_curve": 0,
      "amp": 1,
      "pre_mix": 1,
      "pre_amp_slide": 0,
      "pre_mix_slide_shape": 1,
      "mix": 1,
      "freq": 100,
      "freq_slide": 0,
      "mix_slide": 0,
      "freq_slide_curve": 0,
      "pre_amp_slide_shape": 1,
      "db_slide": 0,
      "res_slide": 0,
      "amp_slide_shape": 1,
      "pre_mix_slide": 0,
      "res_slide_curve": 0,
      "db_slide_curve": 0,
      "amp_slide_curve": 0,
      "amp_slide": 0,
      "pre_mix_slide_curve": 0,
      "db_slide_shape": 1
    },
    "inherit_base": "FXInfo",
    "inherit_arg": true,
    "summary": "Band EQ Filter",
    "hiden": false
  },
  "FXDistortion": {
    "name": ":fx_distortion",
    "opts": {
      "pre_amp": 1,
      "pre_amp_slide_curve": 0,
      "mix_slide_shape": 1,
      "mix_slide_curve": 0,
      "amp": 1,
      "pre_mix": 1,
      "pre_amp_slide": 0,
      "pre_mix_slide_shape": 1,
      "mix": 1,
      "distort_slide": 0,
      "mix_slide": 0,
      "pre_amp_slide_shape": 1,
      "distort_slide_curve": 0,
      "distort": 0.5,
      "amp_slide_shape": 1,
      "pre_mix_slide": 0,
      "amp_slide_curve": 0,
      "amp_slide": 0,
      "pre_mix_slide_curve": 0,
      "distort_slide_shape": 1
    },
    "inherit_base": "FXInfo",
    "inherit_arg": true,
    "summary": "Distortion",
    "hiden": false
  },
  "FXSlicer": {
    "name": ":fx_slicer",
    "opts": {
      "smooth_down_slide_shape": 1,
      "smooth_up": 0,
      "mix_slide_shape": 1,
      "mix_slide_curve": 0,
      "amp": 1,
      "pre_amp_slide": 0,
      "pulse_width": 0.5,
      "phase": 0.25,
      "prob_pos_slide_shape": 1,
      "pulse_width_slide_shape": 1,
      "amp_min_slide": 0,
      "prob_pos": 0,
      "smooth_up_slide": 0,
      "pre_amp_slide_shape": 1,
      "amp_min_slide_curve": 0,
      "probability_slide_shape": 1,
      "phase_slide": 0,
      "amp_max_slide": 0,
      "seed": 0,
      "amp_min_slide_shape": 1,
      "amp_min": 0,
      "smooth_down": 0,
      "smooth": 0,
      "pre_mix_slide_curve": 0,
      "pulse_width_slide": 0,
      "smooth_up_slide_shape": 1,
      "pre_amp": 1,
      "pre_amp_slide_curve": 0,
      "amp_slide_shape": 1,
      "pulse_width_slide_curve": 0,
      "phase_slide_shape": 1,
      "pre_mix": 1,
      "amp_max_slide_shape": 1,
      "pre_mix_slide_shape": 1,
      "mix": 1,
      "probability_slide": 0,
      "amp_max_slide_curve": 0,
      "probability": 0,
      "amp_max": 1,
      "mix_slide": 0,
      "smooth_down_slide": 0,
      "smooth_slide_shape": 1,
      "smooth_up_slide_curve": 0,
      "smooth_slide": 0,
      "phase_offset": 0,
      "wave": 1,
      "phase_slide_curve": 0,
      "invert_wave": 0,
      "amp_slide": 0,
      "pre_mix_slide": 0,
      "smooth_slide_curve": 0,
      "smooth_down_slide_curve": 0,
      "probability_slide_curve": 0,
      "amp_slide_curve": 0,
      "prob_pos_slide": 0,
      "prob_pos_slide_curve": 0
    },
    "inherit_base": "FXInfo",
    "inherit_arg": true,
    "summary": "Slicer",
    "hiden": false
  },
  "FXRingMod": {
    "name": ":fx_ring_mod",
    "opts": {
      "freq_slide_shape": 1,
      "pre_amp": 1,
      "pre_amp_slide_curve": 0,
      "mix_slide_shape": 1,
      "mix_slide_curve": 0,
      "amp": 1,
      "pre_mix": 1,
      "pre_amp_slide": 0,
      "pre_mix_slide_shape": 1,
      "mod_amp_slide_shape": 1,
      "mix": 1,
      "mod_amp_slide_curve": 0,
      "freq_slide": 0,
      "mix_slide": 0,
      "freq_slide_curve": 0,
      "pre_amp_slide_shape": 1,
      "amp_slide_shape": 1,
      "pre_mix_slide": 0,
      "freq": 30,
      "mod_amp": 1,
      "mod_amp_slide": 0,
      "amp_slide_curve": 0,
      "amp_slide": 0,
      "pre_mix_slide_curve": 0
    },
    "inherit_base": "FXInfo",
    "inherit_arg": true,
    "summary": "Ring Modulator",
    "hiden": false
  },
  "FXBitcrusher": {
    "name": ":fx_bitcrusher",
    "opts": {
      "bits_slide_curve": 0,
      "pre_amp": 1,
      "pre_amp_slide_curve": 0,
      "cutoff": 0,
      "mix_slide_shape": 1,
      "mix_slide_curve": 0,
      "amp": 1,
      "pre_mix": 1,
      "pre_amp_slide": 0,
      "pre_mix_slide_shape": 1,
      "mix": 1,
      "bits_slide_shape": 1,
      "sample_rate": 10000,
      "cutoff_slide": 0,
      "mix_slide": 0,
      "bits": 8,
      "pre_amp_slide_shape": 1,
      "cutoff_slide_shape": 1,
      "sample_rate_slide_curve": 0,
      "bits_slide": 0,
      "sample_rate_slide": 0,
      "amp_slide_shape": 1,
      "pre_mix_slide": 0,
      "cutoff_slide_curve": 0,
      "sample_rate_slide_shape": 1,
      "amp_slide_curve": 0,
      "amp_slide": 0,
      "pre_mix_slide_curve": 0
    },
    "inherit_base": "FXInfo",
    "inherit_arg": true,
    "summary": "Bitcrusher",
    "hiden": false
  },
  "FXNormLPF": {
    "name": ":fx_nlpf",
    "opts": {
      "pre_amp": 1,
      "pre_amp_slide_curve": 0,
      "cutoff": 100,
      "mix_slide_shape": 1,
      "mix_slide_curve": 0,
      "amp": 1,
      "pre_mix": 1,
      "pre_amp_slide": 0,
      "pre_mix_slide_shape": 1,
      "mix": 1,
      "cutoff_slide": 0,
      "mix_slide": 0,
      "cutoff_slide_shape": 1,
      "pre_amp_slide_shape": 1,
      "amp_slide_shape": 1,
      "pre_mix_slide": 0,
      "cutoff_slide_curve": 0,
      "amp_slide_curve": 0,
      "amp_slide": 0,
      "pre_mix_slide_curve": 0
    },
    "inherit_base": "FXLPF",
    "inherit_arg": true,
    "summary": "Normalised Low Pass Filter.",
    "hiden": true
  },
  "FXPitchShift": {
    "name": ":fx_pitch_shift",
    "opts": {
      "pre_amp": 1,
      "pre_amp_slide_curve": 0,
      "time_dis_slide": 0,
      "mix_slide_shape": 1,
      "time_dis": 0.0,
      "mix_slide_curve": 0,
      "amp": 1,
      "pre_mix": 1,
      "pre_amp_slide": 0,
      "pre_mix_slide_shape": 1,
      "pitch_slide_shape": 1,
      "pitch_slide_curve": 0,
      "mix": 1,
      "pitch_dis_slide_shape": 1,
      "pitch_dis": 0.0,
      "pitch": 0,
      "pitch_slide": 0,
      "time_dis_slide_curve": 0,
      "window_size_slide": 0,
      "mix_slide": 0,
      "pitch_dis_slide": 0,
      "pre_amp_slide_shape": 1,
      "window_size_slide_curve": 0,
      "time_dis_slide_shape": 1,
      "pitch_dis_slide_curve": 0,
      "amp_slide_shape": 1,
      "pre_mix_slide": 0,
      "window_size": 0.2,
      "window_size_slide_shape": 1,
      "amp_slide_curve": 0,
      "amp_slide": 0,
      "pre_mix_slide_curve": 0
    },
    "inherit_base": "FXInfo",
    "inherit_arg": true,
    "summary": "Pitch shift",
    "hiden": false
  },
  "FXRHPF": {
    "name": ":fx_rhpf",
    "opts": {
      "res": 0.5,
      "pre_amp": 1,
      "pre_amp_slide_curve": 0,
      "cutoff": 100,
      "mix_slide_shape": 1,
      "mix_slide_curve": 0,
      "amp": 1,
      "pre_mix": 1,
      "pre_amp_slide": 0,
      "pre_mix_slide_shape": 1,
      "mix": 1,
      "res_slide_shape": 1,
      "cutoff_slide": 0,
      "mix_slide": 0,
      "cutoff_slide_shape": 1,
      "pre_amp_slide_shape": 1,
      "res_slide": 0,
      "amp_slide_shape": 1,
      "pre_mix_slide": 0,
      "res_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "amp_slide_curve": 0,
      "amp_slide": 0,
      "pre_mix_slide_curve": 0
    },
    "inherit_base": "FXHPF",
    "inherit_arg": true,
    "summary": "Resonant High Pass Filter",
    "hiden": true
  },
  "FXCompressor": {
    "name": ":fx_compressor",
    "opts": {
      "pre_amp": 1,
      "pre_amp_slide_curve": 0,
      "threshold": 0.2,
      "threshold_slide_curve": 0,
      "mix_slide_shape": 1,
      "mix_slide_curve": 0,
      "amp": 1,
      "pre_mix": 1,
      "slope_above_slide_curve": 0,
      "pre_amp_slide": 0,
      "relax_time": 0.01,
      "pre_mix_slide_shape": 1,
      "relax_time_slide": 0,
      "mix": 1,
      "relax_time_slide_curve": 0,
      "threshold_slide": 0,
      "clamp_time_slide": 0,
      "relax_time_slide_shape": 1,
      "threshold_slide_shape": 1,
      "slope_below_slide": 0,
      "mix_slide": 0,
      "clamp_time_slide_curve": 0,
      "slope_above_slide": 0,
      "pre_amp_slide_shape": 1,
      "clamp_time": 0.01,
      "slope_below": 1,
      "slope_below_slide_curve": 0,
      "clamp_time_slide_shape": 1,
      "amp_slide_shape": 1,
      "slope_above_slide_shape": 1,
      "pre_mix_slide": 0,
      "slope_below_slide_shape": 1,
      "slope_above": 0.5,
      "amp_slide_curve": 0,
      "amp_slide": 0,
      "pre_mix_slide_curve": 0
    },
    "inherit_base": "FXInfo",
    "inherit_arg": true,
    "summary": "Compressor",
    "hiden": false
  },
  "FXNormRLPF": {
    "name": ":fx_nrlpf",
    "opts": {
      "res": 0.5,
      "pre_amp": 1,
      "pre_amp_slide_curve": 0,
      "cutoff": 100,
      "mix_slide_shape": 1,
      "mix_slide_curve": 0,
      "amp": 1,
      "pre_mix": 1,
      "pre_amp_slide": 0,
      "pre_mix_slide_shape": 1,
      "mix": 1,
      "cutoff_slide": 0,
      "res_slide_shape": 1,
      "mix_slide": 0,
      "cutoff_slide_shape": 1,
      "pre_amp_slide_shape": 1,
      "res_slide": 0,
      "amp_slide_shape": 1,
      "pre_mix_slide": 0,
      "pre_mix_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "amp_slide_curve": 0,
      "amp_slide": 0,
      "res_slide_curve": 0
    },
    "inherit_base": "FXRLPF",
    "inherit_arg": true,
    "summary": "Normalised Resonant Low Pass Filter",
    "hiden": true
  },
  "FXPan": {
    "name": ":fx_pan",
    "opts": {
      "pre_amp": 1,
      "pre_amp_slide_curve": 0,
      "pan_slide": 0,
      "mix_slide_shape": 1,
      "mix_slide_curve": 0,
      "amp": 1,
      "pre_mix": 1,
      "pre_amp_slide": 0,
      "pre_mix_slide_shape": 1,
      "pan_slide_shape": 1,
      "mix": 1,
      "mix_slide": 0,
      "pre_amp_slide_shape": 1,
      "amp_slide_shape": 1,
      "pan": 0,
      "pre_mix_slide": 0,
      "pan_slide_curve": 0,
      "amp_slide_curve": 0,
      "amp_slide": 0,
      "pre_mix_slide_curve": 0
    },
    "inherit_base": "FXInfo",
    "inherit_arg": true,
    "summary": "Pan",
    "hiden": false
  },
  "FXKrush": {
    "name": ":fx_krush",
    "opts": {
      "res": 0,
      "pre_amp": 1,
      "pre_amp_slide_curve": 0,
      "cutoff": 100,
      "mix_slide_shape": 1,
      "gain_slide_shape": 1,
      "mix_slide_curve": 0,
      "amp": 1,
      "pre_mix": 1,
      "pre_amp_slide": 0,
      "pre_mix_slide_shape": 1,
      "mix": 1,
      "res_slide_shape": 1,
      "cutoff_slide": 0,
      "gain_slide": 0,
      "mix_slide": 0,
      "cutoff_slide_shape": 1,
      "pre_amp_slide_shape": 1,
      "gain": 5,
      "res_slide": 0,
      "amp_slide_shape": 1,
      "pre_mix_slide": 0,
      "res_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "gain_slide__curve": 0,
      "amp_slide_curve": 0,
      "amp_slide": 0,
      "pre_mix_slide_curve": 0
    },
    "inherit_base": "FXInfo",
    "inherit_arg": true,
    "summary": "krush",
    "hiden": false
  },
  "FXTanh": {
    "name": ":fx_tanh",
    "opts": {
      "pre_amp": 1,
      "pre_amp_slide_curve": 0,
      "mix_slide_shape": 1,
      "mix_slide_curve": 0,
      "amp": 1,
      "pre_mix": 1,
      "pre_amp_slide": 0,
      "pre_mix_slide_shape": 1,
      "mix": 1,
      "krunch_slide_shape": 1,
      "krunch_slide_curve": 0,
      "mix_slide": 0,
      "krunch": 5,
      "krunch_slide": 0,
      "pre_amp_slide_shape": 1,
      "amp_slide_shape": 1,
      "pre_mix_slide": 0,
      "amp_slide_curve": 0,
      "amp_slide": 0,
      "pre_mix_slide_curve": 0
    },
    "inherit_base": "FXInfo",
    "inherit_arg": true,
    "summary": "Hyperbolic Tangent",
    "hiden": false
  },
  "FXRLPF": {
    "name": ":fx_rlpf",
    "opts": {
      "res": 0.5,
      "pre_amp": 1,
      "pre_amp_slide_curve": 0,
      "cutoff": 100,
      "mix_slide_shape": 1,
      "mix_slide_curve": 0,
      "amp": 1,
      "pre_mix": 1,
      "pre_amp_slide": 0,
      "pre_mix_slide_shape": 1,
      "mix": 1,
      "res_slide_shape": 1,
      "cutoff_slide": 0,
      "mix_slide": 0,
      "cutoff_slide_shape": 1,
      "pre_amp_slide_shape": 1,
      "res_slide": 0,
      "amp_slide_shape": 1,
      "pre_mix_slide": 0,
      "res_slide_curve": 0,
      "cutoff_slide_curve": 0,
      "amp_slide_curve": 0,
      "amp_slide": 0,
      "pre_mix_slide_curve": 0
    },
    "inherit_base": "FXLPF",
    "inherit_arg": true,
    "summary": "Resonant Low Pass Filter",
    "hiden": true
  },
  "FXVowel": {
    "name": ":fx_vowel",
    "opts": {
      "vowel_sound": 1,
      "pre_amp": 1,
      "pre_amp_slide_curve": 0,
      "mix_slide_shape": 1,
      "mix_slide_curve": 0,
      "amp": 1,
      "pre_mix": 1,
      "pre_amp_slide": 0,
      "voice": 0,
      "pre_mix_slide_shape": 1,
      "mix": 1,
      "mix_slide": 0,
      "pre_amp_slide_shape": 1,
      "amp_slide_shape": 1,
      "pre_mix_slide": 0,
      "amp_slide_curve": 0,
      "amp_slide": 0,
      "pre_mix_slide_curve": 0
    },
    "inherit_base": "FXInfo",
    "inherit_arg": true,
    "summary": "Vowel",
    "hiden": false
  },
  "FXChorus": {
    "name": ":fx_chorus",
    "opts": {
      "decay": 1e-05,
      "pre_amp": 1,
      "pre_amp_slide_curve": 0,
      "mix_slide_shape": 1,
      "mix_slide_curve": 0,
      "amp": 1,
      "pre_mix": 1,
      "pre_amp_slide": 0,
      "pre_mix_slide_shape": 1,
      "decay_slide_curve": 0,
      "mix": 1,
      "phase_slide": 0,
      "decay_slide": 0,
      "mix_slide": 0,
      "pre_amp_slide_shape": 1,
      "decay_slide_shape": 1,
      "phase_slide_curve": 0,
      "phase_slide_shape": 1,
      "amp_slide_shape": 1,
      "pre_mix_slide": 0,
      "max_phase": 1,
      "amp_slide_curve": 0,
      "amp_slide": 0,
      "pre_mix_slide_curve": 0,
      "phase": 0.25
    },
    "inherit_base": "FXInfo",
    "inherit_arg": true,
    "summary": "Chorus",
    "hiden": true
  },
  "FXMono": {
    "name": ":fx_mono",
    "opts": {
      "pre_amp": 1,
      "pre_amp_slide_curve": 0,
      "pan_slide": 0,
      "mix_slide_shape": 1,
      "mix_slide_curve": 0,
      "amp": 1,
      "pre_mix": 1,
      "pre_amp_slide": 0,
      "pre_mix_slide_shape": 1,
      "pan_slide_shape": 1,
      "mix": 1,
      "mix_slide": 0,
      "pre_amp_slide_shape": 1,
      "amp_slide_shape": 1,
      "pan": 0,
      "pre_mix_slide": 0,
      "pan_slide_curve": 0,
      "amp_slide_curve": 0,
      "amp_slide": 0,
      "pre_mix_slide_curve": 0
    },
    "inherit_base": "FXInfo",
    "inherit_arg": true,
    "summary": "Mono",
    "hiden": false
  },
  "FXBPF": {
    "name": ":fx_bpf",
    "opts": {
      "res": 0.6,
      "pre_amp": 1,
      "pre_amp_slide_curve": 0,
      "res_slide_shape": 1,
      "mix_slide_shape": 1,
      "mix_slide_curve": 0,
      "amp": 1,
      "pre_mix": 1,
      "pre_amp_slide": 0,
      "centre_slide_curve": 0,
      "pre_mix_slide_shape": 1,
      "mix": 1,
      "centre_slide": 0,
      "mix_slide": 0,
      "pre_amp_slide_shape": 1,
      "centre_slide_shape": 1,
      "res_slide": 0,
      "amp_slide_shape": 1,
      "centre": 100,
      "pre_mix_slide": 0,
      "res_slide_curve": 0,
      "amp_slide_curve": 0,
      "amp_slide": 0,
      "pre_mix_slide_curve": 0
    },
    "inherit_base": "FXInfo",
    "inherit_arg": true,
    "summary": "Band Pass Filter",
    "hiden": false
  },
  "FXWobble": {
    "name": ":fx_wobble",
    "opts": {
      "res": 0.8,
      "smooth_up": 0,
      "smooth_down_slide_shape": 1,
      "mix_slide_shape": 1,
      "mix_slide_curve": 0,
      "amp": 1,
      "pre_amp_slide": 0,
      "pulse_width": 0.5,
      "phase": 0.5,
      "prob_pos_slide_shape": 1,
      "cutoff_max": 120,
      "cutoff_max_slide_shape": 1,
      "seed": 0,
      "prob_pos": 0,
      "cutoff_max_slide": 0,
      "cutoff_min_slide_curve": 0,
      "smooth_up_slide": 0,
      "pre_amp_slide_shape": 1,
      "probability_slide_shape": 1,
      "phase_slide": 0,
      "phase_offset": 0,
      "smooth_down": 0,
      "smooth": 0,
      "pre_mix_slide_curve": 0,
      "pulse_width_slide": 0,
      "smooth_up_slide_shape": 1,
      "pre_amp": 1,
      "pre_amp_slide_curve": 0,
      "res_slide_shape": 1,
      "amp_slide_shape": 1,
      "pulse_width_slide_curve": 0,
      "phase_slide_shape": 1,
      "filter": 0,
      "pre_mix": 1,
      "cutoff_min_slide_shape": 1,
      "pulse_width_slide_shape": 1,
      "pre_mix_slide_shape": 1,
      "mix": 1,
      "probability_slide": 0,
      "cutoff_min_slide": 0,
      "probability": 0,
      "smooth_down_slide": 0,
      "mix_slide": 0,
      "smooth_slide_shape": 1,
      "smooth_up_slide_curve": 0,
      "smooth_slide": 0,
      "wave": 0,
      "phase_slide_curve": 0,
      "invert_wave": 0,
      "cutoff_max_slide_curve": 0,
      "pre_mix_slide": 0,
      "smooth_slide_curve": 0,
      "prob_pos_slide_curve": 0,
      "res_slide": 0,
      "prob_pos_slide": 0,
      "smooth_down_slide_curve": 0,
      "probability_slide_curve": 0,
      "amp_slide_curve": 0,
      "amp_slide": 0,
      "res_slide_curve": 0,
      "cutoff_min": 60
    },
    "inherit_base": "FXInfo",
    "inherit_arg": true,
    "summary": "Wobble",
    "hiden": false
  },
  "FXNRBPF": {
    "name": ":fx_nrbpf",
    "opts": {
      "res": 0.5,
      "pre_amp": 1,
      "pre_amp_slide_curve": 0,
      "res_slide_shape": 1,
      "mix_slide_shape": 1,
      "mix_slide_curve": 0,
      "amp": 1,
      "pre_mix": 1,
      "pre_amp_slide": 0,
      "centre_slide_curve": 0,
      "pre_mix_slide_shape": 1,
      "mix": 1,
      "centre_slide": 0,
      "mix_slide": 0,
      "pre_amp_slide_shape": 1,
      "centre_slide_shape": 1,
      "res_slide": 0,
      "amp_slide_shape": 1,
      "centre": 100,
      "pre_mix_slide": 0,
      "res_slide_curve": 0,
      "amp_slide_curve": 0,
      "amp_slide": 0,
      "pre_mix_slide_curve": 0
    },
    "inherit_base": "FXRBPF",
    "inherit_arg": true,
    "summary": "Normalised Resonant Band Pass Filter",
    "hiden": true
  },
  "FXOctaver": {
    "name": ":fx_octaver",
    "opts": {
      "pre_amp": 1,
      "pre_amp_slide_curve": 0,
      "subsub_amp_slide_curve": 0,
      "mix_slide_shape": 1,
      "sub_amp_slide_curve": 0,
      "mix_slide_curve": 0,
      "amp": 1,
      "pre_mix": 1,
      "super_amp_slide_curve": 0,
      "pre_amp_slide": 0,
      "pre_mix_slide_shape": 1,
      "mix": 1,
      "subsub_amp_slide": 0,
      "subsub_amp": 1,
      "super_amp_slide_shape": 1,
      "super_amp": 1,
      "subsub_amp_slide_shape": 1,
      "super_amp_slide": 0,
      "mix_slide": 0,
      "pre_amp_slide_shape": 1,
      "amp_slide_shape": 1,
      "pre_mix_slide": 0,
      "sub_amp": 1,
      "sub_amp_slide": 0,
      "amp_slide_curve": 0,
      "amp_slide": 0,
      "pre_mix_slide_curve": 0,
      "sub_amp_slide_shape": 1
    },
    "inherit_base": "FXInfo",
    "inherit_arg": true,
    "summary": "Octaver",
    "hiden": false
  },
  "FXWhammy": {
    "name": ":fx_whammy",
    "opts": {
      "transpose_slide_shape": 1,
      "pre_amp": 1,
      "pre_amp_slide_curve": 0,
      "mix_slide_shape": 1,
      "mix_slide_curve": 0,
      "amp": 1,
      "pre_mix": 1,
      "pre_amp_slide": 0,
      "pre_mix_slide_shape": 1,
      "transpose_slide_curve": 0,
      "mix": 1,
      "max_delay_time": 1,
      "transpose_slide": 0,
      "deltime": 0.05,
      "mix_slide": 0,
      "pre_amp_slide_shape": 1,
      "amp_slide_shape": 1,
      "pre_mix_slide": 0,
      "grainsize": 0.075,
      "transpose": 12,
      "amp_slide_curve": 0,
      "amp_slide": 0,
      "pre_mix_slide_curve": 0
    },
    "inherit_base": "FXInfo",
    "inherit_arg": true,
    "summary": "Whammy",
    "hiden": false
  },
  "FXLevel": {
    "name": ":fx_level",
    "opts": {
      "amp_slide_shape": 1,
      "amp": 1,
      "amp_slide_curve": 0,
      "amp_slide": 0
    },
    "inherit_base": "FXInfo",
    "inherit_arg": false,
    "summary": "Level Amplifier",
    "hiden": false
  },
  "FXReverb": {
    "name": ":fx_reverb",
    "opts": {
      "damp_slide_shape": 1,
      "pre_amp": 1,
      "pre_amp_slide_curve": 0,
      "damp_slide_curve": 0,
      "room_slide_shape": 1,
      "mix_slide_shape": 1,
      "mix_slide_curve": 0,
      "amp": 1,
      "pre_mix": 1,
      "pre_amp_slide": 0,
      "pre_mix_slide_shape": 1,
      "mix": 0.4,
      "damp_slide": 0,
      "room_slide": 0,
      "room_slide_curve": 0,
      "mix_slide": 0,
      "pre_amp_slide_shape": 1,
      "amp_slide_shape": 1,
      "pre_mix_slide": 0,
      "room": 0.6,
      "amp_slide_curve": 0,
      "amp_slide": 0,
      "pre_mix_slide_curve": 0,
      "damp": 0.5
    },
    "inherit_base": "FXInfo",
    "inherit_arg": true,
    "summary": "Reverb",
    "hiden": false
  },
  "FXInfo": {
    "inherit_arg": false,
    "opts": {
      "pre_amp": 1,
      "pre_amp_slide_curve": 0,
      "mix_slide": 0,
      "mix_slide_shape": 1,
      "pre_amp_slide_shape": 1,
      "mix_slide_curve": 0,
      "amp": 1,
      "pre_mix": 1,
      "pre_amp_slide": 0,
      "amp_slide_shape": 1,
      "pre_mix_slide_shape": 1,
      "pre_mix_slide": 0,
      "mix": 1,
      "amp_slide_curve": 0,
      "amp_slide": 0,
      "pre_mix_slide_curve": 0
    },
    "hiden": true,
    "inherit_base": "BaseInfo"
  },
  "FXNormHPF": {
    "name": ":fx_nhpf",
    "opts": {
      "pre_amp": 1,
      "pre_amp_slide_curve": 0,
      "cutoff": 100,
      "mix_slide_shape": 1,
      "mix_slide_curve": 0,
      "amp": 1,
      "pre_mix": 1,
      "pre_amp_slide": 0,
      "pre_mix_slide_shape": 1,
      "mix": 1,
      "cutoff_slide": 0,
      "mix_slide": 0,
      "cutoff_slide_shape": 1,
      "pre_amp_slide_shape": 1,
      "amp_slide_shape": 1,
      "pre_mix_slide": 0,
      "cutoff_slide_curve": 0,
      "amp_slide_curve": 0,
      "amp_slide": 0,
      "pre_mix_slide_curve": 0
    },
    "inherit_base": "FXHPF",
    "inherit_arg": true,
    "summary": "Normalised High Pass Filter",
    "hiden": true
  },
  "FXLPF": {
    "name": ":fx_lpf",
    "opts": {
      "pre_amp": 1,
      "pre_amp_slide_curve": 0,
      "cutoff": 100,
      "mix_slide_shape": 1,
      "mix_slide_curve": 0,
      "amp": 1,
      "pre_mix": 1,
      "pre_amp_slide": 0,
      "pre_mix_slide_shape": 1,
      "mix": 1,
      "cutoff_slide": 0,
      "mix_slide": 0,
      "cutoff_slide_shape": 1,
      "pre_amp_slide_shape": 1,
      "amp_slide_shape": 1,
      "pre_mix_slide": 0,
      "cutoff_slide_curve": 0,
      "amp_slide_curve": 0,
      "amp_slide": 0,
      "pre_mix_slide_curve": 0
    },
    "inherit_base": "FXInfo",
    "inherit_arg": true,
    "summary": "Low Pass Filter",
    "hiden": false
  },
  "FXEcho": {
    "name": ":fx_echo",
    "opts": {
      "decay": 2,
      "pre_amp": 1,
      "pre_amp_slide_curve": 0,
      "mix_slide_shape": 1,
      "mix_slide_curve": 0,
      "amp": 1,
      "pre_mix": 1,
      "pre_amp_slide": 0,
      "pre_mix_slide_shape": 1,
      "decay_slide_curve": 0,
      "mix": 1,
      "phase_slide": 0,
      "decay_slide": 0,
      "mix_slide": 0,
      "pre_amp_slide_shape": 1,
      "decay_slide_shape": 1,
      "phase_slide_curve": 0,
      "phase_slide_shape": 1,
      "amp_slide_shape": 1,
      "pre_mix_slide": 0,
      "max_phase": 2,
      "amp_slide_curve": 0,
      "amp_slide": 0,
      "pre_mix_slide_curve": 0,
      "phase": 0.25
    },
    "inherit_base": "FXInfo",
    "inherit_arg": true,
    "summary": "Echo",
    "hiden": false
  },
  "FXRBPF": {
    "name": ":fx_rbpf",
    "opts": {
      "res": 0.5,
      "pre_amp": 1,
      "pre_amp_slide_curve": 0,
      "res_slide_shape": 1,
      "mix_slide_shape": 1,
      "mix_slide_curve": 0,
      "amp": 1,
      "pre_mix": 1,
      "pre_amp_slide": 0,
      "centre_slide_curve": 0,
      "pre_mix_slide_shape": 1,
      "mix": 1,
      "centre_slide": 0,
      "mix_slide": 0,
      "pre_amp_slide_shape": 1,
      "centre_slide_shape": 1,
      "res_slide": 0,
      "amp_slide_shape": 1,
      "centre": 100,
      "pre_mix_slide": 0,
      "pre_mix_slide_curve": 0,
      "amp_slide_curve": 0,
      "amp_slide": 0,
      "res_slide_curve": 0
    },
    "inherit_base": "FXBPF",
    "inherit_arg": true,
    "summary": "Resonant Band Pass Filter",
    "hiden": true
  },
  "FXGVerb": {
    "name": ":fx_gverb",
    "opts": {
      "damp_slide_shape": 1,
      "pre_amp": 1,
      "pre_amp_slide_curve": 0,
      "damp_slide_curve": 0,
      "ref_level": 0.7,
      "mix_slide_shape": 1,
      "mix_slide_curve": 0,
      "amp": 1,
      "pre_mix": 1,
      "pre_damp_slide": 0,
      "pre_amp_slide": 0,
      "dry_slide": 0,
      "pre_mix_slide_shape": 1,
      "spread": 0.5,
      "pre_damp_slide_shape": 1,
      "mix": 1,
      "tail_level": 0.5,
      "damp_slide": 0,
      "pre_damp_slide_curve": 0,
      "dry": 1,
      "dry_slide_shape": 1,
      "release": 3,
      "mix_slide": 0,
      "pre_amp_slide_shape": 1,
      "spread_slide": 0,
      "amp_slide_shape": 1,
      "spread_slide_shape": 1,
      "pre_mix_slide": 0,
      "pre_damp": 0.5,
      "dry_slide_curve": 0,
      "room": 10,
      "spread_slide_curve": 0,
      "amp_slide_curve": 0,
      "amp_slide": 0,
      "pre_mix_slide_curve": 0,
      "damp": 0.5
    },
    "inherit_base": "FXInfo",
    "inherit_arg": true,
    "summary": "GVerb",
    "hiden": false
  }
}

samples = {
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
  "Miscellaneous Sounds": [
    ":misc_burp",
    ":misc_crow",
    ":misc_cineboom"
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
  ]
}

