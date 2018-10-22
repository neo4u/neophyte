# @param {Integer[]} nums
# @return {Integer}
# @param {Integer[]} nums
# @return {Integer}
def remove_duplicates(nums)
  return 0 if nums.length.zero?
  i, j = 0, 0

  nums[i += 1] = nums[j] if nums[j] != nums[i] while (j += 1) < nums.length

  i + 1
end

# Keep incrementing j each iteration while increment i only when we can distinct elemen

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(remove_duplicates([1,1,2]), 2)
