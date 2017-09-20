#!/bin/ruby

def pairs(a, k) 
  a.combination(2).each do |c|
    puts c
  end
end

a = gets.strip.split.map!(&:to_i)
_ = a[0]
k = a[1]
b = gets.strip.split.map!(&:to_i)
puts pairs(b, k)
