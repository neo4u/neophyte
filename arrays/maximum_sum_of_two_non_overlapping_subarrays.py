from typing import List


class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        # do a CDF so that range sum can easily be calculated
        for i in range(1, len(A)): A[i] += A[i - 1]
        result, l_max, m_max = A[L + M - 1], A[L - 1], A[M - 1]
        n = len(A)

        # window  | --- L --- | --- M --- |
        for i in range(L + M, n):
            l_max = max(l_max, A[i - M] - A[i - L - M])
            result = max(result, l_max + A[i] - A[i - M])

        # window  | --- M --- | --- L --- |
        for i in range(L + M, n):
            m_max = max(m_max, A[i - L] - A[i - L - M])
            result = max(result, m_max + A[i] - A[i - L])

        return result


# So the problem is essentially 2 separate cases.

# But it's important to keep in mind that the L+M maximum could be reached before L & M separate from each other
# So you cannot divide each case into simply 2 steps:

# find the global maximum of the window on the left
# find the maximum of the second window in the region to the right of the first window
# case 1: L-window comes before M-windows
# Once L-window reaches it's global maximum, it will stop sliding but M window can keep going on

# case 2: M-window comes before L-windows
# Once M-window reaches it's global maximum, it will stop sliding but L window can keep going on


# 1031. Maximum Sum of Two Non-Overlapping Subarrays
# https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/description/
