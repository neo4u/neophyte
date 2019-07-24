class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 != 0:
            return False
        target = s // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for t in range(target, -1, -1):
                if num > t:
                    continue
                dp[t] = dp[t] or dp[t - num]

        return dp[target]

# 416. Partition Equal Subset Sum
# https://leetcode.com/problems/partition-equal-subset-sum/description/

# dp[i] = can you partiton the array such that one subset equals sum = i
# dp[i] = dp[i] or dp[i-num] for each num in nums
# dp[0] = True

# [1,2,5]
# t = 4

# num = 1
# j = 4
# [T,F,F,F,F]
# j = 3
# [T,F,F,F,F]
# j = 2
# [T,F,F,F,F]
# j = 1
# [T,T,F,F,F]


# num = 2
# j = 4
# [T,T,F,F,F]
# j = 3
# [T,T,F,T,F]
# j = 2
# [T,T,T,T,F]
# j = 1