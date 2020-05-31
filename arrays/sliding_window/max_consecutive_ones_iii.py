from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, r = 0, 0
        zero, max_len = 0, 0
        n = len(nums)

        while r < n:
            if nums[r] == 0: zero += 1
            while zero > k:
                if nums[l] == 0: zero -= 1
                l += 1

            max_len = max(max_len, r - l + 1)
            r += 1

        return max_len


# 1004. Max Consecutive Ones III
# https://leetcode.com/problems/max-consecutive-ones-iii/description/
