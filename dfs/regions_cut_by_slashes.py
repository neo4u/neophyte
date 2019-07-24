class Solution:
    def regionsBySlashes(self, grid: 'List[str]') -> 'int':
        self.inner_expand_dir = [
            {"/": [1], "\\":[2], " ":[1,2,3]}, # Pos: 0
            {"/": [0], "\\":[3], " ":[0,2,3]}, # Pos: 1
            {"/": [3], "\\":[0], " ":[0,1,3]}, # Pos: 2
            {"/": [2], "\\":[1], " ":[0,1,2]}  # Pos: 3
        ]
        self.outer_expand_dir = [
            (-1, 0), (0, -1), (0, 1), (1, 0)
        ]
        N = len(grid)
        self.visited = [[[False, False, False, False] for _ in range(N)] for _ in range(N)]

        row, col, count = 0, 0, 0
        while row < N:
            for pos in range(4):
                if self.dfs(grid, N, row, col, pos): count += 1
            col += 1
            if col == N: row, col = row + 1, 0

        return count

    def dfs(self, grid, N, row, col, pos):
        if not self.valid(N, row, col, pos): return
        self.visited[row][col][pos] = True
        # Outter expand
        self.dfs(
            grid, N,
            row + self.outer_expand_dir[pos][0],
            col + self.outer_expand_dir[pos][1],
            3 - pos)

        # Inner expand
        for p in self.inner_expand_dir[pos][grid[row][col]]:
            self.dfs(grid, N, row, col, p)
        return True

    def valid(self, N, row, col, pos):
        return 0 <= row <= N - 1 and 0 <= col <= N - 1 and not self.visited[row][col][pos]


class Solution(object):
    def dfs(self, y, x, k):
        if y < 0 or y >= self.h or x < 0 or x >= self.w or self.visited[y][x][k]:
            return
        
        if self.grid[y][x] == ' ':
            self.visited[y][x] = [1] * 4
            self.dfs(y+1, x, 0)
            self.dfs(y-1, x, 2)
            self.dfs(y, x-1, 1)
            self.dfs(y, x+1, 3)
        else:
            key = (k, self.grid[y][x])
            for i in self.idxmap[key]:
                self.visited[y][x][i] = 1
                dy, dx, dk = self.nextmap[i]
                self.dfs(y + dy, x + dx, dk)

    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        self.w = len(grid[0])
        self.h = len(grid)
        self.visited = [[[0] * 4 for _ in range(self.w)] for _ in range(self.h)]
        self.counter = 0
        self.grid = grid
        self.nextmap = {0: (-1, 0, 2), 1:(0, 1, 3), 2: (1, 0, 0), 3: (0, -1, 1)}
        self.idxmap = {(0, '/'): (0, 3), (3, '/'): (0, 3),
                       (1, '/'): (1, 2), (2, '/'): (1, 2),
                       (0, '\\'): (0, 1), (1, '\\'): (0, 1),
                       (2, '\\'): (2, 3), (3, '\\'): (2, 3)}
        
        for y in range(self.h):
            for x in range(self.w):
                for k in range(4):
                    if not self.visited[y][x][k]:
                        self.dfs(y, x, k)
                        self.counter += 1

        return self.counter



# Approach 1: DFS
# Devide each cell into 4 pieces numbered its position as:
# -------
# | \0 /|
# |1 X 2|
# |/ 3 \|
# -------
# Using inner_expand_dir to indicate which sub-cell to expand inside a cell
# Using outter_expand_dir to the only adjacent sub-cell,
# Notice the adjacent sub-cell always with position of (3 - previous pos)

# Approach 2: Union Find
# https://leetcode.com/problems/regions-cut-by-slashes/discuss/233278/Java-better-solution-with-Union-Find-100-(time)
