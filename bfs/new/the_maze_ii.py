from heapq import heappop, heappush

class Solution:
    def shortestDistance(self, maze, start, destination):
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))

        sx, sy = start
        q, m, n, visited = [(0, sx, sy)], len(maze), len(maze[0]), {(sx, sy): 0}
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))

        while q:
            dist, i, j = heappop(q)
            if [i, j] == destination: return dist

            for x, y in dirs:
                r, c, d = i, j, 0
                
                while 0 <= r + x <= m - 1 and 0 <= c + y <= n - 1 and maze[r + x][c + y] == 0:
                    r += x
                    c += y
                    d += 1

                if (r, c) not in visited or dist + d < visited[(r, c)]:
                    visited[(r, c)] = dist + d
                    heappush(q, (dist + d, r, c))

        return -1

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

