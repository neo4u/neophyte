# @param {Integer} x
# @return {Boolean}
def is_palindrome(x)
  return false if x < 0
  ranger = 1
  ranger *= 10 until (x / ranger) < 10

  until x.zero?
    l, r = x / ranger, x % 10
    return false if l != r
    x = (x % ranger) / 10
    ranger /= 100
  end

  true
end

# 9. Palindrome Number
# https://leetcode.com/problems/palindrome-number/description/

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(is_palindrome(100001), true)
assert_equal(is_palindrome(123321), true)
assert_equal(is_palindrome(1221), true)

