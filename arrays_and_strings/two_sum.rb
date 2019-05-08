# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer[]}
def two_sum(nums, target)
    map = {}
    nums.each_with_index do |a, i|
        b = target - a
        return [map[b], i] if map.key?(b)
        map[a] = i
    end

    nil
end

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(two_sum([3, 3], 6), [0, 1])
assert_equal(two_sum([3, 3, 5], 0), nil)
assert_equal(two_sum([1, 7, 10, 1_029_445, 3, 5], 1_029_452), [1, 3])

# 1. Two Sum
# https://leetcode.com/problems/two-sum/description/

# Brute-Force
# def two_sum(nums, target)
#   0.upto(nums.size - 1) do |i|
#     (i + 1).upto(nums.size - 1) do |j|
#       return [i, j] if nums[i] + nums[j] == target
#     end
#   end
# end


# @param {Integer[]} numbers
# @param {Integer} target
# @return {Integer[]}
def two_sum(numbers, target)
    l, r = 0, numbers.size - 1

    while l < r
        sum = numbers[l] + numbers[r]
        return [l + 1, r + 1] if sum == target
        sum < target ? l += 1 : r -= 1
    end

    nil
end