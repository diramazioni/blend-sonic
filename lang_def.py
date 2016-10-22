null = None; true = True; false = False;
#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/

lang_core = {
  "assert": {
    "accepts_block": false,
    "alt_args": {
      "arg": ":anything",
      "error_msg": ":string"
    },
    "args": {
      "arg": ":anything"
    },
    "introduced": "2,8,0",
    "opts": null,
    "signature": {
      "arg": null,
      "msg": "nil"
    },
    "summary": "Ensure arg is valid"
  },
  "assert_equal": {
    "accepts_block": false,
    "alt_args": {
      "arg1": ":anything",
      "arg2": ":anything",
      "error_msg": ":string"
    },
    "args": {
      "arg1": ":anything",
      "arg2": ":anything"
    },
    "introduced": "2,8,0",
    "opts": null,
    "signature": {
      "arg1": null,
      "arg2": null,
      "msg": "nil"
    },
    "summary": "Ensure args are equal"
  },
  "at": {
    "accepts_block": true,
    "args": {
      "params": ":list",
      "times": ":list"
    },
    "async_block": true,
    "introduced": "2,1,0",
    "opts": null,
    "requires_block": true,
    "signature": {
      "&block": null,
      "params": "nil",
      "times": 0
    },
    "summary": "Asynchronous Time. Run a block at the given time(s)"
  },
  "beat": {
    "accepts_block": false,
    "args": {},
    "introduced": "2,10,0",
    "opts": null,
    "summary": "Get current beat"
  },
  "block_duration": {
    "accepts_block": true,
    "args": {},
    "async_block": false,
    "introduced": "2,9,0",
    "opts": null,
    "requires_block": true,
    "signature": {
      "&block": null
    },
    "summary": "Return block duration"
  },
  "block_slept?": {
    "accepts_block": true,
    "args": {},
    "async_block": false,
    "introduced": "2,9,0",
    "opts": null,
    "requires_block": true,
    "signature": {
      "&block": null
    },
    "summary": "Determine if block contains sleep time"
  },
  "bools": {
    "accepts_block": false,
    "args": {
      "list": ":array"
    },
    "introduced": "2,2,0",
    "opts": null,
    "returns": ":ring",
    "signature": {
      "*args": null
    },
    "summary": "Create a ring of boolean values"
  },
  "bt": {
    "accepts_block": false,
    "args": {
      "seconds": ":number"
    },
    "introduced": "2,8,0",
    "opts": null,
    "signature": {
      "t": null
    },
    "summary": "Beat time conversion"
  },
  "choose": {
    "accepts_block": false,
    "args": {
      "list": ":array"
    },
    "introduced": "2,0,0",
    "opts": null,
    "signature": {
      "args": null
    },
    "summary": "Random list selection"
  },
  "clear": {
    "accepts_block": false,
    "args": {},
    "introduced": "2,11,0",
    "opts": null,
    "returns": null,
    "summary": "Clear all thread locals to defaults"
  },
  "comment": {
    "accepts_block": true,
    "introduced": "2,0,0",
    "opts": null,
    "requires_block": true,
    "signature": {
      "&block": null,
      "*args": null
    },
    "summary": "Block level commenting"
  },
  "cue": {
    "accepts_block": false,
    "args": {
      "cue_id": ":symbol"
    },
    "introduced": "2,0,0",
    "opts": {
      "key": "foo: 64"
    },
    "signature": {
      "*opts": null,
      "cue_id": null
    },
    "summary": "Cue other threads"
  },
  "current_beat_duration": {
    "accepts_block": false,
    "introduced": "2,6,0",
    "opts": null,
    "summary": "Duration of current beat"
  },
  "current_bpm": {
    "accepts_block": false,
    "introduced": "2,0,0",
    "opts": null,
    "summary": "Get current tempo"
  },
  "current_random_seed": {
    "accepts_block": false,
    "introduced": "2,10,0",
    "opts": null,
    "summary": "Get current random seed"
  },
  "dec": {
    "accepts_block": false,
    "args": {
      "n": ":number"
    },
    "introduced": "2, 1, 0",
    "opts": {},
    "signature": {
      "n": null
    },
    "summary": "Decrement"
  },
  "define": {
    "accepts_block": true,
    "args": {
      "name": ":symbol"
    },
    "intro_fn": true,
    "introduced": "2,0,0",
    "opts": null,
    "requires_block": true,
    "signature": {
      "&block": null,
      "name": null
    },
    "summary": "Define a new function"
  },
  "defonce": {
    "accepts_block": true,
    "args": {
      "name": ":symbol"
    },
    "introduced": "2,0,0",
    "opts": {
      "override": false
    },
    "requires_block": true,
    "signature": {
      "&block": null,
      "*opts": null,
      "name": null
    },
    "summary": "Define a named value only once"
  },
  "density": {
    "accepts_block": true,
    "args": {
      "d": ":density"
    },
    "introduced": "2,3,0",
    "opts": null,
    "signature": {
      "&block": null,
      "d": null
    },
    "summary": "Squash and repeat time"
  },
  "dice": {
    "accepts_block": false,
    "args": {
      "num_sides": ":number"
    },
    "introduced": "2,0,0",
    "opts": null,
    "signature": {
      "num_sides": 6
    },
    "summary": "Random dice throw"
  },
  "doubles": {
    "accepts_block": false,
    "args": {
      "num_doubles": ":int",
      "start": ":number"
    },
    "introduced": "2,10,0",
    "memoize": true,
    "opts": null,
    "returns": ":ring",
    "signature": {
      "num_doubles": 1,
      "start": null
    },
    "summary": "Create a ring of successive doubles"
  },
  "factor?": {
    "accepts_block": false,
    "args": {
      "factor": ":number",
      "val": ":number"
    },
    "introduced": "2,1,0",
    "opts": null,
    "signature": {
      "factor": null,
      "val": null
    },
    "summary": "Factor test"
  },
  "halves": {
    "accepts_block": false,
    "args": {
      "num_halves": ":int",
      "start": ":number"
    },
    "introduced": "2,10,0",
    "memoize": true,
    "opts": null,
    "returns": ":ring",
    "signature": {
      "num_halves": 1,
      "start": null
    },
    "summary": "Create a ring of successive halves"
  },
  "in_thread": {
    "accepts_block": true,
    "async_block": true,
    "introduced": "2,0,0",
    "opts": {
      "sync_bpm": ":foo"
    },
    "requires_block": true,
    "signature": {
      "&block": null,
      "*opts": null
    },
    "summary": "Run code block at the same time"
  },
  "inc": {
    "accepts_block": false,
    "args": {
      "n": ":number"
    },
    "introduced": "2, 1, 0",
    "opts": {},
    "signature": {
      "n": null
    },
    "summary": "Increment"
  },
  "knit": {
    "accepts_block": false,
    "args": {
      "count": ":number",
      "value": ":anything"
    },
    "introduced": "2,2,0",
    "opts": null,
    "returns": ":ring",
    "signature": {
      "*args": null
    },
    "summary": "Knit a sequence of repeated values"
  },
  "line": {
    "accepts_block": false,
    "args": {
      "finish": ":number",
      "start": ":number"
    },
    "introduced": "2,5,0",
    "memoize": true,
    "opts": {
      "inclusive": false
    },
    "returns": ":ring",
    "signature": {
      "*args": null,
      "finish": null,
      "start": null
    },
    "summary": "Create a ring buffer representing a straight line"
  },
  "live_loop": {
    "accepts_block": true,
    "args": {
      "name": ":symbol"
    },
    "async_block": true,
    "intro_fn": true,
    "introduced": "2,1,0",
    "opts": "}",
    "requires_block": true,
    "signature": {
      "&block": null,
      "*args": null,
      "name": "nil"
    },
    "summary": "A loop for live coding"
  },
  "load_buffer": {
    "accepts_block": false,
    "args": {
      "path": ":string"
    },
    "introduced": "2,10,0",
    "opts": null,
    "signature": {
      "path": null
    },
    "summary": "Load the contents of a file to the current buffer"
  },
  "load_example": {
    "accepts_block": false,
    "args": {
      "path": ":string"
    },
    "introduced": "2,10,0",
    "opts": null,
    "signature": {
      "example_name": null
    },
    "summary": "Load a built-in example"
  },
  "look": {
    "accepts_block": false,
    "alt_args": {
      "key": ":symbol"
    },
    "introduced": "2,6,0",
    "opts": {
      "offset": 0
    },
    "returns": ":number",
    "signature": {
      "*args": null
    },
    "summary": "Obtain value of a tick"
  },
  "ndefine": {
    "accepts_block": true,
    "args": {
      "name": ":symbol"
    },
    "introduced": "2,1,0",
    "opts": null,
    "requires_block": true,
    "signature": {
      "&block": null,
      "name": null
    },
    "summary": "Define a new function"
  },
  "on": {
    "accepts_block": false,
    "args": {
      "condition": ":truthy"
    },
    "introduced": "2,10,0",
    "opts": null,
    "returns": null,
    "signature": {
      "&blk": null,
      "condition": null
    },
    "summary": "Optionally evaluate block"
  },
  "one_in": {
    "accepts_block": false,
    "args": {
      "num": ":number"
    },
    "introduced": "2,0,0",
    "opts": null,
    "signature": {
      "num": null
    },
    "summary": "Random true value with specified probability"
  },
  "osc": {
    "signature": {
      "*args": null,
      "path": null
    }
  },
  "pick": {
    "accepts_block": false,
    "args": {
      "list": ":array",
      "n": ":number_or_nil"
    },
    "introduced": "2,10,0",
    "opts": {
      "skip": 0
    },
    "signature": {
      "*args": null
    },
    "summary": "Randomly pick from list (with duplicates)"
  },
  "print": {
    "accepts_block": false,
    "args": {
      "output": ":anything"
    },
    "intro_fn": true,
    "introduced": "2,0,0",
    "opts": null,
    "signature": {
      "*msgs": null
    },
    "summary": "Display a message in the output pane"
  },
  "puts": {
    "accepts_block": false,
    "args": {
      "output": ":anything"
    },
    "intro_fn": true,
    "introduced": "2,0,0",
    "opts": null,
    "signature": {
      "*msgs": null
    },
    "summary": "Display a message in the output pane"
  },
  "quantise": {
    "accepts_block": false,
    "args": {
      "n": ":number",
      "step": ":positive_number"
    },
    "introduced": "2,1,0",
    "opts": null,
    "signature": {
      "n": null,
      "step": null
    },
    "summary": "Quantise a value to resolution"
  },
  "ramp": {
    "accepts_block": false,
    "args": {
      "list": ":array"
    },
    "introduced": "2,6,0",
    "opts": null,
    "returns": ":ramp",
    "signature": {
      "*args": null
    },
    "summary": "Create a ramp vector"
  },
  "rand": {
    "accepts_block": false,
    "args": {
      "max": ":number_or_range"
    },
    "intro_fn": true,
    "introduced": "2,0,0",
    "opts": null,
    "signature": {
      "max": 1
    },
    "summary": "Generate a random float below a value"
  },
  "rand_back": {
    "accepts_block": false,
    "args": {
      "amount": ":number"
    },
    "introduced": "2,7,0",
    "opts": null,
    "signature": {
      "amount": 1
    },
    "summary": "Roll back random generator"
  },
  "rand_i": {
    "accepts_block": false,
    "args": {
      "max": ":number_or_range"
    },
    "introduced": "2,0,0",
    "opts": null,
    "signature": {
      "max": 2
    },
    "summary": "Generate a random whole number below a value (exclusive)"
  },
  "rand_i_look": {
    "accepts_block": false,
    "args": {
      "max": ":number_or_range"
    },
    "introduced": "2,11,0",
    "opts": null,
    "signature": {
      "*args": null
    },
    "summary": "Generate a random whole number without consuming a rand"
  },
  "rand_look": {
    "accepts_block": false,
    "args": {
      "max": ":number_or_range"
    },
    "introduced": "2,11,0",
    "opts": null,
    "signature": {
      "*args": null
    },
    "summary": "Generate a random number without consuming a rand"
  },
  "rand_reset": {
    "accepts_block": false,
    "args": {},
    "introduced": "2,7,0",
    "opts": null,
    "summary": "Reset rand generator to last seed"
  },
  "rand_skip": {
    "accepts_block": false,
    "args": {
      "amount": ":number"
    },
    "introduced": "2,7,0",
    "opts": null,
    "signature": {
      "amount": 1
    },
    "summary": "Jump forward random generator"
  },
  "range": {
    "accepts_block": false,
    "args": {
      "finish": ":number",
      "start": ":number",
      "step_size": ":number"
    },
    "introduced": "2,2,0",
    "memoize": true,
    "opts": {
      "inclusive": false
    },
    "returns": ":ring",
    "signature": {
      "*args": null,
      "finish": null,
      "start": null
    },
    "summary": "Create a ring buffer with the specified start, finish and step size"
  },
  "rdist": {
    "accepts_block": false,
    "alt_args": {
      "width": ":number"
    },
    "args": {
      "centre": ":number",
      "width": ":number"
    },
    "introduced": "2,3,0",
    "opts": {
      "step": 1
    },
    "signature": {
      "*opts": null,
      "centre": 0,
      "width": null
    },
    "summary": "Random number in centred distribution"
  },
  "reset": {
    "accepts_block": false,
    "args": {},
    "introduced": "2,11,0",
    "opts": null,
    "returns": null,
    "summary": "Reset all thread locals"
  },
  "ring": {
    "accepts_block": false,
    "args": {
      "list": ":array"
    },
    "introduced": "2,2,0",
    "opts": null,
    "returns": ":ring",
    "signature": {
      "*args": null
    },
    "summary": "Create a ring buffer"
  },
  "rrand": {
    "accepts_block": false,
    "args": {
      "max": ":number",
      "min": ":number"
    },
    "intro_fn": true,
    "introduced": "2,0,0",
    "opts": {
      "step": 1
    },
    "signature": {
      "*opts": null,
      "max": null,
      "min": null
    },
    "summary": "Generate a random float between two numbers"
  },
  "rrand_i": {
    "accepts_block": false,
    "args": {
      "max": ":number",
      "min": ":number"
    },
    "introduced": "2,0,0",
    "opts": null,
    "signature": {
      "max": null,
      "min": null
    },
    "summary": "Generate a random whole number between two points inclusively"
  },
  "rt": {
    "accepts_block": false,
    "args": {
      "seconds": ":number"
    },
    "introduced": "2,0,0",
    "opts": null,
    "signature": {
      "t": null
    },
    "summary": "Real time conversion"
  },
  "run_code": {
    "accepts_block": false,
    "args": {
      "code": ":string"
    },
    "introduced": "2,11,0",
    "opts": null,
    "returns": null,
    "signature": {
      "code": null
    },
    "summary": "Evaluate the code passed as a String as a new Run"
  },
  "run_file": {
    "accepts_block": false,
    "args": {
      "filename": ":path"
    },
    "introduced": "2,11,0",
    "opts": null,
    "returns": null,
    "signature": {
      "path": null
    },
    "summary": "Evaluate the contents of the file as a new Run"
  },
  "shuffle": {
    "accepts_block": false,
    "args": {
      "list": ":array"
    },
    "introduced": "2,1,0",
    "opts": null,
    "signature": {
      "list": null
    },
    "summary": "Randomise order of a list"
  },
  "sleep": {
    "accepts_block": false,
    "advances_time": true,
    "args": {
      "beats": ":number"
    },
    "introduced": "2,0,0",
    "opts": null,
    "signature": {
      "beats": null
    },
    "summary": "Wait for beat duration"
  },
  "spark": {
    "accepts_block": false,
    "hide": false,
    "introduced": "2,5,0",
    "opts": null,
    "signature": {
      "*values": null
    },
    "summary": "Print a string representing a list of numeric values as a spark graph/bar chart"
  },
  "spark_graph": {
    "accepts_block": false,
    "introduced": "2,5,0",
    "opts": null,
    "signature": {
      "*values": null
    },
    "summary": "Returns a string representing a list of numeric values as a spark graph/bar chart"
  },
  "spread": {
    "accepts_block": false,
    "args": {
      "num_accents": ":number",
      "size": ":number"
    },
    "introduced": "2,4,0",
    "opts": {
      "rotate": false
    },
    "returns": ":ring",
    "signature": {
      "*args": null,
      "num_accents": null,
      "size": null
    },
    "summary": "Euclidean distribution for beats"
  },
  "stop": {
    "accepts_block": false,
    "introduced": "2,5,0",
    "opts": null,
    "returns": null,
    "summary": "Stop current thread or run"
  },
  "stretch": {
    "accepts_block": false,
    "args": {
      "count": ":number",
      "list": ":anything"
    },
    "introduced": "2,6,0",
    "opts": null,
    "returns": ":ring",
    "signature": {
      "*args": null
    },
    "summary": "Stretch a sequence of values"
  },
  "sync": {
    "accepts_block": false,
    "advances_time": true,
    "args": {
      "cue_id": ":symbol"
    },
    "introduced": "2,0,0",
    "opts": {
      "bpm_sync": false
    },
    "signature": {
      "cue_ids": null,
      "opts": "{}"
    },
    "summary": "Sync with other threads"
  },
  "sync_bpm": {
    "accepts_block": false,
    "advances_time": true,
    "args": {
      "cue_id": ":symbol"
    },
    "introduced": "2,10,0",
    "opts": {},
    "signature": {
      "cue_ids": null,
      "opts": "{}"
    },
    "summary": "Sync and inherit BPM from other threads "
  },
  "tick": {
    "accepts_block": false,
    "alt_args": {
      "key": ":symbol",
      "value": ":number"
    },
    "args": {
      "key": ":symbol"
    },
    "introduced": "2,6,0",
    "opts": {
      "offset": 0
    },
    "returns": ":number",
    "signature": {
      "*args": null
    },
    "summary": "Increment a tick and return value"
  },
  "tick_reset": {
    "accepts_block": false,
    "alt_args": {
      "key": ":symbol"
    },
    "introduced": "2,6,0",
    "opts": null,
    "returns": ":number",
    "signature": {
      "*args": null
    },
    "summary": "Reset tick to 0"
  },
  "tick_reset_all": {
    "accepts_block": false,
    "alt_args": {
      "key": ":symbol",
      "value": ":number"
    },
    "args": {
      "value": ":number"
    },
    "introduced": "2,6,0",
    "opts": null,
    "returns": null,
    "summary": "Reset all ticks"
  },
  "tick_set": {
    "accepts_block": false,
    "alt_args": {
      "key": ":symbol",
      "value": ":number"
    },
    "args": {
      "value": ":number"
    },
    "introduced": "2,6,0",
    "opts": null,
    "returns": ":number",
    "signature": {
      "*args": null
    },
    "summary": "Set tick to a specific value"
  },
  "time_shift": {
    "accepts_block": true,
    "args": {
      "delta_time": ":number"
    },
    "introduced": "2,11,0",
    "opts": null,
    "returns": null,
    "signature": {
      "&blk": null,
      "delta": null
    },
    "summary": "Slide time forwards or backwards for the given block"
  },
  "uncomment": {
    "accepts_block": true,
    "introduced": "2,0,0",
    "opts": null,
    "requires_block": true,
    "signature": {
      "&block": null,
      "*args": null
    },
    "summary": "Block level comment ignoring"
  },
  "use_bpm": {
    "accepts_block": false,
    "args": {
      "bpm": ":number"
    },
    "intro_fn": true,
    "introduced": "2,0,0",
    "opts": null,
    "signature": {
      "&block": null,
      "bpm": null
    },
    "summary": "Set the tempo"
  },
  "use_bpm_mul": {
    "accepts_block": false,
    "args": {
      "mul": ":number"
    },
    "introduced": "2,3,0",
    "opts": null,
    "signature": {
      "&block": null,
      "mul": null
    },
    "summary": "Set new tempo as a multiple of current tempo"
  },
  "use_cue_logging": {
    "accepts_block": false,
    "args": {
      "true_or_false": ":boolean"
    },
    "introduced": "2,6,0",
    "opts": null,
    "signature": {
      "&block": null,
      "v": null
    },
    "summary": "Enable and disable cue logging"
  },
  "use_osc": {
    "signature": {
      "host_or_port": null,
      "port": "nil"
    }
  },
  "use_random_seed": {
    "accepts_block": false,
    "args": {
      "seed": ":number"
    },
    "introduced": "2,0,0",
    "opts": null,
    "signature": {
      "&block": null,
      "seed": null
    },
    "summary": "Set random seed generator to known seed"
  },
  "vector": {
    "accepts_block": false,
    "args": {
      "list": ":array"
    },
    "introduced": "2,6,0",
    "opts": null,
    "returns": ":vector",
    "signature": {
      "*args": null
    },
    "summary": "Create a vector"
  },
  "version": {
    "accepts_block": false,
    "introduced": "2,0,0",
    "opts": null,
    "summary": "Get current version information"
  },
  "vt": {
    "accepts_block": false,
    "introduced": "2,1,0",
    "opts": null,
    "summary": "Get virtual time"
  },
  "wait": {
    "accepts_block": false,
    "advances_time": true,
    "args": {
      "beats": ":number"
    },
    "introduced": "2,0,0",
    "opts": null,
    "signature": {
      "time": null
    },
    "summary": "Wait for duration"
  },
  "with_bpm": {
    "accepts_block": true,
    "args": {
      "bpm": ":number"
    },
    "introduced": "2,0,0",
    "opts": null,
    "requires_block": true,
    "signature": {
      "&block": null,
      "bpm": null
    },
    "summary": "Set the tempo for the code block"
  },
  "with_bpm_mul": {
    "accepts_block": true,
    "args": {
      "mul": ":number"
    },
    "introduced": "2,3,0",
    "opts": null,
    "requires_block": true,
    "signature": {
      "&block": null,
      "mul": null
    },
    "summary": "Set new tempo as a multiple of current tempo for block"
  },
  "with_cue_logging": {
    "accepts_block": true,
    "args": {
      "true_or_false": ":boolean"
    },
    "introduced": "2,6,0",
    "opts": null,
    "requires_block": true,
    "signature": {
      "&block": null,
      "v": null
    },
    "summary": "Block-level enable and disable cue logging"
  },
  "with_random_seed": {
    "accepts_block": true,
    "args": {
      "seed": ":number"
    },
    "introduced": "2,0,0",
    "opts": null,
    "requires_block": true,
    "signature": {
      "&block": null,
      "seed": null
    },
    "summary": "Specify random seed for code block"
  },
  "with_tempo": {
    "signature": {
      "&block": null,
      "*args": null
    }
  }
}

