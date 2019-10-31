from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        sum_map, pre_sum = {0: -1}, 0

        for r, num in enumerate(nums):
            pre_sum += num
            if k != 0: pre_sum %= k

            if pre_sum in sum_map:
                l = sum_map[pre_sum]
                if r - l >= 2: return True
            else:
                sum_map[pre_sum] = r

        return False


# 523. Continuous Subarray Sum
# https://leetcode.com/problems/continuous-subarray-sum/description/

Steps:
1. Using a 