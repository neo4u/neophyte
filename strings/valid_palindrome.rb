# @param {String} s
# @return {Boolean}
def is_palindrome(s)
  s.gsub(/[^a-z0-9]/i, '').tap { |str| return str.casecmp(str.reverse).zero? }
end

require 'test/unit'
extend Test::Unit::Assertions

# 125. Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/description/
# Approach two pointer.
# Time: O(n), Space: O(1)

require 'test/unit'
extend Test::Unit::Assertions


assert_equal(is_palindrome("abba"), true)
assert_equal(is_palindrome("race a car"), false)
assert_equal(is_palindrome("A man, a plan, a canal: Panama"), true)
assert_equal(is_palindrome(".a"), true)
assert_equal(is_palindrome("0P"), false)
assert_equal(is_palindrome("_a" * 1_000_000), true)