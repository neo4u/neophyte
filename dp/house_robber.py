from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) <= 2: return max(nums)
        n = len(nums)

        dp = [-1] * n
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[n - 1]


# 198. House Robber
# https://leetcode.com/problems/house-robber/description/


sol = Solution()
assert sol.rob([]) == 0
assert sol.rob([0, 0, 0]) == 0
assert sol.rob([1, 1, 1]) == 2
assert sol.rob([1, 1]) == 1
