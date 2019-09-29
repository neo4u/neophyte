from typing import List


class Solution:
    INF = 2**31 - 1

    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        if not rooms or not rooms[0]: return

        q, self.m, self.n = [], len(rooms), len(rooms[0])
        self.dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for i in range(self.m):
            for j in range(self.n):
                if rooms[i][j] != 0: continue
                q.append((i, j, 0))

        while q:
            i, j, d = q.pop(0)
            for di, dj in self.dirs:
                x, y = i + di, j + dj
                if not self.is_valid_empty_room(rooms, x, y): continue
                q.append((x, y, d + 1))
                rooms[x][y] = d + 1

    def is_valid_empty_room(self, rooms, i, j):
        return 0 <= i <= self.m - 1 and 0 <= j <= self.n - 1 and rooms[i][j] == self.INF


# 286. Walls and Gates
# https://leetcode.com/problems/walls-and-gates/description/

# Key Insights
# 1. We just have to modify distances in place, so nothing to return
# 2. We don't need a visited set in this case, cuz visited means shortest gate was found

# Steps
# 1. We can visit all empty spaces from each gate
# 2. While visiting a cell, if it was already visited from another gate,
#    it means we don't have to visit it again
# 3. Nothing to return

# Time: O(m * n)
# Space: O(m * n)
