# @param {Integer[]} nums
# @return {Integer[]}
def product_except_self(nums)
    n = nums.size
    output, pi, pj = Array.new(n, 1), 1, 1

    0.upto(n - 1) do |i|
        j = n - 1 - i
        output[i] *= pi
        output[j] *= pj
        pi *= nums[i]
        pj *= nums[j]
    end

    output
end



# 238. Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/description/

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(product_except_self([0, 0]), [0, 0])
assert_equal(product_except_self([0, 1]), [1, 0])
assert_equal(product_except_self([1, 0]), [0, 1])
assert_equal(product_except_self([1, 2, 3, 4]), [24, 12, 8, 6])
assert_equal(product_except_self([1, 2, 3, 4, 5, 5]), [600, 300, 200, 150, 120, 120])