import heapq


# Definition for an Interval.
class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def employeeFreeTime(self, schedule: 'list<list<Interval>>') -> 'list<Interval>':
        q = [(iv.start, iv.end) for emp_ivs in schedule for iv in emp_ivs]
        heapq.heapify(q)

        s, e = heapq.heappop(q)
        prev_e, result = e, []

        while q:
            s, e = heapq.heappop(q)
            if s > prev_e:
                result.append(Interval(prev_e, s))
                prev_e = e
            else:
                prev_e = max(prev_e, e)

        return result


# 759. Employee Free Time
# https://leetcode.com/problems/employee-free-time/description/


# Steps:
# 1. We sort all the intervals by the starts, using a heap,
#    we could've just sorted but we need to use the heappop so we use heap
# 2. When we pop from the pq we get the next start of all employee's busy intervals
# 3. The interval between any employee's busy interval end
#    and this employee's busy start gives one interval towards total employee free time
# 4. So if curr employee's busy start is > prev employee's busy end then we append the interval from [prev_e, e] to result
#    and then we update the curr employee's busy end to prev_e
# 5. Else if curr employee's busy start is <= prev employee's busy end then we only need to update the prev_e to max(prev_e, e)
#    This is because the prev employee's end could be after the curr employee's end.


sol = Solution()
ans = sol.employeeFreeTime([
    [Interval(1, 2), Interval(5, 6)],
    [Interval(1, 3)],
    [Interval(4, 10)]
])

assert isinstance(ans[0], Interval)
assert ans[0].start == 3 and ans[0].end == 4
