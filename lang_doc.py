null = None; true = True; false = False;
#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/

funct_doc = {
  "rest": {
    "doc": "Given a note or an args map, returns true if it represents a rest and false if otherwise",
    "summary": "Determine if note or args is a rest",
    "examples": "puts rest? nil # true\nputs rest? :r # true\",\n\n        \"puts rest? :rest # true\",\n\n        \"puts rest? 60 # false\",\n\n        \"puts rest? {} # false\",\n\n        \"puts rest? {note: :rest} # true\",\n\n        \"puts rest? {note: nil} # true\",\n\n        \"puts rest? {note: 50} # false"
  },
  "on": {
    "doc": "Optionally evaluate the block depending on the truthiness of the supplied condition. The truthiness rules are as follows: all values are seen as true except for: false, nil and 0. Lambdas will be automatically called and the truthiness of their results used.",
    "summary": "Optionally evaluate block",
    "examples": "\n\non true do\n\n  play 70     #=> will play 70 as true is truthy\n\nend\",\n\n\"\n\non 1 do\n\n  play 70     #=> will play 70 as 1 is truthy\n\nend\",\n\n\"\n\non 0 do\n\n  play 70     #=> will *not* play 70 as 0 is not truthy\n\nend\",\n\n\"\n\non false do\n\n  play 70     #=> will *not* play 70 as false is not truthy\n\nend\",\n\n\"\n\non nil do\n\n  play 70     #=> will *not* play 70 as nil is not truthy\n\nend\",\n\n\"\n\non lambda{true} do\n\n  play 70     #=> will play 70 as the lambda returns a truthy value\n\nend\",\n\n\"\n\non lambda{false} do\n\n  play 70     #=> will *not* play 70 as the lambda does not return a truthy value\n\nend\",\n\n\"\n\non lambda{[true, false].choose} do\n\n  play 70     #=> will maybe play 70 depending on the choice in the lambda\n\nend"
  },
  "in_thread": {
    "doc": "Execute a given block (between `do` ... `end`) in a new thread. Use for playing multiple 'parts' at once. Each new thread created inherits all the use/with defaults of the parent thread such as the time, current synth, bpm, default synth args, etc. Despite inheriting defaults from the parent thread, any modifications of the defaults in the new thread will *not* affect the parent thread. Threads may be named with the `name:` optional arg. Named threads will print their name in the logging pane when they print their activity. If you attempt to create a new named thread with a name that is already in use by another executing thread, no new thread will be created.\nIt is possible to delay the initial trigger of the thread on creation with both the `delay:` and `sync:` opts. See their respective docstrings. If both `delay:` and `sync:` are specified, on initial thread creation first the delay will be honoured and then the sync.\n",
    "summary": "Run code block at the same time",
    "examples": "  loop do      # If you write two loops one after another like this,\n\n    play 50    # then only the first loop will execute as the loop acts\n\n    sleep 1    # like a trap not letting the flow of control out\n\n  end\n\n  loop do      # This code is never executed.\n\n    play 55\n\n    sleep 0.5\n\n  end \",\n\n  \"\n\n  # In order to play two loops at the same time, the first loops need to\n\n  # be in a thread (note that it's probably more idiomatic to use live_loop\n\n  # when performing):\n\n  # By wrapping our loop in an in_thread block, we split the\n\n  # control flow into two parts. One flows into the loop (a) and\n\n  # the other part flows immediately after the in_thread block (b).\n\n  # both parts of the control flow execute at exactly the same time.\n\n  in_thread do\n\n    # (a)\n\n    loop do\n\n      # (a)\n\n      play 50\n\n      sleep 1\n\n    end\n\n  end\n\n  # (b)\n\n  loop do      # This loop is executed thanks to the thread above\n\n    play 55\n\n    sleep 0.5\n\n  end\",\n\n  \"\n\n  use_bpm 120  # Set the bpm to be double rate\n\n  use_synth :dsaw  # Set the current synth to be :dsaw\n\n  in_thread do     # Create a new thread\n\n    play 50        # Play note 50 at time 0\n\n    use_synth :fm  # Switch to fm synth (only affects this thread)\n\n    sleep 1        # sleep for 0.5 seconds (as we're double rate)\n\n    play 38        # Play note 38 at time 0.5\n\n  end\n\n  play 62          # Play note 62 at time 0 (with dsaw synth)\n\n  sleep 2          # sleep 1s\n\n  play 67          # Play note 67 at time 1s (also with dsaw synth)\n\n  \",\n\n  \"\n\n  in_thread(name: :foo) do # Here we've created a named thread\n\n    loop do\n\n      sample :drum_bass_hard\n\n      sleep 1\n\n    end\n\n  end\n\n  in_thread(name: :foo) do # This thread isn't created as the name is\n\n    loop do                # the same as the previous thread which is\n\n      sample :elec_chime   # still executing.\n\n      sleep 0.5\n\n    end\n\n  end\",\n\n  \"\n\n   # Named threads work well with functions for live coding:\n\n  define :foo do  # Create a function foo\n\n    play 50       # which does something simple\n\n    sleep 1       # and sleeps for some time\n\n  end\n\n  in_thread(name: :main) do  # Create a named thread\n\n    loop do                  # which loops forever\n\n      foo                    # calling our function\n\n    end\n\n  end\n\n  # We are now free to modify the contents of :foo and re-run the entire buffer.\n\n  # We'll hear the effect immediately without having to stop and re-start the code.\n\n  # This is because our fn has been redefined, (which our thread will pick up) and\n\n  # due to the thread being named, the second re-run will not create a new similarly\n\n  # named thread. This is a nice pattern for live coding and is the basis of live_loop.\n\n  \",\n\n  \"\n\n  #Delaying the start of a thread\n\n  in_thread delay: 1 do\n\n    sample :ambi_lunar_land # this sample is not triggered at time 0 but after 1 beat\n\n  end\n\n  play 80                   # Note 80 is played at time 0\n\n  "
  },
  "set_control_delta": {
    "doc": "Specify how many seconds between successive modifications (i.e. trigger then controls) of a specific node on a specific thread. Set larger if you are missing control messages sent extremely close together in time.",
    "summary": "Set control delta globally",
    "examples": "\n\nset_control_delta! 0.1                 # Set control delta to 0.1\n\ns = play 70, release: 8, note_slide: 8 # Play a note and set the slide time\n\ncontrol s, note: 82                    # immediately start sliding note.\n\n                                       # This control message might not be\n\n                                       # correctly handled as it is sent at the\n\n                                       # same virtual time as the trigger.\n\n                                       # If you don't hear a slide, try increasing the\n\n                                       # control delta until you do."
  },
  "beat": {
    "doc": "Returns the beat value for the current thread/live_loop. Beats are advanced only by calls to `sleep` and `sync`. Beats are distinct from virtual time (the value obtained by calling `vt`) in that it has no notion of rate. It is just essentially a counter for sleeps. After a `sync`, the beat is overridden with the beat value from the thread which called `cue`.",
    "summary": "Get current beat",
    "examples": "  use_bpm 120  # The current BPM makes no difference\n\n  puts beat    #=> 0\n\n  sleep 1\n\n  puts beat    #=> 1\n\n  use_bpm 2000\n\n  sleep 2\n\n  puts beat    #=> 3"
  },
  "run_code": {
    "doc": "Executes the code passed as a string in a new Run. This works as if the code was in a buffer and Run button was pressed.",
    "summary": "Evaluate the code passed as a String as a new Run",
    "examples": "run_code \\\"sample :ambi_lunar_land\\\" #=> will play the :ambi_lunar_land sample\",\n\n        \"# Works with any amount of code:\n\nrun_code \\\"8.times do\\nplay 60\\nsleep 1\\nend # will play 60 8 times"
  },
  "current_random_seed": {
    "doc": "Returns the current random seed.\nThis can be set via the fns `use_random_seed` and `with_random_seed`. It is incremented every time you use the random number generator via fns such as `choose` and `rand`.",
    "summary": "Get current random seed",
    "examples": "  puts current_random_seed # Print out the current random seed\",\n\n\"\n\n## Resetting the seed back to a known place\n\nputs rand               #=>  0.75006103515625\n\nputs rand               #=>  0.733917236328125\n\na = current_random_seed # Grab the current seed\n\nputs rand               #=> 0.464202880859375\n\nputs rand               #=> 0.24249267578125\n\nuse_random_seed a       # Restore the seed\n\n                        # we'll now get the same random values:\n\nputs rand               #=> 0.464202880859375\n\nputs rand               #=> 0.24249267578125\n\n"
  },
  "with_transpose": {
    "doc": "Similar to use_transpose except only applies to code within supplied `do`/`end` block. Previous transpose value is restored after block. To transpose entire octaves see `with_octave`.",
    "summary": "Block-level note transposition",
    "examples": "use_transpose 3\n\nplay 62 # Plays note 65\n\nwith_transpose 12 do\n\n  play 50 # Plays note 62\n\n  sleep 1\n\n  play 72 # Plays note 84\n\nend\n\n# Original transpose value is restored\n\nplay 80 # Plays note 83\n\n"
  },
  "bt": {
    "doc": "Beat time representation. Scales the time to the current BPM. Useful for adding bpm scaling",
    "summary": "Beat time conversion",
    "examples": "  use_bpm 120  # Set the BPM to be double the default\n\n  puts bt(1) # 0.5\n\n  use_bpm 60   # BPM is now default\n\n  puts bt(1) # 1\n\n  use_bpm 30   # BPM is now half the default\n\n  puts bt(1) # 2\n\n"
  },
  "rand_skip": {
    "doc": "Jump the random generator forward essentially skipping the next call to `rand`. You may specify an amount to jump allowing you to skip n calls to `rand`.",
    "summary": "Jump forward random generator",
    "examples": "  # Basic rand stream skip\n\n  puts rand # prints 0.75006103515625\n\n  rand_skip # jump random stream forward one\n\n            # typically the next rand is 0.733917236328125\n\n  puts rand # prints 0.464202880859375\",\n\n  \"\n\n  # Jumping forward multiple places in the rand stream\n\n  puts rand # prints 0.75006103515625\n\n  puts rand # prints 0.733917236328125\n\n  puts rand # prints 0.464202880859375\n\n  puts rand # prints 0.24249267578125\n\n  rand_reset  # reset the random stream\n\n  puts rand # prints 0.75006103515625\n\n  rand_skip(2) # jump random stream forward three places\n\n               # the result of the next call to rand will be\n\n               # exactly the same as if rand had been called\n\n               # three times\n\n  puts rand 0.24249267578125"
  },
  "use_synth": {
    "doc": "Switch the current synth to `synth_name`. Affects all further calls to `play`. See `with_synth` for changing the current synth only for a specific `do`/`end` block.",
    "summary": "Switch current synth",
    "examples": "play 50 # Plays with default synth\n\nuse_synth :mod_sine\n\nplay 50 # Plays with mod_sine synth"
  },
  "chord_names": {
    "doc": "Returns a ring containing all chord names known to Sonic Pi",
    "summary": "All chord names",
    "examples": "puts chord_names #=>  prints a list of all the chords"
  },
  "use_sample_bpm": {
    "doc": "Modify bpm so that sleeping for 1 will sleep for the duration of the sample.",
    "summary": "Sample-duration-based bpm modification",
    "examples": "use_sample_bpm :loop_amen  #Set bpm based on :loop_amen durationlive_loop :dnb do\n\n  sample :bass_dnb_f\n\n  sample :loop_amen\n\n  sleep 1                  #`sleep`ing for 1 actually sleeps for duration of :loop_amen\n\nend\",\n\n        \"\n\nuse_sample_bpm :loop_amen, num_beats: 4  # Set bpm based on :loop_amen duration\n\n                                         # but also specify that the sample duration\n\n                                         # is actually 4 beats long.\n\nlive_loop :dnb do\n\n  sample :bass_dnb_f\n\n  sample :loop_amen\n\n  sleep 4                  #`sleep`ing for 4 actually sleeps for duration of :loop_amen\n\n                           # as we specified that the sample consisted of\n\n                           # 4 beats\n\nend"
  },
  "use_cue_logging": {
    "doc": "Enable or disable log messages created on cues. This does not disable the cues themselves, it just stops them from being printed to the log",
    "summary": "Enable and disable cue logging",
    "examples": "use_cue_logging true # Turn on cue messages\nuse_cue_logging false # Disable cue messages"
  },
  "time_shift": {
    "doc": "The code within the given block is executed with the specified delta time shift specified in beats. For example, if the delta value is 0.1 then all code within the block is executed with a 0.1 beat delay. Negative values are allowed which means you can move a block of code *backwards in time*. For example a delta value of -0.1 will execute the code in the block 0.1 beats ahead of time. Normal time is restored after the execution of the block.\nNote that the the block is executed synchronously, so all sleeps within the block will be accounted for.\nAlso, note that the abs of the delta value must be less than the `sched_ahead_time!`.",
    "summary": "Slide time forwards or backwards for the given block",
    "examples": "# shift forwards in timeplay 70            #=> plays at time 0\n\nsleep 1\n\nplay 75            #=> plays at time 1\n\ntime_shift 0.1 do\n\n                   # time shifts forward by 0.1 beats\n\n  play 80          #=> plays at 1.1\n\n  sleep 0.5\n\n  play 80          #=> plays at 1.6\n\n                   # time shifts back by 0.1 beats\n\n                   # however, the sleep 0.5 is still accounted for\n\nend\n\n                   # we now honour the original sleep 1 and the\n\n                   # sleep 0.5 within the time_shift block, but\n\n                   # any time shift delta has been removed\n\nplay 70            #=> plays at 1.5\",\n\n        \"# shift backwards in time\n\nplay 70            #=> plays at time 0\n\nsleep 1\n\nplay 75            #=> plays at time 1\n\ntime_shift -0.1 do\n\n                   # time shifts backwards by 0.1 beats\n\n  play 80          #=> plays at 0.9\n\n  sleep 0.5\n\n  play 80          #=> plays at 1.4\n\n                   # time shifts forward by 0.1 beats\n\n                   # however, the sleep 0.5 is still accounted for\n\nend\n\n                   # we now honour the original sleep 1 and the\n\n                   # sleep 0.5 within the time_shift block, but\n\n                   # any time shift delta has been removed\n\nplay 70            #=> plays at 1.5"
  },
  "play_pattern": {
    "doc": "Play list of notes with the current synth one after another with a sleep of 1\nAccepts optional args for modification of the synth being played. See each synth's documentation for synth-specific opts. See use_synth and with_synth for changing the current synth.",
    "summary": "Play pattern of notes",
    "examples": "play_pattern [40, 41, 42] # Same as:\n\n                          #   play 40\n\n                          #   sleep 1\n\n                          #   play 41\n\n                          #   sleep 1\n\n                          #   play 42\n\n\",\n\n        \"play_pattern [:d3, :c1, :Eb5] # You can use keyword notes\",\n\n        \"play_pattern [:d3, :c1, :Eb5], amp: 0.5, cutoff: 90 # Supports the same arguments as play:"
  },
  "define": {},
  "load_buffer": {
    "doc": "Given a path to a file, will read the contents and load it into the current buffer. This will replace any previous content.",
    "summary": "Load the contents of a file to the current buffer",
    "examples": "load_buffer \\\"~/sonic-pi-tracks/phat-beats.rb\\\" # will replace content of current buffer with contents of the file"
  },
  "rand_i_look": {
    "doc": "Given a max number, produces a whole number between `0` and the supplied max value exclusively. If max is a range produces an int within the range. With no args returns either `0` or `1`.\nDoes not consume a random value from the stream. Therefore, multiple sequential calls to `rand_i_look` will all return the same value.",
    "summary": "Generate a random whole number without consuming a rand",
    "examples": "print rand_i_look(5) #=> will print either 0, 1, 2, 3, or 4 to the output pane\",\n\n        \"\n\nprint rand_i_look(5) #=> will print either 0, 1, 2, 3, or 4 to the output pane\n\nprint rand_i_look(5) #=> will print the same number again\n\nprint rand_i_look(5) #=> will print the same number again\n\nprint rand_i(5) #=> will print either 0, 1, 2, 3, or 4 to the output pane\n\nprint rand_i_look(5) #=> will print the same number as the previous statement"
  },
  "shuffle": {
    "doc": "Returns a new list with the same elements as the original but with their order shuffled. Also works for strings",
    "summary": "Randomise order of a list",
    "examples": "\n\n  shuffle [1, 2, 3, 4] #=> Would return something like: [3, 4, 2, 1] \",\n\n        \"\n\n  shuffle \\\"foobar\\\"  #=> Would return something like: \\\"roobfa\\\""
  },
  "with_bpm_mul": {
    "doc": "Sets the tempo in bpm (beats per minute) for everything in the given block as a multiplication of the current tempo. Affects all containing calls to `sleep` and all temporal synth arguments which will be scaled to match the new bpm. See also `with_bpm`",
    "summary": "Set new tempo as a multiple of current tempo for block",
    "examples": "  use_bpm 60   # Set the BPM to 60\n\n  play 50\n\n  sleep 1      # Sleeps for 1 second\n\n  play 62\n\n  sleep 2      # Sleeps for 2 seconds\n\n  with_bpm_mul 0.5 do # BPM is now (60 * 0.5) == 30\n\n    play 50\n\n    sleep 1           # Sleeps for 2 seconds\n\n    play 62\n\n  end\n\n  sleep 1            # BPM is now back to 60, therefore sleep is 1 second\n\n  "
  },
  "run_file": {
    "doc": "Reads the full contents of the file with `path` and executes it in a new Run. This works as if the code in the file was in a buffer and Run button was pressed.",
    "summary": "Evaluate the contents of the file as a new Run",
    "examples": "run_file \\\"~/path/to/sonic-pi-code.rb\\\" #=> will run the contents of this file"
  },
  "doubles": {
    "doc": "Create a ring containing the results of successive doubling of the `start` value. If `num_doubles` is negative, will return a ring of `halves`.",
    "summary": "Create a ring of successive doubles",
    "examples": "(doubles 60, 2)  #=> (ring 60, 120)\",\n\n        \"(doubles 1.5, 3) #=> (ring 1.5, 3, 6)\",\n\n        \"(doubles 1.5, 5) #=> (ring 1.5, 3, 6, 12, 24)\",\n\n        \"(doubles 100, -4) #=> (ring 100, 50, 25, 12.5)"
  },
  "current_beat_duration": {
    "doc": "Get the duration of the current beat in seconds. This is the actual length of time which will elapse with `sleep 1`.\nAffected by calls to `use_bpm`, `with_bpm`, `use_sample_bpm` and `with_sample_bpm`.",
    "summary": "Duration of current beat",
    "examples": "  use_bpm 60\n\n  puts current_beat_duration #=> 1\n\n  use_bpm 120\n\n  puts current_beat_duration #=> 0.5"
  },
  "note_range": {
    "doc": "Produces a ring of all the notes between a low note and a high note. By default this is chromatic (all the notes) but can be filtered with a pitches: argument. This opens the door to arpeggiator style sequences and other useful patterns. If you try to specify only pitches which aren't in the range it will raise an error - you have been warned!",
    "summary": "Get a range of notes",
    "examples": "(note_range :c4, :c5) # => (ring 60,61,62,63,64,65,66,67,68,69,70,71,72)\",\n\n        \"(note_range :c4, :c5, pitches: (chord :c, :major)) # => (ring 60,64,67,72)\",\n\n        \"(note_range :c4, :c6, pitches: (chord :c, :major)) # => (ring 60,64,67,72,76,79,84)\",\n\n        \"(note_range :c4, :c5, pitches: (scale :c, :major)) # => (ring 60,62,64,65,67,69,71,72)\",\n\n        \"(note_range :c4, :c5, pitches: [:c4, :g2]) # => (ring 60,67,72)\",\n\n        \"live_loop :arpeggiator do\n\n  # try changing the chord\n\n  play (note_range :c4, :c5, pitches: (chord :c, :major)).tick\n\n  sleep 0.125\n\nend"
  },
  "with_random_seed": {
    "doc": "Resets the random number generator to the specified seed for the specified code block. All generated random numbers and randomisation functions such as `shuffle` and `choose` within the code block will use this new generator. Once the code block has completed, the original generator is restored and the code block generator is discarded. Use this to change the sequence of random numbers in your piece in a way that can be reproduced. Especially useful if combined with iteration. See examples.",
    "summary": "Specify random seed for code block",
    "examples": "  use_random_seed 1 # reset random seed to 1\n\n  puts rand # => 0.417022004702574\n\n  puts rand  #=> 0.7203244934421581\n\n  use_random_seed 1 # reset it back to 1\n\n  puts rand # => 0.417022004702574\n\n  with_random_seed 1 do # reset seed back to 1 just for this block\n\n    puts rand # => 0.417022004702574\n\n    puts rand #=> 0.7203244934421581\n\n  end\n\n  puts rand # => 0.7203244934421581\n\n            # notice how the original generator is restored\",\n\n  \"\n\n  ## Generating melodies\n\n  notes = (scale :eb3, :minor_pentatonic, num_octaves: 2)  # Create a set of notes to choose from.\n\n                                           # Scales work well for this\n\n  with_fx :reverb do\n\n    live_loop :repeating_melody do         # Create a live loop\n\n      with_random_seed 300 do              # Set the random seed to a known value every\n\n                                           # time around the loop. This seed is the key\n\n                                           # to our melody. Try changing the number to\n\n                                           # something else. Different numbers produce\n\n                                           # different melodies\n\n        8.times do                         # Now iterate a number of times. The size of\n\n                                           # the iteration will be the length of the\n\n                                           # repeating melody.\n\n          play notes.choose, release: 0.1  # 'Randomly' choose a note from our ring of\n\n                                           # notes. See how this isn't actually random\n\n                                           # but uses a reproducible method! These notes\n\n                                           # are therefore repeated over and over...\n\n          sleep 0.125\n\n        end\n\n      end\n\n      play notes.choose, amp: 1.5, release: 0.5 # Note that this line is outside of\n\n                                                # the with_random_seed block and therefore\n\n                                                # the randomisation never gets reset and this\n\n                                                # part of the melody never repeats.\n\n    end\n\n  end\n\n  "
  },
  "range": {
    "doc": "Create a new ring buffer from the range arguments (start, finish and step size). Step size defaults to `1`. Indexes wrap around positively and negatively",
    "summary": "Create a ring buffer with the specified start, finish and step size",
    "examples": "(range 1, 5)    #=> (ring 1, 2, 3, 4)\",\n\n        \"(range 1, 5, inclusive: true) #=> (ring 1, 2, 3, 4, 5)\",\n\n        \"(range 1, 5, step: 2) #=> (ring 1, 3)\",\n\n        \"(range 1, -5, step: 2) #=> (ring 1, -1, -3)\",\n\n        \"(range 1, -5, step: 2)[-1] #=> -3"
  },
  "rand_i": {
    "doc": "Given a max number, produces a whole number between `0` and the supplied max value exclusively. If max is a range produces an int within the range. With no args returns either `0` or `1`",
    "summary": "Generate a random whole number below a value (exclusive)",
    "examples": "  print rand_i(5) #=> will print either 0, 1, 2, 3, or 4 to the output pane"
  },
  "rdist": {
    "doc": "Returns a random number within the range with width around centre. If optional arg `step:` is used, the result is quantised by step.",
    "summary": "Random number in centred distribution",
    "examples": "\n\n  print rdist(1, 0) #=> will print a number between -1 and 1\n\n  \",\n\n  \"\n\n  print rdist(1) #=> centre defaults to 0 so this is the same as rdist(1, 0)\n\n  \",\n\n  \"\n\n  loop do\n\n    play :c3, pan: rdist(1) #=> Will play :c3 with random L/R panning\n\n    sleep 0.125\n\n  end"
  },
  "sample": {
    "doc": "Play back a recorded sound file (sample). Sonic Pi comes with lots of great samples included (see the section under help) but you can also load and play `.wav`, `.wave`, `.aif`, `.aiff` or `.flac` files from anywhere on your computer too. To play a built-in sample use the corresponding keyword such as `sample :bd_haus`. To play any file on your computer use a full path such as `sample \\\"/path/to/sample.wav\\\"`.\nThere are many opts for manipulating the playback. For example, the `rate:` opt affects both the speed and the pitch of the playback. To control the rate of the sample in a pitch-meaningful way take a look at the `rpitch:` opt.\nThe sampler synth has three separate envelopes - one for amplitude, one for a low pass filter and another for a high pass filter. These work very similar to the standard synth envelopes except for two major differences. Firstly, the envelope times do not stretch or shrink to match the BPM. Secondly, the sustain time by default stretches to make the envelope fit the length of the sample. This is explained in detail in the tutorial.\nSamples are loaded on-the-fly when first requested (and subsequently remembered). If the sample loading process takes longer than the schedule ahead time, the sample trigger will be skipped rather than be played late and out of time. To avoid this you may preload any samples you wish to work with using `load_sample` or `load_samples`.\nIt is possible to set the `start:` and `finish:` positions within the sample to play only a sub-section of it. These values can be automatically chosen based on an onset detection algorithm which will essentially isolate each individual drum or synth hit in the sample and let you access each one by an integer index. See the `onset:` docstring and examples for more information.\nFinally, the sampler supports a powerful filtering system to make it easier to work with large folders of samples. The filter commands must be used before the first standard opt. There are six kinds of filter parameters you may use:\n1. Folder strings - `\\\"/foo/bar\\\"` - which will add all samples within the folder to the set of candidates.\n2. Recursive folder strings - `\\\"/foo/bar/**\\\"` - Folder strings ending with `**` will add all samples contained within all subfolders (searched recursively).\n3. Sample strings - `\\\"/path/to/sample.wav\\\"` - which will add the specific sample to the set of candidates.\n4. Other strings - `\\\"foobar\\\"` - which will filter the candidates based on whether the filename contains the string.\n5. Regular expressions - `/b[aA]z.*/` - which will filter the candidates based on whether the regular expression matches the filename.\n6. Keywords - `:quux` - will filter the candidates based on whether the keyword is a direct match of the filename (without extension).\n7. Numbers - `0` - will select the candidate with that index (wrapping round like a ring if necessary).\n8. Lists of the above - `[\\\"/foo/bar\\\", \\\"baz\\\", /0-9.*/]` - will recurse down and work through the internal filter parameters as if they were in the top level.\n9. Lambdas - `lambda {|s| [s.choose] } - the ultimate power tool for filters. Allows you to create a custom fn which receives a list of candidates as an arg and which should return a new list of candidates (this may be smaller, larger, re-ordered it's up to you).\nBy combining commands which add to the candidates and then filtering those candidates it is possible to work with folders full of samples in very powerful ways. Note that the specific ordering of filter parameters is irrelevant with the exception of the numbers - in which case the last number is the index. All the candidates will be gathered first before the filters are applied.\n",
    "summary": "Trigger sample",
    "examples": "# Play a built-in sample\n\nsample :loop_amen # Plays the Amen break\",\n\n        \"\n\n# Play two samples at the same time\n\n# with incredible timing accuracy\n\nsample :loop_amen\n\nsample :ambi_lunar_land # Note, for timing guarantees select the pref:\n\n                        #   Studio -> Synths and FX -> Enforce timing guarantees\",\n\n        \"\n\n# Create a simple repeating bass drum\n\nlive_loop :bass do\n\n  sample :bd_haus\n\n  sleep 0.5\n\nend\",\n\n        \"\n\n# Create a more complex rhythm with multiple live loops:\n\nlive_loop :rhythm do\n\n  sample :tabla_ghe3 if (spread 5, 7).tick\n\n  sleep 0.125\n\nend\n\nlive_loop :bd, sync: :rhythm do\n\n  sample :bd_haus, lpf: 90, amp: 2\n\n  sleep 0.5\n\nend\",\n\n        \"\n\n# Change the playback speed of the sample using rate:\n\nsample :loop_amen, rate: 0.5 # Play the Amen break at half speed\n\n                             # for old school hip-hop\",\n\n        \"\n\n# Speed things up\n\nsample :loop_amen, rate: 1.5 # Play the Amen break at 1.5x speed\n\n                             # for a jungle/gabba sound\",\n\n        \"\n\n# Go backwards\n\nsample :loop_amen, rate: -1 # Negative rates play the sample backwards\",\n\n        \"\n\n# Fast rewind\n\nsample :loop_amen, rate: -3 # Play backwards at 3x speed for a fast rewind effect\",\n\n        \"\n\n# Start mid sample\n\nsample :loop_amen, start: 0.5 # Start playback half way through\",\n\n        \"\n\n# Finish mid sample\n\nsample :loop_amen, finish: 0.5 # Finish playback half way through\",\n\n        \"\n\n# Play part of a sample\n\nsample :loop_amen, start: 0.125, finish: 0.25 # Play the second eighth of the sample\",\n\n        \"\n\n# Finishing before the start plays backwards\n\nsample :loop_amen, start: 0.25, finish: 0.125 # Play the second eighth of the sample backwards\",\n\n        \"\n\n# Play a section of a sample at quarter speed backwards\n\nsample :loop_amen, start: 0.125, finish: 0.25, rate: -0.25 # Play the second eighth of the\n\n                                                           # amen break backwards at a\n\n                                                           # quarter speed\",\n\n        \"\n\n# Control a sample synchronously\n\ns = sample :loop_amen, lpf: 70\n\nsleep 0.5\n\ncontrol s, lpf: 130\n\nsleep 0.5\n\nsynth :dsaw, note: :e3 # This is triggered 1s from start\",\n\n\" # Controlling a sample asynchronously\n\nsample :loop_amen, lpf: 70 do |s|\n\n  sleep 1                                # This block is run in an implicit in_thread\n\n  control s, lpf: 130                    # and therefore is asynchronous\n\nend\n\nsleep 0.5\n\nsynth :dsaw, note: :e3 # This is triggered 0.5s from start\",\n\n        \"\n\n# Play with slices\n\nsample :loop_garzul, slice: 0      # => play the first 16th of the sample\n\nsleep 0.5\n\n4.times do\n\n  sample :loop_garzul, slice: 1    # => play the second 16th of the sample 4 times\n\n  sleep 0.125\n\nend\n\nsample :loop_garzul, slice: 4, num_slices: 4, rate: -1      # => play the final quarter backwards\n\n\",\n\n        \"\n\n# Build a simple beat slicer\n\nuse_sample_bpm :loop_amen                    # Set the BPM to match the amen break sample\n\nlive_loop :beat_slicer do\n\n  n = 8                                      # Specify number of slices\n\n                                             # (try changing to 2, 4, 6, 16 or 32)\n\n  s = rand_i n                               # Choose a random slice within range\n\n  sample :loop_amen, slice: s, num_slices: n # Play the specific part of the sample\n\n  sleep 1.0/n                                # Sleep for the duration of the slice\n\nend\",\n\n        \"\n\n# Play with the built-in low pass filter, high pass filter and compressor\n\nsample :loop_amen, lpf: 80, hpf: 70, compress: 1, pre_amp: 10 # Make the amen break sound punchy.\",\n\n        \"\n\n# Use the cutoff filter envelopes\n\nsample :loop_garzul, lpf_attack: 8 # Sweep the low pass filter up over 8 beats\n\nsleep 8\n\nsample :loop_garzul, hpf_attack: 8 # Sweep the high pass filter down over 8 beats\",\n\n        \"\n\n# Sample stretching\n\nputs sample_duration :loop_industrial                   # => 0.88347\n\nputs sample_duration :loop_industrial, beat_stretch: 1  # => 1\n\nlive_loop :industrial do\n\n  sample :loop_industrial, beat_stretch: 1              # Stretch the sample to make it 1 beat long\n\n  sleep 1                                               # This now loops perfectly.\n\n                                                        # However, note that stretching/shrinking\n\n                                                        # also modifies the pitch.\n\nend\",\n\n        \"\n\n# Sample shrinking\n\nputs sample_duration :loop_garzul                       # => 8\n\nputs sample_duration :loop_garzul, beat_stretch: 6      # => 6\n\nlive_loop :garzul do\n\n  sample :loop_garzul, beat_stretch: 6                  # As :loop_garzul is longer than 6 beats\n\n                                                        # it is shrunk to fit. This increases the\n\n                                                        # pitch.\n\n  sleep 6\n\nend\",\n\n        \"\n\n# Sample stretching matches the BPM\n\nuse_bpm 30                                              # Set the BPM to 30\n\nputs sample_duration :loop_garzul                       # => 4.0 (at 30 BPM the sample lasts for 4 beats)\n\nputs sample_duration :loop_garzul, beat_stretch: 6      # => 6.0\n\nlive_loop :garzul do\n\n  sample :loop_garzul, beat_stretch: 6                  # The sample is stretched to match 6 beats at 30 BPM\n\n  sleep 6\n\nend\",\n\n        \"\n\n# External samples\n\nsample \\\"/path/to/sample.wav\\\"                          # Play any Wav, Aif or FLAC sample on your computer\n\n                                                        # by simply passing a string representing the full\n\n                                                        # path\",\n\n        \"\n\n# Sample pack filtering\n\ndir = \\\"/path/to/dir/of/samples\\\"                       # You can easily work with a directory of samples\n\nsample dir                                              # Play the first sample in the directory\n\n                                                        # (it is sorted alphabetically)\n\nsample dir, 1                                           # Play the second sample in the directory\n\nsample dir, 99                                          # Play the 100th sample in the directory, or if there\n\n                                                        # are fewer, treat the directory like a ring and keep\n\n                                                        # wrapping the index round until a sample is found.\n\n                                                        # For example, if there are 90 samples, the 10th sample\n\n                                                        # is played (index 9).\n\nsample dir, \\\"120\\\"                                     # Play the first sample in the directory that contains\n\n                                                        # the substring \\\"120\\\".\n\n                                                        # For example, this may be \\\"beat1_120_rave.wav\\\"\n\nsample dir, \\\"120\\\", 1                                  # Play the second sample in the directory that contains\n\n                                                        # the substring \\\"120\\\".\n\n                                                        # For example, this may be \\\"beat2_120_rave.wav\\\"\n\nsample dir, /beat[0-9]/                                 # Play the first sample in the directory that matches\n\n                                                        # the regular expression /beat[0-9]/.\n\n                                                        # For example, this may be \\\"beat0_100_trance.wav\\\"\n\n                                                        # You may use the full power of Ruby's regular expression\n\n                                                        # system here: http://ruby-doc.org/core-2.1.1/Regexp.html\n\nsample dir, /beat[0-9]0/, \\\"100\\\"                       # Play the first sample in the directory that both matches\n\n                                                        # the regular expression /beat[0-9]0/ and contains the\n\n                                                        # the substring \\\"100\\\".\n\n                                                        # For example, this may be \\\"beat10_100_rave.wav\\\"\",\n\n        \"\n\n# Filtering built-in samples\n\n                                                        # If you don't pass a directory source, you can filter over\n\n                                                        # the built-in samples.\n\nsample \\\"tabla_\\\"                                       # Play the first built-in sample that contains the substring\n\n                                                        # \\\"tabla\\\"\n\nsample \\\"tabla_\\\", 2                                    # Play the third built-in sample that contains the substring\n\n                                                        # \\\"tabla\\\"\",\n\n        \"\n\n# Play with whole directories of samples\n\nload_samples \\\"tabla_\\\"                                 # You may pass any of the source/filter options to load_samples\n\n                                                        # to load all matching samples. This will load all the built-in\n\n                                                        # samples containing the substring \\\"tabla_\\\"\n\nlive_loop :tabla do\n\n  sample \\\"tabla_\\\", tick                               # Treat the matching samples as a ring and tick through them\n\n  sleep 0.125\n\nend\",\n\n        \"\n\n# Specify multiple sources\n\ndir1 = \\\"/path/to/sample/directory\\\"\n\ndir2 = \\\"/path/to/other/sample/directory\\\"\n\nsample dir1, dir2, \\\"foo\\\"                              # Match the first sample that contains the string \\\"foo\\\" out of\n\n                                                        # all the samples in dir1 and dir2 combined.\n\n                                                        # Note that the sources must be listed before any filters.\",\n\n        \"\n\n# List contents recursively\n\ndir = \\\"/path/to/sample/directory\\\"                     # By default the list of all top-level samples within the directory\n\n                                                        # is considered.\n\ndir_recursive = \\\"/path/to/sample/directory/**\\\"        # However, if you finish your directory string with ** then if that\n\n                                                        # directory contains other directories then the samples within the\n\n                                                        # subdirectories and their subsubdirectories in turn are considered.\n\nsample dir, 0                                           # Play the first top-level sample in the directory\n\nsample dir_recursive, 0                                 # Play the first sample found after combining all samples found in\n\n                                                        # the directory and all directories within it recursively.\n\n                                                        # Note that if there are many sub directories this may take some time\n\n                                                        # to execute. However, the result is cached so subsequent calls will\n\n                                                        # be fast.\",\n\n        \"\n\n# Bespoke filters\n\nfilter = lambda do |candidates|                         # If the built-in String, Regexp and index filters are not sufficient\n\n  [candidates.choose]                                   # you may write your own. They need to be a function which takes a list\n\nend                                                     # of paths to samples and return a list of samples. This one returns a\n\n                                                        # list of a single randomly selected sample.\n\n8.times do\n\n  sample \\\"drum_\\\", filter                              # Play 8 randomly selected samples from the built-in sample set that also\n\n  sleep 0.25                                            # contain the substring \\\"drum_\\\"\n\nend\",\n\n        \"\n\n# Basic Onset Detection\n\nsample :loop_tabla, start: 0, finish: 0.00763           # If you know the right start: and finish: values, you can extract a\n\n                                                        # single drum hit from a longer sample. However, finding these values\n\n                                                        # can be very time consuming.\n\nsleep 1\n\n                                                        # Instead of specifying the start: and finish: values manually you can\n\n                                                        # use the onset: option to find them for you using an integer index.\n\nsample :loop_tabla, onset: 0                            # onset: 0 will set the start: and finish: values so that the first\n\n                                                        # percussive sound (something that shifts from quiet to loud quickly)\n\n                                                        # is picked out.\n\nsleep 1\n\nsample :loop_tabla, onset: 1                            # We can easily find the second percussive sound in the sample with\n\n                                                        # onset: 1\",\n\n        \"\n\n# Ticking through onsets\n\n                                                        # The onsets are actually a ring so the index will wrap around. This\n\n                                                        # means that if there are only 8 onsets in a sample, specifying an\n\n                                                        # onset of 100 will still return one of the 8 onsets. This means we\n\n                                                        # can use tick to work through each onset in sequence. This allows us\n\n                                                        # to redefine the rhythm and tempo of a sample\n\nlive_loop :tabla do\n\n  use_bpm 50                                            # We can choose our own BPM here - it doesn't need to match the sample\n\n  sample :loop_tabla, onset: tick                       # tick through each onset in sequence\n\n  sleep [0.125, 0.25].choose                            # randomly choose a delay between onset triggers\n\nend\n\n\",\n\n        \"\n\n# Random Onset Triggering\n\n                                                        # We can easily pick a random onset using the pick fn\n\nuse_bpm 50\n\nlive_loop :tabla do\n\n  sample :loop_tabla, onset: pick                       # Each time round the live loop we now trigger a random onset\n\n  sleep [0.125, 0.25].choose                            # creating an infinite stream of randomly selected drums\n\nend\n\n        \",\n\n        \"\n\n# Repeatable Random Onsets\n\n                                                        # Instead of an infinite stream of choices, we can combine iteration\n\n                                                        # and use_random_seed to create repeatable riffs:\n\nlive_loop :tabla do\n\n  use_random_seed 30000                                 # every 8 times, reset the random seed, this resets the riff\n\n  8.times do\n\n    sample :loop_tabla, onset: pick\n\n    sleep [0.125, 0.25].choose\n\n  end\n\nend\n\n\",\n\n        \"\n\n#  Random Onset Duration\n\n                                                            # Each onset has a variable length (determined by the sample contents).\n\n                                                            # Therefore, if you wish to ensure each onset has a specific length it\n\n                                                            # is necessary to use the sample's amplitude envelope.\n\n                                                            # As the sample's envelope automatically changes the sustain: value to\n\n                                                            # match the duration - you also need to override this with a value of 0.\n\nlive_loop :tabla do\n\n  sample :loop_tabla, onset: pick, sustain: 0, release: 0.1 # Each drum onset will now be no longer than 0.1. Note that the envelope\n\n                                                            # for a sample only determines the maximum duration of a sample trigger.\n\n                                                            # If the actual audible duration of the onset is smaller than 0.1 then\n\n                                                            # it will *not* be extended.\n\n  sleep [0.125, 0.25].choose\n\nend\n\n\",\n\n        \"\n\n# Onset lambdas\n\n                                                        # The onset index can be a lambda as well as an integer. If a lambda is\n\n                                                        # given, it will be passed a ring of all of the onsets as an argument.\n\n                                                        # This will be a ring of maps:\n\nl = lambda {|c| puts c ; c[0]}                          # define a lambda which accepts a single argument, prints it and\n\n                                                        # returns the first value. This particular example is essentially\n\n                                                        # the same as using onset: 0 with the side effect of also printing out\n\n                                                        # the full ring of onsets:\n\nsample :loop_tabla, onset: l                            # (ring {:start=>0.0, :finish=>0.0076}, {:start=>0.0076, :finish 0.015}...)\n\n                                                        # We are therefore free to define this lambda to do anything we want.\n\n                                                        # This gives us very powerful control over the choice of onset. It is\n\n                                                        # unlikely you will use this frequently, but it is a powerful tool\n\n                                                        # that's there when you need it.\n\n"
  },
  "tick_reset": {
    "doc": "Reset default tick to 0. If a `key` is referenced, set that tick to 0 instead. Same as calling tick_set(0)",
    "summary": "Reset tick to 0",
    "examples": "           # increment default tick a few times\n\n  tick\n\n  tick\n\n  tick\n\n  puts look #=> 2 (default tick is now 2)\n\n  tick_set 0 # default tick is now 0\n\n  puts look #=> 0 (default tick is now 0\n\n  \",\n\n  \"\n\n                  # increment tick :foo a few times\n\n  tick :foo\n\n  tick :foo\n\n  tick :foo\n\n  puts look(:foo) #=> 2 (tick :foo is now 2)\n\n  tick_set 0 # default tick is now 0\n\n  puts look(:foo) #=> 2 (tick :foo is still 2)\n\n  tick_set :foo, 0 #  reset tick :foo\n\n  puts look(:foo) #=> 0 (tick :foo is now 0)"
  },
  "halves": {
    "doc": "Create a ring containing the results of successive halving of the `start` value. If `num_halves` is negative, will return a ring of `doubles`.",
    "summary": "Create a ring of successive halves",
    "examples": "(halves 60, 2)  #=> (ring 60, 30)\",\n\n        \"(halves 120, 3) #=> (ring 120, 60, 30)\",\n\n        \"(halves 120, 5) #=> (ring 120, 60, 30, 15, 7.5)\",\n\n        \"(halves 30, -5) #=> (ring 30, 60, 120, 240, 480)"
  },
  "wait": {
    "doc": "Synonym for `sleep` - see `sleep`",
    "summary": "Wait for duration"
  },
  "play_chord": {
    "doc": "Play a list of notes at the same time.\nAccepts optional args for modification of the synth being played. See each synth's documentation for synth-specific opts. See `use_synth` and `with_synth` for changing the current synth.",
    "summary": "Play notes simultaneously",
    "examples": "play_chord [40, 45, 47]\n\n# same as:\n\nplay 40\n\nplay 45\n\nplay 47\",\n\n        \"play_chord [40, 45, 47], amp: 0.5\n\n# same as:\n\nplay 40, amp: 0.5\n\nplay 45, amp: 0.5\n\nplay 47, amp: 0.5\",\n\n        \"play_chord chord(:e3, :minor)"
  },
  "ndefine": {
    "doc": "Does nothing. Use to stop a define from actually defining. Simpler than wrapping whole define in a comment block or commenting each individual line out.",
    "summary": "Define a new function"
  },
  "with_octave": {
    "doc": "Transposes your music by shifting all notes played by the specified number of octaves within the specified block. To shift up by an octave use a transpose of 1. To shift down use negative numbers. For transposing the notes within the octave range see `with_transpose`.",
    "summary": "Block level octave transposition",
    "examples": "play 50 # Plays note 50\n\nsleep 1\n\nwith_octave 1 do\n\n play 50 # Plays note 62\n\nend\n\nsleep 1\n\nplay 50 # Plays note 50"
  },
  "rrand": {
    "doc": "Given two numbers, this produces a float between the supplied min and max values exclusively. Both min and max need to be supplied. For random integers, see `rrand_i`. If optional arg `step:` is used, the result is quantised by step.",
    "summary": "Generate a random float between two numbers",
    "examples": "  print rrand(0, 10) #=> will print a number like 8.917730007820797 to the output pane\",\n\n  \"\n\n  loop do\n\n    play rrand(60, 72) #=> Will play a random non-integer midi note between C4 (60) and C5 (72) such as 67.3453 or 71.2393\n\n    sleep 0.125\n\n  end"
  },
  "chord_invert": {
    "doc": "Given a set of notes, apply a number of inversions indicated by the `shift` parameter. Inversions being an increase to notes if `shift` is positive or decreasing the notes if `shift` is negative.\nAn inversion is simply rotating the chord and shifting the wrapped notes up or down an octave. For example, consider the chord :e3, :minor - `(ring 52, 55, 59)`. When we invert it once, we rotate the notes around to `(ring 55, 59, 52)`. However, because note 52 is wrapped round, it's shifted up an octave (12 semitones) so the actual first inversion of the chord :e3, :minor is `(ring 55, 59, 52 + 12)` or `(ring 55, 59, 64)`.\nNote that it's also possible to directly invert chords on creation with the `invert:` opt - `(chord :e3, :minor, invert: 2)`",
    "summary": "Chord inversion",
    "examples": "play (chord_invert (chord :A3, \\\"M\\\"), 0) #No inversion     - (ring 57, 61, 64)\n\nsleep 1\n\nplay (chord_invert (chord :A3, \\\"M\\\"), 1) #First inversion  - (ring 61, 64, 69)\n\nsleep 1\n\nplay (chord_invert (chord :A3, \\\"M\\\"), 2) #Second inversion - (ring 64, 69, 73)\n\n"
  },
  "use_merged_synth_defaults": {
    "doc": "Specify synth arg values to be used by any following call to play. Merges the specified values with any previous defaults, rather than replacing them.",
    "summary": "Merge synth defaults",
    "examples": "play 50 #=> Plays note 50\n\nuse_merged_synth_defaults amp: 0.5\n\nplay 50 #=> Plays note 50 with amp 0.5\n\nuse_merged_synth_defaults cutoff: 80\n\nplay 50 #=> Plays note 50 with amp 0.5 and cutoff 80\n\nuse_merged_synth_defaults amp: 0.7\n\nplay 50 #=> Plays note 50 with amp 0.7 and cutoff 80\n\n\",\n\n        \"use_synth_defaults amp: 0.5, cutoff: 80, pan: -1\n\nuse_merged_synth_defaults amp: 0.7\n\nplay 50 #=> Plays note 50 with amp 0.7, cutoff 80 and pan -1"
  },
  "load_samples": {
    "doc": "Given a directory containing multiple `.wav`, `.wave`, `.aif`, `.aiff` or `.flac` files, pre-loads all the samples into memory.\nYou may also specify the same set of source and filter pre-args available to `sample` itself. `load_sample` will load all matching samples (not just the sample `sample` would play given the same opts) - see `sample`'s docs for more information.\" ",
    "summary": "Pre-load all matching samples",
    "examples": " load_sample :elec_blip # :elec_blip is now loaded and ready to play as a sample\n\n sample :elec_blip # No delay takes place when attempting to trigger it\",\n\n \"# Using source and filter pre-args\n\n dir = \\\"/path/to/sample/dir\\\"\n\n load_sample dir # loads all samples in \\\"/path/to/sample/dir\\\"\n\n load_sample dir, 1 # loads sample with index 1 in \\\"/path/to/sample/dir\\\"\n\n load_sample dir, :foo # loads sample with name \\\"foo\\\" in \\\"/path/to/sample/dir\\\"\n\n load_sample dir, \\\"quux\\\" # loads all samples with file names containing \\\"quux\\\" in \\\"/path/to/sample/dir\\\"\n\n load_sample dir, /[Bb]ar/ # loads all samples which match regex /[Bb]ar/ in \\\"/path/to/sample/dir\\\"\n\n "
  },
  "tick_reset_all": {
    "doc": "Reset all ticks - default and keyed",
    "summary": "Reset all ticks",
    "examples": "  tick      # increment default tick and tick :foo\n\n  tick\n\n  tick :foo\n\n  tick :foo\n\n  tick :foo\n\n  puts look #=> 1\n\n  puts look(:foo) #=> 2\n\n  tick_reset_all\n\n  puts look #=> 0\n\n  puts look(:foo) #=> 0\n\n  "
  },
  "with_synth": {
    "doc": "Switch the current synth to `synth_name` but only for the duration of the `do`/`end` block. After the `do`/`end` block has completed, the previous synth is restored.",
    "summary": "Block-level synth switching",
    "examples": "play 50 # Plays with default synth\n\nsleep 2\n\nuse_synth :supersaw\n\nplay 50 # Plays with supersaw synth\n\nsleep 2\n\nwith_synth :saw_beep do\n\n  play 50 # Plays with saw_beep synth\n\nend\n\nsleep 2\n\n# Previous synth is restored\n\nplay 50 # Plays with supersaw synth\n\n"
  },
  "use_bpm_mul": {
    "doc": "Sets the tempo in bpm (beats per minute) as a multiplication of the current tempo. Affects all containing calls to `sleep` and all temporal synth arguments which will be scaled to match the new bpm. See also `use_bpm`",
    "summary": "Set new tempo as a multiple of current tempo",
    "examples": "  use_bpm 60   # Set the BPM to 60\n\n  play 50\n\n  sleep 1      # Sleeps for 1 seconds\n\n  play 62\n\n  sleep 2      # Sleeps for 2 seconds\n\n  use_bpm_mul 0.5 # BPM is now (60 * 0.5) == 30\n\n  play 50\n\n  sleep 1           # Sleeps for 2 seconds\n\n  play 62\n\n  "
  },
  "dec": {
    "doc": "Decrement a number by `1`. Equivalent to `n - 1`",
    "summary": "Decrement",
    "examples": "dec 1 # returns 0\",\n\n        \"dec -1 # returns -2"
  },
  "with_debug": {
    "doc": "Similar to use_debug except only applies to code within supplied `do`/`end` block. Previous debug value is restored after block.",
    "summary": "Block-level enable and disable debug",
    "examples": "# Turn on debugging:\n\nuse_debug true\n\nplay 80 # Debug message is sent\n\nwith_debug false do\n\n  #Debug is now disabled\n\n  play 50 # Debug message is not sent\n\n  sleep 1\n\n  play 72 # Debug message is not sent\n\nend\n\n# Debug is re-enabled\n\nplay 90 # Debug message is sent\n\n"
  },
  "current_volume": {
    "doc": "Returns the current volume.\nThis can be set via the fn `set_volume!`.",
    "summary": "Get current volume",
    "examples": "puts current_volume # Print out the current volume\",\n\n        \"set_volume! 2\n\nputs current_volume #=> 2"
  },
  "ratio_to_pitch": {
    "doc": "Convert a frequency ratio to a midi note which when added to a note will transpose the note to match the frequency ratio.",
    "summary": "relative frequency ratio to MIDI pitch",
    "examples": "ratio_to_pitch 2 #=> 12.0\",\n\n        \"ratio_to_pitch 0.5 #=> -12.0"
  },
  "with_tuning": {
    "doc": "Similar to use_tuning except only applies to code within supplied `do`/`end` block. Previous tuning value is restored after block.",
    "summary": "Block-level tuning modification",
    "examples": "use_tuning :equal, :c\n\nplay :e4 # Plays note 64\n\nwith_tuning :just, :c do\n\n  play :e4 # Plays note 63.8631\n\n  sleep 1\n\n  play :c4 # Plays note 60\n\nend\n\n# Original tuning value is restored\n\nplay :e4 # Plays note 64"
  },
  "current_synth_defaults": {
    "doc": "Returns the current synth defaults. This is a map of synth arg names to either values or functions.\nThis can be set via the fns `use_synth_defaults`, `with_synth_defaults`, `use_merged_synth_defaults` and `with_merged_synth_defaults`.",
    "summary": "Get current synth defaults",
    "examples": "use_synth_defaults amp: 0.5, cutoff: 80\n\nplay 50 # Plays note 50 with amp 0.5 and cutoff 80\n\nputs current_synth_defaults #=> Prints {amp: 0.5, cutoff: 80}"
  },
  "load_sample": {
    "doc": "Given a path to a `.wav`, `.wave`, `.aif`, `.aiff` or `.flac` file, pre-loads the sample into memory.\n+You may also specify the same set of source and filter pre-args available to `sample` itself. `load_sample` will then load all matching samples. See `sample`'s docs for more information.\" ",
    "summary": "Pre-load first matching sample",
    "examples": "load_sample :elec_blip # :elec_blip is now loaded and ready to play as a sample\n\nsample :elec_blip # No delay takes place when attempting to trigger it\",\n\n\"# Using source and filter pre-args\n\ndir = \\\"/path/to/sample/dir\\\"\n\nload_sample dir # loads first matching sample in \\\"/path/to/sample/dir\\\"\n\nload_sample dir, 1 # loads sample with index 1 in \\\"/path/to/sample/dir\\\"\n\nload_sample dir, :foo # loads sample with name \\\"foo\\\" in \\\"/path/to/sample/dir\\\"\n\nload_sample dir, \\\"quux\\\" # loads first sample with file name containing \\\"quux\\\" in \\\"/path/to/sample/dir\\\"\n\nload_sample dir, /[Bb]ar/ # loads first sample which matches regex /[Bb]ar/ in \\\"/path/to/sample/dir\\\"\n\n"
  },
  "tick": {
    "doc": "Increment the default tick by 1 and return value. Successive calls to `tick` will continue to increment the default tick. If a `key` is specified, increment that specific tick. If an increment `value` is specified, increment key by that value rather than 1. Ticks are `in_thread` and `live_loop` local, so incrementing a tick only affects the current thread's version of that tick. See `tick_reset` and `tick_set` for directly manipulating the tick vals.",
    "summary": "Increment a tick and return value",
    "examples": "  puts tick #=> 0\n\n  puts tick #=> 1\n\n  puts tick #=> 2\n\n  puts tick #=> 3\n\n  \",\n\n  \"\n\n  puts tick(:foo) #=> 0 # named ticks have their own counts\n\n  puts tick(:foo) #=> 1\n\n  puts tick(:foo) #=> 2\n\n  puts tick(:bar) #=> 0 # tick :bar is independent of tick :foo\n\n  \",\n\n  \" # Each_live loop has its own separate ticks\n\n  live_loop :fast_tick do\n\n    puts tick   # the fast_tick live_loop's tick will\n\n    sleep 2     # be updated every 2 seconds\n\n  end\n\n  live_loop :slow_tick do\n\n    puts tick   # the slow_tick live_loop's tick is\n\n    sleep 4     # totally independent from the fast_tick\n\n                # live loop and will be updated every 4\n\n                # seconds\n\n  end\n\n  \",\n\n  \"\n\n  live_loop :regular_tick do\n\n    puts tick   # the regular_tick live_loop's tick will\n\n    sleep 1     # be updated every second\n\n  end\n\n  live_loop :random_reset_tick do\n\n    if one_in 3 # randomly reset tick\n\n      tick_reset\n\n      puts \\\"reset tick!\\\"\n\n    end\n\n    puts tick   # this live_loop's tick is totally\n\n    sleep 1     # independent and the reset only affects\n\n                # this tick.\n\n  end\n\n  \",\n\n  \"\n\n  # Ticks work directly on lists, and will tick through each element\n\n  # However, once they get to the end, they'll return nil\n\n  live_loop :scale do\n\n    play [:c, :d, :e, :f, :g].tick   # play all notes just once, then rests\n\n    sleep 1\n\n  end\n\n  \",\n\n  \"\n\n  # Normal ticks interact directly with list ticks\n\n  live_loop :odd_scale do\n\n    tick  # Increment the default tick\n\n    play [:c, :d, :e, :f, :g, :a].tick   # this now play every *other* note just once,\n\n                                         # then rests\n\n    sleep 1\n\n  end\n\n  \",\n\n  \"\n\n  # Ticks work wonderfully with rings\n\n  # as the ring ensures the tick wraps\n\n  # round internally always returning a\n\n  # value\n\n  live_loop :looped_scale do\n\n    play (ring :c, :d, :e, :f, :g).tick   # play all notes just once, then repeats\n\n    sleep 1\n\n  end\n\n  \",\n\n  \"\n\n  # Ticks work wonderfully with scales\n\n  # which are also rings\n\n  live_loop :looped_scale do\n\n    play (scale :e3, :minor_pentatonic).tick   # play all notes just once, then repeats\n\n    sleep 0.25\n\n  end\n\n  "
  },
  "use_timing_guarantees": {
    "doc": "If set to true, synths will not trigger if it is too late. If false, some synth triggers may be late.",
    "summary": "Inhibit synth triggers if too late",
    "examples": "use_timing_guarantees true\n\nsample :loop_amen  #=> if time is behind by any margin, this will not trigger\",\n\n        \"\n\nuse_timing_guarantees false\n\nsample :loop_amen  #=> unless time is too far behind, this will trigger even when late."
  },
  "current_cent_tuning": {
    "doc": "Returns the cent shift value.\nThis can be set via the fns `use_cent_tuning` and `with_cent_tuning`.",
    "summary": "Get current cent shift",
    "examples": "puts current_cent_tuning # Print out the current cent shift"
  },
  "with_sample_bpm": {
    "doc": "Block-scoped modification of bpm so that sleeping for 1 will sleep for the duration of the sample.",
    "summary": "Block-scoped sample-duration-based bpm modification",
    "examples": "live_loop :dnb do\n\n  with_sample_bpm :loop_amen do #Set bpm based on :loop_amen duration\n\n    sample :bass_dnb_f\n\n    sample :loop_amen\n\n    sleep 1                     #`sleep`ing for 1 sleeps for duration of :loop_amen\n\n  end\n\nend\",\n\n        \"live_loop :dnb do\n\n  with_sample_bpm :loop_amen, num_beats: 4 do # Set bpm based on :loop_amen duration\n\n                                              # but also specify that the sample duration\n\n                                              # is actually 4 beats long.\n\n    sample :bass_dnb_f\n\n    sample :loop_amen\n\n    sleep 4                     #`sleep`ing for 4 sleeps for duration of :loop_amen\n\n                                # as we specified that the sample consisted of\n\n                                # 4 beats\n\n  end\n\nend"
  },
  "factor": {
    "doc": "Test to see if factor is indeed a factor of `val`. In other words, can `val` be divided exactly by factor.",
    "summary": "Factor test",
    "examples": "\n\n  factor?(10, 2) # true - 10 is a multiple of 2 (2 * 5 = 10)\n\n  \",\n\n  \"\n\n  factor?(11, 2) #false - 11 is not a multiple of 2\n\n  \",\n\n  \"\n\n  factor?(2, 0.5) #true - 2 is a multiple of 0.5 (0.5 * 4 = 2) "
  },
  "recording_stop": {
    "doc": "Stop current recording.",
    "summary": "Stop recording"
  },
  "rrand_i": {
    "doc": "Given two numbers, this produces a whole number between the min and max you supplied inclusively. Both min and max need to be supplied. For random floats, see `rrand`",
    "summary": "Generate a random whole number between two points inclusively",
    "examples": "  print rrand_i(0, 10) #=> will print a random number between 0 and 10 (e.g. 4, 0 or 10) to the output pane\",\n\n  \"\n\n  loop do\n\n    play rrand_i(60, 72) #=> Will play a random midi note between C4 (60) and C5 (72)\n\n    sleep 0.125\n\n  end"
  },
  "spark": {
    "doc": "Given a list of numeric values, this method turns them into a string of bar heights and prints them out. Useful for quickly graphing the shape of an array.",
    "summary": "Print a string representing a list of numeric values as a spark graph/bar chart",
    "examples": "spark (range 1, 5))    #=> ▁▃▅█\",\n\n  \"spark (range 1, 5).shuffle) #=> ▃█▅▁"
  },
  "quantise": {
    "doc": "Round value to the nearest multiple of step resolution.",
    "summary": "Quantise a value to resolution",
    "examples": "\n\n  quantise(10, 1) # 10 is already a multiple of 1, so returns 10\" ,\n\n  \"\n\n  quantise(10, 1.1) # Returns 9.9 which is 1.1 * 9\",\n\n  \"\n\n  quantise(13.3212, 0.1) # 13.3\",\n\n  \"\n\n  quantise(13.3212, 0.2) # 13.4\",\n\n  \"\n\n  quantise(13.3212, 0.3) # 13.2\",\n\n  \"\n\n  quantise(13.3212, 0.5) # 13.5"
  },
  "live_loop": {
    "doc": "Loop the do/end block forever. However, unlike a basic loop, a live_loop has two special properties. Firstly it runs in a thread - so you can have any number of live loops running at the same time (concurrently). Secondly, you can change the behaviour of a live loop whilst it is still running without needing to stop it. Live loops are therefore the secret to live coding with Sonic Pi.\nAs live loops are excecuted within a named in_thread, they behave similarly. See the in_thread documentation for all the details. However, it's worth mentioning a few important points here. Firstly, only one live loop with a given name can run at any one time. Therefore, if you define two or more `live_loop`s called `:foo` only one will be running. Another important aspect of `live_loop`s is that they manage their own thread locals set with the `use_*` and `with_*` fns. This means that each `live_loop` can have its own separate default synth, BPM and sample defaults. When a `live_loop` is *first* created, it inherits the thread locals from the parent thread, but once it has started, the only way to change them is by re-defining the do/end body of the `live_loop`. See the examples below for details. Finally, as mentioned above, provided their names are different, you may have many `live_loop`s executing at once.\nA typical way of live coding with live loops is to define a number of them in a buffer, hit Run to start them and then to modify their do/end blocks and then hit Run again. This will not create any more thread, but instead just modify the behaviour of the existing threads. The changes will *not* happen immediately. Instead, they will only happen the next time round the loop. This is because the behaviour of each live loop is implemented with a standard function. When a live loop is updated, the function definition is also updated. Each time round the live loop, the function is called, so the new behviour is only observed next time round the loop.\nAlso sends a `cue` with the same name each time the `live_loop` repeats. This may be used to `sync` with other threads and `live_loop`s.\nIf the `live_loop` block is given a parameter, this is given the result of the last run of the loop (with initial value either being `0` or an init arg). This allows you to 'thread' values across loops.\nFinally, it is possible to delay the initial trigger of the live_loop on creation with both the `delay:` and `sync:` opts. See their respective docstrings. If both `delay:` and `sync:` are specified, on initial live_loop creation first the delay will be honoured and then the sync.\n",
    "summary": "A loop for live coding",
    "examples": "## Define and start a simple live loop\n\nlive_loop :ping do  # Create a live loop called :ping\n\n  sample :elec_ping # This live loops plays the :elec_ping sample\n\n  sleep 1           # Then sleeps for 1 beat before repeating\n\nend\n\n  \",\n\n        \"\n\n## Every live loop must sleep or sync\n\nlive_loop :ping do  # Create a live loop called :ping\n\n  sample :elec_ping # This live loops plays the :elec_ping sample\n\n                    # However, because the do/end lock of the live loop does not\n\n                    # contain any calls to sleep or sync, the live loop stops at\n\n                    # the end of the first loop with a 'Did not sleep' error.\n\nend\",\n\n        \"\n\n## Multiple live loops will play at the same time\n\nlive_loop :foo do  # Start a live loop called :foo\n\n  play 70\n\n  sleep 1\n\nend\n\nlive_loop :bar do  # Start another live loop called :bar\n\n  sample :bd_haus  # Both :foo and :bar will be playing\n\n  sleep 0.5        # at the same time.\n\nend\n\n\",\n\n        \"\n\n## Live loops inherit external use_* thread locals\n\nuse_bpm 30\n\nlive_loop :foo do\n\n  play 70           # live loop :foo now has a BPM of 30\n\n  sleep 1           # This sleep will be for 2 seconds\n\nend\n\n\",\n\n        \"\n\n## Live loops can have their own thread locals\n\nlive_loop :foo do\n\n  use_bpm 30       # Set the BPM of live loop :foo to 30\n\n  play 70\n\n  sleep 1          # This sleep will be for 2 seconds\n\nend\n\nlive_loop :bar do\n\n  use_bpm 120      # Set the BPM of live loop :bar to 120\n\n  play 82\n\n  sleep 1          # This sleep will be for 0.5 seconds\n\nend\n\n\",\n\n        \"\n\n## Live loops can pass values between iterations\n\nlive_loop :foo do |a|  # pass a param (a) to the block (inits to 0)\n\n  puts a               # prints out all the integers\n\n  sleep 1\n\n  a += 1               # increment a by 1 (last value is passed back into the loop)\n\nend\n\n  \",\n\n        \"\n\n## Live loop names must be unique\n\nlive_loop :foo do  # Start a live loop called :foo\n\n  play 70\n\n  sleep 1\n\nend\n\nlive_loop :foo do  # Attempt to start another also called :foo\n\n  sample :bd_haus  # With a different do/end block\n\n  sleep 0.5        # This will not start another live loop\n\n                   # but instead replace the behaviour of the first.\n\nend                # There will only be one live loop running playing\n\n                   # The bass drum\n\n\",\n\n        \"\n\n## You can sync multiple live loops together\n\nlive_loop :foo, sync: :bar do # Wait for a :bar cue event before starting :foo\n\n play 70                      # Live loop :foo is therefore blocked and does\n\n sleep 1                      # not make a sound initially\n\nend\n\nsleep 4                       # Wait for 4 beats\n\nlive_loop :bar do             # Start a live loop called :foo which will emit a :bar\n\n  sample :bd_haus             # cue message therefore releasing the :foo live loop.\n\n  sleep 0.5                   # Live loop :foo therefore starts and also inherits the\n\nend                           # logical time of live loop :bar.\n\n                              # This pattern is also useful to re-sync live loops after\n\n                              # errors are made. For example, when modifying live loop :foo\n\n                              # it is possible to introduce a runtime error which will stop\n\n                              # :foo but not :bar (as they are separate, isolated threads).\n\n                              # Once the error has been fixed and the code is re-run, :foo\n\n                              # will automatically wait for :bar to loop round and restart\n\n                              # in sync with the correct virtual clock."
  },
  "with_fx": {
    "doc": "This applies the named effect (FX) to everything within a given `do`/`end` block. Effects may take extra parameters to modify their behaviour. See FX help for parameter details.\nFor advanced control, it is also possible to modify the parameters of an effect within the body of the block. If you define the block with a single argument, the argument becomes a reference to the current effect and can be used to control its parameters (see examples).",
    "summary": "Use Studio FX",
    "examples": "# Basic usage\n\nwith_fx :distortion do # Use the distortion effect with default parameters\n\n  play 50 # => plays note 50 with distortion\n\n  sleep 1\n\n  sample :loop_amen # => plays the loop_amen sample with distortion too\n\nend\",\n\n        \"# Specify effect parameters\n\nwith_fx :level, amp: 0.3 do # Use the level effect with the amp parameter set to 0.3\n\n  play 50\n\n  sleep 1\n\n  sample :loop_amen\n\nend\",\n\n        \"\n\n# Controlling the effect parameters within the block\n\nwith_fx :reverb, mix: 0.1 do |fx|\n\n  # here we set the reverb level quite low to start with (0.1)\n\n  # and we can change it later by using the 'fx' reference we've set up\n\n  play 60 # plays note 60 with a little bit of reverb\n\n  sleep 2\n\n  control fx, mix: 0.5 # change the parameters of the effect to add more reverb\n\n  play 60 # again note 60 but with more reverb\n\n  sleep 2\n\n  control fx, mix: 1 # change the parameters of the effect to add more reverb\n\n  play 60 # plays note 60 with loads of reverb\n\n  sleep 2\n\nend\",\n\n        \"\n\n# Repeat the block 16 times internally\n\nwith_fx :reverb, reps: 16 do\n\n  play (scale :e3, :minor_pentatonic), release: 0.1\n\n  sleep 0.125\n\nend\n\n# The above is a shorthand for this:\n\nwith_fx :reverb do\n\n  16.times do\n\n    play (scale :e3, :minor_pentatonic), release: 0.1\n\n    sleep 0.125\n\n  end\n\nend\n\n"
  },
  "sample_free_all": {
    "doc": "Unloads all samples therefore freeing the memory and resources consumed. Subsequent calls to `sample` and friends will re-load the sample on the server.",
    "summary": "Free all loaded samples on the synth server",
    "examples": "sample :loop_amen        # load and play :loop_amen\n\nsample :ambi_lunar_land  # load and play :ambi_lunar_land\n\nsleep 2\n\nsample_free_all\n\nsample :loop_amen        # re-loads and plays amen"
  },
  "all_sample_names": {
    "doc": "Return a list of all the sample names available",
    "summary": "Get all sample names"
  },
  "with_arg_checks": {
    "doc": "Similar to `use_arg_checks` except only applies to code within supplied `do`/`end` block. Previous arg check value is restored after block.",
    "summary": "Block-level enable and disable arg checks",
    "examples": "# Turn on arg checking:\n\nuse_arg_checks true\n\nplay 80, cutoff: 100 # Args are checked\n\nwith_arg_checks false do\n\n  #Arg checking is now disabled\n\n  play 50, release: 3 # Args are not checked\n\n  sleep 1\n\n  play 72             # Arg is not checked\n\nend\n\n# Arg checking is re-enabled\n\nplay 90 # Args are checked\n\n"
  },
  "load_synthdefs": {
    "doc": "Load all pre-compiled synth designs in the specified directory. The binary files containing synth designs need to have the extension `.scsyndef`. This is useful if you wish to use your own SuperCollider synthesiser designs within Sonic Pi.\n## Important notes\nYou may not trigger external synthdefs unless you enable the following GUI preference:\n```\nStudio -> Synths and FX -> Enable external synths and FX\n```\nAlso, if you wish your synth to work with Sonic Pi's automatic stereo sound infrastructure *you need to ensure your synth outputs a stereo signal* to an audio bus with an index specified by a synth arg named `out_bus`. For example, the following synth would work nicely:\n(\nSynthDef(\\\\piTest\n{|freq = 200, amp = 1, out_bus = 0 |\nOut.ar(out_bus\nSinOsc.ar([freq,freq],0,0.5)* Line.kr(1, 0, 5, amp, doneAction: 2))}\n).writeDefFile(\\\"/Users/sam/Desktop/\\\")\n)\n",
    "summary": "Load external synthdefs",
    "examples": "load_synthdefs \\\"~/Desktop/my_noises\\\" # Load all synthdefs in my_noises folder"
  },
  "current_octave": {
    "doc": "Returns the octave shift value.\nThis can be set via the fns `use_octave` and `with_octave`.",
    "summary": "Get current octave shift",
    "examples": "puts current_octave # Print out the current octave shift"
  },
  "with_sample_defaults": {
    "doc": "Specify new default values to be used by all subsequent calls to `sample` within the `do`/`end` block. After the `do`/`end` block has completed, the previous sampled defaults (if any) are restored. For the contents of the block, will remove and override any previous defaults.",
    "summary": "Block-level use new sample defaults",
    "examples": "sample :loop_amen # plays amen break with default arguments\n\nuse_sample_defaults amp: 0.5, cutoff: 70\n\nsample :loop_amen # plays amen break with an amp of 0.5, cutoff of 70 and defaults for rest of args\n\nwith_sample_defaults cutoff: 90 do\n\n  sample :loop_amen  # plays amen break with a cutoff of 90 and defaults for rest of args - note that amp is no longer 0.5\n\nend\n\nsample :loop_amen  # plays amen break with a cutoff of 70 and amp is 0.5 again as the previous defaults are restored."
  },
  "pick": {
    "doc": "Pick n elements from list or ring. Unlike shuffle, after each element has been picked, it is 'returned' to the list so it may be picked again. This means there may be duplicates in the result. If n is greater than the size of the ring/list then duplicates are guaranteed to be in the result.\nIf `n` isn't supplied it defaults to the size of the list/ring.\nIf no arguments are given, will return a lambda function which when called takes an argument which will be a list to be picked from. This is useful for choosing random `onset:` vals for samples.",
    "summary": "Randomly pick from list (with duplicates)",
    "examples": "puts [1, 2, 3, 4, 5].pick(3) #=> [4, 4, 3]\",\n\n\"\n\nputs (ring 1, 2, 3, 4, 5).pick(3) #=> (ring 4, 4, 3)\",\n\n\"\n\nputs (ring 1, 2).pick(5) #=> (ring 2, 2, 1, 1, 1)\",\n\n\"\n\nputs (ring 1, 2, 3).pick #=> (ring 3, 3, 2)"
  },
  "with_timing_guarantees": {
    "doc": "For the given block, if set to true, synths will not trigger if it is too late. If false, some synth triggers may be late. After the block has completed, the previous value is restored.",
    "summary": "Block-scoped inhibition of synth triggers if too late",
    "examples": "with_timing_guarantees true\n\n  sample :loop_amen  #=> if time is behind by any margin, this will not trigger\n\nend\",\n\n\"\n\nwith_timing_guarantees false\n\n  sample :loop_amen  #=> unless time is too far behind, this will trigger even when late.\n\nend"
  },
  "synth_names": {
    "doc": "Return a list of all the synths available",
    "summary": "Get all synth names"
  },
  "block_slept": {
    "doc": "Given a block, runs it and returns whether or not the block contained sleeps or syncs",
    "summary": "Determine if block contains sleep time",
    "examples": "slept = block_slept? do\n\n  play 50\n\n  sleep 1\n\n  play 62\n\n  sleep 2\n\nend\n\nputs slept #=> Returns true as there were sleeps in the block\",\n\n\"\n\nin_thread do\n\n  sleep 1\n\n  cue :foo  # trigger a cue on a different thread\n\nend\n\nslept = block_slept? do\n\n  sync :foo  # wait for the cue before playing the note\n\n  play 62\n\nend\n\nputs slept #=> Returns true as the block contained a sync.\",\n\n\"\n\nslept = block_slept? do\n\n  play 50\n\n  play 62\n\nend\n\nputs slept #=> Returns false as there were no sleeps in the block"
  },
  "tick_set": {
    "doc": "Set the default tick to the specified `value`. If a `key` is referenced, set that tick to `value` instead. Next call to `look` will return `value`.",
    "summary": "Set tick to a specific value",
    "examples": "  tick_set 40 # set default tick to 40\n\n  puts look   #=> 40\",\n\n  \"\n\n  tick_set :foo, 40 # set tick :foo to 40\n\n  puts look(:foo)   #=> 40 (tick :foo is now 40)\n\n  puts look         #=> 0 (default tick is unaffected)\n\n  "
  },
  "uncomment": {
    "doc": "Evaluates all of the code within the block. Use to reverse the effect of the comment without having to explicitly remove it.",
    "summary": "Block level comment ignoring",
    "examples": "  uncomment do # starting a block level comment:\n\n    play 50 # played\n\n    sleep 1 # sleep happens\n\n    play 62 # played\n\n  end"
  },
  "with_cue_logging": {
    "doc": "Similar to use_cue_logging except only applies to code within supplied `do`/`end` block. Previous cue log value is restored after block.",
    "summary": "Block-level enable and disable cue logging",
    "examples": "  # Turn on debugging:\n\n  use_cue_logging true\n\n  cue :foo # cue message is printed to log\n\n  with_cue_logging false do\n\n    #Cue logging is now disabled\n\n    cue :bar # cue *is* sent but not displayed in log\n\n  end\n\n  sleep 1\n\n  # Debug is re-enabled\n\n  cue :quux # cue is displayed in log\n\n  "
  },
  "version": {
    "doc": "Return information representing the current version of Sonic Pi. This information may be further inspected with `version.major`, `version.minor`, `version.patch` and `version.dev`",
    "summary": "Get current version information",
    "examples": "  puts version # => Prints out the current version such as v2.0.1\",\n\n  \"\n\n  puts version.major # => Prints out the major version number such as 2\",\n\n  \"\n\n  puts version.minor # => Prints out the minor version number such as 0\",\n\n  \"\n\n  puts version.patch # => Prints out the patch level for this version such as 0"
  },
  "with_bpm": {
    "doc": "Sets the tempo in bpm (beats per minute) for everything in the given block. Affects all containing calls to `sleep` and all temporal synth arguments which will be scaled to match the new bpm. See also `use_bpm`\nFor dance music here's a rough guide for which BPM to aim for depending on your genre:\n* Dub: 60-90 bpm\n* Hip-hop: 60-100 bpm\n* Downtempo: 90-120 bpm\n* House: 115-130 bpm\n* Techno/trance: 120-140 bpm\n* Dubstep: 135-145 bpm\n* Drum and bass: 160-180 bpm\n",
    "summary": "Set the tempo for the code block",
    "examples": "  # default tempo is 60 bpm\n\n  4.times do\n\n    sample :drum_bass_hard\n\n    sleep 1 # sleeps for 1 second\n\n  end\n\n  sleep 5 # sleeps for 5 seconds\n\n  # with_bpm sets a tempo for everything between do ... end (a block)\n\n  # Hear how it gets faster?\n\n  with_bpm 120 do  # set bpm to be twice as fast\n\n    4.times do\n\n      sample :drum_bass_hard\n\n      sleep 1 # now sleeps for 0.5 seconds\n\n    end\n\n  end\n\n  sleep 5\n\n  # bpm goes back to normal\n\n  4.times do\n\n    sample :drum_bass_hard\n\n    sleep 1 # sleeps for 1 second\n\n  end"
  },
  "use_sample_defaults": {
    "doc": "Specify new default values to be used by all subsequent calls to `sample`. Will remove and override any previous defaults.",
    "summary": "Use new sample defaults",
    "examples": "sample :loop_amen # plays amen break with default arguments\n\nuse_sample_defaults amp: 0.5, cutoff: 70\n\nsample :loop_amen # plays amen break with an amp of 0.5, cutoff of 70 and defaults for rest of args\n\nuse_sample_defaults cutoff: 90\n\nsample :loop_amen  # plays amen break with a cutoff of 90 and defaults for rest of args - note that amp is no longer 0.5\n\n"
  },
  "one_in": {
    "doc": "Returns `true` or `false` with a specified probability - it will return true every one in num times where num is the param you specify",
    "summary": "Random true value with specified probability",
    "examples": "  one_in 2 # will return true with a probability of 1/2, false with probability 1/2\",\n\n  \"\n\n  one_in 3 # will return true with a probability of 1/3, false with a probability of 2/3\",\n\n  \"\n\n  one_in 100 # will return true with a probability of 1/100, false with a probability of 99/100"
  },
  "vector": {
    "doc": "Create a new immutable vector from args. Out of range indexes return nil.",
    "summary": "Create a vector",
    "examples": "(vector 1, 2, 3)[0] #=> 1\",\n\n        \"(vector 1, 2, 3)[1] #=> 2\",\n\n        \"(vector 1, 2, 3)[2] #=> 3\",\n\n        \"(vector 1, 2, 3)[3] #=> nil\",\n\n        \"(vector 1, 2, 3)[1000] #=> nil\",\n\n        \"(vector 1, 2, 3)[-1] #=> nil\",\n\n        \"(vector 1, 2, 3)[-1000] #=> nil"
  },
  "rand_back": {
    "doc": "Roll the random generator back essentially 'undoing' the last call to `rand`. You may specify an amount to roll back allowing you to skip back n calls to `rand`.",
    "summary": "Roll back random generator",
    "examples": "  # Basic rand stream rollback\n\n  puts rand # prints 0.75006103515625\n\n  rand_back # roll random stream back one\n\n            # the result of the next call to rand will be\n\n            # exactly the same as the previous call\n\n  puts rand # prints 0.75006103515625 again!\n\n  puts rand # prints 0.733917236328125\",\n\n  \"\n\n  # Jumping back multiple places in the rand stream\n\n  puts rand # prints 0.75006103515625\n\n  puts rand # prints 0.733917236328125\n\n  puts rand # prints 0.464202880859375\n\n  puts rand # prints 0.24249267578125\n\n  rand_back(3) # roll random stream back three places\n\n               # the result of the next call to rand will be\n\n               # exactly the same as the result 3 calls to\n\n               # rand ago.\n\n  puts rand # prints  0.733917236328125 again!\n\n  puts rand # prints  0.464202880859375"
  },
  "current_transpose": {
    "doc": "Returns the current transpose value.\nThis can be set via the fns `use_transpose` and `with_transpose`.",
    "summary": "Get current transposition",
    "examples": "puts current_transpose # Print out the current transpose value"
  },
  "sample_paths": {
    "doc": "Accepts the same pre-args and opts as `sample` and returns a ring of matched sample paths.",
    "summary": "Sample Pack Filter Resolution",
    "examples": "sample_paths \\\"/path/to/samples/\\\" #=> ring of all top-level samples in /path/to/samples\",\n\n\"\n\nsample_paths \\\"/path/to/samples/**\\\" #=> ring of all nested samples in /path/to/samples\",\n\n\"\n\nsample_paths \\\"/path/to/samples/\\\", \\\"foo\\\" #=> ring of all samples in /path/to/samples\n\n                                                containing the string \\\"foo\\\" in their filename."
  },
  "bools": {
    "doc": "Create a new ring of booleans values from 1s and 0s, which can be easier to write and manipulate in a live setting.",
    "summary": "Create a ring of boolean values",
    "examples": "(bools 1, 0)    #=> (ring true, false)\",\n\n        \"(bools 1, 0, true, false, nil) #=> (ring true, false, true, false, false)"
  },
  "sync_bpm": {
    "doc": "An alias for `sync` with the `bpm_sync:` opt set to true.",
    "summary": "Sync and inherit BPM from other threads ",
    "examples": "See examples for sync"
  },
  "play": {
    "doc": "Play note with current synth. Accepts a set of standard options which include control of an amplitude envelope with `attack:`, `decay:`, `sustain:` and `release:` phases. These phases are triggered in order, so the duration of the sound is attack + decay + sustain + release times. The duration of the sound does not affect any other notes. Code continues executing whilst the sound is playing through its envelope phases.\nAccepts optional args for modification of the synth being played. See each synth's documentation for synth-specific opts. See `use_synth` and `with_synth` for changing the current synth.\nIf note is `nil`, `:r` or `:rest`, play is ignored and treated as a rest. Also, if the `on:` opt is specified and returns `false`, or `nil` then play is similarly ignored and treated as a rest.\nNote that the default opts listed are only a guide to the most common opts across all the synths. Not all synths support all the default opts and each synth typically supports many more opts specific to that synth. For example, the `:tb303` synth supports 45 unique opts. For a full list of a synth's opts see its documentation in the Help system.\n",
    "summary": "Play current synth",
    "examples": "play 50 # Plays note 50 on the current synth\",\n\n        \"play 50, attack: 1 # Plays note 50 with a fade-in time of 1s\",\n\n        \"play 62, pan: -1, release: 3 # Play note 62 in the left ear with a fade-out time of 3s.\",\n\n      \" # controlling a synth synchronously\n\ns = play :e3, release: 4\n\nsleep 1\n\ncontrol s, note: :e5\n\nsleep 0.5\n\nuse_synth :dsaw\n\nplay :e3   # This is triggered after 1.5s from start\",\n\n\" # Controlling a synth asynchronously\n\nplay :e3, release: 4 do |s|\n\n  sleep 1                                               # This block is run in an implicit in_thread\n\n  control s, note: :e5                                  # and therefore is asynchronous\n\nend\n\nsleep 0.5\n\nuse_synth :dsaw\n\nplay :e3 # This is triggered after 0.5s from start"
  },
  "rand": {
    "doc": "Given a max number, produces a float between `0` and the supplied max value. If max is a range, produces a float within the range. With no args returns a random value between `0` and `1`.",
    "summary": "Generate a random float below a value",
    "examples": "  print rand(0.5) #=> will print a number like 0.375030517578125 to the output pane"
  },
  "set_volume": {
    "doc": "Set the main system volume to `vol`. Accepts a value between `0` and `5` inclusive. Vols greater or smaller than the allowed values are trimmed to keep them within range. Default is `1`.",
    "summary": "Set Volume globally",
    "examples": "set_volume! 2 # Set the main system volume to 2\",\n\n        \"set_volume! -1 # Out of range, so sets main system volume to 0\",\n\n        \"set_volume! 7 # Out of range, so sets main system volume to 5"
  },
  "stretch": {
    "doc": "Stretches a list of values each value repeated count times. Always returns a ring regardless of the type of the list that is stretched. To preserve type, consider using `.stretch` i.e. `(ramp 1, 2, 3).stretch(2) #=> (ramp 1, 1, 2, 2, 3, 3)`",
    "summary": "Stretch a sequence of values",
    "examples": "(stretch [1,2], 3)    #=> (ring 1, 1, 1, 2, 2, 2)\",\n\n        \"(stretch [:e2, :c3], 1, [:c2, :d3], 2) #=> (ring :e2, :c3, :c2, :c2, :d3, :d3)"
  },
  "note_info": {
    "doc": "Returns an instance of `SonicPi::Note`. Please note - `octave:` param overrides any octave specified in a symbol i.e. `:c3`",
    "summary": "Get note info",
    "examples": "%Q{puts note_info(:C, octave: 2)\n\n# returns #<SonicPi::Note :C2>}"
  },
  "note": {
    "doc": "Takes a midi note, a symbol (e.g. `:C`) or a string (e.g. `\\\"C\\\"`) and resolves it to a midi note. You can also pass an optional `octave:` parameter to get the midi note for a given octave. Please note - `octave:` param overrides any octave specified in a symbol i.e. `:c3`. If the note is `nil`, `:r` or `:rest`, then `nil` is returned (`nil` represents a rest)",
    "summary": "Describe note",
    "examples": "# These all return 60 which is the midi number for middle C (octave 4)\n\nputs note(60)\n\nputs note(:C)\n\nputs note(:C4)\n\nputs note('C')\n\n\",\n\n        \"# returns 60 - octave param has no effect if we pass in a number\n\nputs note(60, octave: 2)\n\n# These all return 36 which is the midi number for C2 (two octaves below middle C)\n\nputs note(:C, octave: 2)\n\nputs note(:C4, octave: 2) # note the octave param overrides any octaves specified in a symbol\n\nputs note('C', octave: 2)\n\n"
  },
  "reset_mixer": {
    "doc": "The master mixer is the final mixer that all sound passes through. This fn resets it to its default set - undoing any changes made via set_mixer_control!",
    "summary": "Reset master mixer",
    "examples": "set_mixer_control! lpf: 70 # LPF cutoff value of master mixer is now 70\n\nsample :loop_amen          # :loop_amen sample is played with low cutoff\n\nsleep 3\n\nreset_mixer!               # mixer is now reset to default values\n\nsample :loop_amen          # :loop_amen sample is played with normal cutoff"
  },
  "chord_degree": {
    "doc": "In music we build chords from scales. For example, a C major chord is made by taking the 1st, 3rd and 5th notes of the C major scale (C, E and G). If you do this on a piano you might notice that you play one, skip one, play one, skip one etc. If we use the same spacing and start from the second note in C major (which is a D), we get a D minor chord which is the 2nd, 4th and 6th notes in C major (D, F and A). We can move this pattern all the way up or down the scale to get different types of chords. `chord_degree` is a helper method that returns a ring of midi note numbers when given a degree (starting point in a scale) which is a symbol `:i`, `:ii`, `:iii`, `:iv`, `:v`, `:vi`, `:vii` or a number `1`-`7`. The second argument is the tonic note of the scale, the third argument is the scale type and finally the fourth argument is number of notes to stack up in the chord. If we choose 4 notes from degree `:i` of the C major scale, we take the 1st, 3rd, 5th and 7th notes of the scale to get a C major 7 chord.",
    "summary": "Construct chords of stacked thirds, based on scale degrees",
    "examples": "puts (chord_degree :i, :A3, :major) # returns a ring of midi notes - (ring 57, 61, 64, 68) - an A major 7 chord\nplay (chord_degree :i, :A3, :major, 3)\",\n\n        \"play (chord_degree :ii, :A3, :major, 3) # Chord ii in A major is a B minor chord\",\n\n        \"play (chord_degree :iii, :A3, :major, 3) # Chord iii in A major is a C# minor chord\",\n\n        \"play (chord_degree :iv, :A3, :major, 3) # Chord iv in A major is a D major chord\",\n\n        \"play (chord_degree :i, :C4, :major, 4) # Taking four notes is the default. This gives us 7th chords - here it plays a C major 7\",\n\n        \"play (chord_degree :i, :C4, :major, 5) # Taking five notes gives us 9th chords - here it plays a C major 9 chord"
  },
  "print": {
    "doc": "Displays the information you specify as a string inside the output pane. This can be a number, symbol, or a string itself. Useful for debugging. Synonym for `puts`.",
    "summary": "Display a message in the output pane",
    "examples": "print \\\"hello there\\\"   #=> will print the string \\\"hello there\\\" to the output pane\",\n\n  \"print 5               #=> will print the number 5 to the output pane\",\n\n  \"print foo             #=> will print the contents of foo to the output pane"
  },
  "assert_equal": {
    "doc": "Raises an exception if both arguments aren't equal.",
    "summary": "Ensure args are equal",
    "examples": "# Simple assertions\n\nassert_equal 1, 1\n\n\",\n\n\"\n\n# More interesting assertions\n\nassert_equal 1 + 1, 2 # Ensure that arithmetic is sane!\n\nassert_equal [:a, :b, :c].size,  3 # ensure lists can be correctly counted\n\n\",\n\n\"\n\n# Add messages to the exceptions\n\nassert_equal 3, 5, \\\"something is seriously wrong!\\\"\n\n"
  },
  "with_arg_bpm_scaling": {
    "doc": "Turn synth argument bpm scaling on or off for the supplied block. Note, using `rt` for args will result in incorrect times when used within this block.",
    "summary": "Block-level enable and disable BPM scaling",
    "examples": "use_bpm 120play 50, release: 2 # release is actually 1 due to bpm scaling\n\nwith_arg_bpm_scaling false do\n\n  play 50, release: 2 # release is now 2\n\nend\",\n\n        \"                         # Interaction with rt\n\nuse_bpm 120\n\nplay 50, release: rt(2)   # release is 2 seconds\n\nsleep rt(2)               # sleeps for 2 seconds\n\nwith_arg_bpm_scaling false do\n\n  play 50, release: rt(2) # ** Warning: release is NOT 2 seconds! **\n\n  sleep rt(2)             # still sleeps for 2 seconds\n\nend"
  },
  "look": {
    "doc": "Read and return value of default tick. If a `key` is specified, read the value of that specific tick. Ticks are `in_thread` and `live_loop` local, so the tick read will be the tick of the current thread calling `look`.",
    "summary": "Obtain value of a tick",
    "examples": "  puts look #=> 0\n\n  puts look #=> 0\n\n  puts look #=> 0 # look doesn't advance the tick, it just returns the current value\n\n  \",\n\n  \"\n\n  puts look #=> 0 # A look is always 0 before the first tick\n\n  tick # advance the tick\n\n  puts look #=> 0 # Note: a look is still 0 after the first tick.\n\n  tick\n\n  puts look #=> 1\n\n  puts look #=> 1 # making multiple calls to look doesn't affect tick value\n\n  tick\n\n  puts look #=> 2\n\n  \",\n\n  \"\n\n  tick(:foo)\n\n  tick(:foo)\n\n  puts look(:foo) #=> 1 (keyed look :foo has been advanced)\n\n  puts look #=> 0 (default look hasn't been advanced)\n\n  puts look(:bar) #=> 0 (other keyed looks haven't been advanced either)\n\n  \",\n\n  \"\n\n  # You can call look on lists and rings\n\n  live_loop :foo do\n\n    tick                                      # advance the default tick\n\n    use_synth :beep\n\n    play (scale :e3, :minor_pentatonic).look  # look into the default tick to play all notes in sequence\n\n    sleep 0.5\n\n    use_synth :square\n\n    play (ring :e1, :e2, :e3).look, release: 0.25 # use the same look on another ring\n\n    sleep 0.25\n\n  end\n\n  \",\n\n\"\n\n# Returns numbers unchanged if single argument\n\nputs look(0)     #=> 0\n\nputs look(4)     #=> 4\n\nputs look(-4)    #=> -4\n\nputs look(20.3)  #=> 20.3"
  },
  "current_sample_defaults": {
    "doc": "Returns the current sample defaults. This is a map of synth arg names to either values or functions.\nThis can be set via the fns `use_sample_defaults`, `with_sample_defaults`, `use_merged_sample_defaults` and `with_merged_sample_defaults`.",
    "summary": "Get current sample defaults",
    "examples": "use_sample_defaults amp: 0.5, cutoff: 80\n\nsample :loop_amen # Plays amen break with amp 0.5 and cutoff 80\n\nputs current_sample_defaults #=> Prints {amp: 0.5, cutoff: 80}"
  },
  "midi_to_hz": {
    "doc": "Convert a midi note to hz",
    "summary": "MIDI to Hz conversion",
    "examples": "midi_to_hz(60) #=> 261.6256"
  },
  "current_debug": {
    "doc": "Returns the current debug setting (`true` or `false`).\nThis can be set via the fns `use_debug` and `with_debug`.",
    "summary": "Get current debug status",
    "examples": "puts current_debug # Print out the current debug setting"
  },
  "use_cent_tuning": {
    "doc": "Uniformly tunes your music by shifting all notes played by the specified number of cents. To shift up by a cent use a cent tuning of 1. To shift down use negative numbers. One semitone consists of 100 cents.\nSee `with_cent_tuning` for setting the cent tuning value only for a specific `do`/`end` block. To transpose entire semitones see `use_transpose`.",
    "summary": "Cent tuning",
    "examples": "play 50 # Plays note 50\n\nuse_cent_tuning 1\n\nplay 50 # Plays note 50.01"
  },
  "control": {
    "doc": "Control a running synth node by passing new parameters to it. A synth node represents a running synth and can be obtained by assigning the return value of a call to play or sample or by specifying a parameter to the do/end block of an FX. You may modify any of the parameters you can set when triggering the synth, sample or FX. See documentation for opt details. If the synth to control is a chord, then control will change all the notes of that chord group at once to a new target set of notes - see example. Also, you may use the on: opt to conditionally trigger the control - see the docs for the `synth` and `sample` fns for more information.\nIf no synth to control is specified, then the last synth triggered by the current (or parent) thread will be controlled - see example below.",
    "summary": "Control running synth",
    "examples": "## Basic control\n\nmy_node = play 50, release: 5, cutoff: 60 # play note 50 with release of 5 and cutoff of 60. Assign return value to variable my_node\n\nsleep 1 # Sleep for a second\n\ncontrol my_node, cutoff: 70 # Now modify cutoff from 60 to 70, sound is still playing\n\nsleep 1 # Sleep for another second\n\ncontrol my_node, cutoff: 90 # Now modify cutoff from 70 to 90, sound is still playing\",\n\n        \"\n\n## Combining control with slide opts allows you to create nice transitions.\n\ns = synth :prophet, note: :e1, cutoff: 70, cutoff_slide: 8, release: 8 # start synth and specify slide time for cutoff opt\n\ncontrol s, cutoff: 130 # Change the cutoff value with a control.\n\n                       # Cutoff will now slide over 8 beats from 70 to 130\",\n\n        \"\n\n## Use a short slide time and many controls to create a sliding melody\n\nnotes = (scale :e3, :minor_pentatonic, num_octaves: 2).shuffle # get a random ordering of a scale\n\ns = synth :beep, note: :e3, sustain: 8, note_slide: 0.05 # Start our synth running with a long sustain and short note slide time\n\n64.times do\n\n  control s, note: notes.tick                            # Keep quickly changing the note by ticking through notes repeatedly\n\n  sleep 0.125\n\nend\n\n\",\n\n        \"\n\n## Controlling FX\n\nwith_fx :bitcrusher, sample_rate: 1000, sample_rate_slide: 8 do |bc| # Start FX but also use the handy || goalposts\n\n                                                                     # to grab a handle on the running FX. We can call\n\n                                                                     # our handle anything we want. Here we've called it bc\n\n  sample :loop_garzul, rate: 1\n\n  control bc, sample_rate: 5000                                      # We can use our handle bc now just like we used s in the\n\n                                                                     # previous example to modify the FX as it runs.\n\nend\",\n\n        \"\n\n## Controlling chords\n\ncg = play (chord :e4, :minor), sustain: 2  # start a chord\n\nsleep 1\n\ncontrol cg, notes: (chord :c3, :major)     # transition to new chord.\n\n                                           # Each note in the original chord is mapped onto\n\n                                           # the equivalent in the new chord.\n\n\",\n\n        \"\n\n## Sliding between chords\n\ncg = play (chord :e4, :minor), sustain: 4, note_slide: 3  # start a chord\n\nsleep 1\n\ncontrol cg, notes: (chord :c3, :major)                    # slide to new chord.\n\n                                                          # Each note in the original chord is mapped onto\n\n                                                          # the equivalent in the new chord.\n\n\",\n\n        \"\n\n## Sliding from a larger to smaller chord\n\ncg = play (chord :e3, :m13), sustain: 4, note_slide: 3  # start a chord with 7 notes\n\nsleep 1\n\ncontrol cg, notes: (chord :c3, :major)                    # slide to new chord with fewer notes (3)\n\n                                                          # Each note in the original chord is mapped onto\n\n                                                          # the equivalent in the new chord using ring-like indexing.\n\n                                                          # This means that the 4th note in the original chord will\n\n                                                          # be mapped onto the 1st note in the second chord and so-on.\n\n\",\n\n        \"\n\n## Sliding from a smaller to larger chord\n\ncg = play (chord :c3, :major), sustain: 4, note_slide: 3  # start a chord with 3 notes\n\nsleep 1\n\ncontrol cg, notes: (chord :e3, :m13)                     # slide to new chord with more notes (7)\n\n                                                          # Each note in the original chord is mapped onto\n\n                                                          # the equivalent in the new chord.\n\n                                                          # This means that the 4th note in the new chord\n\n                                                          # will not sound as there is no 4th note in the\n\n                                                          # original chord.\n\n\",\n\n        \"\n\n## Changing the slide rate\n\ns = synth :prophet, note: :e1, release: 8, cutoff: 70, cutoff_slide: 8 # Start a synth playing with a long cutoff slide\n\nsleep 1                                                                # wait a beat\n\ncontrol s, cutoff: 130                                                 # change the cutoff so it starts sliding slowly\n\nsleep 3                                                                # wait for 3 beats\n\ncontrol s, cutoff_slide: 1                                             # Change the cutoff_slide - the cutoff now slides more quickly to 130\n\n                                                                       # it will now take 1 beat to slide from its *current* value\n\n                                                                       # (somewhere between 70 and 130) to 130\n\n\",\n\n        \"\n\n## Controlling the last triggered synth\n\nsynth :prophet, note: :e1, release: 8                                  # Every time a synth is triggered, Sonic Pi automatically remembers the node\n\nsleep 1\n\n16.times do\n\n  control note: (octs :e1, 3).tick                                     # This means we don't need to use an explicit variable to control the synth\n\n  sleep 0.125                                                          # we last triggered.\n\nend\",\n\n        \"\n\n## Controlling multiple synths without variables\n\nsynth :beep, release: 4                  # Trigger a beep synth\n\nsleep 0.1\n\ncontrol note: :e5                        # Control last triggered synth (:beep)\n\nsleep 0.5\n\nsynth :dsaw, release: 4                  # Next, trigger a dsaw synth\n\nsleep 0.1\n\ncontrol note: :e4                        # Control last triggered synth (:dsaw)\n\n"
  },
  "spread": {
    "doc": "Creates a new ring of boolean values which space a given number of accents as evenly as possible throughout a bar. This is an implementation of the process described in 'The Euclidean Algorithm Generates Traditional Musical Rhythms' (Toussaint 2005).",
    "summary": "Euclidean distribution for beats",
    "examples": "(spread 3, 8)    #=> (ring true, false, false, true, false, false, true, false) a spacing of 332\",\n\n        \"(spread 3, 8, rotate: 1) #=> (ring true, false, false, true, false, true, false, false) a spacing of 323\",\n\n        \"\n\n  # Easily create interesting polyrhythmic beats\n\n  live_loop :euclid_beat do\n\n    sample :elec_bong, amp: 1.5 if (spread 3, 8).tick # Spread 3 bongs over 8\n\n    sample :perc_snap, amp: 0.8 if (spread 7, 11).look # Spread 7 snaps over 11\n\n    sample :bd_haus, amp: 2 if (spread 1, 4).look # Spread 1 bd over 4\n\n    sleep 0.125\n\n  end\n\n  \",\n\n  \"\n\n  # Spread descriptions from\n\n  # 'The Euclidean Algorithm Generates Traditional Musical Rhythms' (Toussaint 2005).\n\n  (spread 2, 5)  # A thirteenth century Persian rhythm called Khafif-e-ramal.\n\n  (spread 3, 4)  # The archetypal pattern of the Cumbria from Columbia, as well\n\n                 # as a Calypso rhythm from Trinidad\n\n  (spread 3, 5)  # When started on the second onset, is another thirteenth\n\n                 # century Persian rhythm by the name of Khafif-e-ramal, as well\n\n                 # as a Romanian folk-dance rhythm.\n\n  (spread 3, 7)  # A ruchenitza rhythm used in a Bulgarian folk-dance.\n\n  (spread 3, 8)  # The Cuban tresillo pattern\n\n  (spread 4, 7)  # Another Ruchenitza Bulgarian folk-dance rhythm\n\n  (spread 4, 9)  # The Aksak rhythm of Turkey.\n\n  (spread 4, 11) # The metric pattern used by Frank Zappa in his piece Outside Now\n\n  (spread 5, 6)  # Yields the York-Samai pattern, a popular Arab rhythm, when\n\n                 # started on the second onset.\n\n  (spread 5, 7)  # The Nawakhat pattern, another popular Arab rhythm.\n\n  (spread 5, 8)  # The Cuban cinquillo pattern.\n\n  (spread 5, 9)  # A popular Arab rhythm called Agsag-Samai.\n\n  (spread 5, 11) # The metric pattern used by Moussorgsky in Pictures at an\n\n                 # Exhibition\n\n  (spread 5, 12) # The Venda clapping pattern of a South African children's\n\n                 # song.\n\n  (spread 5, 16) # The Bossa-Nova rhythm necklace of Brazil.\n\n  (spread 7, 8)  # A typical rhythm played on the Bendir (frame drum)\n\n  (spread 7, 12) # A common West African bell pattern.\n\n  (spread 7, 16) # A Samba rhythm necklace from Brazil.\n\n  (spread 9, 16) # A rhythm necklace used in the Central African Republic.\n\n  (spread 11, 24) # A rhythm necklace of the Aka Pygmies of Central Africa.\n\n  (spread 13, 24) # Another rhythm necklace of the Aka Pygmies of the upper\n\n                  # Sangha.\n\n  "
  },
  "hz_to_midi": {
    "doc": "Convert a frequency in hz to a midi note. Note that the result isn't an integer and there is a potential for some very minor rounding errors.",
    "summary": "Hz to MIDI conversion",
    "examples": "hz_to_midi(261.63) #=> 60.0003"
  },
  "ramp": {
    "doc": "Create a new immutable ramp vector from args. Indexes always return first or last value if out of bounds.",
    "summary": "Create a ramp vector",
    "examples": "(ramp 1, 2, 3)[0] #=> 1\",\n\n        \"(ramp 1, 2, 3)[1] #=> 2\",\n\n        \"(ramp 1, 2, 3)[2] #=> 3\",\n\n        \"(ramp 1, 2, 3)[3] #=> 3\",\n\n        \"(ramp 1, 2, 3)[1000] #=> 3\",\n\n        \"(ramp 1, 2, 3)[-1] #=> 1\",\n\n        \"(ramp 1, 2, 3)[-1000] #=> 1"
  },
  "sample_names": {
    "doc": "Return a ring of sample names for the specified group",
    "summary": "Get sample names"
  },
  "choose": {
    "doc": "Choose an element at random from a list (array).",
    "summary": "Random list selection",
    "examples": "  loop do\n\n    play choose([60, 64, 67]) #=> plays one of 60, 64 or 67 at random\n\n    sleep 1\n\n    play chord(:c, :major).choose #=> You can also call .choose on the list\n\n    sleep 1\n\n  end"
  },
  "stop": {
    "doc": "Stops the current thread or if not in a thread, stops the current run. Does not stop any running synths triggered previously in the run/thread or kill any existing sub-threads.",
    "summary": "Stop current thread or run",
    "examples": "  sample :loop_amen #=> this sample is played until completion\n\n  sleep 0.5\n\n  stop                #=> signal to stop executing this run\n\n  sample :loop_garzul #=> this never executes\n\n  \",\n\n  \"\n\n  in_thread do\n\n    play 60      #=> this note plays\n\n    stop\n\n    sleep 0.5    #=> this sleep never happens\n\n    play 72      #=> this play never happens\n\n  end\n\n  play 80  #=> this plays as the stop only affected the above thread\",\n\n  \"\n\n  # Stopping live loops\n\n  live_loop :foo\n\n    sample :bd_haus\n\n    sleep 1\n\n    stop               # live loop :foo will now stop and no longer loop\n\n  end\n\n  live_loop :bar       # live loop :bar will continue looping\n\n    sample :elec_blip\n\n    sleep 0.25\n\n  end"
  },
  "current_arg_checks": {
    "doc": "Returns the current arg checking setting (`true` or `false`).\nThis can be set via the fns `use_arg_checks` and `with_arg_checks`.",
    "summary": "Get current arg checking status",
    "examples": "puts current_arg_checks # Print out the current arg check setting"
  },
  "sample_duration": {
    "doc": "Given the name of a loaded sample, or a path to a `.wav`, `.wave`, `.aif`, `.aiff` or `.flac` file returns the length of time in beats that the sample would play for. `sample_duration` understands and accounts for all the opts you can pass to `sample` which have an effect on the playback duration such as `rate:`. The time returned is scaled to the current BPM.\n*Note:* avoid using `sample_duration` to set the sleep time in `live_loop`s, prefer stretching the sample with the `beat_stretch:` opt or changing the BPM instead. See the examples below for details.",
    "summary": "Get duration of sample in beats",
    "examples": "# Simple use\n\nputs sample_duration(:loop_garzul) # returns 8.0 because this sample is 8 seconds long\n\n\",\n\n\"\n\n# The result is scaled to the current BPM\n\nuse_bpm 120\n\nputs sample_duration(:loop_garzul) # => 16.0\n\nuse_bpm 90\n\nputs sample_duration(:loop_garzul) # => 12.0\n\nuse_bpm 21\n\nputs sample_duration(:loop_garzul) # => 2.8\n\n\",\n\n\"\n\n# Avoid using sample_duration to set the sleep time in live_loops\n\nlive_loop :avoid_this do               # It is possible to use sample_duration to drive the frequency of a live loop.\n\n  with_fx :slicer do                   # However, if you're using a rhythmical sample such as a drum beat and it isn't\n\n    sample :loop_amen                  # in the same BPM as the current BPM, then the FX such as this slicer will be\n\n    sleep sample_duration(:loop_amen)  # badly out of sync. This is because the slicer slices at the current BPM and\n\n  end                                  # this live_loop is looping at a different BPM (that of the sample)\n\nend\n\nlive_loop :prefer_this do              # Instead prefer to set the BPM of the live_loop to match the sample. It has\n\n  use_sample_bpm :loop_amen            # two benefits. Now our sleep is a nice and simple 1 (as it's one beat).\n\n  with_fx :slicer do                   # Also, our slicer now works with the beat and sounds much better.\n\n    sample :loop_amen\n\n    sleep 1\n\n  end\n\nend\n\nlive_loop :or_this do                  # Alternatively we can beat_stretch the sample to match the current BPM. This has the\n\n  with_fx :slicer do                   # side effect of changing the rate of the sample (and hence the pitch). However, the\n\n    sample :loop_amen, beat_stretch: 1 # FX works nicely in time and the sleep time is also a simple 1.\n\n    sleep 1\n\n  end\n\nend\n\n\",\n\n\"\n\n# The standard sample opts are also honoured\n\n                                                                  # Playing a sample at standard speed will return standard length\n\nsample_duration :loop_garzul, rate: 1                             # => 8.0\n\n                                                                  # Playing a sample at half speed will double duration\n\nsample_duration :loop_garzul, rate: 0.5                           # => 16.0\n\n                                                                  # Playing a sample at double speed will halve duration\n\nsample_duration :loop_garzul, rate: 2                             # => 4.0\n\n                                                                  # Playing a sample backwards at double speed will halve duration\n\nsample_duration :loop_garzul, rate: -2                            # => 4.0\n\n                                                                  # Without an explicit sustain: opt attack: just affects amplitude not duration\n\nsample_duration :loop_garzul, attack: 1                           # => 8.0\n\nsample_duration :loop_garzul, attack: 100                         # => 8.0\n\nsample_duration :loop_garzul, attack: 0                           # => 8.0\n\n                                                                  # Without an explicit sustain: opt release: just affects amplitude not duration\n\nsample_duration :loop_garzul, release: 1                          # => 8.0\n\nsample_duration :loop_garzul, release: 100                        # => 8.0\n\nsample_duration :loop_garzul, release: 0                          # => 8.0\n\n                                                                  # Without an explicit sustain: opt decay: just affects amplitude not duration\n\nsample_duration :loop_garzul, decay: 1                            # => 8.0\n\nsample_duration :loop_garzul, decay: 100                          # => 8.0\n\nsample_duration :loop_garzul, decay: 0                            # => 8.0\n\n                                                                  # With an explicit sustain: opt, if the attack + decay + sustain + release envelope\n\n                                                                  # duration is less than the sample duration time, the envelope will shorten the\n\n                                                                  # sample time.\n\nsample_duration :loop_garzul, sustain: 0, attack: 0.5             # => 0.5\n\nsample_duration :loop_garzul, sustain: 0, decay: 0.1              # => 0.1\n\nsample_duration :loop_garzul, sustain: 0, release: 1              # => 1.0\n\nsample_duration :loop_garzul, sustain: 2, attack: 0.5, release: 1 # => 3.5\n\n                                                                  # If the envelope duration is longer than the sample it will not affect the\n\n                                                                  # sample duration\n\nsample_duration :loop_garzul, sustain: 0, attack: 8, release: 3   # => 8\n\n                                                                  # All other opts are taken into account before the comparison with the envelope opts.\n\nsample_duration :loop_garzul, rate: 10                            # => 0.8\n\nsample_duration :loop_garzul, sustain: 0, attack: 0.9, rate: 10   # => 0.8 (The duration of the sample is less than the envelope length so wins)\n\n                                                                  # The rpitch: opt will modify the rate to shift the pitch of the sample up and down\n\n                                                                  # and therefore affects duration.\n\nsample_duration :loop_garzul, rpitch: 12                          # => 4.0\n\nsample_duration :loop_garzul, rpitch: -12                         # => 16\n\n                                                                  # The rpitch: and rate: opts combine together.\n\nsample_duration :loop_garzul, rpitch: 12, rate: 2                 # => 2.0\n\n                                                                  # The beat_stretch: opt stretches the sample so that its duration matches the value.\n\n                                                                  # It also combines with rate:\n\nsample_duration :loop_garzul, beat_stretch: 3                     # => 3.0\n\nsample_duration :loop_garzul, beat_stretch: 3, rate: 0.5          # => 6.0\n\n                                                                  # The pitch_stretch: opt acts identically to beat_stretch when just considering sample\n\n                                                                  # duration.\n\nsample_duration :loop_garzul, pitch_stretch: 3                    # => 3.0\n\nsample_duration :loop_garzul, pitch_stretch: 3, rate: 0.5         # => 6.0\n\n                                                                  # The start: and finish: opts can also shorten the sample duration and also combine\n\n                                                                  # with other opts such as rate:\n\nsample_duration :loop_garzul, start: 0.5                          # => 4.0\n\nsample_duration :loop_garzul, start: 0.5, finish: 0.75            # => 2.0\n\nsample_duration :loop_garzul, finish: 0.5, start: 0.75            # => 2.0\n\nsample_duration :loop_garzul, rate: 2, finish: 0.5, start: 0.75 # => 1.0\n\n\",\n\n\"\n\n# Triggering samples one after another\n\nsample :loop_amen                    # start the :loop_amen sample\n\nsleep sample_duration(:loop_amen)    # wait for the duration of :loop_amen before\n\nsample :loop_amen                    # starting it again\n\n"
  },
  "recording_start": {
    "doc": "Start recording all sound to a `.wav` file stored in a temporary directory.",
    "summary": "Start recording"
  },
  "clear": {
    "doc": "All settings such as the current synth, BPM, random stream and tick values will be reset to their defaults. Consider using `reset` to reset all these values to those inherited from the parent thread.",
    "summary": "Clear all thread locals to defaults",
    "examples": "Clear wipes out the threads locals\n\nuse_synth :blade\n\nuse_octave 3\n\nputs \\\"before\\\"         #=> \\\"before\\\"\n\nputs current_synth      #=> :blade\n\nputs current_octave     #=> 3\n\nputs rand               #=> 0.75006103515625\n\nputs tick               #=> 0\n\nat do\n\n  use_synth :tb303\n\n  puts rand               #=> 0.9287109375\n\n  clear\n\n  puts \\\"thread\\\"         #=> \\\"thread\\\"\n\n                          # The clear reset the current synth to the default\n\n                          # of :beep. We are therefore ignoring any inherited\n\n                          # synth settings. It is as if the thread was a completely\n\n                          # new Run.\n\n  puts current_synth      #=> :beep\n\n                          # The current octave defaults back to 0\n\n  puts current_octave     #=> 0\n\n                          # The random stream defaults back to the standard\n\n                          # stream used by every new Run.\n\n  puts rand               #=> 0.75006103515625\n\n  puts tick               #=> 0\n\nend"
  },
  "load_example": {
    "doc": "Given a keyword representing an example, will load it into the current buffer. This will replace any previous content.",
    "summary": "Load a built-in example",
    "examples": "load_example :rerezzed # will replace content of current buffer with the rerezzed example"
  },
  "cue": {
    "doc": "Send a heartbeat synchronisation message containing the (virtual) timestamp of the current thread. Useful for syncing up external threads via the `sync` fn. Any opts which are passed are given to the thread which syncs on the `cue_id` as a map. The values of the opts must be immutable. Currently only numbers, symbols and booleans are supported.",
    "summary": "Cue other threads",
    "examples": "  in_thread do\n\n    sync :foo # this parks the current thread waiting for a foo cue message to be received.\n\n    sample :ambi_lunar_land\n\n  end\n\n  sleep 5\n\n  cue :foo # We send a cue message from the main thread.\n\n            # This then unblocks the thread above and we then hear the sample\",\n\n  \"\n\n  in_thread do   # Start a metronome thread\n\n    loop do      # Loop forever:\n\n      cue :tick  # sending tick heartbeat messages\n\n      sleep 0.5  # and sleeping for 0.5 beats between ticks\n\n    end\n\n  end\n\n  # We can now play sounds using the metronome.\n\n  loop do                    # In the main thread, just loop\n\n    sync :tick               # waiting for :tick cue messages\n\n    sample :drum_heavy_kick  # after which play the drum kick sample\n\n  end\",\n\n  \"\n\n  in_thread do   # Start a metronome thread\n\n    loop do      # Loop forever:\n\n      cue [:foo, :bar, :baz].choose # sending one of three tick heartbeat messages randomly\n\n      sleep 0.5  # and sleeping for 0.5 beats between ticks\n\n    end\n\n  end\n\n  # We can now play sounds using the metronome:\n\n  in_thread do\n\n    loop do              # In the main thread, just loop\n\n      sync :foo          # waiting for :foo cue messages\n\n      sample :elec_beep  # after which play the elec beep sample\n\n    end\n\n  end\n\n  in_thread do\n\n    loop do              # In the main thread, just loop\n\n      sync :bar          # waiting for :bar cue messages\n\n      sample :elec_flip  # after which play the elec flip sample\n\n    end\n\n  end\n\n  in_thread do\n\n    loop do              # In the main thread, just loop\n\n      sync :baz          # waiting for :baz cue messages\n\n      sample :elec_blup  # after which play the elec blup sample\n\n    end\n\n  end\",\n\n  \"\n\n  in_thread do\n\n    loop do\n\n      cue :tick, foo: 64  # sending tick heartbeat messages with a value :foo\n\n      sleep 0.5\n\n    end\n\n  end\n\n  # The value for :foo can now be used in synced threads\n\n  loop do\n\n    values = sync :tick\n\n    play values[:foo]    # play the note value from :foo\n\n  end"
  },
  "comment": {
    "doc": "Does not evaluate any of the code within the block. However, any optional args passed before the block *will* be evaluated although they will be ignored. See `uncomment` for switching commenting off without having to remove the comment form.",
    "summary": "Block level commenting",
    "examples": "  comment do # starting a block level comment:\n\n    play 50 # not played\n\n    sleep 1 # no sleep happens\n\n    play 62 # not played\n\n  end"
  },
  "assert": {
    "doc": "Raises an exception if the argument is either nil or false.",
    "summary": "Ensure arg is valid",
    "examples": "# Simple assertions\n\nassert true   # As true is neither nil or false, this assertion passes\n\nassert 1      # Similarly, 1 passes\n\nassert \\\"foo\\\" # As do string\n\nassert false  # This will raise an exception\n\n\",\n\n\"\n\n# Communicating error messages\n\nassert false, \\\"oops\\\" # This will raise an exception containing the message \\\"oops\\\"\n\n\",\n\n\"\n\n# More interesting assertions\n\nassert (1 + 1) == 2 # Ensure that arithmetic is sane!\n\nassert [:a, :b, :c].size == 3 # ensure lists can be correctly counted\n\n"
  },
  "dice": {
    "doc": "Throws a dice with the specified num_sides (defaults to `6`) and returns the score as a number between `1` and `num_sides`.",
    "summary": "Random dice throw",
    "examples": "  dice # will return a number between 1 and 6 inclusively\n\n       # (with an even probability distribution).\",\n\n  \"\n\n  dice 3 # will return a number between 1 and 3 inclusively"
  },
  "spark_graph": {
    "doc": "Given a list of numeric values, this method turns them into a string of bar heights. Useful for quickly graphing the shape of an array. Remember to use puts so you can see the output. See `spark` for a simple way of printing a spark graph.",
    "summary": "Returns a string representing a list of numeric values as a spark graph/bar chart",
    "examples": "puts (spark_graph (range 1, 5))    #=> ▁▃▅█\",\n\n  \"puts (spark_graph (range 1, 5).shuffle) #=> ▃█▅▁"
  },
  "current_synth": {
    "doc": "Returns the current synth name.\nThis can be set via the fns `use_synth` and `with_synth`.",
    "summary": "Get current synth",
    "examples": "puts current_synth # Print out the current synth name"
  },
  "sample_buffer": {
    "doc": "Alias for the `load_sample` method. Loads sample if necessary and returns buffer information.",
    "summary": "Get sample data",
    "examples": "see load_sample"
  },
  "sleep": {
    "doc": "Wait for a number of beats before triggering the next command. Beats are converted to seconds by scaling to the current bpm setting.",
    "summary": "Wait for beat duration",
    "examples": "  # Without calls to sleep, all sounds would happen at once:\n\n  play 50  # This is actually a chord with all notes played simultaneously\n\n  play 55\n\n  play 62\n\n  sleep 1  # Create a gap, to allow a moment's pause for reflection...\n\n  play 50  # Let's try the chord again, but this time with sleeps:\n\n  sleep 0.5 # With the sleeps, we turn a chord into an arpeggio\n\n  play 55\n\n  sleep 0.5\n\n  play 62\",\n\n  \"\n\n  # The amount of time sleep pauses for is scaled to match the current bpm. The default bpm is 60. Let's double it:\n\n  use_bpm 120\n\n  play 50\n\n  sleep 1 # This actually sleeps for 0.5 seconds as we're now at double speed\n\n  play 55\n\n  sleep 1\n\n  play 62\n\n  # Let's go down to half speed:\n\n  use_bpm 30\n\n  play 50\n\n  sleep 1 # This now sleeps for 2 seconds as we're now at half speed.\n\n  play 55\n\n  sleep 1\n\n  play 62\n\n  "
  },
  "use_tuning": {
    "doc": "In most music we make semitones by dividing the octave into 12 equal parts, which is known as equal temperament. However there are lots of other ways to tune the 12 notes. This method adjusts each midi note into the specified tuning system. Because the ratios between notes aren't always equal, be careful to pick a centre note that is in the key of the music you're making for the best sound. Currently available tunings are `:just`, `:pythagorean`, `:meantone` and the default of `:equal`",
    "summary": "Use alternative tuning systems",
    "examples": "play :e4 # Plays note 64\n\nuse_tuning :just, :c\n\nplay :e4 # Plays note 63.8631\n\n# transparently changes midi notes too\n\nplay 64 # Plays note 63.8631\",\n\n        \"\n\n# You may change the tuning multiple times:\n\nplay 64 # Plays note 64\n\nuse_tuning :just\n\nplay 64 # Plays note 63.8631\n\nuse_tuning :equal\n\nplay 64 # Plays note 64"
  },
  "use_bpm": {
    "doc": "Sets the tempo in bpm (beats per minute) for everything afterwards. Affects all subsequent calls to `sleep` and all temporal synth arguments which will be scaled to match the new bpm. If you wish to bypass scaling in calls to sleep, see the fn `rt`. Also, if you wish to bypass time scaling in synth args see `use_arg_bpm_scaling`. See also `with_bpm` for a block scoped version of `use_bpm`.\nFor dance music here's a rough guide for which BPM to aim for depending on your genre:\n* Dub: 60-90 bpm\n* Hip-hop: 60-100 bpm\n* Downtempo: 90-120 bpm\n* House: 115-130 bpm\n* Techno/trance: 120-140 bpm\n* Dubstep: 135-145 bpm\n* Drum and bass: 160-180 bpm",
    "summary": "Set the tempo",
    "examples": "  # default tempo is 60 bpm\n\n  4.times do\n\n    play 50, attack: 0.5, release: 0.25 # attack is 0.5s and release is 0.25s\n\n    sleep 1 # sleep for 1 second\n\n  end\n\n  sleep 2  # sleep for 2 seconds\n\n  # Let's make it go faster...\n\n  use_bpm 120  # double the bpm\n\n  4.times do\n\n    play 62, attack: 0.5, release: 0.25 # attack is scaled to 0.25s and release is now 0.125s\n\n    sleep 1 # actually sleeps for 0.5 seconds\n\n  end\n\n  sleep 2 # sleep for 1 second\n\n  # Let's make it go even faster...\n\n  use_bpm 240  #  bpm is 4x original speed!\n\n  8.times do\n\n    play 62, attack: 0.5, release: 0.25 # attack is scaled to 0.125s and release is now 0.0625s\n\n    sleep 1 # actually sleeps for 0.25 seconds\n\n  end\n\n  "
  },
  "synth": {
    "doc": "Trigger specified synth with given opts. Bypasses `current_synth` value, yet still honours `current_synth_defaults`. When using `synth`, the note is no longer an explicit argument but an opt with the key `note:`.\nIf note: opt is `nil`, `:r` or `:rest`, play is ignored and treated as a rest. Also, if the `on:` opt is specified and returns `false`, or `nil` then play is similarly ignored and treated as a rest.\nIf the synth name is `nil` behaviour is identical to that of `play` in that the `current_synth` will determine the actual synth triggered.\nIf a block is given, it is assumed to take one arg which will be the controllable synth node and the body of the block is run in an implicit `in_thread`. This allows for asynchronous control of the synth without interferring with time. For synchronous control capture the result of `synth` as a variable and use that.\nNote that the default opts listed are only a guide to the most common opts across all the synths. Not all synths support all the default opts and each synth typically supports many more opts specific to that synth. For example, the `:tb303` synth supports 45 unique opts. For a full list of a synth's opts see its documentation in the Help system. This can be accessed directly by clicking on the name of the synth and using the shortcut `C-i`",
    "summary": "Trigger specific synth",
    "examples": "\n\nuse_synth :beep            # Set current synth to :beep\n\nplay 60                    # Play note 60 with opt defaults\n\nsynth :dsaw, note: 60    # Bypass current synth and play :dsaw\n\n                         # with note 60 and opt defaults \",\n\n\"\n\nsynth :fm, note: 60, amp: 0.5 # Play note 60 of the :fm synth with an amplitude of 0.5\",\n\n        \"\n\nuse_synth_defaults release: 5\n\nsynth :dsaw, note: 50 # Play note 50 of the :dsaw synth with a release of 5\",\n\n\"# You can play chords with the notes: opt:\n\nsynth :dsaw, notes: (chord :e3, :minor)\",\n\n\"\n\n# on: vs if\n\nnotes = (scale :e3, :minor_pentatonic, num_octaves: 2)\n\nlive_loop :rhyth do\n\n  8.times do\n\n    trig = (spread 3, 7).tick(:rhyth)\n\n    synth :tri, on: trig, note: notes.tick, release: 0.1  # Here, we're calling notes.tick\n\n                                                          # every time we attempt to play the synth\n\n                                                          # so the notes rise faster than rhyth2\n\n    sleep 0.125\n\n  end\n\nend\n\nlive_loop :rhyth2 do\n\n  8.times do\n\n    trig = (spread 3, 7).tick(:rhyth)\n\n    synth :saw, note: notes.tick, release: 0.1 if trig  # Here, we're calling notes.tick\n\n                                                        # only when the spread says to play\n\n                                                        # so the notes rise slower than rhyth\n\n    sleep 0.125\n\n  end\n\nend\n\n\",\n\n\" # controlling a synth synchronously\n\ns = synth :beep, note: :e3, release: 4\n\nsleep 1\n\ncontrol s, note: :e5\n\nsleep 0.5\n\nsynth :dsaw, note: :e3   # This is triggered after 1.5s from start\",\n\n\" # Controlling a synth asynchronously\n\nsynth :beep, note: :e3, release: 4 do |s|\n\n  sleep 1                                               # This block is run in an implicit in_thread\n\n  control s, note: :e5                                  # and therefore is asynchronous\n\nend\n\nsleep 0.5\n\nsynth :dsaw, note: :e3 # This is triggered after 0.5s from start"
  },
  "current_bpm": {
    "doc": "Returns the current tempo as a bpm value.\nThis can be set via the fns `use_bpm`, `with_bpm`, `use_sample_bpm` and `with_sample_bpm`.",
    "summary": "Get current tempo",
    "examples": "  puts current_bpm # Print out the current bpm"
  },
  "fx_names": {
    "doc": "Return a list of all the FX available",
    "summary": "Get all FX names"
  },
  "sample_loaded": {
    "doc": "Given a path to a `.wav`, `.wave`, `.aif`, `.aiff` or `.flac` file, returns `true` if the sample has already been loaded.",
    "summary": "Test if sample was pre-loaded",
    "examples": "load_sample :elec_blip # :elec_blip is now loaded and ready to play as a sample\n\nputs sample_loaded? :elec_blip # prints true because it has been pre-loaded\n\nputs sample_loaded? :misc_burp # prints false because it has not been loaded"
  },
  "set_cent_tuning": {
    "doc": "Globally tune Sonic Pi to play with another external instrument.\nUniformly tunes your music by shifting all notes played by the specified number of cents. To shift up by a cent use a cent tuning of 1. To shift down use negative numbers. One semitone consists of 100 cents.\nSee `use_cent_tuning` for setting the cent tuning value locally for a specific thread or `live_loop`. This is a global value and will shift the tuning for *all* notes. It will also persist for the entire session.\nImportant note: the cent tuning set by `set_cent_tuning!` is independent of any thread-local cent tuning values set by `use_cent_tuning` or `with_cent_tuning`. ",
    "summary": "Global Cent tuning",
    "examples": "play 50 # Plays note 50\n\nset_cent_tuning! 1\n\nplay 50 # Plays note 50.01"
  },
  "use_transpose": {
    "doc": "Transposes your music by shifting all notes played by the specified amount. To shift up by a semitone use a transpose of 1. To shift down use negative numbers. See `with_transpose` for setting the transpose value only for a specific `do`/`end` block. To transpose entire octaves see `use_octave`.",
    "summary": "Note transposition",
    "examples": "play 50 # Plays note 50\n\nuse_transpose 1\n\nplay 50 # Plays note 51\",\n\n        \"\n\n# You may change the transposition multiple times:\n\nplay 62 # Plays note 62\n\nuse_transpose -12\n\nplay 62 # Plays note 50\n\nuse_transpose 3\n\nplay 62 # Plays note 65"
  },
  "set_sched_ahead_time": {
    "doc": "Specify how many seconds ahead of time the synths should be triggered. This represents the amount of time between pressing 'Run' and hearing audio. A larger time gives the system more room to work with and can reduce performance issues in playing fast sections on slower platforms. However, a larger time also increases latency between modifying code and hearing the result whilst live coding.",
    "summary": "Set sched ahead time globally",
    "examples": "set_sched_ahead_time! 1 # Code will now run approximately 1 second ahead of audio."
  },
  "defonce": {
    "doc": "Allows you to assign the result of some code to a name, with the property that the code will only execute once - therefore stopping re-definitions. This is useful for defining values that you use in your compositions but you don't want to reset every time you press run. You may force the block to execute again regardless of whether or not it has executed once already by using the override option (see examples).",
    "summary": "Define a named value only once",
    "examples": "  defonce :foo do  # Define a new function called foo\n\n    sleep 1        # Sleep for a beat in the function definition. Note that this amount\n\n                   # of time in seconds will depend on the current BPM of the live_loop\n\n                   # or thread calling this function.\n\n    puts \\\"hello\\\" # Print hello\n\n    10             # Return a value of 10\n\n  end\n\n  # Call foo on its own\n\n  puts foo # The run sleeps for a beat and prints \\\"hello\\\" before returning 10\n\n  # Try it again:\n\n  puts foo # This time the run doesn't sleep or print anything out. However, 10 is still returned.\n\n  defonce :foo do # Try redefining foo\n\n    puts \\\"you can't redefine me\\\"\n\n    15\n\n  end\n\n  puts foo # We still don't see any printing or sleeping, and the result is still 10\n\n  # You can use foo anywhere you would use normal code.\n\n  # For example, in a block:\n\n  3.times do\n\n    play foo  # play 10\n\n  end\",\n\n  \"\n\n  defonce :bar do\n\n    50\n\n  end\n\n  play bar # plays 50\n\n  defonce :bar do # This redefinition doesn't work due to the behaviour of defonce\n\n    70\n\n  end\n\n  play bar # Still plays 50\n\n  defonce :bar, override: true do  # Force definition to take place with override option\n\n    80\n\n  end\n\n  play bar # plays 80"
  },
  "current_sched_ahead_time": {
    "doc": "Returns the current schedule ahead time.\nThis can be set via the fn `set_sched_ahead_time!`.",
    "summary": "Get current sched ahead time",
    "examples": "set_sched_ahead_time! 0.5\n\nputs current_sched_ahead_time # Prints 0.5"
  },
  "rt": {
    "doc": "Real time representation. Returns the amount of beats for the value in real-time seconds. Useful for bypassing any bpm scaling",
    "summary": "Real time conversion",
    "examples": "  use_bpm 120  # modifies all time to be half\n\n  play 50\n\n  sleep 1      # actually sleeps for half of a second\n\n  play 62\n\n  sleep rt(1)  # bypasses bpm scaling and sleeps for a second\n\n  play 72"
  },
  "use_arg_checks": {
    "doc": "When triggering synths, each argument is checked to see if it is sensible. When argument checking is enabled and an argument isn't sensible, you'll see an error in the debug pane. This setting allows you to explicitly enable and disable the checking mechanism. See with_arg_checks for enabling/disabling argument checking only for a specific `do`/`end` block.",
    "summary": "Enable and disable arg checks",
    "examples": "play 50, release: 5 # Args are checked\n\nuse_arg_checks false\n\nplay 50, release: 5 # Args are not checked"
  },
  "puts": {
    "doc": "Displays the information you specify as a string inside the output pane. This can be a number, symbol, or a string itself. Useful for debugging. Synonym for `print`.",
    "summary": "Display a message in the output pane",
    "examples": "print \\\"hello there\\\"   #=> will print the string \\\"hello there\\\" to the output pane\",\n\n  \"print 5               #=> will print the number 5 to the output pane\",\n\n  \"print foo             #=> will print the contents of foo to the output pane"
  },
  "recording_delete": {
    "doc": "After using `recording_start` and `recording_stop`, a temporary file is created until you decide to use `recording_save`. If you've decided you don't want to save it you can use this method to delete the temporary file straight away, otherwise the operating system will take care of deleting it later."
  },
  "sample_info": {
    "doc": "Alias for the `load_sample` method. Loads sample if necessary and returns sample information.",
    "summary": "Get sample information",
    "examples": "see load_sample"
  },
  "set_mixer_control": {
    "doc": "The master mixer is the final mixer that all sound passes through. This fn gives you control over the master mixer allowing you to manipulate all the sound playing through Sonic Pi at once. For example, you can sweep a lpf or hpf over the entire sound. You can reset the controls back to their defaults with `reset_mixer!`.",
    "summary": "Control master mixer",
    "examples": "set_mixer_control! lpf: 30, lpf_slide: 16 # slide the global lpf to 30 over 16 beats."
  },
  "use_random_seed": {
    "doc": "Resets the random number generator to the specified seed. All subsequently generated random numbers and randomisation functions such as `shuffle` and `choose` will use this new generator and the current generator is discarded. Use this to change the sequence of random numbers in your piece in a way that can be reproduced. Especially useful if combined with iteration. See examples.",
    "summary": "Set random seed generator to known seed",
    "examples": "  ## Basic usage\n\n  use_random_seed 1 # reset random seed to 1\n\n  puts rand # => 0.417022004702574\n\n  use_random_seed 1 # reset random seed back to 1\n\n  puts rand  #=> 0.417022004702574\n\n  \",\n\n  \"\n\n  ## Generating melodies\n\n  notes = (scale :eb3, :minor_pentatonic)  # Create a set of notes to choose from.\n\n                                           # Scales work well for this\n\n  with_fx :reverb do\n\n    live_loop :repeating_melody do         # Create a live loop\n\n      use_random_seed 300                  # Set the random seed to a known value every\n\n                                           # time around the loop. This seed is the key\n\n                                           # to our melody. Try changing the number to\n\n                                           # something else. Different numbers produce\n\n                                           # different melodies\n\n      8.times do                           # Now iterate a number of times. The size of\n\n                                           # the iteration will be the length of the\n\n                                           # repeating melody.\n\n        play notes.choose, release: 0.1    # 'Randomly' choose a note from our ring of\n\n                                           # notes. See how this isn't actually random\n\n                                           # but uses a reproducible method! These notes\n\n                                           # are therefore repeated over and over...\n\n        sleep 0.125\n\n      end\n\n    end\n\n  end\n\n  "
  },
  "reset": {
    "doc": "All settings such as the current synth, BPM, random stream and tick values will be reset to the values inherited from the parent thread. Consider using `clear` to reset all these values to their defaults.",
    "summary": "Reset all thread locals",
    "examples": "# Basic Reset\n\nuse_synth :blade\n\nuse_octave 3\n\nputs \\\"before\\\"         #=> \\\"before\\\"\n\nputs current_synth      #=> :blade\n\nputs current_octave     #=> 3\n\nputs rand               #=> 0.75006103515625\n\nputs tick               #=> 0\n\nreset\n\nputs \\\"after\\\"          #=> \\\"after\\\"\n\nputs current_synth      #=> :beep\n\nputs current_octave     #=> 0\n\nputs rand               #=> 0.75006103515625\n\nputs tick               #=> 0\",\n\n\"Reset remembers defaults from when the thread was created:\n\nuse_synth :blade\n\nuse_octave 3\n\nputs \\\"before\\\"         #=> \\\"before\\\"\n\nputs current_synth      #=> :blade\n\nputs current_octave     #=> 3\n\nputs rand               #=> 0.75006103515625\n\nputs tick               #=> 0\n\nat do\n\n  use_synth :tb303\n\n  puts rand               #=> 0.9287109375\n\n  reset\n\n  puts \\\"thread\\\"          #=> \\\"thread\\\"\n\n                          # The call to reset ensured that the current\n\n                          # synth was returned to the the state at the\n\n                          # time this thread was started. Thus any calls\n\n                          # to use_synth between this line and the start\n\n                          # of the thread are ignored\n\n  puts current_synth      #=> :blade\n\n  puts current_octave     #=> 3\n\n                          # The call to reset ensured\n\n                          # that the random stream was reset\n\n                          # to the same state as it was when\n\n                          # the current thread was started\n\n  puts rand               #=> 0.9287109375\n\n  puts tick               #=> 0\n\nend"
  },
  "ring": {
    "doc": "Create a new immutable ring buffer from args. Indexes wrap around positively and negatively",
    "summary": "Create a ring buffer",
    "examples": "(ring 1, 2, 3)[0] #=> 1\",\n\n        \"(ring 1, 2, 3)[1] #=> 2\",\n\n        \"(ring 1, 2, 3)[3] #=> 1\",\n\n        \"(ring 1, 2, 3)[-1] #=> 3"
  },
  "inc": {
    "doc": "Increment a number by `1`. Equivalent to `n + 1`",
    "summary": "Increment",
    "examples": "inc 1 # returns 2\",\n\n        \"inc -1 # returns 0"
  },
  "scale": {
    "doc": "Creates a ring of MIDI note numbers when given a tonic note and a scale name. Also takes an optional `num_octaves:` parameter (octave `1` is the default). If only passed the scale name, the tonic defaults to 0. See examples.",
    "summary": "Create scale",
    "examples": "puts (scale :C, :major) # returns the following ring of MIDI note numbers: (ring 60, 62, 64, 65, 67, 69, 71, 72)\",\n\n        \"# anywhere you can use a list or ring of notes, you can also use scale\n\nplay_pattern (scale :C, :major)\",\n\n        \"# you can use the :num_octaves parameter to get more notes\n\nplay_pattern (scale :C, :major, num_octaves: 2)\",\n\n        \"# Scales can start with any note:\n\nputs (scale 50, :minor) #=> (ring 50, 52, 53, 55, 57, 58, 60, 62)\n\nputs (scale 50.1, :minor) #=> (ring 50.1, 52.1, 53.1, 55.1, 57.1, 58.1, 60.1, 62.1)\n\nputs (scale :minor) #=> (ring 0, 2, 3, 5, 7, 8, 10, 12)\",\n\n\" # scales are also rings\n\nlive_loop :scale_player do\n\n  play (scale :Eb3, :super_locrian).tick, release: 0.1\n\n  sleep 0.125\n\nend\",\n\n        \" # scales starting with 0 are useful in combination with sample's rpitch:\n\nlive_loop :scaled_sample do\n\n  sample :bass_trance_c, rpitch: (scale 0, :minor).tick\n\n  sleep 1\n\nend\",\n\n\"# Sonic Pi supports a large range of scales:\n\n(scale :C, :diatonic)\n\n(scale :C, :ionian)\n\n(scale :C, :major)\n\n(scale :C, :dorian)\n\n(scale :C, :phrygian)\n\n(scale :C, :lydian)\n\n(scale :C, :mixolydian)\n\n(scale :C, :aeolian)\n\n(scale :C, :minor)\n\n(scale :C, :locrian)\n\n(scale :C, :hex_major6)\n\n(scale :C, :hex_dorian)\n\n(scale :C, :hex_phrygian)\n\n(scale :C, :hex_major7)\n\n(scale :C, :hex_sus)\n\n(scale :C, :hex_aeolian)\n\n(scale :C, :minor_pentatonic)\n\n(scale :C, :yu)\n\n(scale :C, :major_pentatonic)\n\n(scale :C, :gong)\n\n(scale :C, :egyptian)\n\n(scale :C, :shang)\n\n(scale :C, :jiao)\n\n(scale :C, :zhi)\n\n(scale :C, :ritusen)\n\n(scale :C, :whole_tone)\n\n(scale :C, :whole)\n\n(scale :C, :chromatic)\n\n(scale :C, :harmonic_minor)\n\n(scale :C, :melodic_minor_asc)\n\n(scale :C, :hungarian_minor)\n\n(scale :C, :octatonic)\n\n(scale :C, :messiaen1)\n\n(scale :C, :messiaen2)\n\n(scale :C, :messiaen3)\n\n(scale :C, :messiaen4)\n\n(scale :C, :messiaen5)\n\n(scale :C, :messiaen6)\n\n(scale :C, :messiaen7)\n\n(scale :C, :super_locrian)\n\n(scale :C, :hirajoshi)\n\n(scale :C, :kumoi)\n\n(scale :C, :neapolitan_major)\n\n(scale :C, :bartok)\n\n(scale :C, :bhairav)\n\n(scale :C, :locrian_major)\n\n(scale :C, :ahirbhairav)\n\n(scale :C, :enigmatic)\n\n(scale :C, :neapolitan_minor)\n\n(scale :C, :pelog)\n\n(scale :C, :augmented2)\n\n(scale :C, :scriabin)\n\n(scale :C, :harmonic_major)\n\n(scale :C, :melodic_minor_desc)\n\n(scale :C, :romanian_minor)\n\n(scale :C, :hindu)\n\n(scale :C, :iwato)\n\n(scale :C, :melodic_minor)\n\n(scale :C, :diminished2)\n\n(scale :C, :marva)\n\n(scale :C, :melodic_major)\n\n(scale :C, :indian)\n\n(scale :C, :spanish)\n\n(scale :C, :prometheus)\n\n(scale :C, :diminished)\n\n(scale :C, :todi)\n\n(scale :C, :leading_whole)\n\n(scale :C, :augmented)\n\n(scale :C, :purvi)\n\n(scale :C, :chinese)\n\n(scale :C, :lydian_minor)\n\n"
  },
  "degree": {
    "doc": "For a given scale and tonic it takes a symbol `:i`, `:ii`, `:iii`, `:iv`,`:v`, `:vi`, `:vii` or a number `1`-`7` and resolves it to a midi note.",
    "summary": "Convert a degree into a note",
    "examples": "%Q{play degree(:ii, :D3, :major)\n\nplay degree(2, :C3, :minor)\n\n}"
  },
  "pitch_to_ratio": {
    "doc": "Convert a midi note to a ratio which when applied to a frequency will scale the frequency by the number of semitones. Useful for changing the pitch of a sample by using it as a way of generating the rate.",
    "summary": "relative MIDI pitch to frequency ratio",
    "examples": "pitch_to_ratio 12 #=> 2.0\",\n\n        \"pitch_to_ratio 1 #=> 1.05946\",\n\n        \"pitch_to_ratio -12 #=> 0.5\",\n\n        \"sample :ambi_choir, rate: pitch_to_ratio(3) # Plays :ambi_choir 3 semitones above default.\",\n\n        \"\n\n# Play a chromatic scale of semitones\n\n(range 0, 16).each do |n|                  # For each note in the range 0->16\n\n  sample :ambi_choir, rate: pitch_to_ratio(n) # play :ambi_choir at the relative pitch\n\n  sleep 0.5                                # and wait between notes\n\nend"
  },
  "at": {
    "doc": "Given a list of times, run the block once after waiting each given time. If passed an optional params list, will pass each param individually to each block call. If size of params list is smaller than the times list, the param values will act as rings (rotate through). If the block is given 1 arg, the times are fed through. If the block is given 2 args, both the times and the params are fed through. A third block arg will receive the index of the time.\nNote, all code within the block is executed in its own thread. Therefore despite inheriting all thread locals such as the random stream and ticks, modifications will be isolated to the block and will not affect external code.",
    "summary": "Asynchronous Time. Run a block at the given time(s)",
    "examples": "  at 4 do\n\n    sample :ambi_choir    # play sample after waiting for 4 beats\n\n  end\n\n  \",\n\n  \"\n\n  at [1, 2, 4] do  # plays a note after waiting 1 beat,\n\n    play 75           # then after 1 more beat,\n\n  end                 # then after 2 more beats (4 beats total)\n\n  \",\n\n  \"\n\n  at [1, 2, 3], [75, 76, 77] do |n|  # plays 3 different notes\n\n    play n\n\n  end\n\n  \",\n\n  \"\n\n  at [1, 2, 3],\n\n      [{:amp=>0.5}, {:amp=> 0.8}] do |p| # alternate soft and loud\n\n    sample :drum_cymbal_open, p          # cymbal hits three times\n\n  end\n\n  \",\n\n  \"\n\n  at [0, 1, 2] do |t| # when no params are given to at, the times are fed through to the block\n\n    puts t #=> prints 0, 1, then 2\n\n  end\n\n  \",\n\n  \"\n\n  at [0, 1, 2], [:a, :b] do |t, b|  #If you specify the block with 2 args, it will pass through both the time and the param\n\n    puts [t, b] #=> prints out [0, :a], [1, :b], then [2, :a]\n\n  end\n\n  \",\n\n  \"\n\n  at [0, 0.5, 2] do |t, idx|  #If you specify the block with 2 args, and no param list to at, it will pass through both the time and the index\n\n    puts [t, idx] #=> prints out [0, 0], [0.5, 1], then [2, 2]\n\n  end\n\n  \",\n\n  \"\n\n  at [0, 0.5, 2], [:a, :b] do |t, b, idx|  #If you specify the block with 3 args, it will pass through the time, the param and the index\n\n    puts [t, b, idx] #=> prints out [0, :a, 0], [0.5, :b, 1], then [2, :a, 2]\n\n  end\n\n  \",\n\n  \" # at does not consume & interfere with the outer random stream\n\nputs \\\"main: \\\", rand  # 0.75006103515625\n\nrand_back\n\nat 1 do         # the random stream inside the at block is separate and\n\n                # isolated from the outer stream.\n\n  puts \\\"at:\\\", rand # 0.9287109375\n\n  puts \\\"at:\\\", rand # 0.1043701171875\n\nend\n\nsleep 2\n\nputs \\\"main: \\\", rand # value is still 0.75006103515625\n\n\",\n\n\"\n\n            # Each block run within at has its own isolated random stream:\n\nat [1, 2] do\n\n            # first time round (after 1 beat) prints:\n\n  puts rand # 0.9287109375\n\n  puts rand # 0.1043701171875\n\nend\n\n            # second time round (after 2 beats) prints:\n\n            # 0.1043701171875\n\n            # 0.764617919921875\n\n"
  },
  "sample_groups": {
    "doc": "Return a list of all the sample groups available",
    "summary": "Get all sample groups"
  },
  "use_merged_sample_defaults": {
    "doc": "Specify new default values to be used by all subsequent calls to `sample`. Merges the specified values with any previous defaults, rather than replacing them.",
    "summary": "Merge new sample defaults",
    "examples": "sample :loop_amen # plays amen break with default arguments\n\nuse_merged_sample_defaults amp: 0.5, cutoff: 70\n\nsample :loop_amen # plays amen break with an amp of 0.5, cutoff of 70 and defaults for rest of args\n\nuse_merged_sample_defaults cutoff: 90\n\nsample :loop_amen  # plays amen break with a cutoff of 90 and and an amp of 0.5 with defaults for rest of args\n\n"
  },
  "recording_save": {
    "doc": "Save previous recording to the specified location",
    "summary": "Save recording"
  },
  "rand_reset": {
    "doc": "Resets the random stream to the last specified seed. See `use_random_seed` for changing the seed.",
    "summary": "Reset rand generator to last seed",
    "examples": "  puts rand # prints 0.75006103515625\n\n  puts rand # prints 0.733917236328125\n\n  puts rand # prints 0.464202880859375\n\n  puts rand # prints 0.24249267578125\n\n  rand_reset  # reset the random stream\n\n  puts rand # prints 0.75006103515625\n\n  "
  },
  "sample_free": {
    "doc": "Frees the memory and resources consumed by loading the sample on the server. Subsequent calls to `sample` and friends will re-load the sample on the server.\nYou may also specify the same set of source and filter pre-args available to `sample` itself. `sample_free` will then free all matching samples. See `sample`'s docs for more information.",
    "summary": "Free a sample on the synth server",
    "examples": "sample :loop_amen # The Amen break is now loaded into memory and played\n\nsleep 2\n\nsample :loop_amen # The Amen break is not loaded but played from memory\n\nsleep 2\n\nsample_free :loop_amen # The Amen break is freed from memory\n\nsample :loop_amen # the Amen break is re-loaded and played\",\n\n\"\n\nputs sample_info(:loop_amen).to_i # This returns the buffer id of the sample i.e. 1\n\nputs sample_info(:loop_amen).to_i # The buffer id remains constant whilst the sample\n\n                                  # is loaded in memory\n\nsample_free :loop_amen\n\nputs sample_info(:loop_amen).to_i # The Amen break is re-loaded and gets a *new* id.\",\n\n\"\n\nsample :loop_amen\n\nsample :ambi_lunar_land\n\nsleep 2\n\nsample_free :loop_amen, :ambi_lunar_land\n\nsample :loop_amen                        # re-loads and plays amen\n\nsample :ambi_lunar_land                  # re-loads and plays lunar land\",\n\n\"# Using source and filter pre-args\n\ndir = \\\"/path/to/sample/dir\\\"\n\nsample_free dir # frees any loaded samples in \\\"/path/to/sample/dir\\\"\n\nsample_free dir, 1 # frees sample with index 1 in \\\"/path/to/sample/dir\\\"\n\nsample_free dir, :foo # frees sample with name \\\"foo\\\" in \\\"/path/to/sample/dir\\\"\n\nsample_free dir, /[Bb]ar/ # frees sample which matches regex /[Bb]ar/ in \\\"/path/to/sample/dir\\\"\n\n"
  },
  "vt": {
    "doc": "Get the virtual time of the current thread.",
    "summary": "Get virtual time",
    "examples": "  puts vt # prints 0\n\n   sleep 1\n\n   puts vt # prints 1"
  },
  "with_merged_sample_defaults": {
    "doc": "Specify new default values to be used by all subsequent calls to `sample` within the `do`/`end` block.  Merges the specified values with any previous sample defaults, rather than replacing them. After the `do`/`end` block has completed, the previous sampled defaults (if any) are restored.",
    "summary": "Block-level use merged sample defaults",
    "examples": "sample :loop_amen # plays amen break with default arguments\n\nuse_merged_sample_defaults amp: 0.5, cutoff: 70\n\nsample :loop_amen # plays amen break with an amp of 0.5, cutoff of 70 and defaults for rest of args\n\nwith_merged_sample_defaults cutoff: 90 do\n\n  sample :loop_amen  # plays amen break with a cutoff of 90 and amp of 0.5\n\nend\n\nsample :loop_amen  # plays amen break with a cutoff of 70 and amp is 0.5 again as the previous defaults are restored."
  },
  "scale_names": {
    "doc": "Returns a ring containing all scale names known to Sonic Pi",
    "summary": "All scale names",
    "examples": "puts scale_names #=>  prints a list of all the scales"
  },
  "block_duration": {
    "doc": "Given a block, runs it and returns the amount of time that has passed. This time is in seconds and is not scaled to the current BPM. Any threads spawned in the block are not accounted for.",
    "summary": "Return block duration",
    "examples": "dur = block_duration do\n\n  play 50\n\n  sleep 1\n\n  play 62\n\n  sleep 2\n\nend\n\nputs dur #=> Returns 3 as 3 seconds have passed within the block\",\n\n\"use_bpm 120\n\ndur = block_duration do\n\n  play 50\n\n  sleep 1\n\n  play 62\n\n  sleep 2\n\nend\n\nputs dur #=> Returns 1.5 as 1.5 seconds have passed within the block\n\n         #   (due to the BPM being 120)"
  },
  "use_arg_bpm_scaling": {
    "doc": "Turn synth argument bpm scaling on or off for the current thread. This is on by default. Note, using `rt` for args will result in incorrect times when used after turning arg bpm scaling off.",
    "summary": "Enable and disable BPM scaling",
    "examples": "use_bpm 120\n\nplay 50, release: 2 # release is actually 1 due to bpm scaling\n\nsleep 2             # actually sleeps for 1 second\n\nuse_arg_bpm_scaling false\n\nplay 50, release: 2 # release is now 2\n\nsleep 2             # still sleeps for 1 second\",\n\n        \"                       # Interaction with rt\n\nuse_bpm 120\n\nplay 50, release: rt(2) # release is 2 seconds\n\nsleep rt(2)             # sleeps for 2 seconds\n\nuse_arg_bpm_scaling false\n\nplay 50, release: rt(2) # ** Warning: release is NOT 2 seconds! **\n\nsleep rt(2)             # still sleeps for 2 seconds"
  },
  "status": {
    "doc": "This returns a Hash of information about the synthesis environment. Mostly used for debugging purposes.",
    "summary": "Get server status",
    "examples": "puts status # Returns something similar to:\n\n            # {\n\n            #   :ugens=>10,\n\n            #   :synths=>1,\n\n            #   :groups=>7,\n\n            #   :sdefs=>61,\n\n            #   :avg_cpu=>0.20156468451023102,\n\n            #   :peak_cpu=>0.36655542254447937,\n\n            #   :nom_samp_rate=>44100.0,\n\n            #   :act_samp_rate=>44099.9998411752,\n\n            #   :audio_busses=>2,\n\n            #   :control_busses=>0\n\n            # }\n\n"
  },
  "chord": {
    "doc": "Creates an immutable ring of Midi note numbers when given a tonic note and a chord type. If only passed a chord type, will default the tonic to 0. See examples.",
    "summary": "Create chord",
    "examples": "puts (chord :e, :minor) # returns a ring of midi notes - (ring 64, 67, 71)\n\n\",\n\n        \"# Play all the notes together\n\nplay (chord :e, :minor)\",\n\n\"\n\n# Chord inversions (see the fn chord_invert)\n\nplay (chord :e3, :minor, invert: 0) # Play the basic :e3, :minor chord - (ring 52, 55, 59)\n\nplay (chord :e3, :minor, invert: 1) # Play the first inversion of :e3, :minor - (ring 55, 59, 64)\n\nplay (chord :e3, :minor, invert: 2) # Play the first inversion of :e3, :minor - (ring 59, 64, 67)\n\n\",\n\n\"# You can create a chord without a tonic:\n\nputs (chord :minor) #=> (ring 0, 3, 7)\",\n\n\"# chords are great for arpeggiators\n\nlive_loop :arp do\n\n  play chord(:e, :minor, num_octaves: 2).tick, release: 0.1\n\n  sleep 0.125\n\nend\",\n\n        \"# Sonic Pi supports a large range of chords\n\n # Notice that the more exotic ones have to be surrounded by ' quotes\n\n(chord :C, '1')\n\n(chord :C, '5')\n\n(chord :C, '+5')\n\n(chord :C, 'm+5')\n\n(chord :C, :sus2)\n\n(chord :C, :sus4)\n\n(chord :C, '6')\n\n(chord :C, :m6)\n\n(chord :C, '7sus2')\n\n(chord :C, '7sus4')\n\n(chord :C, '7-5')\n\n(chord :C, 'm7-5')\n\n(chord :C, '7+5')\n\n(chord :C, 'm7+5')\n\n(chord :C, '9')\n\n(chord :C, :m9)\n\n(chord :C, 'm7+9')\n\n(chord :C, :maj9)\n\n(chord :C, '9sus4')\n\n(chord :C, '6*9')\n\n(chord :C, 'm6*9')\n\n(chord :C, '7-9')\n\n(chord :C, 'm7-9')\n\n(chord :C, '7-10')\n\n(chord :C, '9+5')\n\n(chord :C, 'm9+5')\n\n(chord :C, '7+5-9')\n\n(chord :C, 'm7+5-9')\n\n(chord :C, '11')\n\n(chord :C, :m11)\n\n(chord :C, :maj11)\n\n(chord :C, '11+')\n\n(chord :C, 'm11+')\n\n(chord :C, '13')\n\n(chord :C, :m13)\n\n(chord :C, :add2)\n\n(chord :C, :add4)\n\n(chord :C, :add9)\n\n(chord :C, :add11)\n\n(chord :C, :add13)\n\n(chord :C, :madd2)\n\n(chord :C, :madd4)\n\n(chord :C, :madd9)\n\n(chord :C, :madd11)\n\n(chord :C, :madd13)\n\n(chord :C, :major)\n\n(chord :C, :M)\n\n(chord :C, :minor)\n\n(chord :C, :m)\n\n(chord :C, :major7)\n\n(chord :C, :dom7)\n\n(chord :C, '7')\n\n(chord :C, :M7)\n\n(chord :C, :minor7)\n\n(chord :C, :m7)\n\n(chord :C, :augmented)\n\n(chord :C, :a)\n\n(chord :C, :diminished)\n\n(chord :C, :dim)\n\n(chord :C, :i)\n\n(chord :C, :diminished7)\n\n(chord :C, :dim7)\n\n(chord :C, :i7)\n\n"
  },
  "density": {
    "doc": "Runs the block `d` times with the bpm for the block also multiplied by `d`. Great for repeating sections a number of times faster yet keeping within a fixed time. If `d` is less than 1, then time will be stretched accordingly and the block will take longer to complete.",
    "summary": "Squash and repeat time",
    "examples": "  use_bpm 60   # Set the BPM to 60\n\n  density 2 do       # BPM for block is now 120\n\n                     # block is called 2.times\n\n    sample :bd_haus # sample is played twice\n\n    sleep 0.5        # sleep is 0.25s\n\n  end\",\n\n  \"\n\n  density 2 do |idx| # You may also pass a param to the block similar to n.times\n\n    puts idx         # prints out 0, 1\n\n    sleep 0.5        # sleep is 0.25s\n\n  end\n\n  \",\n\n  \"\n\n  density 0.5 do          # Specifying a density val of < 1 will stretch out time\n\n                          # A density of 0.5 will double the length of the block's\n\n                          # execution time.\n\n    play 80, release: 1   # plays note 80 with 2s release\n\n    sleep 0.5             # sleep is 1s\n\n  end\n\n  "
  },
  "use_synth_defaults": {
    "doc": "Specify new default values to be used by all subsequent calls to `play`. Will remove and override any previous defaults.",
    "summary": "Use new synth defaults",
    "examples": "play 50 # plays note 50 with default arguments\n\nuse_synth_defaults amp: 0.5, cutoff: 70\n\nplay 50 # plays note 50 with an amp of 0.5, cutoff of 70 and defaults for rest of args\n\nuse_synth_defaults cutoff: 90\n\nplay 50 # plays note 50 with a cutoff of 90 and defaults for rest of args - note that amp is no longer 0.5\n\n"
  },
  "line": {
    "doc": "Create a ring buffer representing a straight line between start and finish of num_slices elements. Num slices defaults to `8`. Indexes wrap around positively and negatively. Similar to `range`.",
    "summary": "Create a ring buffer representing a straight line",
    "examples": "(line 0, 4, steps: 4)    #=> (ring 0.0, 1.0, 2.0, 3.0)\",\n\n        \"(line 5, 0, steps: 5)    #=> (ring 5.0, 4.0, 3.0, 2.0, 1.0)\",\n\n        \"(line 0, 3, inclusive: true) #=> (ring 0.0, 1.0, 2.0, 3.0)"
  },
  "sync": {
    "doc": "Pause/block the current thread until a `cue` heartbeat with a matching `cue_id` is received. When a matching `cue` message is received, unblock the current thread, and continue execution with the virtual time set to match the thread that sent the `cue` heartbeat. The current thread is therefore synced to the `cue` thread. If multiple cue ids are passed as arguments, it will `sync` on the first matching `cue_id`. By default the BPM of the cueing thread is inherited. This can be disabled using the bpm_sync: opt.",
    "summary": "Sync with other threads",
    "examples": "  in_thread do\n\n    sync :foo # this parks the current thread waiting for a foo sync message to be received.\n\n    sample :ambi_lunar_land\n\n  end\n\n  sleep 5\n\n  cue :foo # We send a sync message from the main thread.\n\n            # This then unblocks the thread above and we then hear the sample\",\n\n  \"\n\n  in_thread do   # Start a metronome thread\n\n    loop do      # Loop forever:\n\n      cue :tick # sending tick heartbeat messages\n\n      sleep 0.5  # and sleeping for 0.5 beats between ticks\n\n    end\n\n  end\n\n  # We can now play sounds using the metronome.\n\n  loop do                    # In the main thread, just loop\n\n    sync :tick               # waiting for :tick sync messages\n\n    sample :drum_heavy_kick  # after which play the drum kick sample\n\n  end\",\n\n  \"\n\n  sync :foo, :bar # Wait for either a :foo or :bar cue \",\n\n  \"\n\n  in_thread do   # Start a metronome thread\n\n    loop do      # Loop forever:\n\n      cue [:foo, :bar, :baz].choose # sending one of three tick heartbeat messages randomly\n\n      sleep 0.5  # and sleeping for 0.5 beats between ticks\n\n    end\n\n  end\n\n  # We can now play sounds using the metronome:\n\n  in_thread do\n\n    loop do                    # In the main thread, just loop\n\n      sync :foo               # waiting for :foo sync messages\n\n      sample :elec_beep  # after which play the elec beep sample\n\n    end\n\n  end\n\n  in_thread do\n\n    loop do                    # In the main thread, just loop\n\n      sync :bar               # waiting for :bar sync messages\n\n      sample :elec_flip  # after which play the elec flip sample\n\n    end\n\n  end\n\n  in_thread do\n\n    loop do                    # In the main thread, just loop\n\n      sync :baz               # waiting for :baz sync messages\n\n      sample :elec_blup  # after which play the elec blup sample\n\n    end\n\n  end"
  },
  "with_cent_tuning": {
    "doc": "Similar to `use_cent_tuning` except only applies cent shift to code within supplied `do`/`end` block. Previous cent tuning value is restored after block. One semitone consists of 100 cents. To transpose entire semitones see `with_transpose`.",
    "summary": "Block-level cent tuning",
    "examples": "use_cent_tuning 1\n\nplay 50 # Plays note 50.01\n\nwith_cent_tuning 2 do\n\n  play 50 # Plays note 50.02\n\nend\n\n# Original cent tuning value is restored\n\nplay 50 # Plays note 50.01\n\n"
  },
  "use_debug": {
    "doc": "Enable or disable messages created on synth triggers. If this is set to false, the synths will be silent until debug is turned back on. Silencing debug messages can reduce output noise and also increase performance on slower platforms. See `with_debug` for setting the debug value only for a specific `do`/`end` block.",
    "summary": "Enable and disable debug",
    "examples": "use_debug true # Turn on debug messages\nuse_debug false # Disable debug messages"
  },
  "kill": {
    "doc": "Kill a running synth sound or sample. In order to kill a sound, you need to have stored a reference to it in a variable.",
    "summary": "Kill synth",
    "examples": "# store a reference to a running synth in a variable called foo:\n\nfoo = play 50, release: 4\n\nsleep 1\n\n# foo is still playing, but we can kill it early:\n\nkill foo\n\n\",\n\n        \"bar = sample :loop_amen\n\nsleep 0.5\n\nkill bar"
  },
  "knit": {
    "doc": "Knits a series of value, count pairs to create a ring buffer where each value is repeated count times.",
    "summary": "Knit a sequence of repeated values",
    "examples": "(knit 1, 5)    #=> (ring 1, 1, 1, 1, 1)\",\n\n        \"(knit :e2, 2, :c2, 3) #=> (ring :e2, :e2, :c2, :c2, :c2)"
  },
  "rand_look": {
    "doc": "Given a max number, produces a number between `0` and the supplied max value exclusively. If max is a range produces an int within the range. With no args returns a value between `0` and `1`.\nDoes not consume a random value from the stream. Therefore, multiple sequential calls to `rand_look` will all return the same value.",
    "summary": "Generate a random number without consuming a rand",
    "examples": "  print rand_look(0.5) #=> will print a number like 0.375030517578125 to the output pane\",\n\n        \"\n\n  print rand_look(0.5) #=> will print a number like 0.375030517578125 to the output pane\n\n  print rand_look(0.5) #=> will print the same number again\n\n  print rand_look(0.5) #=> will print the same number again\n\n  print rand_(0.5) #=> will print a different random number\n\n  print rand_look(0.5) #=> will print the same number as the prevoius line again."
  },
  "midi_notes": {
    "doc": "Create a new immutable ring buffer of notes from args. Indexes wrap around positively and negatively. Final ring consists only of MIDI numbers and nil.",
    "summary": "Create a ring buffer of midi note numbers",
    "examples": "(midi_notes :d3, :d4, :d5) #=> (ring 50, 62, 74)\",\n\n        \"(midi_notes :d3, 62,  nil) #=> (ring 50, 62, nil)"
  },
  "with_synth_defaults": {
    "doc": "Specify new default values to be used by all calls to `play` within the `do`/`end` block. After the `do`/`end` block has completed the previous synth defaults (if any) are restored.",
    "summary": "Block-level use new synth defaults",
    "examples": "play 50 # plays note 50 with default arguments\n\nuse_synth_defaults amp: 0.5, pan: -1\n\nplay 50 # plays note 50 with an amp of 0.5, pan of -1 and defaults for rest of args\n\nwith_synth_defaults amp: 0.6, cutoff: 80 do\n\n  play 50 # plays note 50 with an amp of 0.6, cutoff of 80 and defaults for rest of args (including pan)\n\nend\n\nplay 60 # plays note 60 with an amp of 0.5, pan of -1 and defaults for rest of args\n\n"
  },
  "play_pattern_timed": {
    "doc": "Play each note in a list of notes one after another with specified times between them. The notes should be a list of MIDI numbers, symbols such as :E4 or chords such as chord(:A3, :major) - identical to the first parameter of the play function. The times should be a list of times between the notes in beats.\nIf the list of times is smaller than the number of gaps between notes, the list is repeated again. If the list of times is longer than the number of gaps between notes, then some of the times are ignored. See examples for more detail.\nAccepts optional args for modification of the synth being played. See each synth's documentation for synth-specific opts. See `use_synth` and `with_synth` for changing the current synth.",
    "summary": "Play pattern of notes with specific times",
    "examples": "play_pattern_timed [40, 42, 44, 46], [1, 2, 3]\n\n# same as:\n\nplay 40\n\nsleep 1\n\nplay 42\n\nsleep 2\n\nplay 44\n\nsleep 3\n\nplay 46\",\n\n        \"play_pattern_timed [40, 42, 44, 46, 49], [1, 0.5]\n\n# same as:\n\nplay 40\n\nsleep 1\n\nplay 42\n\nsleep 0.5\n\nplay 44\n\nsleep 1\n\nplay 46\n\nsleep 0.5\n\nplay 49\",\n\n        \"play_pattern_timed [40, 42, 44, 46], [0.5]\n\n# same as:\n\nplay 40\n\nsleep 0.5\n\nplay 42\n\nsleep 0.5\n\nplay 44\n\nsleep 0.5\n\nplay 46\",\n\n        \"play_pattern_timed [40, 42, 44], [1, 2, 3, 4, 5]\n\n#same as:\n\nplay 40\n\nsleep 1\n\nplay 42\n\nsleep 2\n\nplay 44"
  },
  "octs": {
    "doc": "Create a ring of successive octaves starting at `start` for `num_octaves`.",
    "summary": "Create a ring of octaves",
    "examples": "(octs 60, 2)  #=> (ring 60, 72)\",\n\n        \"(octs :e3, 3) #=> (ring 52, 64, 76)"
  },
  "with_merged_synth_defaults": {
    "doc": "Specify synth arg values to be used by any following call to play within the specified `do`/`end` block. Merges the specified values with any previous synth defaults, rather than replacing them. After the `do`/`end` block has completed, previous defaults (if any) are restored.",
    "summary": "Block-level merge synth defaults",
    "examples": "with_merged_synth_defaults amp: 0.5, pan: 1 do\n\n  play 50 # => plays note 50 with amp 0.5 and pan 1\n\nend\",\n\n        \"play 50 #=> plays note 50\n\nwith_merged_synth_defaults amp: 0.5 do\n\n  play 50 #=> plays note 50 with amp 0.5\n\n  with_merged_synth_defaults pan: -1 do\n\n    with_merged_synth_defaults amp: 0.7 do\n\n      play 50 #=> plays note 50 with amp 0.7 and pan -1\n\n    end\n\n  end\n\n  play 50 #=> plays note 50 with amp 0.5\n\nend"
  },
  "use_octave": {
    "doc": "Transposes your music by shifting all notes played by the specified number of octaves. To shift up by an octave use a transpose of 1. To shift down use negative numbers. See `with_octave` for setting the octave shift only for a specific `do`/`end` block. For transposing the notes within the octave range see `use_transpose`.",
    "summary": "Note octave transposition",
    "examples": "play 50 # Plays note 50\n\nuse_octave 1\n\nplay 50 # Plays note 62\",\n\n        \"\n\n# You may change the transposition multiple times:\n\nplay 62 # Plays note 62\n\nuse_octave -1\n\nplay 62 # Plays note 50\n\nuse_octave 2\n\nplay 62 # Plays note 86"
  }
}

