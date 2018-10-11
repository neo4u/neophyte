# @param {String} s
# @return {Integer}
def count_substrings(s)
    count, n = 0, s.size

    0.upto(n - 1) do |i|
        count += count_for_center(s, i, i)       # Case of centers between chars
        count += count_for_center(s, i, i + 1)   # Case of centers around a char
    end

    count
end

def count_for_center(s, l, r)
    count = 0
    while 0 <= l && r < s.size && s[l] == s[r]
        count += 1
        l -= 1; r += 1
    end

    count
end

# https://leetcode.com/problems/palindromic-substrings/description/
# 647. Palindromic Substrings

# Approach 1: O(n**2) Time,  O(1) Space
# Total of 2n - 1 centers
# abba 4 centers at abba (n chars are n centers)
# | | | |
# a b b a
# abba has 3 center in between characters (n chars have n - 1 centers in betwee then)
# a|b|b|a
# For each center we find the number of palindromes around it.
# O(n**2) Because of the two levels of nested loops.

# Approach 2: O(n) Time, O(n) space
# O(n) Manacher's Algorithm uses an array to store palindromes as each enter
# Uses the concept of not having to check all the centers and mirroring of centers for a palindrome

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(count_substrings('aaa'), 6)
assert_equal(count_substrings('aaaaa'), 15)
