from typing import List


# Approach 1: DP Recursion with memoization
class Solution1:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        self.memo = {}
        self.compute_ways(nums, 0, S)
        return self.memo[0, S]

    def compute_ways(self, nums, i, rem):
        if (i, rem) in self.memo: return self.memo[i, rem]

        n = len(nums)
        ways = 0
        if i == n:
            if rem == 0: ways = 1
        else:
            a = self.compute_ways(nums, i + 1, rem - nums[i])
            b = self.compute_ways(nums, i + 1, rem + nums[i])
            ways = a + b

        self.memo[i, rem] = ways
        return ways


# Approach 3: DP 1D
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        tsum = sum(nums)
        if (tsum + S) % 2 == 1 or abs(S) > tsum: return 0
        target = (tsum + S) // 2
        dp = [1] + [0] * target

        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] += dp[i - num]

        return dp[target]


# Intuition:
# Let's say we have nums = [1,2,3,4,5] and S = 3.
# There is a solution 1 - 2 + 3 - 4 + 5 = 3. After moving nums in negative to the right side,
# it becomes 1+3+5=3+2+4. Each side is half of sum(nums)+S.
# To make it more generic, Let's say you're trying to form S with numbers A B C D
# We need to have A +/- B +/- C +/- D = S
# That is we should be able to partition the array into equal sums such that
# A + B = S + C + D => A + B - C - D = S

# This means we can turn this into a knapsack problem with sack = nums and target = (sum(nums) + S) / 2.
# In this example sacks = [1,2,3,4,5] and target = 9,
# [1, 3, 5] is one of the solutions.


sol = Solution()
assert sol.findTargetSumWays([1, 1, 1, 1, 1], 3) == 5
assert sol.findTargetSumWays([2, 107, 109, 113, 127, 131, 137, 3, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 47, 53], 2) == 2790
assert sol.findTargetSumWays([2, 107, 109, 113, 127, 131, 137, 3, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 47, 53], 2147483647) == 0
assert sol.findTargetSumWays([2, 107, 109, 113, 127, 131, 137, 3, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 47, 53], 6) == 2796


# 494. Target Sum
# https://leetcode.com/problems/target-sum/description/


# Approach 1: DP Recursion with memoization

# Approach 2: DP 2D

# Model:
# dp[i][j] ways for nums[0:i] to form target j

# Recurrance relation
# dp[i][j] = dp[i-1][j-nums[i]] + dp[i-1][j+nums[i]]
# ways to approach j - nums[i] with 1 less element  + no. of ways to approach j + nums[i] with 1 less element

# Final answer is ways to get to target S using nums[0:n]
# dp[n][S]

# Example:
# i/S 0 1 2
# 0   1 0
# 1
# 2
# 3


# Approach 3: DP 1D
# dp[i] represents number of ways to get to target i
# dp[S] is the required number of ways
# Base case:
# dp[0] = 1, One way to form the zero sum
