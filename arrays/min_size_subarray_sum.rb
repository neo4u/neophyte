# Approach 3: Binary Search on pre_sum array
# @param {Integer} s
# @param {Integer[]} nums
# @return {Integer}
def min_sub_array_len(s, nums)
    result, n = nums.size + 1, nums.size

    1.upto(n - 1) do |i|
        nums[i] += nums[i - 1]
    end

    l = 0
    nums.each_with_index do |num, r|
        next if num < s
        l = bisect_left(l, r, nums, s, num)
        result = [result, r - l + 1].min
    end

    result <= nums.size ? result : 0
end

def bisect_left(l, r, nums, s, num)
    while l < r
        mid = (l + r) / 2
        num - nums[mid] >= s ? l = mid + 1 : r = mid
    end

    l
end

# Approach 4: Two-pointers
# @param {Integer} s
# @param {Integer[]} nums
# @return {Integer}
def min_sub_array_len(s, nums)
    pre_sum = l = 0
    result = nums.size + 1

    nums.each_with_index do |num, r|
        pre_sum += num

        while pre_sum >= s
            result = [result, r - l + 1].min
            pre_sum -= nums[l]
            l += 1
        end
    end

    result <= nums.size ? result : 0
end

# 209. Minimum Size Subarray Sum
# https://leetcode.com/problems/minimum-size-subarray-sum/


# Approach 1: Brute-Force
# Approach 2: Brute-Force with pre_sum array

# Approach 3: Binary Search on pre_sum array

# Approach 4: Two-Pointers (Sliding window) Time: O(n), Space: O(1)
# Algo:
# 1. Keep r index fixed at each index 
# 2. Start l index off at 0 and keep moving it to the right, while:
#    sum >= s
# 3. As we keep moving l to the right we need to exclude the element
#    at last removed index


require 'test/unit'
extend Test::Unit::Assertions

assert_equal(min_sub_array_len(7, [2,3,1,2,4,3]), 2)