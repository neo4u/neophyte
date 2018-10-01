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

# 152. Maximum Product Subarray
# https://leetcode.com/problems/maximum-product-subarray/description/

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(max_product([2,3,-2,4]), 6)
assert_equal(max_product([-2]), -2)
