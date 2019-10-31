import collections
from typing import List


class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        sum_map, pre_sum, max_len = collections.defaultdict(int), 0, 0
        sum_map[0] = -1

        for r, num in enumerate(nums):
            pre_sum += num

            if pre_sum - k in sum_map:
                l = sum_map[pre_sum - k]
                max_len = max(max_len, r - l)

            if pre_sum not in sum_map: sum_map[pre_sum] = r

        return max_len


# 325. Maximum Size Subarray Sum Equals k
# https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/description/


# Approach 1: PrefixSum + Dictionary, Time: O(N), Space: O(N)
# 1. Let's map[V], be the number of previous prefix sums with value V
# 2. If our current prefix sum has value W, and W - V == K, think of sequences
#    with sum W and sequences with sum V, such that W - V == k, then we do result += map[V].
# 3. This is because at time t, A[0] + A[1] + ... + A[t-1] = W,
#    and there are count[V] indices j with j < t-1 and A[0] + A[1] + ... + A[j] = V.
#    Thus, there are count[V] subarrays A[j+1] + A[j+2] + ... + A[t-1] = K.

# Simple Steps:
# 1. Similar set up as other prefix sum problems
# 2. if pre_sum - k is in sum_map, then everything between pre_sum - k and pre_sum has the sum k.
# 3. Important bit is if pre_sum not in sum_map, we add it for the curr index r.

# Imagine as
# A[0] + A[1] + ... + ... + ... + ... + ... + ... + A[t - 1] = W
#                          W
# ---------------------------------------------------------
#           V                               k
# ------------------------   ------------------------------
# A[0] + A[1] + ... + A[j] + A[j+1] + A[j+2] + ...  + A[t-1]


# Best you can do is
# Time: O(n), The entire nums array is traversed only once.
# Space: O(n), Hashmap map can contain upto n distinct entries in the worst case.
