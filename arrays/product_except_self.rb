# @param {Integer[]} nums
# @return {Integer[]}
def product_except_self(nums)
  return false if nums.empty?
  output, pi, pj = [1] * nums.length, 1, 1
  0.upto(nums.length - 1) do |i|
    j = -i - 1
    output[i] *= pi
    output[j] *= pj
    pi *= nums[i]
    pj *= nums[j]
  end

  output
end

# @param {Integer[]} nums
# @return {Integer[]}
def product_except_self_alt(nums)
  hash = {}
  nums.each_with_index do |num, index|
    if !hash.include?(num)
      num_to_remember = num
      nums[index] = 1
      hash[num] = nums.reduce(:*)
      nums[index] = num_to_remember
    end
  end
  nums.each_with_index do |num, index|
    nums[index] = hash[num]
  end
  nums
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

assert_equal(product_except_self_alt([0, 0]), [0, 0])
assert_equal(product_except_self_alt([0, 1]), [1, 0])
assert_equal(product_except_self_alt([1, 0]), [0, 1])
assert_equal(product_except_self_alt([1, 2, 3, 4]), [24, 12, 8, 6])
assert_equal(product_except_self_alt([1, 2, 3, 4, 5, 5]), [600, 300, 200, 150, 120, 120])