opts_doc = {
  "pitch": "Pitch adjustment in semitones. 1 is up a semitone, 12 is up an octave, -12 is down an octave etc. Maximum upper limit of 24 (up 2 octaves). Lower limit of -72 (down 6 octaves). Decimal numbers can be used for fine tuning.",
  "decay": "Duration of the decay phase of the envelope.",
  "rpitch": "Rate modified pitch. Multiplies the rate by the appropriate ratio to shift up or down the specified amount in MIDI notes. Please note - this does *not* keep the duration and rhythmical rate constant and is essentially the same as modifying the rate directly.",
  "another_key": "Another value",
  "octave": "The octave of the note. Overrides any octave declaration in the note symbol such as :c2. Default is 4",
  "on": "If specified and false/nil/0 will stop the synth from being played. Ensures all opts are evaluated.",
  "release": "Time (from the end of the sample) to go from full amplitude to 0. Default is 0.",
  "sustain": "Time to stay at full volume. Default is to stretch to length of sample (minus attack and release times).",
  "hpf": "Cutoff value of the built-in high pass filter (hpf) in MIDI notes. Unless specified, the hpf is *not* added to the signal chain.",
  "decay_level": "Amplitude level reached after decay phase and immediately before sustain phase. Defaults to sustain_level unless explicitly set",
  "lpf_env_curve": "Select the shape of the curve between levels in the lpf cutoff envelope. 1=linear, 2=exponential, 3=sine, 4=welch, 6=squared, 7=cubed.",
  "finish": "Position in sample as a fraction between 0 and 1 to end playback. Default is 1.",
  "delay": "Initial delay in beats before the thread starts. Default is 0.",
  "bpm_sync": "Inherit the BPM of the cueing thread. Default is false",
  "relax_time": "Time taken for the amplitude adjustments to be released. Usually a little longer than clamp_time. If both times are too short, you can get some (possibly unwanted) artefacts. Also known as the time of the release phase. Only valid if the compressor is enabled by turning on the `compress:` opt.",
  "start": "Position in sample as a fraction between 0 and 1 to start playback. Default is 0.",
  "inclusive": "boolean value representing whether or not to include finish value in line",
  "threshold": "Threshold value determining the break point between slope_below and slope_above. Only valid if the compressor is enabled by turning on the `compress:` opt.",
  "hpf_sustain": "Amount of time for hpf cutoff value to remain at sustain level in beats. When -1 (the default) will auto-stretch.",
  "amp_slide": "The duration in beats for amplitude changes to take place",
  "env_curve": "Select the shape of the curve between levels in the envelope. 1=linear, 2=exponential, 3=sine, 4=welch, 6=squared, 7=cubed",
  "norm": "Normalise the audio (make quieter parts of the sample louder and louder parts quieter) - this is similar to the normaliser FX. This may emphasise any clicks caused by clipping.",
  "lpf_min": "Starting value of the lpf cutoff envelope. Default is 30.",
  "reps": "Number of times to repeat the block in an iteration.",
  "clamp_time": "Time taken for the amplitude adjustments to kick in fully (in seconds). This is usually pretty small (not much more than 10 milliseconds). Also known as the time of the attack phase. Only valid if the compressor is enabled by turning on the `compress:` opt.",
  "hpf_bypass": "Bypass the global hpf. 0=no bypass, 1=bypass. Default 0.",
  "hpf_decay_level": "The level of hpf cutoff after the decay phase as a MIDI note. Default value is to match the `hpf_sustain_level:` opt.",
  "hpf_sustain_level": "The sustain cutoff (value of hpf cutoff at sustain time) as a MIDI note. Default value is to match the `hpf_release_level:` opt.",
  "amp": "Amplitude of playback.",
  "num_beats": "The number of beats within the sample. By default this is 1.",
  "sync": "Initial sync symbol. Will sync with this symbol before the thread starts.",
  "limiter_bypass": "Bypass the final limiter. 0=no bypass, 1=bypass. Default 0.",
  "attack_level": "Amplitude level reached after attack phase and immediately before decay phase",
  "hpf_env_curve": "Select the shape of the curve between levels in the hpf cutoff envelope. 1=linear, 2=exponential, 3=sine, 4=welch, 6=squared, 7=cubed.",
  "slide": "Default slide time in beats for all slide opts. Individually specified slide opts will override this value.",
  "hpf_attack_level": "The peak hpf cutoff (value of cutoff at peak of attack) as a MIDI note. Default value is to match the `hpf_decay_level:` opt.",
  "slope_below": "Slope of the amplitude curve below the threshold. A value of 1 means that the output of signals with amplitude below the threshold will be unaffected. Greater values will magnify and smaller values will attenuate the signal. Only valid if the compressor is enabled by turning on the `compress:` opt.",
  "pitches": "An array of notes (symbols or ints) to filter on. Octave information is ignored.",
  "seed": "override initial random generator seed before starting loop.",
  "lpf_sustain": "Amount of time for lpf cutoff value to remain at sustain level in beats. When -1 (the default) will auto-stretch.",
  "pan": "Stereo position of audio. -1 is left ear only, 1 is right ear only, and values in between position the sound accordingly. Default is 0.",
  "pre_amp": "Amplitude multiplier which takes place immediately before any internal FX such as the low pass filter, compressor or pitch modification. Use this opt if you want to overload the compressor.",
  "num_octaves": "Create an arpeggio of the chord over n octaves",
  "hpf_release": "Amount of time (in beats) for sound to move from hpf cutoff sustain value to hpf cutoff min value. Default value is set to match amp envelope's release value.",
  "name": "Make this thread a named thread with name. If a thread with this name already exists, a new thread will not be created.",
  "invert": "Apply the specified num inversions to chord. See the fn `chord_invert`.",
  "sustain_level": "Amplitude level reached after decay phase and immediately before release phase.",
  "lpf": "Cutoff value of the built-in low pass filter (lpf) in MIDI notes. Unless specified, the lpf is *not* added to the signal chain.",
  "time_dis": "Pitch shift-specific opt - only honoured if the `pitch:` opt is used. Time dispersion - how much random delay before playing each grain (measured in seconds). Again, low values here like 0.001 can help to soften up metallic sounds introduced by the effect. Large values are also fun as they can make soundscapes and textures from the input, although you will most likely lose the rhythm of the original. NB - This won't have an effect if it's larger than window_size.",
  "key": "All these opts are passed through to the thread which syncs",
  "path": "Path of the sample to play. Typically this opt is rarely used instead of the more powerful source/filter system. However it can be useful when working with pre-made opt maps.",
  "pitch_dis": "Pitch shift-specific opt - only honoured if the `pitch:` opt is used. Pitch dispersion - how much random variation in pitch to add. Using a low value like 0.001 can help to \\\"soften up\\\" the metallic sounds, especially on drum loops. To be really technical, pitch_dispersion is the maximum random deviation of the pitch from the pitch ratio (which is set by the `pitch:` opt).",
  "lpf_attack_level": "The peak lpf cutoff (value of cutoff at peak of attack) as a MIDI note. Default value is to match the `lpf_decay_level:` opt.",
  "steps": "number of slices or segments along the line",
  "init": "initial value for optional block arg",
  "lpf_bypass": "Bypass the global lpf. 0=no bypass, 1=bypass. Default 0.",
  "compress": "Enable the compressor. This sits at the end of the internal FX chain immediately before the `amp:` opt. Therefore to drive the compressor use the `pre_amp:` opt which will amplify the signal before it hits any internal FX. The compressor compresses the dynamic range of the incoming signal. Equivalent to automatically turning the amp down when the signal gets too loud and then back up again when it's quiet. Useful for ensuring the containing signal doesn't overwhelm other aspects of the sound. Also a general purpose hard-knee dynamic range processor which can be tuned via the opts to both expand and compress the signal.",
  "lpf_release_level": "The final value of the low pass filter envelope as a MIDI note. This envelope is bypassed if no lpf env opts are specified. Default value is to match the `lpf:` opt.",
  "lpf_release": "Amount of time (in beats) for sound to move from lpf cutoff sustain value to lpf cutoff min value. Default value is set to match amp envelope's release value.",
  "pitch_stretch": "Stretch (or shrink) the sample to last for exactly the specified number of beats. This attempts to keep the pitch constant using the `pitch:` opt. Note, it's very likely you'll need to experiment with the `window_size:`, `pitch_dis:` and `time_dis:` opts depending on the sample and the amount you'd like to stretch/shrink from original size.",
  "skip": "Number of rands to skip over with each successive pick",
  "lpf_decay": "Decay time for lpf cutoff filter. Amount of time (in beats) for sound to move from full cutoff value (cutoff attack level) to the cutoff sustain level. Default value is set to match amp envelope's decay value.",
  "hpf_attack": "Attack time for hpf cutoff filter. Amount of time (in beats) for sound to reach full cutoff value. Default value is set to match amp envelope's attack value.",
  "offset": "Offset to add to index returned. Useful when calling look on lists, rings and vectors to offset the returned value",
  "step": "Step size of value to quantise to.",
  "lpf_init_level": "The initial low pass filter envelope value as a MIDI note. This envelope is bypassed if no lpf env opts are specified. Default value is to match the `lpf_min:` opt.",
  "auto_cue": "enable or disable automatic cue (default is true)",
  "beat_stretch": "Stretch (or shrink) the sample to last for exactly the specified number of beats. Please note - this does *not* keep the pitch constant and is essentially the same as modifying the rate directly.",
  "lpf_attack": "Attack time for lpf cutoff filter. Amount of time (in beats) for sound to reach full cutoff value. Default value is set to match amp envelope's attack value.",
  "hpf_max": "Maximum value of the high pass filter envelope. Default is 200.",
  "rotate": "rotate to the next strong beat allowing for easy permutations of the original rhythmic grouping (see example)",
  "onset": "Analyse the sample with an onset detection algorithm and set the `start:` and `finish:` opts to play the nth onset only. Allows you to treat a rhythm sample as a palette of individual drum/synth hits",
  "your_key": "Your value",
  "lpf_sustain_level": "The sustain cutoff (value of lpf cutoff at sustain time) as a MIDI note. Default value is to match the `lpf_release_level:` opt.",
  "pan_slide": "The duration in beats for the pan value to change",
  "hpf_init_level": "The initial high pass filter envelope value as a MIDI note. This envelope is bypassed if no hpf env opts are specified. Default value is set to 130.",
  "leak_dc_bypass": "Bypass the final DC leak correction FX. 0=no bypass, 1=bypass. Default 0.",
  "attack": "Time to reach full volume. Default is 0.",
  "lpf_decay_level": "The level of lpf cutoff after the decay phase as a MIDI note. Default value is to match the `lpf_sustain_level:` opt.",
  "window_size": "Pitch shift-specific opt - only honoured if the `pitch:` opt is used. Pitch shift works by chopping the input into tiny slices, then playing these slices at a higher or lower rate. If we make the slices small enough and overlap them, it sounds like the original sound with the pitch changed. The window_size is the length of the slices and is measured in seconds. It needs to be around 0.2 (200ms) or greater for pitched sounds like guitar or bass, and needs to be around 0.02 (20ms) or lower for percussive sounds like drum loops. You can experiment with this to get the best sound for your input.",
  "kill_delay": "Amount of time to wait after all synths triggered by the block have completed before stopping and freeing the effect synthesiser.",
  "hpf_decay": "Decay time for hpf cutoff filter. Amount of time (in beats) for sound to move from full cutoff value (cutoff attack level) to the cutoff sustain level. Default value is set to match amp envelope's decay value.",
  "sync_bpm": "Initial sync symbol. Will sync with this symbol before the live_loop starts. Live loop will also inherit the BPM of the thread which cued the symbol.",
  "hpf_release_level": "The sustain hpf cutoff (value of hpf cutoff at sustain time) as a MIDI note. Default value is to match the `hpf:` opt.",
  "slope_above": "Slope of the amplitude curve above the threshold. A value of 1 means that the output of signals with amplitude above the threshold will be unaffected. Greater values will magnify and smaller values will attenuate the signal. Only valid if the compressor is enabled by turning on the `compress:` opt.",
  "override": "If set to true, re-definitions are allowed and this acts like define",
  "rate": "Rate with which to play back the sample. Higher rates mean an increase in pitch and a decrease in duration. Default is 1."
}

synth_doc = {}

synth_opts_doc = {}

