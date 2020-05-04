from typing import List


class Solution:
    def time_covered_by_intervals(self, intervals: List[int]) -> List[int]:
        intervals.sort()
        merged = [intervals[0]]

        for curr in intervals[1:]:
            if merged[-1][1] < curr[0]: # no overlap with last interval's end
                merged.append(curr)
            else:
                merged[-1][1] = max([curr[1], merged[-1][1]])

        return sum([b - a for a, b in merged])

# This is basically:
# 1. Merge intervals
# 2. Add the time covered by the intervals.

sol = Solution()
assert sol.time_covered_by_intervals([[1, 4], [2, 3]]) == 3
assert sol.time_covered_by_intervals([[4, 6], [1, 2]]) == 3
assert sol.time_covered_by_intervals([[1, 4], [6, 8], [2, 4], [7, 9], [10, 15]]) == 11
