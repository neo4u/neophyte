#!/bin/env ruby

# -------------------------------------------------------------------------------
# String  always consists of two distinct alternating characters.
# For example, if string 's two distinct characters are x and y,
# then t could be xyxyx or yxyxy but not xxyy or xyyx.
# Sample Input
# 10
# beabeefeab

# Sample Output
# 5
# Explanation

# The characters present in  are a, b, e, and f. This means that  must consist of two of those characters.
# If we delete e and f, the resulting string is babab. This is a valid  as there are only two distinct characters (a and b), and they are alternating within the string.
# If we delete a and f, the resulting string is bebeeeb. This is not a valid string  because there are three consecutive e's present.
# If we delete only e, the resulting string is babfab. This is not a valid string  because it contains three distinct characters.
# Thus, we print the length of babab, which is , as our answer.
# -------------------------------------------------------------------------------


def valid_t?(s)
  two_chars = s.chars.uniq
  return false if two_chars.size != 2
  s.chars.each_cons(2) do |c1, c2|
    return false if c1 == c2
  end
  true
end

def longest_2_char(s, len)
  return len if valid_t?(s)
  max = 0
  s.chars.uniq.combination(2).each do |c1, c2|
    cpy = s.chars.select { |c| [c1, c2].include?(c) }
    max = [max, cpy.size].max if valid_t?(cpy.join())
  end
  max
end

len = gets.strip.to_i
s = gets.strip
puts longest_2_char(s, len)
