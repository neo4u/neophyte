from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_p, min_p, result, n = nums[0], nums[0], nums[0], len(nums)

        for i in range(1, n):
            curr_max = max_p
            max_p = max(nums[i], max_p * nums[i], min_p * nums[i])
            min_p = min(nums[i], curr_max * nums[i], min_p * nums[i])
            result = max(result, max_p)

        return result


# 152. Maximum Product Subarray
# https://leetcode.com/problems/maximum-product-subarray/description/


# Example: nums = [2, 3, -2, 4]
# max_p, min_p, result = 2, 2, 2
# i = 1
# curr_p = 2
# max_p = max(3, 2 * 3, 2 * 3) = 6
# min_p = min(3, 2 * 3, 2 * 3) = 6
# result = max(6, 2) = 6

# i = 2
# curr_p = 6
# max_p = max(-2, 6 * -2, 6 * -2) = -2
# min_p = min(-2, 6 * -2, 6 * -2) = -12
# result = max(-2, 6) = 6

# i = 3
# curr_p = -2
# max_p = max(4, -2 * 4, -2 * 4) = 4
# min_p = min(4, -2 * 4, -12 * 4) = -8
# result = max(4, 6) = 6
# We return 6

sol = Solution()

assert sol.maxProduct([2, 3, -2, 4]) == 6
assert sol.maxProduct([-2]) == -2
