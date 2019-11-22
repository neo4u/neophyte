from typing import List

class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        shapes = set()
        m, n = len(grid), len(grid[0])
        self.dirs = {
            # down       up            right        left
            'd': [1, 0], 'u': [-1, 0], 'r': [0, 1], 'l': [0, -1]
        }

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0: continue
                shape = self.dfs(grid, m, n, i, j, [], 'o')  # 'o' for origin
                shapes.add("".join(shape))
        return len(shapes)

    def dfs(self, grid, m, n, i, j, shape, di):
        shape.append(di)
        grid[i][j] = 0

        for k, v in self.dirs.items():
            x, y = i + v[0], j + v[1]
            if not self.valid(grid, m, n, x, y): continue
            self.dfs(grid, m, n, x, y, shape, k)

        shape.append('b') # back
        return shape

    def valid(self, grid, m, n, i, j):
        return 0 <= i <= m - 1 and 0 <= j <= n - 1 and grid[i][j] == 1

# 694. Number of Distinct Islands
# https://leetcode.com/problems/number-of-distinct-islands/description/

sol = Solution()
assert sol.numDistinctIslands(
    [[1, 1, 0, 0, 0],
     [1, 1, 0, 0, 0],
     [0, 0, 0, 1, 1],
     [0, 0, 0, 1, 1]]
) == 1
assert sol.numDistinctIslands(
    [[1, 1, 0, 1, 1],
     [1, 0, 0, 0, 0],
     [0, 0, 0, 0, 1],
     [1, 1, 0, 1, 1]]
) == 3
