from typing import List


# Approach 1: DFS [TLE]
class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        result, grid = [], [["0" for _ in range(n)] for _ in range(m)]

        for i, j in positions:
            grid[i][j] = '1'
            result.append(self.cc(grid, m, n))

        return result

    def cc(self, grid, m, n):
        count, self.visited = 0, set()
        self.dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0' or (i, j) in self.visited: continue
                self.dfs(grid, m, n, i, j)
                count += 1

        return count

    def dfs(self, grid, m, n, i, j):
        if grid[i][j] == '0' or (i, j) in self.visited: return
        self.visited.add((i, j))

        for di, dj in self.dirs:
            x, y = i + di, j + dj
            if not self.valid_land(grid, m, n, x, y): continue
            self.dfs(grid, m, n, x, y)

    def valid_land(self, grid, m, n, i, j):
        return 0 <= i <= m - 1 and 0 <= j <= n - 1 and grid[i][j] == '1'


# Approach 3: Disjoint Set Union Find
class DS:
    def __init__(self):
        self.parent = {}
        self.rank = {}
        self.count = 0

    def find(self, x):
        if x != self.parent[x]: self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py: return False

        if self.rank[px] > self.rank[py]:
            self.parent[py] = px
        elif self.rank[py] > self.rank[px]:
            self.parent[px] = py
        else:
            self.parent[py] = px
            self.rank[px] += 1

        self.count -= 1
        return True

    def set_parent(self, x):
        self.parent[x] = x
        self.count += 1
        self.rank[x] = 0

    def has_parent(self, x):
        return x in self.parent


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        result, ds = [], DS()
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for i, j in positions:
            if not ds.has_parent((i, j)): ds.set_parent((i, j))
            for di, dj in dirs:
                x, y = i + di, j + dj
                if not self.valid_land(m, n, x, y, ds): continue
                if not ds.has_parent((x, y)): ds.set_parent((x, y))
                ds.union((i, j), (x, y))

            result.append(ds.count)

        return result

    def valid_land(self, m, n, x, y, ds):
        return 0 <= x <= m - 1 and 0 <= y <= n - 1 and (x, y) in ds.parent



# 305. Number of Islands II
# https://leetcode.com/problems/number-of-islands-ii/description/

# Key Insight:
# 1. This is an undirected graph in the form of an adjacency matrix
# 2. There is an edge between two horizontally or vertically adjacent nodes of value 1
# 3. The problem is now to find the no. of connected components
#    in the graph after each addLand operation

# Approach 1: Brute force [TLE]
# Approach 2: DFS [TLE]
# Approach 3: Ad hoc
# Approach 4: Disjoint Set Union Find (with rank and path compression)


sol = Solution()
assert sol.num_islands2(3, 3, [[0,0], [0,1], [1,2], [2,1]]) == [1, 1, 2, 3]
