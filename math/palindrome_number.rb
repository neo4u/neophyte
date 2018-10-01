# @param {Integer} x
# @return {Boolean}
def is_palindrome(x)
	return false if x < 0
	ranger = 1
	ranger *= 10 until (x / ranger) < 10

	until x.zero?
		l, r = x / ranger, x % 10	# l for digit from left and r for digit from right
		return false if l != r		# 
		x = (x % ranger) / 10		# Mod ranger removes first digit, div 10 remove last digit
		ranger /= 100				# remove 10 for removal of digit at each end
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

