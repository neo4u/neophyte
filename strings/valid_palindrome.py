# Two pointer method

import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s: return True
        l, r = 0, len(s) - 1

        while l < r:
            while not self.alpha_num(s[l]) and l < r: l += 1 # Skip non-alpha numeric from left, within bounds
            while not self.alpha_num(s[r]) and l < r: r -= 1 # Skip non-alpha numeric from right, within bounds

            if s[l].lower() != s[r].lower(): return False
            l += 1; r -= 1

        return True

    def alpha_num(self, s):
        return re.match('[a-zA-Z0-9]', s) is not None


# # Gsub method
# def is_palindrome(s)
#     s.gsub(/[^a-z0-9]/i, '').tap { |str| return str.casecmp(str.reverse).zero? }
# end

# 125. Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/description/

# Approach 1: two pointer
# 1. two pointers from either end
# 2. return as soon as mismatch
# 3. If match keep inc l and dec r
# 4. If either of the chars are non-alpha keep inc/dec accordingly, within bounds

# Approach 2: Gsub method
# delete unneccessary chars 
# compare do casecmp() of str and str.reverse

# Time: O(n)
# Space: O(1)

# require 'test/unit'
# extend Test::Unit::Assertions

# assert_equal(is_palindrome("abba"), true)
# assert_equal(is_palindrome("race a car"), false)
# assert_equal(is_palindrome("A man, a plan, a canal: Panama"), true)
# assert_equal(is_palindrome(".a"), true)
# assert_equal(is_palindrome("0P"), false)
# assert_equal(is_palindrome("_a" * 1_000_000), true)