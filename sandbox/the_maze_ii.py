from heapq import heappop, heappush

class Solution:
    def shortestDistance(self, maze, src, dst):
        if not maze or not maze[0]: return -1
        if src == dst: return 0

        sx, sy = src
        q, m, n, visited = [(0, sx, sy)], len(maze), len(maze[0]), {(sx, sy): 0}
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))

        while q:
            dist, i, j = heappop(q)

            for x, y in dirs:
                r, c, d = i, j, 0

                while self.valid(maze, m, n, r + x, c + y):
                    r += x; c += y; d += 1

                if (r, c) not in visited or dist + d < visited[(r, c)]:
                    if [r, c] == dst: return dist + d

                    visited[(r, c)] = dist + d
                    heappush(q, (dist + d, r, c))

        return -1

    def valid(self, maze, m, n, i, j):
        return 0 <= i <= m - 1 and 0 <= j <= n - 1 and maze[i][j] == 0


# no early return, although online judge doesn't test for cases that exercises early return as faulty
class Solution2:
    def shortestDistance(self, maze, src, dst):
        if not maze or not maze[0]: return -1
        if src == dst: return 0

        sx, sy = src
        q, m, n, visited = [(0, sx, sy)], len(maze), len(maze[0]), {(sx, sy): 0}
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))

        while q:
            dist, i, j = heappop(q)

            for x, y in dirs:
                r, c, d = i, j, 0

                while self.valid(maze, m, n, r + x, c + y):
                    r += x; c += y; d += 1

                if (r, c) not in visited or dist + d < visited[(r, c)]:
                    visited[(r, c)] = dist + d
                    if [r, c] == dst: continue
                    heappush(q, (dist + d, r, c))

        return -1 if tuple(dst) not in visited else visited[tuple(dst)]

    def valid(self, maze, m, n, i, j):
        return 0 <= i <= m - 1 and 0 <= j <= n - 1 and maze[i][j] == 0


# 505. The Maze II
# https://leetcode.com/problems/the-maze-ii/description/
