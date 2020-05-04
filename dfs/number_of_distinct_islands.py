from typing import List


class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        shapes = set()
        self.m, self.n = len(grid), len(grid[0])
        self.grid = grid
        self.dirs = {
            'u': (-1, 0), 'd': (1, 0),
            'l': (0, -1), 'r': (0, 1)
        }
        for i in range(self.m):
            for j in range(self.n):
                if self.grid[i][j] == 0: continue
                shape = self.dfs(i, j, ['o'])
                shapes.add("".join(shape))
        return len(shapes)

    def dfs(self, i, j, shape_path):
        self.grid[i][j] = 0

        for k, v in self.dirs.items():
            x, y = i + v[0], j + v[1]
            if not self.valid_land(x, y): continue
            shape_path.append(k)
            self.dfs(x, y, shape_path)
        shape_path.append('b')
        return shape_path

    def valid_land(self, i, j):
        return 0 <= i <= self.m - 1 and 0 <= j <= self.n - 1 and self.grid[i][j] == 1


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
