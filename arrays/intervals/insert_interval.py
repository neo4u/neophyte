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

        # low is the index of ends such that, for all e in ends[:low], e < newInt.start
        # high is the index of starts such that, for all s in starts[high:], newInt.end < s
        
        # Essentially finding ends less than newInt's start and starts after newInt's end
        low = bisect.bisect_left([i.end for i in intervals], newInterval.start)     # Find a place for the newInterval start
        high = bisect.bisect_right([i.start for i in intervals], newInterval.end)   # Find a place for the newInterval end

        
        # determine left half, newInterval.start > intervals[low].end
        # if newInterval has overlap with interval[low], merge it by taking min of starts
        if low < n:
            newInterval.start = min(newInterval.start, intervals[low].start)
        left = intervals[:low]

        # determine right half, newInterval.end < intervals[high - 1].start
        # if newInterval has overlap with interval[high - 1], merge it by taking max of ends
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


Bisect left
The return value i is such that all e in a[:i] have e < x, and all e in
a[i:] have e >= x.  So if x already appears in the list, a.insert(x) will
insert just before the leftmost x already there.

    e < x              x <= e
--------------  --------------------
0, ...., i - 1, i, i + 1, ..., n - 1

Bisect right
The return value i is such that all e in a[:i] have e <= x, and all e in
a[i:] have e > x.  So if x already appears in the list, a.insert(x) will
insert just after the rightmost x already there.

    e <= x             x < e
--------------  --------------------
0, ...., i - 1, i, i + 1, ..., n - 1
