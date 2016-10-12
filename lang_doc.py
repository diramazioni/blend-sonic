null = None
#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/

funct_doc = {
  "all_sample_names": {
    "doc": "Return a list of all the sample names available",
    "examples": "",
    "summary": "Get all sample names"
  },
  "chord": {
    "doc": "Creates an immutable ring of Midi note numbers when given a tonic note and a chord type. If only passed a chord type, will default the tonic to 0. See examples.",
    "examples": "\nputs (chord :e, :minor) # returns a ring of midi notes - (ring 64, 67, 71)\n\n# Play all the notes together\nplay (chord :e, :minor)\n\n# Chord inversions (see the fn chord_invert)\nplay (chord :e3, :minor, invert: 0) # Play the basic :e3, :minor chord - (ring 52, 55, 59)\nplay (chord :e3, :minor, invert: 1) # Play the first inversion of :e3, :minor - (ring 55, 59, 64)\nplay (chord :e3, :minor, invert: 2) # Play the first inversion of :e3, :minor - (ring 59, 64, 67)\n\n\n# You can create a chord without a tonic:\nputs (chord :minor) #=> (ring 0, 3, 7)\n\n# chords are great for arpeggiators\nlive_loop :arp do\nplay chord(:e, :minor, num_octaves: 2).tick, release: 0.1\nsleep 0.125\nend\n# Sonic Pi supports a large range of chords\n# Notice that the more exotic ones have to be surrounded by ' quotes\n(chord :C, '1')\n(chord :C, '5')\n(chord :C, '+5')\n(chord :C, 'm+5')\n(chord :C, :sus2)\n(chord :C, :sus4)\n(chord :C, '6')\n(chord :C, :m6)\n(chord :C, '7sus2')\n(chord :C, '7sus4')\n(chord :C, '7-5')\n(chord :C, 'm7-5')\n(chord :C, '7+5')\n(chord :C, 'm7+5')\n(chord :C, '9')\n(chord :C, :m9)\n(chord :C, 'm7+9')\n(chord :C, :maj9)\n(chord :C, '9sus4')\n(chord :C, '6*9')\n(chord :C, 'm6*9')\n(chord :C, '7-9')\n(chord :C, 'm7-9')\n(chord :C, '7-10')\n(chord :C, '9+5')\n(chord :C, 'm9+5')\n(chord :C, '7+5-9')\n(chord :C, 'm7+5-9')\n(chord :C, '11')\n(chord :C, :m11)\n(chord :C, :maj11)\n(chord :C, '11+')\n(chord :C, 'm11+')\n(chord :C, '13')\n(chord :C, :m13)\n(chord :C, :add2)\n(chord :C, :add4)\n(chord :C, :add9)\n(chord :C, :add11)\n(chord :C, :add13)\n(chord :C, :madd2)\n(chord :C, :madd4)\n(chord :C, :madd9)\n(chord :C, :madd11)\n(chord :C, :madd13)\n(chord :C, :major)\n(chord :C, :M)\n(chord :C, :minor)\n(chord :C, :m)\n(chord :C, :major7)\n(chord :C, :dom7)\n(chord :C, '7')\n(chord :C, :M7)\n(chord :C, :minor7)\n(chord :C, :m7)\n(chord :C, :augmented)\n(chord :C, :a)\n(chord :C, :diminished)\n(chord :C, :dim)\n(chord :C, :i)\n(chord :C, :diminished7)\n(chord :C, :dim7)\n(chord :C, :i7)",
    "summary": "Create chord"
  },
  "chord_degree": {
    "doc": "In music we build chords from scales. For example, a C major chord is made by taking the 1st, 3rd and 5th notes of the C major scale (C, E and G). If you do this on a piano you might notice that you play one, skip one, play one, skip one etc. If we use the same spacing and start from the second note in C major (which is a D), we get a D minor chord which is the 2nd, 4th and 6th notes in C major (D, F and A). We can move this pattern all the way up or down the scale to get different types of chords. `chord_degree` is a helper method that returns a ring of midi note numbers when given a degree (starting point in a scale) which is a symbol `:i`, `:ii`, `:iii`, `:iv`, `:v`, `:vi`, `:vii` or a number `1`-`7`. The second argument is the tonic note of the scale, the third argument is the scale type and finally the fourth argument is number of notes to stack up in the chord. If we choose 4 notes from degree `:i` of the C major scale, we take the 1st, 3rd, 5th and 7th notes of the scale to get a C major 7 chord.",
    "examples": "\"puts (chord_degree :i, :A3, :major) # returns a ring of midi notes - (ring 57, 61, 64, 68) - an A major 7 chord\nplay (chord_degree :i, :A3, :major, 3)\nplay (chord_degree :ii, :A3, :major, 3) # Chord ii in A major is a B minor chord\nplay (chord_degree :iii, :A3, :major, 3) # Chord iii in A major is a C# minor chord\nplay (chord_degree :iv, :A3, :major, 3) # Chord iv in A major is a D major chord\nplay (chord_degree :i, :C4, :major, 4) # Taking four notes is the default. This gives us 7th chords - here it plays a C major 7\nplay (chord_degree :i, :C4, :major, 5) # Taking five notes gives us 9th chords - here it plays a C major 9 chord",
    "summary": "Construct chords of stacked thirds, based on scale degrees"
  },
  "chord_invert": {
    "doc": "Given a set of notes, apply a number of inversions indicated by the `shift` parameter. Inversions being an increase to notes if `shift` is positive or decreasing the notes if `shift` is negative.\n\nAn inversion is simply rotating the chord and shifting the wrapped notes up or down an octave. For example, consider the chord :e3, :minor - `(ring 52, 55, 59)`. When we invert it once, we rotate the notes around to `(ring 55, 59, 52)`. However, because note 52 is wrapped round, it's shifted up an octave (12 semitones) so the actual first inversion of the chord :e3, :minor is `(ring 55, 59, 52 + 12)` or `(ring 55, 59, 64)`.\n\nNote that it's also possible to directly invert chords on creation with the `invert:` opt - `(chord :e3, :minor, invert: 2)`",
    "examples": "\nplay (chord_invert (chord :A3, \\\"M\\\"), 0) #No inversion     - (ring 57, 61, 64)\nsleep 1\nplay (chord_invert (chord :A3, \\\"M\\\"), 1) #First inversion  - (ring 61, 64, 69)\nsleep 1\nplay (chord_invert (chord :A3, \\\"M\\\"), 2) #Second inversion - (ring 64, 69, 73)",
    "summary": "Chord inversion"
  },
  "chord_names": {
    "doc": "Returns a ring containing all chord names known to Sonic Pi",
    "examples": "",
    "summary": "All chord names"
  },
  "control": {
    "doc": "Control a running synth node by passing new parameters to it. A synth node represents a running synth and can be obtained by assigning the return value of a call to play or sample or by specifying a parameter to the do/end block of an FX. You may modify any of the parameters you can set when triggering the synth, sample or FX. See documentation for opt details. If the synth to control is a chord, then control will change all the notes of that chord group at once to a new target set of notes - see example. Also, you may use the on: opt to conditionally trigger the control - see the docs for the `synth` and `sample` fns for more information.\n\nIf no synth to control is specified, then the last synth triggered by the current (or parent) thread will be controlled - see example below.",
    "examples": "\n## Basic control\n\nmy_node = play 50, release: 5, cutoff: 60 # play note 50 with release of 5 and cutoff of 60. Assign return value to variable my_node\nsleep 1 # Sleep for a second\ncontrol my_node, cutoff: 70 # Now modify cutoff from 60 to 70, sound is still playing\nsleep 1 # Sleep for another second\ncontrol my_node, cutoff: 90 # Now modify cutoff from 70 to 90, sound is still playing\n\n## Combining control with slide opts allows you to create nice transitions.\n\ns = synth :prophet, note: :e1, cutoff: 70, cutoff_slide: 8, release: 8 # start synth and specify slide time for cutoff opt\ncontrol s, cutoff: 130 # Change the cutoff value with a control.\n# Cutoff will now slide over 8 beats from 70 to 130\n\n\n## Use a short slide time and many controls to create a sliding melody\n\nnotes = (scale :e3, :minor_pentatonic, num_octaves: 2).shuffle # get a random ordering of a scale\n\ns = synth :beep, note: :e3, sustain: 8, note_slide: 0.05 # Start our synth running with a long sustain and short note slide time\n64.times do\ncontrol s, note: notes.tick                            # Keep quickly changing the note by ticking through notes repeatedly\nsleep 0.125\nend\n\n\n\n## Controlling FX\n\nwith_fx :bitcrusher, sample_rate: 1000, sample_rate_slide: 8 do |bc| # Start FX but also use the handy || goalposts\n# to grab a handle on the running FX. We can call\n# our handle anything we want. Here we've called it bc\nsample :loop_garzul, rate: 1\ncontrol bc, sample_rate: 5000                                      # We can use our handle bc now just like we used s in the\n# previous example to modify the FX as it runs.\nend\n\n## Controlling chords\n\ncg = play (chord :e4, :minor), sustain: 2  # start a chord\nsleep 1\ncontrol cg, notes: (chord :c3, :major)     # transition to new chord.\n# Each note in the original chord is mapped onto\n# the equivalent in the new chord.\n\n\n## Sliding between chords\n\ncg = play (chord :e4, :minor), sustain: 4, note_slide: 3  # start a chord\nsleep 1\ncontrol cg, notes: (chord :c3, :major)                    # slide to new chord.\n# Each note in the original chord is mapped onto\n# the equivalent in the new chord.\n\n\n## Sliding from a larger to smaller chord\n\ncg = play (chord :e3, :m13), sustain: 4, note_slide: 3  # start a chord with 7 notes\nsleep 1\ncontrol cg, notes: (chord :c3, :major)                    # slide to new chord with fewer notes (3)\n# Each note in the original chord is mapped onto\n# the equivalent in the new chord using ring-like indexing.\n# This means that the 4th note in the original chord will\n# be mapped onto the 1st note in the second chord and so-on.\n\n\n## Sliding from a smaller to larger chord\ncg = play (chord :c3, :major), sustain: 4, note_slide: 3  # start a chord with 3 notes\nsleep 1\ncontrol cg, notes: (chord :e3, :m13)                     # slide to new chord with more notes (7)\n# Each note in the original chord is mapped onto\n# the equivalent in the new chord.\n# This means that the 4th note in the new chord\n# will not sound as there is no 4th note in the\n# original chord.\n\n\n\n## Changing the slide rate\n\ns = synth :prophet, note: :e1, release: 8, cutoff: 70, cutoff_slide: 8 # Start a synth playing with a long cutoff slide\nsleep 1                                                                # wait a beat\ncontrol s, cutoff: 130                                                 # change the cutoff so it starts sliding slowly\nsleep 3                                                                # wait for 3 beats\ncontrol s, cutoff_slide: 1                                             # Change the cutoff_slide - the cutoff now slides more quickly to 130\n# it will now take 1 beat to slide from its *current* value\n# (somewhere between 70 and 130) to 130\n\n\n\n## Controlling the last triggered synth\n\nsynth :prophet, note: :e1, release: 8                                  # Every time a synth is triggered, Sonic Pi automatically remembers the node\nsleep 1\n16.times do\ncontrol note: (octs :e1, 3).tick                                     # This means we don't need to use an explicit variable to control the synth\nsleep 0.125                                                          # we last triggered.\nend\n\n## Controlling multiple synths without variables\n\nsynth :beep, release: 4                  # Trigger a beep synth\nsleep 0.1\ncontrol note: :e5                        # Control last triggered synth (:beep)\nsleep 0.5\nsynth :dsaw, release: 4                  # Next, trigger a dsaw synth\nsleep 0.1\ncontrol note: :e4                        # Control last triggered synth (:dsaw)\n\n\n",
    "summary": "Control running synth"
  },
  "current_arg_checks": {
    "doc": "Returns the current arg checking setting (`true` or `false`).\n\nThis can be set via the fns `use_arg_checks` and `with_arg_checks`.",
    "examples": "",
    "summary": "Get current arg checking status"
  },
  "current_cent_tuning": {
    "doc": "Returns the cent shift value.\n\nThis can be set via the fns `use_cent_tuning` and `with_cent_tuning`.",
    "examples": "",
    "summary": "Get current cent shift"
  },
  "current_debug": {
    "doc": "Returns the current debug setting (`true` or `false`).\n\nThis can be set via the fns `use_debug` and `with_debug`.",
    "examples": "",
    "summary": "Get current debug status"
  },
  "current_octave": {
    "doc": "Returns the octave shift value.\n\nThis can be set via the fns `use_octave` and `with_octave`.",
    "examples": "",
    "summary": "Get current octave shift"
  },
  "current_sample_defaults": {
    "doc": "Returns the current sample defaults. This is a map of synth arg names to either values or functions.\n\nThis can be set via the fns `use_sample_defaults`, `with_sample_defaults`, `use_merged_sample_defaults` and `with_merged_sample_defaults`.",
    "examples": "\nuse_sample_defaults amp: 0.5, cutoff: 80\nsample :loop_amen # Plays amen break with amp 0.5 and cutoff 80",
    "summary": "Get current sample defaults"
  },
  "current_sched_ahead_time": {
    "doc": "Returns the current schedule ahead time.\n\nThis can be set via the fn `set_sched_ahead_time!`.",
    "examples": "\nset_sched_ahead_time! 0.5",
    "summary": "Get current sched ahead time"
  },
  "current_synth": {
    "doc": "Returns the current synth name.\n\nThis can be set via the fns `use_synth` and `with_synth`.",
    "examples": "",
    "summary": "Get current synth"
  },
  "current_synth_defaults": {
    "doc": "Returns the current synth defaults. This is a map of synth arg names to either values or functions.\n\nThis can be set via the fns `use_synth_defaults`, `with_synth_defaults`, `use_merged_synth_defaults` and `with_merged_synth_defaults`.",
    "examples": "\nuse_synth_defaults amp: 0.5, cutoff: 80\nplay 50 # Plays note 50 with amp 0.5 and cutoff 80",
    "summary": "Get current synth defaults"
  },
  "current_transpose": {
    "doc": "Returns the current transpose value.\n\nThis can be set via the fns `use_transpose` and `with_transpose`.",
    "examples": "",
    "summary": "Get current transposition"
  },
  "current_volume": {
    "doc": "Returns the current volume.\n\nThis can be set via the fn `set_volume!`.",
    "examples": "\nputs current_volume # Print out the current volume\nset_volume! 2",
    "summary": "Get current volume"
  },
  "degree": {
    "doc": "For a given scale and tonic it takes a symbol `:i`, `:ii`, `:iii`, `:iv`,`:v`, `:vi`, `:vii` or a number `1`-`7` and resolves it to a midi note.",
    "examples": "\nputs (scale :C, :major) # returns the following ring of MIDI note numbers: (ring 60, 62, 64, 65, 67, 69, 71, 72)\n# anywhere you can use a list or ring of notes, you can also use scale\nplay_pattern (scale :C, :major)\n# you can use the :num_octaves parameter to get more notes\nplay_pattern (scale :C, :major, num_octaves: 2)\n# Scales can start with any note:\nputs (scale 50, :minor) #=> (ring 50, 52, 53, 55, 57, 58, 60, 62)\nputs (scale 50.1, :minor) #=> (ring 50.1, 52.1, 53.1, 55.1, 57.1, 58.1, 60.1, 62.1)\nputs (scale :minor) #=> (ring 0, 2, 3, 5, 7, 8, 10, 12)\n\n\n# scales are also rings\nlive_loop :scale_player do\nplay (scale :Eb3, :super_locrian).tick, release: 0.1\nsleep 0.125\nend\n\n# scales starting with 0 are useful in combination with sample's rpitch:\nlive_loop :scaled_sample do\nsample :bass_trance_c, rpitch: (scale 0, :minor).tick\nsleep 1\nend\n\n\n# Sonic Pi supports a large range of scales:\n\n(scale :C, :diatonic)\n(scale :C, :ionian)\n(scale :C, :major)\n(scale :C, :dorian)\n(scale :C, :phrygian)\n(scale :C, :lydian)\n(scale :C, :mixolydian)\n(scale :C, :aeolian)\n(scale :C, :minor)\n(scale :C, :locrian)\n(scale :C, :hex_major6)\n(scale :C, :hex_dorian)\n(scale :C, :hex_phrygian)\n(scale :C, :hex_major7)\n(scale :C, :hex_sus)\n(scale :C, :hex_aeolian)\n(scale :C, :minor_pentatonic)\n(scale :C, :yu)\n(scale :C, :major_pentatonic)\n(scale :C, :gong)\n(scale :C, :egyptian)\n(scale :C, :shang)\n(scale :C, :jiao)\n(scale :C, :zhi)\n(scale :C, :ritusen)\n(scale :C, :whole_tone)\n(scale :C, :whole)\n(scale :C, :chromatic)\n(scale :C, :harmonic_minor)\n(scale :C, :melodic_minor_asc)\n(scale :C, :hungarian_minor)\n(scale :C, :octatonic)\n(scale :C, :messiaen1)\n(scale :C, :messiaen2)\n(scale :C, :messiaen3)\n(scale :C, :messiaen4)\n(scale :C, :messiaen5)\n(scale :C, :messiaen6)\n(scale :C, :messiaen7)\n(scale :C, :super_locrian)\n(scale :C, :hirajoshi)\n(scale :C, :kumoi)\n(scale :C, :neapolitan_major)\n(scale :C, :bartok)\n(scale :C, :bhairav)\n(scale :C, :locrian_major)\n(scale :C, :ahirbhairav)\n(scale :C, :enigmatic)\n(scale :C, :neapolitan_minor)\n(scale :C, :pelog)\n(scale :C, :augmented2)\n(scale :C, :scriabin)\n(scale :C, :harmonic_major)\n(scale :C, :melodic_minor_desc)\n(scale :C, :romanian_minor)\n(scale :C, :hindu)\n(scale :C, :iwato)\n(scale :C, :melodic_minor)\n(scale :C, :diminished2)\n(scale :C, :marva)\n(scale :C, :melodic_major)\n(scale :C, :indian)\n(scale :C, :spanish)\n(scale :C, :prometheus)\n(scale :C, :diminished)\n(scale :C, :todi)\n(scale :C, :leading_whole)\n(scale :C, :augmented)\n(scale :C, :purvi)\n(scale :C, :chinese)\n(scale :C, :lydian_minor)",
    "summary": "Convert a degree into a note"
  },
  "fx_names": {
    "doc": "Return a list of all the FX available",
    "examples": "",
    "summary": "Get all FX names"
  },
  "hz_to_midi": {
    "doc": "Convert a frequency in hz to a midi note. Note that the result isn't an integer and there is a potential for some very minor rounding errors.",
    "examples": "",
    "summary": "Hz to MIDI conversion"
  },
  "kill": {
    "doc": "Kill a running synth sound or sample. In order to kill a sound, you need to have stored a reference to it in a variable.",
    "examples": "\n# store a reference to a running synth in a variable called foo:\nfoo = play 50, release: 4\nsleep 1\n# foo is still playing, but we can kill it early:\nkill foo\n\nbar = sample :loop_amen\nsleep 0.5",
    "summary": "Kill synth"
  },
  "load_sample": {
    "doc": "Given a path to a `.wav`, `.wave`, `.aif`, `.aiff` or `.flac` file, pre-loads the sample into memory.\n\n+You may also specify the same set of source and filter pre-args available to `sample` itself. `load_sample` will then load all matching samples. See `sample`'s docs for more information.",
    "examples": "\nload_sample :elec_blip # :elec_blip is now loaded and ready to play as a sample\nsample :elec_blip # No delay takes place when attempting to trigger it\n\n# Using source and filter pre-args\ndir = \\\"/path/to/sample/dir\\\nload_sample dir # loads first matching sample in \\\"/path/to/sample/dir\\\nload_sample dir, 1 # loads sample with index 1 in \\\"/path/to/sample/dir\\\nload_sample dir, :foo # loads sample with name \\\"foo\\\" in \\\"/path/to/sample/dir\\\nload_sample dir, \\\"quux\\\" # loads first sample with file name containing \\\"quux\\\" in \\\"/path/to/sample/dir\\",
    "summary": "Pre-load first matching sample"
  },
  "load_samples": {
    "doc": "Given a directory containing multiple `.wav`, `.wave`, `.aif`, `.aiff` or `.flac` files, pre-loads all the samples into memory.\n\nYou may also specify the same set of source and filter pre-args available to `sample` itself. `load_sample` will load all matching samples (not just the sample `sample` would play given the same opts) - see `sample`'s docs for more information.",
    "examples": "\nload_sample :elec_blip # :elec_blip is now loaded and ready to play as a sample\nsample :elec_blip # No delay takes place when attempting to trigger it\n\n# Using source and filter pre-args\ndir = \\\"/path/to/sample/dir\\\nload_sample dir # loads all samples in \\\"/path/to/sample/dir\\\nload_sample dir, 1 # loads sample with index 1 in \\\"/path/to/sample/dir\\\nload_sample dir, :foo # loads sample with name \\\"foo\\\" in \\\"/path/to/sample/dir\\\nload_sample dir, \\\"quux\\\" # loads all samples with file names containing \\\"quux\\\" in \\\"/path/to/sample/dir\\",
    "summary": "Pre-load all matching samples"
  },
  "load_synthdefs": {
    "doc": "Load all pre-compiled synth designs in the specified directory. The binary files containing synth designs need to have the extension `.scsyndef`. This is useful if you wish to use your own SuperCollider synthesiser designs within Sonic Pi.\n\n## Important notes\n\nYou may not trigger external synthdefs unless you enable the following GUI preference:\n\n```\nStudio -> Synths and FX -> Enable external synths and FX\n```\n\nAlso, if you wish your synth to work with Sonic Pi's automatic stereo sound infrastructure *you need to ensure your synth outputs a stereo signal* to an audio bus with an index specified by a synth arg named `out_bus`. For example, the following synth would work nicely:\n\n\n(\nSynthDef(\\\\piTest\n{|freq = 200, amp = 1, out_bus = 0 |\nOut.ar(out_bus\nSinOsc.ar([freq,freq],0,0.5)* Line.kr(1, 0, 5, amp, doneAction: 2))}\n).writeDefFile(\\\"/Users/sam/Desktop/\\\")\n)\n\n\n",
    "examples": "",
    "summary": "Load external synthdefs"
  },
  "midi_to_hz": {
    "doc": "Convert a midi note to hz",
    "examples": "",
    "summary": "MIDI to Hz conversion"
  },
  "note": {
    "doc": "Takes a midi note, a symbol (e.g. `:C`) or a string (e.g. `\\\"C\\\"`) and resolves it to a midi note. You can also pass an optional `octave:` parameter to get the midi note for a given octave. Please note - `octave:` param overrides any octave specified in a symbol i.e. `:c3`. If the note is `nil`, `:r` or `:rest`, then `nil` is returned (`nil` represents a rest)",
    "examples": "\n# These all return 60 which is the midi number for middle C (octave 4)\nputs note(60)\nputs note(:C)\nputs note(:C4)\nputs note('C')\n\n# returns 60 - octave param has no effect if we pass in a number\nputs note(60, octave: 2)\n\n# These all return 36 which is the midi number for C2 (two octaves below middle C)\nputs note(:C, octave: 2)\nputs note(:C4, octave: 2) # note the octave param overrides any octaves specified in a symbol\nputs note('C', octave: 2)",
    "summary": "Describe note"
  },
  "note_range": {
    "doc": "Produces a ring of all the notes between a low note and a high note. By default this is chromatic (all the notes) but can be filtered with a pitches: argument. This opens the door to arpeggiator style sequences and other useful patterns. If you try to specify only pitches which aren't in the range it will raise an error - you have been warned!\nexamples:       [\n(note_range :c4, :c5) # => (ring 60,61,62,63,64,65,66,67,68,69,70,71,72)\n(note_range :c4, :c5, pitches: (chord :c, :major)) # => (ring 60,64,67,72)\n(note_range :c4, :c6, pitches: (chord :c, :major)) # => (ring 60,64,67,72,76,79,84)\n(note_range :c4, :c5, pitches: (scale :c, :major)) # => (ring 60,62,64,65,67,69,71,72)\n(note_range :c4, :c5, pitches: [:c4, :g2]) # => (ring 60,67,72)\nlive_loop :arpeggiator do\n# try changing the chord\nplay (note_range :c4, :c5, pitches: (chord :c, :major)).tick\nsleep 0.125\nend\n\n\n\n\n\n\n\ndef note_info(n, *args)\nraise Exception.new(\"note_info argument must be a valid note. Got nil.\") if(n.nil?)\nargs_h = resolve_synth_opts_hash_or_array(args)\noctave = args_h[:octave\nSonicPi::Note.new(n, octave)\nend\ndoc name:          :note_info\nintroduced:    Version.new(2,0,0)\nsummary:       \"Get note info\nReturns an instance of `SonicPi::Note`. Please note - `octave:` param overrides any octave specified in a symbol i.e. `:c3`",
    "examples": "%Q{\nputs note_info(:C, octave: 2)",
    "summary": "Get a range of notes"
  },
  "octs": {
    "doc": "Create a ring of successive octaves starting at `start` for `num_octaves`.\nexamples:       [\n(octs 60, 2)  #=> (ring 60, 72)\n(octs :e3, 3) #=> (ring 52, 64, 76)\n\n\n\n\n\ndef sample_free(*paths)\npaths.each do |p|\np = [p] unless is_list_like?(p)\nfilts_and_sources, args_a = sample_split_filts_and_opts(p)\nresolve_sample_paths(filts_and_sources).each do |p|\nif sample_loaded?(p)\n@mod_sound_studio.free_sample([p])\n__info \"Freed sample: #{unify_tilde_dir(p).inspect}\nend\nend\nend\n\n\nend\ndoc name:           :sample_free\nintroduced:     Version.new(2,9,0)\nsummary:        \"Free a sample on the synth server",
    "examples": "\nsample :loop_amen # The Amen break is now loaded into memory and played\nsleep 2\nsample :loop_amen # The Amen break is not loaded but played from memory\nsleep 2\nsample_free :loop_amen # The Amen break is freed from memory\nsample :loop_amen # the Amen break is re-loaded and played\n\n\nputs sample_info(:loop_amen).to_i # This returns the buffer id of the sample i.e. 1\nputs sample_info(:loop_amen).to_i # The buffer id remains constant whilst the sample\n# is loaded in memory\nsample_free :loop_amen\nputs sample_info(:loop_amen).to_i # The Amen break is re-loaded and gets a *new* id.\n\nsample :loop_amen\nsample :ambi_lunar_land\nsleep 2\nsample_free :loop_amen, :ambi_lunar_land\nsample :loop_amen                        # re-loads and plays amen\nsample :ambi_lunar_land                  # re-loads and plays lunar land\n\n# Using source and filter pre-args\ndir = \\\"/path/to/sample/dir\\\nsample_free dir # frees any loaded samples in \\\"/path/to/sample/dir\\\nsample_free dir, 1 # frees sample with index 1 in \\\"/path/to/sample/dir\\\nsample_free dir, :foo # frees sample with name \\\"foo\\\" in \\\"/path/to/sample/dir\\",
    "summary": "Create a ring of octaves"
  },
  "pitch_to_ratio": {
    "doc": "Convert a midi note to a ratio which when applied to a frequency will scale the frequency by the number of semitones. Useful for changing the pitch of a sample by using it as a way of generating the rate.",
    "examples": "\npitch_to_ratio 12 #=> 2.0\npitch_to_ratio 1 #=> 1.05946\npitch_to_ratio -12 #=> 0.5\nsample :ambi_choir, rate: pitch_to_ratio(3) # Plays :ambi_choir 3 semitones above default.\n\n# Play a chromatic scale of semitones\n(range 0, 16).each do |n|                  # For each note in the range 0->16\nsample :ambi_choir, rate: pitch_to_ratio(n) # play :ambi_choir at the relative pitch\nsleep 0.5                                # and wait between notes\nend",
    "summary": "relative MIDI pitch to frequency ratio"
  },
  "play": {
    "doc": "Play note with current synth. Accepts a set of standard options which include control of an amplitude envelope with `attack:`, `decay:`, `sustain:` and `release:` phases. These phases are triggered in order, so the duration of the sound is attack + decay + sustain + release times. The duration of the sound does not affect any other notes. Code continues executing whilst the sound is playing through its envelope phases.\n\nAccepts optional args for modification of the synth being played. See each synth's documentation for synth-specific opts. See `use_synth` and `with_synth` for changing the current synth.\n\nIf note is `nil`, `:r` or `:rest`, play is ignored and treated as a rest. Also, if the `on:` opt is specified and returns `false`, or `nil` then play is similarly ignored and treated as a rest.\n\nNote that the default opts listed are only a guide to the most common opts across all the synths. Not all synths support all the default opts and each synth typically supports many more opts specific to that synth. For example, the `:tb303` synth supports 45 unique opts. For a full list of a synth's opts see its documentation in the Help system.\n",
    "examples": "\nplay 50 # Plays note 50 on the current synth\n\nplay 50, attack: 1 # Plays note 50 with a fade-in time of 1s\n\nplay 62, pan: -1, release: 3 # Play note 62 in the left ear with a fade-out time of 3s.\n\n# controlling a synth synchronously\ns = play :e3, release: 4\nsleep 1\ncontrol s, note: :e5\nsleep 0.5\nuse_synth :dsaw\nplay :e3   # This is triggered after 1.5s from start\n\n# Controlling a synth asynchronously\nplay :e3, release: 4 do |s|\nsleep 1                                               # This block is run in an implicit in_thread\ncontrol s, note: :e5                                  # and therefore is asynchronous\nend\n\nsleep 0.5\nuse_synth :dsaw",
    "summary": "Play current synth"
  },
  "play_chord": {
    "doc": "Play a list of notes at the same time.\n\nAccepts optional args for modification of the synth being played. See each synth's documentation for synth-specific opts. See `use_synth` and `with_synth` for changing the current synth.",
    "examples": "",
    "summary": "Play notes simultaneously"
  },
  "play_pattern": {
    "doc": "Play list of notes with the current synth one after another with a sleep of 1\n\nAccepts optional args for modification of the synth being played. See each synth's documentation for synth-specific opts. See use_synth and with_synth for changing the current synth.",
    "examples": "",
    "summary": "Play pattern of notes"
  },
  "play_pattern_timed": {
    "doc": "Play each note in a list of notes one after another with specified times between them. The notes should be a list of MIDI numbers, symbols such as :E4 or chords such as chord(:A3, :major) - identical to the first parameter of the play function. The times should be a list of times between the notes in beats.\n\nIf the list of times is smaller than the number of gaps between notes, the list is repeated again. If the list of times is longer than the number of gaps between notes, then some of the times are ignored. See examples for more detail.\n\nAccepts optional args for modification of the synth being played. See each synth's documentation for synth-specific opts. See `use_synth` and `with_synth` for changing the current synth.",
    "examples": "",
    "summary": "Play pattern of notes with specific times"
  },
  "ratio_to_pitch": {
    "doc": "Convert a frequency ratio to a midi note which when added to a note will transpose the note to match the frequency ratio.",
    "examples": "\nratio_to_pitch 2 #=> 12.0\nratio_to_pitch 0.5 #=> -12.0\n",
    "summary": "relative frequency ratio to MIDI pitch"
  },
  "recording_delete": {
    "doc": "The master mixer is the final mixer that all sound passes through. This fn resets it to its default set - undoing any changes made via set_mixer_control!",
    "examples": "\nset_mixer_control! lpf: 70 # LPF cutoff value of master mixer is now 70\nsample :loop_amen          # :loop_amen sample is played with low cutoff\nsleep 3\nreset_mixer!               # mixer is now reset to default values",
    "summary": "Reset master mixer"
  },
  "recording_save": {
    "doc": "Save previous recording to the specified location",
    "examples": "",
    "summary": "Save recording"
  },
  "recording_start": {
    "doc": "Start recording all sound to a `.wav` file stored in a temporary directory.",
    "examples": "",
    "summary": "Start recording"
  },
  "recording_stop": {
    "doc": "Stop current recording.",
    "examples": "",
    "summary": "Stop recording"
  },
  "rest?": {
    "doc": "Given a note or an args map, returns true if it represents a rest and false if otherwise",
    "examples": "\nuse_timing_guarantees true\n\nsample :loop_amen  #=> if time is behind by any margin, this will not trigger\n\nuse_timing_guarantees false\n",
    "summary": "Determine if note or args is a rest"
  },
  "sample_buffer": {
    "doc": "Alias for the `load_sample` method. Loads sample if necessary and returns buffer information.",
    "examples": "",
    "summary": "Get sample data"
  },
  "sample_free_all": {
    "doc": "Unloads all samples therefore freeing the memory and resources consumed. Subsequent calls to `sample` and friends will re-load the sample on the server.\nexamples:       [\nsample :loop_amen        # load and play :loop_amen\nsample :ambi_lunar_land  # load and play :ambi_lunar_land\nsleep 2\nsample_free_all\nsample :loop_amen        # re-loads and plays amen\"\n\n\n\n\ndef start_amp_monitor\n@mod_sound_studio.start_amp_monitor\nend\n\ndef current_amp\n@mod_sound_studio.amp\nend\n\ndef midi_notes(*args)\nargs = args.map {|a| note(a)}\nSonicPi::Core::RingVector.new(args)\nend\ndoc name:           :midi_notes\nintroduced:     Version.new(2,7,0)\nsummary:        \"Create a ring buffer of midi note numbers",
    "examples": "\n(midi_notes :d3, :d4, :d5) #=> (ring 50, 62, 74)\n(midi_notes :d3, 62,  nil) #=> (ring 50, 62, nil)",
    "summary": "Free all loaded samples on the synth server"
  },
  "sample_groups": {
    "doc": "Return a list of all the sample groups available",
    "examples": "",
    "summary": "Get all sample groups"
  },
  "sample_info": {
    "doc": "Alias for the `load_sample` method. Loads sample if necessary and returns sample information.",
    "examples": "",
    "summary": "Get sample information"
  },
  "sample_names": {
    "doc": "Return a ring of sample names for the specified group",
    "examples": "",
    "summary": "Get sample names"
  },
  "sample_paths": {
    "doc": "Accepts the same pre-args and opts as `sample` and returns a ring of matched sample paths.",
    "examples": "\nsample_paths \\\"/path/to/samples/\\\" #=> ring of all top-level samples in /path/to/samples\n\nsample_paths \\\"/path/to/samples/**\\\" #=> ring of all nested samples in /path/to/samples\n\nsample_paths \\\"/path/to/samples/\\\", \\\"foo\\\" #=> ring of all samples in /path/to/samples",
    "summary": "Sample Pack Filter Resolution"
  },
  "scale_names": {
    "doc": "Returns a ring containing all scale names known to Sonic Pi",
    "examples": "",
    "summary": "All scale names"
  },
  "set_cent_tuning!": {
    "doc": "Globally tune Sonic Pi to play with another external instrument.\n\nUniformly tunes your music by shifting all notes played by the specified number of cents. To shift up by a cent use a cent tuning of 1. To shift down use negative numbers. One semitone consists of 100 cents.\n\nSee `use_cent_tuning` for setting the cent tuning value locally for a specific thread or `live_loop`. This is a global value and will shift the tuning for *all* notes. It will also persist for the entire session.\n\nImportant note: the cent tuning set by `set_cent_tuning!` is independent of any thread-local cent tuning values set by `use_cent_tuning` or `with_cent_tuning`.",
    "examples": "\nplay 50 # Plays note 50\nset_cent_tuning! 1",
    "summary": "Global Cent tuning"
  },
  "set_control_delta!": {
    "doc": "Specify how many seconds between successive modifications (i.e. trigger then controls) of a specific node on a specific thread. Set larger if you are missing control messages sent extremely close together in time.",
    "examples": "\n\nset_control_delta! 0.1                 # Set control delta to 0.1\n\ns = play 70, release: 8, note_slide: 8 # Play a note and set the slide time\ncontrol s, note: 82                    # immediately start sliding note.\n# This control message might not be\n# correctly handled as it is sent at the\n# same virtual time as the trigger.\n# If you don't hear a slide, try increasing the",
    "summary": "Set control delta globally"
  },
  "set_mixer_control!": {
    "doc": "The master mixer is the final mixer that all sound passes through. This fn gives you control over the master mixer allowing you to manipulate all the sound playing through Sonic Pi at once. For example, you can sweep a lpf or hpf over the entire sound. You can reset the controls back to their defaults with `reset_mixer!`.",
    "examples": "",
    "summary": "Control master mixer"
  },
  "set_sched_ahead_time!": {
    "doc": "Specify how many seconds ahead of time the synths should be triggered. This represents the amount of time between pressing 'Run' and hearing audio. A larger time gives the system more room to work with and can reduce performance issues in playing fast sections on slower platforms. However, a larger time also increases latency between modifying code and hearing the result whilst live coding.",
    "examples": "",
    "summary": "Set sched ahead time globally"
  },
  "set_volume!": {
    "doc": "Set the main system volume to `vol`. Accepts a value between `0` and `5` inclusive. Vols greater or smaller than the allowed values are trimmed to keep them within range. Default is `1`.",
    "examples": "\nset_volume! 2 # Set the main system volume to 2\n\nset_volume! -1 # Out of range, so sets main system volume to 0\n\nset_volume! 7 # Out of range, so sets main system volume to 5",
    "summary": "Set Volume globally"
  },
  "status": {
    "doc": "This returns a Hash of information about the synthesis environment. Mostly used for debugging purposes.",
    "examples": "\nputs status # Returns something similar to:\n# {\n#   :ugens=>10\n#   :synths=>1\n#   :groups=>7\n#   :sdefs=>61\n#   :avg_cpu=>0.20156468451023102\n#   :peak_cpu=>0.36655542254447937\n#   :nom_samp_rate=>44100.0\n#   :act_samp_rate=>44099.9998411752\n#   :audio_busses=>2\n#   :control_busses=>0\n# }",
    "summary": "Get server status"
  },
  "synth": {
    "doc": "Trigger specified synth with given opts. Bypasses `current_synth` value, yet still honours `current_synth_defaults`. When using `synth`, the note is no longer an explicit argument but an opt with the key `note:`.\n\nIf note: opt is `nil`, `:r` or `:rest`, play is ignored and treated as a rest. Also, if the `on:` opt is specified and returns `false`, or `nil` then play is similarly ignored and treated as a rest.\n\nIf the synth name is `nil` behaviour is identical to that of `play` in that the `current_synth` will determine the actual synth triggered.\n\nIf a block is given, it is assumed to take one arg which will be the controllable synth node and the body of the block is run in an implicit `in_thread`. This allows for asynchronous control of the synth without interferring with time. For synchronous control capture the result of `synth` as a variable and use that.\n\nNote that the default opts listed are only a guide to the most common opts across all the synths. Not all synths support all the default opts and each synth typically supports many more opts specific to that synth. For example, the `:tb303` synth supports 45 unique opts. For a full list of a synth's opts see its documentation in the Help system. This can be accessed directly by clicking on the name of the synth and using the shortcut `C-i`",
    "examples": "\n\nuse_synth :beep            # Set current synth to :beep\nplay 60                    # Play note 60 with opt defaults\n\nsynth :dsaw, note: 60    # Bypass current synth and play :dsaw\n# with note 60 and opt defaults\n\nsynth :fm, note: 60, amp: 0.5 # Play note 60 of the :fm synth with an amplitude of 0.5\n\n\nuse_synth_defaults release: 5\nsynth :dsaw, note: 50 # Play note 50 of the :dsaw synth with a release of 5\n# You can play chords with the notes: opt:\nsynth :dsaw, notes: (chord :e3, :minor)\n\n# on: vs if\nnotes = (scale :e3, :minor_pentatonic, num_octaves: 2)\n\nlive_loop :rhyth do\n8.times do\ntrig = (spread 3, 7).tick(:rhyth)\nsynth :tri, on: trig, note: notes.tick, release: 0.1  # Here, we're calling notes.tick\n# every time we attempt to play the synth\n# so the notes rise faster than rhyth2\nsleep 0.125\nend\nend\n\n\nlive_loop :rhyth2 do\n8.times do\ntrig = (spread 3, 7).tick(:rhyth)\nsynth :saw, note: notes.tick, release: 0.1 if trig  # Here, we're calling notes.tick\n# only when the spread says to play\n# so the notes rise slower than rhyth\nsleep 0.125\nend\nend\n\n# controlling a synth synchronously\ns = synth :beep, note: :e3, release: 4\nsleep 1\ncontrol s, note: :e5\nsleep 0.5\nsynth :dsaw, note: :e3   # This is triggered after 1.5s from start\n\n# Controlling a synth asynchronously\nsynth :beep, note: :e3, release: 4 do |s|\nsleep 1                                               # This block is run in an implicit in_thread\ncontrol s, note: :e5                                  # and therefore is asynchronous\nend\n\nsleep 0.5\nsynth :dsaw, note: :e3 # This is triggered after 0.5s from start\n",
    "summary": "Trigger specific synth"
  },
  "synth_names": {
    "doc": "Return a list of all the synths available",
    "examples": "",
    "summary": "Get all synth names"
  },
  "use_arg_bpm_scaling": {
    "doc": "Turn synth argument bpm scaling on or off for the current thread. This is on by default. Note, using `rt` for args will result in incorrect times when used after turning arg bpm scaling off.",
    "examples": "\nuse_bpm 120\nplay 50, release: 2 # release is actually 1 due to bpm scaling\nsleep 2             # actually sleeps for 1 second\nuse_arg_bpm_scaling false\nplay 50, release: 2 # release is now 2\nsleep 2             # still sleeps for 1 second\n\n# Interaction with rt\nuse_bpm 120\nplay 50, release: rt(2) # release is 2 seconds\nsleep rt(2)             # sleeps for 2 seconds\nuse_arg_bpm_scaling false\nplay 50, release: rt(2) # ** Warning: release is NOT 2 seconds! **",
    "summary": "Enable and disable BPM scaling"
  },
  "use_arg_checks": {
    "doc": "When triggering synths, each argument is checked to see if it is sensible. When argument checking is enabled and an argument isn't sensible, you'll see an error in the debug pane. This setting allows you to explicitly enable and disable the checking mechanism. See with_arg_checks for enabling/disabling argument checking only for a specific `do`/`end` block.",
    "examples": "\nplay 50, release: 5 # Args are checked\nuse_arg_checks false",
    "summary": "Enable and disable arg checks"
  },
  "use_cent_tuning": {
    "doc": "Uniformly tunes your music by shifting all notes played by the specified number of cents. To shift up by a cent use a cent tuning of 1. To shift down use negative numbers. One semitone consists of 100 cents.\n\nSee `with_cent_tuning` for setting the cent tuning value only for a specific `do`/`end` block. To transpose entire semitones see `use_transpose`.",
    "examples": "\nplay 50 # Plays note 50\nuse_cent_tuning 1",
    "summary": "Cent tuning"
  },
  "use_debug": {
    "doc": "Enable or disable messages created on synth triggers. If this is set to false, the synths will be silent until debug is turned back on. Silencing debug messages can reduce output noise and also increase performance on slower platforms. See `with_debug` for setting the debug value only for a specific `do`/`end` block.",
    "examples": "",
    "summary": "Enable and disable debug"
  },
  "use_merged_sample_defaults": {
    "doc": "Specify new default values to be used by all subsequent calls to `sample`. Merges the specified values with any previous defaults, rather than replacing them.",
    "examples": "\nsample :loop_amen # plays amen break with default arguments\n\nuse_merged_sample_defaults amp: 0.5, cutoff: 70\n\nsample :loop_amen # plays amen break with an amp of 0.5, cutoff of 70 and defaults for rest of args\n\nuse_merged_sample_defaults cutoff: 90\n\nsample :loop_amen  # plays amen break with a cutoff of 90 and and an amp of 0.5 with defaults for rest of args",
    "summary": "Merge new sample defaults"
  },
  "use_merged_synth_defaults": {
    "doc": "Specify synth arg values to be used by any following call to play. Merges the specified values with any previous defaults, rather than replacing them.",
    "examples": "\nplay 50 #=> Plays note 50\n\nuse_merged_synth_defaults amp: 0.5\nplay 50 #=> Plays note 50 with amp 0.5\n\nuse_merged_synth_defaults cutoff: 80\nplay 50 #=> Plays note 50 with amp 0.5 and cutoff 80\n\nuse_merged_synth_defaults amp: 0.7\nplay 50 #=> Plays note 50 with amp 0.7 and cutoff 80\n\n\nuse_synth_defaults amp: 0.5, cutoff: 80, pan: -1\nuse_merged_synth_defaults amp: 0.7",
    "summary": "Merge synth defaults"
  },
  "use_octave": {
    "doc": "Transposes your music by shifting all notes played by the specified number of octaves. To shift up by an octave use a transpose of 1. To shift down use negative numbers. See `with_octave` for setting the octave shift only for a specific `do`/`end` block. For transposing the notes within the octave range see `use_transpose`.",
    "examples": "\nplay 50 # Plays note 50\nuse_octave 1\nplay 50 # Plays note 62\n\n\n# You may change the transposition multiple times:\nplay 62 # Plays note 62\nuse_octave -1\nplay 62 # Plays note 50\nuse_octave 2",
    "summary": "Note octave transposition"
  },
  "use_sample_bpm": {
    "doc": "Modify bpm so that sleeping for 1 will sleep for the duration of the sample.",
    "examples": "\"use_sample_bpm :loop_amen  #Set bpm based on :loop_amen duration\n\nlive_loop :dnb do\nsample :bass_dnb_f\nsample :loop_amen\nsleep 1                  #`sleep`ing for 1 actually sleeps for duration of :loop_amen\nend\n\nuse_sample_bpm :loop_amen, num_beats: 4  # Set bpm based on :loop_amen duration\n# but also specify that the sample duration\n# is actually 4 beats long.\n\nlive_loop :dnb do\nsample :bass_dnb_f\nsample :loop_amen\nsleep 4                  #`sleep`ing for 4 actually sleeps for duration of :loop_amen\n# as we specified that the sample consisted of\n# 4 beats",
    "summary": "Sample-duration-based bpm modification"
  },
  "use_sample_defaults": {
    "doc": "Specify new default values to be used by all subsequent calls to `sample`. Will remove and override any previous defaults.",
    "examples": "\nsample :loop_amen # plays amen break with default arguments\n\nuse_sample_defaults amp: 0.5, cutoff: 70\n\nsample :loop_amen # plays amen break with an amp of 0.5, cutoff of 70 and defaults for rest of args\n\nuse_sample_defaults cutoff: 90\n\nsample :loop_amen  # plays amen break with a cutoff of 90 and defaults for rest of args - note that amp is no longer 0.5",
    "summary": "Use new sample defaults"
  },
  "use_synth": {
    "doc": "Switch the current synth to `synth_name`. Affects all further calls to `play`. See `with_synth` for changing the current synth only for a specific `do`/`end` block.",
    "examples": "\nplay 50 # Plays with default synth\nuse_synth :mod_sine",
    "summary": "Switch current synth"
  },
  "use_synth_defaults": {
    "doc": "Specify new default values to be used by all subsequent calls to `play`. Will remove and override any previous defaults.",
    "examples": "\nplay 50 # plays note 50 with default arguments\n\nuse_synth_defaults amp: 0.5, cutoff: 70\n\nplay 50 # plays note 50 with an amp of 0.5, cutoff of 70 and defaults for rest of args\n\nuse_synth_defaults cutoff: 90\n\nplay 50 # plays note 50 with a cutoff of 90 and defaults for rest of args - note that amp is no longer 0.5",
    "summary": "Use new synth defaults"
  },
  "use_transpose": {
    "doc": "Transposes your music by shifting all notes played by the specified amount. To shift up by a semitone use a transpose of 1. To shift down use negative numbers. See `with_transpose` for setting the transpose value only for a specific `do`/`end` block. To transpose entire octaves see `use_octave`.",
    "examples": "\nplay 50 # Plays note 50\nuse_transpose 1\nplay 50 # Plays note 51\n\n\n# You may change the transposition multiple times:\nplay 62 # Plays note 62\nuse_transpose -12\nplay 62 # Plays note 50\nuse_transpose 3",
    "summary": "Note transposition"
  },
  "use_tuning": {
    "doc": "In most music we make semitones by dividing the octave into 12 equal parts, which is known as equal temperament. However there are lots of other ways to tune the 12 notes. This method adjusts each midi note into the specified tuning system. Because the ratios between notes aren't always equal, be careful to pick a centre note that is in the key of the music you're making for the best sound. Currently available tunings are `:just`, `:pythagorean`, `:meantone` and the default of `:equal`",
    "examples": "\nplay :e4 # Plays note 64\nuse_tuning :just, :c\nplay :e4 # Plays note 63.8631\n# transparently changes midi notes too\nplay 64 # Plays note 63.8631\n\n\n# You may change the tuning multiple times:\nplay 64 # Plays note 64\nuse_tuning :just\nplay 64 # Plays note 63.8631\nuse_tuning :equal",
    "summary": "Use alternative tuning systems"
  },
  "with_arg_bpm_scaling": {
    "doc": "Turn synth argument bpm scaling on or off for the supplied block. Note, using `rt` for args will result in incorrect times when used within this block.",
    "examples": "\"use_bpm 120\nplay 50, release: 2 # release is actually 1 due to bpm scaling\nwith_arg_bpm_scaling false do\nplay 50, release: 2 # release is now 2\nend\n\n# Interaction with rt\nuse_bpm 120\nplay 50, release: rt(2)   # release is 2 seconds\nsleep rt(2)               # sleeps for 2 seconds\nwith_arg_bpm_scaling false do\nplay 50, release: rt(2) # ** Warning: release is NOT 2 seconds! **\nsleep rt(2)             # still sleeps for 2 seconds",
    "summary": "Block-level enable and disable BPM scaling"
  },
  "with_arg_checks": {
    "doc": "Similar to `use_arg_checks` except only applies to code within supplied `do`/`end` block. Previous arg check value is restored after block.",
    "examples": "\n# Turn on arg checking:\nuse_arg_checks true\n\nplay 80, cutoff: 100 # Args are checked\n\nwith_arg_checks false do\n#Arg checking is now disabled\nplay 50, release: 3 # Args are not checked\nsleep 1\nplay 72             # Arg is not checked\nend\n\n# Arg checking is re-enabled\nplay 90 # Args are checked\n",
    "summary": "Block-level enable and disable arg checks"
  },
  "with_cent_tuning": {
    "doc": "Similar to `use_cent_tuning` except only applies cent shift to code within supplied `do`/`end` block. Previous cent tuning value is restored after block. One semitone consists of 100 cents. To transpose entire semitones see `with_transpose`.",
    "examples": "\nuse_cent_tuning 1\nplay 50 # Plays note 50.01\n\nwith_cent_tuning 2 do\nplay 50 # Plays note 50.02\nend\n\n# Original cent tuning value is restored\nplay 50 # Plays note 50.01\n",
    "summary": "Block-level cent tuning"
  },
  "with_debug": {
    "doc": "Similar to use_debug except only applies to code within supplied `do`/`end` block. Previous debug value is restored after block.",
    "examples": "\n# Turn on debugging:\nuse_debug true\n\nplay 80 # Debug message is sent\n\nwith_debug false do\n#Debug is now disabled\nplay 50 # Debug message is not sent\nsleep 1\nplay 72 # Debug message is not sent\nend\n\n# Debug is re-enabled\nplay 90 # Debug message is sent\n",
    "summary": "Block-level enable and disable debug"
  },
  "with_fx": {
    "doc": "This applies the named effect (FX) to everything within a given `do`/`end` block. Effects may take extra parameters to modify their behaviour. See FX help for parameter details.\n\nFor advanced control, it is also possible to modify the parameters of an effect within the body of the block. If you define the block with a single argument, the argument becomes a reference to the current effect and can be used to control its parameters (see examples).",
    "examples": "\n# Basic usage\nwith_fx :distortion do # Use the distortion effect with default parameters\nplay 50 # => plays note 50 with distortion\nsleep 1\nsample :loop_amen # => plays the loop_amen sample with distortion too\nend\n\n\n# Specify effect parameters\nwith_fx :level, amp: 0.3 do # Use the level effect with the amp parameter set to 0.3\nplay 50\nsleep 1\nsample :loop_amen\nend\n\n\n# Controlling the effect parameters within the block\nwith_fx :reverb, mix: 0.1 do |fx|\n# here we set the reverb level quite low to start with (0.1)\n# and we can change it later by using the 'fx' reference we've set up\n\nplay 60 # plays note 60 with a little bit of reverb\nsleep 2\n\ncontrol fx, mix: 0.5 # change the parameters of the effect to add more reverb\nplay 60 # again note 60 but with more reverb\nsleep 2\n\ncontrol fx, mix: 1 # change the parameters of the effect to add more reverb\nplay 60 # plays note 60 with loads of reverb\nsleep 2\nend\n\n\n# Repeat the block 16 times internally\nwith_fx :reverb, reps: 16 do\nplay (scale :e3, :minor_pentatonic), release: 0.1\nsleep 0.125\nend\n\n# The above is a shorthand for this:\nwith_fx :reverb do\n16.times do\nplay (scale :e3, :minor_pentatonic), release: 0.1\nsleep 0.125\nend\nend\n",
    "summary": "Use Studio FX"
  },
  "with_merged_sample_defaults": {
    "doc": "Specify new default values to be used by all subsequent calls to `sample` within the `do`/`end` block.  Merges the specified values with any previous sample defaults, rather than replacing them. After the `do`/`end` block has completed, the previous sampled defaults (if any) are restored.",
    "examples": "\nsample :loop_amen # plays amen break with default arguments\n\nuse_merged_sample_defaults amp: 0.5, cutoff: 70\n\nsample :loop_amen # plays amen break with an amp of 0.5, cutoff of 70 and defaults for rest of args\n\nwith_merged_sample_defaults cutoff: 90 do\nsample :loop_amen  # plays amen break with a cutoff of 90 and amp of 0.5\nend\n",
    "summary": "Block-level use merged sample defaults"
  },
  "with_merged_synth_defaults": {
    "doc": "Specify synth arg values to be used by any following call to play within the specified `do`/`end` block. Merges the specified values with any previous synth defaults, rather than replacing them. After the `do`/`end` block has completed, previous defaults (if any) are restored.",
    "examples": "\nwith_merged_synth_defaults amp: 0.5, pan: 1 do\nplay 50 # => plays note 50 with amp 0.5 and pan 1\nend\n\nplay 50 #=> plays note 50\nwith_merged_synth_defaults amp: 0.5 do\nplay 50 #=> plays note 50 with amp 0.5\n\nwith_merged_synth_defaults pan: -1 do\nwith_merged_synth_defaults amp: 0.7 do\nplay 50 #=> plays note 50 with amp 0.7 and pan -1\nend\nend\nplay 50 #=> plays note 50 with amp 0.5",
    "summary": "Block-level merge synth defaults"
  },
  "with_octave": {
    "doc": "Transposes your music by shifting all notes played by the specified number of octaves within the specified block. To shift up by an octave use a transpose of 1. To shift down use negative numbers. For transposing the notes within the octave range see `with_transpose`.",
    "examples": "\nplay 50 # Plays note 50\nsleep 1\nwith_octave 1 do\nplay 50 # Plays note 62\nend\nsleep 1",
    "summary": "Block level octave transposition"
  },
  "with_sample_bpm": {
    "doc": "Block-scoped modification of bpm so that sleeping for 1 will sleep for the duration of the sample.",
    "examples": "\nlive_loop :dnb do\nwith_sample_bpm :loop_amen do #Set bpm based on :loop_amen duration\nsample :bass_dnb_f\nsample :loop_amen\nsleep 1                     #`sleep`ing for 1 sleeps for duration of :loop_amen\nend\nend\nlive_loop :dnb do\nwith_sample_bpm :loop_amen, num_beats: 4 do # Set bpm based on :loop_amen duration\n# but also specify that the sample duration\n# is actually 4 beats long.\nsample :bass_dnb_f\nsample :loop_amen\nsleep 4                     #`sleep`ing for 4 sleeps for duration of :loop_amen\n# as we specified that the sample consisted of\n# 4 beats\nend",
    "summary": "Block-scoped sample-duration-based bpm modification"
  },
  "with_sample_defaults": {
    "doc": "Specify new default values to be used by all subsequent calls to `sample` within the `do`/`end` block. After the `do`/`end` block has completed, the previous sampled defaults (if any) are restored. For the contents of the block, will remove and override any previous defaults.",
    "examples": "\nsample :loop_amen # plays amen break with default arguments\n\nuse_sample_defaults amp: 0.5, cutoff: 70\n\nsample :loop_amen # plays amen break with an amp of 0.5, cutoff of 70 and defaults for rest of args\n\nwith_sample_defaults cutoff: 90 do\nsample :loop_amen  # plays amen break with a cutoff of 90 and defaults for rest of args - note that amp is no longer 0.5\nend\n",
    "summary": "Block-level use new sample defaults"
  },
  "with_synth": {
    "doc": "Switch the current synth to `synth_name` but only for the duration of the `do`/`end` block. After the `do`/`end` block has completed, the previous synth is restored.",
    "examples": "\nplay 50 # Plays with default synth\nsleep 2\nuse_synth :supersaw\nplay 50 # Plays with supersaw synth\nsleep 2\nwith_synth :saw_beep do\nplay 50 # Plays with saw_beep synth\nend\nsleep 2\n# Previous synth is restored\nplay 50 # Plays with supersaw synth",
    "summary": "Block-level synth switching"
  },
  "with_synth_defaults": {
    "doc": "Specify new default values to be used by all calls to `play` within the `do`/`end` block. After the `do`/`end` block has completed the previous synth defaults (if any) are restored.",
    "examples": "\nplay 50 # plays note 50 with default arguments\n\nuse_synth_defaults amp: 0.5, pan: -1\n\nplay 50 # plays note 50 with an amp of 0.5, pan of -1 and defaults for rest of args\n\nwith_synth_defaults amp: 0.6, cutoff: 80 do\nplay 50 # plays note 50 with an amp of 0.6, cutoff of 80 and defaults for rest of args (including pan)\nend\n\nplay 60 # plays note 60 with an amp of 0.5, pan of -1 and defaults for rest of args",
    "summary": "Block-level use new synth defaults"
  },
  "with_timing_guarantees": {
    "doc": "For the given block, if set to true, synths will not trigger if it is too late. If false, some synth triggers may be late. After the block has completed, the previous value is restored.",
    "examples": "\nwith_timing_guarantees true\nsample :loop_amen  #=> if time is behind by any margin, this will not trigger\nend\n\nwith_timing_guarantees false\nsample :loop_amen  #=> unless time is too far behind, this will trigger even when late.",
    "summary": "Block-scoped inhibition of synth triggers if too late"
  },
  "with_transpose": {
    "doc": "Similar to use_transpose except only applies to code within supplied `do`/`end` block. Previous transpose value is restored after block. To transpose entire octaves see `with_octave`.",
    "examples": "\nuse_transpose 3\nplay 62 # Plays note 65\n\nwith_transpose 12 do\nplay 50 # Plays note 62\nsleep 1\nplay 72 # Plays note 84\nend\n\n# Original transpose value is restored\nplay 80 # Plays note 83\n",
    "summary": "Block-level note transposition"
  },
  "with_tuning": {
    "doc": "Similar to use_tuning except only applies to code within supplied `do`/`end` block. Previous tuning value is restored after block.",
    "examples": "\nuse_tuning :equal, :c\nplay :e4 # Plays note 64\nwith_tuning :just, :c do\nplay :e4 # Plays note 63.8631\nsleep 1\nplay :c4 # Plays note 60\nend\n# Original tuning value is restored",
    "summary": "Block-level tuning modification"
  }
}
#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/#\#/

