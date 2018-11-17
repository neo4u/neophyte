# @param {Integer[]} nums
# @param {Integer} k
# @return {Boolean}
def contains_nearby_duplicate(nums, k)
    map = {}
    nums.each_with_index do |num, i|
        return true if map.key?(num) && (i - map[num]).abs <= k
        map[num] = i
    end

    false
end

# 219. Contains Duplicate II
# https://leetcode.com/problems/contains-duplicate-ii

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(contains_nearby_duplicate([1,2,3,1], 3), true)
assert_equal(contains_nearby_duplicate([1,0,1,1], 1), true)
assert_equal(contains_nearby_duplicate([1,2,3,1,2,3], 2), false)
