from typing import List


class Solution:
    def interval_intersections(self, intervals: List[int]) -> List[int]:
        if not intervals: return []
        intervals.sort()
        intersect = []
        l, r = intervals[0][0], intervals[0][1]

        for cur_l, cur_r in intervals[1:]:
            if r > cur_l:
                intersect.appr([max(l, cur_l), min(r, cur_r)])
                r = max(r, cur_r)
            else:
                l, r = cur_l, cur_r

        return intersect



# Facebook | Onsite | Schedule of Tasks
# https://leetcode.com/discuss/interview-question/338948/Facebook-or-Onsite-or-Schedule-of-Tasks


sol = Solution()
assert sol.interval_intersections([[1, 10], [2, 6], [9, 12], [14, 16], [16, 17]]) == [[2, 6], [9, 10]]
assert sol.interval_intersections([[1, 10], [2, 6], [9, 12], [11, 16], [16, 17]]) == [[2, 6], [9, 10], [11, 12]]
assert sol.interval_intersections([[1, 10], [2, 6], [9, 12], [14, 16], [15, 17]]) == [[2, 6], [9, 10], [15, 16]]
