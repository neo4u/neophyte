def length_of_lis(nums)
    return 0 if !nums || nums.empty?
    n = nums.size
    dp = Array.new(n, 1)
    max_size_global = dp[0] = 1

    1.upto(n - 1) do |i|                    # For every size of sequence (2 to n represented by 1 to n - 1 for indexing dp)
        max_size_local = 0                  # Local maximum for sequence of length i
        0.upto(i - 1) do |j|                # 0th element upto i - 1 th element
            next if nums[j] >= nums[i]      # We only care about strictly increasing so nums[j] < nums[i]
            max_size_local = [dp[j], max_size_local].max
        end
        dp[i] = max_size_local + 1
        max_size_global = [max_size_global, dp[i]].max
    end

    max_size_global
end

# Popular python solution: This is slower than above solution
# class Solution(object):
#     #using dP
#     def lengthOfLIS1(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         if not nums:
#             return 0
#         dp = [1]*len(nums)

#         for i in range (1, len(nums)):
#             for j in range(i):
#                 if nums[i] >nums[j]:
#                     dp[i] = max(dp[i], dp[j]+1)
#         return max(dp)

# 300. Longest Increasing Subsequence
# https://leetcode.com/problems/longest-increasing-subsequence/

# Leetcode solution (code in ruby above)
# Approach #3 Dynamic Programming [Accepted]

# Algorithm Description
# This method relies on the fact that the longest increasing subsequence possible upto the ith
# index in a given array is independent of the elements coming later on in the array.
# Thus, if we know the length of the LIS upto ith index, we can figure out the
# length of the LIS possible by including the (i + 1)th element based on the elements
# with indices j such that 0 ≤ j ≤ (i+1).

# dp[i] represents the length of the LIS possible for array nums[0...i]

# In order to find out dp[i], we need to try to append the current element(nums[i])
# in every possible increasing subsequences upto the (i−1)th index (including the (i−1)th index),
# such that the new sequence formed by adding the current element is also an increasing subsequence.

# Thus, we can easily determine dp[i]dp[i] using:
# dp[i] = max(dp[j]) + 1, for all j from 0 to i - 1

# At the end, the maximum out of all the dp[i]'s to determine the final result.
# LIS_length = max(dp[i]), ∀ 0 ≤ i < n

# Complexity
# Time complexity: O(n^2), Two nested n loops
# Space complexity : O(n), dp array of size n is used.