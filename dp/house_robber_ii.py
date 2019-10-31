from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) <= 2: return max(nums)

        return max(self.rob_flat(nums[:-1]), self.rob_flat(nums[1:]))

    def rob_flat(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) <= 2: return max(nums)

        n = len(nums)
        dp = [-1] * n
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[n - 1]


# 213. House Robber II
# https://leetcode.com/problems/house-robber-ii/description/


sol = Solution()

assert sol.rob([]) == 0
assert sol.rob([0, 0, 0]) == 0
assert sol.rob([1, 1, 1]) == 1
assert sol.rob([1, 1]) == 1
assert sol.rob([2, 3, 2]) == 3
assert sol.rob([1, 2, 3, 1]) == 4
