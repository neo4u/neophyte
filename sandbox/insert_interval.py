class Solution:
    def insert(self, intervals, newInterval):
        if not intervals: return [newInterval]
        if not newInterval: return intervals
        n = len(intervals)

        i = self.find_left([interval[1] for interval in intervals], newInterval[0])
        j = self.find_right([interval[0] for interval in intervals], newInterval[1])

        if i < n: newInterval[0] = min(newInterval[0], intervals[i][0])
        if j > 0: newInterval[1] = max(newInterval[1], intervals[j - 1][1])
        l, r = intervals[:i], intervals[j:]

        return l + [newInterval] + r

    # return represents position of interval to merge
    # can do with binary search in log(n)
    def find_left(self, ends, start):
        for i, e in enumerate(ends):
            if e >= start: return i
        else:
            return len(ends)

    # can do with binary search in log(n)
    def find_right(self, starts, end):
        for i, s in enumerate(starts):
            if s > end: return i
        else:
            return len(starts)
