from collections import defaultdict
class Solution:
    def solveSudoku(self, board):
        def could_place(d, row, col):
            return not (d in rows[row] or d in columns[col] or \
                    d in boxes[box_index(row, col)])

        def place_number(d, row, col):
            rows[row][d] += 1
            columns[col][d] += 1
            boxes[box_index(row, col)][d] += 1
            board[row][col] = str(d)

        def remove_number(d, row, col):
            del rows[row][d]
            del columns[col][d]
            del boxes[box_index(row, col)][d]
            board[row][col] = '.'    

        def place_next_numbers(row, col):
            # if we're in the last cell
            # that means we have the solution
            if col == N - 1 and row == N - 1:
                nonlocal sudoku_solved
                sudoku_solved = True
            #if not yet
            else:
                # if we're in the end of the row
                # go to the next row
                if col == N - 1:
                    backtrack(row + 1, 0)
                # go to the next column
                else:
                    backtrack(row, col + 1)

        def backtrack(row = 0, col = 0):
            # if the cell is empty
            if board[row][col] == '.':
                # iterate over all numbers from 1 to 9
                for d in range(1, 10):
                    if could_place(d, row, col):
                        place_number(d, row, col)
                        place_next_numbers(row, col)
                        # if sudoku is solved, there is no need to backtrack
                        # since the single unique solution is promised
                        if not sudoku_solved:
                            remove_number(d, row, col)
            else:
                place_next_numbers(row, col)
                    
        # box size
        n = 3
        # row size
        N = n * n
        # lambda function to compute box index
        box_index = lambda row, col: (row // n ) * n + col // n
        
        # init rows, columns and boxes
        rows = [defaultdict(int) for i in range(N)]
        columns = [defaultdict(int) for i in range(N)]
        boxes = [defaultdict(int) for i in range(N)]
        for i in range(N):
            for j in range(N):
                if board[i][j] != '.': 
                    d = int(board[i][j])
                    place_number(d, i, j)
        
        sudoku_solved = False
        backtrack()

import string
class Solution2:
    def solveSudoku(self, board: List[List[str]]) -> None:
        if not board: return

        visited = set()
        self.build_visited(board, visited)
        self.solve(board, visited)

    def build_visited(self, board, visited):
        for r, board_row in enumerate(board):
            for c, digit in enumerate(board_row):
                if digit != ".": self.add_visited(r, c, digit, visited)

    def solve(self, board, visited):
        for r, board_row in enumerate(board):
            for c, curr_digit in enumerate(board_row):
                if curr_digit != ".": continue

                for new_digit in string.digits[1:]:
                    if not self.valid(r, c, new_digit, visited): continue

                    board[r][c] = new_digit
                    self.add_visited(r, c, new_digit, visited)
                    if self.solve(board, visited): return True
                    self.remove_visited(r, c, new_digit, visited)
                    board[r][c] = curr_digit

                return False

        return True

    def remove_visited(self, r, c, digit, visited):
        visited.remove("row" + str(r) + ":" + str(digit))
        visited.remove("col" + str(c) + ":" + str(digit))
        visited.remove("block" + str(r // 3) + "-" + str(c // 3) + ":" + str(digit))

    def add_visited(self, r, c, digit, visited):
        visited.add("row" + str(r) + ":" + str(digit))
        visited.add("col" + str(c) + ":" + str(digit))
        visited.add("block" + str(r // 3) + "-" + str(c // 3) + ":" + str(digit))

    def valid(self, r, c, digit, visited):
        return (
            "row" + str(r) + ":" + digit not in visited
            and "col" + str(c) + ":" + digit not in visited
            and "block" + str(r // 3) + "-" + str(c // 3) + ":" + str(digit) not in visited
        )



class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        self.board = board
        self.solve()

    def findUnassigned(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == ".":
                    return row, col
        return -1, -1

    def solve(self):
        row, col = self.findUnassigned()
        #no unassigned position is found, puzzle solved
        if row == -1 and col == -1:
            return True
        for num in ["1","2","3","4","5","6","7","8","9"]:
            if self.isSafe(row, col, num):
                self.board[row][col] = num
                if self.solve():
                    return True
                self.board[row][col] = "."

        return False

    def isSafe(self, row, col, ch):
        boxrow = row // 3
        boxcol = col // 3
        if self.checkrow(row,ch) and self.checkcol(col,ch) and self.checksquare(boxrow, boxcol, ch):
            return True
        return False

    def checkrow(self, row, ch):
        for col in range(9):
            if self.board[row][col] == ch:
                return False
        return True

    def checkcol(self, col, ch):
        for row in range(9):
            if self.board[row][col] == ch:
                return False
        return True

    def checksquare(self, b_row, b_col, ch):
        for r in range(b_row * 3, b_row * 3 + 3):
            for c in range(b_col * 3, b_col * 3 + 3):
                if self.board[r][c] == ch: return False
        return True

board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]
solved = [["5","3","4","6","7","8","9","1","2"],
          ["6","7","2","1","9","5","3","4","8"],
          ["1","9","8","3","4","2","5","6","7"],
          ["8","5","9","7","6","1","4","2","3"],
          ["4","2","6","8","5","3","7","9","1"],
          ["7","1","3","9","2","4","8","5","6"],
          ["9","6","1","5","3","7","2","8","4"],
          ["2","8","7","4","1","9","6","3","5"],
          ["3","4","5","2","8","6","1","7","9"]]

# block 0, 0 - 0, 0 to 3, 3
# block 1, 1 - 3, 3 to 6, 6
# block 2, 2 - 6, 6 to 9, 9

sol = Solution()
sol.solveSudoku(board)
assert board == solved