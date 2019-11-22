from typing import List


class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return 0
        m, n, self.num_buildings = len(grid), len(grid[0]), 0
        c, d = [[0 for _ in range(n)] for _ in range(m)], [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: self.num_buildings += 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] != 1: continue
                if not self.bfs(grid, i, j, c, d): return -1

        shortest = float('inf')
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0 or c[i][j] < self.num_buildings: continue
                shortest = min(shortest, d[i][j])

        return -1 if shortest == float('inf') else shortest

    def bfs(self, grid, start_x, start_y, c, d):
        count = 1 # Bcuz we only start the BFS after building was found so the count should already be 1
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m, n = len(grid), len(grid[0])
        q, visited = [(start_x, start_y, 0)], set([(start_x, start_y)]) # Start with the building co-ordinates and a distance of 0

        while q:
            x, y, dist = q.pop(0)
            for di, dj in dirs:
                i, j = x + di, y + dj
                if not self.valid(m, n, i, j, visited): continue # Only when the points are within the bounds of the matrix && not yet visited
                visited.add((i, j))
                if grid[i][j] == 0: # Only add 0 points to the queue, cuz we only needs distances of each 0 to all 1s
                    q.append((i, j, dist + 1))
                    d[i][j] += dist + 1
                    c[i][j] += 1
                elif grid[i][j] == 1:
                    count += 1

        return count == self.num_buildings

    def valid(self, m, n, i, j, visited):
        return 0 <= i <= m - 1 and 0 <= j <= n - 1 and (i, j) not in visited



class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return 0
        self.m, self.n, self.num_buildings = len(grid), len(grid[0]), 0
        self.c, self.d = [[0 for _ in range(self.n)] for _ in range(self.m)], [[0 for _ in range(self.n)] for _ in range(self.m)]

        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 1: self.num_buildings += 1

        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] != 1: continue
                if not self.bfs(grid, i, j): return -1

        shortest = float('inf')
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] != 0 or self.c[i][j] < self.num_buildings: continue
                shortest = min(shortest, self.d[i][j])

        return -1 if shortest == float('inf') else shortest

    def bfs(self, grid, start_x, start_y):
        count = 1
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        q, visited = [(start_x, start_y, 0)], set([(start_x, start_y)])

        while q:
            i, j, dist = q.pop(0)
            for di, dj in dirs:
                x, y = i + di, j + dj
                if not self.valid(x, y, visited): continue
                visited.add((x, y))
                if grid[x][y] == 0:
                    q.append((x, y, dist + 1))
                    self.d[x][y] += dist + 1
                    self.c[x][y] += 1
                elif grid[x][y] == 1:
                    count += 1

        return count == self.num_buildings

    def valid(self, i, j, visited):
        return 0 <= i <= self.m - 1 and 0 <= j <= self.n - 1 and (i, j) not in visited



# 317. Shortest Distance from All Buildings
# https://leetcode.com/problems/shortest-distance-from-all-buildings/


# Key Insights
# 1. We want to build a house on a 0 point
# 2. We want to reach ALL the 1 points
# 3. We want to choose a 0 point that has the least total distance to all such points


# Approach 1: BFS from each building
# Steps:
# 1. Perform BFS from each building to each 0 and keep as a matrix of sum of distances from 0 points,
#    then calculate min of them all
# 2. prune bfs for nodes which will not result in small

# Time:  O(k * m * n), k is the number of the buildings or O(m^2.n^2)
# Space: O(m * n)

# A powerful pruning is that during the BFS we use count1 to count how many 1 grids we reached.
# If count1 < buildings then we know not all 1 grids are connected so we can return -1 immediately,
# which greatly improved speed (beat 100% submissions).


sol = Solution()
assert sol.shortestDistance([[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]) == 7
assert sol.shortestDistance([[1]]) == -1
assert sol.shortestDistance([[1,1]]) == -1
assert sol.shortestDistance([[1],[1]]) == -1
assert sol.shortestDistance([[1,2,0]]) == -1
assert sol.shortestDistance([[1],[2],[0]]) == -1

assert sol.shortestDistance([[1,0]]) == 1
assert sol.shortestDistance([[1],[0]]) == 1
assert sol.shortestDistance([[1,0,1]]) == 2
assert sol.shortestDistance([[1],[0],[1]]) == 2
assert sol.shortestDistance([[1,0],[0,1]]) == 2
assert sol.shortestDistance([[2,0,0],[0,1,0],[1,0,0]]) == 2
assert sol.shortestDistance([[1,2,0],[0,0,0],[0,0,0]]) == 1
assert sol.shortestDistance([[0,2,1],[1,0,2],[0,1,0]]) == -1

assert sol.shortestDistance([[1,1],[0,1]]) == -1
assert sol.shortestDistance([[1,0,1,0,1]]) == -1
assert sol.shortestDistance([[1],[0],[1],[0],[1]]) == -1
assert sol.shortestDistance([
    [1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 1],
    [0, 1, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 1],
    [0, 1, 1, 1, 1, 0]
]) == 88
assert sol.shortestDistance([
    [1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1],
    [0, 1, 1, 1, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [0, 1, 1, 1, 1, 1, 1, 0]
]) == 226
