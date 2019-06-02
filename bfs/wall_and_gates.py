class Solution:
    INF = 2**31 - 1

    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not rooms[0]: return

        m, n = len(rooms), len(rooms[0])
        q, dirs = [], [[0, -1], [0, 1], [-1, 0], [1, 0]]

        for i in range(m):
            for j in range(n):
                if rooms[i][j] != 0: continue
                q.append([i, j, 0])

        while q:
            i, j, d = q.pop(0)

            for dx, dy in dirs:
                x, y = i + dx, j + dy
                if not self.valid_empty(x, y, m, n, rooms): continue
                q.append([x, y, d + 1])
                rooms[x][y] = d + 1

    def valid_empty(self, i, j, m, n, rooms):
        return 0 <= i <= m - 1 and 0 <= j <= n - 1 and rooms[i][j] == self.INF


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