core_args_types_conversion = {}

core_opts_types_conversion = {}

#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/

lang_sound = {
  "all_sample_names": {
    "accepts_block": false,
    "introduced": "2,0,0",
    "memoize": true,
    "opts": null,
    "summary": "Get all sample names"
  },
  "chord": {
    "accepts_block": false,
    "args": {
      "name": ":symbol",
      "tonic": ":symbol"
    },
    "intro_fn": true,
    "introduced": "2,0,0",
    "memoize": true,
    "opts": {
      "num_octaves": 1
    },
    "returns": ":ring",
    "signature": {
      "*opts": null,
      "tonic_or_name": null
    },
    "summary": "Create chord"
  },
  "chord_degree": {
    "accepts_block": false,
    "args": {
      "degree": ":symbol_or_number",
      "number_of_notes": ":number",
      "scale": ":symbol",
      "tonic": ":symbol"
    },
    "introduced": "2,1,0",
    "memoize": true,
    "opts": null,
    "returns": ":ring",
    "signature": {
      "*opts": null,
      "degree": null,
      "number_of_notes": 4,
      "scale": ":major",
      "tonic": null
    },
    "summary": "Construct chords of stacked thirds, based on scale degrees"
  },
  "chord_invert": {
    "accepts_block": false,
    "args": {
      "notes": ":list",
      "shift": ":number"
    },
    "introduced": "2,6,0",
    "opts": null,
    "returns": ":ring",
    "signature": {
      "notes": null,
      "shift": null
    },
    "summary": "Chord inversion"
  },
  "chord_names": {
    "accepts_block": false,
    "introduced": "2,6,0",
    "memoize": true,
    "opts": null,
    "summary": "All chord names"
  },
  "control": {
    "accepts_block": false,
    "args": {
      "node": ":synth_node"
    },
    "introduced": "2,0,0",
    "opts": {},
    "signature": {
      "*args": null
    },
    "summary": "Control running synth"
  },
  "current_amp": {},
  "current_arg_checks": {
    "accepts_block": false,
    "introduced": "2,0,0",
    "opts": null,
    "summary": "Get current arg checking status"
  },
  "current_cent_tuning": {
    "accepts_block": false,
    "introduced": "2,9,0",
    "opts": null,
    "summary": "Get current cent shift"
  },
  "current_debug": {
    "accepts_block": false,
    "introduced": "2,0,0",
    "opts": null,
    "summary": "Get current debug status"
  },
  "current_octave": {
    "accepts_block": false,
    "introduced": "2,9,0",
    "opts": null,
    "summary": "Get current octave shift"
  },
  "current_sample_defaults": {
    "accepts_block": false,
    "introduced": "2,5,0",
    "opts": null,
    "summary": "Get current sample defaults"
  },
  "current_sched_ahead_time": {
    "accepts_block": false,
    "introduced": "2,0,0",
    "opts": null,
    "summary": "Get current sched ahead time"
  },
  "current_synth": {
    "accepts_block": false,
    "introduced": "2,0,0",
    "opts": null,
    "summary": "Get current synth"
  },
  "current_synth_defaults": {
    "accepts_block": false,
    "introduced": "2,0,0",
    "opts": null,
    "summary": "Get current synth defaults"
  },
  "current_transpose": {
    "accepts_block": false,
    "introduced": "2,0,0",
    "opts": null,
    "summary": "Get current transposition"
  },
  "current_volume": {
    "accepts_block": false,
    "introduced": "2,0,0",
    "opts": null,
    "summary": "Get current volume"
  },
  "degree": {
    "accepts_block": false,
    "args": {
      "degree": ":symbol_or_number",
      "scale": ":symbol",
      "tonic": ":symbol"
    },
    "introduced": "2,1,0",
    "signature": {
      "degree": null,
      "scale": null,
      "tonic": null
    },
    "summary": "Convert a degree into a note"
  },
  "fx_names": {
    "accepts_block": false,
    "introduced": "2,10,0",
    "memoize": true,
    "opts": null,
    "summary": "Get all FX names"
  },
  "hz_to_midi": {
    "accepts_block": false,
    "args": {
      "freq": ":number"
    },
    "introduced": "2,0,0",
    "opts": null,
    "signature": {
      "freq": null
    },
    "summary": "Hz to MIDI conversion"
  },
  "invert_chord": {
    "signature": {
      "*args": null
    }
  },
  "kill": {
    "accepts_block": false,
    "args": {
      "node": ":synth_node"
    },
    "introduced": "2,0,0",
    "opts": {},
    "signature": {
      "node": null
    },
    "summary": "Kill synth"
  },
  "load_sample": {
    "accepts_block": false,
    "args": {
      "path": ":string"
    },
    "introduced": "2,0,0",
    "opts": null,
    "signature": {
      "*args": null
    },
    "summary": "Pre-load first matching sample"
  },
  "load_sample_at_path": {
    "signature": {
      "path": null
    }
  },
  "load_samples": {
    "accepts_block": false,
    "args": {
      "paths": ":list"
    },
    "introduced": "2,0,0",
    "opts": null,
    "signature": {
      "*args": null
    },
    "summary": "Pre-load all matching samples"
  },
  "load_synthdefs": {
    "accepts_block": false,
    "args": {
      "path": ":string"
    },
    "introduced": "2,0,0",
    "opts": null,
    "signature": {
      "path": "synthdef_path"
    },
    "summary": "Load external synthdefs"
  },
  "midi_notes": {
    "accepts_block": false,
    "args": {
      "list": ":array"
    },
    "introduced": "2,7,0",
    "memoize": true,
    "opts": null,
    "returns": ":ring",
    "signature": {
      "*args": null
    },
    "summary": "Create a ring buffer of midi note numbers"
  },
  "midi_to_hz": {
    "accepts_block": false,
    "args": {
      "note": ":symbol_or_number"
    },
    "introduced": "2,0,0",
    "opts": null,
    "signature": {
      "n": null
    },
    "summary": "MIDI to Hz conversion"
  },
  "note": {
    "accepts_block": false,
    "args": {
      "note": ":symbol_or_number"
    },
    "introduced": "2,0,0",
    "opts": {
      "octave": 4
    },
    "signature": {
      "*args": null,
      "n": null
    },
    "summary": "Describe note"
  },
  "note_info": {
    "accepts_block": false,
    "args": {
      "note": ":symbol_or_number"
    },
    "introduced": "2,0,0",
    "opts": {
      "octave": 4
    },
    "signature": {
      "*args": null,
      "n": null
    },
    "summary": "Get note info"
  },
  "note_range": {
    "accepts_block": false,
    "args": {
      "high_note": ":note",
      "low_note": ":note"
    },
    "introduced": "2,6,0",
    "opts": {
      "pitches": []
    },
    "returns": ":ring",
    "signature": {
      "*opts": null,
      "high_note": null,
      "low_note": null
    },
    "summary": "Get a range of notes"
  },
  "octs": {
    "accepts_block": false,
    "args": {
      "num_octaves": ":pos_int",
      "start": ":note"
    },
    "introduced": "2,8,0",
    "opts": null,
    "returns": ":ring",
    "signature": {
      "num_octs": 1,
      "start": null
    },
    "summary": "Create a ring of octaves"
  },
  "pitch_ratio": {
    "signature": {
      "*args": null
    }
  },
  "pitch_to_ratio": {
    "accepts_block": false,
    "args": {
      "pitch": ":midi_number"
    },
    "introduced": "2,5,0",
    "opts": null,
    "signature": {
      "m": null
    },
    "summary": "relative MIDI pitch to frequency ratio"
  },
  "play": {
    "accepts_block": true,
    "args": {
      "note": ":symbol_or_number"
    },
    "intro_fn": true,
    "introduced": "2,0,0",
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
    "signature": {
      "&blk": null,
      "*args": null,
      "n": null
    },
    "summary": "Play current synth"
  },
  "play_chord": {
    "accepts_block": false,
    "args": {
      "notes": ":list"
    },
    "introduced": "2,0,0",
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
    "signature": {
      "*args": null,
      "notes": null
    },
    "summary": "Play notes simultaneously"
  },
  "play_pattern": {
    "accepts_block": false,
    "args": {
      "notes": ":list"
    },
    "introduced": "2,0,0",
    "opts": {},
    "signature": {
      "*args": null,
      "notes": null
    },
    "summary": "Play pattern of notes"
  },
  "play_pattern_timed": {
    "accepts_block": false,
    "args": {
      "notes": ":list",
      "times": ":list_or_number"
    },
    "introduced": "2,0,0",
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
    "signature": {
      "*args": null,
      "notes": null,
      "times": null
    },
    "summary": "Play pattern of notes with specific times"
  },
  "ratio_to_pitch": {
    "accepts_block": false,
    "args": {
      "ratio": ":number"
    },
    "introduced": "2,7,0",
    "opts": null,
    "signature": {
      "r": null
    },
    "summary": "relative frequency ratio to MIDI pitch"
  },
  "recording_delete": {
    "accepts_block": false,
    "hide": true,
    "opts": null
  },
  "recording_save": {
    "accepts_block": false,
    "args": {
      "path": ":string"
    },
    "hide": true,
    "introduced": "2,0,0",
    "opts": null,
    "signature": {
      "filename": null
    },
    "summary": "Save recording"
  },
  "recording_start": {
    "accepts_block": false,
    "hide": true,
    "introduced": "2,0,0",
    "opts": null,
    "summary": "Start recording"
  },
  "recording_stop": {
    "accepts_block": false,
    "hide": true,
    "introduced": "2,0,0",
    "opts": null,
    "summary": "Stop recording"
  },
  "reset_mixer!": {
    "accepts_block": false,
    "introduced": "2,9,0",
    "opts": {},
    "signature": {
      "": null
    },
    "summary": "Reset master mixer"
  },
  "resolve_sample_path": {
    "signature": {
      "filts_and_sources": null
    }
  },
  "resolve_sample_paths": {
    "signature": {
      "filts_and_sources": null
    }
  },
  "rest?": {
    "accepts_block": false,
    "args": {
      "note_or_args": ":number_symbol_or_map"
    },
    "introduced": "2,1,0",
    "signature": {
      "n": null
    },
    "summary": "Determine if note or args is a rest"
  },
  "sample": {
    "accepts_block": true,
    "args": {
      "name_or_path": ":symbol_or_string"
    },
    "intro_fn": true,
    "introduced": "2,0,0",
    "opts": {
      "path": "/path/to/file"
    },
    "signature": {
      "&blk": null,
      "*args": null
    },
    "summary": "Trigger sample"
  },
  "sample_buffer": {
    "accepts_block": false,
    "args": {
      "path": ":string"
    },
    "introduced": "2,0,0",
    "opts": null,
    "signature": {
      "*args": null
    },
    "summary": "Get sample data"
  },
  "sample_duration": {
    "accepts_block": false,
    "args": {
      "path": ":string"
    },
    "introduced": "2,0,0",
    "opts": {
      "rpitch": 0
    },
    "signature": {
      "*args": null
    },
    "summary": "Get duration of sample in beats"
  },
  "sample_free": {
    "accepts_block": false,
    "args": {
      "path": ":string"
    },
    "introduced": "2,9,0",
    "opts": null,
    "returns": null,
    "signature": {
      "*paths": null
    },
    "summary": "Free a sample on the synth server"
  },
  "sample_free_all": {
    "accepts_block": false,
    "args": {},
    "introduced": "2,9,0",
    "opts": null,
    "returns": null,
    "summary": "Free all loaded samples on the synth server"
  },
  "sample_groups": {
    "accepts_block": false,
    "introduced": "2,0,0",
    "memoize": true,
    "opts": null,
    "summary": "Get all sample groups"
  },
  "sample_info": {
    "accepts_block": false,
    "args": {
      "path": ":string"
    },
    "introduced": "2,0,0",
    "opts": null,
    "signature": {
      "*args": null
    },
    "summary": "Get sample information"
  },
  "sample_loaded?": {
    "accepts_block": false,
    "args": {
      "path": ":string"
    },
    "introduced": "2,2,0",
    "opts": null,
    "signature": {
      "*args": null
    },
    "summary": "Test if sample was pre-loaded"
  },
  "sample_names": {
    "accepts_block": false,
    "args": {
      "group": ":symbol"
    },
    "introduced": "2,0,0",
    "memoize": true,
    "opts": null,
    "returns": ":ring",
    "signature": {
      "group": null
    },
    "summary": "Get sample names"
  },
  "sample_paths": {
    "accepts_block": false,
    "args": {
      "pre_args": ":source_and_filter_types"
    },
    "introduced": "2,10,0",
    "opts": null,
    "returns": ":ring",
    "signature": {
      "*args": null
    },
    "summary": "Sample Pack Filter Resolution"
  },
  "sample_split_filts_and_opts": {
    "signature": {
      "args": null
    }
  },
  "scale": {
    "accepts_block": false,
    "args": {
      "name": ":symbol",
      "tonic": ":symbol"
    },
    "intro_fn": true,
    "introduced": "2,0,0",
    "memoize": true,
    "opts": {
      "num_octaves": 1
    },
    "returns": ":ring",
    "signature": {
      "*opts": null,
      "tonic_or_name": null
    },
    "summary": "Create scale"
  },
  "scale_names": {
    "accepts_block": false,
    "introduced": "2,6,0",
    "memoize": true,
    "opts": null,
    "summary": "All scale names"
  },
  "set_cent_tuning!": {
    "accepts_block": false,
    "args": {
      "cent_shift": ":number"
    },
    "intro_fn": false,
    "introduced": "2,10,0",
    "opts": null,
    "signature": {
      "shift": null
    },
    "summary": "Global Cent tuning"
  },
  "set_control_delta!": {
    "accepts_block": false,
    "args": {
      "time": ":number"
    },
    "introduced": "2,1,0",
    "modifies_env": true,
    "opts": null,
    "signature": {
      "t": null
    },
    "summary": "Set control delta globally"
  },
  "set_mixer_control!": {
    "accepts_block": false,
    "introduced": "2,7,0",
    "opts": {
      "leak_dc_bypass": 0
    },
    "signature": {
      "opts": null
    },
    "summary": "Control master mixer"
  },
  "set_mixer_invert_stereo!": {},
  "set_mixer_mono_mode!": {},
  "set_mixer_standard_stereo!": {},
  "set_mixer_stereo_mode!": {},
  "set_sched_ahead_time!": {
    "accepts_block": false,
    "args": {
      "time": ":number"
    },
    "introduced": "2,0,0",
    "modifies_env": true,
    "opts": null,
    "signature": {
      "t": null
    },
    "summary": "Set sched ahead time globally"
  },
  "set_volume!": {
    "accepts_block": false,
    "args": {
      "vol": ":number"
    },
    "introduced": "2,0,0",
    "modifies_env": true,
    "opts": null,
    "signature": {
      "vol": null
    },
    "summary": "Set Volume globally"
  },
  "should_trigger?": {
    "signature": {
      "args_h": null
    }
  },
  "start_amp_monitor": {},
  "status": {
    "accepts_block": false,
    "introduced": "2,0,0",
    "opts": null,
    "summary": "Get server status"
  },
  "synth": {
    "accepts_block": true,
    "args": {
      "synth_name": ":symbol"
    },
    "introduced": "2,0,0",
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
    "signature": {
      "&blk": null,
      "*args": null,
      "synth_name": null
    },
    "summary": "Trigger specific synth"
  },
  "synth_names": {
    "accepts_block": false,
    "introduced": "2,9,0",
    "memoize": true,
    "opts": null,
    "summary": "Get all synth names"
  },
  "truthy?": {
    "signature": {
      "val": null
    }
  },
  "use_arg_bpm_scaling": {
    "accepts_block": false,
    "args": {
      "bool": ":boolean"
    },
    "introduced": "2,0,0",
    "opts": null,
    "signature": {
      "&block": null,
      "bool": null
    },
    "summary": "Enable and disable BPM scaling"
  },
  "use_arg_checks": {
    "accepts_block": false,
    "args": {
      "true_or_false": ":boolean"
    },
    "introduced": "2,0,0",
    "opts": null,
    "signature": {
      "&block": null,
      "v": null
    },
    "summary": "Enable and disable arg checks"
  },
  "use_cent_tuning": {
    "accepts_block": false,
    "args": {
      "cent_shift": ":number"
    },
    "intro_fn": true,
    "introduced": "2,9,0",
    "opts": null,
    "signature": {
      "&block": null,
      "shift": null
    },
    "summary": "Cent tuning"
  },
  "use_debug": {
    "accepts_block": false,
    "args": {
      "true_or_false": ":boolean"
    },
    "introduced": "2,0,0",
    "opts": null,
    "signature": {
      "&block": null,
      "v": null
    },
    "summary": "Enable and disable debug"
  },
  "use_external_synths": {
    "signature": {
      "&block": null,
      "v": null
    }
  },
  "use_fx": {
    "signature": {
      "&block": null,
      "*args": null
    }
  },
  "use_merged_sample_defaults": {
    "accepts_block": false,
    "introduced": "2,9,0",
    "opts": {},
    "signature": {
      "&block": null,
      "*args": null
    },
    "summary": "Merge new sample defaults"
  },
  "use_merged_synth_defaults": {
    "accepts_block": false,
    "introduced": "2,0,0",
    "opts": {},
    "signature": {
      "&block": null,
      "*args": null
    },
    "summary": "Merge synth defaults"
  },
  "use_octave": {
    "accepts_block": false,
    "args": {
      "octave_shift": ":number"
    },
    "intro_fn": true,
    "introduced": "2,9,0",
    "opts": null,
    "signature": {
      "&block": null,
      "shift": null
    },
    "summary": "Note octave transposition"
  },
  "use_sample_bpm": {
    "accepts_block": false,
    "args": {
      "string_or_number": ":sample_name_or_duration"
    },
    "introduced": "2,1,0",
    "opts": {
      "num_beats": 1
    },
    "signature": {
      "*args": null,
      "sample_name": null
    },
    "summary": "Sample-duration-based bpm modification"
  },
  "use_sample_defaults": {
    "accepts_block": false,
    "introduced": "2,5,0",
    "opts": {},
    "signature": {
      "&block": null,
      "*args": null
    },
    "summary": "Use new sample defaults"
  },
  "use_synth": {
    "accepts_block": false,
    "args": {
      "synth_name": ":symbol"
    },
    "intro_fn": true,
    "introduced": "2,0,0",
    "opts": null,
    "signature": {
      "&block": null,
      "*args": null,
      "synth_name": null
    },
    "summary": "Switch current synth"
  },
  "use_synth_defaults": {
    "accepts_block": false,
    "introduced": "2,0,0",
    "opts": {},
    "signature": {
      "&block": null,
      "*args": null
    },
    "summary": "Use new synth defaults"
  },
  "use_timing_guarantees": {
    "accepts_block": true,
    "args": {
      "bool": ":true_or_false"
    },
    "introduced": "2,10,0",
    "opts": null,
    "signature": {
      "&block": null,
      "v": null
    },
    "summary": "Inhibit synth triggers if too late"
  },
  "use_timing_warnings": {
    "signature": {
      "&block": null,
      "v": null
    }
  },
  "use_transpose": {
    "accepts_block": false,
    "args": {
      "note_shift": ":number"
    },
    "intro_fn": true,
    "introduced": "2,0,0",
    "opts": null,
    "signature": {
      "&block": null,
      "shift": null
    },
    "summary": "Note transposition"
  },
  "use_tuning": {
    "accepts_block": false,
    "args": {
      "fundamental_note": ":symbol_or_number",
      "tuning": ":symbol"
    },
    "introduced": "2,6,0",
    "opts": null,
    "signature": {
      "&block": null,
      "fundamental_note": ":c",
      "tuning": null
    },
    "summary": "Use alternative tuning systems"
  },
  "with_afx": {
    "signature": {
      "&block": null,
      "*args": null,
      "fx_name": null
    }
  },
  "with_arg_bpm_scaling": {
    "accepts_block": true,
    "introduced": "2,0,0",
    "opts": null,
    "requires_block": true,
    "signature": {
      "&block": null,
      "bool": null
    },
    "summary": "Block-level enable and disable BPM scaling"
  },
  "with_arg_checks": {
    "accepts_block": true,
    "args": {
      "true_or_false": ":boolean"
    },
    "introduced": "2,0,0",
    "opts": null,
    "requires_block": true,
    "signature": {
      "&block": null,
      "v": null
    },
    "summary": "Block-level enable and disable arg checks"
  },
  "with_cent_tuning": {
    "accepts_block": true,
    "args": {
      "cent_shift": ":number"
    },
    "introduced": "2,9,0",
    "opts": null,
    "requires_block": true,
    "signature": {
      "&block": null,
      "shift": null
    },
    "summary": "Block-level cent tuning"
  },
  "with_debug": {
    "accepts_block": true,
    "args": {
      "true_or_false": ":boolean"
    },
    "introduced": "2,0,0",
    "opts": null,
    "requires_block": true,
    "signature": {
      "&block": null,
      "v": null
    },
    "summary": "Block-level enable and disable debug"
  },
  "with_fx": {
    "accepts_block": true,
    "args": {
      "fx_name": ":symbol"
    },
    "intro_fn": true,
    "introduced": "2,0,0",
    "opts": {
      "kill_delay": 1
    },
    "requires_block": true,
    "signature": {
      "&block": null,
      "*args": null,
      "fx_name": null
    },
    "summary": "Use Studio FX"
  },
  "with_merged_sample_defaults": {
    "accepts_block": false,
    "introduced": "2,9,0",
    "opts": {},
    "requires_block": false,
    "signature": {
      "&block": null,
      "*args": null
    },
    "summary": "Block-level use merged sample defaults"
  },
  "with_merged_synth_defaults": {
    "accepts_block": true,
    "introduced": "2,0,0",
    "opts": {},
    "requires_block": true,
    "signature": {
      "&block": null,
      "*args": null
    },
    "summary": "Block-level merge synth defaults"
  },
  "with_octave": {
    "accepts_block": true,
    "args": {
      "octave_shift": ":number"
    },
    "intro_fn": true,
    "introduced": "2,9,0",
    "opts": null,
    "signature": {
      "&block": null,
      "shift": null
    },
    "summary": "Block level octave transposition"
  },
  "with_sample_bpm": {
    "accepts_block": true,
    "args": {
      "string_or_number": ":sample_name_or_duration"
    },
    "introduced": "2,1,0",
    "opts": {
      "num_beats": 1
    },
    "requires_block": true,
    "signature": {
      "&block": null,
      "*args": null,
      "sample_name": null
    },
    "summary": "Block-scoped sample-duration-based bpm modification"
  },
  "with_sample_defaults": {
    "accepts_block": false,
    "introduced": "2,5,0",
    "opts": {},
    "requires_block": false,
    "signature": {
      "&block": null,
      "*args": null
    },
    "summary": "Block-level use new sample defaults"
  },
  "with_synth": {
    "accepts_block": true,
    "args": {
      "synth_name": ":symbol"
    },
    "introduced": "2,0,0",
    "opts": null,
    "requires_block": true,
    "signature": {
      "&block": null,
      "*args": null,
      "synth_name": null
    },
    "summary": "Block-level synth switching"
  },
  "with_synth_defaults": {
    "accepts_block": true,
    "introduced": "2,0,0",
    "opts": {},
    "requires_block": true,
    "signature": {
      "&block": null,
      "*args": null
    },
    "summary": "Block-level use new synth defaults"
  },
  "with_timing_guarantees": {
    "accepts_block": true,
    "args": {
      "bool": ":true_or_false"
    },
    "introduced": "2,10,0",
    "opts": null,
    "signature": {
      "&block": null,
      "v": null
    },
    "summary": "Block-scoped inhibition of synth triggers if too late"
  },
  "with_timing_warnings": {
    "signature": {
      "&block": null,
      "v": null
    }
  },
  "with_transpose": {
    "accepts_block": true,
    "args": {
      "note_shift": ":number"
    },
    "introduced": "2,0,0",
    "opts": null,
    "requires_block": true,
    "signature": {
      "&block": null,
      "shift": null
    },
    "summary": "Block-level note transposition"
  },
  "with_tuning": {
    "accepts_block": true,
    "args": {
      "fundamental_note": ":symbol_or_number",
      "tuning": ":symbol"
    },
    "introduced": "2,6,0",
    "opts": null,
    "signature": {
      "&block": null,
      "fundamental_note": ":c",
      "tuning": null
    },
    "summary": "Block-level tuning modification"
  }
}

