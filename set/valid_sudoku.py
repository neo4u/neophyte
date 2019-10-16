from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        visited = set()

        for i in range(9):
            for j in range(9):
                num = board[i][j]

                if num == '.': continue
                row_tup, col_tup, blk_tup = ('r', num, i), ('c', num, j), ('b', num, i // 3, j // 3)
                if row_tup in visited  or col_tup in visited or blk_tup in visited: return False

                visited.add(row_tup)
                visited.add(col_tup)
                visited.add(blk_tup)

        return True


# 36. Valid Sudoku
# https://leetcode.com/problems/valid-sudoku/description/
