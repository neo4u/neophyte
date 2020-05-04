from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        count = cur = 0
        for _, r in sorted(intervals, key=lambda i: (i[0], -i[1])):
            if cur >= r: continue
            cur = r
            count += 1

        return count


# 1288. Remove Covered Intervals
# https://leetcode.com/problems/remove-covered-intervals/description/


# Time: O(nlogn)
# Space: O(1)
