from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        m, n = len(matrix), len(matrix[0])
        l, r, u, d = 0, n - 1, 0, m - 1
        result = []

        while l <= r and u <= d:
            for i in range(l, r + 1):
                result.append(matrix[u][i])
            u += 1

            for i in range(u, d + 1):
                result.append(matrix[i][r])
            r -= 1

            if u <= d:
                for i in reversed(range(l, r + 1)):
                    result.append(matrix[d][i])
                d -= 1

            if l <= r:
                for i in reversed(range(u, d + 1)):
                    result.append(matrix[i][l])
                l += 1
        return result


# 54. Spiral Matrix
# https://leetcode.com/problems/spiral-matrix/description/
