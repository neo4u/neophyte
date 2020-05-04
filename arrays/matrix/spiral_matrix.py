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


# Steps:
# 1. Set l, r, u, d at the border indexes
#    Then, have a loop while u <= d and l <= r, i.e. bounds don't crossover
# 2. Capture u's row items b/w [l, r], then inc u
# 3. Capture r's col items b/w [u, d], then dec r
# 4. Capture d's row items b/w [r, l], then inc l, important to check bounds here
# 5. Capture l's col items b/w [d, u], then important to check bounds here
