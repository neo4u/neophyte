# # Combination Sum IV 
# https://leetcode.com/problems/combination-sum-iv/

# Memoization

# The time complexity is O(target * nums)
# Top down Memoization solution
class Solution(object):
    def helper(self, nums, target, cache):
        if target not in cache:
            cache[target] = 0
            for x in nums:
                if target - x >= 0:
                    cache[target] += self.helper(nums, target-x, cache)
        return cache[target]

    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.helper(nums, target, {0:1})

# Dynamic Programming
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        results = [0] * (target + 1)
        results[0] = 1
        for i in range(1, target + 1):
            for x in nums:
                if i - x >= 0:
                    results[i] += results[i - x]
        return results[target]

# Follow Up
# What if negative numbers are allowed?
# We need additional constraints in the problem else we will have an infinite loop.
# https://discuss.leetcode.com/topic/53553/what-if-negative-numbers-are-allowed-in-the-given-array


# ALL combination sum problems
# https://leetcode.com/problems/combination-sum-iv/discuss/85120/C++-template-for-ALL-Combination-Problem-Set

# https://leetcode.com/problems/combination-sum-iv/discuss/85106/A-summary-of-all-combination-sum-problem-in-LC-C++