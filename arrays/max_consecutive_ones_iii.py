from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_len = 0
        l, r = 0, 0
        n = len(nums)

        while r < n:
            if nums[r] == 0:    l = r + 1
            else:               max_len = max(max_len, r - l + 1)
            r += 1

        return max_len




# 1004. Max Consecutive Ones III
# https://leetcode.com/problems/max-consecutive-ones-iii/discuss/


# Approach 1: Sliding Window

# [1,1,0,1,1,1]
#        l
#             r

# Approach 2: Binary Search
