class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        start, end = newInterval.start, newInterval.end
        result, i = [], 0

        while i < len(intervals):
            if start <= intervals[i].end:
                if end < intervals[i].start: break
                start = min(start, intervals[i].start)
                end = max(end, intervals[i].end)
            else:
                result.append(intervals[i])
            i += 1

        result.append(Interval(start, end))
        result += intervals[i:]
        return result


class SolutionBinarySearch(object):
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
        # python implementation of bisect.bisect_left and bisect_right using binary search. Very straightforward.
        # https://github.com/python/cpython/blob/master/Lib/bisect.py
        low = bisect.bisect_left([i.end for i in intervals], newInterval.start) # Find a place for the start
        high = bisect.bisect_right([i.start for i in intervals], newInterval.end) # Fina a place for the end

        # determine left half, newInterval.start > intervals[low - 1].end
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

# 57. Insert Interval
# https://leetcode.com/problems/insert-interval/

# By far the best solution I have seen is of O(n) time (some solutions claim to be of O(logn) turns out to be O(n)).
# One of the simplest ideas is to compare each interval in intervals (intervals[i])
# with newInterval and then perform respective operations according to their relationships.

# If they overlap, merge them to newInterval;
# If intervals[i] is to the left of newInterval, push intervals[i] to the result vector;
# If newInterval is to the left of intervals[i], push newInterval and all the remaining intervals (intervals[i], ..., intervals[n - 1]) to the result vector.
# The code is as follows.

# Time: O(log(n)) or O(n). Not fully sure the finds for low and high take log(n),
#       but the last return statement may take O(n)
# Space: O(n)
