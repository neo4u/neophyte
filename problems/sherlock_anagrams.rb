#!/bin/ruby

def sherlock_and_anagrams(s)
  anagram_subs = 0
  subs = all_substrings(s)
  subs.combination(2).each do |str1, str2|
    if check_anagrams(str1, str2)
      anagram_subs += 1
    end
  end

  anagram_subs
end

def all_substrings(str)
  (0...str.size).flat_map do |i|
    (i...str.size).map do |j|
      str[i..j]
    end
  end
end

def check_anagrams(a, b)
  return false if a.size != b.size
  a_freq = {}
  b_freq = {}

  a.chars.each do |c|
    a_freq[c] = 0 if a_freq[c].nil?
    a_freq[c] += 1
  end

  b.chars.each do |c|
    b_freq[c] = 0 if b_freq[c].nil?
    b_freq[c] += 1
  end

  ('a'..'z').each do |c|
    return false if a_freq[c] != b_freq[c]
  end

  true
end

q = gets.strip.to_i
list = []
(0..q-1).each do |_|
  s = gets.strip
  list << s
end

list.each do |str|
  result = sherlock_and_anagrams(str)
  puts result
end
