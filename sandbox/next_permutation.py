class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        r = len(nums) - 1

        while r > 0 and nums[r] <= nums[r - 1]: r -= 1
        if r == 0:
            nums = self.reverse(nums, 0, n - 1)
            return

        pivot, to_replace = r - 1, 0

        for i in range(n - 1, pivot, -1):
            if nums[i] <= nums[pivot]: continue
            to_replace = i
            break

        nums[pivot], nums[to_replace] = nums[to_replace], nums[pivot]
        self.reverse(nums, pivot + 1, n - 1)

    def reverse(self, nums, l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1; r -= 1
