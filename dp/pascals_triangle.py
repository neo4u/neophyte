from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        prev, result = [], []

        for i in range(numRows):
            curr = []
            for j in range(i + 1):
                to_insert = 1 if j == 0 or j == i else prev[j - 1] + prev[j]
                curr.append(to_insert)

            prev = curr
            result.append(curr)

        return result


# 118. Pascal's Triangle
# https://leetcode.com/problems/pascals-triangle/description/
