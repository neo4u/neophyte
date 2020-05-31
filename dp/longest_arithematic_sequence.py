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


# Approach 1: DP
# Intutition
# Example of an arithmetic seq is: [3,6,9,12]
# - All 4 values at indexes 0, 1, 2, 3 are such that seq[i + 1] - seq[i] == 3
# - Thus the entire sequence is an arithmetic sequence.
# - We can use DP with the respresentation:
#   dp[i] represents a dict where:
#   1. keys are diffs and
#   2. values are length of the subsequence for that diff upto index i
#   Recurrence relation is:
#   For every element at index i, and for every prev element at j, check if the a[i],
#   a[j] diff appears in dp[j], then a[j] was part of a sequence with same diff
#   i.e. dp[i][diff] = dp[j][diff] + 1, we've found another consequtive element with same diff so inc len


# Steps:
# 1. We firstly iterate every size of subarray, from 1 to n and call this i
# 2. Then we iterate through all the indexes of the subarray of size i, i.e. from 0 to i - 1, calll this j
# 3. We get the diff, between the elements at index i and j, i.e.
#    For the last element of every sequence, get the diff of the last element with every element before it
# 4. If we've seen the diff value before for that subarray size, then add 1 else just default it to 2,
#    cuz atleast 2 elements are involved in the sequence
# 5. Key step here is using the recurrence relation to update dp[i][diff] by adding to dp[j][diff]

# Example: A = [9,4,7,2,10]
# dp = [{}, {}, {}, {}, {}]
# max_len = 0

# ----
# i = 1
# j = 0, diff = -5
# dp[1][-5] = 2
# dp = [{}, {-5: 2}, {}, {}, {}], max_len = 2

# ----
# i = 2
# j = 0, diff = 7 - 9 = -2
# dp[2][-2] = 2
# dp = [{}, {-5: 2}, {-2: 2} {}, {}], max_len = 2

# j = 1, diff = 7 - 4 = 3
# dp = [{}, {-5: 2}, {-2: 2, 3: 2}, {}, {}], max_len = 2

# ----
# i = 3
# j = 0, diff = -7
# dp = [{}, {-5: 2}, {-2: 2, 3, 2}, {-7: 2}, {}], max_len = 2

# j = 1, diff = -2
# dp = [{}, {-5: 2}, {-2: 2, 3: 2}, {-7: 2, -2: 2}, {}], max_len = 2

# j = 2, diff = -5
# dp = [{}, {-5: 2}, {-2: 2, 3: 2}, {-7: 2, -2: 2, -5:2}, {}], max_len = 2

# ----
# i = 4
# j = 0, diff = 1
# dp = [{}, {-5: 2}, {-2: 2, 3: 2}, {-7: 2}, {1: 2}], max_len = 2

# j = 1, diff = 6
# dp = [{}, {-5: 2}, {-2: 2, 3, 2}, {-7: 2}, {1: 2, 6: 2}], max_len = 2

# j = 2, diff = 3
# dp = [{}, {-5: 2}, {-2: 2, 3: 2}, {-7: 2}, {1: 2, 6: 2, 3: 3}], max_len = 3

# j = 3, diff = 8
# dp = [{}, {-5: 2}, {-2: 2, 3: 2}, {-7: 2}, {1: 2, 6: 2, 3: 3, 8: 2}], max_len = 3

# ----
# return max_len = 3

# Time: O(n^2)
# Space: O(n^2), worst case, all number before has different diff for n times 
