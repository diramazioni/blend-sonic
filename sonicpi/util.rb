1#--
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
require 'cgi'
require 'fileutils'
require 'securerandom'

module SonicPi
  module Util
    @@safe_mode = false
    @@tilde_dir = Dir.home
    @@project_path = nil
    @@log_path = nil
    @@current_uuid = nil
    @@home_dir = nil
    @@util_lock = Mutex.new
    @@raspberry_pi_1 = RUBY_PLATFORM.match(/.*arm.*-linux.*/) && File.exists?('/proc/cpuinfo') && !(`cat /proc/cpuinfo | grep BCM2708`).empty?
    @@raspberry_pi_2 = RUBY_PLATFORM.match(/.*arm.*-linux.*/) && File.exists?('/proc/cpuinfo') && !(`cat /proc/cpuinfo | grep BCM2709`).empty? && (`cat /proc/cpuinfo | grep crc32`).empty?
    @@raspberry_pi_3 = RUBY_PLATFORM.match(/.*arm.*-linux.*/) && File.exists?('/proc/cpuinfo') && !(`cat /proc/cpuinfo | grep BCM2709`).empty? && !(`cat /proc/cpuinfo | grep crc32`).empty?

    @@home_dir = File.expand_path((ENV['SONIC_PI_HOME'] || Dir.home) + '/.sonic-pi/')
    @@project_path = @@home_dir + '/store/default/'
    @@log_path = @@home_dir + '/log/'

    [@@home_dir, @@project_path, @@log_path].each do |dir|

      begin
        FileUtils.mkdir_p(dir) unless File.exists?(dir)
      rescue
        @@safe_mode = true
        STDERR.puts "Unable to create #{dir} due to permissions errors"
      end
    end

    begin
      @@log_file = File.open("#{@@log_path}/debug.log", 'w')
    rescue
      @@safe_mode = true
      STDERR.puts "Unable to open log file #{@@log_path}/debug.log"
      @@log_file = nil
    end

    begin
      @@process_log_file = File.open("#{@@log_path}/processes.log", 'a')
    rescue
      @@safe_mode = true
      STDERR.puts "Unable to open process log file #{@@log_path}/processes.log"
      @@process_log_file = nil
    end

    at_exit do
      @@log_file.close if @@log_file
      @@process_log_file.close if @@process_log_file
    end

    def os
      case RUBY_PLATFORM
      when /.*arm.*-linux.*/
        :raspberry
      when /.*linux.*/
        :linux
      when /.*darwin.*/
        :osx
      when /.*mingw.*/
        :windows
      else
        raise "Unsupported platform #{RUBY_PLATFORM}"
      end
    end

    def raspberry_pi?
      os == :raspberry
    end

    def raspberry_pi_1?
      os == :raspberry && @@raspberry_pi_1
    end

    def raspberry_pi_2?
      os == :raspberry && @@raspberry_pi_2
    end

    def raspberry_pi_3?
      os == :raspberry && @@raspberry_pi_3
    end

    def unify_tilde_dir(path)
      path.gsub(/\A#{@@tilde_dir}/, "~")
    end

    def num_buffers_for_current_os
      4096
    end

    def num_audio_busses_for_current_os
      if os == :raspberry
        64
      else
        1024
      end

    end

    def default_sched_ahead_time
      if raspberry_pi_1?
        1
      else
        0.5
      end
    end

    def host_platform_desc
      case os
      when :raspberry
        if raspberry_pi_1?
          "Raspberry Pi 1"
        elsif raspberry_pi_2?
          "Raspberry Pi 2"
        elsif raspberry_pi_3?
          "Raspberry Pi 3"
        else
          "Raspberry Pi"
        end
      when :linux
        "Linux"
      when :osx
        "Mac"
      when :windows
        "Win"
      end
    end

    def default_control_delta
      if raspberry_pi?
        if raspberry_pi_1?
          0.02
        else
          0.013
        end
      else
        0.005
      end
    end

    def home_dir
      @@home_dir
    end

    def init_path
      home_dir + '/init.rb'
    end

    def project_path
      @@project_path
    end

    def log_path
      @@log_path
    end

    def global_uuid
      return @@current_uuid if @@current_uuid
      @@util_lock.synchronize do
        return @@current_uuid if @@current_uuid
        path = home_dir + '/.uuid'

        if (File.exists? path)
          old_id = File.readlines(path).first.strip
          if  (not old_id.empty?) &&
              (old_id.size == 36)
            @@current_uuid = old_id
            return old_id
          end
        end

        # invalid or no uuid - create and store a new one
        new_uuid = SecureRandom.uuid
        begin
          File.open(path, 'w') {|f| f.write(new_uuid)}
        rescue
          @@safe_mode = true
          log "Unable to write uuid file to #{path}"
        end
        @@current_uuid = new_uuid
        new_uuid
      end
    end

    def ensure_dir(d)
      begin
        FileUtils.mkdir_p(dir) unless File.exists?(dir)
      rescue
        @@safe_mode = true
        log "Unable to create #{dir} due to permissions errors"
      end
    end

    def root_path
      File.absolute_path("#{File.dirname(__FILE__)}/../../../../../")
    end

    def etc_path
      File.absolute_path("#{root_path}/etc")
    end

    def snippets_path
      File.absolute_path("#{etc_path}/snippets")
    end

    def doc_path
      File.absolute_path("#{etc_path}/doc")
    end

    def cheatsheets_path
      File.absolute_path("#{doc_path}/cheatsheets")
    end

    def tutorial_path
      File.absolute_path("#{doc_path}/tutorial")
    end

    def tmp_path
      File.absolute_path("#{root_path}/tmp")
    end

    def synthdef_path
      File.absolute_path("#{etc_path}/synthdefs/compiled")
    end

    def samples_path
      File.absolute_path("#{etc_path}/samples")
    end

    def buffers_path
      File.absolute_path("#{etc_path}/buffers")
    end

    def app_path
      File.absolute_path("#{root_path}/app")
    end

    def html_public_path
      File.absolute_path("#{app_path}/gui/html")
    end

    def qt_gui_path
      File.absolute_path("#{app_path}/gui/qt")
    end

    def examples_path
      File.absolute_path("#{etc_path}/examples")
    end

    def server_path
      File.absolute_path("#{app_path}/server")
    end

    def server_bin_path
      File.absolute_path("#{server_path}/bin")
    end

    def native_path
      if os == :windows
        File.absolute_path("#{server_path}/native/win")
      else
        File.absolute_path("#{server_path}/native/#{os}")
      end
    end

    def scsynth_log_path
      log_path + '/scsynth.log'
    end

    def ruby_path
      # For running tests
      case os
      when :windows
        File.join(native_path, "ruby", "bin", "ruby.exe")
      when :osx, :raspberry, :linux
        File.join(native_path, "ruby", "bin", "ruby")
      end
    end

    def user_settings_path
      File.absolute_path("#{home_dir}/settings.json")
    end

    def log_raw(s)
      if @@log_file
        @@log_file.write("[#{Time.now.strftime("%Y-%m-%d %H:%M:%S")}] #{s}")
        @@log_file.flush
      else
        Kernel.puts("[#{Time.now.strftime("%Y-%m-%d %H:%M:%S")}] #{s}")
      end
    end

    def log_exception(e, context="")
      if debug_mode
        res = "Exception => #{context} #{e.message}"
        e.backtrace.each do |b|
          res << "                                        "
          res << b
          res << "\n"
        end
        log_raw res
      end
    end

    def log_info(s)
      log "--------------->  " + s
    end

    def log(message)
      if debug_mode
        message = message.to_s
        res = ""
        res << "\n" if message.empty?
        first = true
        while !(message.empty?)
          if first
            res << message.slice!(0..151)
            res << "\n"
            first = false
          else
            res << "                                        "
            res << message.slice!(0..133)
            res << "\n"
          end
        end
        log_raw res
      end
    end

    def log_process_info(s)
      if @@process_log_file
        @@process_log_file.puts s
        @@process_log_file.flush
      end
    end

    def debug_mode
      true
    end

    def osc_debug_mode
      true
    end

    def incoming_osc_debug_mode
      true
    end

    def resolve_synth_opts_hash_or_array(opts)
      case opts
      when Hash, SonicPi::Core::SPMap
        return opts
      when Array, SonicPi::Core::SPVector
        merge_synth_arg_maps_array(opts)
      when NilClass
        return {}
      else
        raise "Invalid options. Options should either be an even list of key value pairs, a single Hash or nil. Got #{opts.inspect}"
      end
    end

    def merge_synth_arg_maps_array(opts_a)
      res = {}
      idx = 0
      size = opts_a.size

      while (idx < size) && (m = opts_a[idx]).is_a?(Hash)
        res = res.merge(m)
        idx += 1
      end

      return res if idx == size
      left = (opts_a[idx..-1])
      raise "There must be an even number of trailing synth args" unless left.size.even?
      h = Hash[*left]
      res.merge()
    end

    def purge_nil_vals!(m)
      m.delete_if { |k, v| v.nil? }
    end

    def arg_h_pp(arg_h)
      s = "{"
      arg_h.each do |k, v|
        if v
          rounded = v.is_a?(Float) ? v.round(4) : v.inspect
          s << "#{k}: #{rounded}, "
        end
      end
      s.chomp(", ") << "}"
    end

    def safe_mode?
      @@safe_mode
    end

    def is_list_like?(o)
      o.is_a?(SonicPi::Core::SPVector) || o.is_a?(Array)
    end

    def register_process(pid)
      `'#{ruby_path}' '#{server_path}/bin/task-register.rb' '#{pid}'`
    end

    def __thread_locals(t = Thread.current)
      tls = t.thread_variable_get(:sonic_pi_thread_locals)
      tls = t.thread_variable_set(:sonic_pi_thread_locals, SonicPi::Core::ThreadLocal.new) unless tls
      return tls
    end

    def __system_thread_locals(t = Thread.current)
      tls = t.thread_variable_get(:sonic_pi_system_thread_locals)
      tls = t.thread_variable_set(:sonic_pi_system_thread_locals, SonicPi::Core::ThreadLocal.new) unless tls
      return tls
    end

    def __thread_locals_reset!(tls, t = Thread.current)
      t.thread_variable_set(:sonic_pi_thread_locals, tls)
    end

    def __system_thread_locals_reset!(tls, t = Thread.current)
      t.thread_variable_set(:sonic_pi_system_thread_locals, tls)
    end

    def __no_kill_block(t = Thread.current, &block)
      mut = __system_thread_locals(t).get(:sonic_pi_local_spider_no_kill_mutex)

      # just call block when in a non-sonic-pi-thread
      return block.call unless mut

      # if we're already in a no_kill_block, run code anyway
      return block.call if __system_thread_locals(t).get(:sonic_pi_local_spider_in_no_kill_block)

      mut.synchronize do
        __system_thread_locals(t).set_local(:sonic_pi_local_spider_in_no_kill_block, true)
        r = block.call
        __system_thread_locals(t).set_local(:sonic_pi_local_spider_in_no_kill_block, false)
        r
      end
    end
  end
end
