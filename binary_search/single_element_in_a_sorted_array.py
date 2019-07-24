class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            if mid % 2 == 1: mid -= 1

            if nums[mid] != nums[mid + 1]:
                r = mid
            else:
                l = mid + 2

        return nums[l]


# 540. Single Element in a Sorted Array
# https://leetcode.com/problems/single-element-in-a-sorted-array/description/