#!/bin/ruby

def reduce_string(s)
  reduce(s) until reduced?(s)
  s.empty? ? 'Empty String' : s
end

def reduce(s)
  s.gsub!(adjacent_pairs(s).first.join, '')
end

def reduced?(s)
  adjacent_pairs(s).empty?
end

def adjacent_pairs(s)
  s.chars.each_cons(2).select { |c1, c2| c1 == c2 }
end

s = gets.strip
result = reduced_string(s)
puts result
