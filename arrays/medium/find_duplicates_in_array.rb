# @param {Integer[]} nums
# @return {Integer[]}
def find_duplicates(nums)
    p nums
    puts
    res = []
    nums.each do |x|
        i = x.abs - 1
        nums[i] < 0 ? res.push(x.abs) : nums[i] = -nums[i]
    end

    res
end

# 442. Find All Duplicates in an Array
# https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

# Approach 1: Hash
# Approach 2: Two Pass


require 'test/unit'
extend Test::Unit::Assertions

assert_equal(find_duplicates([4,3,2,7,8,2,3,1]), [2,3])
