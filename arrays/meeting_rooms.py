from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        n = len(intervals)
        intervals.sort()

        for i in range(1, n):
            prev, curr = intervals[i - 1], intervals[i]
            if curr[0] < prev[1]: return False
        return True


# 252. Meeting Rooms
# https://leetcode.com/problems/meeting-rooms/description/
