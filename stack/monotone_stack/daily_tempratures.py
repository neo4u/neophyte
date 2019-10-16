from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        next_greater, stack = [0] * len(T), []

        for r, num in enumerate(T):
            while stack and T[stack[-1]] < num:
                l = stack.pop()
                next_greater[l] = r - l

            stack.append(r)

        return next_greater


# 739. Daily Temperatures
# https://leetcode.com/problems/daily-temperatures/description/

# Intuition:
# We need a way show how 