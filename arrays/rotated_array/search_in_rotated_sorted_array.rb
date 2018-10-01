# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer}
def search(nums, target)
  l, r = 0, nums.size - 1

  while l <= r
		mid = (l + r) / 2
		return mid if nums[mid] == target
	
		if nums[l] <= nums[mid]
			target.between?(nums[l], nums[mid]) ? r = mid - 1 : l = mid + 1
		else
			target.between?(nums[mid], nums[r]) ? l = mid + 1 : r = mid - 1
		end
  end

	-1
end

# 33. Search in Rotated Sorted Array
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(search([4,5,6,7,0,1,2], 0), 4)
assert_equal(search([1], 1), 0)

