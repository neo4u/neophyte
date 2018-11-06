# @param {Integer[]} nums
# @return {Integer}
def pivot_index(nums)
    largest, largest_idx = -1, -1

    nums.each_with_index do |num, i|
        if num > largest
            largest = num
            largest_idx = i
        end
    end

    nums.each do |num|
        return -1 if largest < 2 * num && largest != num
    end

    largest_idx
end

# 724. Find Pivot Index
# https://leetcode.com/problems/find-pivot-index/description/

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(dominant_index([3, 6, 1, 0]), 1)
assert_equal(dominant_index([1, 2, 3, 4]), -1)
