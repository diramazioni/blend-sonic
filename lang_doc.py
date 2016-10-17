null = None; true = True; false = False;
#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/

funct_doc = {
  "chord": {
    "doc": "Creates an immutable ring of Midi note numbers when given a tonic note and a chord type. If only passed a chord type, will default the tonic to 0. See examples.",
    "examples": "puts (chord :e, :minor) # returns a ring of midi notes - (ring 64, 67, 71)\n\"\n\"# Play all the notes together\nplay (chord :e, :minor)\"\n\"\n# Chord inversions (see the fn chord_invert)\nplay (chord :e3, :minor, invert: 0) # Play the basic :e3, :minor chord - (ring 52, 55, 59)\nplay (chord :e3, :minor, invert: 1) # Play the first inversion of :e3, :minor - (ring 55, 59, 64)\nplay (chord :e3, :minor, invert: 2) # Play the first inversion of :e3, :minor - (ring 59, 64, 67)\n\"\n\"# You can create a chord without a tonic:\nputs (chord :minor) #=> (ring 0, 3, 7)\"\n\"# chords are great for arpeggiators\nlive_loop :arp do\nplay chord(:e, :minor, num_octaves: 2).tick, release: 0.1\nsleep 0.125\nend\"\n\"# Sonic Pi supports a large range of chords\n# Notice that the more exotic ones have to be surrounded by ' quotes\n(chord :C, '1')\n(chord :C, '5')\n(chord :C, '+5')\n(chord :C, 'm+5')\n(chord :C, :sus2)\n(chord :C, :sus4)\n(chord :C, '6')\n(chord :C, :m6)\n(chord :C, '7sus2')\n(chord :C, '7sus4')\n(chord :C, '7-5')\n(chord :C, 'm7-5')\n(chord :C, '7+5')\n(chord :C, 'm7+5')\n(chord :C, '9')\n(chord :C, :m9)\n(chord :C, 'm7+9')\n(chord :C, :maj9)\n(chord :C, '9sus4')\n(chord :C, '6*9')\n(chord :C, 'm6*9')\n(chord :C, '7-9')\n(chord :C, 'm7-9')\n(chord :C, '7-10')\n(chord :C, '9+5')\n(chord :C, 'm9+5')\n(chord :C, '7+5-9')\n(chord :C, 'm7+5-9')\n(chord :C, '11')\n(chord :C, :m11)\n(chord :C, :maj11)\n(chord :C, '11+')\n(chord :C, 'm11+')\n(chord :C, '13')\n(chord :C, :m13)\n(chord :C, :add2)\n(chord :C, :add4)\n(chord :C, :add9)\n(chord :C, :add11)\n(chord :C, :add13)\n(chord :C, :madd2)\n(chord :C, :madd4)\n(chord :C, :madd9)\n(chord :C, :madd11)\n(chord :C, :madd13)\n(chord :C, :major)\n(chord :C, :M)\n(chord :C, :minor)\n(chord :C, :m)\n(chord :C, :major7)\n(chord :C, :dom7)\n(chord :C, '7')\n(chord :C, :M7)\n(chord :C, :minor7)\n(chord :C, :m7)\n(chord :C, :augmented)\n(chord :C, :a)\n(chord :C, :diminished)\n(chord :C, :dim)\n(chord :C, :i)\n(chord :C, :diminished7)\n(chord :C, :dim7)\n(chord :C, :i7)\n",
    "summary": "Create chord"
  },
  "chord_degree": {
    "doc": "In music we build chords from scales. For example, a C major chord is made by taking the 1st, 3rd and 5th notes of the C major scale (C, E and G). If you do this on a piano you might notice that you play one, skip one, play one, skip one etc. If we use the same spacing and start from the second note in C major (which is a D), we get a D minor chord which is the 2nd, 4th and 6th notes in C major (D, F and A). We can move this pattern all the way up or down the scale to get different types of chords. `chord_degree` is a helper method that returns a ring of midi note numbers when given a degree (starting point in a scale) which is a symbol `:i`, `:ii`, `:iii`, `:iv`, `:v`, `:vi`, `:vii` or a number `1`-`7`. The second argument is the tonic note of the scale, the third argument is the scale type and finally the fourth argument is number of notes to stack up in the chord. If we choose 4 notes from degree `:i` of the C major scale, we take the 1st, 3rd, 5th and 7th notes of the scale to get a C major 7 chord.",
    "examples": "puts (chord_degree :i, :A3, :major) # returns a ring of midi notes - (ring 57, 61, 64, 68) - an A major 7 chord\",\n\"play (chord_degree :i, :A3, :major, 3)\"\n\"play (chord_degree :ii, :A3, :major, 3) # Chord ii in A major is a B minor chord\"\n\"play (chord_degree :iii, :A3, :major, 3) # Chord iii in A major is a C# minor chord\"\n\"play (chord_degree :iv, :A3, :major, 3) # Chord iv in A major is a D major chord\"\n\"play (chord_degree :i, :C4, :major, 4) # Taking four notes is the default. This gives us 7th chords - here it plays a C major 7\"\n\"play (chord_degree :i, :C4, :major, 5) # Taking five notes gives us 9th chords - here it plays a C major 9 chord",
    "summary": "Construct chords of stacked thirds, based on scale degrees"
  },
  "chord_invert": {
    "doc": "Given a set of notes, apply a number of inversions indicated by the `shift` parameter. Inversions being an increase to notes if `shift` is positive or decreasing the notes if `shift` is negative.\nAn inversion is simply rotating the chord and shifting the wrapped notes up or down an octave. For example, consider the chord :e3, :minor - `(ring 52, 55, 59)`. When we invert it once, we rotate the notes around to `(ring 55, 59, 52)`. However, because note 52 is wrapped round, it's shifted up an octave (12 semitones) so the actual first inversion of the chord :e3, :minor is `(ring 55, 59, 52 + 12)` or `(ring 55, 59, 64)`.\nNote that it's also possible to directly invert chords on creation with the `invert:` opt - `(chord :e3, :minor, invert: 2)`",
    "examples": "play (chord_invert (chord :A3, \\\"M\\\"), 0) #No inversion     - (ring 57, 61, 64)\nsleep 1\nplay (chord_invert (chord :A3, \\\"M\\\"), 1) #First inversion  - (ring 61, 64, 69)\nsleep 1\nplay (chord_invert (chord :A3, \\\"M\\\"), 2) #Second inversion - (ring 64, 69, 73)\n",
    "summary": "Chord inversion"
  },
  "chord_names": {
    "doc": "Returns a ring containing all chord names known to Sonic Pi",
    "examples": "puts chord_names #=>  prints a list of all the chords",
    "summary": "All chord names"
  },
  "control": {
    "doc": "Control a running synth node by passing new parameters to it. A synth node represents a running synth and can be obtained by assigning the return value of a call to play or sample or by specifying a parameter to the do/end block of an FX. You may modify any of the parameters you can set when triggering the synth, sample or FX. See documentation for opt details. If the synth to control is a chord, then control will change all the notes of that chord group at once to a new target set of notes - see example. Also, you may use the on: opt to conditionally trigger the control - see the docs for the `synth` and `sample` fns for more information.\nIf no synth to control is specified, then the last synth triggered by the current (or parent) thread will be controlled - see example below.",
    "examples": "## Basic control\nmy_node = play 50, release: 5, cutoff: 60 # play note 50 with release of 5 and cutoff of 60. Assign return value to variable my_node\nsleep 1 # Sleep for a second\ncontrol my_node, cutoff: 70 # Now modify cutoff from 60 to 70, sound is still playing\nsleep 1 # Sleep for another second\ncontrol my_node, cutoff: 90 # Now modify cutoff from 70 to 90, sound is still playing\"\n\"\n## Combining control with slide opts allows you to create nice transitions.\ns = synth :prophet, note: :e1, cutoff: 70, cutoff_slide: 8, release: 8 # start synth and specify slide time for cutoff opt\ncontrol s, cutoff: 130 # Change the cutoff value with a control.\n# Cutoff will now slide over 8 beats from 70 to 130\"\n\"\n## Use a short slide time and many controls to create a sliding melody\nnotes = (scale :e3, :minor_pentatonic, num_octaves: 2).shuffle # get a random ordering of a scale\ns = synth :beep, note: :e3, sustain: 8, note_slide: 0.05 # Start our synth running with a long sustain and short note slide time\n64.times do\ncontrol s, note: notes.tick                            # Keep quickly changing the note by ticking through notes repeatedly\nsleep 0.125\nend\n\"\n\"\n## Controlling FX\nwith_fx :bitcrusher, sample_rate: 1000, sample_rate_slide: 8 do |bc| # Start FX but also use the handy || goalposts\n# to grab a handle on the running FX. We can call\n# our handle anything we want. Here we've called it bc\nsample :loop_garzul, rate: 1\ncontrol bc, sample_rate: 5000                                      # We can use our handle bc now just like we used s in the\n# previous example to modify the FX as it runs.\nend\"\n\"\n## Controlling chords\ncg = play (chord :e4, :minor), sustain: 2  # start a chord\nsleep 1\ncontrol cg, notes: (chord :c3, :major)     # transition to new chord.\n# Each note in the original chord is mapped onto\n# the equivalent in the new chord.\n\"\n\"\n## Sliding between chords\ncg = play (chord :e4, :minor), sustain: 4, note_slide: 3  # start a chord\nsleep 1\ncontrol cg, notes: (chord :c3, :major)                    # slide to new chord.\n# Each note in the original chord is mapped onto\n# the equivalent in the new chord.\n\"\n\"\n## Sliding from a larger to smaller chord\ncg = play (chord :e3, :m13), sustain: 4, note_slide: 3  # start a chord with 7 notes\nsleep 1\ncontrol cg, notes: (chord :c3, :major)                    # slide to new chord with fewer notes (3)\n# Each note in the original chord is mapped onto\n# the equivalent in the new chord using ring-like indexing.\n# This means that the 4th note in the original chord will\n# be mapped onto the 1st note in the second chord and so-on.\n\"\n\"\n## Sliding from a smaller to larger chord\ncg = play (chord :c3, :major), sustain: 4, note_slide: 3  # start a chord with 3 notes\nsleep 1\ncontrol cg, notes: (chord :e3, :m13)                     # slide to new chord with more notes (7)\n# Each note in the original chord is mapped onto\n# the equivalent in the new chord.\n# This means that the 4th note in the new chord\n# will not sound as there is no 4th note in the\n# original chord.\n\"\n\"\n## Changing the slide rate\ns = synth :prophet, note: :e1, release: 8, cutoff: 70, cutoff_slide: 8 # Start a synth playing with a long cutoff slide\nsleep 1                                                                # wait a beat\ncontrol s, cutoff: 130                                                 # change the cutoff so it starts sliding slowly\nsleep 3                                                                # wait for 3 beats\ncontrol s, cutoff_slide: 1                                             # Change the cutoff_slide - the cutoff now slides more quickly to 130\n# it will now take 1 beat to slide from its *current* value\n# (somewhere between 70 and 130) to 130\n\"\n\"\n## Controlling the last triggered synth\nsynth :prophet, note: :e1, release: 8                                  # Every time a synth is triggered, Sonic Pi automatically remembers the node\nsleep 1\n16.times do\ncontrol note: (octs :e1, 3).tick                                     # This means we don't need to use an explicit variable to control the synth\nsleep 0.125                                                          # we last triggered.\nend\"\n\"\n## Controlling multiple synths without variables\nsynth :beep, release: 4                  # Trigger a beep synth\nsleep 0.1\ncontrol note: :e5                        # Control last triggered synth (:beep)\nsleep 0.5\nsynth :dsaw, release: 4                  # Next, trigger a dsaw synth\nsleep 0.1\ncontrol note: :e4                        # Control last triggered synth (:dsaw)\n",
    "summary": "Control running synth"
  },
  "current_arg_checks": {
    "doc": "Returns the current arg checking setting (`true` or `false`).\nThis can be set via the fns `use_arg_checks` and `with_arg_checks`.",
    "examples": "puts current_arg_checks # Print out the current arg check setting",
    "summary": "Get current arg checking status"
  },
  "current_cent_tuning": {
    "doc": "Returns the cent shift value.\nThis can be set via the fns `use_cent_tuning` and `with_cent_tuning`.",
    "examples": "puts current_cent_tuning # Print out the current cent shift",
    "summary": "Get current cent shift"
  },
  "current_debug": {
    "doc": "Returns the current debug setting (`true` or `false`).\nThis can be set via the fns `use_debug` and `with_debug`.",
    "examples": "puts current_debug # Print out the current debug setting",
    "summary": "Get current debug status"
  },
  "current_octave": {
    "doc": "Returns the octave shift value.\nThis can be set via the fns `use_octave` and `with_octave`.",
    "examples": "puts current_octave # Print out the current octave shift",
    "summary": "Get current octave shift"
  },
  "current_sample_defaults": {
    "doc": "Returns the current sample defaults. This is a map of synth arg names to either values or functions.\nThis can be set via the fns `use_sample_defaults`, `with_sample_defaults`, `use_merged_sample_defaults` and `with_merged_sample_defaults`.",
    "examples": "use_sample_defaults amp: 0.5, cutoff: 80\nsample :loop_amen # Plays amen break with amp 0.5 and cutoff 80\nputs current_sample_defaults #=> Prints {amp: 0.5, cutoff: 80}",
    "summary": "Get current sample defaults"
  },
  "current_sched_ahead_time": {
    "doc": "Returns the current schedule ahead time.\nThis can be set via the fn `set_sched_ahead_time!`.",
    "examples": "set_sched_ahead_time! 0.5\nputs current_sched_ahead_time # Prints 0.5",
    "summary": "Get current sched ahead time"
  },
  "current_synth": {
    "doc": "Returns the current synth name.\nThis can be set via the fns `use_synth` and `with_synth`.",
    "examples": "puts current_synth # Print out the current synth name",
    "summary": "Get current synth"
  },
  "current_synth_defaults": {
    "doc": "Returns the current synth defaults. This is a map of synth arg names to either values or functions.\nThis can be set via the fns `use_synth_defaults`, `with_synth_defaults`, `use_merged_synth_defaults` and `with_merged_synth_defaults`.",
    "examples": "use_synth_defaults amp: 0.5, cutoff: 80\nplay 50 # Plays note 50 with amp 0.5 and cutoff 80\nputs current_synth_defaults #=> Prints {amp: 0.5, cutoff: 80}",
    "summary": "Get current synth defaults"
  },
  "current_transpose": {
    "doc": "Returns the current transpose value.\nThis can be set via the fns `use_transpose` and `with_transpose`.",
    "examples": "puts current_transpose # Print out the current transpose value",
    "summary": "Get current transposition"
  },
  "current_volume": {
    "doc": "Returns the current volume.\nThis can be set via the fn `set_volume!`.",
    "examples": "puts current_volume # Print out the current volume\"\n\"set_volume! 2\nputs current_volume #=> 2",
    "summary": "Get current volume"
  },
  "hz_to_midi": {
    "doc": "Convert a frequency in hz to a midi note. Note that the result isn't an integer and there is a potential for some very minor rounding errors.",
    "examples": "hz_to_midi(261.63) #=> 60.0003",
    "summary": "Hz to MIDI conversion"
  },
  "kill": {
    "doc": "Kill a running synth sound or sample. In order to kill a sound, you need to have stored a reference to it in a variable.",
    "examples": "# store a reference to a running synth in a variable called foo:\nfoo = play 50, release: 4\nsleep 1\n# foo is still playing, but we can kill it early:\nkill foo\n\"\n\"bar = sample :loop_amen\nsleep 0.5\nkill bar",
    "summary": "Kill synth"
  },
  "load_sample": {
    "doc": "Given a path to a `.wav`, `.wave`, `.aif`, `.aiff` or `.flac` file, pre-loads the sample into memory.\n+You may also specify the same set of source and filter pre-args available to `sample` itself. `load_sample` will then load all matching samples. See `sample`'s docs for more information.\" ",
    "examples": "load_sample :elec_blip # :elec_blip is now loaded and ready to play as a sample\nsample :elec_blip # No delay takes place when attempting to trigger it\"\n\"# Using source and filter pre-args\ndir = \\\"/path/to/sample/dir\\\"\nload_sample dir # loads all samples in \\\"/path/to/sample/dir\\\"\nload_sample dir, 1 # loads sample with index 1 in \\\"/path/to/sample/dir\\\"\nload_sample dir, :foo # loads sample with name \\\"foo\\\" in \\\"/path/to/sample/dir\\\"\nload_sample dir, \\\"quux\\\" # loads all samples with file names containing \\\"quux\\\" in \\\"/path/to/sample/dir\\\"\nload_sample dir, /[Bb]ar/ # loads all samples which match regex /[Bb]ar/ in \\\"/path/to/sample/dir\\\"\n",
    "summary": "Pre-load first matching sample"
  },
  "midi_notes": {
    "doc": "Create a new immutable ring buffer of notes from args. Indexes wrap around positively and negatively. Final ring consists only of MIDI numbers and nil.",
    "examples": "(midi_notes :d3, :d4, :d5) #=> (ring 50, 62, 74)\"\n\"(midi_notes :d3, 62,  nil) #=> (ring 50, 62, nil)",
    "summary": "Create a ring buffer of midi note numbers"
  },
  "midi_to_hz": {
    "doc": "Convert a midi note to hz",
    "examples": "midi_to_hz(60) #=> 261.6256",
    "summary": "MIDI to Hz conversion"
  },
  "note": {
    "doc": "Takes a midi note, a symbol (e.g. `:C`) or a string (e.g. `\\\"C\\\"`) and resolves it to a midi note. You can also pass an optional `octave:` parameter to get the midi note for a given octave. Please note - `octave:` param overrides any octave specified in a symbol i.e. `:c3`. If the note is `nil`, `:r` or `:rest`, then `nil` is returned (`nil` represents a rest)",
    "examples": "# These all return 60 which is the midi number for middle C (octave 4)\nputs note(60)\nputs note(:C)\nputs note(:C4)\nputs note('C')\n\"\n\"# returns 60 - octave param has no effect if we pass in a number\nputs note(60, octave: 2)\n# These all return 36 which is the midi number for C2 (two octaves below middle C)\nputs note(:C, octave: 2)\nputs note(:C4, octave: 2) # note the octave param overrides any octaves specified in a symbol\nputs note('C', octave: 2)\n",
    "summary": "Describe note"
  },
  "note_info": {
    "doc": "Returns an instance of `SonicPi::Note`. Please note - `octave:` param overrides any octave specified in a symbol i.e. `:c3`",
    "examples": "puts (scale :C, :major) # returns the following ring of MIDI note numbers: (ring 60, 62, 64, 65, 67, 69, 71, 72)\"\n\"# anywhere you can use a list or ring of notes, you can also use scale\nplay_pattern (scale :C, :major)\"\n\"# you can use the :num_octaves parameter to get more notes\nplay_pattern (scale :C, :major, num_octaves: 2)\"\n\"# Scales can start with any note:\nputs (scale 50, :minor) #=> (ring 50, 52, 53, 55, 57, 58, 60, 62)\nputs (scale 50.1, :minor) #=> (ring 50.1, 52.1, 53.1, 55.1, 57.1, 58.1, 60.1, 62.1)\nputs (scale :minor) #=> (ring 0, 2, 3, 5, 7, 8, 10, 12)\"\n\" # scales are also rings\nlive_loop :scale_player do\nplay (scale :Eb3, :super_locrian).tick, release: 0.1\nsleep 0.125\nend\"\n\" # scales starting with 0 are useful in combination with sample's rpitch:\nlive_loop :scaled_sample do\nsample :bass_trance_c, rpitch: (scale 0, :minor).tick\nsleep 1\nend\"\n\"# Sonic Pi supports a large range of scales:\n(scale :C, :diatonic)\n(scale :C, :ionian)\n(scale :C, :major)\n(scale :C, :dorian)\n(scale :C, :phrygian)\n(scale :C, :lydian)\n(scale :C, :mixolydian)\n(scale :C, :aeolian)\n(scale :C, :minor)\n(scale :C, :locrian)\n(scale :C, :hex_major6)\n(scale :C, :hex_dorian)\n(scale :C, :hex_phrygian)\n(scale :C, :hex_major7)\n(scale :C, :hex_sus)\n(scale :C, :hex_aeolian)\n(scale :C, :minor_pentatonic)\n(scale :C, :yu)\n(scale :C, :major_pentatonic)\n(scale :C, :gong)\n(scale :C, :egyptian)\n(scale :C, :shang)\n(scale :C, :jiao)\n(scale :C, :zhi)\n(scale :C, :ritusen)\n(scale :C, :whole_tone)\n(scale :C, :whole)\n(scale :C, :chromatic)\n(scale :C, :harmonic_minor)\n(scale :C, :melodic_minor_asc)\n(scale :C, :hungarian_minor)\n(scale :C, :octatonic)\n(scale :C, :messiaen1)\n(scale :C, :messiaen2)\n(scale :C, :messiaen3)\n(scale :C, :messiaen4)\n(scale :C, :messiaen5)\n(scale :C, :messiaen6)\n(scale :C, :messiaen7)\n(scale :C, :super_locrian)\n(scale :C, :hirajoshi)\n(scale :C, :kumoi)\n(scale :C, :neapolitan_major)\n(scale :C, :bartok)\n(scale :C, :bhairav)\n(scale :C, :locrian_major)\n(scale :C, :ahirbhairav)\n(scale :C, :enigmatic)\n(scale :C, :neapolitan_minor)\n(scale :C, :pelog)\n(scale :C, :augmented2)\n(scale :C, :scriabin)\n(scale :C, :harmonic_major)\n(scale :C, :melodic_minor_desc)\n(scale :C, :romanian_minor)\n(scale :C, :hindu)\n(scale :C, :iwato)\n(scale :C, :melodic_minor)\n(scale :C, :diminished2)\n(scale :C, :marva)\n(scale :C, :melodic_major)\n(scale :C, :indian)\n(scale :C, :spanish)\n(scale :C, :prometheus)\n(scale :C, :diminished)\n(scale :C, :todi)\n(scale :C, :leading_whole)\n(scale :C, :augmented)\n(scale :C, :purvi)\n(scale :C, :chinese)\n(scale :C, :lydian_minor)\n",
    "summary": "Get note info"
  },
  "note_range": {
    "doc": "Produces a ring of all the notes between a low note and a high note. By default this is chromatic (all the notes) but can be filtered with a pitches: argument. This opens the door to arpeggiator style sequences and other useful patterns. If you try to specify only pitches which aren't in the range it will raise an error - you have been warned!",
    "examples": "(note_range :c4, :c5) # => (ring 60,61,62,63,64,65,66,67,68,69,70,71,72)\"\n\"(note_range :c4, :c5, pitches: (chord :c, :major)) # => (ring 60,64,67,72)\"\n\"(note_range :c4, :c6, pitches: (chord :c, :major)) # => (ring 60,64,67,72,76,79,84)\"\n\"(note_range :c4, :c5, pitches: (scale :c, :major)) # => (ring 60,62,64,65,67,69,71,72)\"\n\"(note_range :c4, :c5, pitches: [:c4, :g2]) # => (ring 60,67,72)\"\n\"live_loop :arpeggiator do\n# try changing the chord\nplay (note_range :c4, :c5, pitches: (chord :c, :major)).tick\nsleep 0.125\nend",
    "summary": "Get a range of notes"
  },
  "octs": {
    "doc": "Create a ring of successive octaves starting at `start` for `num_octaves`.",
    "examples": "(octs 60, 2)  #=> (ring 60, 72)\"\n\"(octs :e3, 3) #=> (ring 52, 64, 76)",
    "summary": "Create a ring of octaves"
  },
  "pitch_to_ratio": {
    "doc": "Convert a midi note to a ratio which when applied to a frequency will scale the frequency by the number of semitones. Useful for changing the pitch of a sample by using it as a way of generating the rate.",
    "examples": "pitch_to_ratio 12 #=> 2.0\"\n\"pitch_to_ratio 1 #=> 1.05946\"\n\"pitch_to_ratio -12 #=> 0.5\"\n\"sample :ambi_choir, rate: pitch_to_ratio(3) # Plays :ambi_choir 3 semitones above default.\"\n\"\n# Play a chromatic scale of semitones\n(range 0, 16).each do |n|                  # For each note in the range 0->16\nsample :ambi_choir, rate: pitch_to_ratio(n) # play :ambi_choir at the relative pitch\nsleep 0.5                                # and wait between notes\nend",
    "summary": "relative MIDI pitch to frequency ratio"
  },
  "play": {
    "doc": "Play note with current synth. Accepts a set of standard options which include control of an amplitude envelope with `attack:`, `decay:`, `sustain:` and `release:` phases. These phases are triggered in order, so the duration of the sound is attack + decay + sustain + release times. The duration of the sound does not affect any other notes. Code continues executing whilst the sound is playing through its envelope phases.\nAccepts optional args for modification of the synth being played. See each synth's documentation for synth-specific opts. See `use_synth` and `with_synth` for changing the current synth.\nIf note is `nil`, `:r` or `:rest`, play is ignored and treated as a rest. Also, if the `on:` opt is specified and returns `false`, or `nil` then play is similarly ignored and treated as a rest.\nNote that the default opts listed are only a guide to the most common opts across all the synths. Not all synths support all the default opts and each synth typically supports many more opts specific to that synth. For example, the `:tb303` synth supports 45 unique opts. For a full list of a synth's opts see its documentation in the Help system.\n",
    "examples": "play 50 # Plays note 50 on the current synth\"\n\"play 50, attack: 1 # Plays note 50 with a fade-in time of 1s\"\n\"play 62, pan: -1, release: 3 # Play note 62 in the left ear with a fade-out time of 3s.\"\n\" # controlling a synth synchronously\ns = play :e3, release: 4\nsleep 1\ncontrol s, note: :e5\nsleep 0.5\nuse_synth :dsaw\nplay :e3   # This is triggered after 1.5s from start\"\n\" # Controlling a synth asynchronously\nplay :e3, release: 4 do |s|\nsleep 1                                               # This block is run in an implicit in_thread\ncontrol s, note: :e5                                  # and therefore is asynchronous\nend\nsleep 0.5\nuse_synth :dsaw\nplay :e3 # This is triggered after 0.5s from start",
    "summary": "Play current synth"
  },
  "play_chord": {
    "doc": "Play a list of notes at the same time.\nAccepts optional args for modification of the synth being played. See each synth's documentation for synth-specific opts. See `use_synth` and `with_synth` for changing the current synth.",
    "examples": "play_chord [40, 45, 47\n# same as:\nplay 40\nplay 45\nplay 47\"\n\"play_chord [40, 45, 47], amp: 0.5\n# same as:\nplay 40, amp: 0.5\nplay 45, amp: 0.5\nplay 47, amp: 0.5\"\n\"play_chord chord(:e3, :minor)",
    "summary": "Play notes simultaneously"
  },
  "play_pattern": {
    "doc": "Play list of notes with the current synth one after another with a sleep of 1\nAccepts optional args for modification of the synth being played. See each synth's documentation for synth-specific opts. See use_synth and with_synth for changing the current synth.",
    "examples": "play_pattern [40, 41, 42] # Same as:\n#   play 40\n#   sleep 1\n#   play 41\n#   sleep 1\n#   play 42\n\"\n\"play_pattern [:d3, :c1, :Eb5] # You can use keyword notes\"\n\"play_pattern [:d3, :c1, :Eb5], amp: 0.5, cutoff: 90 # Supports the same arguments as play:",
    "summary": "Play pattern of notes"
  },
  "play_pattern_timed": {
    "doc": "Play each note in a list of notes one after another with specified times between them. The notes should be a list of MIDI numbers, symbols such as :E4 or chords such as chord(:A3, :major) - identical to the first parameter of the play function. The times should be a list of times between the notes in beats.\nIf the list of times is smaller than the number of gaps between notes, the list is repeated again. If the list of times is longer than the number of gaps between notes, then some of the times are ignored. See examples for more detail.\nAccepts optional args for modification of the synth being played. See each synth's documentation for synth-specific opts. See `use_synth` and `with_synth` for changing the current synth.",
    "examples": "play_pattern_timed [40, 42, 44, 46], [1, 2, 3\n# same as:\nplay 40\nsleep 1\nplay 42\nsleep 2\nplay 44\nsleep 3\nplay 46\"\n\"play_pattern_timed [40, 42, 44, 46, 49], [1, 0.5\n# same as:\nplay 40\nsleep 1\nplay 42\nsleep 0.5\nplay 44\nsleep 1\nplay 46\nsleep 0.5\nplay 49\"\n\"play_pattern_timed [40, 42, 44, 46], [0.5\n# same as:\nplay 40\nsleep 0.5\nplay 42\nsleep 0.5\nplay 44\nsleep 0.5\nplay 46\"\n\"play_pattern_timed [40, 42, 44], [1, 2, 3, 4, 5\n#same as:\nplay 40\nsleep 1\nplay 42\nsleep 2\nplay 44",
    "summary": "Play pattern of notes with specific times"
  },
  "ratio_to_pitch": {
    "doc": "Convert a frequency ratio to a midi note which when added to a note will transpose the note to match the frequency ratio.",
    "examples": "ratio_to_pitch 2 #=> 12.0\"\n\"ratio_to_pitch 0.5 #=> -12.0",
    "summary": "relative frequency ratio to MIDI pitch"
  },
  "recording_delete": {
    "doc": "After using `recording_start` and `recording_stop`, a temporary file is created until you decide to use `recording_save`. If you've decided you don't want to save it you can use this method to delete the temporary file straight away, otherwise the operating system will take care of deleting it later.",
    "examples": ","
  },
  "recording_save": {
    "doc": "Save previous recording to the specified location",
    "examples": ",",
    "summary": "Save recording"
  },
  "recording_start": {
    "doc": "Start recording all sound to a `.wav` file stored in a temporary directory.",
    "examples": ",",
    "summary": "Start recording"
  },
  "recording_stop": {
    "doc": "Stop current recording.",
    "examples": ",",
    "summary": "Stop recording"
  },
  "reset_mixer!": {
    "doc": "The master mixer is the final mixer that all sound passes through. This fn resets it to its default set - undoing any changes made via set_mixer_control!",
    "examples": "set_mixer_control! lpf: 70 # LPF cutoff value of master mixer is now 70\nsample :loop_amen          # :loop_amen sample is played with low cutoff\nsleep 3\nreset_mixer!               # mixer is now reset to default values\nsample :loop_amen          # :loop_amen sample is played with normal cutoff",
    "summary": "Reset master mixer"
  },
  "rest?": {
    "doc": "Given a note or an args map, returns true if it represents a rest and false if otherwise",
    "examples": "puts rest? nil # true\",\n\"puts rest? :r # true\"\n\"puts rest? :rest # true\"\n\"puts rest? 60 # false\"\n\"puts rest? {} # false\"\n\"puts rest? {note: :rest} # true\"\n\"puts rest? {note: nil} # true\"\n\"puts rest? {note: 50} # false",
    "summary": "Determine if note or args is a rest"
  },
  "sample": {
    "doc": "Play back a recorded sound file (sample). Sonic Pi comes with lots of great samples included (see the section under help) but you can also load and play `.wav`, `.wave`, `.aif`, `.aiff` or `.flac` files from anywhere on your computer too. To play a built-in sample use the corresponding keyword such as `sample :bd_haus`. To play any file on your computer use a full path such as `sample \\\"/path/to/sample.wav\\\"`.\nThere are many opts for manipulating the playback. For example, the `rate:` opt affects both the speed and the pitch of the playback. To control the rate of the sample in a pitch-meaningful way take a look at the `rpitch:` opt.\nThe sampler synth has three separate envelopes - one for amplitude, one for a low pass filter and another for a high pass filter. These work very similar to the standard synth envelopes except for two major differences. Firstly, the envelope times do not stretch or shrink to match the BPM. Secondly, the sustain time by default stretches to make the envelope fit the length of the sample. This is explained in detail in the tutorial.\nSamples are loaded on-the-fly when first requested (and subsequently remembered). If the sample loading process takes longer than the schedule ahead time, the sample trigger will be skipped rather than be played late and out of time. To avoid this you may preload any samples you wish to work with using `load_sample` or `load_samples`.\nIt is possible to set the `start:` and `finish:` positions within the sample to play only a sub-section of it. These values can be automatically chosen based on an onset detection algorithm which will essentially isolate each individual drum or synth hit in the sample and let you access each one by an integer index. See the `onset:` docstring and examples for more information.\nFinally, the sampler supports a powerful filtering system to make it easier to work with large folders of samples. The filter commands must be used before the first standard opt. There are six kinds of filter parameters you may use:\n1. Folder strings - `\\\"/foo/bar\\\"` - which will add all samples within the folder to the set of candidates.\n2. Recursive folder strings - `\\\"/foo/bar/**\\\"` - Folder strings ending with `**` will add all samples contained within all subfolders (searched recursively).\n3. Sample strings - `\\\"/path/to/sample.wav\\\"` - which will add the specific sample to the set of candidates.\n4. Other strings - `\\\"foobar\\\"` - which will filter the candidates based on whether the filename contains the string.\n5. Regular expressions - `/b[aA]z.*/` - which will filter the candidates based on whether the regular expression matches the filename.\n6. Keywords - `:quux` - will filter the candidates based on whether the keyword is a direct match of the filename (without extension).\n7. Numbers - `0` - will select the candidate with that index (wrapping round like a ring if necessary).\n8. Lists of the above - `[\\\"/foo/bar\\\", \\\"baz\\\", /0-9.*/]` - will recurse down and work through the internal filter parameters as if they were in the top level.\n9. Lambdas - `lambda {|s| [s.choose] } - the ultimate power tool for filters. Allows you to create a custom fn which receives a list of candidates as an arg and which should return a new list of candidates (this may be smaller, larger, re-ordered it's up to you).\nBy combining commands which add to the candidates and then filtering those candidates it is possible to work with folders full of samples in very powerful ways. Note that the specific ordering of filter parameters is irrelevant with the exception of the numbers - in which case the last number is the index. All the candidates will be gathered first before the filters are applied.\n",
    "examples": "# Play a built-in sample\nsample :loop_amen # Plays the Amen break\"\n\"\n# Play two samples at the same time\n# with incredible timing accuracy\nsample :loop_amen\nsample :ambi_lunar_land # Note, for timing guarantees select the pref:\n#   Studio -> Synths and FX -> Enforce timing guarantees\"\n\"\n# Create a simple repeating bass drum\nlive_loop :bass do\nsample :bd_haus\nsleep 0.5\nend\"\n\"\n# Create a more complex rhythm with multiple live loops:\nlive_loop :rhythm do\nsample :tabla_ghe3 if (spread 5, 7).tick\nsleep 0.125\nend\nlive_loop :bd, sync: :rhythm do\nsample :bd_haus, lpf: 90, amp: 2\nsleep 0.5\nend\"\n\"\n# Change the playback speed of the sample using rate:\nsample :loop_amen, rate: 0.5 # Play the Amen break at half speed\n# for old school hip-hop\"\n\"\n# Speed things up\nsample :loop_amen, rate: 1.5 # Play the Amen break at 1.5x speed\n# for a jungle/gabba sound\"\n\"\n# Go backwards\nsample :loop_amen, rate: -1 # Negative rates play the sample backwards\"\n\"\n# Fast rewind\nsample :loop_amen, rate: -3 # Play backwards at 3x speed for a fast rewind effect\"\n\"\n# Start mid sample\nsample :loop_amen, start: 0.5 # Start playback half way through\"\n\"\n# Finish mid sample\nsample :loop_amen, finish: 0.5 # Finish playback half way through\"\n\"\n# Play part of a sample\nsample :loop_amen, start: 0.125, finish: 0.25 # Play the second eighth of the sample\"\n\"\n# Finishing before the start plays backwards\nsample :loop_amen, start: 0.25, finish: 0.125 # Play the second eighth of the sample backwards\"\n\"\n# Play a section of a sample at quarter speed backwards\nsample :loop_amen, start: 0.125, finish: 0.25, rate: -0.25 # Play the second eighth of the\n# amen break backwards at a\n# quarter speed\"\n\"\n# Control a sample synchronously\ns = sample :loop_amen, lpf: 70\nsleep 0.5\ncontrol s, lpf: 130\nsleep 0.5\nsynth :dsaw, note: :e3 # This is triggered 1s from start\"\n\" # Controlling a sample asynchronously\nsample :loop_amen, lpf: 70 do |s|\nsleep 1                                # This block is run in an implicit in_thread\ncontrol s, lpf: 130                    # and therefore is asynchronous\nend\nsleep 0.5\nsynth :dsaw, note: :e3 # This is triggered 0.5s from start\"\n\"\n# Play with slices\nsample :loop_garzul, slice: 0      # => play the first 16th of the sample\nsleep 0.5\n4.times do\nsample :loop_garzul, slice: 1    # => play the second 16th of the sample 4 times\nsleep 0.125\nend\nsample :loop_garzul, slice: 4, num_slices: 4, rate: -1      # => play the final quarter backwards\n\"\n\"\n# Build a simple beat slicer\nuse_sample_bpm :loop_amen                    # Set the BPM to match the amen break sample\nlive_loop :beat_slicer do\nn = 8                                      # Specify number of slices\n# (try changing to 2, 4, 6, 16 or 32)\ns = rand_i n                               # Choose a random slice within range\nsample :loop_amen, slice: s, num_slices: n # Play the specific part of the sample\nsleep 1.0/n                                # Sleep for the duration of the slice\nend\"\n\"\n# Play with the built-in low pass filter, high pass filter and compressor\nsample :loop_amen, lpf: 80, hpf: 70, compress: 1, pre_amp: 10 # Make the amen break sound punchy.\"\n\"\n# Use the cutoff filter envelopes\nsample :loop_garzul, lpf_attack: 8 # Sweep the low pass filter up over 8 beats\nsleep 8\nsample :loop_garzul, hpf_attack: 8 # Sweep the high pass filter down over 8 beats\"\n\"\n# Sample stretching\nputs sample_duration :loop_industrial                   # => 0.88347\nputs sample_duration :loop_industrial, beat_stretch: 1  # => 1\nlive_loop :industrial do\nsample :loop_industrial, beat_stretch: 1              # Stretch the sample to make it 1 beat long\nsleep 1                                               # This now loops perfectly.\n# However, note that stretching/shrinking\n# also modifies the pitch.\nend\"\n\"\n# Sample shrinking\nputs sample_duration :loop_garzul                       # => 8\nputs sample_duration :loop_garzul, beat_stretch: 6      # => 6\nlive_loop :garzul do\nsample :loop_garzul, beat_stretch: 6                  # As :loop_garzul is longer than 6 beats\n# it is shrunk to fit. This increases the\n# pitch.\nsleep 6\nend\"\n\"\n# Sample stretching matches the BPM\nuse_bpm 30                                              # Set the BPM to 30\nputs sample_duration :loop_garzul                       # => 4.0 (at 30 BPM the sample lasts for 4 beats)\nputs sample_duration :loop_garzul, beat_stretch: 6      # => 6.0\nlive_loop :garzul do\nsample :loop_garzul, beat_stretch: 6                  # The sample is stretched to match 6 beats at 30 BPM\nsleep 6\nend\"\n\"\n# External samples\nsample \\\"/path/to/sample.wav\\\"                          # Play any Wav, Aif or FLAC sample on your computer\n# by simply passing a string representing the full\n# path\"\n\"\n# Sample pack filtering\ndir = \\\"/path/to/dir/of/samples\\\"                       # You can easily work with a directory of samples\nsample dir                                              # Play the first sample in the directory\n# (it is sorted alphabetically)\nsample dir, 1                                           # Play the second sample in the directory\nsample dir, 99                                          # Play the 100th sample in the directory, or if there\n# are fewer, treat the directory like a ring and keep\n# wrapping the index round until a sample is found.\n# For example, if there are 90 samples, the 10th sample\n# is played (index 9).\nsample dir, \\\"120\\\"                                     # Play the first sample in the directory that contains\n# the substring \\\"120\\\".\n# For example, this may be \\\"beat1_120_rave.wav\\\"\nsample dir, \\\"120\\\", 1                                  # Play the second sample in the directory that contains\n# the substring \\\"120\\\".\n# For example, this may be \\\"beat2_120_rave.wav\\\"\nsample dir, /beat[0-9]/                                 # Play the first sample in the directory that matches\n# the regular expression /beat[0-9]/.\n# For example, this may be \\\"beat0_100_trance.wav\\\"\n# You may use the full power of Ruby's regular expression\n# system here: http://ruby-doc.org/core-2.1.1/Regexp.html\nsample dir, /beat[0-9]0/, \\\"100\\\"                       # Play the first sample in the directory that both matches\n# the regular expression /beat[0-9]0/ and contains the\n# the substring \\\"100\\\".\n# For example, this may be \\\"beat10_100_rave.wav\\\"\"\n\"\n# Filtering built-in samples\n# If you don't pass a directory source, you can filter over\n# the built-in samples.\nsample \\\"tabla_\\\"                                       # Play the first built-in sample that contains the substring\n# \\\"tabla\\\"\nsample \\\"tabla_\\\", 2                                    # Play the third built-in sample that contains the substring\n# \\\"tabla\\\"\"\n\"\n# Play with whole directories of samples\nload_samples \\\"tabla_\\\"                                 # You may pass any of the source/filter options to load_samples\n# to load all matching samples. This will load all the built-in\n# samples containing the substring \\\"tabla_\\\"\nlive_loop :tabla do\nsample \\\"tabla_\\\", tick                               # Treat the matching samples as a ring and tick through them\nsleep 0.125\nend\"\n\"\n# Specify multiple sources\ndir1 = \\\"/path/to/sample/directory\\\"\ndir2 = \\\"/path/to/other/sample/directory\\\"\nsample dir1, dir2, \\\"foo\\\"                              # Match the first sample that contains the string \\\"foo\\\" out of\n# all the samples in dir1 and dir2 combined.\n# Note that the sources must be listed before any filters.\"\n\"\n# List contents recursively\ndir = \\\"/path/to/sample/directory\\\"                     # By default the list of all top-level samples within the directory\n# is considered.\ndir_recursive = \\\"/path/to/sample/directory/**\\\"        # However, if you finish your directory string with ** then if that\n# directory contains other directories then the samples within the\n# subdirectories and their subsubdirectories in turn are considered.\nsample dir, 0                                           # Play the first top-level sample in the directory\nsample dir_recursive, 0                                 # Play the first sample found after combining all samples found in\n# the directory and all directories within it recursively.\n# Note that if there are many sub directories this may take some time\n# to execute. However, the result is cached so subsequent calls will\n# be fast.\"\n\"\n# Bespoke filters\nfilter = lambda do |candidates|                         # If the built-in String, Regexp and index filters are not sufficient\n[candidates.choose]                                   # you may write your own. They need to be a function which takes a list\nend                                                     # of paths to samples and return a list of samples. This one returns a\n# list of a single randomly selected sample.\n8.times do\nsample \\\"drum_\\\", filter                              # Play 8 randomly selected samples from the built-in sample set that also\nsleep 0.25                                            # contain the substring \\\"drum_\\\"\nend\"\n\"\n# Basic Onset Detection\nsample :loop_tabla, start: 0, finish: 0.00763           # If you know the right start: and finish: values, you can extract a\n# single drum hit from a longer sample. However, finding these values\n# can be very time consuming.\nsleep 1\n# Instead of specifying the start: and finish: values manually you can\n# use the onset: option to find them for you using an integer index.\nsample :loop_tabla, onset: 0                            # onset: 0 will set the start: and finish: values so that the first\n# percussive sound (something that shifts from quiet to loud quickly)\n# is picked out.\nsleep 1\nsample :loop_tabla, onset: 1                            # We can easily find the second percussive sound in the sample with\n# onset: 1\"\n\"\n# Ticking through onsets\n# The onsets are actually a ring so the index will wrap around. This\n# means that if there are only 8 onsets in a sample, specifying an\n# onset of 100 will still return one of the 8 onsets. This means we\n# can use tick to work through each onset in sequence. This allows us\n# to redefine the rhythm and tempo of a sample\nlive_loop :tabla do\nuse_bpm 50                                            # We can choose our own BPM here - it doesn't need to match the sample\nsample :loop_tabla, onset: tick                       # tick through each onset in sequence\nsleep [0.125, 0.25].choose                            # randomly choose a delay between onset triggers\nend\n\"\n\"\n# Random Onset Triggering\n# We can easily pick a random onset using the pick fn\nuse_bpm 50\nlive_loop :tabla do\nsample :loop_tabla, onset: pick                       # Each time round the live loop we now trigger a random onset\nsleep [0.125, 0.25].choose                            # creating an infinite stream of randomly selected drums\nend\n\"\n\"\n# Repeatable Random Onsets\n# Instead of an infinite stream of choices, we can combine iteration\n# and use_random_seed to create repeatable riffs:\nlive_loop :tabla do\nuse_random_seed 30000                                 # every 8 times, reset the random seed, this resets the riff\n8.times do\nsample :loop_tabla, onset: pick\nsleep [0.125, 0.25].choose\nend\nend\n\"\n\"\n#  Random Onset Duration\n# Each onset has a variable length (determined by the sample contents).\n# Therefore, if you wish to ensure each onset has a specific length it\n# is necessary to use the sample's amplitude envelope.\n# As the sample's envelope automatically changes the sustain: value to\n# match the duration - you also need to override this with a value of 0.\nlive_loop :tabla do\nsample :loop_tabla, onset: pick, sustain: 0, release: 0.1 # Each drum onset will now be no longer than 0.1. Note that the envelope\n# for a sample only determines the maximum duration of a sample trigger.\n# If the actual audible duration of the onset is smaller than 0.1 then\n# it will *not* be extended.\nsleep [0.125, 0.25].choose\nend\n\"\n\"\n# Onset lambdas\n# The onset index can be a lambda as well as an integer. If a lambda is\n# given, it will be passed a ring of all of the onsets as an argument.\n# This will be a ring of maps:\nl = lambda {|c| puts c ; c[0]}                          # define a lambda which accepts a single argument, prints it and\n# returns the first value. This particular example is essentially\n# the same as using onset: 0 with the side effect of also printing out\n# the full ring of onsets:\nsample :loop_tabla, onset: l                            # (ring {:start=>0.0, :finish=>0.0076}, {:start=>0.0076, :finish 0.015}...)\n# We are therefore free to define this lambda to do anything we want.\n# This gives us very powerful control over the choice of onset. It is\n# unlikely you will use this frequently, but it is a powerful tool\n# that's there when you need it.\n",
    "summary": "Trigger sample"
  },
  "sample_buffer": {
    "doc": "Alias for the `load_sample` method. Loads sample if necessary and returns buffer information.",
    "examples": "see load_sample",
    "summary": "Get sample data"
  },
  "sample_duration": {
    "doc": "Given the name of a loaded sample, or a path to a `.wav`, `.wave`, `.aif`, `.aiff` or `.flac` file returns the length of time in beats that the sample would play for. `sample_duration` understands and accounts for all the opts you can pass to `sample` which have an effect on the playback duration such as `rate:`. The time returned is scaled to the current BPM.\n*Note:* avoid using `sample_duration` to set the sleep time in `live_loop`s, prefer stretching the sample with the `beat_stretch:` opt or changing the BPM instead. See the examples below for details.",
    "examples": "# Simple use\nputs sample_duration(:loop_garzul) # returns 8.0 because this sample is 8 seconds long\n\"\n\"\n# The result is scaled to the current BPM\nuse_bpm 120\nputs sample_duration(:loop_garzul) # => 16.0\nuse_bpm 90\nputs sample_duration(:loop_garzul) # => 12.0\nuse_bpm 21\nputs sample_duration(:loop_garzul) # => 2.8\n\"\n\"\n# Avoid using sample_duration to set the sleep time in live_loops\nlive_loop :avoid_this do               # It is possible to use sample_duration to drive the frequency of a live loop.\nwith_fx :slicer do                   # However, if you're using a rhythmical sample such as a drum beat and it isn't\nsample :loop_amen                  # in the same BPM as the current BPM, then the FX such as this slicer will be\nsleep sample_duration(:loop_amen)  # badly out of sync. This is because the slicer slices at the current BPM and\nend                                  # this live_loop is looping at a different BPM (that of the sample)\nend\nlive_loop :prefer_this do              # Instead prefer to set the BPM of the live_loop to match the sample. It has\nuse_sample_bpm :loop_amen            # two benefits. Now our sleep is a nice and simple 1 (as it's one beat).\nwith_fx :slicer do                   # Also, our slicer now works with the beat and sounds much better.\nsample :loop_amen\nsleep 1\nend\nend\nlive_loop :or_this do                  # Alternatively we can beat_stretch the sample to match the current BPM. This has the\nwith_fx :slicer do                   # side effect of changing the rate of the sample (and hence the pitch). However, the\nsample :loop_amen, beat_stretch: 1 # FX works nicely in time and the sleep time is also a simple 1.\nsleep 1\nend\nend\n\"\n\"\n# The standard sample opts are also honoured\n# Playing a sample at standard speed will return standard length\nsample_duration :loop_garzul, rate: 1                             # => 8.0\n# Playing a sample at half speed will double duration\nsample_duration :loop_garzul, rate: 0.5                           # => 16.0\n# Playing a sample at double speed will halve duration\nsample_duration :loop_garzul, rate: 2                             # => 4.0\n# Playing a sample backwards at double speed will halve duration\nsample_duration :loop_garzul, rate: -2                            # => 4.0\n# Without an explicit sustain: opt attack: just affects amplitude not duration\nsample_duration :loop_garzul, attack: 1                           # => 8.0\nsample_duration :loop_garzul, attack: 100                         # => 8.0\nsample_duration :loop_garzul, attack: 0                           # => 8.0\n# Without an explicit sustain: opt release: just affects amplitude not duration\nsample_duration :loop_garzul, release: 1                          # => 8.0\nsample_duration :loop_garzul, release: 100                        # => 8.0\nsample_duration :loop_garzul, release: 0                          # => 8.0\n# Without an explicit sustain: opt decay: just affects amplitude not duration\nsample_duration :loop_garzul, decay: 1                            # => 8.0\nsample_duration :loop_garzul, decay: 100                          # => 8.0\nsample_duration :loop_garzul, decay: 0                            # => 8.0\n# With an explicit sustain: opt, if the attack + decay + sustain + release envelope\n# duration is less than the sample duration time, the envelope will shorten the\n# sample time.\nsample_duration :loop_garzul, sustain: 0, attack: 0.5             # => 0.5\nsample_duration :loop_garzul, sustain: 0, decay: 0.1              # => 0.1\nsample_duration :loop_garzul, sustain: 0, release: 1              # => 1.0\nsample_duration :loop_garzul, sustain: 2, attack: 0.5, release: 1 # => 3.5\n# If the envelope duration is longer than the sample it will not affect the\n# sample duration\nsample_duration :loop_garzul, sustain: 0, attack: 8, release: 3   # => 8\n# All other opts are taken into account before the comparison with the envelope opts.\nsample_duration :loop_garzul, rate: 10                            # => 0.8\nsample_duration :loop_garzul, sustain: 0, attack: 0.9, rate: 10   # => 0.8 (The duration of the sample is less than the envelope length so wins)\n# The rpitch: opt will modify the rate to shift the pitch of the sample up and down\n# and therefore affects duration.\nsample_duration :loop_garzul, rpitch: 12                          # => 4.0\nsample_duration :loop_garzul, rpitch: -12                         # => 16\n# The rpitch: and rate: opts combine together.\nsample_duration :loop_garzul, rpitch: 12, rate: 2                 # => 2.0\n# The beat_stretch: opt stretches the sample so that its duration matches the value.\n# It also combines with rate:\nsample_duration :loop_garzul, beat_stretch: 3                     # => 3.0\nsample_duration :loop_garzul, beat_stretch: 3, rate: 0.5          # => 6.0\n# The pitch_stretch: opt acts identically to beat_stretch when just considering sample\n# duration.\nsample_duration :loop_garzul, pitch_stretch: 3                    # => 3.0\nsample_duration :loop_garzul, pitch_stretch: 3, rate: 0.5         # => 6.0\n# The start: and finish: opts can also shorten the sample duration and also combine\n# with other opts such as rate:\nsample_duration :loop_garzul, start: 0.5                          # => 4.0\nsample_duration :loop_garzul, start: 0.5, finish: 0.75            # => 2.0\nsample_duration :loop_garzul, finish: 0.5, start: 0.75            # => 2.0\nsample_duration :loop_garzul, rate: 2, finish: 0.5, start: 0.75 # => 1.0\n\"\n\"\n# Triggering samples one after another\nsample :loop_amen                    # start the :loop_amen sample\nsleep sample_duration(:loop_amen)    # wait for the duration of :loop_amen before\nsample :loop_amen                    # starting it again\n",
    "summary": "Get duration of sample in beats"
  },
  "sample_free": {
    "doc": "Frees the memory and resources consumed by loading the sample on the server. Subsequent calls to `sample` and friends will re-load the sample on the server.\nYou may also specify the same set of source and filter pre-args available to `sample` itself. `sample_free` will then free all matching samples. See `sample`'s docs for more information.",
    "examples": "sample :loop_amen # The Amen break is now loaded into memory and played\nsleep 2\nsample :loop_amen # The Amen break is not loaded but played from memory\nsleep 2\nsample_free :loop_amen # The Amen break is freed from memory\nsample :loop_amen # the Amen break is re-loaded and played\"\n\"\nputs sample_info(:loop_amen).to_i # This returns the buffer id of the sample i.e. 1\nputs sample_info(:loop_amen).to_i # The buffer id remains constant whilst the sample\n# is loaded in memory\nsample_free :loop_amen\nputs sample_info(:loop_amen).to_i # The Amen break is re-loaded and gets a *new* id.\"\n\"\nsample :loop_amen\nsample :ambi_lunar_land\nsleep 2\nsample_free :loop_amen, :ambi_lunar_land\nsample :loop_amen                        # re-loads and plays amen\nsample :ambi_lunar_land                  # re-loads and plays lunar land\"\n\"# Using source and filter pre-args\ndir = \\\"/path/to/sample/dir\\\"\nsample_free dir # frees any loaded samples in \\\"/path/to/sample/dir\\\"\nsample_free dir, 1 # frees sample with index 1 in \\\"/path/to/sample/dir\\\"\nsample_free dir, :foo # frees sample with name \\\"foo\\\" in \\\"/path/to/sample/dir\\\"\nsample_free dir, /[Bb]ar/ # frees sample which matches regex /[Bb]ar/ in \\\"/path/to/sample/dir\\\"\n",
    "summary": "Free a sample on the synth server"
  },
  "sample_free_all": {
    "doc": "Unloads all samples therefore freeing the memory and resources consumed. Subsequent calls to `sample` and friends will re-load the sample on the server.",
    "examples": "sample :loop_amen        # load and play :loop_amen\nsample :ambi_lunar_land  # load and play :ambi_lunar_land\nsleep 2\nsample_free_all\nsample :loop_amen        # re-loads and plays amen",
    "summary": "Free all loaded samples on the synth server"
  },
  "sample_info": {
    "doc": "Alias for the `load_sample` method. Loads sample if necessary and returns sample information.",
    "examples": "see load_sample",
    "summary": "Get sample information"
  },
  "sample_loaded?": {
    "doc": "Given a path to a `.wav`, `.wave`, `.aif`, `.aiff` or `.flac` file, returns `true` if the sample has already been loaded.",
    "examples": "load_sample :elec_blip # :elec_blip is now loaded and ready to play as a sample\nputs sample_loaded? :elec_blip # prints true because it has been pre-loaded\nputs sample_loaded? :misc_burp # prints false because it has not been loaded",
    "summary": "Test if sample was pre-loaded"
  },
  "sample_names": {
    "doc": "Return a ring of sample names for the specified group",
    "examples": "load_synthdefs \\\"~/Desktop/my_noises\\\" # Load all synthdefs in my_noises folder",
    "summary": "Get sample names"
  },
  "sample_paths": {
    "doc": "Accepts the same pre-args and opts as `sample` and returns a ring of matched sample paths.",
    "examples": "sample_paths \\\"/path/to/samples/\\\" #=> ring of all top-level samples in /path/to/samples\"\n\"\nsample_paths \\\"/path/to/samples/**\\\" #=> ring of all nested samples in /path/to/samples\"\n\"\nsample_paths \\\"/path/to/samples/\\\", \\\"foo\\\" #=> ring of all samples in /path/to/samples\ncontaining the string \\\"foo\\\" in their filename.\"     ",
    "summary": "Sample Pack Filter Resolution"
  },
  "scale_names": {
    "doc": "Returns a ring containing all scale names known to Sonic Pi",
    "examples": "puts scale_names #=>  prints a list of all the scales",
    "summary": "All scale names"
  },
  "set_cent_tuning!": {
    "doc": "Globally tune Sonic Pi to play with another external instrument.\nUniformly tunes your music by shifting all notes played by the specified number of cents. To shift up by a cent use a cent tuning of 1. To shift down use negative numbers. One semitone consists of 100 cents.\nSee `use_cent_tuning` for setting the cent tuning value locally for a specific thread or `live_loop`. This is a global value and will shift the tuning for *all* notes. It will also persist for the entire session.\nImportant note: the cent tuning set by `set_cent_tuning!` is independent of any thread-local cent tuning values set by `use_cent_tuning` or `with_cent_tuning`. ",
    "examples": "play 50 # Plays note 50\nset_cent_tuning! 1\nplay 50 # Plays note 50.01",
    "summary": "Global Cent tuning"
  },
  "set_control_delta!": {
    "doc": "Specify how many seconds between successive modifications (i.e. trigger then controls) of a specific node on a specific thread. Set larger if you are missing control messages sent extremely close together in time.",
    "examples": "\nset_control_delta! 0.1                 # Set control delta to 0.1\ns = play 70, release: 8, note_slide: 8 # Play a note and set the slide time\ncontrol s, note: 82                    # immediately start sliding note.\n# This control message might not be\n# correctly handled as it is sent at the\n# same virtual time as the trigger.\n# If you don't hear a slide, try increasing the\n# control delta until you do.",
    "summary": "Set control delta globally"
  },
  "set_mixer_control!": {
    "doc": "The master mixer is the final mixer that all sound passes through. This fn gives you control over the master mixer allowing you to manipulate all the sound playing through Sonic Pi at once. For example, you can sweep a lpf or hpf over the entire sound. You can reset the controls back to their defaults with `reset_mixer!`.",
    "examples": "set_mixer_control! lpf: 30, lpf_slide: 16 # slide the global lpf to 30 over 16 beats.",
    "summary": "Control master mixer"
  },
  "set_sched_ahead_time!": {
    "doc": "Specify how many seconds ahead of time the synths should be triggered. This represents the amount of time between pressing 'Run' and hearing audio. A larger time gives the system more room to work with and can reduce performance issues in playing fast sections on slower platforms. However, a larger time also increases latency between modifying code and hearing the result whilst live coding.",
    "examples": "set_sched_ahead_time! 1 # Code will now run approximately 1 second ahead of audio.",
    "summary": "Set sched ahead time globally"
  },
  "set_volume!": {
    "doc": "Set the main system volume to `vol`. Accepts a value between `0` and `5` inclusive. Vols greater or smaller than the allowed values are trimmed to keep them within range. Default is `1`.",
    "examples": "set_volume! 2 # Set the main system volume to 2\"\n\"set_volume! -1 # Out of range, so sets main system volume to 0\"\n\"set_volume! 7 # Out of range, so sets main system volume to 5",
    "summary": "Set Volume globally"
  },
  "status": {
    "doc": "This returns a Hash of information about the synthesis environment. Mostly used for debugging purposes.",
    "examples": "puts status # Returns something similar to:\n# {\n#   :ugens=>10\n#   :synths=>1\n#   :groups=>7\n#   :sdefs=>61\n#   :avg_cpu=>0.20156468451023102\n#   :peak_cpu=>0.36655542254447937\n#   :nom_samp_rate=>44100.0\n#   :act_samp_rate=>44099.9998411752\n#   :audio_busses=>2\n#   :control_busses=>0\n# }\n",
    "summary": "Get server status"
  },
  "synth": {
    "doc": "Trigger specified synth with given opts. Bypasses `current_synth` value, yet still honours `current_synth_defaults`. When using `synth`, the note is no longer an explicit argument but an opt with the key `note:`.\nIf note: opt is `nil`, `:r` or `:rest`, play is ignored and treated as a rest. Also, if the `on:` opt is specified and returns `false`, or `nil` then play is similarly ignored and treated as a rest.\nIf the synth name is `nil` behaviour is identical to that of `play` in that the `current_synth` will determine the actual synth triggered.\nIf a block is given, it is assumed to take one arg which will be the controllable synth node and the body of the block is run in an implicit `in_thread`. This allows for asynchronous control of the synth without interferring with time. For synchronous control capture the result of `synth` as a variable and use that.\nNote that the default opts listed are only a guide to the most common opts across all the synths. Not all synths support all the default opts and each synth typically supports many more opts specific to that synth. For example, the `:tb303` synth supports 45 unique opts. For a full list of a synth's opts see its documentation in the Help system. This can be accessed directly by clicking on the name of the synth and using the shortcut `C-i`",
    "examples": "\nuse_synth :beep            # Set current synth to :beep\nplay 60                    # Play note 60 with opt defaults\nsynth :dsaw, note: 60    # Bypass current synth and play :dsaw\n# with note 60 and opt defaults \"\n\"\nsynth :fm, note: 60, amp: 0.5 # Play note 60 of the :fm synth with an amplitude of 0.5\"\n\"\nuse_synth_defaults release: 5\nsynth :dsaw, note: 50 # Play note 50 of the :dsaw synth with a release of 5\"\n\"# You can play chords with the notes: opt:\nsynth :dsaw, notes: (chord :e3, :minor)\"\n\"\n# on: vs if\nnotes = (scale :e3, :minor_pentatonic, num_octaves: 2)\nlive_loop :rhyth do\n8.times do\ntrig = (spread 3, 7).tick(:rhyth)\nsynth :tri, on: trig, note: notes.tick, release: 0.1  # Here, we're calling notes.tick\n# every time we attempt to play the synth\n# so the notes rise faster than rhyth2\nsleep 0.125\nend\nend\nlive_loop :rhyth2 do\n8.times do\ntrig = (spread 3, 7).tick(:rhyth)\nsynth :saw, note: notes.tick, release: 0.1 if trig  # Here, we're calling notes.tick\n# only when the spread says to play\n# so the notes rise slower than rhyth\nsleep 0.125\nend\nend\n\"\n\" # controlling a synth synchronously\ns = synth :beep, note: :e3, release: 4\nsleep 1\ncontrol s, note: :e5\nsleep 0.5\nsynth :dsaw, note: :e3   # This is triggered after 1.5s from start\"\n\" # Controlling a synth asynchronously\nsynth :beep, note: :e3, release: 4 do |s|\nsleep 1                                               # This block is run in an implicit in_thread\ncontrol s, note: :e5                                  # and therefore is asynchronous\nend\nsleep 0.5\nsynth :dsaw, note: :e3 # This is triggered after 0.5s from start",
    "summary": "Trigger specific synth"
  },
  "use_arg_bpm_scaling": {
    "doc": "Turn synth argument bpm scaling on or off for the current thread. This is on by default. Note, using `rt` for args will result in incorrect times when used after turning arg bpm scaling off.",
    "examples": "use_bpm 120\nplay 50, release: 2 # release is actually 1 due to bpm scaling\nsleep 2             # actually sleeps for 1 second\nuse_arg_bpm_scaling false\nplay 50, release: 2 # release is now 2\nsleep 2             # still sleeps for 1 second\"\n\"                       # Interaction with rt\nuse_bpm 120\nplay 50, release: rt(2) # release is 2 seconds\nsleep rt(2)             # sleeps for 2 seconds\nuse_arg_bpm_scaling false\nplay 50, release: rt(2) # ** Warning: release is NOT 2 seconds! **\nsleep rt(2)             # still sleeps for 2 seconds",
    "summary": "Enable and disable BPM scaling"
  },
  "use_arg_checks": {
    "doc": "When triggering synths, each argument is checked to see if it is sensible. When argument checking is enabled and an argument isn't sensible, you'll see an error in the debug pane. This setting allows you to explicitly enable and disable the checking mechanism. See with_arg_checks for enabling/disabling argument checking only for a specific `do`/`end` block.",
    "examples": "play 50, release: 5 # Args are checked\nuse_arg_checks false\nplay 50, release: 5 # Args are not checked",
    "summary": "Enable and disable arg checks"
  },
  "use_cent_tuning": {
    "doc": "Uniformly tunes your music by shifting all notes played by the specified number of cents. To shift up by a cent use a cent tuning of 1. To shift down use negative numbers. One semitone consists of 100 cents.\nSee `with_cent_tuning` for setting the cent tuning value only for a specific `do`/`end` block. To transpose entire semitones see `use_transpose`.",
    "examples": "play 50 # Plays note 50\nuse_cent_tuning 1\nplay 50 # Plays note 50.01",
    "summary": "Cent tuning"
  },
  "use_debug": {
    "doc": "Enable or disable messages created on synth triggers. If this is set to false, the synths will be silent until debug is turned back on. Silencing debug messages can reduce output noise and also increase performance on slower platforms. See `with_debug` for setting the debug value only for a specific `do`/`end` block.",
    "examples": "use_debug true # Turn on debug messages\", \"use_debug false # Disable debug messages",
    "summary": "Enable and disable debug"
  },
  "use_merged_sample_defaults": {
    "doc": "Specify new default values to be used by all subsequent calls to `sample`. Merges the specified values with any previous defaults, rather than replacing them.",
    "examples": "sample :loop_amen # plays amen break with default arguments\nuse_merged_sample_defaults amp: 0.5, cutoff: 70\nsample :loop_amen # plays amen break with an amp of 0.5, cutoff of 70 and defaults for rest of args\nuse_merged_sample_defaults cutoff: 90\nsample :loop_amen  # plays amen break with a cutoff of 90 and and an amp of 0.5 with defaults for rest of args\n",
    "summary": "Merge new sample defaults"
  },
  "use_merged_synth_defaults": {
    "doc": "Specify synth arg values to be used by any following call to play. Merges the specified values with any previous defaults, rather than replacing them.",
    "examples": "play 50 #=> Plays note 50\nuse_merged_synth_defaults amp: 0.5\nplay 50 #=> Plays note 50 with amp 0.5\nuse_merged_synth_defaults cutoff: 80\nplay 50 #=> Plays note 50 with amp 0.5 and cutoff 80\nuse_merged_synth_defaults amp: 0.7\nplay 50 #=> Plays note 50 with amp 0.7 and cutoff 80\n\"\n\"use_synth_defaults amp: 0.5, cutoff: 80, pan: -1\nuse_merged_synth_defaults amp: 0.7\nplay 50 #=> Plays note 50 with amp 0.7, cutoff 80 and pan -1",
    "summary": "Merge synth defaults"
  },
  "use_octave": {
    "doc": "Transposes your music by shifting all notes played by the specified number of octaves. To shift up by an octave use a transpose of 1. To shift down use negative numbers. See `with_octave` for setting the octave shift only for a specific `do`/`end` block. For transposing the notes within the octave range see `use_transpose`.",
    "examples": "play 50 # Plays note 50\nuse_octave 1\nplay 50 # Plays note 62\"\n\"\n# You may change the transposition multiple times:\nplay 62 # Plays note 62\nuse_octave -1\nplay 62 # Plays note 50\nuse_octave 2\nplay 62 # Plays note 86",
    "summary": "Note octave transposition"
  },
  "use_sample_bpm": {
    "doc": "Modify bpm so that sleeping for 1 will sleep for the duration of the sample.",
    "examples": "use_sample_bpm :loop_amen  #Set bpm based on :loop_amen duration\nlive_loop :dnb do\nsample :bass_dnb_f\nsample :loop_amen\nsleep 1                  #`sleep`ing for 1 actually sleeps for duration of :loop_amen\nend\"\n\"\nuse_sample_bpm :loop_amen, num_beats: 4  # Set bpm based on :loop_amen duration\n# but also specify that the sample duration\n# is actually 4 beats long.\nlive_loop :dnb do\nsample :bass_dnb_f\nsample :loop_amen\nsleep 4                  #`sleep`ing for 4 actually sleeps for duration of :loop_amen\n# as we specified that the sample consisted of\n# 4 beats\nend",
    "summary": "Sample-duration-based bpm modification"
  },
  "use_sample_defaults": {
    "doc": "Specify new default values to be used by all subsequent calls to `sample`. Will remove and override any previous defaults.",
    "examples": "sample :loop_amen # plays amen break with default arguments\nuse_sample_defaults amp: 0.5, cutoff: 70\nsample :loop_amen # plays amen break with an amp of 0.5, cutoff of 70 and defaults for rest of args\nuse_sample_defaults cutoff: 90\nsample :loop_amen  # plays amen break with a cutoff of 90 and defaults for rest of args - note that amp is no longer 0.5\n",
    "summary": "Use new sample defaults"
  },
  "use_synth": {
    "doc": "Switch the current synth to `synth_name`. Affects all further calls to `play`. See `with_synth` for changing the current synth only for a specific `do`/`end` block.",
    "examples": "play 50 # Plays with default synth\nuse_synth :mod_sine\nplay 50 # Plays with mod_sine synth",
    "summary": "Switch current synth"
  },
  "use_synth_defaults": {
    "doc": "Specify new default values to be used by all subsequent calls to `play`. Will remove and override any previous defaults.",
    "examples": "play 50 # plays note 50 with default arguments\nuse_synth_defaults amp: 0.5, cutoff: 70\nplay 50 # plays note 50 with an amp of 0.5, cutoff of 70 and defaults for rest of args\nuse_synth_defaults cutoff: 90\nplay 50 # plays note 50 with a cutoff of 90 and defaults for rest of args - note that amp is no longer 0.5\n",
    "summary": "Use new synth defaults"
  },
  "use_timing_guarantees": {
    "doc": "If set to true, synths will not trigger if it is too late. If false, some synth triggers may be late.",
    "examples": "use_timing_guarantees true\nsample :loop_amen  #=> if time is behind by any margin, this will not trigger\"\n\"\nuse_timing_guarantees false\nsample :loop_amen  #=> unless time is too far behind, this will trigger even when late.",
    "summary": "Inhibit synth triggers if too late"
  },
  "use_transpose": {
    "doc": "Transposes your music by shifting all notes played by the specified amount. To shift up by a semitone use a transpose of 1. To shift down use negative numbers. See `with_transpose` for setting the transpose value only for a specific `do`/`end` block. To transpose entire octaves see `use_octave`.",
    "examples": "play 50 # Plays note 50\nuse_transpose 1\nplay 50 # Plays note 51\"\n\"\n# You may change the transposition multiple times:\nplay 62 # Plays note 62\nuse_transpose -12\nplay 62 # Plays note 50\nuse_transpose 3\nplay 62 # Plays note 65",
    "summary": "Note transposition"
  },
  "use_tuning": {
    "doc": "In most music we make semitones by dividing the octave into 12 equal parts, which is known as equal temperament. However there are lots of other ways to tune the 12 notes. This method adjusts each midi note into the specified tuning system. Because the ratios between notes aren't always equal, be careful to pick a centre note that is in the key of the music you're making for the best sound. Currently available tunings are `:just`, `:pythagorean`, `:meantone` and the default of `:equal`",
    "examples": "play :e4 # Plays note 64\nuse_tuning :just, :c\nplay :e4 # Plays note 63.8631\n# transparently changes midi notes too\nplay 64 # Plays note 63.8631\"\n\"\n# You may change the tuning multiple times:\nplay 64 # Plays note 64\nuse_tuning :just\nplay 64 # Plays note 63.8631\nuse_tuning :equal\nplay 64 # Plays note 64",
    "summary": "Use alternative tuning systems"
  },
  "with_arg_bpm_scaling": {
    "doc": "Turn synth argument bpm scaling on or off for the supplied block. Note, using `rt` for args will result in incorrect times when used within this block.",
    "examples": "use_bpm 120\nplay 50, release: 2 # release is actually 1 due to bpm scaling\nwith_arg_bpm_scaling false do\nplay 50, release: 2 # release is now 2\nend\"\n\"                         # Interaction with rt\nuse_bpm 120\nplay 50, release: rt(2)   # release is 2 seconds\nsleep rt(2)               # sleeps for 2 seconds\nwith_arg_bpm_scaling false do\nplay 50, release: rt(2) # ** Warning: release is NOT 2 seconds! **\nsleep rt(2)             # still sleeps for 2 seconds\nend",
    "summary": "Block-level enable and disable BPM scaling"
  },
  "with_arg_checks": {
    "doc": "Similar to `use_arg_checks` except only applies to code within supplied `do`/`end` block. Previous arg check value is restored after block.",
    "examples": "# Turn on arg checking:\nuse_arg_checks true\nplay 80, cutoff: 100 # Args are checked\nwith_arg_checks false do\n#Arg checking is now disabled\nplay 50, release: 3 # Args are not checked\nsleep 1\nplay 72             # Arg is not checked\nend\n# Arg checking is re-enabled\nplay 90 # Args are checked\n",
    "summary": "Block-level enable and disable arg checks"
  },
  "with_cent_tuning": {
    "doc": "Similar to `use_cent_tuning` except only applies cent shift to code within supplied `do`/`end` block. Previous cent tuning value is restored after block. One semitone consists of 100 cents. To transpose entire semitones see `with_transpose`.",
    "examples": "use_cent_tuning 1\nplay 50 # Plays note 50.01\nwith_cent_tuning 2 do\nplay 50 # Plays note 50.02\nend\n# Original cent tuning value is restored\nplay 50 # Plays note 50.01\n",
    "summary": "Block-level cent tuning"
  },
  "with_debug": {
    "doc": "Similar to use_debug except only applies to code within supplied `do`/`end` block. Previous debug value is restored after block.",
    "examples": "# Turn on debugging:\nuse_debug true\nplay 80 # Debug message is sent\nwith_debug false do\n#Debug is now disabled\nplay 50 # Debug message is not sent\nsleep 1\nplay 72 # Debug message is not sent\nend\n# Debug is re-enabled\nplay 90 # Debug message is sent\n",
    "summary": "Block-level enable and disable debug"
  },
  "with_fx": {
    "doc": "This applies the named effect (FX) to everything within a given `do`/`end` block. Effects may take extra parameters to modify their behaviour. See FX help for parameter details.\nFor advanced control, it is also possible to modify the parameters of an effect within the body of the block. If you define the block with a single argument, the argument becomes a reference to the current effect and can be used to control its parameters (see examples).",
    "examples": "# Basic usage\nwith_fx :distortion do # Use the distortion effect with default parameters\nplay 50 # => plays note 50 with distortion\nsleep 1\nsample :loop_amen # => plays the loop_amen sample with distortion too\nend\"\n\"# Specify effect parameters\nwith_fx :level, amp: 0.3 do # Use the level effect with the amp parameter set to 0.3\nplay 50\nsleep 1\nsample :loop_amen\nend\"\n\"\n# Controlling the effect parameters within the block\nwith_fx :reverb, mix: 0.1 do |fx|\n# here we set the reverb level quite low to start with (0.1)\n# and we can change it later by using the 'fx' reference we've set up\nplay 60 # plays note 60 with a little bit of reverb\nsleep 2\ncontrol fx, mix: 0.5 # change the parameters of the effect to add more reverb\nplay 60 # again note 60 but with more reverb\nsleep 2\ncontrol fx, mix: 1 # change the parameters of the effect to add more reverb\nplay 60 # plays note 60 with loads of reverb\nsleep 2\nend\"\n\"\n# Repeat the block 16 times internally\nwith_fx :reverb, reps: 16 do\nplay (scale :e3, :minor_pentatonic), release: 0.1\nsleep 0.125\nend\n# The above is a shorthand for this:\nwith_fx :reverb do\n16.times do\nplay (scale :e3, :minor_pentatonic), release: 0.1\nsleep 0.125\nend\nend\n",
    "summary": "Use Studio FX"
  },
  "with_merged_sample_defaults": {
    "doc": "Specify new default values to be used by all subsequent calls to `sample` within the `do`/`end` block.  Merges the specified values with any previous sample defaults, rather than replacing them. After the `do`/`end` block has completed, the previous sampled defaults (if any) are restored.",
    "examples": "sample :loop_amen # plays amen break with default arguments\nuse_merged_sample_defaults amp: 0.5, cutoff: 70\nsample :loop_amen # plays amen break with an amp of 0.5, cutoff of 70 and defaults for rest of args\nwith_merged_sample_defaults cutoff: 90 do\nsample :loop_amen  # plays amen break with a cutoff of 90 and amp of 0.5\nend\nsample :loop_amen  # plays amen break with a cutoff of 70 and amp is 0.5 again as the previous defaults are restored.",
    "summary": "Block-level use merged sample defaults"
  },
  "with_merged_synth_defaults": {
    "doc": "Specify synth arg values to be used by any following call to play within the specified `do`/`end` block. Merges the specified values with any previous synth defaults, rather than replacing them. After the `do`/`end` block has completed, previous defaults (if any) are restored.",
    "examples": "with_merged_synth_defaults amp: 0.5, pan: 1 do\nplay 50 # => plays note 50 with amp 0.5 and pan 1\nend\"\n\"play 50 #=> plays note 50\nwith_merged_synth_defaults amp: 0.5 do\nplay 50 #=> plays note 50 with amp 0.5\nwith_merged_synth_defaults pan: -1 do\nwith_merged_synth_defaults amp: 0.7 do\nplay 50 #=> plays note 50 with amp 0.7 and pan -1\nend\nend\nplay 50 #=> plays note 50 with amp 0.5\nend",
    "summary": "Block-level merge synth defaults"
  },
  "with_octave": {
    "doc": "Transposes your music by shifting all notes played by the specified number of octaves within the specified block. To shift up by an octave use a transpose of 1. To shift down use negative numbers. For transposing the notes within the octave range see `with_transpose`.",
    "examples": "play 50 # Plays note 50\nsleep 1\nwith_octave 1 do\nplay 50 # Plays note 62\nend\nsleep 1\nplay 50 # Plays note 50",
    "summary": "Block level octave transposition"
  },
  "with_sample_bpm": {
    "doc": "Block-scoped modification of bpm so that sleeping for 1 will sleep for the duration of the sample.",
    "examples": "live_loop :dnb do\nwith_sample_bpm :loop_amen do #Set bpm based on :loop_amen duration\nsample :bass_dnb_f\nsample :loop_amen\nsleep 1                     #`sleep`ing for 1 sleeps for duration of :loop_amen\nend\nend\"\n\"live_loop :dnb do\nwith_sample_bpm :loop_amen, num_beats: 4 do # Set bpm based on :loop_amen duration\n# but also specify that the sample duration\n# is actually 4 beats long.\nsample :bass_dnb_f\nsample :loop_amen\nsleep 4                     #`sleep`ing for 4 sleeps for duration of :loop_amen\n# as we specified that the sample consisted of\n# 4 beats\nend\nend",
    "summary": "Block-scoped sample-duration-based bpm modification"
  },
  "with_sample_defaults": {
    "doc": "Specify new default values to be used by all subsequent calls to `sample` within the `do`/`end` block. After the `do`/`end` block has completed, the previous sampled defaults (if any) are restored. For the contents of the block, will remove and override any previous defaults.",
    "examples": "sample :loop_amen # plays amen break with default arguments\nuse_sample_defaults amp: 0.5, cutoff: 70\nsample :loop_amen # plays amen break with an amp of 0.5, cutoff of 70 and defaults for rest of args\nwith_sample_defaults cutoff: 90 do\nsample :loop_amen  # plays amen break with a cutoff of 90 and defaults for rest of args - note that amp is no longer 0.5\nend\nsample :loop_amen  # plays amen break with a cutoff of 70 and amp is 0.5 again as the previous defaults are restored.",
    "summary": "Block-level use new sample defaults"
  },
  "with_synth": {
    "doc": "Switch the current synth to `synth_name` but only for the duration of the `do`/`end` block. After the `do`/`end` block has completed, the previous synth is restored.",
    "examples": "play 50 # Plays with default synth\nsleep 2\nuse_synth :supersaw\nplay 50 # Plays with supersaw synth\nsleep 2\nwith_synth :saw_beep do\nplay 50 # Plays with saw_beep synth\nend\nsleep 2\n# Previous synth is restored\nplay 50 # Plays with supersaw synth\n",
    "summary": "Block-level synth switching"
  },
  "with_synth_defaults": {
    "doc": "Specify new default values to be used by all calls to `play` within the `do`/`end` block. After the `do`/`end` block has completed the previous synth defaults (if any) are restored.",
    "examples": "play 50 # plays note 50 with default arguments\nuse_synth_defaults amp: 0.5, pan: -1\nplay 50 # plays note 50 with an amp of 0.5, pan of -1 and defaults for rest of args\nwith_synth_defaults amp: 0.6, cutoff: 80 do\nplay 50 # plays note 50 with an amp of 0.6, cutoff of 80 and defaults for rest of args (including pan)\nend\nplay 60 # plays note 60 with an amp of 0.5, pan of -1 and defaults for rest of args\n",
    "summary": "Block-level use new synth defaults"
  },
  "with_timing_guarantees": {
    "doc": "For the given block, if set to true, synths will not trigger if it is too late. If false, some synth triggers may be late. After the block has completed, the previous value is restored.",
    "examples": "with_timing_guarantees true\nsample :loop_amen  #=> if time is behind by any margin, this will not trigger\nend\"\n\"\nwith_timing_guarantees false\nsample :loop_amen  #=> unless time is too far behind, this will trigger even when late.\nend",
    "summary": "Block-scoped inhibition of synth triggers if too late"
  },
  "with_transpose": {
    "doc": "Similar to use_transpose except only applies to code within supplied `do`/`end` block. Previous transpose value is restored after block. To transpose entire octaves see `with_octave`.",
    "examples": "use_transpose 3\nplay 62 # Plays note 65\nwith_transpose 12 do\nplay 50 # Plays note 62\nsleep 1\nplay 72 # Plays note 84\nend\n# Original transpose value is restored\nplay 80 # Plays note 83\n",
    "summary": "Block-level note transposition"
  },
  "with_tuning": {
    "doc": "Similar to use_tuning except only applies to code within supplied `do`/`end` block. Previous tuning value is restored after block.",
    "examples": "use_tuning :equal, :c\nplay :e4 # Plays note 64\nwith_tuning :just, :c do\nplay :e4 # Plays note 63.8631\nsleep 1\nplay :c4 # Plays note 60\nend\n# Original tuning value is restored\nplay :e4 # Plays note 64",
    "summary": "Block-level tuning modification"
  }
}
#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/

