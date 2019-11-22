class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]
        dp[0][0] = True # Empty string and empty patterns are considered a match

        # if pattern has a * then we fill t/f based of empty string with string of size j with
        # previous match status of empty string with string of size j - 1
        # This loop fills the first row in the matrix
        # Example:
        # Matching s = '' with p = '*********'
        for j in range(1, n + 1):
            if p[j - 1] == '*': dp[0][j] = dp[0][j - 1]

        # Use the conditions to fill rest of the matrix
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == s[i - 1] or p[j - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                # 1 less on s  or 1 less on p
                # empty char   or 1 char 
                if p[j - 1] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]

        return dp[m][n]


# 44. Wildcard Matching
# https://leetcode.com/problems/wildcard-matching/

# 1. dp[i][j]: represents a match between s[0 to i - 1] (len i) and p[0 to j - 1] (len j)
# 2. Base case:
#     - origin: dp[0][0]: they do match, so dp[0][0] = true
#     - first row: dp[0][j]: except for String p starts with *, otherwise all false
#     - first col: dp[i][0]: can't match when p is empty. All false.
# 3. Recursion:
#     - Iterate through every 1 to m and inner 1 to n (0 is covered by base case)
#     - dp[i][j] = true:
#         - if (s[i - 1] == p[j - 1] || p[j - 1] == '?') && dp[i - 1][j - 1] == true
#         - elif p[j - 1] == '*' && (dp[i-1][j] == true || dp[i][j-1] == true)

# dp[i-1][j] represents the match between s[0 to i - 2] (len i - 1) and p[0 to j - 1] (len j) [1 less char in s]
# This case we're considering the * as 1 more repitition
# Consider the current char as part of * quota, Borrow from top cell
# dp[i][j-1] represents the match between s[0 to i - 1] (len i) and p[0 to j - 2] (len j - 1) [1 less char in p]
# This case we're considering the * as 0 repititions
# Consider the match between current string and without * in pattern

# Example 1: Case where dp[i - 1][j] is true, and we consider * as 1 repition
# S: xxx
# P: xx*
#   '' x x *
# '' T F F F
#  x F T F F
#  x F F T T
#  x F F F T

# For i=3, j=3: we're considering a match between s[0...i]: xxx p[0...j]: xx*
# dp[3][3] = dp[2][3] || dp[3][2]
# dp[2][3] means we use the match from s: xx and p: xx* (notice 1 less char in s)
# dp[3][2] means we use the match from s: xxx and p: xx (notice 1 less char in p)
# dp[2][3] is true hence this ends up being a match

# Example 2: Case where dp[i][j - 1] is true, and we consider * as 0 repitions
# S: adceb
# P: *a*b
#   '' * a * b
# '' T T F F F
#  a F T T X
#  d F T 
#  c F T 
#  e F T 
#  b F T 

# For i=1, j=3: we're considering a match between s[0...i]: a p[0...j]: *a*
# dp[1][3] = dp[0][3] || dp[1][2]
# dp[0][3] means we use the match from s: '' and p: *a* (notice 1 less char in s)
# dp[1][2] means we use the match from s: a and p: *a (notice 1 less char in p)
# dp[1][2] is true hence this ends up being a match


# Time: O(m * n)
# Space: O(m * n)

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(is_match('aa', 'a'), false)
assert_equal(is_match('ab', '*'), true)
assert_equal(is_match('abcd', '*'), true)
assert_equal(is_match('adceb', '*a*b'), true)
assert_equal(is_match('acdceb', 'a*c?b'), true)
assert_equal(is_match('acasdfa32452345sdfasdfdceb', 'a*c?b'), true)
assert_equal(is_match('acdcb', 'a*c?b'), false)
assert_equal(is_match('xb', 'xa*'), false)
assert_equal(is_match('xa', 'xa*'), true)
