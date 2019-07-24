class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum, cur_sum = nums[0], nums[0]

        for num in nums[1:]:
            cur_sum = max(num, cur_sum + num)
            max_sum = max(max_sum, cur_sum)

        return max_sum

# 53. Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/description/

# Input: [-2,1,-3,4,-1,2,1,-5,4],
