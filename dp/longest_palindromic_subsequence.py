# Approach 1: Recursion with memoization
from collections import defaultdict
class Solution1:
    def helper(self, i, j, s, cache):
        if i > j:                           return 0
        elif i == j:                        return 1
        elif i in cache and j in cache[i]:  return cache[i][j]
        elif s[i] == s[j]:
            cache[i][j] = self.helper(i + 1, j - 1, s, cache) + 2
            return cache[i][j]
        else:
            cache[i][j] = max(self.helper(i, j - 1, s, cache), self.helper(i + 1, j, s, cache))
            return cache[i][j]

    def longestPalindromeSubseq(self, s: str) -> int:
        cache = defaultdict(dict)
        return self.helper(0, len(s) - 1, s, cache)


# Approach 2: DP 2D
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[1] * n for _ in range(n)]

        for sz in range(2, n + 1):
            for i in range(n - sz + 1):     # i ranges from [0 to n - sz] == [0 to n]
                j = i + sz - 1              # j ranges from [1 to i]

                if s[i] == s[j]:    dp[i][j] = dp[i + 1][j - 1] + 2 if sz != 2 else 2
                else:               dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][n - 1]


# This is tricky don't bother.
# if they tell u to use O(n) space in the interview, u're screwed.
# but if you can explain the below method, then good for you
# Approach 3: DP 1D
class Solution3:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [1] * n

        for j in range(1, n):
            pre = dp[j]
            for i in reversed(range(j)): # Same as range(j - 1, -1, -1)
                tmp = dp[i]
                if s[i] == s[j]:
                    dp[i] = 2 + pre if i + 1 <= j - 1 else 2
                else:
                    dp[i] = max(dp[i + 1], dp[i])
                pre = tmp

        return dp[0]


# 516. Longest Palindromic Subsequence
# https://leetcode.com/problems/longest-palindromic-subsequence/description/

# Approach 1: Recursion with memoization


# Approach 2: DP 2D
# Model:
# dp[i][j] = longest palindrome subsequence of s[i to j].
# Recurrance relation:
# dp[i][j] = 2 + dp[i + 1][j - 1]           If s[i] == s[j], or 2 if sz == 2 (?? Why?)
#            max(dp[i + 1][j], dp[i][j-1])  else case

# Special case:
# When s[i] == s[j] and sz = 2, we can add two to dp[i + 1][j - 1] which was init to 1
# Since the 2 chars in the string are equal, we just set dp[i][j] to 2
# Or we can see this as we add 2 in sz != 2 or 1 if sz is anything else
# This is just and extension of the base case

# Some details of the indexing, as this can get hard to visualize
# when sz = 2
# i goes ranges in [0, n - sz + 1] == [0, n - 2 + 1 - 1(for python limit)] == [0, n - 2]
# j goes ranges in i + sz - 1 == [0 + 2 - 1, n - 2 + 2 - 1] == [1, n - 1],
# which makes sense cuz 2nd char is 1 char away

# when sz = n
# i goes ranges in [0, n - sz + 1] == [0, n - n + 1 - 1(for python limit)] == [0, 0]
# j goes ranges in i + sz - 1 == [0 + n - 1, 0 + n - 1] == [n - 1, n - 1],

# Which basically means that only the top right half above the diagonal (\) is used,
# and indexes converge to the right top corner at (0, n - 1), which is where the corner is

# Example: "cbbc"
#   0 1 2 3
# 0 1 1 2 4
# 1 1 1 2 1
# 2 1 1 1 1
# 3 1 1 1 1

# Time: O(n^2)
# Space: O(n)

# Approach 3: DP 1D

# Time: O(n^2)
# Space: O(n)


# There is also manacher's algorithm, What is that? Supposed to be the fastest.
# This is another hard one so, is it practical for interviews I'm not sure.