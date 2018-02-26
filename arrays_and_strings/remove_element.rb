# @param {Integer[]} nums
# @param {Integer} val
# @return {Integer}
def remove_element(nums, val)
  i, j = 0, 0
  while j < nums.length
    if nums[j] != val
      nums[i] = nums[j]
      i += 1
    end
    j += 1
  end

  i
end

# Concept is again a slow and fast pointer
# Move one pointer (i) to keep the next index of the index where val was not seen
# Move j for each iteration to check for an element that equals val
# if val in first place move j till a non
require 'test/unit'
extend Test::Unit::Assertions

assert_equal(remove_element([3,2,2,3], 3), 2)