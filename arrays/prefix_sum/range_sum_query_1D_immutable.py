from typing import List


# Approach 1: Prefix Sum, Additional Memory
class NumArray:
    def __init__(self, nums: List[int]):
        n = len(nums)
        self.pre_sum = [0] * (n + 1)
        for i, num in enumerate(self.nums):
            self.pre_sum[i + 1] = self.pre_sum[i] + num

    def sumRange(self, i: int, j: int) -> int:
        return self.pre_sum[j + 1] - self.pre_sum[i]


class NumArray:
    def __init__(self, nums: List[int]):
        n = len(nums)
        self.pre_sum = [0] * (n + 1)
        for i in range(1, n):
            self.pre_sum[i] = self.pre_sum[i - 1] + nums[i - 1]

    def sumRange(self, i: int, j: int) -> int:
        return self.pre_sum[j + 1] - self.pre_sum[i]


# Approach 2: Prefix Sum, Using nums itself
class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        for i, n in enumerate(1, self.nums):
            self.nums[i] += self.nums[i - 1]

    def sumRange(self, i: int, j: int) -> int:
        if i == 0: return self.nums[j]
        return self.nums[j] - self.nums[i - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)


# 303. Range Sum Query - Immutable
# https://leetcode.com/problems/range-sum-query-immutable/description/

# Approach 1: Cumulative Sum
# Steps:
# 1. Make prefix sum / cumulative sum array
#    Where sum[i] represents sum of nums sub-array of length i (nums[0 to i - 1])
#    Base case:             sum[0] = 0
#    Recurrance relation:   sum[i] = sum[i - 1] + nums[i - 1]
#    for i from 1 to n (get the sum from previous element + current element)
# 2. When sum_range(i, j) is called we subtract the cumulative sum
#    of the first idx from the idx outside the window
#    Example:[1,2,3,4, 5]
#    cum_sum:[0,1,3,6,10,15]
#    sum_range(1, 3): we need the sum 2+3+4 = 9
#    cum_sum[4] - cum[1] = 10 - 1 = 9
