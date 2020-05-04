from typing import List


class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1 = sorted(slots1, key=lambda x: x[0])
        slots2 = sorted(slots2, key=lambda x: x[0])
        m, n = len(slots1), len(slots2)
        i, j, result = 0, 0, []

        while i < m and j < n:
            a, b = slots1[i], slots2[j]
            l, r = max(a[0], b[0]), min(a[1], b[1])

            if l < r and l + duration <= r:
                return [l, l + duration]

            if a[1] < b[1]: i += 1
            else:           j += 1

        return result


# 1229. Meeting Scheduler
# https://leetcode.com/problems/meeting-scheduler/description/
