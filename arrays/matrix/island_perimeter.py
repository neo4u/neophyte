from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        self.m, self.n = len(grid), len(grid[0])
        self.perimeter = 0
        self.dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 0: continue
                self.perimeter += 4 - self.get_nbr_count(grid, i, j)

        return self.perimeter

    def get_nbr_count(self, grid, i, j):
        count = 0
        for d in self.dirs:
            x, y = i + d[0], j + d[1]
            if self.valid_land(grid, x, y):
                count += 1

        return count

    def valid_land(self, grid, i, j):
        return 0 <= i <= self.m - 1 and 0 <= j <= self.n - 1 and grid[i][j]


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        self.m, self.n = len(grid), len(grid[0])
        land_count, nbr_count = 0, 0
        self.dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 0: continue
                land_count += 1
                nbr_count += self.neighbor_count(grid, i, j)

        return 4 * land_count - nbr_count

    def neighbor_count(self, grid, i, j) -> int:
        count = 0
        for di, dj in self.dirs:
            x, y = i + di, j + dj
            if not self.valid_land(grid, x, y): continue
            count += 1
        return count

    def valid_land(self, grid, i, j):
        return 0 <= i <= self.m - 1 and 0 <= j <= self.n - 1 and grid[i][j] == 1


# Faster version:
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0: continue
                perimeter += 4
                if i and grid[i - 1][j]: perimeter -= 2
                if j and grid[i][j - 1]: perimeter -= 2

        return perimeter



# 463. Island Perimeter
# https://leetcode.com/problems/island-perimeter/description/


# Intuition:
# 1. We can optimize checking 4 neighbors by checking only left and top neighbors


# 1 1 1 1
# 1 1 1 1 
# 1 1 1 1 
