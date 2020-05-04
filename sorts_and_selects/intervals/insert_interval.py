from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start, end = newInterval[0], newInterval[1]
        result, i = [], 0

        while i < len(intervals):
            if start <= intervals[i][1]:
                if end < intervals[i][0]: break
                start = min(start, intervals[i][0])
                end = max(end, intervals[i][1])
            else:
                result.append(intervals[i])
            i += 1

        result.append([start, end])
        result += intervals[i:]
        return result


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals: return [newInterval]
        if not newInterval: return intervals

        n = len(intervals)

        low = bisect.bisect_left([i[1] for i in intervals], newInterval[0]) # Find a place for the[0]
        high = bisect.bisect_right([i[0] for i in intervals], newInterval[1]) # Fina a place for the[1]

        # determine left half, newInterval[0] > intervals[low - 1][1]
        # if newInterval has overlap with interval[low], expand it
        if low < n: newInterval[0] = min(newInterval[0], intervals[low][0])
        left = intervals[:low]

        # determine right half, newInterval[1] < intervals[high][0]
        # if newInterval has overlap with interval[high - 1], expand it
        if high > 0: newInterval[1] = max(newInterval[1], intervals[high - 1][1])
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


# 57. Insert Interval
# https://leetcode.com/problems/insert-interval/

# By far the best solution I have seen is of O(n) time (some solutions claim to be of O(logn) turns out to be O(n)).
# One of the simplest ideas is to compare each interval in intervals (intervals[i])
# with newInterval and then perform respective operations according to their relationships.

# If they overlap, merge them to newInterval;
# If intervals[i] is to the left of newInterval, push intervals[i] to the result vector;
# If newInterval is to the left of intervals[i], push newInterval and all the remaining intervals (intervals[i], ..., intervals[n - 1]) to the result vector.

# Time: O(log(n)) or O(n). Not fully sure the finds for low and high take log(n),
#       but the last return statement may take O(n)
# Space: O(n)


# Bisect left
# The return value i is such that all e in a[:i] have e < x, and all e in
# a[i:] have e >= x.  So if x already appears in the list, a.insert(x) will
# insert just before the leftmost x already there.

#     e < x              x <= e
# --------------  --------------------
# 0, ...., i - 1, i, i + 1, ..., n - 1

# Bisect right
# The return value i is such that all e in a[:i] have e <= x, and all e in
# a[i:] have e > x.  So if x already appears in the list, a.insert(x) will
# insert just after the rightmost x already there.

#     e <= x             x < e
# --------------  --------------------
# 0, ...., i - 1, i, i + 1, ..., n - 1
