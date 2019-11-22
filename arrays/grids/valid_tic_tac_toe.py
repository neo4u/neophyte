from typing import List


class Solution(object):
    def validTicTacToe(self, board):
        FIRST, SECOND = 'XO'
        x_count = sum(row.count(FIRST) for row in board)        # Check count of Xs
        o_count = sum(row.count(SECOND) for row in board)       # Check count of Os

        if o_count not in {x_count - 1, x_count}: return False
        if self.winner(board, FIRST) and x_count - 1 != o_count: return False   # Check state, if x is winner
        if self.winner(board, SECOND) and x_count != o_count: return False      # Check state, if o is winner

        return True

    def winner(self, board, player):
        n = len(board)
        for i in range(n):
            if all(board[i][j] == player for j in range(n)): return True
            if all(board[j][i] == player for j in range(n)): return True

        if all(board[i][i] == player for i in range(n)): return True
        if all(board[i][n - 1 - i] == player for i in range(n)): return True

        return False




# 794. Valid Tic-Tac-Toe State
# https://leetcode.com/problems/valid-tic-tac-toe-state/description/

# Intuition:
# 1. "X" always goes first,
# 2. At any time, their counts differ by utmost 1
# 3. if x wins then, o_count == x_count - 1
# 4. if o wins then, x_count == o_count
# 5. if winner
