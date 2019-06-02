class Solution(object):
    def isToeplitzMatrix(self, matrix):
        m, n = len(matrix), len(matrix[0])
        return all(r == m - 1  or c == n - 1 or matrix[r + 1][c + 1] == val
                   for r, row in enumerate(matrix)
                   for c, val in enumerate(row))