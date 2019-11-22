from typing import List


class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []

        r, c, m, n = 0, 0, len(matrix), len(matrix[0])
        result = [None] * (m * n)

        for i in range(m * n):
            result[i] = matrix[r][c]

            # prepare next index
            if (r + c) % 2 == 0:                # If 0, 2, 4, 6...cuz even diags go up
                if c == n - 1:  r += 1          # We hit the last col, so go down to the next row
                elif r == 0:    c += 1          # We hit the top row (first), so go right to next col
                else:           r -= 1; c += 1  # Go to one step up to prev row and next col

            else:                               # If 1, 3, 5, 7...cuz even diags go up
                if r == m - 1:  c += 1          # We hit the last row, so go right to the next col
                elif c == 0:    r += 1          # We hit the left most col (first), so go down to next row
                else:           r += 1; c -= 1  # Go to one step up to prev row and next col

        return result


# 498. Diagonal Traverse
# https://leetcode.com/problems/diagonal-traverse/description/

# Warning: 
# Note that the below lines look they can be in any order, But that will result in error
# if c == n - 1:  r += 1          # We hit the last col, so go down to the next row
# elif r == 0:    c += 1          # We hit the top row (first), so go right to next col

# if r == m - 1:  c += 1          # We hit the last row, so go right to the next col
# elif c == 0:    r += 1          # We hit the left most col (first), so go down to next row

# We shud be careful of corners like when we reach 6 in figure below:
# as it can be reached by going up in odd case and can lead to first row
# and last column in the same iteration but this should only cause us to go down
# and not right to next column. this can be avoided by checking for reaching
# the last column first, and then checking for reaching the first row.

# 1 2 6
# 3 5 7
# 4 8 9
