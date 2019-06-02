class DS:
    def __init__(self):
        self.parent = {}
        self.rank = {}
        self.count = 0

    def find(self, x):
        if x != self.parent[x]: self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def has_parent(self, x):
        return x in self.parent

    def set_parent(self, x):
        self.parent[x] = x
        self.rank[x] = 0
        self.count += 1

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

    def print_ds(self):
        print(self.parent)
        print(self.count)


class Solution:
    def numIslands(self, grid):
        if not grid or not grid[0]: return 0
        m, n, ds = len(grid), len(grid[0]), DS()
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0": continue
                ds.set_parent((i, j))

                for dx, dy in dirs:
                    x, y = i + dx, j + dy
                    if not self.valid_land(grid, m, n, x, y): continue
                    if not ds.has_parent((x, y)): ds.set_parent((x, y))
                    ds.union((i, j), (x, y))

        return ds.count

    def valid_land(self, grid, m, n, r, c):
        return 0 <= r <= m - 1 and 0 <= c <= n - 1 and grid[r][c] == "1"


class Solution:
    def numIslands(self, grid):
        if not grid or not grid[0]: return 0
        m, n = len(grid), len(grid[0])

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0': continue
                self.dfs(grid, m, n, i, j)
                count += 1

        return count

    def dfs(self, grid, m, n, i, j):
        grid[i][j] = '0'
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for d in dirs:
            dx, dy = d
            x, y = i + dx, j + dy
            if not self.valid_land(grid, m, n, x, y): continue
            self.dfs(grid, m, n, x, y)

    def valid_land(self, grid, m, n, r, c):
        return 0 <= r <= m - 1 and 0 <= c <= n - 1 and grid[r][c] == "1"


sol = Solution()

assert sol.numIslands(
    [["1","1","1","1","0"],
     ["1","1","0","1","0"],
     ["1","1","0","0","0"],
     ["0","0","0","0","0"]]) == 1


    #  ["0","0","0","0","0"]
    #  ["0","0","0","0","0"]
    #  ["0","0","0","0","0"]
    #  ["0","0","0","0","0"]



# dfs(0, 0, 0) [0]
#     dfs(1, 0, 1) [0, 1]
#         dfs(1,1,2) [0, 1, 2]
#             dfs(1,3,2) [0 1 2 2]
#             [0 1 2 2 0]

# (r+1, c, 1)
# (r-1, c, 2)
# (r, c+1, 3)
# (r, c-1, 4)

# [[1,1,0],
#  [0,1,1],
#  [0,0,0],
#  [1,1,1],
#  [0,1,0]]


# 0 3 1 3 0 0 0 0

# 0 3 1 0 3

# - -
#  |