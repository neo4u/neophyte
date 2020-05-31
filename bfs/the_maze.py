from typing import List


# Approach 1: DFS


# Approach 2: BFS
class Solution:
    def hasPath(self, maze: List[List[int]], src: List[int], dst: List[int]) -> bool:
        if src == dst: return True
        m, n = len(maze), len(maze[0])
        q, maze[src[0]][src[1]] = [src], 2
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while q:
            i, j = q.pop(0)

            for dx, dy in dirs:
                r, c = i, j
                while self.not_wall(maze, m, n, r + dx, c + dy): r += dx; c += dy

                if maze[r][c] == 2: continue
                if [r, c] == dst: return True

                q.append([r, c])
                maze[r][c] = 2

        return False

    def not_wall(self, maze, m, n, i, j):
        return 0 <= i <= m - 1 and 0 <= j <= n - 1 and maze[i][j] != 1


# 490. The Maze
# https://leetcode.com/problems/the-maze/description/
