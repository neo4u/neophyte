# @param {Integer[]} nums
# @return {Integer}
def first_missing_positive(nums)
  missing = (1..nums.count + 1).to_a - nums
  missing[0]
end

# 41. First Missing Positive
# https://leetcode.com/problems/first-missing-positive/description/
# Algorithm
# 1. Iterate from 1 to 1 more than the size of the array
# 2. Find all the missing positive numbers
# 3. return the first

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(first_missing_positive([1,2,0]), 3)
assert_equal(first_missing_positive([3,4,-1,1]), 2)
assert_equal(first_missing_positive([7,8,9,11,12]), 1)
