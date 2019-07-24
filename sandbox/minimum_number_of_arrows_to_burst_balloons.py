class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        points.sort(key=lambda x: x[1])
        curr_end, arrows = points[0][1], 1

        for s, e in points:
            if s > curr_end:
                arrows += 1
                curr_end = e

        return arrows


# [[10,16], [2,8], [1,6], [7,12]]
# [1,6] [2,8], [7, 12], [10, 16]

# ce: 6
# a: 1

# ce: 12
# a 2


# 452. Minimum Number of Arrows to Burst Balloons
# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/
