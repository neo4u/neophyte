#  1  2  3  4
#  4  5  6  7
# -3 -3 -3 -3


#  -3  2  3  4
#  -3  5  6  7
#  -3  1  2  3
#  -3 -3 -3 -3


class Solution(object):
    def candyCrush(self, board):
        R, C = len(board), len(board[0])
        todo = False

        for r in range(R):
            for c in range(C - 2):
                if abs(board[r][c]) == abs(board[r][c + 1]) == abs(board[r][c + 2]) != 0:
                    board[r][c] = board[r][c + 1] = board[r][c + 2] = -abs(board[r][c])
                    todo = True

        for r in range(R - 2):
            for c in range(C):
                if abs(board[r][c]) == abs(board[r + 1][c]) == abs(board[r + 2][c]) != 0:
                    board[r][c] = board[r + 1][c] = board[r + 2][c] = -abs(board[r][c])
                    todo = True

        for c in range(C):
            wr = R - 1
            for r in range(R - 1, -1, -1):
                if board[r][c] > 0:
                    board[wr][c] = board[r][c]
                    wr -= 1
            for wr in range(wr, -1, -1):
                board[wr][c] = 0

        return self.candyCrush(board) if todo else board
