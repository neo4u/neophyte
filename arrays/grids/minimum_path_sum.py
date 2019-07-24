from typing import List

# O(m*n) space
# dp[i][j] represents the minimum sum to reach index i, j
# what we're looking for is dp[m][n]

# base case:
# dp[0][0] = grid[0][0]

# first column
# dp[i][0] = dp[i - 1][0] + grid[i][0]

# first row
# dp[0][i] = dp[0][i - 1] + grid[0][i]

# recurrance relation
# dp[i][j] = min(dp[i - 1][j], dp[i][j]) + grid[i][j]
class Solution0:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return

        m, n = len(grid), len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = grid[0][0]

        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[m - 1][n - 1]


# O(2*n) space
class Solution2:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid: return

        m, n = len(grid), len(grid[0])
        pre = cur = [0] * n
        pre[0] = grid[0][0]

        for i in range(1, n):
            pre[i] = pre[i - 1] + grid[0][i]

        for i in range(1, m):
            cur[0] = pre[0] + grid[i][0]
            for j in range(1, n):
                cur[j] = min(cur[j - 1], pre[j]) + grid[i][j]
            pre = cur
        return cur[-1]

# O(n) space
class Solution3:
    def minPathSum(self, grid):
        if not grid: return
        m, n = len(grid), len(grid[0])

        cur_row = [0] * n
        cur_row[0] = grid[0][0]
        for i in range(1, n):
            cur_row[i] = cur_row[i - 1] + grid[0][i]

        for i in range(1, m):
            cur_row[0] += grid[i][0]
            for j in range(1, n):
                cur_row[j] = min(cur_row[j-1], cur_row[j]) + grid[i][j]

        return cur_row[-1]


# change the grid itself
class Solution:
    def minPathSum(self, grid):
        if not grid: return
        m, n = len(grid), len(grid[0])

        for i in range(1, m): grid[i][0] += grid[i - 1][0]
        for j in range(1, n): grid[0][j] += grid[0][j - 1]

        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

        return grid[m - 1][n - 1]
