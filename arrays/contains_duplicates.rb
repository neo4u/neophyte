# @param {Integer[]} nums
# @return {Boolean}
def contains_duplicate(nums)
	1.upto(nums.size - 1) do |i|
		return true if nums[i] == nums[i - 1]
	end

	false
end

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(contains_duplicate([1,2,3,4,6,6]), true)