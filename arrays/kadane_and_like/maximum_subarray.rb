# @param {Integer[]} nums
# @return {Integer}
def max_sub_array(nums)
    n = nums.size
    dp = [-Float::INFINITY] * n
    max = dp[0] = nums[0]

    1.upto(n - 1) do |i|
        dp[i] = [dp[i - 1] + nums[i], nums[i]].max
        max = [dp[i], max].max
    end

    max
end

# @param {Integer[]} nums
# @return {Integer}
def max_sub_array2(nums)
    return 0 if !nums
    cur_sum, max_sum, n = nums[0], nums[0], nums.size

    1.upto(n - 1) do |i|
        cur_sum = [cur_sum + nums[i], nums[i]].max # Extend the previous max or start a new sub-arr
        max_sum = [max_sum, cur_sum].max
    end

    max_sum
end


# 53. Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/

# Approach 1: DP
# Time: O(n)
# Space: O(n)

# Approach 2: Kadane
# Time: O(n)
# Space: O(1)

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(max_sub_array([-2,1,-3,4,-1,2,1,-5,4]), 6)

assert_equal(max_sub_array2([-2,1,-3,4,-1,2,1,-5,4]), 6)

# ms, cs = -2 . -2

# i = 1
# cs = 1, ms = 1

# i = 2
# cs = -2, ms = 1

# i = 3
# cs = 4, ms = 4

# i = 4
# cs = 3, ms = 4

# i = 5
# cs = 5, ms = 5

# i = 6
# cs = 6, ms = 6

# i = 7
# cs = 1, ms = 6

# i = 8
# cs = 5, ms = 6

