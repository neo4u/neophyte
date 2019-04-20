# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer[]}
def max_sum_of_three_subarrays(nums, k)
    best_1_seq = 0
    best_2_seq = [0, k]
    best_3_seq = [0, k, 2*k]
    
    seq_1_sum = nums[0...k].reduce(0, :+)
    seq_2_sum = nums[k...2*k].reduce(0, :+)
    seq_3_sum = nums[2*k...3*k].reduce(0, :+)
    
    best_1_sum = seq_1_sum
    best_2_sum = seq_1_sum + seq_2_sum
    best_3_sum = seq_1_sum + seq_2_sum + seq_3_sum
    
    seq_1_idx = 1           # start 1 index after 1st window
    seq_2_idx = k + 1       # start 1 index after 2nd window
    seq_3_idx = 2*k + 1     # start 1 index after 3rd window

    while seq_3_idx <= nums.size - k
        seq_1_sum = seq_1_sum - nums[seq_1_idx - 1] + nums[seq_1_idx + k - 1]
        seq_2_sum = seq_2_sum - nums[seq_2_idx - 1] + nums[seq_2_idx + k - 1]
        seq_3_sum = seq_3_sum - nums[seq_3_idx - 1] + nums[seq_3_idx + k - 1]

        best_1_seq, best_1_sum = seq_1_idx, seq_1_sum if seq_1_sum > best_1_sum
        best_2_seq, best_2_sum = [best_1_seq, seq_2_idx], seq_2_sum + best_1_sum if seq_2_sum + best_1_sum > best_2_sum
        best_3_seq, best_3_sum = best_2_seq + [seq_3_idx], seq_3_sum + best_2_sum if seq_3_sum + best_2_sum > best_3_sum

        seq_1_idx += 1; seq_2_idx += 1; seq_3_idx += 1
    end

    best_3_seq
end

# 689. Maximum Sum of 3 Non-Overlapping Subarrays
# https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/

# Steps:
# 1. Start windows with 1st k, 2nd k, and 3rd k
# 2. Keep moving each one and recording the indices of the best sum windows

# Time: O(n), one traversal of list
# Space: O(1)

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(max_sum_of_three_subarrays([1,2,1,2,6,7,5,1], 2), [0, 3, 5])
assert_equal(max_sum_of_three_subarrays([7,13,20,19,19,2,10,1,1,19], 3), [1,4,7])
assert_equal(max_sum_of_three_subarrays([4,5,10,6,11,17,4,11,1,3], 1), [4,5,7])

