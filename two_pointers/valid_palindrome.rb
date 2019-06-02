# Two pointer method
# @param {String} s
# @return {Boolean}
def is_palindrome(s)
    return true if !s || s.empty?
    l, r = 0, s.size - 1

    while l < r
        l += 1 while !alpha_num?(s[l]) && l < r # Skip non-alpha numeric from left
        r -= 1 while !alpha_num?(s[r]) && l < r # Skip non-alpha numeric from right
        return false if s[l].downcase != s[r].downcase
        l += 1; r -= 1
    end

    true
end

def alpha_num?(c)
    c.match(/[a-zA-Z0-9]/)
end

# Gsub method
def is_palindrome(s)
    s.gsub(/[^a-z0-9]/i, '').tap { |str| return str.casecmp(str.reverse).zero? }
end

# 125. Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/description/

# Approach 1: two pointer
# 1. two pointers from either end
# 2. return as soon as mismatch
# 3. If match keep inc l and dec r
# 4. If either of the chars are non-alpha keep inc/dec accordingly

# Approach 2: Gsub method
# delete unneccessary chars 
# compare do casecmp() of str and str.reverse

# Time: O(n)
# Space: O(1)

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(is_palindrome("abba"), true)
assert_equal(is_palindrome("race a car"), false)
assert_equal(is_palindrome("A man, a plan, a canal: Panama"), true)
assert_equal(is_palindrome(".a"), true)
assert_equal(is_palindrome("0P"), false)
assert_equal(is_palindrome("_a" * 1_000_000), true)