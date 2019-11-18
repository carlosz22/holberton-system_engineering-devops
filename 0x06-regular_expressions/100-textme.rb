#!/usr/bin/env ruby
puts ARGV[0].scan(/\[from:(\+?[a-zA-Z0-9]*)\]\s\[to:(\+?[a-zA-Z0-9]*)\]\s\[flags:([0-9:-]*)\]/).join(",")
