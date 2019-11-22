from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if not n: return []
        matrix = [[None for _ in range(n)] for _ in range(n)]
        num = 1
        l, r, u, d = 0, n - 1, 0, n - 1

        while l <= r and u <= d:
            for i in range(l, r + 1):
                matrix[u][i] = num; num += 1
            u += 1

            for i in range(u, d + 1):
                matrix[i][r] = num; num += 1
            r -= 1

            if u <= d:
                for i in reversed(range(l, r + 1)):
                    matrix[d][i] = num; num += 1
                d -= 1

            if l <= r:
                for i in reversed(range(u, d + 1)):
                    matrix[i][l] = num; num += 1
                l += 1
        return matrix


# 59. Spiral Matrix II
# https://leetcode.com/problems/spiral-matrix-ii/description/
