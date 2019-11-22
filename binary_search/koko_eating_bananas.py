from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        l, r = 1, max(piles)
        while l < r:
            mid = (l + r) // 2
            if not self.can_eat_in_h(mid, H, piles):    l = mid + 1
            else:                                       r = mid

        return l

    def can_eat_in_h(self, k, h, piles):
        return sum(math.ceil(p / k) for p in piles) <= h
        # return sum((p - 1) // k + 1 for p in piles) <= h, Also another way to get the same value


# 875. Koko Eating Bananas
# https://leetcode.com/problems/koko-eating-bananas/description/


# Steps:
# - we use a min and max as l, r and binary search for the optimal speed, (min) required to finish all bananas
# - If we find a speed which works, we keep reducing until we can't finish
# - If we find a speed that doesn't work we keep increasing till we can
# - The last part is the function "possible":
#   This is basically Math.ceil(p / K) for each pile,
#   sorta like distance / speed = time for each then sum all those times

# Time: O(n * log(max(piles)))
# Size: O(1)
