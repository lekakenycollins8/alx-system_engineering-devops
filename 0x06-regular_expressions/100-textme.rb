#!/usr/bin/env ruby

sender = ARGV[0][/from:(\S+)/, 1]
receiver = ARGV[0][/to:(\S+)/, 1]
flags = ARGV[0][/flags:([\d:-]+)/, 1]

puts "#{sender},#{receiver},#{flags}"