opts_doc = {
  "amp": "Amplitude of playback.",
  "amp_slide": "The duration in beats for amplitude changes to take place",
  "attack": "Time to reach full volume. Default is 0.",
  "attack_level": "Amplitude level reached after attack phase and immediately before decay phase",
  "beat_stretch": "Stretch (or shrink) the sample to last for exactly the specified number of beats. Please note - this does *not* keep the pitch constant and is essentially the same as modifying the rate directly.",
  "clamp_time": "Time taken for the amplitude adjustments to kick in fully (in seconds). This is usually pretty small (not much more than 10 milliseconds). Also known as the time of the attack phase. Only valid if the compressor is enabled by turning on the `compress:` opt.",
  "compress": "Enable the compressor. This sits at the end of the internal FX chain immediately before the `amp:` opt. Therefore to drive the compressor use the `pre_amp:` opt which will amplify the signal before it hits any internal FX. The compressor compresses the dynamic range of the incoming signal. Equivalent to automatically turning the amp down when the signal gets too loud and then back up again when it's quiet. Useful for ensuring the containing signal doesn't overwhelm other aspects of the sound. Also a general purpose hard-knee dynamic range processor which can be tuned via the opts to both expand and compress the signal.",
  "decay": "Duration of the decay phase of the envelope.",
  "decay_level": "Amplitude level reached after decay phase and immediately before sustain phase. Defaults to sustain_level unless explicitly set",
  "env_curve": "Select the shape of the curve between levels in the envelope. 1=linear, 2=exponential, 3=sine, 4=welch, 6=squared, 7=cubed",
  "finish": "Position in sample as a fraction between 0 and 1 to end playback. Default is 1.",
  "hpf": "Cutoff value of the built-in high pass filter (hpf) in MIDI notes. Unless specified, the hpf is *not* added to the signal chain.",
  "hpf_attack": "Attack time for hpf cutoff filter. Amount of time (in beats) for sound to reach full cutoff value. Default value is set to match amp envelope's attack value.",
  "hpf_attack_level": "The peak hpf cutoff (value of cutoff at peak of attack) as a MIDI note. Default value is to match the `hpf_decay_level:` opt.",
  "hpf_bypass": "Bypass the global hpf. 0=no bypass, 1=bypass. Default 0.",
  "hpf_decay": "Decay time for hpf cutoff filter. Amount of time (in beats) for sound to move from full cutoff value (cutoff attack level) to the cutoff sustain level. Default value is set to match amp envelope's decay value.",
  "hpf_decay_level": "The level of hpf cutoff after the decay phase as a MIDI note. Default value is to match the `hpf_sustain_level:` opt.",
  "hpf_env_curve": "Select the shape of the curve between levels in the hpf cutoff envelope. 1=linear, 2=exponential, 3=sine, 4=welch, 6=squared, 7=cubed.",
  "hpf_init_level": "The initial high pass filter envelope value as a MIDI note. This envelope is bypassed if no hpf env opts are specified. Default value is set to 130.",
  "hpf_max": "Maximum value of the high pass filter envelope. Default is 200.",
  "hpf_release": "Amount of time (in beats) for sound to move from hpf cutoff sustain value to hpf cutoff min value. Default value is set to match amp envelope's release value.",
  "hpf_release_level": "The sustain hpf cutoff (value of hpf cutoff at sustain time) as a MIDI note. Default value is to match the `hpf:` opt.",
  "hpf_sustain": "Amount of time for hpf cutoff value to remain at sustain level in beats. When -1 (the default) will auto-stretch.",
  "hpf_sustain_level": "The sustain cutoff (value of hpf cutoff at sustain time) as a MIDI note. Default value is to match the `hpf_release_level:` opt.",
  "invert": "Apply the specified num inversions to chord. See the fn `chord_invert`.",
  "kill_delay": "Amount of time to wait after all synths triggered by the block have completed before stopping and freeing the effect synthesiser.",
  "leak_dc_bypass": "Bypass the final DC leak correction FX. 0=no bypass, 1=bypass. Default 0.",
  "limiter_bypass": "Bypass the final limiter. 0=no bypass, 1=bypass. Default 0.",
  "lpf": "Cutoff value of the built-in low pass filter (lpf) in MIDI notes. Unless specified, the lpf is *not* added to the signal chain.",
  "lpf_attack": "Attack time for lpf cutoff filter. Amount of time (in beats) for sound to reach full cutoff value. Default value is set to match amp envelope's attack value.",
  "lpf_attack_level": "The peak lpf cutoff (value of cutoff at peak of attack) as a MIDI note. Default value is to match the `lpf_decay_level:` opt.",
  "lpf_bypass": "Bypass the global lpf. 0=no bypass, 1=bypass. Default 0.",
  "lpf_decay": "Decay time for lpf cutoff filter. Amount of time (in beats) for sound to move from full cutoff value (cutoff attack level) to the cutoff sustain level. Default value is set to match amp envelope's decay value.",
  "lpf_decay_level": "The level of lpf cutoff after the decay phase as a MIDI note. Default value is to match the `lpf_sustain_level:` opt.",
  "lpf_env_curve": "Select the shape of the curve between levels in the lpf cutoff envelope. 1=linear, 2=exponential, 3=sine, 4=welch, 6=squared, 7=cubed.",
  "lpf_init_level": "The initial low pass filter envelope value as a MIDI note. This envelope is bypassed if no lpf env opts are specified. Default value is to match the `lpf_min:` opt.",
  "lpf_min": "Starting value of the lpf cutoff envelope. Default is 30.",
  "lpf_release": "Amount of time (in beats) for sound to move from lpf cutoff sustain value to lpf cutoff min value. Default value is set to match amp envelope's release value.",
  "lpf_release_level": "The final value of the low pass filter envelope as a MIDI note. This envelope is bypassed if no lpf env opts are specified. Default value is to match the `lpf:` opt.",
  "lpf_sustain": "Amount of time for lpf cutoff value to remain at sustain level in beats. When -1 (the default) will auto-stretch.",
  "lpf_sustain_level": "The sustain cutoff (value of lpf cutoff at sustain time) as a MIDI note. Default value is to match the `lpf_release_level:` opt.",
  "norm": "Normalise the audio (make quieter parts of the sample louder and louder parts quieter) - this is similar to the normaliser FX. This may emphasise any clicks caused by clipping.",
  "num_beats": "The number of beats within the sample. By default this is 1.",
  "num_octaves": "Create an arpeggio of the chord over n octaves",
  "octave": "The octave of the note. Overrides any octave declaration in the note symbol such as :c2. Default is 4",
  "on": "If specified and false/nil/0 will stop the synth from being played. Ensures all opts are evaluated.",
  "onset": "Analyse the sample with an onset detection algorithm and set the `start:` and `finish:` opts to play the nth onset only. Allows you to treat a rhythm sample as a palette of individual drum/synth hits",
  "pan": "Stereo position of audio. -1 is left ear only, 1 is right ear only, and values in between position the sound accordingly. Default is 0.",
  "pan_slide": "The duration in beats for the pan value to change",
  "path": "Path of the sample to play. Typically this opt is rarely used instead of the more powerful source/filter system. However it can be useful when working with pre-made opt maps.",
  "pitch": "Pitch adjustment in semitones. 1 is up a semitone, 12 is up an octave, -12 is down an octave etc. Maximum upper limit of 24 (up 2 octaves). Lower limit of -72 (down 6 octaves). Decimal numbers can be used for fine tuning.",
  "pitch_dis": "Pitch shift-specific opt - only honoured if the `pitch:` opt is used. Pitch dispersion - how much random variation in pitch to add. Using a low value like 0.001 can help to \\\"soften up\\\" the metallic sounds, especially on drum loops. To be really technical, pitch_dispersion is the maximum random deviation of the pitch from the pitch ratio (which is set by the `pitch:` opt).",
  "pitch_stretch": "Stretch (or shrink) the sample to last for exactly the specified number of beats. This attempts to keep the pitch constant using the `pitch:` opt. Note, it's very likely you'll need to experiment with the `window_size:`, `pitch_dis:` and `time_dis:` opts depending on the sample and the amount you'd like to stretch/shrink from original size.",
  "pitches": "An array of notes (symbols or ints) to filter on. Octave information is ignored.",
  "pre_amp": "Amplitude multiplier which takes place immediately before any internal FX such as the low pass filter, compressor or pitch modification. Use this opt if you want to overload the compressor.",
  "rate": "Rate with which to play back the sample. Higher rates mean an increase in pitch and a decrease in duration. Default is 1.",
  "relax_time": "Time taken for the amplitude adjustments to be released. Usually a little longer than clamp_time. If both times are too short, you can get some (possibly unwanted) artefacts. Also known as the time of the release phase. Only valid if the compressor is enabled by turning on the `compress:` opt.",
  "release": "Time (from the end of the sample) to go from full amplitude to 0. Default is 0.",
  "reps": "Number of times to repeat the block in an iteration.",
  "rpitch": "Rate modified pitch. Multiplies the rate by the appropriate ratio to shift up or down the specified amount in MIDI notes. Please note - this does *not* keep the duration and rhythmical rate constant and is essentially the same as modifying the rate directly.",
  "slide": "Default slide time in beats for all slide opts. Individually specified slide opts will override this value.",
  "slope_above": "Slope of the amplitude curve above the threshold. A value of 1 means that the output of signals with amplitude above the threshold will be unaffected. Greater values will magnify and smaller values will attenuate the signal. Only valid if the compressor is enabled by turning on the `compress:` opt.",
  "slope_below": "Slope of the amplitude curve below the threshold. A value of 1 means that the output of signals with amplitude below the threshold will be unaffected. Greater values will magnify and smaller values will attenuate the signal. Only valid if the compressor is enabled by turning on the `compress:` opt.",
  "start": "Position in sample as a fraction between 0 and 1 to start playback. Default is 0.",
  "sustain": "Time to stay at full volume. Default is to stretch to length of sample (minus attack and release times).",
  "sustain_level": "Amplitude level reached after decay phase and immediately before release phase.",
  "threshold": "Threshold value determining the break point between slope_below and slope_above. Only valid if the compressor is enabled by turning on the `compress:` opt.",
  "time_dis": "Pitch shift-specific opt - only honoured if the `pitch:` opt is used. Time dispersion - how much random delay before playing each grain (measured in seconds). Again, low values here like 0.001 can help to soften up metallic sounds introduced by the effect. Large values are also fun as they can make soundscapes and textures from the input, although you will most likely lose the rhythm of the original. NB - This won't have an effect if it's larger than window_size.",
  "window_size": "Pitch shift-specific opt - only honoured if the `pitch:` opt is used. Pitch shift works by chopping the input into tiny slices, then playing these slices at a higher or lower rate. If we make the slices small enough and overlap them, it sounds like the original sound with the pitch changed. The window_size is the length of the slices and is measured in seconds. It needs to be around 0.2 (200ms) or greater for pitched sounds like guitar or bass, and needs to be around 0.02 (20ms) or lower for percussive sounds like drum loops. You can experiment with this to get the best sound for your input."
}
