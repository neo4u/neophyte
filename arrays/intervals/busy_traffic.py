from typing import List
import collections


class Solution:
    def __init__(self):
        self.tree_map = collections.defaultdict(list)

    def build_treemap(self, intervals):
        for s, e, speed in intervals:
            self.tree_map[s].append(speed)
            self.tree_map[e].append(-speed)
        print(sorted(self.tree_map))
        print([self.tree_map[key] for key in sorted(self.tree_map)])
        print()

    def query_treemap(self):
        speed, times, output = 0, sorted(self.tree_map), []
        no_of_cars, n = 0, len(times)

        for i in range(n):
            prv_sp, cur_sp = times[i - 1], times[i]
            if i > 0: output.append([prv_sp, cur_sp, speed // no_of_cars])
            for each_sp in self.tree_map[times[i]]:
                no_of_cars += (-1 if each_sp < 0 else 1)
                speed = speed + each_sp

        return output

    def get_avg_speeds(self, intervals):
        self.build_treemap(intervals)
        return self.query_treemap()


# Busy Traffic [Google Onsite Interview]
# https://leetcode.com/discuss/interview-question/294744/Google-or-Onsite-or-Busy-traffic


sol = Solution()
assert sol.get_avg_speeds([[5, 15, 20], [10, 20, 30], [7, 25, 10], [20, 25, 40]]) == [
    [5, 7, 20], [7, 10, 15], [10, 15, 20], [15, 20, 20], [20, 25, 25]
]
sol = Solution()
assert sol.get_avg_speeds([[0, 14, 90], [3, 15, 80]]) == [[0, 3, 90], [3, 14, 85], [14, 15, 80]]
sol = Solution()
assert sol.get_avg_speeds([[5, 15, 20], [10, 20, 30]]) == [[5, 10, 20], [10, 15, 25], [15, 20, 30]]
sol = Solution()
assert sol.get_avg_speeds([[5, 15, 20], [10, 20, 30], [7, 25, 10]]) == [
    [5, 7, 20], [7, 10, 15], [10, 15, 20], [15, 20, 20], [20, 25, 10]
]
sol = Solution()
assert sol.get_avg_speeds([[5, 15, 20], [10, 20, 30]]) == [[5, 10, 20], [10, 15, 25], [15, 20, 30]]
sol = Solution()
assert sol.get_avg_speeds([[0, 14, 90], [3, 15, 80]]) == [[0, 3, 90], [3, 14, 85], [14, 15, 80]]
sol = Solution()
assert sol.get_avg_speeds([[0, 14, 90], [16, 20, 70], [3, 18, 80]]) == [
    [0, 3, 90], [3, 14, 85], [14, 16, 80], [16, 18, 75], [18, 20, 70]
]
