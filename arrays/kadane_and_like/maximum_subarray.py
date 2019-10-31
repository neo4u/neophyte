from typing import List


# Approach 1: DP
class Solution1:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-float('inf')] * n
        max_sum = dp[0] = nums[0]

        for i in range(1, n):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            max_sum = max(max_sum, dp[i])

        return max_sum


# Approach 2: Kadane
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        max_sum, cur_sum = nums[0], nums[0]

        for i in range(1, n):
            cur_sum = max(nums[i], cur_sum + nums[i])
            max_sum = max(max_sum, cur_sum)

        return max_sum


# 53. Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/

# Approach 1: DP
# Time: O(n)
# Space: O(n)

# Approach 2: Kadane
# Time: O(n)
# Space: O(1)