opts_doc = {
  "amp": "The amplitude of the note",
  "amp_slide": "The duration in beats for amplitude changes to take place",
  "attack": "Amount of time (in beats) for sound to reach full amplitude (attack_level). A short attack (i.e. 0.01) makes the initial part of the sound very percussive like a sharp tap. A longer attack (i.e 1) fades the sound in gently.",
  "attack_level": "Amplitude level reached after attack phase and immediately before decay phase",
  "decay": "Amount of time (in beats) for the sound to move from full amplitude (attack_level) to the sustain amplitude (sustain_level).",
  "decay_level": "Amplitude level reached after decay phase and immediately before sustain phase. Defaults to sustain_level unless explicitly set",
  "env_curve": "Select the shape of the curve between levels in the envelope. 1=linear, 2=exponential, 3=sine, 4=welch, 6=squared, 7=cubed",
  "invert": "Apply the specified num inversions to chord. See the fn `chord_invert`.",
  "num_beats": "The number of beats within the sample. By default this is 1.",
  "num_octaves": "The number of octaves you'd like the scale to consist of. More octaves means a larger scale. Default is 1.",
  "octave": "The octave of the note. Overrides any octave declaration in the note symbol such as :c2. Default is 4",
  "on": "If specified and false/nil/0 will stop the synth from being played. Ensures all opts are evaluated.",
  "pan": "The stereo position of the sound. -1 is left, 0 is in the middle and 1 is on the right. You may use a value in between -1 and 1 such as 0.25",
  "pan_slide": "The duration in beats for the pan value to change",
  "pitch": "Pitch adjustment in semitones. 1 is up a semitone, 12 is up an octave, -12 is down an octave etc.  Decimal numbers can be used for fine tuning.",
  "pre_amp": "Controls the amplitude of the signal prior to the FX stage of the mixer (prior to lpf/hpf stages). Has slide opts. Default 1.",
  "release": "Amount of time (in beats) for sound to move from sustain level amplitude to silent. A short release (i.e. 0.01) makes the final part of the sound very percussive (potentially resulting in a click). A longer release (i.e 1) fades the sound out gently.",
  "reps": "Number of times to repeat the block in an iteration.",
  "slide": "Default slide time in beats for all slide opts. Individually specified slide opts will override this value",
  "sustain": "Amount of time (in beats) for sound to remain at sustain level amplitude. Longer sustain values result in longer sounds. Full length of sound is attack + decay + sustain + release.",
  "sustain_level": "Amplitude level reached after decay phase and immediately before release phase."
}
