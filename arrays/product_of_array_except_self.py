from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pi, pj, n = 1, 1, len(nums)
        result = [1] * n

        for i in range(n):
            j = n - 1 - i
            result[i] *= pi
            result[j] *= pj

            pi *= nums[i]
            pj *= nums[j]

        return result


# 238. Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/description/


# [1, 2, 3, 4, 5, 5]
#  i              j

# pi = 1, pj = 1
# [1, 1, 1, 1, 1, 1]
# pi = 1, pj = 5

# [1, 1, 1, 1, 5, 1]
# pi = 2, pj = 25

# [1, 1, 2, 25, 5, 1]
# pi = 6, pj = 100

# [1, 1, 200, 150, 5, 1]
# pi = 24, pj = 300

# [1, 300, 200, 150, 120, 1]
# pi = 120, pj = 600

# [600, 300, 200, 150, 120, 120]
# pi = 120, pj = 600

sol = Solution()

assert sol.productExceptSelf([0, 0]) == [0, 0]
assert sol.productExceptSelf([0, 1]) == [1, 0]
assert sol.productExceptSelf([1, 0]) == [0, 1]
assert sol.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
assert sol.productExceptSelf([1, 2, 3, 4, 5, 5]) == [600, 300, 200, 150, 120, 120]
