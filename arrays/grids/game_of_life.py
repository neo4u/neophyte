from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        DEAD = [0, 2]
        self.nbrs = [
            (0, 1), (0, -1), (1, 0), (-1, 0),
            (-1, -1), (1, 1), (-1, 1), (1, -1)
        ]

        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                count = self.live_nbrs(board, i, j)
                if board[i][j] in DEAD:             # dead and 3 nbrs -> bring to life
                    if count == 3: board[i][j] = 2
                else:                               # alive and bad conditions -> make dead
                    if count < 2 or count > 3: board[i][j] = 3

        for i in range(m):
            for j in range(n):
                if board[i][j] == 2: board[i][j] = 1
                if board[i][j] == 3: board[i][j] = 0

    def live_nbrs(self, board, i, j):
        count = 0
        m, n = len(board), len(board[0])
        for dx, dy in self.nbrs:
            x, y = i + dx, j + dy
            if not self.valid_alive(board, x, y, m, n): continue
            count += 1 # returns 1 for 1, 3, and 0 for 0, 2, Remember it could be either of 0, 1, 2, 3

        return count

    def valid_alive(self, board, x, y, m, n):
        return 0 <= x <= m - 1 and 0 <= y <= n - 1 and board[x][y] % 2 == 1


# 289. Game of Life
# https://leetcode.com/problems/game-of-life/

# We denote two transistion states:
# 2 to represent a trainsition state of going from dead -> live, hence % 2 == 0 implies currently dead
# 3 to represent a trainsition state of going from live -> dead, hence % 2 == 1 implies currently alive

# These are the possible states and conditions:

# If Current State is Dead (0)
# Neighbours conditions:
# - < 2     -> remain dead
# - == 2    -> remain dead
# - == 3    -> make alive
# - > 3     -> remain dead

# If Current State is Alive (1)
# Neighbours conditions:
# - < 2     -> make dead
# - == 2    -> remain alive
# - == 3    -> remain alive
# - > 3     -> make dead

# while counting live neighbors:
# - 2 represents a dead nbr
# - 3 represents a live nbr

# Thus only the following 2 conditions a switch of state:
# | State |live neighbrs | new value | transition it represents |
# |-------|--------------|-----------|--------------------------|
# | dead  | 3            | 2         | 0  ->  1                 |
# | alive | < 2 and > 3  | 3         | 1  ->  0                 |

# Complexity
# Time: O(m * n)
# Space: O(1)
