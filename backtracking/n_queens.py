from typing import List


class Solution:
    def solveNQueens(self, n: int):
        self.n = n
        self.cols = [0] * n
        self.dales = [0] * (2 * n - 1)
        self.hills = [0] * (2 * n - 1)
        self.queens = set()
        self.output = []
        self.bt()
        return self.output

    def could_place(self, row, col):
        return (self.cols[col] + self.dales[row - col] + self.hills[row + col]) == 0

    def place_queen(self, row, col):
        self.queens.add((row, col))
        self.cols[col] = 1
        self.hills[row + col] = 1
        self.dales[row - col] = 1

    def remove_queen(self, row, col):
        self.queens.remove((row, col))
        self.cols[col] = 0
        self.hills[row + col] = 0
        self.dales[row - col] = 0

    def add_solution(self):
        solution = []
        for _, col in sorted(self.queens):
            solution.append('.' * col + 'Q' + '.' * (self.n - col - 1))
        self.output.append(solution)

    def bt(self, row=0):
        for col in range(self.n):
            if self.could_place(row, col):
                self.place_queen(row, col)
                if row + 1 == self.n:
                    self.add_solution()
                else:
                    self.bt(row + 1)
                self.remove_queen(row, col)


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        answers, positions = [], []
        self.bt(answers, positions, 0, n)
        return answers

    def compatible(self, prev_cols_list, curr_col, curr_row):
        for prev_row in range(curr_row):
            if prev_cols_list[prev_row] == curr_col or curr_row - prev_row == abs(prev_cols_list[prev_row] - curr_col):
                return False
        return True

    def bt(self, answers, positions, row, n):
        if row == n:
            answers.append(['.' * p + 'Q' + '.' * (n-1-p) for p in positions])
            return answers
        for col in range(n):
            if self.compatible(positions, col, row):
                positions.append(col)
                self.bt(answers, positions, row+1, n)
                positions.pop()
        return answers
