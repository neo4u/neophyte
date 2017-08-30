#!/bin/ruby

def cipher(s, key)
  encrypted = []
  key = key % 26
  s.chars.each do |c|
    c_ord = c.ord
    cipher_ord = if c_ord >= 'a'.ord && c_ord <= 'z'.ord && c_ord + key > 'z'.ord
                   c_ord + key - 26
                 elsif c_ord >= 'a'.ord && c_ord <= 'z'.ord && c_ord + key <= 'z'.ord
                   c_ord + key
                 elsif c_ord >= 'A'.ord && c_ord <= 'Z'.ord && c_ord + key > 'Z'.ord
                   c_ord + key - 26
                 elsif c_ord >= 'A'.ord && c_ord <= 'Z'.ord && c_ord + key <= 'Z'.ord
                   c_ord + key
                 else
                   c_ord
                 end
    cipher_c = cipher_ord.chr
    encrypted << cipher_c
  end

  encrypted.join
end

_ = gets.strip.to_i
s = gets.strip
k = gets.strip.to_i
puts cipher(s, k)
