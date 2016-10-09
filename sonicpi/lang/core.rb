## encoding: utf-8
#--
# This file is part of Sonic Pi: http://sonic-pi.net
# Full project source: https://github.com/samaaron/sonic-pi
# License: https://github.com/samaaron/sonic-pi/blob/master/LICENSE.md
#
# Copyright 2013, 2014, 2015, 2016 by Sam Aaron (http://sam.aaron.name).
# All rights reserved.
#
# Permission is granted for use, copying, modification, and
# distribution of modified versions of this work as long as this
# notice is included.
#++
require_relative 'support/docsystem'
require_relative "../version"
require_relative "../util"
require 'active_support/inflector'

## TODO: create _* equivalents of all fns - for silent (i.e computation) versions

module SonicPi
  module Lang
    module Core

      include SonicPi::Lang::Support::DocSystem
      include SonicPi::Util

      class AssertionError < StandardError ; end

      THREAD_RAND_SEED_MAX = 10e20

      def run_file(path)
        path = File.expand_path(path.to_s)
        raise "Unable to run file - no file found with path: #{path}" unless File.exists?(path)
        __spider_eval(File.read(path))
      end
      doc name:           :run_file,
          introduced:     Version.new(2,11,0),
          summary:        "Evaluate the contents of the file as a new Run",
          args:           [[:filename, :path]],
          returns:        nil,
          opts:           nil,
          accepts_block:  false,
          doc:            "Reads the full contents of the file with `path` and executes it in a new Run. This works as if the code in the file was in a buffer and Run button was pressed.",
          examples: ["
run_file \"~/path/to/sonic-pi-code.rb\" #=> will run the contents of this file"]

      def run_code(code)
        __spider_eval(code.to_s)
      end
      doc name:           :run_code,
          introduced:     Version.new(2,11,0),
          summary:        "Evaluate the code passed as a String as a new Run",
          args:           [[:code, :string]],
          returns:        nil,
          opts:           nil,
          accepts_block:  false,
          doc:            "Executes the code passed as a string in a new Run. This works as if the code was in a buffer and Run button was pressed.",
          examples: ["
run_code \"sample :ambi_lunar_land\" #=> will play the :ambi_lunar_land sample",

        "# Works with any amount of code:
run_code \"8.times do\nplay 60\nsleep 1\nend # will play 60 8 times"]


      def use_osc(host_or_port, port=nil)
        if port
          host = host_or_port.to_s
        else
          host = "localhost"
          port = Integer(host_or_port)
        end
        __thread_locals.set :sonic_pi_osc_client, [host, port]
      end

      def osc(path, *args)
        host, port = __thread_locals.get :sonic_pi_osc_client
        raise "Set outgoing hostname and port for OSC messages with use_osc or with_osc" unless host && port
        begin
          @osc_server.send(host, port, path, *args)
          puts "OSC -> #{host}, #{port}, #{path}, #{args}"
        rescue Exception => e
          puts "Error sending OSC to #{host}, #{port}, #{path}, #{args.inspect}\n#{e.message}\n#{e.backtrace}"
        end
      end

      def reset

        __thread_locals.reset!
      end
      doc name:           :reset,
          introduced:     Version.new(2,11,0),
          summary:        "Reset all thread locals",
          args:           [[]],
          returns:        nil,
          opts:           nil,
          accepts_block:  false,
          doc:            "All settings such as the current synth, BPM, random stream and tick values will be reset to the values inherited from the parent thread. Consider using `clear` to reset all these values to their defaults.",
         examples: ["
# Basic Reset
use_synth :blade
use_octave 3

puts \"before\"         #=> \"before\"
puts current_synth      #=> :blade
puts current_octave     #=> 3
puts rand               #=> 0.75006103515625
puts tick               #=> 0

reset

puts \"after\"          #=> \"after\"
puts current_synth      #=> :beep
puts current_octave     #=> 0
puts rand               #=> 0.75006103515625
puts tick               #=> 0",

"Reset remembers defaults from when the thread was created:
use_synth :blade
use_octave 3

puts \"before\"         #=> \"before\"
puts current_synth      #=> :blade
puts current_octave     #=> 3
puts rand               #=> 0.75006103515625
puts tick               #=> 0

at do
  use_synth :tb303
  puts rand               #=> 0.9287109375
  reset
  puts \"thread\"          #=> \"thread\"


                          # The call to reset ensured that the current
                          # synth was returned to the the state at the
                          # time this thread was started. Thus any calls
                          # to use_synth between this line and the start
                          # of the thread are ignored
  puts current_synth      #=> :blade
  puts current_octave     #=> 3

                          # The call to reset ensured
                          # that the random stream was reset
                          # to the same state as it was when
                          # the current thread was started
  puts rand               #=> 0.9287109375
  puts tick               #=> 0
end"]

      def clear
        __thread_locals.clear!
      end
      doc name:           :clear,
          introduced:     Version.new(2,11,0),
          summary:        "Clear all thread locals to defaults",
          args:           [[]],
          returns:        nil,
          opts:           nil,
          accepts_block:  false,
      doc:            "All settings such as the current synth, BPM, random stream and tick values will be reset to their defaults. Consider using `reset` to reset all these values to those inherited from the parent thread.",
      examples: [
"Clear wipes out the threads locals
use_synth :blade
use_octave 3

puts \"before\"         #=> \"before\"
puts current_synth      #=> :blade
puts current_octave     #=> 3
puts rand               #=> 0.75006103515625
puts tick               #=> 0

at do
  use_synth :tb303
  puts rand               #=> 0.9287109375
  clear
  puts \"thread\"         #=> \"thread\"


                          # The clear reset the current synth to the default
                          # of :beep. We are therefore ignoring any inherited
                          # synth settings. It is as if the thread was a completely
                          # new Run.
  puts current_synth      #=> :beep

                          # The current octave defaults back to 0
  puts current_octave     #=> 0

                          # The random stream defaults back to the standard
                          # stream used by every new Run.
  puts rand               #=> 0.75006103515625
  puts tick               #=> 0
end"
]

      def time_shift(delta, &blk)
        raise "Timeshift requires a do/end block" unless blk
        sat = @mod_sound_studio.sched_ahead_time
        sleep_time = delta * __thread_locals.get(:sonic_pi_spider_sleep_mul)
        raise "Timeshift delta is too large.\nYou specified #{delta} yet the sched ahead time is #{sat}" if sleep_time.abs >= sat
        vt = __system_thread_locals.get :sonic_pi_spider_time
        __system_thread_locals.set :sonic_pi_spider_time, (vt + sleep_time).freeze
        curr_beat = __system_thread_locals.get(:sonic_pi_spider_beat)
        __system_thread_locals.set(:sonic_pi_spider_beat, curr_beat + delta)
        blk.call
        __schedule_delayed_blocks_and_messages!
        vt = __system_thread_locals.get :sonic_pi_spider_time
        __system_thread_locals.set :sonic_pi_spider_time, (vt - sleep_time).freeze
        curr_beat = __system_thread_locals.get(:sonic_pi_spider_beat)
        __system_thread_locals.set(:sonic_pi_spider_beat, curr_beat - delta)
      end
      doc name:           :time_shift,
          introduced:     Version.new(2,11,0),
          summary:        "Slide time forwards or backwards for the given block",
          args:           [[:delta_time, :number]],
          returns:        nil,
          opts:           nil,
          accepts_block:  true,
          doc:            "The code within the given block is executed with the specified delta time shift specified in beats. For example, if the delta value is 0.1 then all code within the block is executed with a 0.1 beat delay. Negative values are allowed which means you can move a block of code *backwards in time*. For example a delta value of -0.1 will execute the code in the block 0.1 beats ahead of time. Normal time is restored after the execution of the block.

Note that the the block is executed synchronously, so all sleeps within the block will be accounted for.

Also, note that the abs of the delta value must be less than the `sched_ahead_time!`.",
          examples:       ["# shift forwards in time
play 70            #=> plays at time 0
sleep 1
play 75            #=> plays at time 1

time_shift 0.1 do
                   # time shifts forward by 0.1 beats
  play 80          #=> plays at 1.1
  sleep 0.5
  play 80          #=> plays at 1.6
                   # time shifts back by 0.1 beats
                   # however, the sleep 0.5 is still accounted for
end
                   # we now honour the original sleep 1 and the
                   # sleep 0.5 within the time_shift block, but
                   # any time shift delta has been removed
play 70            #=> plays at 1.5",

        "# shift backwards in time

play 70            #=> plays at time 0
sleep 1
play 75            #=> plays at time 1

time_shift -0.1 do
                   # time shifts backwards by 0.1 beats
  play 80          #=> plays at 0.9
  sleep 0.5
  play 80          #=> plays at 1.4
                   # time shifts forward by 0.1 beats
                   # however, the sleep 0.5 is still accounted for
end
                   # we now honour the original sleep 1 and the
                   # sleep 0.5 within the time_shift block, but
                   # any time shift delta has been removed
play 70            #=> plays at 1.5"
      ]


      def tick_set(*args)
        SonicPi::Core::ThreadLocalCounter.set(*args)
      end
      doc name:           :tick_set,
          introduced:     Version.new(2,6,0),
          summary:        "Set tick to a specific value",
          args:           [[:value, :number]],
          alt_args:       [[[:key, :symbol], [:value, :number]]],
          returns:        :number,
          opts:           nil,
          accepts_block:  false,
          doc:            "Set the default tick to the specified `value`. If a `key` is referenced, set that tick to `value` instead. Next call to `look` will return `value`.",
          examples:       ["
  tick_set 40 # set default tick to 40
  puts look   #=> 40",
  "
  tick_set :foo, 40 # set tick :foo to 40
  puts look(:foo)   #=> 40 (tick :foo is now 40)
  puts look         #=> 0 (default tick is unaffected)

  "
      ]




      def tick_reset(*args)
        SonicPi::Core::ThreadLocalCounter.rm(*args)
      end
      doc name:           :tick_reset,
          introduced:     Version.new(2,6,0),
          summary:        "Reset tick to 0",
          args:           [],
          alt_args:       [[[:key, :symbol]]],
          returns:        :number,
          opts:           nil,
          accepts_block:  false,
          doc:            "Reset default tick to 0. If a `key` is referenced, set that tick to 0 instead. Same as calling tick_set(0)",
          examples:       ["
           # increment default tick a few times
  tick
  tick
  tick
  puts look #=> 2 (default tick is now 2)
  tick_set 0 # default tick is now 0
  puts look #=> 0 (default tick is now 0
  ",
  "
                  # increment tick :foo a few times
  tick :foo
  tick :foo
  tick :foo
  puts look(:foo) #=> 2 (tick :foo is now 2)
  tick_set 0 # default tick is now 0
  puts look(:foo) #=> 2 (tick :foo is still 2)
  tick_set :foo, 0 #  reset tick :foo
  puts look(:foo) #=> 0 (tick :foo is now 0)"
      ]




      def tick_reset_all
        SonicPi::Core::ThreadLocalCounter.reset_all
      end
      doc name:           :tick_reset_all,
          introduced:     Version.new(2,6,0),
          summary:        "Reset all ticks",
          args:           [[:value, :number]],
          alt_args:       [[[:key, :symbol], [:value, :number]]],
          returns:        :nil,
          opts:           nil,
          accepts_block:  false,
          doc:            "Reset all ticks - default and keyed",
          examples:       ["
  tick      # increment default tick and tick :foo
  tick
  tick :foo
  tick :foo
  tick :foo
  puts look #=> 1
  puts look(:foo) #=> 2
  tick_reset_all
  puts look #=> 0
  puts look(:foo) #=> 0
  "
      ]

      def tick(*args)
        SonicPi::Core::ThreadLocalCounter.tick(*args)
      end
      doc name:           :tick,
          introduced:     Version.new(2,6,0),
          summary:        "Increment a tick and return value",
          args:           [[:key, :symbol]],
          alt_args:       [[[:key, :symbol], [:value, :number]]],
          returns:        :number,
          opts:           {step: "The amount to tick up by. Default is 1.",
                           offset: "Offset to add to index returned. Useful when calling tick on lists, rings and vectors to offset the returned value. Default is 0."},
          accepts_block:  false,
          doc:            "Increment the default tick by 1 and return value. Successive calls to `tick` will continue to increment the default tick. If a `key` is specified, increment that specific tick. If an increment `value` is specified, increment key by that value rather than 1. Ticks are `in_thread` and `live_loop` local, so incrementing a tick only affects the current thread's version of that tick. See `tick_reset` and `tick_set` for directly manipulating the tick vals.",
          examples:       ["
  puts tick #=> 0
  puts tick #=> 1
  puts tick #=> 2
  puts tick #=> 3
  ",
  "
  puts tick(:foo) #=> 0 # named ticks have their own counts
  puts tick(:foo) #=> 1
  puts tick(:foo) #=> 2
  puts tick(:bar) #=> 0 # tick :bar is independent of tick :foo
  ",
  " # Each_live loop has its own separate ticks
  live_loop :fast_tick do
    puts tick   # the fast_tick live_loop's tick will
    sleep 2     # be updated every 2 seconds
  end

  live_loop :slow_tick do
    puts tick   # the slow_tick live_loop's tick is
    sleep 4     # totally independent from the fast_tick
                # live loop and will be updated every 4
                # seconds
  end
  ",
  "
  live_loop :regular_tick do
    puts tick   # the regular_tick live_loop's tick will
    sleep 1     # be updated every second
  end

  live_loop :random_reset_tick do
    if one_in 3 # randomly reset tick
      tick_reset
      puts \"reset tick!\"
    end
    puts tick   # this live_loop's tick is totally
    sleep 1     # independent and the reset only affects
                # this tick.
  end
  ",
  "
  # Ticks work directly on lists, and will tick through each element
  # However, once they get to the end, they'll return nil
  live_loop :scale do
    play [:c, :d, :e, :f, :g].tick   # play all notes just once, then rests
    sleep 1
  end
  ",
  "
  # Normal ticks interact directly with list ticks
  live_loop :odd_scale do
    tick  # Increment the default tick
    play [:c, :d, :e, :f, :g, :a].tick   # this now play every *other* note just once,
                                         # then rests
    sleep 1
  end
  ",
  "
  # Ticks work wonderfully with rings
  # as the ring ensures the tick wraps
  # round internally always returning a
  # value
  live_loop :looped_scale do
    play (ring :c, :d, :e, :f, :g).tick   # play all notes just once, then repeats
    sleep 1
  end
  ",
  "
  # Ticks work wonderfully with scales
  # which are also rings
  live_loop :looped_scale do
    play (scale :e3, :minor_pentatonic).tick   # play all notes just once, then repeats
    sleep 0.25
  end
  "
      ]




      def look(*args)
        return args[1] if args[1].is_a?(Numeric) && args.size == 1
        SonicPi::Core::ThreadLocalCounter.look(*args)
      end
      doc name:           :look,
          introduced:     Version.new(2,6,0),
          summary:        "Obtain value of a tick",
          args:           [],
          alt_args:       [[[:key, :symbol]]],
          returns:        :number,
          opts:           {offset: "Offset to add to index returned. Useful when calling look on lists, rings and vectors to offset the returned value"},
          accepts_block:  false,
          doc:            "Read and return value of default tick. If a `key` is specified, read the value of that specific tick. Ticks are `in_thread` and `live_loop` local, so the tick read will be the tick of the current thread calling `look`.",
          examples:       ["
  puts look #=> 0
  puts look #=> 0
  puts look #=> 0 # look doesn't advance the tick, it just returns the current value
  ",
  "
  puts look #=> 0 # A look is always 0 before the first tick
  tick # advance the tick
  puts look #=> 0 # Note: a look is still 0 after the first tick.
  tick
  puts look #=> 1
  puts look #=> 1 # making multiple calls to look doesn't affect tick value
  tick
  puts look #=> 2
  ",
  "
  tick(:foo)
  tick(:foo)
  puts look(:foo) #=> 1 (keyed look :foo has been advanced)
  puts look #=> 0 (default look hasn't been advanced)
  puts look(:bar) #=> 0 (other keyed looks haven't been advanced either)
  ",
  "
  # You can call look on lists and rings
  live_loop :foo do
    tick                                      # advance the default tick
    use_synth :beep
    play (scale :e3, :minor_pentatonic).look  # look into the default tick to play all notes in sequence
    sleep 0.5
    use_synth :square
    play (ring :e1, :e2, :e3).look, release: 0.25 # use the same look on another ring
    sleep 0.25
  end
  ",
"
# Returns numbers unchanged if single argument
puts look(0)     #=> 0
puts look(4)     #=> 4
puts look(-4)    #=> -4
puts look(20.3)  #=> 20.3"
      ]




      def stop
        # Schedule messages
        __schedule_delayed_blocks_and_messages!
        raise SonicPi::Stop
      end
      doc name:           :stop,
          introduced:     Version.new(2,5,0),
          summary:        "Stop current thread or run",
          args:           [],
          returns:        nil,
          opts:           nil,
          accepts_block:  false,
          doc:            "Stops the current thread or if not in a thread, stops the current run. Does not stop any running synths triggered previously in the run/thread or kill any existing sub-threads.",
          examples:       ["
  sample :loop_amen #=> this sample is played until completion
  sleep 0.5
  stop                #=> signal to stop executing this run
  sample :loop_garzul #=> this never executes
  ",
  "
  in_thread do
    play 60      #=> this note plays
    stop
    sleep 0.5    #=> this sleep never happens
    play 72      #=> this play never happens
  end

  play 80  #=> this plays as the stop only affected the above thread",

  "
  # Stopping live loops
  live_loop :foo
    sample :bd_haus
    sleep 1
    stop               # live loop :foo will now stop and no longer loop
  end

  live_loop :bar       # live loop :bar will continue looping
    sample :elec_blip
    sleep 0.25
  end"
      ]




      def on(condition, &blk)
        blk.call if truthy?(condition)
      end
      doc name:           :on,
          introduced:     Version.new(2,10,0),
          summary:        "Optionally evaluate block",
          args:           [[:condition, :truthy]],
          returns:        nil,
          opts:           nil,
          accepts_block:  false,
          doc:            "Optionally evaluate the block depending on the truthiness of the supplied condition. The truthiness rules are as follows: all values are seen as true except for: false, nil and 0. Lambdas will be automatically called and the truthiness of their results used.",
      examples:       [
"
on true do
  play 70     #=> will play 70 as true is truthy
end",
"
on 1 do
  play 70     #=> will play 70 as 1 is truthy
end",
"
on 0 do
  play 70     #=> will *not* play 70 as 0 is not truthy
end",
"
on false do
  play 70     #=> will *not* play 70 as false is not truthy
end",
"
on nil do
  play 70     #=> will *not* play 70 as nil is not truthy
end",
"
on lambda{true} do
  play 70     #=> will play 70 as the lambda returns a truthy value
end",
"
on lambda{false} do
  play 70     #=> will *not* play 70 as the lambda does not return a truthy value
end",
"
on lambda{[true, false].choose} do
  play 70     #=> will maybe play 70 depending on the choice in the lambda
end"



      ]




      def bools(*args)
        args.map do |a|
          if (a == 0) || (not a)
            false
          else
            true
          end
        end.ring
      end
      doc name:           :bools,
          introduced:     Version.new(2,2,0),
          summary:        "Create a ring of boolean values",
          args:           [[:list, :array]],
          returns:        :ring,
          opts:           nil,
          accepts_block:  false,
          doc:            "Create a new ring of booleans values from 1s and 0s, which can be easier to write and manipulate in a live setting.",
          examples:       [
        "(bools 1, 0)    #=> (ring true, false)",
        "(bools 1, 0, true, false, nil) #=> (ring true, false, true, false, false)"
      ]




      def stretch(*args)
        raise "stretch needs an even number of arguments, you passed: #{args.size} - #{args.inspect}" unless args.size.even?
        res = args.each_slice(2).flat_map do |values, num_its|

          if !values.respond_to? :flat_map
            values = [values]
          end
          knit(*values.flat_map{|v| [v, num_its]})
        end
        (res||[]).ring
      end
      doc name:           :stretch,
          introduced:     Version.new(2,6,0),
          summary:        "Stretch a sequence of values",
          args:           [[:list, :anything], [:count, :number]],
          returns:        :ring,
          opts:           nil,
          accepts_block:  false,
          doc:            "Stretches a list of values each value repeated count times. Always returns a ring regardless of the type of the list that is stretched. To preserve type, consider using `.stretch` i.e. `(ramp 1, 2, 3).stretch(2) #=> (ramp 1, 1, 2, 2, 3, 3)`",
          examples:       [
        "(stretch [1,2], 3)    #=> (ring 1, 1, 1, 2, 2, 2)",
        "(stretch [:e2, :c3], 1, [:c2, :d3], 2) #=> (ring :e2, :c3, :c2, :c2, :d3, :d3)"
      ]




      def knit(*args)
        raise "knit must have a even number of arguments, you passed: #{args.size} - #{args.inspect}" unless args.size.even?
        res = []
        args.each_slice(2) do |val, num_its|
          if num_its > 0
            res = res + ([val] * num_its)
          end
        end
        res.ring
      end
      doc name:           :knit,
          introduced:     Version.new(2,2,0),
          summary:        "Knit a sequence of repeated values",
          args:           [[:value, :anything], [:count, :number]],
          returns:        :ring,
          opts:           nil,
          accepts_block:  false,
          doc:            "Knits a series of value, count pairs to create a ring buffer where each value is repeated count times.",
          examples:       [
        "(knit 1, 5)    #=> (ring 1, 1, 1, 1, 1)",
        "(knit :e2, 2, :c2, 3) #=> (ring :e2, :e2, :c2, :c2, :c2)"
      ]




      def spread(num_accents, size, *args)
        args_h = resolve_synth_opts_hash_or_array(args)
        beat_rotations = args_h[:rotate]
        res = []
        # if someone requests 9 accents in a bar of 8 beats
        # default to filling the output with accents
        if num_accents > size
          res = [true] * size
          return res.ring
        end

        size.times do |i|
          # makes a boolean based on the index
          # true is an accent, false is a rest
          res << ((i * num_accents % size) < num_accents)
        end

        if beat_rotations && beat_rotations.is_a?(Numeric)
          beat_rotations = beat_rotations.abs
          while beat_rotations > 0 do
            beat_rotations -= 1 if res.rotate!.first == true
          end

          res.ring
        else
          res.ring
        end
      end
      doc name:           :spread,
          introduced:     Version.new(2,4,0),
          summary:        "Euclidean distribution for beats",
          args:           [[:num_accents, :number], [:size, :number]],
          returns:        :ring,
          opts:           {rotate: "rotate to the next strong beat allowing for easy permutations of the original rhythmic grouping (see example)"},
          accepts_block:  false,
          doc:            "Creates a new ring of boolean values which space a given number of accents as evenly as possible throughout a bar. This is an implementation of the process described in 'The Euclidean Algorithm Generates Traditional Musical Rhythms' (Toussaint 2005).",
          examples:       [
        "(spread 3, 8)    #=> (ring true, false, false, true, false, false, true, false) a spacing of 332",
        "(spread 3, 8, rotate: 1) #=> (ring true, false, false, true, false, true, false, false) a spacing of 323",
        "
  # Easily create interesting polyrhythmic beats
  live_loop :euclid_beat do
    sample :elec_bong, amp: 1.5 if (spread 3, 8).tick # Spread 3 bongs over 8
    sample :perc_snap, amp: 0.8 if (spread 7, 11).look # Spread 7 snaps over 11
    sample :bd_haus, amp: 2 if (spread 1, 4).look # Spread 1 bd over 4
    sleep 0.125
  end
  ",
  "
  # Spread descriptions from
  # 'The Euclidean Algorithm Generates Traditional Musical Rhythms' (Toussaint 2005).
  (spread 2, 5)  # A thirteenth century Persian rhythm called Khafif-e-ramal.

  (spread 3, 4)  # The archetypal pattern of the Cumbria from Columbia, as well
                 # as a Calypso rhythm from Trinidad

  (spread 3, 5)  # When started on the second onset, is another thirteenth
                 # century Persian rhythm by the name of Khafif-e-ramal, as well
                 # as a Romanian folk-dance rhythm.

  (spread 3, 7)  # A ruchenitza rhythm used in a Bulgarian folk-dance.

  (spread 3, 8)  # The Cuban tresillo pattern

  (spread 4, 7)  # Another Ruchenitza Bulgarian folk-dance rhythm

  (spread 4, 9)  # The Aksak rhythm of Turkey.

  (spread 4, 11) # The metric pattern used by Frank Zappa in his piece Outside Now

  (spread 5, 6)  # Yields the York-Samai pattern, a popular Arab rhythm, when
                 # started on the second onset.

  (spread 5, 7)  # The Nawakhat pattern, another popular Arab rhythm.

  (spread 5, 8)  # The Cuban cinquillo pattern.

  (spread 5, 9)  # A popular Arab rhythm called Agsag-Samai.

  (spread 5, 11) # The metric pattern used by Moussorgsky in Pictures at an
                 # Exhibition

  (spread 5, 12) # The Venda clapping pattern of a South African children's
                 # song.

  (spread 5, 16) # The Bossa-Nova rhythm necklace of Brazil.

  (spread 7, 8)  # A typical rhythm played on the Bendir (frame drum)

  (spread 7, 12) # A common West African bell pattern.

  (spread 7, 16) # A Samba rhythm necklace from Brazil.

  (spread 9, 16) # A rhythm necklace used in the Central African Republic.

  (spread 11, 24) # A rhythm necklace of the Aka Pygmies of Central Africa.

  (spread 13, 24) # Another rhythm necklace of the Aka Pygmies of the upper
                  # Sangha.
  "
      ]




      def range(start, finish, *args)
        if is_list_like?(args) && args.size == 1 && args.first.is_a?(Numeric)
          # Allow one optional arg for legacy reasons. Versions earlier
          # than v2.5 allowed: range(1, 10, 2)
          step_size = args.first
          inclusive = false
        else
          args_h = resolve_synth_opts_hash_or_array(args)
          step_size = args_h[:step] || 1
          inclusive = args_h[:inclusive]
        end

        return [].ring if start == finish
        step_size = step_size.abs
        res = []
        cur = start
        if inclusive
          if start < finish
            while cur <= finish
              res << cur
              cur += step_size
            end
          else
            while cur >= finish
              res << cur
              cur -= step_size
            end
          end

        else
          if start < finish
            while cur < finish
              res << cur
              cur += step_size
            end
          else
            while cur > finish
              res << cur
              cur -= step_size
            end
          end
        end
        res.ring
      end
      doc name:           :range,
          introduced:     Version.new(2,2,0),
          summary:        "Create a ring buffer with the specified start, finish and step size",
          args:           [[:start, :number], [:finish, :number], [:step_size, :number]],
          returns:        :ring,
          opts:           {:step      => "Size of increment between steps; step size.",
                           :inclusive => "If set to true, range is inclusive of finish value"},
          accepts_block:  false,
          memoize: true,
          doc:            "Create a new ring buffer from the range arguments (start, finish and step size). Step size defaults to `1`. Indexes wrap around positively and negatively",
          examples:       [
        "(range 1, 5)    #=> (ring 1, 2, 3, 4)",
        "(range 1, 5, inclusive: true) #=> (ring 1, 2, 3, 4, 5)",
        "(range 1, 5, step: 2) #=> (ring 1, 3)",
        "(range 1, -5, step: 2) #=> (ring 1, -1, -3)",
        "(range 1, -5, step: 2)[-1] #=> -3"
      ]




      def line(start, finish, *args)
        return [].ring if start == finish
        args_h = resolve_synth_opts_hash_or_array(args)
        num_slices = args_h[:steps] || 4
        inclusive = args_h[:inclusive]

        raise "steps: opt for fn line should be a positive non-zero whole number" unless num_slices > 0

        if inclusive
          step_size = (start - finish).abs.to_f / (num_slices - 1)
          range(start.to_f, finish.to_f, inclusive: true,  step: step_size)
        else
          step_size = (start - finish).abs.to_f / num_slices
          range(start.to_f, finish.to_f, step: step_size)
        end
      end
      doc name:           :line,
          introduced:     Version.new(2,5,0),
          summary:        "Create a ring buffer representing a straight line",
          args:           [[:start, :number], [:finish, :number]],
          returns:        :ring,
          opts:           {:steps     => "number of slices or segments along the line",
                           :inclusive => "boolean value representing whether or not to include finish value in line"},
          accepts_block:  false,
          memoize: true,
          doc:            "Create a ring buffer representing a straight line between start and finish of num_slices elements. Num slices defaults to `8`. Indexes wrap around positively and negatively. Similar to `range`.",
          examples:       [
        "(line 0, 4, steps: 4)    #=> (ring 0.0, 1.0, 2.0, 3.0)",
        "(line 5, 0, steps: 5)    #=> (ring 5.0, 4.0, 3.0, 2.0, 1.0)",
        "(line 0, 3, inclusive: true) #=> (ring 0.0, 1.0, 2.0, 3.0)"
      ]




      def halves(start, num_halves=1)
        raise "Start value for halves needs to be a number, got: #{start.inspect}" unless start.is_a?(Numeric)
        start = start.to_f
        return doubles(start, num_halves * -1) if num_halves < 0
        a = []
        val = start
        num_halves.times do
          a << val
          val /= 2.0
        end
        a.ring
      end
      doc name:           :halves,
          introduced:     Version.new(2,10,0),
          summary:        "Create a ring of successive halves",
          args:           [[:start, :number], [:num_halves, :int]],
          returns:        :ring,
          opts:           nil,
          accepts_block:  false,
          memoize: true,
          doc:            "Create a ring containing the results of successive halving of the `start` value. If `num_halves` is negative, will return a ring of `doubles`.",
          examples:       [
        "(halves 60, 2)  #=> (ring 60, 30)",
        "(halves 120, 3) #=> (ring 120, 60, 30)",
        "(halves 120, 5) #=> (ring 120, 60, 30, 15, 7.5)",
        "(halves 30, -5) #=> (ring 30, 60, 120, 240, 480)"
      ]




      def doubles(start, num_doubles=1)
        raise "Start value for doubles needs to be a number, got: #{start.inspect}" unless start.is_a?(Numeric)
        return halves(start, num_doubles * -1) if num_doubles < 0
        start = start.to_f
        a = []
        val = start
        num_doubles.times do
          a << val
          val *= 2.0
        end
        a.ring
      end
      doc name:           :doubles,
          introduced:     Version.new(2,10,0),
          summary:        "Create a ring of successive doubles",
          args:           [[:start, :number], [:num_doubles, :int]],
          returns:        :ring,
          opts:           nil,
          accepts_block:  false,
          memoize: true,
          doc:            "Create a ring containing the results of successive doubling of the `start` value. If `num_doubles` is negative, will return a ring of `halves`.",
          examples:       [
        "(doubles 60, 2)  #=> (ring 60, 120)",
        "(doubles 1.5, 3) #=> (ring 1.5, 3, 6)",
        "(doubles 1.5, 5) #=> (ring 1.5, 3, 6, 12, 24)",
        "(doubles 100, -4) #=> (ring 100, 50, 25, 12.5)"
      ]




      def vector(*args)
        SonicPi::Core::SPVector.new(args)
      end
      doc name:           :vector,
          introduced:     Version.new(2,6,0),
          summary:        "Create a vector",
          args:           [[:list, :array]],
          returns:        :vector,
          opts:           nil,
          accepts_block:  false,
          doc:            "Create a new immutable vector from args. Out of range indexes return nil.",
          examples:       [
        "(vector 1, 2, 3)[0] #=> 1",
        "(vector 1, 2, 3)[1] #=> 2",
        "(vector 1, 2, 3)[2] #=> 3",
        "(vector 1, 2, 3)[3] #=> nil",
        "(vector 1, 2, 3)[1000] #=> nil",
        "(vector 1, 2, 3)[-1] #=> nil",
        "(vector 1, 2, 3)[-1000] #=> nil",
      ]




      def ring(*args)
        SonicPi::Core::RingVector.new(args)
      end
      doc name:           :ring,
          introduced:     Version.new(2,2,0),
          summary:        "Create a ring buffer",
          args:           [[:list, :array]],
          returns:        :ring,
          opts:           nil,
          accepts_block:  false,
          doc:            "Create a new immutable ring buffer from args. Indexes wrap around positively and negatively",
          examples:       [
        "(ring 1, 2, 3)[0] #=> 1",
        "(ring 1, 2, 3)[1] #=> 2",
        "(ring 1, 2, 3)[3] #=> 1",
        "(ring 1, 2, 3)[-1] #=> 3",
      ]




      def ramp(*args)
        SonicPi::Core::RampVector.new(args)
      end
      doc name:           :ramp,
          introduced:     Version.new(2,6,0),
          summary:        "Create a ramp vector",
          args:           [[:list, :array]],
          returns:        :ramp,
          opts:           nil,
          accepts_block:  false,
          doc:            "Create a new immutable ramp vector from args. Indexes always return first or last value if out of bounds.",
          examples:       [
        "(ramp 1, 2, 3)[0] #=> 1",
        "(ramp 1, 2, 3)[1] #=> 2",
        "(ramp 1, 2, 3)[2] #=> 3",
        "(ramp 1, 2, 3)[3] #=> 3",
        "(ramp 1, 2, 3)[1000] #=> 3",
        "(ramp 1, 2, 3)[-1] #=> 1",
        "(ramp 1, 2, 3)[-1000] #=> 1",
      ]




      def choose(args)
        args.to_a.choose
      end
      doc name:           :choose,
          introduced:     Version.new(2,0,0),
          summary:        "Random list selection",
          args:           [[:list, :array]],
          opts:           nil,
          accepts_block:  false,
          doc:            "Choose an element at random from a list (array).",
         examples:       ["
  loop do
    play choose([60, 64, 67]) #=> plays one of 60, 64 or 67 at random
    sleep 1
    play chord(:c, :major).choose #=> You can also call .choose on the list
    sleep 1
  end"]




      def pick(*args)
        if is_list_like?(args[0])
          items = args[0]
          if args[1].is_a? Numeric
            n = args[1]
            args.shift(2)
          else
            n = 1
            args.shift(1)
          end
        else
          items = nil
          if args[0].is_a? Numeric
            n = args[0]
            args.shift(1)
          else
            n = 1
          end
        end

        unless items
          return lambda {|col| col.pick(n, *args)}
        end
        items.pick(n, *args)
      end
      doc name:           :pick,
          introduced:     Version.new(2,10,0),
          summary:        "Randomly pick from list (with duplicates)",
          args:           [[:list, :array], [:n, :number_or_nil]],
          opts:           {:skip => "Number of rands to skip over with each successive pick"},
          accepts_block:  false,
          doc:            "Pick n elements from list or ring. Unlike shuffle, after each element has been picked, it is 'returned' to the list so it may be picked again. This means there may be duplicates in the result. If n is greater than the size of the ring/list then duplicates are guaranteed to be in the result.

If `n` isn't supplied it defaults to the size of the list/ring.

If no arguments are given, will return a lambda function which when called takes an argument which will be a list to be picked from. This is useful for choosing random `onset:` vals for samples.",
         examples:       ["
puts [1, 2, 3, 4, 5].pick(3) #=> [4, 4, 3]",
"
puts (ring 1, 2, 3, 4, 5).pick(3) #=> (ring 4, 4, 3)",

"
puts (ring 1, 2).pick(5) #=> (ring 2, 2, 1, 1, 1)",
"
puts (ring 1, 2, 3).pick #=> (ring 3, 3, 2)"
      ]




      def inc(n)
        n + 1
      end
      doc name:          :inc,
          introduced:    Version.new(2, 1, 0),
          summary:       "Increment",
          args:          [[:n, :number]],
          opts:          {},
          accepts_block: false,
          doc:           "Increment a number by `1`. Equivalent to `n + 1`",
          examples:     [
        "inc 1 # returns 2",
        "inc -1 # returns 0"]




      def dec(n)
        n - 1
      end
      doc name:          :dec,
          introduced:    Version.new(2, 1, 0),
          summary:       "Decrement",
          args:          [[:n, :number]],
          opts:          {},
          accepts_block: false,
          doc:           "Decrement a number by `1`. Equivalent to `n - 1`",
          examples:     [
        "dec 1 # returns 0",
        "dec -1 # returns -2"]



      def live_loop(name=nil, *args, &block)
        raise "live_loop needs to have a unique name. For example: live_loop :foo" unless name
        raise "live_loop's name needs to be a string or symbol, got: #{name.inspect}. Example usage: live_loop :foo" unless (name.is_a?(Symbol) || name.is_a?(String))
        ll_name = "live_loop_#{name}".to_sym
        raise "live_loop #{name.inspect} must be called with a do/end block" unless block

        args_h = resolve_synth_opts_hash_or_array(args)

        sync_sym = args_h[:sync]
        sync_bpm_sym = args_h[:sync_bpm]
        sync_sym = nil if sync_bpm_sym

        raise "livelock detection - live_loop cannot sync with itself - please choose another sync name for live_loop #{name.inspect}" if name == sync_sym || name == sync_bpm_sym

        delay = args_h[:delay]
        raise "live_loop's delay: opt must be a number, got #{delay.inspect}" if delay && !delay.is_a?(Numeric)

        if args_h.has_key? :auto_cue
          auto_cue = args_h[:auto_cue]
        else
          auto_cue = true
        end

        case block.arity
        when 0
          define(ll_name) do |a|
            block.call
          end
        when 1
          define(ll_name) do |a|
            block.call(a)
          end
        else
          raise "Live loop block must only accept 0 or 1 args"
        end

        in_thread(name: ll_name, delay: delay, sync: sync_sym, sync_bpm: sync_bpm_sym) do
          __system_thread_locals.set_local :sonic_pi_local_live_loop_auto_cue, auto_cue
          if args_h.has_key?(:init)
            res = args_h[:init]
          else
            res = 0
          end
          use_random_seed args_h[:seed] if args_h[:seed]
          loop do
            slept = block_slept? do
              __system_thread_locals.set(:sonic_pi_spider_synced, false)
              cue name if __system_thread_locals.get :sonic_pi_local_live_loop_auto_cue
              res = send(ll_name, res)
            end

            raise "Live loop #{name.to_sym.inspect} did not sleep!" unless slept or __system_thread_locals.get(:sonic_pi_spider_synced)
          end
        end

        st = sthread(ll_name)
        __system_thread_locals(st).set_local :sonic_pi_local_live_loop_auto_cue, auto_cue if st
        st
      end
      doc name:           :live_loop,
          introduced:     Version.new(2,1,0),
          summary:        "A loop for live coding",
          args:           [[:name, :symbol]],
          opts:           {:init     => "initial value for optional block arg",
                           :auto_cue => "enable or disable automatic cue (default is true)",
                           :delay    => "Initial delay in beats before the live_loop starts. Default is 0.",
                           :sync     => "Initial sync symbol. Will sync with this symbol before the live_loop starts.",
                           :sync_bpm => "Initial sync symbol. Will sync with this symbol before the live_loop starts. Live loop will also inherit the BPM of the thread which cued the symbol.",
                           :seed     => "override initial random generator seed before starting loop."
      },
          accepts_block:  true,
          requires_block: true,
          async_block:    true,
          intro_fn:       true,
          doc:            "Loop the do/end block forever. However, unlike a basic loop, a live_loop has two special properties. Firstly it runs in a thread - so you can have any number of live loops running at the same time (concurrently). Secondly, you can change the behaviour of a live loop whilst it is still running without needing to stop it. Live loops are therefore the secret to live coding with Sonic Pi.

As live loops are excecuted within a named in_thread, they behave similarly. See the in_thread documentation for all the details. However, it's worth mentioning a few important points here. Firstly, only one live loop with a given name can run at any one time. Therefore, if you define two or more `live_loop`s called `:foo` only one will be running. Another important aspect of `live_loop`s is that they manage their own thread locals set with the `use_*` and `with_*` fns. This means that each `live_loop` can have its own separate default synth, BPM and sample defaults. When a `live_loop` is *first* created, it inherits the thread locals from the parent thread, but once it has started, the only way to change them is by re-defining the do/end body of the `live_loop`. See the examples below for details. Finally, as mentioned above, provided their names are different, you may have many `live_loop`s executing at once.

A typical way of live coding with live loops is to define a number of them in a buffer, hit Run to start them and then to modify their do/end blocks and then hit Run again. This will not create any more thread, but instead just modify the behaviour of the existing threads. The changes will *not* happen immediately. Instead, they will only happen the next time round the loop. This is because the behaviour of each live loop is implemented with a standard function. When a live loop is updated, the function definition is also updated. Each time round the live loop, the function is called, so the new behviour is only observed next time round the loop.

Also sends a `cue` with the same name each time the `live_loop` repeats. This may be used to `sync` with other threads and `live_loop`s.

If the `live_loop` block is given a parameter, this is given the result of the last run of the loop (with initial value either being `0` or an init arg). This allows you to 'thread' values across loops.

Finally, it is possible to delay the initial trigger of the live_loop on creation with both the `delay:` and `sync:` opts. See their respective docstrings. If both `delay:` and `sync:` are specified, on initial live_loop creation first the delay will be honoured and then the sync.
",
          examples:       ["
## Define and start a simple live loop

live_loop :ping do  # Create a live loop called :ping
  sample :elec_ping # This live loops plays the :elec_ping sample
  sleep 1           # Then sleeps for 1 beat before repeating
end
  ",

        "
## Every live loop must sleep or sync

live_loop :ping do  # Create a live loop called :ping
  sample :elec_ping # This live loops plays the :elec_ping sample
                    # However, because the do/end lock of the live loop does not
                    # contain any calls to sleep or sync, the live loop stops at
                    # the end of the first loop with a 'Did not sleep' error.
end",

        "
## Multiple live loops will play at the same time
live_loop :foo do  # Start a live loop called :foo
  play 70
  sleep 1
end

live_loop :bar do  # Start another live loop called :bar
  sample :bd_haus  # Both :foo and :bar will be playing
  sleep 0.5        # at the same time.
end
",

        "
## Live loops inherit external use_* thread locals
use_bpm 30
live_loop :foo do
  play 70           # live loop :foo now has a BPM of 30
  sleep 1           # This sleep will be for 2 seconds
end
",

        "
## Live loops can have their own thread locals
live_loop :foo do
  use_bpm 30       # Set the BPM of live loop :foo to 30
  play 70
  sleep 1          # This sleep will be for 2 seconds
end

live_loop :bar do
  use_bpm 120      # Set the BPM of live loop :bar to 120
  play 82
  sleep 1          # This sleep will be for 0.5 seconds
end
",

        "
## Live loops can pass values between iterations
live_loop :foo do |a|  # pass a param (a) to the block (inits to 0)
  puts a               # prints out all the integers
  sleep 1
  a += 1               # increment a by 1 (last value is passed back into the loop)
end
  ",

        "
## Live loop names must be unique
live_loop :foo do  # Start a live loop called :foo
  play 70
  sleep 1
end

live_loop :foo do  # Attempt to start another also called :foo
  sample :bd_haus  # With a different do/end block
  sleep 0.5        # This will not start another live loop
                   # but instead replace the behaviour of the first.
end                # There will only be one live loop running playing
                   # The bass drum
",
        "
## You can sync multiple live loops together
live_loop :foo, sync: :bar do # Wait for a :bar cue event before starting :foo
 play 70                      # Live loop :foo is therefore blocked and does
 sleep 1                      # not make a sound initially
end

sleep 4                       # Wait for 4 beats

live_loop :bar do             # Start a live loop called :foo which will emit a :bar
  sample :bd_haus             # cue message therefore releasing the :foo live loop.
  sleep 0.5                   # Live loop :foo therefore starts and also inherits the
end                           # logical time of live loop :bar.

                              # This pattern is also useful to re-sync live loops after
                              # errors are made. For example, when modifying live loop :foo
                              # it is possible to introduce a runtime error which will stop
                              # :foo but not :bar (as they are separate, isolated threads).
                              # Once the error has been fixed and the code is re-run, :foo
                              # will automatically wait for :bar to loop round and restart
                              # in sync with the correct virtual clock."

      ]


      def block_duration(&block)
        t1 = __system_thread_locals.get(:sonic_pi_spider_time)
        block.call
        t2 = __system_thread_locals.get(:sonic_pi_spider_time)
        t2 - t1
      end
      doc name:           :block_duration,
          introduced:     Version.new(2,9,0),
          summary:        "Return block duration",
          doc:            "Given a block, runs it and returns the amount of time that has passed. This time is in seconds and is not scaled to the current BPM. Any threads spawned in the block are not accounted for.",
          args:           [[]],
          opts:           nil,
          accepts_block:  true,
          requires_block: true,
          async_block:    false,
          examples: ["
dur = block_duration do
  play 50
  sleep 1
  play 62
  sleep 2
end

puts dur #=> Returns 3 as 3 seconds have passed within the block",
"use_bpm 120
dur = block_duration do
  play 50
  sleep 1
  play 62
  sleep 2
end

puts dur #=> Returns 1.5 as 1.5 seconds have passed within the block
         #   (due to the BPM being 120)"]




      def block_slept?(&block)
        dur = block_duration(&block)
        dur > 0
      end
      doc name:           :block_slept?,
          introduced:     Version.new(2,9,0),
          summary:        "Determine if block contains sleep time",
          doc:            "Given a block, runs it and returns whether or not the block contained sleeps or syncs",
          args:           [[]],
          opts:           nil,
          accepts_block:  true,
          requires_block: true,
          async_block:    false,
          examples: ["
slept = block_slept? do
  play 50
  sleep 1
  play 62
  sleep 2
end

puts slept #=> Returns true as there were sleeps in the block",
"
in_thread do
  sleep 1
  cue :foo  # trigger a cue on a different thread
end

slept = block_slept? do
  sync :foo  # wait for the cue before playing the note
  play 62
end

puts slept #=> Returns true as the block contained a sync.",
"
slept = block_slept? do
  play 50
  play 62
end

puts slept #=> Returns false as there were no sleeps in the block"]



      def at(times=0, params=nil, &block)
        raise "at must be called with a do/end block" unless block
        had_params = params
        times = [times] if times.is_a? Numeric
        # When no params are specified, pass the times through as params
        params ||= times

        raise "params needs to be a list-like thing" unless params.respond_to? :[]
        raise "times needs to be a list-like thing" unless times.respond_to? :each_with_index

        params_size = params.size
        times.each_with_index do |t, idx|
          in_thread do
            sleep t
            case block.arity
            when 0
              block.call
            when 1
              block.call(params[idx % params_size])
            when 2
              if had_params
                block.call(t, params[idx % params_size])
              else
                block.call(t, idx)
              end
            when 3
              block.call(t, params[idx % params_size], idx)
            else
              raise "block for at should only accept 0, 1, 2 or 3 parameters. You gave: #{block.arity}."
            end
          end
        end
      end
      doc name:           :at,
          introduced:     Version.new(2,1,0),
          summary:        "Asynchronous Time. Run a block at the given time(s)",
          doc:            "Given a list of times, run the block once after waiting each given time. If passed an optional params list, will pass each param individually to each block call. If size of params list is smaller than the times list, the param values will act as rings (rotate through). If the block is given 1 arg, the times are fed through. If the block is given 2 args, both the times and the params are fed through. A third block arg will receive the index of the time.

Note, all code within the block is executed in its own thread. Therefore despite inheriting all thread locals such as the random stream and ticks, modifications will be isolated to the block and will not affect external code.",
          args:           [[:times, :list],
                           [:params, :list]],
          opts:           nil,
          accepts_block:  true,
          requires_block: true,
          async_block:    true,
          examples:       ["
  at 4 do
    sample :ambi_choir    # play sample after waiting for 4 beats
  end
  ",
  "
  at [1, 2, 4] do  # plays a note after waiting 1 beat,
    play 75           # then after 1 more beat,
  end                 # then after 2 more beats (4 beats total)
  ",
  "
  at [1, 2, 3], [75, 76, 77] do |n|  # plays 3 different notes
    play n
  end
  ",
  "
  at [1, 2, 3],
      [{:amp=>0.5}, {:amp=> 0.8}] do |p| # alternate soft and loud
    sample :drum_cymbal_open, p          # cymbal hits three times
  end
  ",
  "
  at [0, 1, 2] do |t| # when no params are given to at, the times are fed through to the block
    puts t #=> prints 0, 1, then 2
  end
  ",
  "
  at [0, 1, 2], [:a, :b] do |t, b|  #If you specify the block with 2 args, it will pass through both the time and the param
    puts [t, b] #=> prints out [0, :a], [1, :b], then [2, :a]
  end
  ",
  "
  at [0, 0.5, 2] do |t, idx|  #If you specify the block with 2 args, and no param list to at, it will pass through both the time and the index
    puts [t, idx] #=> prints out [0, 0], [0.5, 1], then [2, 2]
  end
  ",
  "
  at [0, 0.5, 2], [:a, :b] do |t, b, idx|  #If you specify the block with 3 args, it will pass through the time, the param and the index
    puts [t, b, idx] #=> prints out [0, :a, 0], [0.5, :b, 1], then [2, :a, 2]
  end
  ",
  " # at does not consume & interfere with the outer random stream
puts \"main: \", rand  # 0.75006103515625
rand_back
at 1 do         # the random stream inside the at block is separate and
                # isolated from the outer stream.
  puts \"at:\", rand # 0.9287109375
  puts \"at:\", rand # 0.1043701171875
end

sleep 2
puts \"main: \", rand # value is still 0.75006103515625
",

"
            # Each block run within at has its own isolated random stream:
at [1, 2] do
            # first time round (after 1 beat) prints:
  puts rand # 0.9287109375
  puts rand # 0.1043701171875
end
            # second time round (after 2 beats) prints:
            # 0.1043701171875
            # 0.764617919921875
"
      ]




      def version
        @version
      end
      doc name:           :version,
          introduced:     Version.new(2,0,0),
          summary:        "Get current version information",
          args:           [],
          opts:           nil,
          accepts_block:  false,
          doc:            "Return information representing the current version of Sonic Pi. This information may be further inspected with `version.major`, `version.minor`, `version.patch` and `version.dev`",
          examples:       ["
  puts version # => Prints out the current version such as v2.0.1",
  "
  puts version.major # => Prints out the major version number such as 2",
  "
  puts version.minor # => Prints out the minor version number such as 0",
  "
  puts version.patch # => Prints out the patch level for this version such as 0"]




      def spark_graph(*values)
        if is_list_like?(values.first) && values.length == 1
          values = values.first
        end

        return "" if values.length == 0
        return "spark error: can't use nested arrays" if Array(values).flatten.length != Array(values).length

        #implementation stolen from @jcromartie https://gist.github.com/jcromartie/1367091
        @ticks = %w[▁ ▂ ▃ ▄ ▅ ▆ ▇]
        values = values.map do |x|
          case x
          when TrueClass
            1
          when FalseClass
            0
          else
            begin
              x.to_f
            rescue NoMethodError
              0
            end
          end
        end
        min = values.min
        range = values.max - values.min
        scale = @ticks.length - 1

        # Guard lists of length 1 or repeating vals
        range = 1.0 if range.to_f == 0.0

        values.map {|x|
          @ticks[(((x - min) / range) * scale).round]
        }.join
      end
      doc name:           :spark_graph,
          introduced:     Version.new(2,5,0),
          summary:        "Returns a string representing a list of numeric values as a spark graph/bar chart",
          args:           [],
          opts:           nil,
          accepts_block:  false,
          doc:            "Given a list of numeric values, this method turns them into a string of bar heights. Useful for quickly graphing the shape of an array. Remember to use puts so you can see the output. See `spark` for a simple way of printing a spark graph.",
      examples:           [
  "puts (spark_graph (range 1, 5))    #=> ▁▃▅█",
  "puts (spark_graph (range 1, 5).shuffle) #=> ▃█▅▁"
      ]




      def spark(*values)
        puts spark_graph(*values)
      end
      doc name:           :spark,
          hide:           false,
          introduced:     Version.new(2,5,0),
          summary:        "Print a string representing a list of numeric values as a spark graph/bar chart",
          args:           [],
          opts:           nil,
          accepts_block:  false,
          doc:            "Given a list of numeric values, this method turns them into a string of bar heights and prints them out. Useful for quickly graphing the shape of an array.",
          examples:       [
  "spark (range 1, 5))    #=> ▁▃▅█",
  "spark (range 1, 5).shuffle) #=> ▃█▅▁"
      ]




      def defonce(name, *opts, &block)
        raise "defonce must be called with a do/end block" unless block
        args_h = resolve_synth_opts_hash_or_array(opts)
        if args_h[:override] || !(@user_methods.method_defined? name)
          val = block.yield
          val_block = lambda{val}
          define(name, &val_block)
          __info "Evaluating defonce #{name}"
        else
          __info "Not re-evaluating defonce #{name}"
        end
      end
      doc name:           :defonce,
          introduced:     Version.new(2,0,0),
          summary:        "Define a named value only once",
          args:           [[:name, :symbol]],
          opts:           {:override => "If set to true, re-definitions are allowed and this acts like define"},
          accepts_block:  true,
          requires_block: true,
          doc:            "Allows you to assign the result of some code to a name, with the property that the code will only execute once - therefore stopping re-definitions. This is useful for defining values that you use in your compositions but you don't want to reset every time you press run. You may force the block to execute again regardless of whether or not it has executed once already by using the override option (see examples).",
          examples:       ["

  defonce :foo do  # Define a new function called foo
    sleep 1        # Sleep for a beat in the function definition. Note that this amount
                   # of time in seconds will depend on the current BPM of the live_loop
                   # or thread calling this function.
    puts \"hello\" # Print hello
    10             # Return a value of 10
  end

  # Call foo on its own
  puts foo # The run sleeps for a beat and prints \"hello\" before returning 10

  # Try it again:
  puts foo # This time the run doesn't sleep or print anything out. However, 10 is still returned.



  defonce :foo do # Try redefining foo
    puts \"you can't redefine me\"
    15
  end

  puts foo # We still don't see any printing or sleeping, and the result is still 10

  # You can use foo anywhere you would use normal code.
  # For example, in a block:
  3.times do
    play foo  # play 10
  end",

  "
  defonce :bar do
    50
  end

  play bar # plays 50

  defonce :bar do # This redefinition doesn't work due to the behaviour of defonce
    70
  end

  play bar # Still plays 50

  defonce :bar, override: true do  # Force definition to take place with override option
    80
  end

  play bar # plays 80"]




      def ndefine(name, &block)
        # do nothing!
      end
      doc name:           :ndefine,
          introduced:     Version.new(2,1,0),
          summary:        "Define a new function",
          args:           [[:name, :symbol]],
          opts:           nil,
          accepts_block:  true,
          requires_block: true,
          doc:            "Does nothing. Use to stop a define from actually defining. Simpler than wrapping whole define in a comment block or commenting each individual line out.",
          examples:       []




      def define(name, &block)
        raise "define must be called with a do/end block" unless block
        already_defined = @user_methods.method_defined? name

        if !already_defined && self.respond_to?(name)
          raise "A function called #{name} is already part of Sonic Pi's core API. Please choose another name."
        end

        if already_defined
          __info "Redefining fn #{name.inspect}"
        else
          __info "Defining fn #{name.inspect}"
        end
        @user_methods.send(:define_method, name, &block)
      end
      doc name:           :define,
          introduced:     Version.new(2,0,0),
          summary:        "Define a new function",
          args:           [[:name, :symbol]],
          opts:           nil,
          accepts_block:  true,
          requires_block: true,
          intro_fn:       true,
          doc:            "Allows you to group a bunch of code and give it your own name for future re-use. Functions are very useful for structuring your code. They are also the gateway into live coding as you may redefine a function whilst a thread is calling it, and the next time the thread calls your function, it will use the latest definition.",
          examples:       ["
  # Define a new function called foo
  define :foo do
    play 50
    sleep 1
  end

  # Call foo on its own
  foo

  # You can use foo anywhere you would use normal code.
  # For example, in a block:
  3.times do
    foo
  end",]




      # def on_keypress(&block)
      #   @keypress_handlers[:foo] = block
      # end
      # doc name:           :on_keypress,
      #     summary:        "",
      #     args:           [],
      #     opts:           nil,
      #     accepts_block:  true,
      #     doc:            "",
      #     examples:       [],
      #     hide:           true




      def comment(*args, &block)
        raise "comment requires a block." unless block
        #do nothing!
      end
      doc name:           :comment,
          introduced:     Version.new(2,0,0),
          summary:        "Block level commenting",
          args:           [],
          opts:           nil,
          accepts_block:  true,
          requires_block: true,
          doc:            "Does not evaluate any of the code within the block. However, any optional args passed before the block *will* be evaluated although they will be ignored. See `uncomment` for switching commenting off without having to remove the comment form.",
          examples:       ["
  comment do # starting a block level comment:
    play 50 # not played
    sleep 1 # no sleep happens
    play 62 # not played
  end"]




      def uncomment(*args, &block)
        raise "uncomment requires a block." unless block
        block.call
      end
      doc name:           :uncomment,
          introduced:     Version.new(2,0,0),
          summary:        "Block level comment ignoring",
          args:           [],
          opts:           nil,
          accepts_block:  true,
          requires_block: true,
          doc:            "Evaluates all of the code within the block. Use to reverse the effect of the comment without having to explicitly remove it.",
          examples:       ["
  uncomment do # starting a block level comment:
    play 50 # played
    sleep 1 # sleep happens
    play 62 # played
  end"]




      def print(*msgs)
        output = msgs.map{|m| m.inspect}.join(" ")
        __delayed_user_message output
      end
      doc name:          :print,
          introduced:     Version.new(2,0,0),
          summary:       "Display a message in the output pane",
          args:          [[:output, :anything]],
          opts:          nil,
          accepts_block: false,
          intro_fn:       true,
          doc:           "Displays the information you specify as a string inside the output pane. This can be a number, symbol, or a string itself. Useful for debugging. Synonym for `puts`.",
          examples:      [
  "print \"hello there\"   #=> will print the string \"hello there\" to the output pane",
  "print 5               #=> will print the number 5 to the output pane",
  "print foo             #=> will print the contents of foo to the output pane"]




      def puts(*msgs)
        output = msgs.map{|m| m.inspect}.join(" ")
        __delayed_user_message output
      end
      doc name:           :puts,
          introduced:     Version.new(2,0,0),
          summary:        "Display a message in the output pane",
          args:           [[:output, :anything]],
          opts:           nil,
          accepts_block:  false,
          intro_fn:       true,
          doc:            "Displays the information you specify as a string inside the output pane. This can be a number, symbol, or a string itself. Useful for debugging. Synonym for `print`.",
          examples:      [
  "print \"hello there\"   #=> will print the string \"hello there\" to the output pane",
  "print 5               #=> will print the number 5 to the output pane",
  "print foo             #=> will print the contents of foo to the output pane"]




      def vt
        __current_local_run_time
      end
      doc name:           :vt,
          introduced:     Version.new(2,1,0),
          summary:        "Get virtual time",
          args:           [],
          opts:           nil,
          accepts_block:  false,
          doc:            "Get the virtual time of the current thread.",
          examples:      ["
  puts vt # prints 0
   sleep 1
   puts vt # prints 1"]




      def factor?(val, factor)
        return false if factor == 0
        (val % factor) == 0
      end
      doc name:           :factor?,
          introduced:     Version.new(2,1,0),
          summary:        "Factor test",
          args:           [[:val, :number], [:factor, :number]],
          opts:           nil,
          accepts_block:  false,
          doc:            "Test to see if factor is indeed a factor of `val`. In other words, can `val` be divided exactly by factor.",
          examples:       [
  "
  factor?(10, 2) # true - 10 is a multiple of 2 (2 * 5 = 10)
  ",
  "
  factor?(11, 2) #false - 11 is not a multiple of 2
  ",
  "
  factor?(2, 0.5) #true - 2 is a multiple of 0.5 (0.5 * 4 = 2) "
      ]




      def quantise(n, step)
        raise "quantisation step resolution should be positive" if step <= 0
        (n.to_f / step).round * step
      end
      doc name:           :quantise,
          introduced:     Version.new(2,1,0),
          summary:        "Quantise a value to resolution",
          args:           [[:n, :number], [:step, :positive_number]],
          opts:           nil,
          accepts_block:  false,
          doc:            "Round value to the nearest multiple of step resolution.",
          examples:        [
  "
  quantise(10, 1) # 10 is already a multiple of 1, so returns 10" ,
  "
  quantise(10, 1.1) # Returns 9.9 which is 1.1 * 9",
  "
  quantise(13.3212, 0.1) # 13.3",
  "
  quantise(13.3212, 0.2) # 13.4",
  "
  quantise(13.3212, 0.3) # 13.2",
  "
  quantise(13.3212, 0.5) # 13.5"]




      def dice(num_sides=6)
        rrand_i(1, num_sides)
      end
      doc name:           :dice,
          introduced:     Version.new(2,0,0),
          summary:        "Random dice throw",
          args:           [[:num_sides, :number]],
          opts:           nil,
          accepts_block:  false,
          doc:            "Throws a dice with the specified num_sides (defaults to `6`) and returns the score as a number between `1` and `num_sides`.",
          examples:      ["
  dice # will return a number between 1 and 6 inclusively
       # (with an even probability distribution).",
  "
  dice 3 # will return a number between 1 and 3 inclusively"]




      def one_in(num)
        num = num.to_i
        if num < 1
          false
        else
          rrand_i(1, num) == 1
        end
      end
      doc name:           :one_in,
          introduced:     Version.new(2,0,0),
          summary:        "Random true value with specified probability",
          args:           [[:num, :number]],
          opts:           nil,
          accepts_block:  false,
          doc:            "Returns `true` or `false` with a specified probability - it will return true every one in num times where num is the param you specify",
          examples:       ["
  one_in 2 # will return true with a probability of 1/2, false with probability 1/2",
  "
  one_in 3 # will return true with a probability of 1/3, false with a probability of 2/3",
  "
  one_in 100 # will return true with a probability of 1/100, false with a probability of 99/100"]




      def rdist(width, centre=0, *opts)
        rrand(centre - width, centre + width, *opts)
      end
      doc name:           :rdist,
          introduced:     Version.new(2,3,0),
          summary:        "Random number in centred distribution",
          args:           [[:width, :number], [:centre, :number]],
          alt_args:       [[:width, :number]],
          opts:           {:step => "Step size of value to quantise to."},
          accepts_block:  false,
          doc:            "Returns a random number within the range with width around centre. If optional arg `step:` is used, the result is quantised by step.",
          examples:       [
  "
  print rdist(1, 0) #=> will print a number between -1 and 1
  ",
  "
  print rdist(1) #=> centre defaults to 0 so this is the same as rdist(1, 0)
  ",
  "
  loop do
    play :c3, pan: rdist(1) #=> Will play :c3 with random L/R panning
    sleep 0.125
  end"]




      def rrand(min, max, *opts)
        args_h = resolve_synth_opts_hash_or_array(opts)
        res = args_h[:step]
        if min == max
          if res
            return quantise(min, res)
          else
            return min
          end
        end

        range = (min - max).abs
        r = SonicPi::Core::SPRand.rand!(range)
        smallest = [min, max].min

        if res
          return quantise((r + smallest), res)
        else
          r + smallest
        end
      end
      doc name:           :rrand,
          introduced:     Version.new(2,0,0),
          summary:        "Generate a random float between two numbers",
          args:           [[:min, :number], [:max, :number]],
          opts:           {:step => "Step size of value to quantise to."},
          accepts_block:  false,
          intro_fn:       true,
          doc:            "Given two numbers, this produces a float between the supplied min and max values exclusively. Both min and max need to be supplied. For random integers, see `rrand_i`. If optional arg `step:` is used, the result is quantised by step.",
          examples:       ["
  print rrand(0, 10) #=> will print a number like 8.917730007820797 to the output pane",
  "
  loop do
    play rrand(60, 72) #=> Will play a random non-integer midi note between C4 (60) and C5 (72) such as 67.3453 or 71.2393
    sleep 0.125
  end"]




      def rrand_i(min, max)
        return min if min == max
        range = (min - max).abs
        r = SonicPi::Core::SPRand.rand_i!(range.to_i + 1)
        smallest = [min, max].min
        (r + smallest)
      end
      doc name:           :rrand_i,
          introduced:     Version.new(2,0,0),
          summary:        "Generate a random whole number between two points inclusively",
          args:           [[:min, :number], [:max, :number]],
          opts:           nil,
          accepts_block: false,
          doc:            "Given two numbers, this produces a whole number between the min and max you supplied inclusively. Both min and max need to be supplied. For random floats, see `rrand`",
          examples:      ["
  print rrand_i(0, 10) #=> will print a random number between 0 and 10 (e.g. 4, 0 or 10) to the output pane",
  "
  loop do
    play rrand_i(60, 72) #=> Will play a random midi note between C4 (60) and C5 (72)
    sleep 0.125
  end"]




      def rand(max=1)
        return 0.0 if max == 0
        if max.is_a?(Range)
          rrand(max.min, max.max)
        else
          SonicPi::Core::SPRand.rand!(max)
        end
      end
      doc name:           :rand,
          introduced:     Version.new(2,0,0),
          summary:        "Generate a random float below a value",
          args:           [[:max, :number_or_range]],
          opts:           nil,
          accepts_block:  false,
          intro_fn:       true,
          doc:            "Given a max number, produces a float between `0` and the supplied max value. If max is a range, produces a float within the range. With no args returns a random value between `0` and `1`.",
          examples:       ["
  print rand(0.5) #=> will print a number like 0.375030517578125 to the output pane"]




      def rand_i(max=2)
        return 0 if max == 0
        if max.is_a?(Range)
          rrand_i(max.min, max.max)
        else
          SonicPi::Core::SPRand.rand_i!(max)
        end
      end
      doc name:           :rand_i,
          introduced:     Version.new(2,0,0),
          summary:        "Generate a random whole number below a value (exclusive)",
          args:           [[:max, :number_or_range]],
          opts:           nil,
          accepts_block:  false,
          doc:            "Given a max number, produces a whole number between `0` and the supplied max value exclusively. If max is a range produces an int within the range. With no args returns either `0` or `1`",
          examples:       ["
  print rand_i(5) #=> will print either 0, 1, 2, 3, or 4 to the output pane"]


      def rand_look(*args)
        rand(*args)
        rand_back
      end
      doc name:           :rand_look,
          introduced:     Version.new(2,11,0),
          summary:        "Generate a random number without consuming a rand",
          args:           [[:max, :number_or_range]],
          opts:           nil,
          accepts_block:  false,
          doc:            "Given a max number, produces a number between `0` and the supplied max value exclusively. If max is a range produces an int within the range. With no args returns a value between `0` and `1`.

Does not consume a random value from the stream. Therefore, multiple sequential calls to `rand_look` will all return the same value.",
          examples:       ["
  print rand_look(0.5) #=> will print a number like 0.375030517578125 to the output pane",

        "
  print rand_look(0.5) #=> will print a number like 0.375030517578125 to the output pane
  print rand_look(0.5) #=> will print the same number again
  print rand_look(0.5) #=> will print the same number again
  print rand_(0.5) #=> will print a different random number
  print rand_look(0.5) #=> will print the same number as the prevoius line again."
      ]




      def rand_i_look(*args)
        rand_i(*args)
        rand_back
      end
      doc name:           :rand_i_look,
          introduced:     Version.new(2,11,0),
          summary:        "Generate a random whole number without consuming a rand",
          args:           [[:max, :number_or_range]],
          opts:           nil,
          accepts_block:  false,
          doc:            "Given a max number, produces a whole number between `0` and the supplied max value exclusively. If max is a range produces an int within the range. With no args returns either `0` or `1`.

Does not consume a random value from the stream. Therefore, multiple sequential calls to `rand_i_look` will all return the same value.",
          examples:       ["
print rand_i_look(5) #=> will print either 0, 1, 2, 3, or 4 to the output pane",

        "
print rand_i_look(5) #=> will print either 0, 1, 2, 3, or 4 to the output pane
print rand_i_look(5) #=> will print the same number again
print rand_i_look(5) #=> will print the same number again
print rand_i(5) #=> will print either 0, 1, 2, 3, or 4 to the output pane
print rand_i_look(5) #=> will print the same number as the previous statement"
      ]




      def rand_back(amount=1)
        SonicPi::Core::SPRand.dec_idx!(amount)
        SonicPi::Core::SPRand.rand_peek
      end
      doc name:           :rand_back,
          introduced:     Version.new(2,7,0),
          summary:        "Roll back random generator",
          args:           [[:amount, :number]],
          opts:           nil,
          accepts_block:  false,
          doc:            "Roll the random generator back essentially 'undoing' the last call to `rand`. You may specify an amount to roll back allowing you to skip back n calls to `rand`.",
          examples:       ["
  # Basic rand stream rollback

  puts rand # prints 0.75006103515625

  rand_back # roll random stream back one
            # the result of the next call to rand will be
            # exactly the same as the previous call

  puts rand # prints 0.75006103515625 again!
  puts rand # prints 0.733917236328125",
  "
  # Jumping back multiple places in the rand stream

  puts rand # prints 0.75006103515625
  puts rand # prints 0.733917236328125
  puts rand # prints 0.464202880859375
  puts rand # prints 0.24249267578125

  rand_back(3) # roll random stream back three places
               # the result of the next call to rand will be
               # exactly the same as the result 3 calls to
               # rand ago.

  puts rand # prints  0.733917236328125 again!
  puts rand # prints  0.464202880859375"]




      def rand_skip(amount=1)
        SonicPi::Core::SPRand.inc_idx!(amount)
        SonicPi::Core::SPRand.rand_peek
      end
      doc name:           :rand_skip,
          introduced:     Version.new(2,7,0),
          summary:        "Jump forward random generator",
          args:           [[:amount, :number]],
          opts:           nil,
          accepts_block:  false,
          doc:            "Jump the random generator forward essentially skipping the next call to `rand`. You may specify an amount to jump allowing you to skip n calls to `rand`.",
          examples:       ["
  # Basic rand stream skip

  puts rand # prints 0.75006103515625

  rand_skip # jump random stream forward one
            # typically the next rand is 0.733917236328125

  puts rand # prints 0.464202880859375",
  "
  # Jumping forward multiple places in the rand stream

  puts rand # prints 0.75006103515625
  puts rand # prints 0.733917236328125
  puts rand # prints 0.464202880859375
  puts rand # prints 0.24249267578125

  rand_reset  # reset the random stream

  puts rand # prints 0.75006103515625

  rand_skip(2) # jump random stream forward three places
               # the result of the next call to rand will be
               # exactly the same as if rand had been called
               # three times

  puts rand 0.24249267578125"]




      def rand_reset
        SonicPi::Core::SPRand.set_idx!(0)
      end
      doc name:           :rand_reset,
          introduced:     Version.new(2,7,0),
          summary:        "Reset rand generator to last seed",
          args:           [[]],
          opts:           nil,
          accepts_block:  false,
          doc:            "Resets the random stream to the last specified seed. See `use_random_seed` for changing the seed.",
          examples:       ["
  puts rand # prints 0.75006103515625
  puts rand # prints 0.733917236328125
  puts rand # prints 0.464202880859375
  puts rand # prints 0.24249267578125
  rand_reset  # reset the random stream
  puts rand # prints 0.75006103515625
  "]




      def shuffle(list)
        return list.shuffle if list.respond_to? :shuffle
        list.to_a.shuffle
      end
      doc name:           :shuffle,
          introduced:     Version.new(2,1,0),
          summary:        "Randomise order of a list",
          args:           [[:list, :array]],
          opts:           nil,
          accepts_block:  false,
          doc:            "Returns a new list with the same elements as the original but with their order shuffled. Also works for strings",
          examples:       [
        "
  shuffle [1, 2, 3, 4] #=> Would return something like: [3, 4, 2, 1] ",
        "
  shuffle \"foobar\"  #=> Would return something like: \"roobfa\""    ]




      def use_random_seed(seed, &block)
        raise "use_random_seed does not work with a block. Perhaps you meant with_random_seed" if block
        __thread_locals.set :sonic_pi_spider_new_thread_random_gen_idx, 0

        SonicPi::Core::SPRand.set_seed! seed
      end
      doc name:          :use_random_seed,
          introduced:    Version.new(2,0,0),
          summary:       "Set random seed generator to known seed",
          doc:           "Resets the random number generator to the specified seed. All subsequently generated random numbers and randomisation functions such as `shuffle` and `choose` will use this new generator and the current generator is discarded. Use this to change the sequence of random numbers in your piece in a way that can be reproduced. Especially useful if combined with iteration. See examples.",
          args:          [[:seed, :number]],
          opts:          nil,
          accepts_block: false,
          examples:      ["
  ## Basic usage

  use_random_seed 1 # reset random seed to 1
  puts rand # => 0.417022004702574
  use_random_seed 1 # reset random seed back to 1
  puts rand  #=> 0.417022004702574
  ",
  "
  ## Generating melodies
  notes = (scale :eb3, :minor_pentatonic)  # Create a set of notes to choose from.
                                           # Scales work well for this

  with_fx :reverb do
    live_loop :repeating_melody do         # Create a live loop

      use_random_seed 300                  # Set the random seed to a known value every
                                           # time around the loop. This seed is the key
                                           # to our melody. Try changing the number to
                                           # something else. Different numbers produce
                                           # different melodies

      8.times do                           # Now iterate a number of times. The size of
                                           # the iteration will be the length of the
                                           # repeating melody.

        play notes.choose, release: 0.1    # 'Randomly' choose a note from our ring of
                                           # notes. See how this isn't actually random
                                           # but uses a reproducible method! These notes
                                           # are therefore repeated over and over...
        sleep 0.125
      end
    end
  end
  "  ]




      def with_random_seed(seed, &block)
        raise "with_random_seed requires a block. Perhaps you meant use_random_seed" unless block
        new_thread_gen_idx = __thread_locals.get :sonic_pi_spider_new_thread_random_gen_idx

        current_seed, current_idx = SonicPi::Core::SPRand.get_seed_and_idx
        SonicPi::Core::SPRand.set_seed! seed
        __thread_locals.set :sonic_pi_spider_new_thread_random_gen_idx, 0
        res = block.call
        SonicPi::Core::SPRand.set_seed! current_seed, current_idx
        __thread_locals.set :sonic_pi_spider_new_thread_random_gen_idx, new_thread_gen_idx
        res
      end
      doc name:           :with_random_seed,
          introduced:     Version.new(2,0,0),
          summary:        "Specify random seed for code block",
          doc:            "Resets the random number generator to the specified seed for the specified code block. All generated random numbers and randomisation functions such as `shuffle` and `choose` within the code block will use this new generator. Once the code block has completed, the original generator is restored and the code block generator is discarded. Use this to change the sequence of random numbers in your piece in a way that can be reproduced. Especially useful if combined with iteration. See examples.",
          args:           [[:seed, :number]],
          opts:           nil,
          accepts_block:  true,
          requires_block: true,
          examples:      ["
  use_random_seed 1 # reset random seed to 1
  puts rand # => 0.417022004702574
  puts rand  #=> 0.7203244934421581
  use_random_seed 1 # reset it back to 1
  puts rand # => 0.417022004702574
  with_random_seed 1 do # reset seed back to 1 just for this block
    puts rand # => 0.417022004702574
    puts rand #=> 0.7203244934421581
  end
  puts rand # => 0.7203244934421581
            # notice how the original generator is restored",
  "
  ## Generating melodies
  notes = (scale :eb3, :minor_pentatonic, num_octaves: 2)  # Create a set of notes to choose from.
                                           # Scales work well for this

  with_fx :reverb do
    live_loop :repeating_melody do         # Create a live loop

      with_random_seed 300 do              # Set the random seed to a known value every
                                           # time around the loop. This seed is the key
                                           # to our melody. Try changing the number to
                                           # something else. Different numbers produce
                                           # different melodies

        8.times do                         # Now iterate a number of times. The size of
                                           # the iteration will be the length of the
                                           # repeating melody.

          play notes.choose, release: 0.1  # 'Randomly' choose a note from our ring of
                                           # notes. See how this isn't actually random
                                           # but uses a reproducible method! These notes
                                           # are therefore repeated over and over...
          sleep 0.125
        end
      end

      play notes.choose, amp: 1.5, release: 0.5 # Note that this line is outside of
                                                # the with_random_seed block and therefore
                                                # the randomisation never gets reset and this
                                                # part of the melody never repeats.
    end
  end
  "
      ]




      # Give a deprecation warning to users coming from v1.0
      def with_tempo(*args, &block)
        raise "The function with_tempo is deprecated since v2.0. Please consider use_bpm or with_bpm."
      end


      def use_cue_logging(v, &block)
        raise "use_cue_logging does not work with a do/end block. Perhaps you meant with_cue_logging" if block
        __thread_locals.set(:sonic_pi_suppress_cue_logging, !v)
      end
      doc name:          :use_cue_logging,
          introduced:    Version.new(2,6,0),
          summary:       "Enable and disable cue logging",
          doc:           "Enable or disable log messages created on cues. This does not disable the cues themselves, it just stops them from being printed to the log",
          args:          [[:true_or_false, :boolean]],
          opts:          nil,
          accepts_block: false,
          examples:      ["use_cue_logging true # Turn on cue messages", "use_cue_logging false # Disable cue messages"]




      def with_cue_logging(v, &block)
        raise "with_cue_logging requires a do/end block. Perhaps you meant use_cue_logging" unless block
        current = __thread_locals.get(:sonic_pi_suppress_cue_logging)
        __thread_locals.set(:sonic_pi_suppress_cue_logging, !v)
        block.call
        __thread_locals.set(:sonic_pi_suppress_cue_logging, current)
      end
      doc name:          :with_cue_logging,
          introduced:    Version.new(2,6,0),
          summary:       "Block-level enable and disable cue logging",
          doc:           "Similar to use_cue_logging except only applies to code within supplied `do`/`end` block. Previous cue log value is restored after block.",
          args:          [[:true_or_false, :boolean]],
          opts:          nil,
          accepts_block: true,
          requires_block: true,
          examples:      ["
  # Turn on debugging:
  use_cue_logging true

  cue :foo # cue message is printed to log

  with_cue_logging false do
    #Cue logging is now disabled
    cue :bar # cue *is* sent but not displayed in log
  end
  sleep 1
  # Debug is re-enabled
  cue :quux # cue is displayed in log
  "]






      def use_bpm(bpm, &block)
        raise "use_bpm does not work with a block. Perhaps you meant with_bpm" if block
        raise "use_bpm's BPM should be a positive value. You tried to use: #{bpm}" unless bpm > 0
        sleep_mul = 60.0 / bpm
        __thread_locals.set(:sonic_pi_spider_sleep_mul, sleep_mul)
      end
      doc name:           :use_bpm,
          introduced:     Version.new(2,0,0),
          summary:        "Set the tempo",
          doc:            "Sets the tempo in bpm (beats per minute) for everything afterwards. Affects all subsequent calls to `sleep` and all temporal synth arguments which will be scaled to match the new bpm. If you wish to bypass scaling in calls to sleep, see the fn `rt`. Also, if you wish to bypass time scaling in synth args see `use_arg_bpm_scaling`. See also `with_bpm` for a block scoped version of `use_bpm`.

  For dance music here's a rough guide for which BPM to aim for depending on your genre:

  * Dub: 60-90 bpm
  * Hip-hop: 60-100 bpm
  * Downtempo: 90-120 bpm
  * House: 115-130 bpm
  * Techno/trance: 120-140 bpm
  * Dubstep: 135-145 bpm
  * Drum and bass: 160-180 bpm",
          args:           [[:bpm, :number]],
          opts:           nil,
          accepts_block:  false,
          intro_fn:       true,
          examples:       ["
  # default tempo is 60 bpm
  4.times do
    play 50, attack: 0.5, release: 0.25 # attack is 0.5s and release is 0.25s
    sleep 1 # sleep for 1 second
  end

  sleep 2  # sleep for 2 seconds

  # Let's make it go faster...
  use_bpm 120  # double the bpm
  4.times do
    play 62, attack: 0.5, release: 0.25 # attack is scaled to 0.25s and release is now 0.125s
    sleep 1 # actually sleeps for 0.5 seconds
  end

  sleep 2 # sleep for 1 second

  # Let's make it go even faster...
  use_bpm 240  #  bpm is 4x original speed!
  8.times do
    play 62, attack: 0.5, release: 0.25 # attack is scaled to 0.125s and release is now 0.0625s
    sleep 1 # actually sleeps for 0.25 seconds
  end

  "]




      def with_bpm(bpm, &block)
        raise "with_bpm must be called with a do/end block. Perhaps you meant use_bpm" unless block
        raise "with_bpm's BPM should be a positive value. You tried to use: #{bpm}" unless bpm > 0
        current_mul = __thread_locals.get(:sonic_pi_spider_sleep_mul)
        sleep_mul = 60.0 / bpm
        __thread_locals.set(:sonic_pi_spider_sleep_mul, sleep_mul)
        res = block.call
        __thread_locals.set(:sonic_pi_spider_sleep_mul, current_mul)
        res
      end
      doc name:           :with_bpm,
          introduced:     Version.new(2,0,0),
          summary:        "Set the tempo for the code block",
          doc:            "Sets the tempo in bpm (beats per minute) for everything in the given block. Affects all containing calls to `sleep` and all temporal synth arguments which will be scaled to match the new bpm. See also `use_bpm`

  For dance music here's a rough guide for which BPM to aim for depending on your genre:

  * Dub: 60-90 bpm
  * Hip-hop: 60-100 bpm
  * Downtempo: 90-120 bpm
  * House: 115-130 bpm
  * Techno/trance: 120-140 bpm
  * Dubstep: 135-145 bpm
  * Drum and bass: 160-180 bpm
  ",
          args:           [[:bpm, :number]],
          opts:           nil,
          accepts_block:  true,
          requires_block: true,
          examples:       ["
  # default tempo is 60 bpm
  4.times do
    sample :drum_bass_hard
    sleep 1 # sleeps for 1 second
  end

  sleep 5 # sleeps for 5 seconds

  # with_bpm sets a tempo for everything between do ... end (a block)
  # Hear how it gets faster?
  with_bpm 120 do  # set bpm to be twice as fast
    4.times do
      sample :drum_bass_hard
      sleep 1 # now sleeps for 0.5 seconds
    end
  end

  sleep 5

  # bpm goes back to normal
  4.times do
    sample :drum_bass_hard
    sleep 1 # sleeps for 1 second
  end"]




      def with_bpm_mul(mul, &block)
        raise "with_bpm_mul must be called with a do/end block. Perhaps you meant use_bpm_mul" unless block
        raise "with_bpm_mul's mul should be a positive value. You tried to use: #{mul}" unless mul > 0
        current_mul = __thread_locals.get(:sonic_pi_spider_sleep_mul)
        new_mul = current_mul.to_f / mul
        __thread_locals.set(:sonic_pi_spider_sleep_mul, new_mul)
        res = block.call
        __thread_locals.set(:sonic_pi_spider_sleep_mul, current_mul)
        res
      end
      doc name:           :with_bpm_mul,
          introduced:     Version.new(2,3,0),
          summary:        "Set new tempo as a multiple of current tempo for block",
          doc:            "Sets the tempo in bpm (beats per minute) for everything in the given block as a multiplication of the current tempo. Affects all containing calls to `sleep` and all temporal synth arguments which will be scaled to match the new bpm. See also `with_bpm`",
          args:           [[:mul, :number]],
          opts:           nil,
          accepts_block:  true,
          requires_block: true,
          examples:       ["
  use_bpm 60   # Set the BPM to 60
  play 50
  sleep 1      # Sleeps for 1 second
  play 62
  sleep 2      # Sleeps for 2 seconds
  with_bpm_mul 0.5 do # BPM is now (60 * 0.5) == 30
    play 50
    sleep 1           # Sleeps for 2 seconds
    play 62
  end
  sleep 1            # BPM is now back to 60, therefore sleep is 1 second
  "]




      def use_bpm_mul(mul, &block)
        raise "use_bpm_mul must not be called with a block. Perhaps you meant with_bpm_mul" if block
        raise "use_bpm_mul's mul should be a positive value. You tried to use: #{mul}" unless mul > 0
        current_mul = __thread_locals.get(:sonic_pi_spider_sleep_mul)
        new_mul = current_mul.to_f / mul
        __thread_locals.set(:sonic_pi_spider_sleep_mul, new_mul)
      end
      doc name:           :use_bpm_mul,
          introduced:     Version.new(2,3,0),
          summary:        "Set new tempo as a multiple of current tempo",
          doc:            "Sets the tempo in bpm (beats per minute) as a multiplication of the current tempo. Affects all containing calls to `sleep` and all temporal synth arguments which will be scaled to match the new bpm. See also `use_bpm`",
          args:           [[:mul, :number]],
          opts:           nil,
          accepts_block:  false,
          examples:       ["
  use_bpm 60   # Set the BPM to 60
  play 50
  sleep 1      # Sleeps for 1 seconds
  play 62
  sleep 2      # Sleeps for 2 seconds
  use_bpm_mul 0.5 # BPM is now (60 * 0.5) == 30
  play 50
  sleep 1           # Sleeps for 2 seconds
  play 62
  "]




      def density(d, &block)
        raise "density must be called with a do/end block." unless block
        raise "density must be a positive number. Got: #{d.inspect}." unless d.is_a?(Numeric) && d > 0
        reps = d < 1 ? 1.0 : d
        with_bpm_mul d do
          if block.arity == 0
            reps.times do
              block.call
            end
          else
            reps.times do |idx|
              block.call idx
            end
          end
        end
      end
      doc name:           :density,
          introduced:     Version.new(2,3,0),
          summary:        "Squash and repeat time",
          doc:            "Runs the block `d` times with the bpm for the block also multiplied by `d`. Great for repeating sections a number of times faster yet keeping within a fixed time. If `d` is less than 1, then time will be stretched accordingly and the block will take longer to complete.",
          args:           [[:d, :density]],
          opts:           nil,
          accepts_block:  true,
          examples:       ["
  use_bpm 60   # Set the BPM to 60

  density 2 do       # BPM for block is now 120
                     # block is called 2.times
    sample :bd_haus # sample is played twice
    sleep 0.5        # sleep is 0.25s
  end",

  "
  density 2 do |idx| # You may also pass a param to the block similar to n.times
    puts idx         # prints out 0, 1
    sleep 0.5        # sleep is 0.25s
  end
  ",
  "
  density 0.5 do          # Specifying a density val of < 1 will stretch out time
                          # A density of 0.5 will double the length of the block's
                          # execution time.
    play 80, release: 1   # plays note 80 with 2s release
    sleep 0.5             # sleep is 1s
  end
  "    ]


      def current_random_seed
        SonicPi::Core::SPRand.get_seed_plus_idx
      end
      doc name:          :current_random_seed,
          introduced:    Version.new(2,10,0),
          summary:       "Get current random seed",
          doc:           "Returns the current random seed.

This can be set via the fns `use_random_seed` and `with_random_seed`. It is incremented every time you use the random number generator via fns such as `choose` and `rand`.",
          args:          [],
          opts:          nil,
          accepts_block: false,
          examples:      ["
  puts current_random_seed # Print out the current random seed",
"
## Resetting the seed back to a known place
puts rand               #=>  0.75006103515625
puts rand               #=>  0.733917236328125
a = current_random_seed # Grab the current seed
puts rand               #=> 0.464202880859375
puts rand               #=> 0.24249267578125
use_random_seed a       # Restore the seed
                        # we'll now get the same random values:
puts rand               #=> 0.464202880859375
puts rand               #=> 0.24249267578125
"]


      def current_bpm
        60.0 / __thread_locals.get(:sonic_pi_spider_sleep_mul)
      end
      doc name:          :current_bpm,
          introduced:    Version.new(2,0,0),
          summary:       "Get current tempo",
          doc:           "Returns the current tempo as a bpm value.

This can be set via the fns `use_bpm`, `with_bpm`, `use_sample_bpm` and `with_sample_bpm`.",
          args:          [],
          opts:          nil,
          accepts_block: false,
          examples:      ["
  puts current_bpm # Print out the current bpm"]




      def current_beat_duration
        __thread_locals.get(:sonic_pi_spider_sleep_mul)
      end
      doc name:          :current_beat_duration,
          introduced:    Version.new(2,6,0),
          summary:       "Duration of current beat",
          doc:           "Get the duration of the current beat in seconds. This is the actual length of time which will elapse with `sleep 1`.

Affected by calls to `use_bpm`, `with_bpm`, `use_sample_bpm` and `with_sample_bpm`.",
          args:          [],
          opts:          nil,
          accepts_block: false,
          examples:      ["
  use_bpm 60
  puts current_beat_duration #=> 1

  use_bpm 120
  puts current_beat_duration #=> 0.5"]




      def beat
        __system_thread_locals.get(:sonic_pi_spider_beat)
      end
      doc name:          :beat,
          introduced:    Version.new(2,10,0),
          summary:       "Get current beat",
          doc:           "Returns the beat value for the current thread/live_loop. Beats are advanced only by calls to `sleep` and `sync`. Beats are distinct from virtual time (the value obtained by calling `vt`) in that it has no notion of rate. It is just essentially a counter for sleeps. After a `sync`, the beat is overridden with the beat value from the thread which called `cue`. ",
          args:          [[]],
          opts:          nil,
          accepts_block: false,
          examples:      ["
  use_bpm 120  # The current BPM makes no difference
  puts beat    #=> 0
  sleep 1
  puts beat    #=> 1
  use_bpm 2000
  sleep 2
  puts beat    #=> 3"]




      def rt(t)
        t / __thread_locals.get(:sonic_pi_spider_sleep_mul)
      end
      doc name:          :rt,
          introduced:    Version.new(2,0,0),
          summary:       "Real time conversion",
          doc:           "Real time representation. Returns the amount of beats for the value in real-time seconds. Useful for bypassing any bpm scaling",
          args:          [[:seconds, :number]],
          opts:          nil,
          accepts_block: false,
          examples:      ["
  use_bpm 120  # modifies all time to be half
  play 50
  sleep 1      # actually sleeps for half of a second
  play 62
  sleep rt(1)  # bypasses bpm scaling and sleeps for a second
  play 72"]




      def bt(t)
        t * __thread_locals.get(:sonic_pi_spider_sleep_mul)
      end
      doc name:          :bt,
          introduced:    Version.new(2,8,0),
          summary:       "Beat time conversion",
          doc:           "Beat time representation. Scales the time to the current BPM. Useful for adding bpm scaling",
          args:          [[:seconds, :number]],
          opts:          nil,
          accepts_block: false,
          examples:      ["
  use_bpm 120  # Set the BPM to be double the default
  puts bt(1) # 0.5
  use_bpm 60   # BPM is now default
  puts bt(1) # 1
  use_bpm 30   # BPM is now half the default
  puts bt(1) # 2
"]




      def sleep(beats)
        # Schedule messages
        __schedule_delayed_blocks_and_messages!
        curr_beat = __system_thread_locals.get(:sonic_pi_spider_beat)
        __system_thread_locals.set(:sonic_pi_spider_beat, curr_beat + beats)

        return if beats == 0
        # Grab the current virtual time
        last_vt = __system_thread_locals.get :sonic_pi_spider_time

        # Now get on with syncing the rest of the sleep time...

        # Calculate the amount of time to sleep (take into account current bpm setting)
        sleep_time = beats * __thread_locals.get(:sonic_pi_spider_sleep_mul)
        # Calculate the new virtual time
        new_vt = last_vt + sleep_time

        # TODO: remove this, api shouldn't need to know about sound module
        sat = @mod_sound_studio.sched_ahead_time
        now = Time.now
        if now - (sat + 0.5) > new_vt
          raise "Timing Exception: thread got too far behind time"
        elsif (now - sat) > new_vt
          # TODO: Empirical tests to see what effect this priority stuff
          # actually has on typical workloads

          # Hard warning, system is too far behind, expect timing issues.
          p = Thread.current.priority
          p += 10
          p = 100 if p < 100
          p = 150 if p > 150
          Thread.current.priority = p
          __delayed_serious_warning "Timing error: can't keep up..."
        elsif now > new_vt
          # Soft warning, system should work correctly, but is currently behind
          p = Thread.current.priority
          p += 5
          p = 50 if p < 50
          p = 150 if p > 150
          Thread.current.priority = p
          ## TODO: Remove this and replace with a much better silencing system which
          ## is implemented within the __delayed_* fns
          unless __thread_locals.get(:sonic_pi_mod_sound_synth_silent)
            __delayed_warning "Timing warning: running slightly behind..."
          end
        else
          Kernel.sleep new_vt - now
        end

        __system_thread_locals.set :sonic_pi_spider_time, new_vt.freeze
        ## reset control deltas now that time has advanced
        __system_thread_locals.set_local :sonic_pi_local_control_deltas, {}
      end
      doc name:           :sleep,
          introduced:     Version.new(2,0,0),
          summary:        "Wait for beat duration",
          doc:            "Wait for a number of beats before triggering the next command. Beats are converted to seconds by scaling to the current bpm setting.",
          args:           [[:beats, :number]],
          opts:           nil,
          accepts_block:  false,
          advances_time:  true,
          examples:       ["
  # Without calls to sleep, all sounds would happen at once:

  play 50  # This is actually a chord with all notes played simultaneously
  play 55
  play 62

  sleep 1  # Create a gap, to allow a moment's pause for reflection...

  play 50  # Let's try the chord again, but this time with sleeps:
  sleep 0.5 # With the sleeps, we turn a chord into an arpeggio
  play 55
  sleep 0.5
  play 62",

  "
  # The amount of time sleep pauses for is scaled to match the current bpm. The default bpm is 60. Let's double it:

  use_bpm 120
  play 50
  sleep 1 # This actually sleeps for 0.5 seconds as we're now at double speed
  play 55
  sleep 1
  play 62

  # Let's go down to half speed:

  use_bpm 30
  play 50
  sleep 1 # This now sleeps for 2 seconds as we're now at half speed.
  play 55
  sleep 1
  play 62
  "]




      def wait(time)
        if time.is_a? Symbol
          sync(time)
        else
          sleep(time)
        end
      end
      doc name:           :wait,
          introduced:     Version.new(2,0,0),
          summary:        "Wait for duration",
          doc:            "Synonym for `sleep` - see `sleep`",
          args:           [[:beats, :number]],
          opts:           nil,
          accepts_block:  false,
          advances_time:  true,
          examples:       []




      def cue(cue_id, *opts)
        args_h = resolve_synth_opts_hash_or_array(opts)
        args_h.each do |k, v|
          raise "Invalid cue key type. Must be a Symbol" unless k.is_a? Symbol
          raise "Invalid cue value type (#{v.class}) for key #{k.inspect}. Must be immutable - currently accepted types: Numbers, Symbols, Booleans and Nil, or Vectors/Rings of immutable types" unless v.sp_thread_safe?
        end


        payload = {
          :time => __system_thread_locals.get(:sonic_pi_spider_time),
          :sleep_mul => __thread_locals.get(:sonic_pi_spider_sleep_mul),
          :beat => __system_thread_locals.get(:sonic_pi_spider_beat),
          :run => current_job_id,
          :cue_map => args_h,
          :cue => cue_id
        }

        unless __thread_locals.get(:sonic_pi_suppress_cue_logging)
          if args_h.empty?
            __delayed_highlight_message "cue #{cue_id.inspect}"
          else
            __delayed_highlight_message "cue #{cue_id.inspect}, #{arg_h_pp(args_h)}"
          end
        end

        Thread.new do
          __system_thread_locals.set_local(:sonic_pi_local_thread_group, :cue)
          # sleep for a tiny amount of wall-clock time to give other temporally
          # synced threads real time to register syncs at similar virtual
          # times.
          Kernel.sleep @sync_real_sleep_time
          @events.async_event("/spider_thread_sync/" + cue_id.to_s, payload)
        end
      end
      doc name:           :cue,
          introduced:     Version.new(2,0,0),
          summary:        "Cue other threads",
          doc:            "Send a heartbeat synchronisation message containing the (virtual) timestamp of the current thread. Useful for syncing up external threads via the `sync` fn. Any opts which are passed are given to the thread which syncs on the `cue_id` as a map. The values of the opts must be immutable. Currently only numbers, symbols and booleans are supported.",
          args:           [[:cue_id, :symbol]],
          opts:           {:your_key    => "Your value",
                           :another_key => "Another value",
                           :key         => "All these opts are passed through to the thread which syncs"},
          accepts_block:  false,
          examples:       ["
  in_thread do
    sync :foo # this parks the current thread waiting for a foo cue message to be received.
    sample :ambi_lunar_land
  end

  sleep 5

  cue :foo # We send a cue message from the main thread.
            # This then unblocks the thread above and we then hear the sample",

  "
  in_thread do   # Start a metronome thread
    loop do      # Loop forever:
      cue :tick  # sending tick heartbeat messages
      sleep 0.5  # and sleeping for 0.5 beats between ticks
    end
  end

  # We can now play sounds using the metronome.
  loop do                    # In the main thread, just loop
    sync :tick               # waiting for :tick cue messages
    sample :drum_heavy_kick  # after which play the drum kick sample
  end",

  "
  in_thread do   # Start a metronome thread
    loop do      # Loop forever:
      cue [:foo, :bar, :baz].choose # sending one of three tick heartbeat messages randomly
      sleep 0.5  # and sleeping for 0.5 beats between ticks
    end
  end

  # We can now play sounds using the metronome:

  in_thread do
    loop do              # In the main thread, just loop
      sync :foo          # waiting for :foo cue messages
      sample :elec_beep  # after which play the elec beep sample
    end
  end

  in_thread do
    loop do              # In the main thread, just loop
      sync :bar          # waiting for :bar cue messages
      sample :elec_flip  # after which play the elec flip sample
    end
  end

  in_thread do
    loop do              # In the main thread, just loop
      sync :baz          # waiting for :baz cue messages
      sample :elec_blup  # after which play the elec blup sample
    end
  end",

  "
  in_thread do
    loop do
      cue :tick, foo: 64  # sending tick heartbeat messages with a value :foo
      sleep 0.5
    end
  end

  # The value for :foo can now be used in synced threads

  loop do
    values = sync :tick
    play values[:foo]    # play the note value from :foo
  end",
      ]

      def sync_bpm(cue_ids, opts={})
        sync cue_ids, opts.merge({bpm_sync: true})
      end
      doc name:           :sync_bpm,
          introduced:     Version.new(2,10,0),
          summary:        "Sync and inherit BPM from other threads ",
          doc:            "An alias for `sync` with the `bpm_sync:` opt set to true.",
          args:           [[:cue_id, :symbol]],
          opts:           {},
          accepts_block:  false,
          advances_time:  true,
          examples:       ["See examples for sync"]


      def sync(cue_ids, opts={})
        cue_ids = [cue_ids] if cue_ids.is_a?(Symbol) || cue_ids.is_a?(String) || cue_ids.is_a?(SPSym)
        raise "sync needs at least one cue id to sync on. You specified 0" unless cue_ids.size > 0
        __system_thread_locals.set(:sonic_pi_spider_synced, true)
        p = Promise.new
        handles = cue_ids.map {|id| "/spider_thread_sync/" + id.to_s}
        @events.async_multi_oneshot_handler(handles) do |payload|
          p.deliver! payload
        end

        unless __thread_locals.get(:sonic_pi_suppress_cue_logging)
          if cue_ids.size == 1
            __delayed_highlight3_message "sync #{cue_ids.first.inspect}"
          else
            ids_list = cue_ids.map{|cid| cid.to_sym}
            __delayed_highlight3_message "sync #{ids_list.inspect}"
          end
        end

        __schedule_delayed_blocks_and_messages!

        payload = p.get
        time = payload[:time]
        sleep_mul = payload[:sleep_mul]
        beat = payload[:beat]
        bpm_sync = opts.has_key?(:bpm_sync) ? opts[:bpm_sync] : false
        run_id = payload[:run]
        cue_map = payload[:cue_map]
        cue_map = cue_map.dup if cue_map
        cue_map = cue_map || {}
        cue_id = payload[:cue]
        cue_map[:cue] = cue_id
        __system_thread_locals.set :sonic_pi_spider_beat, beat
        __system_thread_locals.set :sonic_pi_spider_time, time.freeze
        __thread_locals.set(:sonic_pi_spider_sleep_mul, sleep_mul) if bpm_sync


        unless __thread_locals.get(:sonic_pi_suppress_cue_logging)
          if bpm_sync
            __delayed_highlight2_message "synced #{cue_id.inspect}. Inheriting bpm of #{current_bpm} (Run #{run_id})"
          else
            __delayed_highlight2_message "synced #{cue_id.inspect} (Run #{run_id})"
          end
        end
        cue_map
      end
      doc name:           :sync,
          introduced:     Version.new(2,0,0),
          summary:        "Sync with other threads",
          doc:            "Pause/block the current thread until a `cue` heartbeat with a matching `cue_id` is received. When a matching `cue` message is received, unblock the current thread, and continue execution with the virtual time set to match the thread that sent the `cue` heartbeat. The current thread is therefore synced to the `cue` thread. If multiple cue ids are passed as arguments, it will `sync` on the first matching `cue_id`. By default the BPM of the cueing thread is inherited. This can be disabled using the bpm_sync: opt.",
          args:           [[:cue_id, :symbol]],
          opts:           {:bpm_sync => "Inherit the BPM of the cueing thread. Default is false"},
          accepts_block:  false,
          advances_time:  true,
          examples:       ["
  in_thread do
    sync :foo # this parks the current thread waiting for a foo sync message to be received.
    sample :ambi_lunar_land
  end

  sleep 5

  cue :foo # We send a sync message from the main thread.
            # This then unblocks the thread above and we then hear the sample",

  "
  in_thread do   # Start a metronome thread
    loop do      # Loop forever:
      cue :tick # sending tick heartbeat messages
      sleep 0.5  # and sleeping for 0.5 beats between ticks
    end
  end

  # We can now play sounds using the metronome.
  loop do                    # In the main thread, just loop
    sync :tick               # waiting for :tick sync messages
    sample :drum_heavy_kick  # after which play the drum kick sample
  end",

  "
  sync :foo, :bar # Wait for either a :foo or :bar cue ",

  "
  in_thread do   # Start a metronome thread
    loop do      # Loop forever:
      cue [:foo, :bar, :baz].choose # sending one of three tick heartbeat messages randomly
      sleep 0.5  # and sleeping for 0.5 beats between ticks
    end
  end

  # We can now play sounds using the metronome:

  in_thread do
    loop do                    # In the main thread, just loop
      sync :foo               # waiting for :foo sync messages
      sample :elec_beep  # after which play the elec beep sample
    end
  end

  in_thread do
    loop do                    # In the main thread, just loop
      sync :bar               # waiting for :bar sync messages
      sample :elec_flip  # after which play the elec flip sample
    end
  end

  in_thread do
    loop do                    # In the main thread, just loop
      sync :baz               # waiting for :baz sync messages
      sample :elec_blup  # after which play the elec blup sample
    end
  end"]




      def in_thread(*opts, &block)
        args_h = resolve_synth_opts_hash_or_array(opts)
        name = args_h[:name]
        delay = args_h[:delay]
        sync_sym = args_h[:sync]
        sync_bpm_sym = args_h[:sync_bpm]
        sync_sym = nil if sync_bpm_sym

        raise "in_thread's delay: opt must be a number, got #{delay.inspect}" if delay && !delay.is_a?(Numeric)

        parent_t = Thread.current

        # Get copy of thread locals whilst we're sure they're not being modified
        # as we're in the thread parent_t

        job_id = __current_job_id
        reg_with_parent_completed = Promise.new

        if args_h[:seed]
          new_rand_seed = args_h[:seed]
        else
          new_thread_gen_idx = __thread_locals.get :sonic_pi_spider_new_thread_random_gen_idx
          new_rand_seed = SonicPi::Core::SPRand.rand!(441000, new_thread_gen_idx)
          __thread_locals.set :sonic_pi_spider_new_thread_random_gen_idx, new_thread_gen_idx + 1
        end

        new_tls = SonicPi::Core::ThreadLocal.new(__thread_locals, SonicPi::Core::SPRand.tl_seed_map(new_rand_seed + SonicPi::Core::SPRand.get_seed, 0))

        new_system_tls = SonicPi::Core::ThreadLocal.new(__system_thread_locals)

        # Create the new thread
        t = Thread.new do
          # Copy thread locals across from parent thread to this new thread
          __thread_locals_reset!(new_tls)
          __system_thread_locals_reset!(new_system_tls)
          __system_thread_locals.set_local(:sonic_pi_local_thread_group, :job_subthread)

          main_t = Thread.current
          main_t.priority = 10

          Thread.new do
            if name
              __system_thread_locals.set_local(:sonic_pi_local_thread_group, "in_thread_join_#{name}".freeze)
            else
              __system_thread_locals.set_local(:sonic_pi_local_thread_group, :in_thread_join)
            end
            Thread.current.priority = -10
            # wait for all subthreads to finish before removing self from
            # the parent subthread tree
            main_t.join
            __join_subthreads(main_t)

            __system_thread_locals(parent_t).get(:sonic_pi_local_spider_subthread_mutex).synchronize do
              __current_subthreads.delete(main_t)
            end
          end

          __system_thread_locals.set_local :sonic_pi_local_spider_users_thread_name, name if name

          __system_thread_locals.set_local :sonic_pi_local_spider_delayed_blocks, []
          __system_thread_locals.set_local :sonic_pi_local_spider_delayed_messages, []
          __system_thread_locals.set_local :sonic_pi_local_control_deltas, {}


          # Reset subthreads thread local to the empty set. This shouldn't
          # be inherited from the parent thread.
          __system_thread_locals.set_local :sonic_pi_local_spider_subthreads, Set.new

          # Give new thread a new subthread mutex
          __system_thread_locals.set_local :sonic_pi_local_spider_subthread_mutex, Mutex.new

          # Give new thread a new no_kill mutex This reduces contention
          # over the alternative of a global no_kill mutex.  Killing a Run
          # then essentially turns into waiting for each no_kill mutext for
          # every sub-in_thread before killing them.
          __system_thread_locals.set_local :sonic_pi_local_spider_no_kill_mutex, Mutex.new




          # Wait for parent to deliver promise. Throws an exception if
          # parent dies before the promise is delivered, thus stopping
          # this thread from continually waiting for forgotten promises...
          wait_for_parent_thread!(parent_t, reg_with_parent_completed)

          # Attempt to associate the current thread with job with
          # job_id. This will kill the current thread if job is no longer
          # running.
          job_subthread_add(job_id, Thread.current, name)

          # Actually run the thread code specified by the user!
          begin
            sleep delay if delay
            sync sync_sym if sync_sym
            sync_bpm sync_bpm_sym if sync_bpm_sym
            block.call
            # ensure delayed jobs and messages are honoured for this
            # thread:
            __schedule_delayed_blocks_and_messages!
          rescue Stop => e
            __schedule_delayed_blocks_and_messages!
            if name
              __info("Stopping thread #{name.inspect}")
            else
              __delayed_message("Stopped internal thread")
              __schedule_delayed_blocks_and_messages!
            end
          rescue Exception => e
            __schedule_delayed_blocks_and_messages!
            if name
              __error e, "Thread death +--> #{name.inspect}"
            else
              __error e, "Thread death!"
            end

          end

          # Wait for any trackers by blocking on all promises until
          # All have been delivered
          __current_tracker.get

          # Disassociate thread with job as it has now finished
          job_subthread_rm(job_id, Thread.current)
        end

        # Whilst we know that the new thread is waiting on the promise to
        # be delivered, we can now add it to our list of subthreads. Using
        # the promise means that we can be assured that killing this
        # current thread won't create a zombie child thread as the child
        # thread will only continue exiting after it has been sucessfully
        # registered.

        __system_thread_locals(parent_t).get(:sonic_pi_local_spider_subthread_mutex).synchronize do
          subthreads = __system_thread_locals(parent_t).get :sonic_pi_local_spider_subthreads
          subthreads.add(t)
        end

        # Allow the subthread to continue running
        reg_with_parent_completed.deliver! true

        # Return subthread
        t
      end
      doc name:           :in_thread,
          introduced:     Version.new(2,0,0),
          summary:        "Run code block at the same time",
          doc:            "Execute a given block (between `do` ... `end`) in a new thread. Use for playing multiple 'parts' at once. Each new thread created inherits all the use/with defaults of the parent thread such as the time, current synth, bpm, default synth args, etc. Despite inheriting defaults from the parent thread, any modifications of the defaults in the new thread will *not* affect the parent thread. Threads may be named with the `name:` optional arg. Named threads will print their name in the logging pane when they print their activity. If you attempt to create a new named thread with a name that is already in use by another executing thread, no new thread will be created.

It is possible to delay the initial trigger of the thread on creation with both the `delay:` and `sync:` opts. See their respective docstrings. If both `delay:` and `sync:` are specified, on initial thread creation first the delay will be honoured and then the sync.
",
          args:           [],
          opts:           {:name  => "Make this thread a named thread with name. If a thread with this name already exists, a new thread will not be created.",
                           :delay => "Initial delay in beats before the thread starts. Default is 0.",
                           :sync => "Initial sync symbol. Will sync with this symbol before the thread starts.",
                           :sync_bpm => "Initial sync symbol. Will sync with this symbol before the live_loop starts. Live loop will also inherit the BPM of the thread which cued the symbol.",},
          accepts_block:  true,
          requires_block: true,
          async_block:    true,
          examples:       ["
  loop do      # If you write two loops one after another like this,
    play 50    # then only the first loop will execute as the loop acts
    sleep 1    # like a trap not letting the flow of control out
  end

  loop do      # This code is never executed.
    play 55
    sleep 0.5
  end ",

  "

  # In order to play two loops at the same time, the first loops need to
  # be in a thread (note that it's probably more idiomatic to use live_loop
  # when performing):

  # By wrapping our loop in an in_thread block, we split the
  # control flow into two parts. One flows into the loop (a) and
  # the other part flows immediately after the in_thread block (b).
  # both parts of the control flow execute at exactly the same time.

  in_thread do
    # (a)
    loop do
      # (a)
      play 50
      sleep 1
    end
  end

  # (b)

  loop do      # This loop is executed thanks to the thread above
    play 55
    sleep 0.5
  end",

  "
  use_bpm 120  # Set the bpm to be double rate
  use_synth :dsaw  # Set the current synth to be :dsaw

  in_thread do     # Create a new thread
    play 50        # Play note 50 at time 0
    use_synth :fm  # Switch to fm synth (only affects this thread)
    sleep 1        # sleep for 0.5 seconds (as we're double rate)
    play 38        # Play note 38 at time 0.5
  end

  play 62          # Play note 62 at time 0 (with dsaw synth)
  sleep 2          # sleep 1s
  play 67          # Play note 67 at time 1s (also with dsaw synth)
  ",

  "
  in_thread(name: :foo) do # Here we've created a named thread
    loop do
      sample :drum_bass_hard
      sleep 1
    end
  end

  in_thread(name: :foo) do # This thread isn't created as the name is
    loop do                # the same as the previous thread which is
      sample :elec_chime   # still executing.
      sleep 0.5
    end
  end",

  "
   # Named threads work well with functions for live coding:
  define :foo do  # Create a function foo
    play 50       # which does something simple
    sleep 1       # and sleeps for some time
  end

  in_thread(name: :main) do  # Create a named thread
    loop do                  # which loops forever
      foo                    # calling our function
    end
  end

  # We are now free to modify the contents of :foo and re-run the entire buffer.
  # We'll hear the effect immediately without having to stop and re-start the code.
  # This is because our fn has been redefined, (which our thread will pick up) and
  # due to the thread being named, the second re-run will not create a new similarly
  # named thread. This is a nice pattern for live coding and is the basis of live_loop.
  ",
  "
  #Delaying the start of a thread
  in_thread delay: 1 do
    sample :ambi_lunar_land # this sample is not triggered at time 0 but after 1 beat
  end

  play 80                   # Note 80 is played at time 0
  "    ]


      def assert(arg, msg=nil)
        unless arg
          error_msg =  "Assert failed! #{msg}"
          raise AssertionError, error_msg
        end

        arg
      end
      doc name:           :assert,
          introduced:     Version.new(2,8,0),
          summary:        "Ensure arg is valid",
          doc:            "Raises an exception if the argument is either nil or false.",
          args:           [[:arg, :anything]],
          alt_args:       [[:arg, :anything],[:error_msg, :string]],
          opts:           nil,
          accepts_block:  false,
          examples:       ["
# Simple assertions
assert true   # As true is neither nil or false, this assertion passes
assert 1      # Similarly, 1 passes
assert \"foo\" # As do string
assert false  # This will raise an exception
",
"
# Communicating error messages
assert false, \"oops\" # This will raise an exception containing the message \"oops\"
",

"
# More interesting assertions
assert (1 + 1) == 2 # Ensure that arithmetic is sane!
assert [:a, :b, :c].size == 3 # ensure lists can be correctly counted
"]

      def assert_equal(arg1, arg2, msg=nil)
        unless arg1 == arg2
          error_msg =  "Assert failed! #{arg1.inspect} is not equal to #{arg2.inspect}. #{msg}"
          raise AssertionError, error_msg
        end
        arg1
      end
      doc name:           :assert_equal,
          introduced:     Version.new(2,8,0),
          summary:        "Ensure args are equal",
          doc:            "Raises an exception if both arguments aren't equal. ",
          args:           [[:arg1, :anything], [:arg2, :anything]],
          alt_args:       [[:arg1, :anything], [:arg2, :anything],[:error_msg, :string]],
          opts:           nil,
          accepts_block:  false,
          examples:       ["
# Simple assertions
assert_equal 1, 1
",
"
# More interesting assertions
assert_equal 1 + 1, 2 # Ensure that arithmetic is sane!
assert_equal [:a, :b, :c].size,  3 # ensure lists can be correctly counted
",

"
# Add messages to the exceptions
assert_equal 3, 5, \"something is seriously wrong!\"
" ]

      def load_buffer(path)
        path = File.expand_path(path.to_s)
        raise "Unable to load buffer - no file found with path: #{path}" unless File.exists?(path)
        buf = __current_job_info[:workspace]
        __info "loading #{buf} with #{path}"
        __replace_buffer(buf, File.read(path))
      end
      doc name:           :load_buffer,
          introduced:     Version.new(2,10,0),
          summary:        "Load the contents of a file to the current buffer",
          doc:            "Given a path to a file, will read the contents and load it into the current buffer. This will replace any previous content.",
          args:           [[:path, :string]],
          opts:           nil,
          accepts_block:  false,
          examples:       ["
load_buffer \"~/sonic-pi-tracks/phat-beats.rb\" # will replace content of current buffer with contents of the file"]


      def load_example(example_name)
        path = Dir[examples_path + '/**/' + example_name.to_s + '.rb'].first
        raise "Error - no example found with name: #{example_name.inspect}" unless path
        buf = __current_job_info[:workspace]
        __info "loading #{buf} with #{path}"
        title = ActiveSupport::Inflector.titleize(example_name)
        __replace_buffer(buf, "# #{title}\n" + File.read(path))
      end
      doc name:           :load_example,
          introduced:     Version.new(2,10,0),
          summary:        "Load a built-in example",
          doc:            "Given a keyword representing an example, will load it into the current buffer. This will replace any previous content.",
          args:           [[:path, :string]],
          opts:           nil,
          accepts_block:  false,
          examples:       ["
load_example :rerezzed # will replace content of current buffer with the rerezzed example"]

      def __on_thread_death(&block)
        gc_jobs = __system_thread_locals.get(:sonic_pi_local_spider_in_thread_gc_jobs) || []
        gc_jobs << block
        __system_thread_locals.set_local(:sonic_pi_local_spider_in_thread_gc_jobs, gc_jobs)
      end
    end
  end
end
