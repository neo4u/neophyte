# @param {String} s
# @return {Integer}
def length_of_longest_substring(s)
  used = {}
  max_len, start = 0, 0

  s.each_char.with_index do |c, i|
    if used.key?(c) && used[c] >= start
      start = used[c] + 1
    else
      max_len = [max_len, i - start + 1].max
    end
    used[c] = i
  end

  max_len
end

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(length_of_longest_substring("abcabcbb"), 3)
assert_equal(length_of_longest_substring("bbbbb"), 1)
assert_equal(length_of_longest_substring("pwwkew"), 3)

# 3. Longest Substring Without Repeating Characters
# Given a string, find the length of the longest substring without repeating characters.

# Examples:
# Given "abcabcbb", the answer is "abc", which the length is 3.
# Given "bbbbb", the answer is "b", with the length of 1.
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

# @param {String} s
# @return {Integer}
def length_of_longest_substring_brute(s)
  max, n = 0, s.size
  0.upto(n - 1) do |i|
    i.upto(n - 1) do |j|
      substr = s[i..j]
      max = substr.size if all_uniq?(substr) && substr.size > max
    end
  end

  max
end

def all_uniq?(s)
  s.chars.uniq.length == s.chars.length
end

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(length_of_longest_substring_brute("abcabcbb"), 3)
assert_equal(length_of_longest_substring_brute("bbbbb"), 1)
assert_equal(length_of_longest_substring_brute("pwwkew"), 3)

# 3. Longest Substring Without Repeating Characters
# Given a string, find the length of the longest substring without repeating characters.

# Examples:
# Given "abcabcbb", the answer is "abc", which the length is 3.
# Given "bbbbb", the answer is "b", with the length of 1.
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
