# @param {Integer[]} nums
# @return {Integer}
def first_missing_positive(nums)
    n = nums.size
    0.upto(n - 1) do |i|
        puts nums.inspect
        if nums[i] > 0 && nums[i] - 1 < n
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1] unless nums[nums[i] - 1] == nums[i]
        end
        puts nums.inspect
    end

    puts nums.inspect
    0.upto(n - 1) do |i|
        return i + 1 if nums[i] != i + 1
    end

    n + 1
end

# 41. First Missing Positive
# https://leetcode.com/problems/first-missing-positive/description/
# Algorithm
# 1st pass put positive, numbers less then or = n into their respective indexes unless they're already in there

require 'test/unit'
extend Test::Unit::Assertions

# assert_equal(first_missing_positive([1,2,0]), 3)
assert_equal(first_missing_positive([3,4,-1,1]), 2)
# assert_equal(first_missing_positive([7,8,9,11,12]), 1)
# assert_equal(first_missing_positive([1,2,2,1,3,1,0,4,0]), 5)
