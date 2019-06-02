class TicTacToe:
    def __init__(self, n):
        self.rows = [0] * n
        self.cols = [0] * n
        self.diag = 0
        self.anti_diag = 0
        self.n = n

    def move(self, row, col, player):
        to_add = 1 if player == 1 else -1

        self.rows[row] += to_add
        self.cols[col] += to_add
        if row == col: self.diag += to_add
        if row + col == self.n - 1: self.anti_diag += to_add

        if self.n in [abs(self.rows[row]), abs(self.cols[row]),
                      abs(self.diag), abs(self.anti_diag)]:
            return player

        return 0

# ["TicTacToe","move","move","move"]
# [[2],[0,0,2],[1,1,1],[0,1,2]]

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
