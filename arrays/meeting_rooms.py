class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        for i in range(1, len(intervals)):
            prev, curr = intervals[i - 1], intervals[i]
            if curr[0] < prev[1]: return False

        return True


# 252. Meeting Rooms
# https://leetcode.com/problems/meeting-rooms/description/
