from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        l, r = 0, n - 1

        while l < r:
            s = nums[l] + nums[r]
            if s < target:      l += 1
            elif s > target:    r -= 1
            else:               return [l + 1, r + 1]


# 167. Two Sum II - Input array is sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
