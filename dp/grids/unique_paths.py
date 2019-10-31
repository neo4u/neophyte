
# Approach 1: DP top-down, recursion with memoization
class Solution1:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = {}
        return self.findPath(m, n, cache)

    def findPath(self, m, n, cache):
        if (m, n) in cache: return cache[(m, n)]
        elif m == 1 or n == 1: return 1

        cache[(m, n)] = self.findPath(m - 1, n, cache) + self.findPath(m, n - 1, cache)
        return cache[(m, n)]


# Approach 2: DP Bottom-up
class Solution:
    def uniquePaths(self, m, n):
        dp = [[1 for _ in range(n)] for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

        return dp[m - 1][n - 1]


# 62. Unique Paths
# https://leetcode.com/problems/unique-paths/description/

# Approach 1: DP top-down, recursion with memoization

# Approach 2: DP Bottom-up
