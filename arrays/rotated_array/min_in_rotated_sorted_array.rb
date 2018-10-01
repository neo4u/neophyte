# @param {Integer[]} nums
# @return {Integer}
def find_min(nums)
  l, r = 0, nums.size - 1
  
  while l < r
    return nums[l] if nums[l] < nums[r]
    mid = (l + r) / 2
    nums[mid] >= nums[l] ? l = mid + 1 : r = mid
  end

  nums[l]
end

# 153. Find Minimum in Rotated Sorted Array
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(find_min([3, 1 ,2]), 1)


