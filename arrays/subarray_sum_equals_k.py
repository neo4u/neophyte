import collections

class Solution:
    def subarraySum(self, nums, k) :
        sum_map, pre_sum = collections.defaultdict(int), 0
        sum_map[0] = 1
        result = 0

        for n in nums:
            pre_sum += n
            result += sum_map[pre_sum - k]
            sum_map[pre_sum] += 1

        return result


# 560. Subarray Sum Equals K
# https://leetcode.com/problems/subarray-sum-equals-k/

# Approach 1: Brute Force (TLE), Time: O(N^3), Space: O(1)
# For every sub-array calculate the sub-array sum and count how many of them == k
# class Solution:
#     def subarraySum(self, nums, k):
#         res = 0
#         for i in range(len(nums)):
#             for j in range(i, len(nums)):
#                 if sum(nums[i:j+1]) == k:
#                     res += 1
#         return res

# Approach 2: PrefixSum + Dictionary, Time: O(N), Space: O(N)
# Best you can do is
# Time: O(n), The entire nums array is traversed only once.
# Space: O(n), Hashmap map can contain upto n distinct entries in the worst case.

# Approach 2 Intuition:
# - Problem here is to find the count of sub-arrays that have a sum of k
# - We can use the concept of prefix sum or cumulative sum to solve this question
#   1. Let's map[V], be the number of previous prefix sums with value V
#   2. If our current prefix sum has value W, and W - V == k, think of sequences
#      with sum W and sequences with sum V, such that W - V == k, then we do result += map[V].
#   3. This is because at time t, A[0] + A[1] + ... + A[t-1] = W,
#      and there are count[V] indices j with j < t-1 and A[0] + A[1] + ... + A[j] = V.
#      Thus, there are count[V] subarrays A[j+1] + A[j+2] + ... + A[t-1] = K.
#      Imagine as
#      A[0] + A[1] + ... + ... + ... + ... + ... + ... + A[t - 1] = W
#                               W
#      ---------------------------------------------------------
#                V                               k
#      ------------------------   ------------------------------
#      A[0] + A[1] + ... + A[j] + A[j+1] + A[j+2] + ...  + A[t-1]

# Other other important things are: contiguous and subsequence

# Steps:
# 1. Use a defaultdict sum_map to store the subarray sums and their counts
# 2. Use a pre_sum variable to store the sum of numbers we've seen so far
# 3. We've to init our array to seed our hash because we add to previous counts,
#    hence we mark that we've seen the sum 0 once. (sum_map[0] = 1)
# 4. Now we iterate through the elements in the array and get the pre_sum
# 5. pre_sum - k represents the no. of sub-arrays that have sum k, within the array [0, current index]
# 6. We add this count to result in each iteration
# 7. We then add the current cumulative sum to sum_map
