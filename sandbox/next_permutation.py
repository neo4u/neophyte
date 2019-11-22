from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        r = n - 1

        while r > 0 and nums[r] <= nums[r - 1]: r -= 1
        if r == 0: return self.reverse(nums, 0, n - 1)

        pivot_idx, to_replace = r - 1, 0
        for i in range(n - 1, pivot_idx, -1):   # to find the smallest element greater than num at pivot index
            if nums[i] <= nums[pivot_idx]: continue
            to_replace = i
            break

        nums[pivot_idx], nums[to_replace] = nums[to_replace], nums[pivot_idx]
        self.reverse(nums, pivot_idx + 1, n - 1)

    def reverse(self, nums, l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1; r -= 1
