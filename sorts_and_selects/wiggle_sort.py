from typing import List


# Approach 1: Sort and swap every 2 elements starting from 1th index
class Solution1:
    def wiggleSort(self, nums: List[int]) -> None:
        n = len(nums)
        nums.sort()

        for i in range(1, n - 1, 2): self.swap(nums, i, i + 1)

    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]


# Approach 2: Sort and swap every 2 elements starting from 1th index
class Solution2:
    def wiggleSort(self, nums: List[int]) -> None:
        n, less = len(nums), True

        for i in range(n - 1):
            if less:
                if nums[i] > nums[i + 1]: self.swap(nums, i, i + 1)
            else:
                if nums[i] < nums[i + 1]: self.swap(nums, i, i + 1)
            less = not less

    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]


# Concise
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        n, less = len(nums), True

        for i in range(n - 1):
            if less and nums[i] > nums[i + 1] or \
                not less and nums[i] < nums[i + 1]:
                self.swap(nums, i, i + 1)

            less = not less

    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]


# a lil tricky to understand, but most concise
class Solution3:
    def wiggleSort(self, nums: List[int]) -> None:
        n = len(nums)

        for i in range(n):
            nums[i:i + 2] = sorted(nums[i:i + 2], reverse=i % 2)


# 280. Wiggle Sort
# https://leetcode.com/problems/wiggle-sort/description/

# Approach 1: Sort and swap every 2 elements starting from 1th index

# Time: O(n * log(n))
# Space: O(1)


# Approach 2: Simple 1-Pass
# Steps:
# - Iterate through nums from 0 upto n - 1
# - We use a bool 'less' which we flip alternatingly,
#   starting with true to indicate nums[i] must be < nums[i + 1]
# - if less and nums[i] > nums[i + 1], we have to swap them,
# - if not less and nums[i] < nums[i + 1], then we have to swap them


# Time: O(n)
# Space: O(1)