sound_args_types_conversion = {}

sound_opts_types_conversion = {}

#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/

synths = {
  "BNoise": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "attack:": 0,
      "attack_level:": 1,
      "cutoff:": 110,
      "cutoff_slide:": 0,
      "cutoff_slide_curve:": 0,
      "cutoff_slide_shape:": 1,
      "decay:": 0,
      "decay_level:": 1,
      "env_curve:": 2,
      "pan:": 0,
      "pan_slide:": 0,
      "pan_slide_curve:": 0,
      "pan_slide_shape:": 1,
      "release:": 1,
      "res:": 0,
      "res_slide:": 0,
      "res_slide_curve:": 0,
      "res_slide_shape:": 1,
      "sustain:": 0,
      "sustain_level:": 1
    },
    "descr": "Brown Noise",
    "hiden": true,
    "inherit_arg": true,
    "inherit_base": "Noise",
    "name": ":bnoise"
  },
  "BaseMixer": {
    "arg_defaults": {},
    "hiden": true,
    "inherit_arg": true,
    "inherit_base": "StudioInfo"
  },
  "BasicMixer": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0.1,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1
    },
    "descr": "Basic Mixer",
    "hiden": true,
    "inherit_arg": false,
    "inherit_base": "BaseMixer",
    "name": ":basic_mixer"
  },
  "BasicMonoPlayer": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "hpf:": -1,
      "hpf_slide:": 0,
      "hpf_slide_curve:": 0,
      "hpf_slide_shape:": 1,
      "lpf:": -1,
      "lpf_slide:": 0,
      "lpf_slide_curve:": 0,
      "lpf_slide_shape:": 1,
      "pan:": 0,
      "pan_slide:": 0,
      "pan_slide_curve:": 0,
      "pan_slide_shape:": 1,
      "rate:": 1
    },
    "descr": "Basic Mono Sample Player (no env)",
    "hiden": true,
    "inherit_arg": false,
    "inherit_base": "StudioInfo",
    "name": ":basic_mono_player"
  },
  "BasicStereoPlayer": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "hpf:": -1,
      "hpf_slide:": 0,
      "hpf_slide_curve:": 0,
      "hpf_slide_shape:": 1,
      "lpf:": -1,
      "lpf_slide:": 0,
      "lpf_slide_curve:": 0,
      "lpf_slide_shape:": 1,
      "pan:": 0,
      "pan_slide:": 0,
      "pan_slide_curve:": 0,
      "pan_slide_shape:": 1,
      "rate:": 1
    },
    "descr": "Basic Stereo Sample Player (no env)",
    "hiden": true,
    "inherit_arg": true,
    "inherit_base": "BasicMonoPlayer",
    "name": ":basic_stereo_player"
  },
  "Beep": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "attack:": 0,
      "attack_level:": 1,
      "decay:": 0,
      "decay_level:": 1,
      "env_curve:": 2,
      "note:": 52,
      "note_slide:": 0,
      "note_slide_curve:": 0,
      "note_slide_shape:": 1,
      "pan:": 0,
      "pan_slide:": 0,
      "pan_slide_curve:": 0,
      "pan_slide_shape:": 1,
      "release:": 1,
      "sustain:": 0,
      "sustain_level:": 1
    },
    "descr": "Sine Wave",
    "hiden": false,
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "name": ":beep"
  },
  "CNoise": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "attack:": 0,
      "attack_level:": 1,
      "cutoff:": 110,
      "cutoff_slide:": 0,
      "cutoff_slide_curve:": 0,
      "cutoff_slide_shape:": 1,
      "decay:": 0,
      "decay_level:": 1,
      "env_curve:": 2,
      "pan:": 0,
      "pan_slide:": 0,
      "pan_slide_curve:": 0,
      "pan_slide_shape:": 1,
      "release:": 1,
      "res:": 0,
      "res_slide:": 0,
      "res_slide_curve:": 0,
      "res_slide_shape:": 1,
      "sustain:": 0,
      "sustain_level:": 1
    },
    "descr": "Clip Noise",
    "hiden": true,
    "inherit_arg": true,
    "inherit_base": "Noise",
    "name": ":cnoise"
  },
  "ChipBass": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "attack:": 0,
      "attack_level:": 1,
      "decay:": 0,
      "decay_level:": 1,
      "env_curve:": 2,
      "note:": 60,
      "note_resolution:": 0.1,
      "note_slide:": 0,
      "note_slide_curve:": 0,
      "note_slide_shape:": 1,
      "pan:": 0,
      "pan_slide:": 0,
      "pan_slide_curve:": 0,
      "pan_slide_shape:": 1,
      "release:": 1,
      "sustain:": 0,
      "sustain_level:": 1
    },
    "descr": "Chip Bass",
    "hiden": false,
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "name": ":chipbass"
  },
  "ChipLead": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "attack:": 0,
      "attack_level:": 1,
      "decay:": 0,
      "decay_level:": 1,
      "env_curve:": 2,
      "note:": 60,
      "note_resolution:": 0.1,
      "note_slide:": 0,
      "note_slide_curve:": 0,
      "note_slide_shape:": 1,
      "pan:": 0,
      "pan_slide:": 0,
      "pan_slide_curve:": 0,
      "pan_slide_shape:": 1,
      "release:": 1,
      "sustain:": 0,
      "sustain_level:": 1,
      "width:": 0
    },
    "descr": "Chip Lead",
    "hiden": false,
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "name": ":chiplead"
  },
  "ChipNoise": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 1,
      "amp_slide_shape:": 0,
      "attack:": 0,
      "attack_level:": 1,
      "decay:": 0,
      "decay_level:": 1,
      "env_curve:": 0,
      "freq_band:": 0,
      "freq_band_slide:": 0,
      "freq_band_slide_curve:": 0,
      "freq_band_slide_shape:": 1,
      "pan:": 0,
      "pan_slide:": 0,
      "pan_slide_curve:": 0,
      "pan_slide_shape:": 1,
      "release:": 0,
      "sustain:": 1,
      "sustain_level:": 1
    },
    "descr": "Chip Noise",
    "hiden": true,
    "inherit_arg": false,
    "inherit_base": "Noise",
    "name": ":chipnoise"
  },
  "DPulse": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "attack:": 0,
      "attack_level:": 1,
      "cutoff:": 100,
      "cutoff_slide:": 0,
      "cutoff_slide_curve:": 0,
      "cutoff_slide_shape:": 1,
      "decay:": 0,
      "decay_level:": 1,
      "detune:": 0.1,
      "detune_slide:": 0,
      "detune_slide_curve:": 0,
      "detune_slide_shape:": 1,
      "dpulse_width:": 0.5,
      "dpulse_width_slide:": 0,
      "dpulse_width_slide_shape:": 1,
      "env_curve:": 2,
      "note:": 52,
      "note_slide:": 0,
      "note_slide_curve:": 0,
      "note_slide_shape:": 1,
      "pan:": 0,
      "pan_slide:": 0,
      "pan_slide_curve:": 0,
      "pan_slide_shape:": 1,
      "pulse_width:": 0.5,
      "pulse_width_slide:": 0,
      "pulse_width_slide_curve:": 0,
      "pulse_width_slide_shape:": 1,
      "release:": 1,
      "sustain:": 0,
      "sustain_level:": 1
    },
    "descr": "Detuned Pulse Wave",
    "hiden": true,
    "inherit_arg": true,
    "inherit_base": "DSaw",
    "name": ":dpulse"
  },
  "DSaw": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "attack:": 0,
      "attack_level:": 1,
      "cutoff:": 100,
      "cutoff_slide:": 0,
      "cutoff_slide_curve:": 0,
      "cutoff_slide_shape:": 1,
      "decay:": 0,
      "decay_level:": 1,
      "detune:": 0.1,
      "detune_slide:": 0,
      "detune_slide_curve:": 0,
      "detune_slide_shape:": 1,
      "env_curve:": 2,
      "note:": 52,
      "note_slide:": 0,
      "note_slide_curve:": 0,
      "note_slide_shape:": 1,
      "pan:": 0,
      "pan_slide:": 0,
      "pan_slide_curve:": 0,
      "pan_slide_shape:": 1,
      "release:": 1,
      "sustain:": 0,
      "sustain_level:": 1
    },
    "descr": "Detuned Saw wave",
    "hiden": false,
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "name": ":dsaw"
  },
  "DTri": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "attack:": 0,
      "attack_level:": 1,
      "cutoff:": 100,
      "cutoff_slide:": 0,
      "cutoff_slide_curve:": 0,
      "cutoff_slide_shape:": 1,
      "decay:": 0,
      "decay_level:": 1,
      "detune:": 0.1,
      "detune_slide:": 0,
      "detune_slide_curve:": 0,
      "detune_slide_shape:": 1,
      "env_curve:": 2,
      "note:": 52,
      "note_slide:": 0,
      "note_slide_curve:": 0,
      "note_slide_shape:": 1,
      "pan:": 0,
      "pan_slide:": 0,
      "pan_slide_curve:": 0,
      "pan_slide_shape:": 1,
      "release:": 1,
      "sustain:": 0,
      "sustain_level:": 1
    },
    "descr": "Detuned Triangle Wave",
    "hiden": true,
    "inherit_arg": true,
    "inherit_base": "DSaw",
    "name": ":dtri"
  },
  "DarkAmbience": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "attack:": 0,
      "attack_level:": 1,
      "cutoff:": 110,
      "cutoff_slide:": 0,
      "cutoff_slide_curve:": 0,
      "cutoff_slide_shape:": 1,
      "decay:": 0,
      "decay_level:": 1,
      "detune1:": 12,
      "detune1_slide:": 0,
      "detune1_slide_curve:": 0,
      "detune1_slide_shape:": 1,
      "detune2:": 24,
      "detune2_slide:": 0,
      "detune2_slide_curve:": 0,
      "detune2_slide_shape:": 1,
      "env_curve:": 2,
      "noise:": 0,
      "note:": 52,
      "note_slide:": 0,
      "note_slide_curve:": 0,
      "note_slide_shape:": 1,
      "pan:": 0,
      "pan_slide:": 0,
      "pan_slide_curve:": 0,
      "pan_slide_shape:": 1,
      "release:": 1,
      "res:": 0.7,
      "res_slide:": 0,
      "res_slide_curve:": 0,
      "res_slide_shape:": 1,
      "reverb_time:": 100,
      "ring:": 0.2,
      "room:": 70,
      "sustain:": 0,
      "sustain_level:": 1
    },
    "descr": "Dark Ambience",
    "hiden": false,
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "name": ":dark_ambience"
  },
  "DarkSeaHorn": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "attack:": 1,
      "attack_level:": 1,
      "decay:": 0,
      "decay_level:": 1,
      "env_curve:": 2,
      "note:": 52,
      "note_slide:": 0,
      "note_slide_curve:": 0,
      "note_slide_shape:": 1,
      "pan:": 0,
      "pan_slide:": 0,
      "pan_slide_curve:": 0,
      "pan_slide_shape:": 1,
      "release:": 4.0,
      "sustain:": 0,
      "sustain_level:": 1
    },
    "descr": "Dark Sea Horn",
    "hiden": true,
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "name": ":dark_sea_horn"
  },
  "DullBell": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "attack:": 0,
      "attack_level:": 1,
      "decay:": 0,
      "decay_level:": 1,
      "env_curve:": 2,
      "note:": 52,
      "note_slide:": 0,
      "note_slide_curve:": 0,
      "note_slide_shape:": 1,
      "pan:": 0,
      "pan_slide:": 0,
      "pan_slide_curve:": 0,
      "pan_slide_shape:": 1,
      "release:": 1,
      "sustain:": 0,
      "sustain_level:": 1
    },
    "descr": "Dull Bell",
    "hiden": false,
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "name": ":dull_bell"
  },
  "FM": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "attack:": 0,
      "attack_level:": 1,
      "cutoff:": 100,
      "cutoff_slide:": 0,
      "cutoff_slide_curve:": 0,
      "cutoff_slide_shape:": 1,
      "decay:": 0,
      "decay_level:": 1,
      "depth:": 1,
      "depth_slide:": 0,
      "depth_slide_curve:": 0,
      "depth_slide_shape:": 1,
      "divisor:": 2,
      "divisor_slide:": 0,
      "divisor_slide_curve:": 0,
      "divisor_slide_shape:": 1,
      "env_curve:": 2,
      "note:": 52,
      "note_slide:": 0,
      "note_slide_curve:": 0,
      "note_slide_shape:": 1,
      "pan:": 0,
      "pan_slide:": 0,
      "pan_slide_curve:": 0,
      "pan_slide_shape:": 1,
      "release:": 1,
      "sustain:": 0,
      "sustain_level:": 1
    },
    "descr": "Basic FM synthesis",
    "hiden": false,
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "name": ":fm"
  },
  "GNoise": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "attack:": 0,
      "attack_level:": 1,
      "cutoff:": 110,
      "cutoff_slide:": 0,
      "cutoff_slide_curve:": 0,
      "cutoff_slide_shape:": 1,
      "decay:": 0,
      "decay_level:": 1,
      "env_curve:": 2,
      "pan:": 0,
      "pan_slide:": 0,
      "pan_slide_curve:": 0,
      "pan_slide_shape:": 1,
      "release:": 1,
      "res:": 0,
      "res_slide:": 0,
      "res_slide_curve:": 0,
      "res_slide_shape:": 1,
      "sustain:": 0,
      "sustain_level:": 1
    },
    "descr": "Grey Noise",
    "hiden": true,
    "inherit_arg": true,
    "inherit_base": "Noise",
    "name": ":gnoise"
  },
  "Growl": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "attack:": 0.1,
      "attack_level:": 1,
      "cutoff:": 130,
      "cutoff_slide:": 0,
      "cutoff_slide_curve:": 0,
      "cutoff_slide_shape:": 1,
      "decay:": 0,
      "decay_level:": 1,
      "env_curve:": 2,
      "note:": 52,
      "note_slide:": 0,
      "note_slide_curve:": 0,
      "note_slide_shape:": 1,
      "pan:": 0,
      "pan_slide:": 0,
      "pan_slide_curve:": 0,
      "pan_slide_shape:": 1,
      "release:": 1,
      "res:": 0.7,
      "res_slide:": 0,
      "res_slide_curve:": 0,
      "res_slide_shape:": 1,
      "sustain:": 0,
      "sustain_level:": 1
    },
    "descr": "Growl",
    "hiden": false,
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "name": ":growl"
  },
  "Hollow": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "attack:": 0,
      "attack_level:": 1,
      "cutoff:": 90,
      "cutoff_slide:": 0,
      "cutoff_slide_curve:": 0,
      "cutoff_slide_shape:": 1,
      "decay:": 0,
      "decay_level:": 1,
      "env_curve:": 2,
      "noise:": 1,
      "norm:": 0,
      "note:": 52,
      "note_slide:": 0,
      "note_slide_curve:": 0,
      "note_slide_shape:": 1,
      "pan:": 0,
      "pan_slide:": 0,
      "pan_slide_curve:": 0,
      "pan_slide_shape:": 1,
      "release:": 1,
      "res:": 0.99,
      "res_slide:": 0,
      "res_slide_curve:": 0,
      "res_slide_shape:": 1,
      "sustain:": 0,
      "sustain_level:": 1
    },
    "descr": "Hollow",
    "hiden": false,
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "name": ":hollow"
  },
  "Hoover": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "attack:": 0.05,
      "attack_level:": 1,
      "cutoff:": 130,
      "cutoff_slide:": 0,
      "cutoff_slide_curve:": 0,
      "cutoff_slide_shape:": 1,
      "decay:": 0,
      "decay_level:": 1,
      "env_curve:": 2,
      "note:": 52,
      "note_slide:": 0,
      "note_slide_curve:": 0,
      "note_slide_shape:": 1,
      "pan:": 0,
      "pan_slide:": 0,
      "pan_slide_curve:": 0,
      "pan_slide_shape:": 1,
      "release:": 1,
      "res:": 0.1,
      "res_slide:": 0,
      "res_slide_curve:": 0,
      "res_slide_shape:": 1,
      "sustain:": 0,
      "sustain_level:": 1
    },
    "descr": "Hoover",
    "hiden": false,
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "name": ":hoover"
  },
  "MainMixer": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0.02,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "force_mono:": 0,
      "hpf:": 0,
      "hpf_bypass:": 0,
      "hpf_slide:": 0.02,
      "hpf_slide_curve:": 0,
      "hpf_slide_shape:": 1,
      "invert_stereo:": 0,
      "limiter_bypass:": 0,
      "lpf:": 135.5,
      "lpf_bypass:": 0,
      "lpf_slide:": 0.02,
      "lpf_slide_curve:": 0,
      "lpf_slide_shape:": 1,
      "pre_amp:": 1,
      "pre_amp_slide:": 0.02,
      "pre_amp_slide_curve:": 0,
      "pre_amp_slide_shape:": 1
    },
    "descr": "Main Mixer",
    "hiden": true,
    "inherit_arg": false,
    "inherit_base": "BaseMixer",
    "name": ":mixer"
  },
  "ModDSaw": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "attack:": 0,
      "attack_level:": 1,
      "cutoff:": 100,
      "cutoff_slide:": 0,
      "cutoff_slide_curve:": 0,
      "cutoff_slide_shape:": 1,
      "decay:": 0,
      "decay_level:": 1,
      "detune:": 0.1,
      "detune_slide:": 0,
      "detune_slide_curve:": 0,
      "detune_slide_shape:": 1,
      "env_curve:": 2,
      "mod_invert_wave:": 0,
      "mod_phase:": 0.25,
      "mod_phase_offset:": 0,
      "mod_phase_slide:": 0,
      "mod_phase_slide_curve:": 0,
      "mod_phase_slide_shape:": 1,
      "mod_pulse_width:": 0.5,
      "mod_pulse_width_slide:": 0,
      "mod_pulse_width_slide_curve:": 0,
      "mod_pulse_width_slide_shape:": 1,
      "mod_range:": 5,
      "mod_range_slide:": 0,
      "mod_range_slide_curve:": 0,
      "mod_range_slide_shape:": 1,
      "mod_wave:": 1,
      "note:": 52,
      "note_slide:": 0,
      "note_slide_curve:": 0,
      "note_slide_shape:": 1,
      "pan:": 0,
      "pan_slide:": 0,
      "pan_slide_curve:": 0,
      "pan_slide_shape:": 1,
      "release:": 1,
      "sustain:": 0,
      "sustain_level:": 1
    },
    "descr": "Modulated Detuned Saw Waves",
    "hiden": false,
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "name": ":mod_dsaw"
  },
  "ModFM": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "attack:": 0,
      "attack_level:": 1,
      "cutoff:": 100,
      "cutoff_slide:": 0,
      "cutoff_slide_curve:": 0,
      "cutoff_slide_shape:": 1,
      "decay:": 0,
      "decay_level:": 1,
      "depth:": 1,
      "depth_slide:": 0,
      "depth_slide_curve:": 0,
      "depth_slide_shape:": 1,
      "divisor:": 2,
      "divisor_slide:": 0,
      "divisor_slide_curve:": 0,
      "divisor_slide_shape:": 1,
      "env_curve:": 2,
      "mod_invert_wave:": 0,
      "mod_phase:": 0.25,
      "mod_phase_offset:": 0,
      "mod_pulse_width:": 0.5,
      "mod_range:": 5,
      "mod_wave:": 1,
      "note:": 52,
      "note_slide:": 0,
      "note_slide_curve:": 0,
      "note_slide_shape:": 1,
      "pan:": 0,
      "pan_slide:": 0,
      "pan_slide_curve:": 0,
      "pan_slide_shape:": 1,
      "release:": 1,
      "sustain:": 0,
      "sustain_level:": 1
    },
    "descr": "Basic FM synthesis with frequency modulation.",
    "hiden": true,
    "inherit_arg": true,
    "inherit_base": "FM",
    "name": ":mod_fm"
  },
  "ModPulse": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "attack:": 0,
      "attack_level:": 1,
      "cutoff:": 100,
      "cutoff_slide:": 0,
      "cutoff_slide_curve:": 0,
      "cutoff_slide_shape:": 1,
      "decay:": 0,
      "decay_level:": 1,
      "env_curve:": 2,
      "mod_invert_wave:": 0,
      "mod_phase:": 0.25,
      "mod_phase_offset:": 0,
      "mod_phase_slide:": 0,
      "mod_phase_slide_curve:": 0,
      "mod_phase_slide_shape:": 1,
      "mod_pulse_width:": 0.5,
      "mod_pulse_width_slide:": 0,
      "mod_pulse_width_slide_curve:": 0,
      "mod_pulse_width_slide_shape:": 1,
      "mod_range:": 5,
      "mod_range_slide:": 0,
      "mod_range_slide_curve:": 0,
      "mod_range_slide_shape:": 1,
      "mod_wave:": 1,
      "note:": 52,
      "note_slide:": 0,
      "note_slide_curve:": 0,
      "note_slide_shape:": 1,
      "pan:": 0,
      "pan_slide:": 0,
      "pan_slide_curve:": 0,
      "pan_slide_shape:": 1,
      "pulse_width:": 0.5,
      "pulse_width_slide:": 0,
      "pulse_width_slide_curve:": 0,
      "pulse_width_slide_shape:": 1,
      "release:": 1,
      "sustain:": 0,
      "sustain_level:": 1
    },
    "descr": "Modulated Pulse",
    "hiden": false,
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "name": ":mod_pulse"
  },
  "ModSaw": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "attack:": 0,
      "attack_level:": 1,
      "cutoff:": 100,
      "cutoff_slide:": 0,
      "cutoff_slide_curve:": 0,
      "cutoff_slide_shape:": 1,
      "decay:": 0,
      "decay_level:": 1,
      "env_curve:": 2,
      "mod_invert_wave:": 0,
      "mod_phase:": 0.25,
      "mod_phase_offset:": 0,
      "mod_phase_slide:": 0,
      "mod_phase_slide_curve:": 0,
      "mod_phase_slide_shape:": 1,
      "mod_pulse_width:": 0.5,
      "mod_pulse_width_slide:": 0,
      "mod_pulse_width_slide_curve:": 0,
      "mod_pulse_width_slide_shape:": 1,
      "mod_range:": 5,
      "mod_range_slide:": 0,
      "mod_range_slide_curve:": 0,
      "mod_range_slide_shape:": 1,
      "mod_wave:": 1,
      "note:": 52,
      "note_slide:": 0,
      "note_slide_curve:": 0,
      "note_slide_shape:": 1,
      "pan:": 0,
      "pan_slide:": 0,
      "pan_slide_curve:": 0,
      "pan_slide_shape:": 1,
      "release:": 1,
      "sustain:": 0,
      "sustain_level:": 1
    },
    "descr": "Modulated Saw Wave",
    "hiden": false,
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "name": ":mod_saw"
  },
  "ModSine": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "attack:": 0,
      "attack_level:": 1,
      "cutoff:": 100,
      "cutoff_slide:": 0,
      "cutoff_slide_curve:": 0,
      "cutoff_slide_shape:": 1,
      "decay:": 0,
      "decay_level:": 1,
      "env_curve:": 2,
      "mod_invert_wave:": 0,
      "mod_phase:": 0.25,
      "mod_phase_offset:": 0,
      "mod_phase_slide:": 0,
      "mod_phase_slide_curve:": 0,
      "mod_phase_slide_shape:": 1,
      "mod_pulse_width:": 0.5,
      "mod_pulse_width_slide:": 0,
      "mod_pulse_width_slide_curve:": 0,
      "mod_pulse_width_slide_shape:": 1,
      "mod_range:": 5,
      "mod_range_slide:": 0,
      "mod_range_slide_curve:": 0,
      "mod_range_slide_shape:": 1,
      "mod_wave:": 1,
      "note:": 52,
      "note_slide:": 0,
      "note_slide_curve:": 0,
      "note_slide_shape:": 1,
      "pan:": 0,
      "pan_slide:": 0,
      "pan_slide_curve:": 0,
      "pan_slide_shape:": 1,
      "release:": 1,
      "sustain:": 0,
      "sustain_level:": 1
    },
    "descr": "Modulated Sine Wave",
    "hiden": false,
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "name": ":mod_sine"
  },
  "ModTri": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "attack:": 0,
      "attack_level:": 1,
      "cutoff:": 100,
      "cutoff_slide:": 0,
      "cutoff_slide_curve:": 0,
      "cutoff_slide_shape:": 1,
      "decay:": 0,
      "decay_level:": 1,
      "env_curve:": 2,
      "mod_invert_wave:": 0,
      "mod_phase:": 0.25,
      "mod_phase_offset:": 0,
      "mod_phase_slide:": 0,
      "mod_phase_slide_curve:": 0,
      "mod_phase_slide_shape:": 1,
      "mod_pulse_width:": 0.5,
      "mod_pulse_width_slide:": 0,
      "mod_pulse_width_slide_curve:": 0,
      "mod_pulse_width_slide_shape:": 1,
      "mod_range:": 5,
      "mod_range_slide:": 0,
      "mod_range_slide_curve:": 0,
      "mod_range_slide_shape:": 1,
      "mod_wave:": 1,
      "note:": 52,
      "note_slide:": 0,
      "note_slide_curve:": 0,
      "note_slide_shape:": 1,
      "pan:": 0,
      "pan_slide:": 0,
      "pan_slide_curve:": 0,
      "pan_slide_shape:": 1,
      "release:": 1,
      "sustain:": 0,
      "sustain_level:": 1
    },
    "descr": "Modulated Triangle Wave",
    "hiden": false,
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "name": ":mod_tri"
  },
  "MonoPlayer": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "attack:": 0,
      "attack_level:": 1,
      "clamp_time:": 0.01,
      "clamp_time_slide:": 0,
      "clamp_time_slide_curve:": 0,
      "clamp_time_slide_shape:": 1,
      "compress:": 0,
      "decay:": 0,
      "decay_level:": 1,
      "env_curve:": 2,
      "finish:": 1,
      "hpf:": -1,
      "hpf_attack:": 0,
      "hpf_attack_level:": -1,
      "hpf_decay:": 0,
      "hpf_decay_level:": -1,
      "hpf_env_curve:": 2,
      "hpf_init_level:": -1,
      "hpf_max:": -1,
      "hpf_max_slide:": 0,
      "hpf_max_slide_curve:": 0,
      "hpf_max_slide_shape:": 1,
      "hpf_release:": 0,
      "hpf_release_level:": -1,
      "hpf_slide:": 0,
      "hpf_slide_curve:": 0,
      "hpf_slide_shape:": 1,
      "hpf_sustain:": -1,
      "hpf_sustain_level:": -1,
      "lpf:": -1,
      "lpf_attack:": 0,
      "lpf_attack_level:": -1,
      "lpf_decay:": 0,
      "lpf_decay_level:": -1,
      "lpf_env_curve:": 2,
      "lpf_init_level:": -1,
      "lpf_min:": -1,
      "lpf_min_slide:": 0,
      "lpf_min_slide_curve:": 0,
      "lpf_min_slide_shape:": 1,
      "lpf_release:": 0,
      "lpf_release_level:": -1,
      "lpf_slide:": 0,
      "lpf_slide_curve:": 0,
      "lpf_slide_shape:": 1,
      "lpf_sustain:": -1,
      "lpf_sustain_level:": -1,
      "norm:": 0,
      "pan:": 0,
      "pan_slide:": 0,
      "pan_slide_curve:": 0,
      "pan_slide_shape:": 1,
      "pitch:": 0,
      "pitch_dis:": 0.0,
      "pitch_dis_slide:": 0,
      "pitch_dis_slide_curve:": 0,
      "pitch_dis_slide_shape:": 1,
      "pitch_slide:": 0,
      "pitch_slide_curve:": 0,
      "pitch_slide_shape:": 1,
      "pre_amp:": 1,
      "pre_amp_slide:": 0,
      "pre_amp_slide_curve:": 0,
      "pre_amp_slide_shape:": 1,
      "rate:": 1,
      "relax_time:": 0.01,
      "relax_time_slide:": 0,
      "relax_time_slide_curve:": 0,
      "relax_time_slide_shape:": 1,
      "release:": 0,
      "slope_above:": 0.5,
      "slope_above_slide:": 0,
      "slope_above_slide_curve:": 0,
      "slope_above_slide_shape:": 1,
      "slope_below:": 1,
      "slope_below_slide:": 0,
      "slope_below_slide_curve:": 0,
      "slope_below_slide_shape:": 1,
      "start:": 0,
      "sustain:": -1,
      "sustain_level:": 1,
      "threshold:": 0.2,
      "threshold_slide:": 0,
      "threshold_slide_curve:": 0,
      "threshold_slide_shape:": 1,
      "time_dis:": 0.0,
      "time_dis_slide:": 0,
      "time_dis_slide_curve:": 0,
      "time_dis_slide_shape:": 1,
      "window_size:": 0.2,
      "window_size_slide:": 0,
      "window_size_slide_curve:": 0,
      "window_size_slide_shape:": 1
    },
    "descr": "Mono Sample Player",
    "hiden": true,
    "inherit_arg": false,
    "inherit_base": "BasicMonoPlayer",
    "name": ":mono_player"
  },
  "Noise": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "attack:": 0,
      "attack_level:": 1,
      "cutoff:": 110,
      "cutoff_slide:": 0,
      "cutoff_slide_curve:": 0,
      "cutoff_slide_shape:": 1,
      "decay:": 0,
      "decay_level:": 1,
      "env_curve:": 2,
      "pan:": 0,
      "pan_slide:": 0,
      "pan_slide_curve:": 0,
      "pan_slide_shape:": 1,
      "release:": 1,
      "res:": 0,
      "res_slide:": 0,
      "res_slide_curve:": 0,
      "res_slide_shape:": 1,
      "sustain:": 0,
      "sustain_level:": 1
    },
    "descr": "Noise",
    "hiden": false,
    "inherit_arg": false,
    "inherit_base": "Pitchless",
    "name": ":noise"
  },
  "PNoise": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "attack:": 0,
      "attack_level:": 1,
      "cutoff:": 110,
      "cutoff_slide:": 0,
      "cutoff_slide_curve:": 0,
      "cutoff_slide_shape:": 1,
      "decay:": 0,
      "decay_level:": 1,
      "env_curve:": 2,
      "pan:": 0,
      "pan_slide:": 0,
      "pan_slide_curve:": 0,
      "pan_slide_shape:": 1,
      "release:": 1,
      "res:": 0,
      "res_slide:": 0,
      "res_slide_curve:": 0,
      "res_slide_shape:": 1,
      "sustain:": 0,
      "sustain_level:": 1
    },
    "descr": "Pink Noise",
    "hiden": true,
    "inherit_arg": true,
    "inherit_base": "Noise",
    "name": ":pnoise"
  },
  "Pitchless": {
    "arg_defaults": {},
    "hiden": true,
    "inherit_arg": true,
    "inherit_base": "SonicPiSynth"
  },
  "PrettyBell": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "attack:": 0,
      "attack_level:": 1,
      "decay:": 0,
      "decay_level:": 1,
      "env_curve:": 2,
      "note:": 52,
      "note_slide:": 0,
      "note_slide_curve:": 0,
      "note_slide_shape:": 1,
      "pan:": 0,
      "pan_slide:": 0,
      "pan_slide_curve:": 0,
      "pan_slide_shape:": 1,
      "release:": 1,
      "sustain:": 0,
      "sustain_level:": 1
    },
    "descr": "Pretty Bell",
    "hiden": true,
    "inherit_arg": true,
    "inherit_base": "DullBell",
    "name": ":pretty_bell"
  },
  "Prophet": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "attack:": 0,
      "attack_level:": 1,
      "cutoff:": 110,
      "cutoff_slide:": 0,
      "cutoff_slide_curve:": 0,
      "cutoff_slide_shape:": 1,
      "decay:": 0,
      "decay_level:": 1,
      "env_curve:": 2,
      "note:": 52,
      "note_slide:": 0,
      "note_slide_curve:": 0,
      "note_slide_shape:": 1,
      "pan:": 0,
      "pan_slide:": 0,
      "pan_slide_curve:": 0,
      "pan_slide_shape:": 1,
      "release:": 1,
      "res:": 0.7,
      "res_slide:": 0,
      "res_slide_curve:": 0,
      "res_slide_shape:": 1,
      "sustain:": 0,
      "sustain_level:": 1
    },
    "descr": "The Prophet",
    "hiden": false,
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "name": ":prophet"
  },
  "Pulse": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "attack:": 0,
      "attack_level:": 1,
      "cutoff:": 100,
      "cutoff_slide:": 0,
      "cutoff_slide_curve:": 0,
      "cutoff_slide_shape:": 1,
      "decay:": 0,
      "decay_level:": 1,
      "env_curve:": 2,
      "note:": 52,
      "note_slide:": 0,
      "note_slide_curve:": 0,
      "note_slide_shape:": 1,
      "pan:": 0,
      "pan_slide:": 0,
      "pan_slide_curve:": 0,
      "pan_slide_shape:": 1,
      "pulse_width:": 0.5,
      "pulse_width_slide:": 0,
      "pulse_width_slide_shape:": 1,
      "release:": 1,
      "sustain:": 0,
      "sustain_level:": 1
    },
    "descr": "Pulse Wave",
    "hiden": true,
    "inherit_arg": true,
    "inherit_base": "Square",
    "name": ":pulse"
  },
  "Saw": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "attack:": 0,
      "attack_level:": 1,
      "decay:": 0,
      "decay_level:": 1,
      "env_curve:": 2,
      "note:": 52,
      "note_slide:": 0,
      "note_slide_curve:": 0,
      "note_slide_shape:": 1,
      "pan:": 0,
      "pan_slide:": 0,
      "pan_slide_curve:": 0,
      "pan_slide_shape:": 1,
      "release:": 1,
      "sustain:": 0,
      "sustain_level:": 1
    },
    "descr": "Saw Wave",
    "hiden": true,
    "inherit_arg": true,
    "inherit_base": "Beep",
    "name": ":saw"
  },
  "Singer": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "attack:": 1,
      "attack_level:": 1,
      "decay:": 0,
      "decay_level:": 1,
      "env_curve:": 2,
      "note:": 52,
      "note_slide:": 0,
      "note_slide_curve:": 0,
      "note_slide_shape:": 1,
      "pan:": 0,
      "pan_slide:": 0,
      "pan_slide_curve:": 0,
      "pan_slide_shape:": 1,
      "release:": 4.0,
      "sustain:": 0,
      "sustain_level:": 1
    },
    "descr": "Singer",
    "hiden": true,
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "name": ":singer"
  },
  "SonicPiSynth": {
    "arg_defaults": {},
    "hiden": true,
    "inherit_arg": true,
    "inherit_base": "SynthInfo"
  },
  "SoundIn": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "attack:": 0,
      "attack_level:": 1,
      "decay:": 0,
      "decay_level:": 1,
      "env_curve:": 0,
      "input:": 1,
      "pan:": 0,
      "pan_slide:": 0,
      "pan_slide_curve:": 0,
      "pan_slide_shape:": 1,
      "release:": 0,
      "sustain:": 1,
      "sustain_level:": 1
    },
    "descr": "Sound In",
    "hiden": false,
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "name": ":sound_in"
  },
  "SoundInStereo": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "attack:": 0,
      "attack_level:": 1,
      "decay:": 0,
      "decay_level:": 1,
      "env_curve:": 0,
      "input:": 1,
      "pan:": 0,
      "pan_slide:": 0,
      "pan_slide_curve:": 0,
      "pan_slide_shape:": 1,
      "release:": 0,
      "sustain:": 1,
      "sustain_level:": 1
    },
    "descr": "Sound In Stereo",
    "hiden": true,
    "inherit_arg": true,
    "inherit_base": "SoundIn",
    "name": ":sound_in_stereo"
  },
  "Square": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "attack:": 0,
      "attack_level:": 1,
      "cutoff:": 100,
      "cutoff_slide:": 0,
      "cutoff_slide_curve:": 0,
      "cutoff_slide_shape:": 1,
      "decay:": 0,
      "decay_level:": 1,
      "env_curve:": 2,
      "note:": 52,
      "note_slide:": 0,
      "note_slide_curve:": 0,
      "note_slide_shape:": 1,
      "pan:": 0,
      "pan_slide:": 0,
      "pan_slide_curve:": 0,
      "pan_slide_shape:": 1,
      "release:": 1,
      "sustain:": 0,
      "sustain_level:": 1
    },
    "descr": "Square Wave",
    "hiden": false,
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "name": ":square"
  },
  "StereoPlayer": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "attack:": 0,
      "attack_level:": 1,
      "clamp_time:": 0.01,
      "clamp_time_slide:": 0,
      "clamp_time_slide_curve:": 0,
      "clamp_time_slide_shape:": 1,
      "compress:": 0,
      "decay:": 0,
      "decay_level:": 1,
      "env_curve:": 2,
      "finish:": 1,
      "hpf:": -1,
      "hpf_attack:": 0,
      "hpf_attack_level:": -1,
      "hpf_decay:": 0,
      "hpf_decay_level:": -1,
      "hpf_env_curve:": 2,
      "hpf_init_level:": -1,
      "hpf_max:": -1,
      "hpf_max_slide:": 0,
      "hpf_max_slide_curve:": 0,
      "hpf_max_slide_shape:": 1,
      "hpf_release:": 0,
      "hpf_release_level:": -1,
      "hpf_slide:": 0,
      "hpf_slide_curve:": 0,
      "hpf_slide_shape:": 1,
      "hpf_sustain:": -1,
      "hpf_sustain_level:": -1,
      "lpf:": -1,
      "lpf_attack:": 0,
      "lpf_attack_level:": -1,
      "lpf_decay:": 0,
      "lpf_decay_level:": -1,
      "lpf_env_curve:": 2,
      "lpf_init_level:": -1,
      "lpf_min:": -1,
      "lpf_min_slide:": 0,
      "lpf_min_slide_curve:": 0,
      "lpf_min_slide_shape:": 1,
      "lpf_release:": 0,
      "lpf_release_level:": -1,
      "lpf_slide:": 0,
      "lpf_slide_curve:": 0,
      "lpf_slide_shape:": 1,
      "lpf_sustain:": -1,
      "lpf_sustain_level:": -1,
      "norm:": 0,
      "pan:": 0,
      "pan_slide:": 0,
      "pan_slide_curve:": 0,
      "pan_slide_shape:": 1,
      "pitch:": 0,
      "pitch_dis:": 0.0,
      "pitch_dis_slide:": 0,
      "pitch_dis_slide_curve:": 0,
      "pitch_dis_slide_shape:": 1,
      "pitch_slide:": 0,
      "pitch_slide_curve:": 0,
      "pitch_slide_shape:": 1,
      "pre_amp:": 1,
      "pre_amp_slide:": 0,
      "pre_amp_slide_curve:": 0,
      "pre_amp_slide_shape:": 1,
      "rate:": 1,
      "relax_time:": 0.01,
      "relax_time_slide:": 0,
      "relax_time_slide_curve:": 0,
      "relax_time_slide_shape:": 1,
      "release:": 0,
      "slope_above:": 0.5,
      "slope_above_slide:": 0,
      "slope_above_slide_curve:": 0,
      "slope_above_slide_shape:": 1,
      "slope_below:": 1,
      "slope_below_slide:": 0,
      "slope_below_slide_curve:": 0,
      "slope_below_slide_shape:": 1,
      "start:": 0,
      "sustain:": -1,
      "sustain_level:": 1,
      "threshold:": 0.2,
      "threshold_slide:": 0,
      "threshold_slide_curve:": 0,
      "threshold_slide_shape:": 1,
      "time_dis:": 0.0,
      "time_dis_slide:": 0,
      "time_dis_slide_curve:": 0,
      "time_dis_slide_shape:": 1,
      "window_size:": 0.2,
      "window_size_slide:": 0,
      "window_size_slide_curve:": 0,
      "window_size_slide_shape:": 1
    },
    "descr": "Stereo Sample Player",
    "hiden": true,
    "inherit_arg": true,
    "inherit_base": "MonoPlayer",
    "name": ":stereo_player"
  },
  "StudioInfo": {
    "arg_defaults": {},
    "hiden": true,
    "inherit_arg": true,
    "inherit_base": "SonicPiSynth"
  },
  "SubPulse": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "attack:": 0,
      "attack_level:": 1,
      "cutoff:": 100,
      "cutoff_slide:": 0,
      "cutoff_slide_curve:": 0,
      "cutoff_slide_shape:": 1,
      "decay:": 0,
      "decay_level:": 1,
      "env_curve:": 2,
      "note:": 52,
      "note_slide:": 0,
      "note_slide_curve:": 0,
      "note_slide_shape:": 1,
      "pan:": 0,
      "pan_slide:": 0,
      "pan_slide_curve:": 0,
      "pan_slide_shape:": 1,
      "pulse_width:": 0.5,
      "pulse_width_slide:": 0,
      "pulse_width_slide_shape:": 1,
      "release:": 1,
      "sub_amp:": 1,
      "sub_amp_slide:": 0,
      "sub_amp_slide_curve:": 0,
      "sub_amp_slide_shape:": 1,
      "sub_detune:": -12,
      "sub_detune_slide:": 0,
      "sub_detune_slide_shape:": 1,
      "sustain:": 0,
      "sustain_level:": 1
    },
    "descr": "Pulse Wave with sub",
    "hiden": true,
    "inherit_arg": true,
    "inherit_base": "Pulse",
    "name": ":subpulse"
  },
  "Supersaw": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "attack:": 0,
      "attack_level:": 1,
      "cutoff:": 130,
      "cutoff_slide:": 0,
      "cutoff_slide_curve:": 0,
      "cutoff_slide_shape:": 1,
      "decay:": 0,
      "decay_level:": 1,
      "env_curve:": 2,
      "note:": 52,
      "note_slide:": 0,
      "note_slide_curve:": 0,
      "note_slide_shape:": 1,
      "pan:": 0,
      "pan_slide:": 0,
      "pan_slide_curve:": 0,
      "pan_slide_shape:": 1,
      "release:": 1,
      "res:": 0.7,
      "res_slide:": 0,
      "res_slide_curve:": 0,
      "res_slide_shape:": 1,
      "sustain:": 0,
      "sustain_level:": 1
    },
    "descr": "Supersaw",
    "hiden": false,
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "name": ":supersaw"
  },
  "SynthInfo": {
    "arg_defaults": {},
    "hiden": true,
    "inherit_arg": true,
    "inherit_base": "BaseInfo"
  },
  "SynthPiano": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "attack:": 0,
      "attack_level:": 1,
      "decay:": 0,
      "decay_level:": 1,
      "hard:": 0.5,
      "note:": 52,
      "note_slide:": 0,
      "note_slide_curve:": 0,
      "note_slide_shape:": 1,
      "pan:": 0,
      "pan_slide:": 0,
      "pan_slide_curve:": 0,
      "pan_slide_shape:": 1,
      "release:": 1,
      "stereo_width:": 0,
      "sustain:": 0,
      "sustain_level:": 1,
      "vel:": 0.2
    },
    "descr": "SynthPiano",
    "hiden": false,
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "name": ":piano"
  },
  "SynthPluck": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "attack:": 0,
      "attack_level:": 1,
      "coef:": 0.3,
      "decay:": 0,
      "decay_level:": 1,
      "max_delay_time:": 0.125,
      "noise_amp:": 0.8,
      "note:": 52,
      "note_slide:": 0,
      "note_slide_curve:": 0,
      "note_slide_shape:": 1,
      "pan:": 0,
      "pan_slide:": 0,
      "pan_slide_curve:": 0,
      "pan_slide_shape:": 1,
      "pluck_decay:": 30,
      "release:": 1,
      "sustain:": 0,
      "sustain_level:": 1
    },
    "descr": "SynthPluck",
    "hiden": false,
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "name": ":pluck"
  },
  "SynthViolin": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "attack:": 0,
      "attack_level:": 1,
      "cutoff:": 100,
      "cutoff_slide:": 0,
      "cutoff_slide_curve:": 0,
      "cutoff_slide_shape:": 1,
      "decay:": 0,
      "decay_level:": 1,
      "env_curve:": 2,
      "note:": 52,
      "note_slide:": 0,
      "note_slide_curve:": 0,
      "note_slide_shape:": 1,
      "pan:": 0,
      "pan_slide:": 0,
      "pan_slide_curve:": 0,
      "pan_slide_shape:": 1,
      "release:": 1,
      "sustain:": 0,
      "sustain_level:": 1,
      "vibrato_delay:": 0.5,
      "vibrato_depth:": 0.15,
      "vibrato_depth_slide_curve:": 0,
      "vibrato_depth_slide_shape:": 1,
      "vibrato_onset:": 0.1,
      "vibrato_rate:": 6,
      "vibrato_rate_slide_curve:": 0,
      "vibrato_rate_slide_shape:": 1
    },
    "descr": "Blade Runner style strings",
    "hiden": false,
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "name": ":synth_violin"
  },
  "TB303": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "attack:": 0,
      "attack_level:": 1,
      "cutoff:": 120,
      "cutoff_attack:": 0,
      "cutoff_attack_level:": 1,
      "cutoff_decay:": 0,
      "cutoff_decay_level:": 1,
      "cutoff_min:": 30,
      "cutoff_min_slide:": 0,
      "cutoff_min_slide_curve:": 0,
      "cutoff_min_slide_shape:": 1,
      "cutoff_release:": 1,
      "cutoff_slide:": 0,
      "cutoff_slide_curve:": 0,
      "cutoff_slide_shape:": 1,
      "cutoff_sustain:": 0,
      "cutoff_sustain_level:": 1,
      "decay:": 0,
      "decay_level:": 1,
      "env_curve:": 2,
      "note:": 52,
      "note_slide:": 0,
      "note_slide_curve:": 0,
      "note_slide_shape:": 1,
      "pan:": 0,
      "pan_slide:": 0,
      "pan_slide_curve:": 0,
      "pan_slide_shape:": 1,
      "pulse_width:": 0.5,
      "pulse_width_slide:": 0,
      "pulse_width_slide_curve:": 0,
      "pulse_width_slide_shape:": 1,
      "release:": 1,
      "res:": 0.9,
      "res_slide:": 0,
      "res_slide_curve:": 0,
      "res_slide_shape:": 1,
      "sustain:": 0,
      "sustain_level:": 1,
      "wave:": 0
    },
    "descr": "TB-303 Emulation",
    "hiden": false,
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "name": ":tb303"
  },
  "TechSaws": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "attack:": 0,
      "attack_level:": 1,
      "cutoff:": 130,
      "cutoff_slide:": 0,
      "cutoff_slide_curve:": 0,
      "cutoff_slide_shape:": 1,
      "decay:": 0,
      "decay_level:": 1,
      "env_curve:": 2,
      "note:": 52,
      "note_slide:": 0,
      "note_slide_curve:": 0,
      "note_slide_shape:": 1,
      "pan:": 0,
      "pan_slide:": 0,
      "pan_slide_curve:": 0,
      "pan_slide_shape:": 1,
      "release:": 1,
      "res:": 0.7,
      "res_slide:": 0,
      "res_slide_curve:": 0,
      "res_slide_shape:": 1,
      "sustain:": 0,
      "sustain_level:": 1
    },
    "descr": "TechSaws",
    "hiden": false,
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "name": ":tech_saws"
  },
  "Tri": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "attack:": 0,
      "attack_level:": 1,
      "cutoff:": 100,
      "cutoff_slide:": 0,
      "cutoff_slide_curve:": 0,
      "cutoff_slide_shape:": 1,
      "decay:": 0,
      "decay_level:": 1,
      "env_curve:": 2,
      "note:": 52,
      "note_slide:": 0,
      "note_slide_curve:": 0,
      "note_slide_shape:": 1,
      "pan:": 0,
      "pan_slide:": 0,
      "pan_slide_curve:": 0,
      "pan_slide_shape:": 1,
      "pulse_width:": 0.5,
      "pulse_width_slide:": 0,
      "pulse_width_slide_shape:": 1,
      "release:": 1,
      "sustain:": 0,
      "sustain_level:": 1
    },
    "descr": "Triangle Wave",
    "hiden": true,
    "inherit_arg": true,
    "inherit_base": "Pulse",
    "name": ":tri"
  },
  "Zawa": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "attack:": 0,
      "attack_level:": 1,
      "cutoff:": 100,
      "cutoff_slide:": 0,
      "cutoff_slide_curve:": 0,
      "cutoff_slide_shape:": 1,
      "decay:": 0,
      "decay_level:": 1,
      "disable_wave:": 0,
      "invert_wave:": 0,
      "note:": 52,
      "note_slide:": 0,
      "note_slide_curve:": 0,
      "note_slide_shape:": 1,
      "pan:": 0,
      "pan_slide:": 0,
      "pan_slide_curve:": 0,
      "pan_slide_shape:": 1,
      "phase:": 1,
      "phase_offset:": 0,
      "phase_slide:": 0,
      "phase_slide_curve:": 0,
      "phase_slide_shape:": 1,
      "pulse_width:": 0.5,
      "pulse_width_slide:": 0,
      "pulse_width_slide_curve:": 0,
      "pulse_width_slide_shape:": 1,
      "range:": 24,
      "range_slide:": 0,
      "range_slide_curve:": 0,
      "range_slide_shape:": 1,
      "release:": 1,
      "res:": 0.9,
      "res_slide:": 0,
      "res_slide_curve:": 0,
      "res_slide_shape:": 1,
      "sustain:": 0,
      "sustain_level:": 1,
      "wave:": 3
    },
    "descr": "Zawa",
    "hiden": false,
    "inherit_arg": false,
    "inherit_base": "SonicPiSynth",
    "name": ":zawa"
  }
}

