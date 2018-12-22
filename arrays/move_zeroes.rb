# Approach 2
# @param {Integer[]} nums
# @return {Void} Do not return anything, modify nums in-place instead.
def move_zeroes(nums)
    idx_after_last_non_zero = 0

    0.upto(nums.size - 1) do |i|
        if nums[i] != 0
            idx_after_last_non_zero += 1
            nums[idx_after_last_non_zero] = nums[i]
        end
    end

    idx_after_last_non_zero.upto(nums.size - 1) { |j| nums[i] = 0 }
end

# Approach 3
# @param {Integer[]} nums
# @return {Void} Do not return anything, modify nums in-place instead.
def move_zeroes(nums)
    idx_after_last_non_zero = 0

    0.upto(nums.size - 1) do |i|
        next if nums[i].zero?   # If curr num == 0, its already after the non-zero idx, so go to next num
        nums[idx_after_last_non_zero], nums[i] = nums[i], nums[idx_after_last_non_zero]
        idx_after_last_non_zero += 1
    end

    nums
end

# 283. Move Zeroes
# https://leetcode.com/problems/move-zeroes/

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(move_zeroes([0,1,0,3,12]), [1,3,12,0,0])
assert_equal(move_zeroes([0,0,1]), [1,0,0])

# Approach 1, Keep an arrray and copy only non-zero elements and then once the aux array is exhausted copy over zeros: Time: O(n) Space: O(n)
# Approach 2, Two-pass solution, Keep a var for last index after a non-zero element, and in the second pass from last index to end fill zeros

# Approach 3 (Optimal) (1 pass)
# 1. Keep the index of last index after non-zero element
# 2. Each time you get a non-zero element swap with the index after last non-zero
# Time: O(n)
# Space: O(1)