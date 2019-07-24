from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int):
        self.memo = {}
        self.compute_ways(nums, 0, S)
        return self.memo[0, S]

    def compute_ways(self, nums, i, rem):
        if (i, rem) in self.memo:
            return self.memo[i, rem]

        n = len(nums)
        ways = 0
        if i == n:
            if rem == 0:
                ways = 1
        else:
            a = self.compute_ways(nums, i + 1, rem - nums[i])
            b = self.compute_ways(nums, i + 1, rem + nums[i])
            ways = a + b

        self.memo[i, rem] = ways
        return ways

# Notation:
# dp[i][j] ways for nums[0:i] to form target j

# Recurrance relation
# dp[i][j] = dp[i-1][j-nums[i]] + dp[i-1][j+nums[i]]
# ways to approach j - nums[i] with 1 less element  + no. of ways to approach j + nums[i] with 1 less element

# Final answer is ways to get to target S using nums[0:n]
# dp[n][S]

import collections
class Solution2:
    def findTargetSumWays(self, nums: List[int], S: int):
        n = len(nums)
        limit = sum(nums)
        dp = collections.defaultdict(int)
        dp[0, 0] = 1

        for i in range(1, n + 1):
            for j in range(-limit, limit + 1):
                if j - nums[i - 1] >= -limit: dp[i, j] += dp[i - 1, j - nums[i - 1]]
                if j + nums[i - 1] <= limit: dp[i, j] += dp[i - 1, j + nums[i - 1]]

        return dp[n, S]


import collections
class Solution3:
    def findTargetSumWays(self, nums, S):
        count = {0: 1}
        for x in nums:
            count2 = collections.defaultdict(int)
            for tmpSum in count:
                count2[tmpSum + x] += count[tmpSum]
                count2[tmpSum - x] += count[tmpSum]
            count = count2

        return count[S]

# dp[i] represents number of ways to get to target i
# dp[S] is the answer
class Solution4(object):
    def findTargetSumWays(self, nums, S):
        if not nums: return 0
        dp = {nums[0]: 1, -nums[0]: 1} if nums[0] != 0 else {0: 2}

        for i in range(1, len(nums)):
            print(dp)
            tmp_dp = collections.defaultdict(int)
            for d in dp:
                tmp_dp[d + nums[i]] += dp[d]
                tmp_dp[d - nums[i]] += dp[d]
            dp = tmp_dp
        return dp.get(S, 0)

# -1- 1 -1- 1
# -1+1-1
# +1-1-1
# -1-1+1

sol = Solution4()
assert sol.findTargetSumWays([1, 1, 1, 1, 1], 3) == 5
assert (
    sol.findTargetSumWays([2,107,109,113,127,131,137,3,2,3,5,7,11,13,17,19,23,29,47,53], 2)
    == 2790
)
assert sol.findTargetSumWays([2,107,109,113,127,131,137,3,2,3,5,7,11,13,17,19,23,29,47,53], 2147483647) == 0
assert sol.findTargetSumWays([2,107,109,113,127,131,137,3,2,3,5,7,11,13,17,19,23,29,47,53], 6) == 2796



# 494. Target Sum
# https://leetcode.com/problems/target-sum/description/


# i/S 0 1 2
# 0   1 0
# 1
# 2
# 3
