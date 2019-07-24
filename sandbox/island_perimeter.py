class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        self.m, self.n = len(grid), len(grid[0])
        self.perimeter = 0
        self.dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 1:
                    self.perimeter += 4 - self.get_nbr_count(grid, i, j)

        return self.perimeter

    def get_nbr_count(self, grid, i, j):
        count = 0
        for d in self.dirs:
            x, y = i + d[0], j + d[1]
            if self.valid(grid, x, y):
                count += 1

        return count

    def valid(self, grid, i, j):
        return 0 <= i <= self.m - 1 and 0 <= j <= self.n - 1 and grid[i][j]


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        self.m, self.n = len(grid), len(grid[0])
        land_count, nbr_count = 0, 0
        self.dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 1:
                    land_count += 1
                    nbr_count += self.get_nbr_count(grid, i, j)

        return 4 * land_count - nbr_count

    def get_nbr_count(self, grid, i, j):
        count = 0
        for d in self.dirs:
            x, y = i + d[0], j + d[1]
            if self.valid(grid, x, y):
                count += 1

        return count

    def valid(self, grid, i, j):
        return 0 <= i <= self.m - 1 and 0 <= j <= self.n - 1 and grid[i][j]



# 463. Island Perimeter
# https://leetcode.com/problems/island-perimeter/description/


# 1 1 1 1
# 1 1 1 1 
# 1 1 1 1 
