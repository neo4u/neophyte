class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if not nums or len(nums) < 2: return 0
        # find the left bound which is 6, and the right bound is 10, these two violates the mono increasking/decreasing stack
        l, r = len(nums) - 1, 0

        mono_stack = []
        # use increasing mono stack to find left bound
        # [2, 6, 4, 8, 10, 9, 15]
        for i, v in enumerate(nums):
            while mono_stack and v < nums[mono_stack[-1]]:
                l = min(l, mono_stack.pop())
            mono_stack.append(i)

        # use decreasing mono stack to find the right bound
        mono_stack = []
        for i in reversed(range(len(nums))):
            while mono_stack and nums[i] > nums[mono_stack[-1]]:
                r = max(r, mono_stack.pop())
            mono_stack.append(i)

        return r - l + 1 if r - l > 0 else 0


# 581. Shortest Unsorted Continuous Subarray
# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/description/
