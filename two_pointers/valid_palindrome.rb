# @param {String} s
# @return {Boolean}
def is_palindrome(s)
    return true if !s || s.empty?
    l, r = 0, s.size - 1

    while l < r
        l += 1 while !alpha_num?(s[l]) && l < r # Skip non-alpha numeric from left
        r -= 1 while !alpha_num?(s[r]) && l < r # Skip non-alpha numeric from right

        return false unless s[l].casecmp(s[r]).zero?
        l += 1; r -= 1
    end

    true
end

def alpha_num?(s)
    s.match(/[a-zA-Z0-9]/)
end

# 125. Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/description/
# Approach two pointer.
# Time: O(n), Space: O(1)

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(is_palindrome("A man, a plan, a canal: Panama"), true)
assert_equal(is_palindrome("race a car"), false)
