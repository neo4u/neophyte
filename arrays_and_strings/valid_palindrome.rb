# @param {String} s
# @return {Boolean}
def is_palindrome(s)
  s.gsub!(/[^a-zA-Z0-9]/, '')
  s.downcase!
  s.reverse == s
end

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(is_palindrome("abba"), true)
assert_equal(is_palindrome("race a car"), false)
assert_equal(is_palindrome("A man, a plan, a canal: Panama"), true)
assert_equal(is_palindrome(".a"), true)
assert_equal(is_palindrome("0P"), false)
assert_equal(is_palindrome("_a" * 1_000_000), true)
