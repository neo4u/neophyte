import collections
from typing import List

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        counts, result = collections.Counter(nums), 0

        for num, freq in counts.items():
            if k == 0 and freq >= 2:
                result += 1

            if k > 0 and num + k in counts:
                result += 1

        return result


# 532. K-diff Pairs in an Array
# https://leetcode.com/problems/k-diff-pairs-in-an-array/description/

sol = Solution()
assert sol.findPairs([3, 1, 4, 1, 5], 2) == 2
