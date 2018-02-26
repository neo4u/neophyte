# @param {String} s
# @return {String}
def reverse_string(s)
  n = s.size - 1 # highest index
  0.upto(n / 2) do |i|
    s[i], s[-i - 1] = s[-i - 1], s[i]
  end

  s
end

# 344. Reverse String
# https://leetcode.com/problems/reverse-string/description/

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(reverse_string("reverse"), "esrever")
assert_equal(reverse_string("abcd"), "dcba")
assert_equal(reverse_string("cdc"), "cdc")
