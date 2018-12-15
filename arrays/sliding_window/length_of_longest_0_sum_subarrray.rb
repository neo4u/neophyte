# Approach 2: Sliding Window
# @param {Integer[]} nums
# @return {Integer}
def longest_zero_sum_subarray(nums)
    pre_sum, max_len, n, map = 0, 0, nums.size, {}

    0.upto(n - 1) do |r|
        pre_sum += nums[r]

        max_len = 1 if max_len.zero? && nums[r].zero?   # sub-array of length 1
        max_len = r + 1 if pre_sum.zero?                # pre_sum holds only sum of 0-sum sub-array, so convert index r to length by +1

        if map.key?(pre_sum)                            # Found the end of a zero-sum window, start is given by map[pre_sum]
            l = map[pre_sum]
            max_len = [max_len, r - l].max
        else                                            # Saving start of a potential 0 sum window
            map[pre_sum] = r
        end
    end

    max_len
end


# Find the length of largest subarray with 0 sum
# https://www.geeksforgeeks.org/find-the-largest-subarray-with-0-sum/

# Approach 1: Brute-Force,        Time: O(n ^ 2),   Space: O(1)
# Approach 2: Sliding Window,     Time: O(n),       Space: O(1)
# 1. Keep adding current number to a pre_fix sum, and keep a map of pre_sum to index of the pre_sum
# 2. Check if pre_sum is in map, if yes, then we hit the end of a 0-sum sub-array who start is captured by the map[pre_sum]
# 3. if no, then we store the current pre_sum and the corresponding index in the map
# 4. We keep a running max to store the max_len, which is returned at the end.

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(longest_zero_sum_subarray([15, -2, 2, -8, 1, 7, 10, 23]), 5)
assert_equal(longest_zero_sum_subarray([1, 2, 3]), 0)
assert_equal(longest_zero_sum_subarray([1, 0, 3]), 1)
assert_equal(longest_zero_sum_subarray([0, 0, 0]), 3)
assert_equal(longest_zero_sum_subarray([0, 0, 1]), 2)
assert_equal(longest_zero_sum_subarray([1, 1, 1]), 0)
assert_equal(longest_zero_sum_subarray([]), 0)



