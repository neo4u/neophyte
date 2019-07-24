import collections
from typing import List

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        prev = None
        avoid = using = 0

        for x in sorted(count):
            if x - 1 != prev:
                avoid, using = max(avoid, using), x * count[x] + max(avoid, using)
            else:
                avoid, using = max(avoid, using), x * count[x] + avoid
            prev = x

        return max(avoid, using)

# 740. Delete and Earn
# https://leetcode.com/problems/delete-and-earn/description/
