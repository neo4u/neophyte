# @param {String} s
# @param {String} p
# @return {Boolean}
def is_match(s, p)
    m, n = s.length, p.length
    dp = Array.new(m + 1) { Array.new(n + 1, false) }
    dp[0][0] = true

    1.upto(n) do |j|
        dp[0][j] = dp[0][j - 1] if p[j - 1] == '*'
    end

    1.upto(m) do |i|
        1.upto(n) do |j|
            dp[i][j] = dp[i - 1][j - 1] if p[j - 1] == s[i - 1] || p[j - 1] == '?'
            dp[i][j] = dp[i - 1][j] || dp[i][j - 1] if p[j - 1] == '*'
        end
    end

    dp[m][n]
end

# 44. Wildcard Matching
# https://leetcode.com/problems/wildcard-matching/

# 1. dp[i][j]: represents a match between s[0 to i - 1] (len i) and p[0 to j - 1] (len j)
# 2. Base case:
#     - origin: dp[0][0]: they do match, so dp[0][0] = true
#     - first row: dp[0][j]: except for String p starts with *, otherwise all false
#     - first col: dp[i][0]: can't match when p is empty. All false.
# 3. Recursion:
#     - Iterate through every dp[i][j]
#     - dp[i][j] = true:
#         - if (s[i - 1] == p[j - 1] || p[j - 1] == '?') && dp[i - 1][j - 1] == true
#         - elif p[j - 1] == '*' && (dp[i-1][j] == true || dp[i][j-1] == true)

# dp[i-1][j] represents the match between s[0 to i - 2] (len i - 1) and p[0 to j - 1] (len j) [1 less char in s]
# dp[i][j-1] represents the match between s[0 to i - 1] (len i) and p[0 to j - 2] (len j - 1) [1 less char in p]

# Example:
# S: xxx
# P: xx*
#   '' x x *
# '' T F F F
#  x F T F F
#  x F F T T
#  x F F F T

# For i=3, j=3: s[i] is x, p[i] is *
# dp[3][3] = dp[2][3] || dp[3][2]
# dp[2][3] means we use the match from s: xx and p: xx* (notice 1 less char in s)
# dp[3][2] means we use the match from s: xxx and p: xx (notice 1 less char in p)
# dp[2][3] is true hence this ends up being a match

# Time: O(m * n)
# Space: O(m * n)

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(is_match('aa', 'a'), false)
assert_equal(is_match('ab', '*'), true)
assert_equal(is_match('abcd', '*'), true)
assert_equal(is_match('adceb', '*a*b'), true)
assert_equal(is_match('acdcb', 'a*c?b'), false)
assert_equal(is_match('xb', 'xa*'), false)
assert_equal(is_match('xa', 'xa*'), true)
