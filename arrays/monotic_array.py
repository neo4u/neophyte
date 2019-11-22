from typing import List


# 1 Pass early exit
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        n = len(A)
        if n < 2: return True
        inc, dec = True, True

        for i in range(1, n):
            cur, prv = A[i], A[i - 1]
            if prv < cur:   inc = False
            elif prv > cur: dec = False
            if not (inc or dec): return False

        return inc or dec


class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        return self.is_down(A) or self.is_up(A)

    def is_up(self, A):
        prev = A[0]

        for curr in A:
            if curr < prev: return False
            prev = curr

        return True

    def is_down(self, A):
        prev = A[0]

        for curr in A:
            if curr > prev: return False
            prev = curr

        return True


# 896. Monotonic Array
# https://leetcode.com/problems/monotonic-array/description/
