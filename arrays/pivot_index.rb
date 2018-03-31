#!/usr/bin/env ruby

# @param {Integer[]} nums
# @return {Integer}
def pivot_index(nums)
  sum, left_sum = nums.reduce(:+), 0
  nums.each_with_index do |num, i|
    return i if left_sum == sum - left_sum - num
    left_sum += num
  end

  -1
end

# 724. Find Pivot Index
# https://leetcode.com/problems/find-pivot-index/description/

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(pivot_index([1, 7, 3, 6, 5, 6]), 3)
assert_equal(pivot_index([1, 2, 3]), -1)
