#!/usr/bin/env ruby

# @param {Integer[]} nums1
# @param {Integer} m
# @param {Integer[]} nums2
# @param {Integer} n
# @return {Void} Do not return anything, modify nums1 in-place instead.
def merge(nums1, m, nums2, n)
  i, j = m - 1, n - 1
  (m + n - 1).downto(0) do |k|
    if i >= 0 && j >= 0
      if nums1[i] > nums2[j]
        nums1[k] = nums1[i]
        i -= 1
      else
        nums1[k] = nums2[j]
        j -= 1
      end
    elsif j >= 0
      nums1[k] = nums2[j]
      j -= 1
    end
  end

  nums1 # Comment this out for submission into leetcode. Bcuz we need in place
end

# 66. Plus One
# https://leetcode.com/problems/plus-one/description/

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(merge([2, 0], 1, [1], 1), [1, 2])
assert_equal(merge([1, 2, 3, 4, 5], 5, [8, 9, 10, 11, 12, 12, 16], 7), [1, 2, 3, 4, 5, 8, 9, 10, 11, 12, 12, 16])

