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


require 'test/unit'
extend Test::Unit::Assertions

assert_equal(product_except_self([0, 0]), [0, 0])
assert_equal(product_except_self([0, 1]), [1, 0])
assert_equal(product_except_self([1, 0]), [0, 1])
assert_equal(product_except_self([1, 2, 3, 4]), [24, 12, 8, 6])
assert_equal(product_except_self([1, 2, 3, 4, 5, 5]), [600, 300, 200, 150, 120, 120])