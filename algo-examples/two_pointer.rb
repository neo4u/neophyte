#!/bin/ruby

def  pairs(a, k) 
  a.combination(2).each do |c|
    puts c
  end
end

a = gets.strip.split(" ").map! {|i| i.to_i}
b_size = a[0]
k = a[1]
b = gets.strip.split(" ").map! {|i| i.to_i}
puts pairs(b,k)
