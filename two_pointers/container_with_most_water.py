from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area, l, r = 0, 0, len(height) - 1

        while l < r:
            max_area = max(max_area, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:   l += 1
            else:                       r -= 1

        return max_area


# 11. Container With Most Water
# https://leetcode.com/problems/container-with-most-water/description/


sol = Solution()

assert sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
