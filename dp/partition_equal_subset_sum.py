from typing import List


# Approach 1: DP 2D
class Solution1:
    def canPartition(self, nums: List[int]) -> bool:
        tsum, n = sum(nums), len(nums)
        if tsum % 2 == 1: return False
        t = int(tsum / 2)

        dp = [[False for _ in range(t + 1)] for _ in range(n + 1)]
        for i in range(n + 1): dp[i][0] = True

        for i in range(1, n + 1):
            for j in range(1, t + 1):
                dp[i][j] = dp[i - 1][j]
                if nums[i - 1] > j: continue
                dp[i][j] = dp[i][j] or dp[i - 1][j - nums[i - 1]]

        return dp[n][t]


# Approach 2: DP 1D
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if not nums: return True
        tsum, n = sum(nums), len(nums)
        if tsum % 2 == 1: return False
        target = tsum // 2

        dp = [True] + [False] * target
        for num in nums:
            for i in range(target, -1, -1):
                if i < num: continue
                dp[i] = dp[i] or dp[i - num]

        return dp[target]


# Small optimization, we don't have to go all the way till 0,
# we only need to go down from target down to num
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if not nums: return True
        tsum, n = sum(nums), len(nums)
        if tsum % 2 == 1: return False
        target = tsum // 2
        dp = [True] + [False] * target

        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]

        return dp[target]


# FASTEST????
# Ad hoc solution
class Solution3:
    def canPartition(self, nums: List[int]) -> bool:
        tot, n = sum(nums), len(nums)
        if tot % 2 == 1: return False
        target = tot // 2
        nums.sort(reverse=True)

        for i in range(n):
            tmp = 0
            for j in range(i, n):
                if tmp + nums[j] == target: return True
                elif tmp + nums[j] < target: tmp += nums[j]

        return False


# 416. Partition Equal Subset Sum
# https://leetcode.com/problems/partition-equal-subset-sum/description/


# Intution:
# This is similar to coin change but here we can only select an element from list, just once.

# Approach 1: DP 2D
# Model:
# dp[i][j] means whether the sum j can be formed from the first i numbers.
#          If we can pick such a series of numbers from 0-i whose sum is j,
#          dp[i][j] is true, otherwise it is false

# base case:
# dp[i][0] = True for all i from [0, n + 1]: We can always get a sum of 0 if we don't take any number

# Transition function:
# dp[i][j] = dp[i - 1][j]            If we don't pick it
# dp[i][j] = dp[i - 1][j - nums[i]]  If we pick nums[i]

# Exaplanation:
# For each number, dp[i][j] = dp[i-1][j] if we don't pick it
# which means if the first i - 1 elements has made it to j,
# dp[i][j] would also make it to j (we can just ignore nums[i]).

# If we pick nums[i]. dp[i][j] = dp[i-1][j-nums[i]],
# which represents that j is composed of the current value nums[i]
# and the remaining composed of other previous numbers.
# Thus, the transition function is dp[i][j] = dp[i-1][j] || dp[i-1][j-nums[i]]

# Time: O(len * sum)
# Space: O(len * sum)


# Approach 2: DP 1D
# Similar approach to with some differences:
# 1. 1/0 Knapsack
# 2. Coin Change
# 3. Perfect Squares

# dp[i] represents the bool for if you can form sum 'i' with the elements from nums[0...i]
# dp[i] = dp[i] or dp[i - num] for each num in nums
# dp[0] = True

# Time: O(len * sum)
# Space: O(sum)

# Why do we move in reverse in approach 2 or 1D approach:
# The reason is that we have to get dp[i] from its previous loop dp[i-1]

# dp[i][j] = dp[i-1][j] || dp[i-1][j-nums[i-1]]
# As for this bit of code:
# for num in nums:
#     for i in range(target, num - 1, -1):
#         dp[i] = dp[i] or dp[i - num]

# Every loop of nums refreshes dp array. We might get dp[i] from dp[i-num] whose index is smaller than i.
# If we increase the index of sum from 0 to sum, we will get dp[i] from dp[i-num],
# while dp[i-num] has been updated in this loop.
# This dp[i-num] is not the number we got from the previous loop.

# So why would we do this? This is because the numbers in nums can only be used once.
# If we can choose each number several times, we have to increase i from 0 to sum.
# Which means, if we are going to choose dp[i], we have to consider the situation where dp[i] has been chosen before.
# In this case, dp[i] is updated from dp[i-num] which is in the same loop with dp[i].
# This dp[i-num] we use is a kind of result where dp[i] has been chosen.


# Example: nums = [1,2,5], t = 4
# num = 1
# j = 4, [T,F,F,F,F]
# j = 3, [T,F,F,F,F]
# j = 2, [T,F,F,F,F]
# j = 1, [T,T,F,F,F]

# num = 2
# j = 4, [T,T,F,F,F]
# j = 3, [T,T,F,T,F]
# j = 2, [T,T,T,T,F]
# j = 1

sol1 = Solution1()
assert sol1.canPartition([1,5,11,5]) == True
assert sol1.canPartition([71,70,66,54,32,63,38,98,4,22,61,40,6,8,6,21,71,36,30,34,44,60,89,53,60,56,73,14,63,37,15,58,51,88,88,32,80,32,10,89,67,29,68,65,34,15,88,8,57,78,37,63,73,65,47,39,32,74,31,44,43,4,10,8,96,22,58,87,29,99,79,13,96,21,62,71,34,55,72,3,96,7,36,64,30,6,14,87,12,90,40,13,29,21,94,33,99,86,4,100]) == True
assert sol1.canPartition([40,96,95,7,65,34,39,12,86,36,35,69,9,62,64,85,53,43,87,5,44,94,94,87,85,28,3,75,62,84,76,85,56,30,88,95,22,11,46,63,35,18,23,10,45,86,11,98,5,1,76,48,76,23,57,21,10,70,78,65,1,21,53,43,88,49,14,60,21,87,46,63,7,57,93,88,57,72,12,69,56,68,95,46,100,30,7,13,87,65,41,60,3,38,16,96,94,3,3]) == True


sol = Solution()
assert sol.canPartition([1,5,11,5]) == True
assert sol.canPartition([71,70,66,54,32,63,38,98,4,22,61,40,6,8,6,21,71,36,30,34,44,60,89,53,60,56,73,14,63,37,15,58,51,88,88,32,80,32,10,89,67,29,68,65,34,15,88,8,57,78,37,63,73,65,47,39,32,74,31,44,43,4,10,8,96,22,58,87,29,99,79,13,96,21,62,71,34,55,72,3,96,7,36,64,30,6,14,87,12,90,40,13,29,21,94,33,99,86,4,100]) == True
assert sol.canPartition([40,96,95,7,65,34,39,12,86,36,35,69,9,62,64,85,53,43,87,5,44,94,94,87,85,28,3,75,62,84,76,85,56,30,88,95,22,11,46,63,35,18,23,10,45,86,11,98,5,1,76,48,76,23,57,21,10,70,78,65,1,21,53,43,88,49,14,60,21,87,46,63,7,57,93,88,57,72,12,69,56,68,95,46,100,30,7,13,87,65,41,60,3,38,16,96,94,3,3]) == True
