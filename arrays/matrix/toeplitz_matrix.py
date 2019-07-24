class Solution(object):
    def isToeplitzMatrix(self, matrix):
        m, n = len(matrix), len(matrix[0])

        for r in range(m - 1):
            for c in range(n - 1):
                if matrix[r][c] != matrix[r + 1][c + 1]:
                    return False
        return True


# 766. Toeplitz Matrix
# https://leetcode.com/problems/toeplitz-matrix/description/

sol = Solution()
assert sol.isToeplitzMatrix([[1,2,3,4],
                             [5,1,2,3],
                             [9,5,1,2]]) == True


