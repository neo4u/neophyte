from typing import List


class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        result = []
        rem_l, rem_r = toBeRemoved

        for l, r in intervals:
            # starts after end or ends before start of toBeRemoved
            if r <= rem_l or l >= rem_r: result.append([l, r])  # No Overlap
            else:                                               # There is Overlap
                if l < rem_l: result.append([l, rem_l])         # only l to rem_l should stay, rest removed
                if r > rem_r: result.append([rem_r, r])         # only rem_r to r should stay, rest removed

        return result

# Approach 1: Linear Scan

# Time: O(n)
# Space: O(1)
