from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if matrix == []: return []
        left, right = 0, len(matrix[0]) - 1
        up, down = 0, len(matrix) - 1
        res = []

        while left <= right and up <= down:
            for i in range(left, right+1):
                res.append(matrix[up][i])
            up += 1

            for i in range(up, down+1):
                res.append(matrix[i][right])
            right -= 1

            if up <= down:
                for i in range(right, left-1, -1):
                    res.append(matrix[down][i])
            down -= 1

            if left <= right:
                for i in range(down, up-1, -1):
                    res.append(matrix[i][left])
            left += 1

        return res


# 54. Spiral Matrix
# https://leetcode.com/problems/spiral-matrix/description/