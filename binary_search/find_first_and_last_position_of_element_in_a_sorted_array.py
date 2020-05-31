class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        print('called')
        l = self.bisect_left(nums, target)
        if l == len(nums) or nums[l] != target: return [-1, -1]
        r = self.bisect_right(nums, target)
        return [l, r]

    def bisect_left(self, nums, target):
        n = len(nums)
        l, r = 0, n

        while l < r:
            mid = (l + r) // 2
            if target <= nums[mid]:
                r = mid
            else:
                l = mid + 1

        return l

    def bisect_right(self, nums, target):
        n = len(nums)
        l, r = 0, n

        while l < r:
            mid = (l + r) // 2
            print(mid)
            if target < nums[mid]:
                r = mid
            else:
                l = mid + 1

        return l - 1


# 34. Find First and Last Position of Element in Sorted Array
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
