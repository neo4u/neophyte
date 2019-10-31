# @param {Integer[]} nums
# @return {Integer}
def max_product(nums)
    max, min, result = nums[0], nums[0], nums[0]

    1.upto(nums.length - 1) do |i|
        tmp = max
        max = [nums[i], max * nums[i], min * nums[i]].max
        min = [nums[i], tmp * nums[i], min * nums[i]].min
        result = [max, result].max
    end

    result
end

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_p, min_p, result = nums[0], nums[0], nums[0]

        for i in range(1, len(nums)):
            curr_max = max_p
            max_p = max(nums[i], max_p * nums[i], min_p * nums[i])
            min_p = min(nums[i], tmp * nums[i], min_p * nums[i])
            result = 

# 152. Maximum Product Subarray
# https://leetcode.com/problems/maximum-product-subarray/description/

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(max_product([2,3,-2,4]), 6)
assert_equal(max_product([-2]), -2)
