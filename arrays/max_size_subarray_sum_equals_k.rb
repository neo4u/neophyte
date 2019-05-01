# Approach 3: PrefixSum + Dictionary, Time: O(N), Space: O(N)
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def max_sub_array_len(nums, k)
    pre_sum, max = 0, 0
    map = {}
    0.upto(nums.size - 1) do |i|
        pre_sum += nums[i]
        if pre_sum == k
            max = i + 1     # Window is everything from 0 to i (len i + 1)
        elsif map.key?(pre_sum - k)
            max = [i - map[sum - k], max].max
        end
        map[sum] = i if !map.key?(sum)
    end

    max
end

# 325. Maximum Size Subarray Sum Equals k
# https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/description/


# Approach 1: PrefixSum + Dictionary, Time: O(N), Space: O(N)
# 1. Let's map[V], be the number of previous prefix sums with value V
# 2. If our current prefix sum has value W, and W - V == K, think of sequences
#    with sum W and sequences with sum V, such that W - V == k, then we do result += map[V].
# 3. This is because at time t, A[0] + A[1] + ... + A[t-1] = W,
#    and there are count[V] indices j with j < t-1 and A[0] + A[1] + ... + A[j] = V.
#    Thus, there are count[V] subarrays A[j+1] + A[j+2] + ... + A[t-1] = K.

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
