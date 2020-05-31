from typing import List


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        result = []
        for i, r in enumerate(nums):
            for j, a in enumerate(r):
                if len(result) <= i + j: result.append([])
                result[i + j].append(a)

        return [a for r in result for a in reversed(r)]


# 1424. Diagonal Traverse II
# https://leetcode.com/problems/diagonal-traverse-ii/description/


# Time: O(n)
# Space: O(n)
