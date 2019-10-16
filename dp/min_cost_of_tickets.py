from typing import List
import collections

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        cost = 0
        last7 = collections.deque()
        last30 = collections.deque()

        for day in days:
            while last7 and last7[0][0] + 7 <= day:
                last7.popleft()
            while last30 and last30[0][0] + 30 <= day:
                last30.popleft()

            last7.append((day, cost + costs[1]))
            last30.append((day, cost + costs[2]))
            cost = min(cost + costs[0], last7[0][1], last30[0][1])

        return cost



# https://leetcode.com/problems/minimum-cost-for-tickets/discuss/226659/Two-DP-solutions-with-pictures


# Time: O(n), where n is the number of travel days.
# Space: O(38). Stricter, it's a sum of duration for all pass types (1 + 7 + 30 in our case).


# 365 day dp
# dp[i] = min({
#               | dp[i - 1] + costs[0],
#         min   | dp[max(0, i - 7)] + costs[1],
#               | dp[max(0, i - 30)] + costs[2]});
