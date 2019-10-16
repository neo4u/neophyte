from typing import List


# two-pointer
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = enumerate(nums)
        nums = sorted(nums, key=lambda x: x[1])
        l, r = 0, len(nums) - 1

        while l < r:
            s = nums[l][1] + nums[r][1]

            if s < target:      l += 1
            elif s > target:    r -= 1
            else:               return [nums[l][0], nums[r][0]]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in nums_dict:
                return [nums_dict[diff], i]
            nums_dict[n] = i

        return []


# 1. Two Sum
# https://leetcode.com/problems/two-sum/description/