synth_nodes = {
  ":basic_mixer": "BasicMixer",
  ":basic_mono_player": "BasicMonoPlayer",
  ":basic_stereo_player": "BasicStereoPlayer",
  ":beep": "Beep",
  ":blade": "SynthViolin",
  ":bnoise": "BNoise",
  ":chipbass": "ChipBass",
  ":chiplead": "ChipLead",
  ":chipnoise": "ChipNoise",
  ":cnoise": "CNoise",
  ":dark_ambience": "DarkAmbience",
  ":dpulse": "DPulse",
  ":dsaw": "DSaw",
  ":dtri": "DTri",
  ":dull_bell": "DullBell",
  ":fm": "FM",
  ":fx_band_eq": "FXBandEQ",
  ":fx_bitcrusher": "FXBitcrusher",
  ":fx_bpf": "FXBPF",
  ":fx_compressor": "FXCompressor",
  ":fx_distortion": "FXDistortion",
  ":fx_echo": "FXEcho",
  ":fx_flanger": "FXFlanger",
  ":fx_gverb": "FXGVerb",
  ":fx_hpf": "FXHPF",
  ":fx_ixi_techno": "FXIXITechno",
  ":fx_krush": "FXKrush",
  ":fx_level": "FXLevel",
  ":fx_lpf": "FXLPF",
  ":fx_mono": "FXMono",
  ":fx_nbpf": "FXNBPF",
  ":fx_nhpf": "FXNormHPF",
  ":fx_nlpf": "FXNormLPF",
  ":fx_normaliser": "FXNormaliser",
  ":fx_nrbpf": "FXNRBPF",
  ":fx_nrhpf": "FXNormRHPF",
  ":fx_nrlpf": "FXNormRLPF",
  ":fx_octaver": "FXOctaver",
  ":fx_pan": "FXPan",
  ":fx_panslicer": "FXPanSlicer",
  ":fx_pitch_shift": "FXPitchShift",
  ":fx_rbpf": "FXRBPF",
  ":fx_replace_compressor": "FXCompressor",
  ":fx_replace_distortion": "FXDistortion",
  ":fx_replace_echo": "FXEcho",
  ":fx_replace_hpf": "FXHPF",
  ":fx_replace_ixi_techno": "FXIXITechno",
  ":fx_replace_level": "FXLevel",
  ":fx_replace_lpf": "FXLPF",
  ":fx_replace_nhpf": "FXNormHPF",
  ":fx_replace_nlpf": "FXNormLPF",
  ":fx_replace_normaliser": "FXNormaliser",
  ":fx_replace_nrhpf": "FXNormRHPF",
  ":fx_replace_nrlpf": "FXNormRLPF",
  ":fx_replace_pan": "FXPan",
  ":fx_replace_reverb": "FXReverb",
  ":fx_replace_rhpf": "FXRHPF",
  ":fx_replace_rlpf": "FXRLPF",
  ":fx_replace_slicer": "FXSlicer",
  ":fx_replace_wobble": "FXWobble",
  ":fx_reverb": "FXReverb",
  ":fx_rhpf": "FXRHPF",
  ":fx_ring_mod": "FXRingMod",
  ":fx_rlpf": "FXRLPF",
  ":fx_slicer": "FXSlicer",
  ":fx_tanh": "FXTanh",
  ":fx_vowel": "FXVowel",
  ":fx_whammy": "FXWhammy",
  ":fx_wobble": "FXWobble",
  ":gnoise": "GNoise",
  ":growl": "Growl",
  ":hollow": "Hollow",
  ":hoover": "Hoover",
  ":main_mixer": "MainMixer",
  ":mod_beep": "ModSine",
  ":mod_dsaw": "ModDSaw",
  ":mod_fm": "ModFM",
  ":mod_pulse": "ModPulse",
  ":mod_saw": "ModSaw",
  ":mod_sine": "ModSine",
  ":mod_tri": "ModTri",
  ":mono_player": "MonoPlayer",
  ":noise": "Noise",
  ":piano": "SynthPiano",
  ":pluck": "SynthPluck",
  ":pnoise": "PNoise",
  ":pretty_bell": "PrettyBell",
  ":prophet": "Prophet",
  ":pulse": "Pulse",
  ":saw": "Saw",
  ":sine": "Beep",
  ":sound_in": "SoundIn",
  ":sound_in_stereo": "SoundInStereo",
  ":square": "Square",
  ":stereo_player": "StereoPlayer",
  ":subpulse": "SubPulse",
  ":supersaw": "Supersaw",
  ":tb303": "TB303",
  ":tech_saws": "TechSaws",
  ":tri": "Tri",
  ":zawa": "Zawa"
}

