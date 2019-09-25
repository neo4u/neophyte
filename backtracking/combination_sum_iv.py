from typing import List


# Approach 1: Top Down DP a.k.a Memoization
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        self.cache = {0:1}
        return self.dfs(nums, target, )

    def dfs(self, nums, target):
        if target in self.cache: return self.cache[target]

        self.cache[target] = 0
        for x in nums:
            if target - x < 0: continue
            self.cache[target] += self.dfs(nums, target - x)

        return self.cache[target]



# Approach 2: Bottom-Up DP a.k.a Tabulation
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        results = [0] * (target + 1)
        results[0] = 1
        for i in range(1, target + 1):
            for x in nums:
                if i - x < 0: continue
                results[i] += results[i - x]

        return results[target]



# Combination Sum IV 
# https://leetcode.com/problems/combination-sum-iv/

# Approach 1: Top Down DP a.k.a Memoization
# Time: O(target * nums)
# Space: O(target * nums)

# Approach 2: Bottom-Up DP a.k.a Tabulation


# Follow Up
# What if negative numbers are allowed?
# We need additional constraints in the problem else we will have an infinite loop.
# https://discuss.leetcode.com/topic/53553/what-if-negative-numbers-are-allowed-in-the-given-array


# ALL combination sum problems
# https://leetcode.com/problems/combination-sum-iv/discuss/85120/C++-template-for-ALL-Combination-Problem-Set

# https://leetcode.com/problems/combination-sum-iv/discuss/85106/A-summary-of-all-combination-sum-problem-in-LC-C++
