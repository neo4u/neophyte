from typing import List


class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        n = len(A)
        max_len, dp = 0, [{} for _ in range(n)]

        for i in range(1, n):
            for j in range(i):
                diff = A[i] - A[j]

                if diff in dp[j]:
                    dp[i][diff] = dp[j][diff] + 1
                else:
                    dp[i][diff] = 2

                max_len = max(max_len, dp[i][diff])

        return max_len


# 1027. Longest Arithmetic Sequence
# https://leetcode.com/problems/longest-arithmetic-sequence/description/

# Steps:
# dp[i] represents a dict where keys are diffs and
# values are length of the subsequence for that diff upto index i


# Example: A = [9,4,7,2,10]
# dp = [{}, {}, {}, {}, {}]
# max_len = 0

# i = 1, j = 0, diff = -5
# dp = [{}, {-5: 2}, {}, {}, {}], max_len = 2

# i = 2
# j = 0, diff = -2
# dp = [{}, {-5: 2}, {-2: 2} {}, {}], max_len = 2

# j = 1, diff = 3
# dp = [{}, {-5: 2}, {-2: 2, 3: 2}, {}, {}], max_len = 2


# i = 3
# j = 0, diff = -7
# dp = [{}, {-5: 2}, {-2: 2, 3, 2}, {-7: 2}, {}], max_len = 2

# j = 1, diff = -2
# dp = [{}, {-5: 2}, {-2: 2, 3: 2}, {-7: 2, -2: 2}, {}], max_len = 2

# j = 2, diff = -5
# dp = [{}, {-5: 2}, {-2: 2, 3: 2}, {-7: 2, -2: 2, -5:2}, {}], max_len = 2

# i = 4
# j = 0, diff = 1
# dp = [{}, {-5: 2}, {-2: 2, 3: 2}, {-7: 2}, {1: 2}], max_len = 2

# j = 1, diff = 6
# dp = [{}, {-5: 2}, {-2: 2, 3, 2}, {-7: 2}, {1: 2, 6: 2}], max_len = 2

# j = 2, diff = 3
# dp = [{}, {-5: 2}, {-2: 2, 3: 2}, {-7: 2}, {1: 2, 6: 2, 3: 3}], max_len = 3

# j = 3, diff = 8
# dp = [{}, {-5: 2}, {-2: 2, 3: 2}, {-7: 2}, {1: 2, 6: 2, 3: 3, 8: 2}], max_len = 3

# return max_len = 3

# Time: O(n^2)
# Space: O(n^2), worst case, all number before has different diff for n times 