fx = {
  "FXBPF": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "centre:": 100,
      "centre_slide:": 0,
      "centre_slide_curve:": 0,
      "centre_slide_shape:": 1,
      "mix:": 1,
      "mix_slide:": 0,
      "mix_slide_curve:": 0,
      "mix_slide_shape:": 1,
      "pre_amp:": 1,
      "pre_amp_slide:": 0,
      "pre_amp_slide_curve:": 0,
      "pre_amp_slide_shape:": 1,
      "pre_mix:": 1,
      "pre_mix_slide:": 0,
      "pre_mix_slide_curve:": 0,
      "pre_mix_slide_shape:": 1,
      "res:": 0.6,
      "res_slide:": 0,
      "res_slide_curve:": 0,
      "res_slide_shape:": 1
    },
    "descr": "Band Pass Filter",
    "hiden": false,
    "inherit_arg": true,
    "inherit_base": "FXInfo",
    "name": ":fx_bpf"
  },
  "FXBandEQ": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "db:": 0.6,
      "db_slide:": 0,
      "db_slide_curve:": 0,
      "db_slide_shape:": 1,
      "freq:": 100,
      "freq_slide:": 0,
      "freq_slide_curve:": 0,
      "freq_slide_shape:": 1,
      "mix:": 1,
      "mix_slide:": 0,
      "mix_slide_curve:": 0,
      "mix_slide_shape:": 1,
      "pre_amp:": 1,
      "pre_amp_slide:": 0,
      "pre_amp_slide_curve:": 0,
      "pre_amp_slide_shape:": 1,
      "pre_mix:": 1,
      "pre_mix_slide:": 0,
      "pre_mix_slide_curve:": 0,
      "pre_mix_slide_shape:": 1,
      "res:": 0.6,
      "res_slide:": 0,
      "res_slide_curve:": 0,
      "res_slide_shape:": 1
    },
    "descr": "Band EQ Filter",
    "hiden": false,
    "inherit_arg": true,
    "inherit_base": "FXInfo",
    "name": ":fx_band_eq"
  },
  "FXBitcrusher": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "bits:": 8,
      "bits_slide:": 0,
      "bits_slide_curve:": 0,
      "bits_slide_shape:": 1,
      "cutoff:": 0,
      "cutoff_slide:": 0,
      "cutoff_slide_curve:": 0,
      "cutoff_slide_shape:": 1,
      "mix:": 1,
      "mix_slide:": 0,
      "mix_slide_curve:": 0,
      "mix_slide_shape:": 1,
      "pre_amp:": 1,
      "pre_amp_slide:": 0,
      "pre_amp_slide_curve:": 0,
      "pre_amp_slide_shape:": 1,
      "pre_mix:": 1,
      "pre_mix_slide:": 0,
      "pre_mix_slide_curve:": 0,
      "pre_mix_slide_shape:": 1,
      "sample_rate:": 10000,
      "sample_rate_slide:": 0,
      "sample_rate_slide_curve:": 0,
      "sample_rate_slide_shape:": 1
    },
    "descr": "Bitcrusher",
    "hiden": false,
    "inherit_arg": true,
    "inherit_base": "FXInfo",
    "name": ":fx_bitcrusher"
  },
  "FXChorus": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "decay:": 1e-05,
      "decay_slide:": 0,
      "decay_slide_curve:": 0,
      "decay_slide_shape:": 1,
      "max_phase:": 1,
      "mix:": 1,
      "mix_slide:": 0,
      "mix_slide_curve:": 0,
      "mix_slide_shape:": 1,
      "phase:": 0.25,
      "phase_slide:": 0,
      "phase_slide_curve:": 0,
      "phase_slide_shape:": 1,
      "pre_amp:": 1,
      "pre_amp_slide:": 0,
      "pre_amp_slide_curve:": 0,
      "pre_amp_slide_shape:": 1,
      "pre_mix:": 1,
      "pre_mix_slide:": 0,
      "pre_mix_slide_curve:": 0,
      "pre_mix_slide_shape:": 1
    },
    "descr": "Chorus",
    "hiden": true,
    "inherit_arg": true,
    "inherit_base": "FXInfo",
    "name": ":fx_chorus"
  },
  "FXCompressor": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "clamp_time:": 0.01,
      "clamp_time_slide:": 0,
      "clamp_time_slide_curve:": 0,
      "clamp_time_slide_shape:": 1,
      "mix:": 1,
      "mix_slide:": 0,
      "mix_slide_curve:": 0,
      "mix_slide_shape:": 1,
      "pre_amp:": 1,
      "pre_amp_slide:": 0,
      "pre_amp_slide_curve:": 0,
      "pre_amp_slide_shape:": 1,
      "pre_mix:": 1,
      "pre_mix_slide:": 0,
      "pre_mix_slide_curve:": 0,
      "pre_mix_slide_shape:": 1,
      "relax_time:": 0.01,
      "relax_time_slide:": 0,
      "relax_time_slide_curve:": 0,
      "relax_time_slide_shape:": 1,
      "slope_above:": 0.5,
      "slope_above_slide:": 0,
      "slope_above_slide_curve:": 0,
      "slope_above_slide_shape:": 1,
      "slope_below:": 1,
      "slope_below_slide:": 0,
      "slope_below_slide_curve:": 0,
      "slope_below_slide_shape:": 1,
      "threshold:": 0.2,
      "threshold_slide:": 0,
      "threshold_slide_curve:": 0,
      "threshold_slide_shape:": 1
    },
    "descr": "Compressor",
    "hiden": false,
    "inherit_arg": true,
    "inherit_base": "FXInfo",
    "name": ":fx_compressor"
  },
  "FXDistortion": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "distort:": 0.5,
      "distort_slide:": 0,
      "distort_slide_curve:": 0,
      "distort_slide_shape:": 1,
      "mix:": 1,
      "mix_slide:": 0,
      "mix_slide_curve:": 0,
      "mix_slide_shape:": 1,
      "pre_amp:": 1,
      "pre_amp_slide:": 0,
      "pre_amp_slide_curve:": 0,
      "pre_amp_slide_shape:": 1,
      "pre_mix:": 1,
      "pre_mix_slide:": 0,
      "pre_mix_slide_curve:": 0,
      "pre_mix_slide_shape:": 1
    },
    "descr": "Distortion",
    "hiden": false,
    "inherit_arg": true,
    "inherit_base": "FXInfo",
    "name": ":fx_distortion"
  },
  "FXEcho": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "decay:": 2,
      "decay_slide:": 0,
      "decay_slide_curve:": 0,
      "decay_slide_shape:": 1,
      "max_phase:": 2,
      "mix:": 1,
      "mix_slide:": 0,
      "mix_slide_curve:": 0,
      "mix_slide_shape:": 1,
      "phase:": 0.25,
      "phase_slide:": 0,
      "phase_slide_curve:": 0,
      "phase_slide_shape:": 1,
      "pre_amp:": 1,
      "pre_amp_slide:": 0,
      "pre_amp_slide_curve:": 0,
      "pre_amp_slide_shape:": 1,
      "pre_mix:": 1,
      "pre_mix_slide:": 0,
      "pre_mix_slide_curve:": 0,
      "pre_mix_slide_shape:": 1
    },
    "descr": "Echo",
    "hiden": false,
    "inherit_arg": true,
    "inherit_base": "FXInfo",
    "name": ":fx_echo"
  },
  "FXFlanger": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "decay:": 2,
      "decay_slide:": 0,
      "decay_slide_curve:": 0,
      "decay_slide_shape:": 1,
      "delay:": 5,
      "delay_slide:": 0,
      "delay_slide_curve:": 0,
      "delay_slide_shape:": 1,
      "depth:": 5,
      "depth_slide:": 0,
      "depth_slide_curve:": 0,
      "depth_slide_shape:": 1,
      "feedback:": 0,
      "feedback_slide:": 0,
      "feedback_slide_curve:": 0,
      "feedback_slide_shape:": 1,
      "invert_flange:": 0,
      "invert_wave:": 0,
      "max_delay:": 20,
      "mix:": 1,
      "mix_slide:": 0,
      "mix_slide_curve:": 0,
      "mix_slide_shape:": 1,
      "phase:": 4,
      "phase_offset:": 0,
      "phase_slide:": 0,
      "phase_slide_curve:": 0,
      "phase_slide_shape:": 1,
      "pre_amp:": 1,
      "pre_amp_slide:": 0,
      "pre_amp_slide_curve:": 0,
      "pre_amp_slide_shape:": 1,
      "pre_mix:": 1,
      "pre_mix_slide:": 0,
      "pre_mix_slide_curve:": 0,
      "pre_mix_slide_shape:": 1,
      "stereo_invert_wave:": 0,
      "wave:": 4
    },
    "descr": "Flanger",
    "hiden": false,
    "inherit_arg": true,
    "inherit_base": "FXInfo",
    "name": ":fx_flanger"
  },
  "FXGVerb": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "damp:": 0.5,
      "damp_slide:": 0,
      "damp_slide_curve:": 0,
      "damp_slide_shape:": 1,
      "dry:": 1,
      "dry_slide:": 0,
      "dry_slide_curve:": 0,
      "dry_slide_shape:": 1,
      "mix:": 1,
      "mix_slide:": 0,
      "mix_slide_curve:": 0,
      "mix_slide_shape:": 1,
      "pre_amp:": 1,
      "pre_amp_slide:": 0,
      "pre_amp_slide_curve:": 0,
      "pre_amp_slide_shape:": 1,
      "pre_damp:": 0.5,
      "pre_damp_slide:": 0,
      "pre_damp_slide_curve:": 0,
      "pre_damp_slide_shape:": 1,
      "pre_mix:": 1,
      "pre_mix_slide:": 0,
      "pre_mix_slide_curve:": 0,
      "pre_mix_slide_shape:": 1,
      "ref_level:": 0.7,
      "release:": 3,
      "room:": 10,
      "spread:": 0.5,
      "spread_slide:": 0,
      "spread_slide_curve:": 0,
      "spread_slide_shape:": 1,
      "tail_level:": 0.5
    },
    "descr": "GVerb",
    "hiden": false,
    "inherit_arg": true,
    "inherit_base": "FXInfo",
    "name": ":fx_gverb"
  },
  "FXHPF": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "cutoff:": 100,
      "cutoff_slide:": 0,
      "cutoff_slide_curve:": 0,
      "cutoff_slide_shape:": 1,
      "mix:": 1,
      "mix_slide:": 0,
      "mix_slide_curve:": 0,
      "mix_slide_shape:": 1,
      "pre_amp:": 1,
      "pre_amp_slide:": 0,
      "pre_amp_slide_curve:": 0,
      "pre_amp_slide_shape:": 1,
      "pre_mix:": 1,
      "pre_mix_slide:": 0,
      "pre_mix_slide_curve:": 0,
      "pre_mix_slide_shape:": 1
    },
    "descr": "High Pass Filter",
    "hiden": false,
    "inherit_arg": true,
    "inherit_base": "FXInfo",
    "name": ":fx_hpf"
  },
  "FXIXITechno": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "cutoff_max:": 120,
      "cutoff_max_slide:": 0,
      "cutoff_max_slide_curve:": 0,
      "cutoff_max_slide_shape:": 1,
      "cutoff_min:": 60,
      "cutoff_min_slide:": 0,
      "cutoff_min_slide_curve:": 0,
      "cutoff_min_slide_shape:": 1,
      "mix:": 1,
      "mix_slide:": 0,
      "mix_slide_curve:": 0,
      "mix_slide_shape:": 1,
      "phase:": 4,
      "phase_offset:": 0,
      "phase_slide:": 0,
      "phase_slide_curve:": 0,
      "phase_slide_shape:": 1,
      "pre_amp:": 1,
      "pre_amp_slide:": 0,
      "pre_amp_slide_curve:": 0,
      "pre_amp_slide_shape:": 1,
      "pre_mix:": 1,
      "pre_mix_slide:": 0,
      "pre_mix_slide_curve:": 0,
      "pre_mix_slide_shape:": 1,
      "res:": 0.8,
      "res_slide:": 0,
      "res_slide_curve:": 0,
      "res_slide_shape:": 1
    },
    "descr": "Techno from IXI Lang",
    "hiden": false,
    "inherit_arg": true,
    "inherit_base": "FXInfo",
    "name": ":fx_ixi_techno"
  },
  "FXInfo": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "mix:": 1,
      "mix_slide:": 0,
      "mix_slide_curve:": 0,
      "mix_slide_shape:": 1,
      "pre_amp:": 1,
      "pre_amp_slide:": 0,
      "pre_amp_slide_curve:": 0,
      "pre_amp_slide_shape:": 1,
      "pre_mix:": 1,
      "pre_mix_slide:": 0,
      "pre_mix_slide_curve:": 0,
      "pre_mix_slide_shape:": 1
    },
    "hiden": true,
    "inherit_arg": false,
    "inherit_base": "BaseInfo"
  },
  "FXKrush": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "cutoff:": 100,
      "cutoff_slide:": 0,
      "cutoff_slide_curve:": 0,
      "cutoff_slide_shape:": 1,
      "gain:": 5,
      "gain_slide:": 0,
      "gain_slide__curve:": 0,
      "gain_slide_shape:": 1,
      "mix:": 1,
      "mix_slide:": 0,
      "mix_slide_curve:": 0,
      "mix_slide_shape:": 1,
      "pre_amp:": 1,
      "pre_amp_slide:": 0,
      "pre_amp_slide_curve:": 0,
      "pre_amp_slide_shape:": 1,
      "pre_mix:": 1,
      "pre_mix_slide:": 0,
      "pre_mix_slide_curve:": 0,
      "pre_mix_slide_shape:": 1,
      "res:": 0,
      "res_slide:": 0,
      "res_slide_curve:": 0,
      "res_slide_shape:": 1
    },
    "descr": "krush",
    "hiden": false,
    "inherit_arg": true,
    "inherit_base": "FXInfo",
    "name": ":fx_krush"
  },
  "FXLPF": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "cutoff:": 100,
      "cutoff_slide:": 0,
      "cutoff_slide_curve:": 0,
      "cutoff_slide_shape:": 1,
      "mix:": 1,
      "mix_slide:": 0,
      "mix_slide_curve:": 0,
      "mix_slide_shape:": 1,
      "pre_amp:": 1,
      "pre_amp_slide:": 0,
      "pre_amp_slide_curve:": 0,
      "pre_amp_slide_shape:": 1,
      "pre_mix:": 1,
      "pre_mix_slide:": 0,
      "pre_mix_slide_curve:": 0,
      "pre_mix_slide_shape:": 1
    },
    "descr": "Low Pass Filter",
    "hiden": false,
    "inherit_arg": true,
    "inherit_base": "FXInfo",
    "name": ":fx_lpf"
  },
  "FXLevel": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1
    },
    "descr": "Level Amplifier",
    "hiden": false,
    "inherit_arg": false,
    "inherit_base": "FXInfo",
    "name": ":fx_level"
  },
  "FXMono": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "mix:": 1,
      "mix_slide:": 0,
      "mix_slide_curve:": 0,
      "mix_slide_shape:": 1,
      "pan:": 0,
      "pan_slide:": 0,
      "pan_slide_curve:": 0,
      "pan_slide_shape:": 1,
      "pre_amp:": 1,
      "pre_amp_slide:": 0,
      "pre_amp_slide_curve:": 0,
      "pre_amp_slide_shape:": 1,
      "pre_mix:": 1,
      "pre_mix_slide:": 0,
      "pre_mix_slide_curve:": 0,
      "pre_mix_slide_shape:": 1
    },
    "descr": "Mono",
    "hiden": false,
    "inherit_arg": true,
    "inherit_base": "FXInfo",
    "name": ":fx_mono"
  },
  "FXNBPF": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "centre:": 100,
      "centre_slide:": 0,
      "centre_slide_curve:": 0,
      "centre_slide_shape:": 1,
      "mix:": 1,
      "mix_slide:": 0,
      "mix_slide_curve:": 0,
      "mix_slide_shape:": 1,
      "pre_amp:": 1,
      "pre_amp_slide:": 0,
      "pre_amp_slide_curve:": 0,
      "pre_amp_slide_shape:": 1,
      "pre_mix:": 1,
      "pre_mix_slide:": 0,
      "pre_mix_slide_curve:": 0,
      "pre_mix_slide_shape:": 1,
      "res:": 0.6,
      "res_slide:": 0,
      "res_slide_curve:": 0,
      "res_slide_shape:": 1
    },
    "descr": "Normalised Band Pass Filter",
    "hiden": true,
    "inherit_arg": true,
    "inherit_base": "FXBPF",
    "name": ":fx_nbpf"
  },
  "FXNRBPF": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "centre:": 100,
      "centre_slide:": 0,
      "centre_slide_curve:": 0,
      "centre_slide_shape:": 1,
      "mix:": 1,
      "mix_slide:": 0,
      "mix_slide_curve:": 0,
      "mix_slide_shape:": 1,
      "pre_amp:": 1,
      "pre_amp_slide:": 0,
      "pre_amp_slide_curve:": 0,
      "pre_amp_slide_shape:": 1,
      "pre_mix:": 1,
      "pre_mix_slide:": 0,
      "pre_mix_slide_curve:": 0,
      "pre_mix_slide_shape:": 1,
      "res:": 0.5,
      "res_slide:": 0,
      "res_slide_curve:": 0,
      "res_slide_shape:": 1
    },
    "descr": "Normalised Resonant Band Pass Filter",
    "hiden": true,
    "inherit_arg": true,
    "inherit_base": "FXRBPF",
    "name": ":fx_nrbpf"
  },
  "FXNormHPF": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "cutoff:": 100,
      "cutoff_slide:": 0,
      "cutoff_slide_curve:": 0,
      "cutoff_slide_shape:": 1,
      "mix:": 1,
      "mix_slide:": 0,
      "mix_slide_curve:": 0,
      "mix_slide_shape:": 1,
      "pre_amp:": 1,
      "pre_amp_slide:": 0,
      "pre_amp_slide_curve:": 0,
      "pre_amp_slide_shape:": 1,
      "pre_mix:": 1,
      "pre_mix_slide:": 0,
      "pre_mix_slide_curve:": 0,
      "pre_mix_slide_shape:": 1
    },
    "descr": "Normalised High Pass Filter",
    "hiden": true,
    "inherit_arg": true,
    "inherit_base": "FXHPF",
    "name": ":fx_nhpf"
  },
  "FXNormLPF": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "cutoff:": 100,
      "cutoff_slide:": 0,
      "cutoff_slide_curve:": 0,
      "cutoff_slide_shape:": 1,
      "mix:": 1,
      "mix_slide:": 0,
      "mix_slide_curve:": 0,
      "mix_slide_shape:": 1,
      "pre_amp:": 1,
      "pre_amp_slide:": 0,
      "pre_amp_slide_curve:": 0,
      "pre_amp_slide_shape:": 1,
      "pre_mix:": 1,
      "pre_mix_slide:": 0,
      "pre_mix_slide_curve:": 0,
      "pre_mix_slide_shape:": 1
    },
    "descr": "Normalised Low Pass Filter.",
    "hiden": true,
    "inherit_arg": true,
    "inherit_base": "FXLPF",
    "name": ":fx_nlpf"
  },
  "FXNormRHPF": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "cutoff:": 100,
      "cutoff_slide:": 0,
      "cutoff_slide_curve:": 0,
      "cutoff_slide_shape:": 1,
      "mix:": 1,
      "mix_slide:": 0,
      "mix_slide_curve:": 0,
      "mix_slide_shape:": 1,
      "pre_amp:": 1,
      "pre_amp_slide:": 0,
      "pre_amp_slide_curve:": 0,
      "pre_amp_slide_shape:": 1,
      "pre_mix:": 1,
      "pre_mix_slide:": 0,
      "pre_mix_slide_curve:": 0,
      "pre_mix_slide_shape:": 1,
      "res:": 0.5,
      "res_slide:": 0,
      "res_slide_curve:": 0,
      "res_slide_shape:": 1
    },
    "descr": "Normalised Resonant High Pass Filter",
    "hiden": true,
    "inherit_arg": true,
    "inherit_base": "FXRHPF",
    "name": ":fx_nrhpf"
  },
  "FXNormRLPF": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "cutoff:": 100,
      "cutoff_slide:": 0,
      "cutoff_slide_curve:": 0,
      "cutoff_slide_shape:": 1,
      "mix:": 1,
      "mix_slide:": 0,
      "mix_slide_curve:": 0,
      "mix_slide_shape:": 1,
      "pre_amp:": 1,
      "pre_amp_slide:": 0,
      "pre_amp_slide_curve:": 0,
      "pre_amp_slide_shape:": 1,
      "pre_mix:": 1,
      "pre_mix_slide:": 0,
      "pre_mix_slide_curve:": 0,
      "pre_mix_slide_shape:": 1,
      "res:": 0.5,
      "res_slide:": 0,
      "res_slide_curve:": 0,
      "res_slide_shape:": 1
    },
    "descr": "Normalised Resonant Low Pass Filter",
    "hiden": true,
    "inherit_arg": true,
    "inherit_base": "FXRLPF",
    "name": ":fx_nrlpf"
  },
  "FXNormaliser": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "level:": 1,
      "level_slide:": 0,
      "level_slide_curve:": 0,
      "level_slide_shape:": 1,
      "mix:": 1,
      "mix_slide:": 0,
      "mix_slide_curve:": 0,
      "mix_slide_shape:": 1,
      "pre_amp:": 1,
      "pre_amp_slide:": 0,
      "pre_amp_slide_curve:": 0,
      "pre_amp_slide_shape:": 1,
      "pre_mix:": 1,
      "pre_mix_slide:": 0,
      "pre_mix_slide_curve:": 0,
      "pre_mix_slide_shape:": 1
    },
    "descr": "Normaliser",
    "hiden": false,
    "inherit_arg": true,
    "inherit_base": "FXInfo",
    "name": ":fx_normaliser"
  },
  "FXOctaver": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "mix:": 1,
      "mix_slide:": 0,
      "mix_slide_curve:": 0,
      "mix_slide_shape:": 1,
      "pre_amp:": 1,
      "pre_amp_slide:": 0,
      "pre_amp_slide_curve:": 0,
      "pre_amp_slide_shape:": 1,
      "pre_mix:": 1,
      "pre_mix_slide:": 0,
      "pre_mix_slide_curve:": 0,
      "pre_mix_slide_shape:": 1,
      "sub_amp:": 1,
      "sub_amp_slide:": 0,
      "sub_amp_slide_curve:": 0,
      "sub_amp_slide_shape:": 1,
      "subsub_amp:": 1,
      "subsub_amp_slide:": 0,
      "subsub_amp_slide_curve:": 0,
      "subsub_amp_slide_shape:": 1,
      "super_amp:": 1,
      "super_amp_slide:": 0,
      "super_amp_slide_curve:": 0,
      "super_amp_slide_shape:": 1
    },
    "descr": "Octaver",
    "hiden": false,
    "inherit_arg": true,
    "inherit_base": "FXInfo",
    "name": ":fx_octaver"
  },
  "FXPan": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "mix:": 1,
      "mix_slide:": 0,
      "mix_slide_curve:": 0,
      "mix_slide_shape:": 1,
      "pan:": 0,
      "pan_slide:": 0,
      "pan_slide_curve:": 0,
      "pan_slide_shape:": 1,
      "pre_amp:": 1,
      "pre_amp_slide:": 0,
      "pre_amp_slide_curve:": 0,
      "pre_amp_slide_shape:": 1,
      "pre_mix:": 1,
      "pre_mix_slide:": 0,
      "pre_mix_slide_curve:": 0,
      "pre_mix_slide_shape:": 1
    },
    "descr": "Pan",
    "hiden": false,
    "inherit_arg": true,
    "inherit_base": "FXInfo",
    "name": ":fx_pan"
  },
  "FXPanSlicer": {
    "arg_defaults": {
      "amp:": 1,
      "amp_max:": 1,
      "amp_max_slide:": 0,
      "amp_max_slide_curve:": 0,
      "amp_max_slide_shape:": 1,
      "amp_min:": 0,
      "amp_min_slide:": 0,
      "amp_min_slide_curve:": 0,
      "amp_min_slide_shape:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "invert_wave:": 0,
      "mix:": 1,
      "mix_slide:": 0,
      "mix_slide_curve:": 0,
      "mix_slide_shape:": 1,
      "pan_max:": 1,
      "pan_max_slide:": 0,
      "pan_max_slide_curve:": 0,
      "pan_max_slide_shape:": 1,
      "pan_min:": -1,
      "pan_min_slide:": 0,
      "pan_min_slide_curve:": 0,
      "pan_min_slide_shape:": 1,
      "phase:": 0.25,
      "phase_offset:": 0,
      "phase_slide:": 0,
      "phase_slide_curve:": 0,
      "phase_slide_shape:": 1,
      "pre_amp:": 1,
      "pre_amp_slide:": 0,
      "pre_amp_slide_curve:": 0,
      "pre_amp_slide_shape:": 1,
      "pre_mix:": 1,
      "pre_mix_slide:": 0,
      "pre_mix_slide_curve:": 0,
      "pre_mix_slide_shape:": 1,
      "prob_pos:": 0,
      "prob_pos_slide:": 0,
      "prob_pos_slide_curve:": 0,
      "prob_pos_slide_shape:": 1,
      "probability:": 0,
      "probability_slide:": 0,
      "probability_slide_curve:": 0,
      "probability_slide_shape:": 1,
      "pulse_width:": 0.5,
      "pulse_width_slide:": 0,
      "pulse_width_slide_curve:": 0,
      "pulse_width_slide_shape:": 1,
      "seed:": 0,
      "smooth:": 0,
      "smooth_down:": 0,
      "smooth_down_slide:": 0,
      "smooth_down_slide_curve:": 0,
      "smooth_down_slide_shape:": 1,
      "smooth_slide:": 0,
      "smooth_slide_curve:": 0,
      "smooth_slide_shape:": 1,
      "smooth_up:": 0,
      "smooth_up_slide:": 0,
      "smooth_up_slide_curve:": 0,
      "smooth_up_slide_shape:": 1,
      "wave:": 1
    },
    "descr": "Pan Slicer",
    "hiden": true,
    "inherit_arg": true,
    "inherit_base": "FXSlicer",
    "name": ":fx_panslicer"
  },
  "FXPitchShift": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "mix:": 1,
      "mix_slide:": 0,
      "mix_slide_curve:": 0,
      "mix_slide_shape:": 1,
      "pitch:": 0,
      "pitch_dis:": 0.0,
      "pitch_dis_slide:": 0,
      "pitch_dis_slide_curve:": 0,
      "pitch_dis_slide_shape:": 1,
      "pitch_slide:": 0,
      "pitch_slide_curve:": 0,
      "pitch_slide_shape:": 1,
      "pre_amp:": 1,
      "pre_amp_slide:": 0,
      "pre_amp_slide_curve:": 0,
      "pre_amp_slide_shape:": 1,
      "pre_mix:": 1,
      "pre_mix_slide:": 0,
      "pre_mix_slide_curve:": 0,
      "pre_mix_slide_shape:": 1,
      "time_dis:": 0.0,
      "time_dis_slide:": 0,
      "time_dis_slide_curve:": 0,
      "time_dis_slide_shape:": 1,
      "window_size:": 0.2,
      "window_size_slide:": 0,
      "window_size_slide_curve:": 0,
      "window_size_slide_shape:": 1
    },
    "descr": "Pitch shift",
    "hiden": false,
    "inherit_arg": true,
    "inherit_base": "FXInfo",
    "name": ":fx_pitch_shift"
  },
  "FXRBPF": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "centre:": 100,
      "centre_slide:": 0,
      "centre_slide_curve:": 0,
      "centre_slide_shape:": 1,
      "mix:": 1,
      "mix_slide:": 0,
      "mix_slide_curve:": 0,
      "mix_slide_shape:": 1,
      "pre_amp:": 1,
      "pre_amp_slide:": 0,
      "pre_amp_slide_curve:": 0,
      "pre_amp_slide_shape:": 1,
      "pre_mix:": 1,
      "pre_mix_slide:": 0,
      "pre_mix_slide_curve:": 0,
      "pre_mix_slide_shape:": 1,
      "res:": 0.5,
      "res_slide:": 0,
      "res_slide_curve:": 0,
      "res_slide_shape:": 1
    },
    "descr": "Resonant Band Pass Filter",
    "hiden": true,
    "inherit_arg": true,
    "inherit_base": "FXBPF",
    "name": ":fx_rbpf"
  },
  "FXRHPF": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "cutoff:": 100,
      "cutoff_slide:": 0,
      "cutoff_slide_curve:": 0,
      "cutoff_slide_shape:": 1,
      "mix:": 1,
      "mix_slide:": 0,
      "mix_slide_curve:": 0,
      "mix_slide_shape:": 1,
      "pre_amp:": 1,
      "pre_amp_slide:": 0,
      "pre_amp_slide_curve:": 0,
      "pre_amp_slide_shape:": 1,
      "pre_mix:": 1,
      "pre_mix_slide:": 0,
      "pre_mix_slide_curve:": 0,
      "pre_mix_slide_shape:": 1,
      "res:": 0.5,
      "res_slide:": 0,
      "res_slide_curve:": 0,
      "res_slide_shape:": 1
    },
    "descr": "Resonant High Pass Filter",
    "hiden": true,
    "inherit_arg": true,
    "inherit_base": "FXHPF",
    "name": ":fx_rhpf"
  },
  "FXRLPF": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "cutoff:": 100,
      "cutoff_slide:": 0,
      "cutoff_slide_curve:": 0,
      "cutoff_slide_shape:": 1,
      "mix:": 1,
      "mix_slide:": 0,
      "mix_slide_curve:": 0,
      "mix_slide_shape:": 1,
      "pre_amp:": 1,
      "pre_amp_slide:": 0,
      "pre_amp_slide_curve:": 0,
      "pre_amp_slide_shape:": 1,
      "pre_mix:": 1,
      "pre_mix_slide:": 0,
      "pre_mix_slide_curve:": 0,
      "pre_mix_slide_shape:": 1,
      "res:": 0.5,
      "res_slide:": 0,
      "res_slide_curve:": 0,
      "res_slide_shape:": 1
    },
    "descr": "Resonant Low Pass Filter",
    "hiden": true,
    "inherit_arg": true,
    "inherit_base": "FXLPF",
    "name": ":fx_rlpf"
  },
  "FXReverb": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "damp:": 0.5,
      "damp_slide:": 0,
      "damp_slide_curve:": 0,
      "damp_slide_shape:": 1,
      "mix:": 0.4,
      "mix_slide:": 0,
      "mix_slide_curve:": 0,
      "mix_slide_shape:": 1,
      "pre_amp:": 1,
      "pre_amp_slide:": 0,
      "pre_amp_slide_curve:": 0,
      "pre_amp_slide_shape:": 1,
      "pre_mix:": 1,
      "pre_mix_slide:": 0,
      "pre_mix_slide_curve:": 0,
      "pre_mix_slide_shape:": 1,
      "room:": 0.6,
      "room_slide:": 0,
      "room_slide_curve:": 0,
      "room_slide_shape:": 1
    },
    "descr": "Reverb",
    "hiden": false,
    "inherit_arg": true,
    "inherit_base": "FXInfo",
    "name": ":fx_reverb"
  },
  "FXRingMod": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "freq:": 30,
      "freq_slide:": 0,
      "freq_slide_curve:": 0,
      "freq_slide_shape:": 1,
      "mix:": 1,
      "mix_slide:": 0,
      "mix_slide_curve:": 0,
      "mix_slide_shape:": 1,
      "mod_amp:": 1,
      "mod_amp_slide:": 0,
      "mod_amp_slide_curve:": 0,
      "mod_amp_slide_shape:": 1,
      "pre_amp:": 1,
      "pre_amp_slide:": 0,
      "pre_amp_slide_curve:": 0,
      "pre_amp_slide_shape:": 1,
      "pre_mix:": 1,
      "pre_mix_slide:": 0,
      "pre_mix_slide_curve:": 0,
      "pre_mix_slide_shape:": 1
    },
    "descr": "Ring Modulator",
    "hiden": false,
    "inherit_arg": true,
    "inherit_base": "FXInfo",
    "name": ":fx_ring_mod"
  },
  "FXSlicer": {
    "arg_defaults": {
      "amp:": 1,
      "amp_max:": 1,
      "amp_max_slide:": 0,
      "amp_max_slide_curve:": 0,
      "amp_max_slide_shape:": 1,
      "amp_min:": 0,
      "amp_min_slide:": 0,
      "amp_min_slide_curve:": 0,
      "amp_min_slide_shape:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "invert_wave:": 0,
      "mix:": 1,
      "mix_slide:": 0,
      "mix_slide_curve:": 0,
      "mix_slide_shape:": 1,
      "phase:": 0.25,
      "phase_offset:": 0,
      "phase_slide:": 0,
      "phase_slide_curve:": 0,
      "phase_slide_shape:": 1,
      "pre_amp:": 1,
      "pre_amp_slide:": 0,
      "pre_amp_slide_curve:": 0,
      "pre_amp_slide_shape:": 1,
      "pre_mix:": 1,
      "pre_mix_slide:": 0,
      "pre_mix_slide_curve:": 0,
      "pre_mix_slide_shape:": 1,
      "prob_pos:": 0,
      "prob_pos_slide:": 0,
      "prob_pos_slide_curve:": 0,
      "prob_pos_slide_shape:": 1,
      "probability:": 0,
      "probability_slide:": 0,
      "probability_slide_curve:": 0,
      "probability_slide_shape:": 1,
      "pulse_width:": 0.5,
      "pulse_width_slide:": 0,
      "pulse_width_slide_curve:": 0,
      "pulse_width_slide_shape:": 1,
      "seed:": 0,
      "smooth:": 0,
      "smooth_down:": 0,
      "smooth_down_slide:": 0,
      "smooth_down_slide_curve:": 0,
      "smooth_down_slide_shape:": 1,
      "smooth_slide:": 0,
      "smooth_slide_curve:": 0,
      "smooth_slide_shape:": 1,
      "smooth_up:": 0,
      "smooth_up_slide:": 0,
      "smooth_up_slide_curve:": 0,
      "smooth_up_slide_shape:": 1,
      "wave:": 1
    },
    "descr": "Slicer",
    "hiden": false,
    "inherit_arg": true,
    "inherit_base": "FXInfo",
    "name": ":fx_slicer"
  },
  "FXTanh": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "krunch:": 5,
      "krunch_slide:": 0,
      "krunch_slide_curve:": 0,
      "krunch_slide_shape:": 1,
      "mix:": 1,
      "mix_slide:": 0,
      "mix_slide_curve:": 0,
      "mix_slide_shape:": 1,
      "pre_amp:": 1,
      "pre_amp_slide:": 0,
      "pre_amp_slide_curve:": 0,
      "pre_amp_slide_shape:": 1,
      "pre_mix:": 1,
      "pre_mix_slide:": 0,
      "pre_mix_slide_curve:": 0,
      "pre_mix_slide_shape:": 1
    },
    "descr": "Hyperbolic Tangent",
    "hiden": false,
    "inherit_arg": true,
    "inherit_base": "FXInfo",
    "name": ":fx_tanh"
  },
  "FXVowel": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "mix:": 1,
      "mix_slide:": 0,
      "mix_slide_curve:": 0,
      "mix_slide_shape:": 1,
      "pre_amp:": 1,
      "pre_amp_slide:": 0,
      "pre_amp_slide_curve:": 0,
      "pre_amp_slide_shape:": 1,
      "pre_mix:": 1,
      "pre_mix_slide:": 0,
      "pre_mix_slide_curve:": 0,
      "pre_mix_slide_shape:": 1,
      "voice:": 0,
      "vowel_sound:": 1
    },
    "descr": "Vowel",
    "hiden": false,
    "inherit_arg": true,
    "inherit_base": "FXInfo",
    "name": ":fx_vowel"
  },
  "FXWhammy": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "deltime:": 0.05,
      "grainsize:": 0.075,
      "max_delay_time:": 1,
      "mix:": 1,
      "mix_slide:": 0,
      "mix_slide_curve:": 0,
      "mix_slide_shape:": 1,
      "pre_amp:": 1,
      "pre_amp_slide:": 0,
      "pre_amp_slide_curve:": 0,
      "pre_amp_slide_shape:": 1,
      "pre_mix:": 1,
      "pre_mix_slide:": 0,
      "pre_mix_slide_curve:": 0,
      "pre_mix_slide_shape:": 1,
      "transpose:": 12,
      "transpose_slide:": 0,
      "transpose_slide_curve:": 0,
      "transpose_slide_shape:": 1
    },
    "descr": "Whammy",
    "hiden": false,
    "inherit_arg": true,
    "inherit_base": "FXInfo",
    "name": ":fx_whammy"
  },
  "FXWobble": {
    "arg_defaults": {
      "amp:": 1,
      "amp_slide:": 0,
      "amp_slide_curve:": 0,
      "amp_slide_shape:": 1,
      "cutoff_max:": 120,
      "cutoff_max_slide:": 0,
      "cutoff_max_slide_curve:": 0,
      "cutoff_max_slide_shape:": 1,
      "cutoff_min:": 60,
      "cutoff_min_slide:": 0,
      "cutoff_min_slide_curve:": 0,
      "cutoff_min_slide_shape:": 1,
      "filter:": 0,
      "invert_wave:": 0,
      "mix:": 1,
      "mix_slide:": 0,
      "mix_slide_curve:": 0,
      "mix_slide_shape:": 1,
      "phase:": 0.5,
      "phase_offset:": 0,
      "phase_slide:": 0,
      "phase_slide_curve:": 0,
      "phase_slide_shape:": 1,
      "pre_amp:": 1,
      "pre_amp_slide:": 0,
      "pre_amp_slide_curve:": 0,
      "pre_amp_slide_shape:": 1,
      "pre_mix:": 1,
      "pre_mix_slide:": 0,
      "pre_mix_slide_curve:": 0,
      "pre_mix_slide_shape:": 1,
      "prob_pos:": 0,
      "prob_pos_slide:": 0,
      "prob_pos_slide_curve:": 0,
      "prob_pos_slide_shape:": 1,
      "probability:": 0,
      "probability_slide:": 0,
      "probability_slide_curve:": 0,
      "probability_slide_shape:": 1,
      "pulse_width:": 0.5,
      "pulse_width_slide:": 0,
      "pulse_width_slide_curve:": 0,
      "pulse_width_slide_shape:": 1,
      "res:": 0.8,
      "res_slide:": 0,
      "res_slide_curve:": 0,
      "res_slide_shape:": 1,
      "seed:": 0,
      "smooth:": 0,
      "smooth_down:": 0,
      "smooth_down_slide:": 0,
      "smooth_down_slide_curve:": 0,
      "smooth_down_slide_shape:": 1,
      "smooth_slide:": 0,
      "smooth_slide_curve:": 0,
      "smooth_slide_shape:": 1,
      "smooth_up:": 0,
      "smooth_up_slide:": 0,
      "smooth_up_slide_curve:": 0,
      "smooth_up_slide_shape:": 1,
      "wave:": 0
    },
    "descr": "Wobble",
    "hiden": false,
    "inherit_arg": true,
    "inherit_base": "FXInfo",
    "name": ":fx_wobble"
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
  "Miscellaneous Sounds": [
    ":misc_burp",
    ":misc_crow",
    ":misc_cineboom"
  ],
  "Percussive Sounds": [
    ":perc_bell",
    ":perc_snap",
    ":perc_snap2",
    ":perc_swash",
    ":perc_till"
  ],
  "Snare Drums": [
    ":sn_dub",
    ":sn_dolf",
    ":sn_zome"
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
  "Vinyl sounds": [
    ":vinyl_backspin",
    ":vinyl_rewind",
    ":vinyl_scratch",
    ":vinyl_hiss"
  ]
}



def all_synth_names():
    for key, value in synths.items():
        if value['hiden'] != True and key != 'SoundIn' and value['name'] in synth_nodes:
            yield value['name']

all_synth = [ synths[synth_nodes[s]] for s in all_synth_names()]

def all_fx_names():
    for key, value in fx.items():
        if value['hiden'] != True and value['name'] in synth_nodes:
            yield value['name']

all_fx = [ fx[synth_nodes[s]] for s in all_fx_names()]

def all_sample_names():
    all = []
    for key, value in samples.items():
        yield all
        all += value

all_sample = [ s for s in all_sample_names()][0]

def sn(ref):
    c_name = synth_nodes[ref]
    if 'FX' in c_name:
        return fx[c_name]
    else:
        return synths[c_name]


if __name__ == '__main__':
    print("synth: ", len(all_synth))
    print("fx: ",len(all_fx))
    print("samples: ",len(all_sample))
    