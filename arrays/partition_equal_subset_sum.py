class Solution(object):
    def canPartition(self, nums):
        # Edge case — return False if we can't divide sum by 2 without remainders
        if sum(nums) % 2 != 0:
            return False

        # These are our dimenions: the target sum number and the number of elements in the array
        target = sum(nums) / 2
        n = len(nums)

        # Initialize the dp table with n+1 for each dimension to handle the "zero" case
        dp = [[False] * (target + 1) for i in [0] * (n + 1)]

        # Initialize first column to all true because any set of numbers has the option to sum zero by not including that number
        for i in range(0, n + 1):
            dp[i][0] = True

        # Enumerate through dp table
        for i in range(0, n + 1):
            for j in range(0, target + 1):
                # Default case — set value to same as row before
                dp[i][j] = dp[i - 1][j]

                # We can try to see if we can combine numbers to sum 
                if j >= nums[i-1]:
                    dp[i][j] = dp[i][j] or dp[i - 1][j - nums[i - 1]]

        # Return final value
        return dp[-1][-1]

# Simplified:
class Solution(object):
    def canPartition(self, nums):
        if sum(nums) % 2 != 0:
            return False

        target = sum(nums)/2

        dp = [False] * (target + 1)
        dp[0] = True

        for i in nums:
            for j in range(target, -1, -1):
                if j >= i:
                    dp[j] = dp[j] or dp[j - i]

        return dp[-1]


# 416. Partition Equal Subset Sum
# https://leetcode.com/problems/partition-equal-subset-sum/

# 0/1 knapsack detailed explanation

# This problem is essentially to find whether there are several numbers
# in a set which are able to sum to a specific value (in this problem, the value is sum/2).

# Actually, this is a 0/1 knapsack problem, for each number, we can pick it or not.

# Let dp[i][j] means whether the specific sum j can be gotten
# from the first i numbers. If we can pick such a series of numbers from
# 0-i whose sum is j, dp[i][j] is true, otherwise it is false.
# Base case: dp[0][0] is true; (zero number consists of sum 0 is true)
# Transition function: For each number, if we don't pick it, dp[i][j] = dp[i-1][j],
# which means if the first i-1 elements has made it to j, dp[i][j] would also
# make it to j (we can just ignore nums[i]). If we pick nums[i].
# dp[i][j] = dp[i-1][j-nums[i]], which represents that j is composed of the current value nums[i]
# and the remaining composed of other previous numbers.
# Thus, the transition function is dp[i][j] = dp[i-1][j] || dp[i-1][j-nums[i]]
