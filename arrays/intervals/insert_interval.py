from typing import List
import bisect


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start, end = newInterval
        result, i = [], 0

        while i < len(intervals):
            curr = intervals[i]
            if start <= curr[1]:            # if new interval's start is before curr interval's end
                if end < curr[0]: break     # if new interval's end is before curr intervals start then no overlap, so we break
                start = min(start, curr[0])
                end = max(end, curr[1])
            else:
                result.append(intervals[i])
            i += 1

        result.append([start, end])
        result.extend(intervals[i:])
        return result



class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals: return [newInterval]
        if not newInterval: return intervals

        n = len(intervals)

        low = bisect.bisect_left([i[1] for i in intervals], newInterval[0])     # Find a place for the start
        high = bisect.bisect_right([i[0] for i in intervals], newInterval[1])   # Find a a place for the end

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

# Time: O(log(n)) or O(n). Not fully sure the finds for low and high take log(n),
#       but the last return statement may take O(n)
# Space: O(n)


# Intuition
# 1. We're given a list of intervals sorted by the start time,
#    also an interval to insert which could overlap with one or more existing intervals
# 2. We've to handle overlap accordingly, For ex:
#    - No Overlap: intervals = [[1, 2], [9, 10]] and to_insert = [5, 8] := result = [[1, 2], [5, 8], [9, 10]]
#    - Full Overlap: intervals = [[1, 2], [5, 10]] and to_insert = [5, 8] := result = [[1, 2], [5, 10]]
#    - 1 Overlap: intervals = [[1, 2], [8, 10]] and to_insert = [5, 9] := result = [[1, 2], [5, 10]]
#    - > 1 Overlap: intervals = [[1, 5], [8, 10]] and to_insert = [4, 9] := result = [[1, 10]]

# Approach 1: Linear Scan
# 1. Compare the interval with every interval
# 2. Check out if no overlap and push to results, else if overlap merge overlap into the new interval
# 3. We have 3 cases:
#    1. interval[i] | new_interval  [newInt appears to right of curr]
#    2. interval[i]                 [newInt overlaps to the left]
#             | new_interval
#    3. new_interval | interval[i]  [newInt appear to the left of curr]
# 4. In case 1. we just add intervals[i] to result, as no overlap
#    In case 3. we break add newInt to result and then add the remaining intervals to the result and return 
#    Case 3 is the tricky part but simple trick here is to update the start/end variables 

# Time: O(n)
# Space: O(n)

# Approach 2: Binary Search to find overlap indexes
# Steps
# 1. Binary Search ends for e >= new_interval[0],
#    i.e. Find the index i into intervals where all the ends are to the left of i are < new_interval[0]
#    i.e. is find the index of end that comes before new interval's start
# 2. Binary Search starts for s > new_interval[1],
#    i.e. Find the index into intervals where all the starts to the right of i are > new_interval[1]
#    i.e. Find the index of the start that comes after new interval's end
# 3. Use n if there is no such index for both the searches
# 4. Merge new_interval's start with interval i's start
# 5. Merge new_interval's end with interval j - 1's end
# 6. Final form the left part, middle part and right part
# 6. Return the combination of the tree parts

# Example 1: intervals = [1, 3], [6, 9] new = [2, 5]
# starts: [1, 6] | ends: [3, 9]
# i: 0 | j: 1
# left: [] | new_interval: [1, 5] | right: [6, 9]

# Example 2: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]] new = [4,8]
# starts: [1, 3, 6, 8, 12] | ends: [2, 5, 7, 10, 16]
# i: 1 | j: 4
# left: [1,2] | new_interval: [3, 10] | right: [12, 16]

# Example 3: intervals = [[1,5]] new = [2,3]
# starts: [1] | ends: [5]
# i: 0 | j: 1
# left: [] | new_interval: [1,5] | right: []

# Example 4: intervals = [[1,2],[6,9]] new = [3,5]
# starts: [1, 6] | ends: [2, 9]
# i: 1 | j: 1
# left: [1,2] | new_interval: [3,5] | right: [6,9]

