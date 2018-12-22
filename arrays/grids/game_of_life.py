class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.neighbors = [
            (0, 1), (0, -1), (1, 0), (-1, 0),
            (-1, -1), (1, 1), (-1, 1), (1, -1)
        ]

        m,n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                count = self.nnb(board,i,j)
                if board[i][j] in [0, 2]:
                    if count == 3: board[i][j] = 2
                else:
                    if count < 2 or count > 3: board[i][j] = 3

        for i in range(m):
            for j in range(n):
                if board[i][j] == 2: board[i][j] = 1
                if board[i][j] == 3: board[i][j] = 0

    def nnb(self, board, i, j):
        count = 0
        m, n = len(board), len(board[0])
        for d in self.neighbors:
            if 0 <= i + d[0] < m and 0 <= j + d[1] < n:
                count += board[i + d[0]][j + d[1]] % 2 
        return count


# 289. Game of Life
# https://leetcode.com/problems/game-of-life/

# We denote:
# 2 to represent trainsition dead -> live
# 3 to represent trainsition live -> dead

# These are the possible states and conditions:

# Current State: Dead (0)
# Neighbours conditions:
# - < 2     -> remain dead
# - == 2    -> remain dead
# - == 3    -> make alive
# - > 3     -> remain dead

# Current State: Alive (1)
# Neighbours conditions:
# - < 2     -> make dead
# - == 2    -> remain alive
# - == 3    -> remain alive
# - > 3     -> make dead

# We only need to care about the following two conditions as they cause a switch of state:
# | State |live neighbrs | new value | change |
# |-------|--------------|-----------|--------|
# | alive | < 2 and > 3  | 3         | 1->0   |
# | dead  | 3            | 2         | 0->1   |

# Complexity
# Time: O(m * n)
# Space: O(1)