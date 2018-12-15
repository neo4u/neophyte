import bisect

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        # corner case
        if not intervals:
            return [newInterval]
        if not newInterval:
            return intervals

        n = len(intervals)
        # binary search
        low = bisect.bisect_left([i.end for i in intervals], newInterval.start)
        high = bisect.bisect_right([i.start for i in intervals], newInterval.end)

        # determine left half, newInterval.start > inervals[low - 1].end
        # if newInterval has overlap with interval[low], expand it
        if low < n:
            newInterval.start = min(newInterval.start, intervals[low].start)
        left = intervals[:low]

        # determine right half, newInterval.end < intervals[high].start
        # if newInterval has overlap with interval[high - 1], expand it
        if high > 0:
            newInterval.end = max(newInterval.end, intervals[high - 1].end)
        right = intervals[high:]

        # return the merged list
        return left + [newInterval] + right
