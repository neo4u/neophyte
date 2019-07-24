from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1

        q, m, n = [], len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                    grid[i][j] = 3

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        minutes = 0
        while q:
            level_q = []
            for i, j in q:
                for dx, dy in dirs:
                    x, y = i + dx, j + dy
                    if not self.isvalid(x, y, m, n, grid): continue
                    level_q.append((x, y))
                    grid[x][y] = 3
            if level_q: minutes += 1
            q = level_q

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: return -1

        return minutes

    def isvalid(self, i, j, m, n, grid):
        return i >= 0 and i < m and j >= 0 and j < n and grid[i][j] == 1


# https://leetcode.com/problems/rotting-oranges/
# 994. Rotting Oranges

sol = Solution()
sol.orangesRotting(
    [[2,1,1],
    [1,1,0],
    [0,1,1]]
) == 4

