from typing import List
from heapq import heappop, heappush


from heapq import heappush, heappop


class Solution:
    def shortestDistance(self, maze: List[List[int]], src: List[int], dst: List[int]) -> int:
        if not maze or not maze[0]: return -1

        sx, sy, self.maze = *src, maze
        self.m, self.n = len(maze), len(maze[0])
        q, visited_dist = [(0, sx, sy)], {(sx, sy): 0}
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))

        while q:
            dist, i, j = q.pop(0)
            if [i, j] == dst: return dist

            for dx, dy in dirs:
                r, c, d = i, j, 0
                while self.valid(r + dx, c + dy): r += dx; c += dy; d += 1

                if (r, c) not in visited_dist or dist + d < visited_dist[(r, c)]:
                    visited_dist[(r, c)] = dist + d
                    heappush(q, (dist + d, r, c))
                    if [r, c] == dst: return dist + d

        return -1

    def valid(self, i, j):
        return 0 <= i <= self.m - 1 and 0 <= j <= self.n - 1 and self.maze[i][j] == 0


# no early return, although online judge doesn't test for cases that exercises early return as faulty
from heapq import heappush, heappop
class Solution:
    def shortestDistance(self, maze: List[List[int]], src: List[int], dst: List[int]) -> int:
        if not maze or not maze[0]: return -1

        sx, sy, self.maze = *src, maze
        self.m, self.n = len(maze), len(maze[0])
        q, visited_dist = [(0, sx, sy)], {(sx, sy): 0}
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))

        while q:
            dist, i, j = heappop(q)
            for dx, dy in dirs:
                r, c, d = i, j, 0
                while self.valid(r + dx, c + dy): r += dx; c += dy; d += 1
                if (r, c) not in visited_dist or dist + d < visited_dist[(r, c)]:
                    visited_dist[(r, c)] = dist + d
                    if [r, c] == dst: return dist + d
                    heappush(q, (dist + d, r, c))

        return -1

    def valid(self, i, j):
        return 0 <= i <= self.m - 1 and 0 <= j <= self.n - 1 and self.maze[i][j] == 0



# 505. The Maze II
# https://leetcode.com/problems/the-maze-ii/description/


sol = Solution()
MAZE = [[0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0]]
assert sol.shortestDistance(MAZE, [0, 4], [3, 2]) == -1
MAZE = [[0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0]]
assert sol.shortestDistance(MAZE, [0, 4], [4, 4]) == 12


1 