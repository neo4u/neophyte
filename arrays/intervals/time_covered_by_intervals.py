class Solution:
    def time_covered_by_intervals(self, intervals: list) -> list:
        intervals.sort()
        merged = [list(intervals[0])]

        for i in intervals[1:]:
            if merged[-1][1] < i[0]:
                merged.append(list(i))
            else:
                merged[-1][1] = max([i[1], merged[-1][1]])

        return sum([b - a for a, b in merged])


sol = Solution()
assert sol.time_covered_by_intervals([(1,4), (2,3)]) == 3
assert sol.time_covered_by_intervals([(4,6), (1,2)]) == 3
assert sol.time_covered_by_intervals([(1,4), (6, 8), (2, 4), (7, 9), (10, 15)]) == 11
