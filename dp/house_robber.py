from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        if n <= 2: return max(nums)

        dp = [0] * n
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[n - 1]


# 198. House Robber
# https://leetcode.com/problems/house-robber/description/


# Steps:
# Model:
# dp[i] represents max profit upto house at index i or i + 1th house

# Base Case:
# dp[0] and dp[1] are nums[0] and max(nums[0], nums[1])

# Recurrance Relation:
# dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
# this is max not robbing current house (thus keep the max from dp[i - 1])
# or robbing the current house in which case we can't use the profits from robbing previous house
# and hence add to max possible from prev to prev house (thus adding nums[i - 2] + nums[i])
# Goal:
# What we want finally is:
# dp[n - 1], max profit upto index n - 1 or the nth house


sol = Solution()
assert sol.rob([]) == 0
assert sol.rob([0, 0, 0]) == 0
assert sol.rob([1, 1, 1]) == 2
assert sol.rob([1, 1]) == 1
