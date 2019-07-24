class Solution(object):
    def validTicTacToe(self, board):
        FIRST, SECOND = 'XO'
        x_count = sum(row.count(FIRST) for row in board)
        o_count = sum(row.count(SECOND) for row in board)

        if o_count not in {x_count-1, x_count}: return False
        if self.winner(board, FIRST, ) and x_count-1 != o_count: return False
        if self.winner(board, SECOND) and x_count != o_count: return False

        return True

    def winner(self, board, player):
        n = len(board)
        for i in range(n):
            if all(board[i][j] == player for j in range(n)):
                return True
            if all(board[j][i] == player for j in range(n)):
                return True

        if all(board[i][i] == player for i in range(n)): return True
        if all(board[i][n - 1 - i] == player for i in range(n)): return True

        return False
