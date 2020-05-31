class Solution:
    def setZeroes(self, matrix):
        is_row0, is_col0 = False, False
        m, n = len(matrix), len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] != 0: continue
                if i == 0: is_row0 = True
                if j == 0: is_col0 = True
                matrix[0][j] = 0
                matrix[i][0] = 0

        for i in range(1, m):
            for j in range(1, n):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0

        if is_row0:
            for j in range(n):
                matrix[0][j] = 0

        if is_col0:
            for i in range(m):
                matrix[i][0] = 0


# 73. Set Matrix Zeroes
# https://leetcode.com/problems/set-matrix-zeroes/description/
