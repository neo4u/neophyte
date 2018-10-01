# @param {Integer[]} nums
# @return {Integer}
def max_sub_array(nums)
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

# Space: O(1)
# Time: O(n)

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(max_sub_array([-2,1,-3,4,-1,2,1,-5,4]), 6)