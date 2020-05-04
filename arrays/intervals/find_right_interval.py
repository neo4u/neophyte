from typing import List
import bisect


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        events = sorted([(x[0], i) for i, x in enumerate(intervals)], key=lambda x: x[0])
        starts, idxs = [x[0] for x in events], [x[1] for x in events]
        result, n = [], len(intervals)

        for _, end in intervals:
            pos = bisect.bisect_left(starts, end)
            if pos == n: result.append(-1)
            else:        result.append(idxs[pos])
        return result


# 436. Find Right Interval
# https://leetcode.com/problems/find-right-interval/description/

# Intuition:
# 1. We need to find the least start interval that comes after each intervals end
# 2. We can use binary search to search for where a given interval's end falls in a sorted list of starts
#    the return value of the binary seach will give us the "right" interval of the given interval
