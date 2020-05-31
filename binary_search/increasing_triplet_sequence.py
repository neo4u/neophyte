from typing import List
import bisect


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        tails, size = [0] * n, 0

        for x in nums:
            pos = bisect.bisect_left(tails, x, lo=0, hi=size)
            tails[pos] = x
            size = max(pos + 1, size)
            if size == 3: return True

        return False


# 334. Increasing Triplet Subsequence
# https://leetcode.com/problems/increasing-triplet-subsequence/description/
