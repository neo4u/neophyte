from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l, r = 0, 0
        zero, max_len = 0, 0
        n, k = len(nums), 1

        while r < n:
            if nums[r] == 0: zero += 1
            while zero > k:
                if nums[l] == 0: zero -= 1
                l += 1

            max_len = max(max_len, r - l + 1)
            r += 1

        return max_len


# 487. Max Consecutive Ones II
# https://leetcode.com/problems/max-consecutive-ones-ii/description/
