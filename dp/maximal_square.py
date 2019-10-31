from typing import List


# Time: O(m * n), Space: O(m * n), 1-Pass
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0

        m, n, size = len(matrix), len(matrix[0]), 0
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or matrix[i][j] == '0':
                    dp[i][j] = int(matrix[i][j]) - int('0')
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
                size = max(size, dp[i][j])

        return size * size


# Time: O(m * n), Space: O(n)
class Solution1:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0

        m, n, size = len(matrix), len(matrix[0]), 0
        curr, prev = [0] * n, None

        for i in range(m):
            for j in range(n):
                tmp = curr[j]
                if i == 0 or j == 0 or matrix[i][j] == '0':
                    curr[j] = int(matrix[i][j]) - int('0')
                else:
                    curr[j] = min(prev, curr[j], curr[j - 1]) + 1
                    size = max(size, curr[j])
                prev = tmp

        return size * size


# 221. Maximal Square
# https://leetcode.com/problems/maximal-square/description/


# Approach 1: DP 2D
# Model:
# dp[i][j] represents the max side of square that has it right bottom corner at (i, j).
# Base Case:
# dp[0][j] and dp[j][0] == 1 if matrix[i][j] == 1 else 0
# Recurrance Relation:
# dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])
# (i, j) is limited by squares ending at (i - 1, j), (i, j - 1), (i - 1, j - 1)
#                                         top row,   left col,   diagonally above
# Refer to diagram files with the same name

# Time: O(mn)
# Space: O(mn)

# Approach 2: DP 1D
# Model:
# curr[j] at iteration i represents the max side of square that has it right bottom corner at (i, j).
# Base Case:
# curr[j] == 1 if matrix[i][j] == 1 else 0, or if iteration is i == 0
# Recurrance Relation:
# curr[j] = min(curr[j], curr[j - 1], prev)
# (i, j) is limited by squares ending at (i - 1, j), (i, j - 1), (i - 1, j - 1)
#                                         top row,   left col,   diagonally above

# Time: O(mn)
# Space: O(n)
