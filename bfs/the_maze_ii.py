from heapq import heappop, heappush

class Solution:
    def shortestDistance(self, maze, start, destination):
        if not maze or not len(maze[0]): return -1

        sx, sy = start
        q, self.m, self.n, visited_dist = [(0, sx, sy)], len(maze), len(maze[0]), {(sx, sy): 0}
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))

        while q:
            dist, i, j = heappop(q)
            if [i, j] == destination: return dist

            for x, y in dirs:
                r, c, d = i, j, 0

                while is_valid(r + x, c + y): r += x; c += y; d += 1

                if (r, c) not in visited_dist or dist + d < visited_dist[(r, c)]:
                    visited_dist[(r, c)] = dist + d
                    heappush(q, (dist + d, r, c))

        return -1

    def is_valid(self, i, j):
        return 0 <= i <= self.m - 1 and 0 <= j <= self.n - 1 and maze[i][j] == 0



sol = Solution()

maze = [[0,0,1,0,0],
        [0,0,0,0,0],
        [0,0,0,1,0],
        [1,1,0,1,1],
        [0,0,0,0,0]]
assert sol.shortestDistance(maze, [0,4], [3,2]) == -1
maze = [[0,0,1,0,0],
        [0,0,0,0,0],
        [0,0,0,1,0],
        [1,1,0,1,1],
        [0,0,0,0,0]]
assert sol.shortestDistance(maze, [0,4], [4,4]) == 12
