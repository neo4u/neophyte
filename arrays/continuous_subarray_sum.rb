# Approach 2: Brute-force with cumulative sum, Time: O(n^2), Space: O(n)
# @param {Integer[]} nums
# @param {Integer} k
# @return {Boolean}
def check_subarray_sum(nums, k)
    n = nums.size
    pre_sum = Array.new(n, 0)
    pre_sum[0] = nums[0]

    1.upto(n - 1) do |i|
        pre_sum[i] =  pre_sum[i - 1] + nums[i]
    end

    0.upto(n - 1) do |l|
        (l + 1).upto(n - 1) do |r|
            sum = pre_sum[r] - pre_sum[l] + nums[l]
            return true if sum == k || k != 0 && sum % k == 0
        end
    end

    false
end

# Approach 3: Hash with cumulative sum % k as key and indices as values
# Complexity: Time: O(n) one traversal, Space: O(min(n, k)) map can have min(n, k) pairings
# @param {Integer[]} nums
# @param {Integer} k
# @return {Boolean}
def check_subarray_sum(nums, k)
    sum, map, n = 0, { 0 => -1 }, nums.size
    
    0.upto(n - 1) do |i|
        sum += nums[i]
        sum %= k if k != 0

        if map.key?(sum)
            return true if i - map[sum] > 1
        else
            map[sum] = i
        end
    end
    
    false
end

# 523. Continuous Subarray Sum
# https://leetcode.com/problems/continuous-subarray-sum/

# Approach 1: Brute-force, Time: O(n^3), Space: O(1)
# Approach 2: Brute-force with cumulative sum array, Time: O(n^2), Space: O(n)
# Approach 3: Hash-map with cumulative sum % k (k != 0), Time: O(n), Space: O(min(n, k))

# Algorithm
# 1. Maintain a hash map with cumulative sum % k as keys and current index as value
# 2. Iterate through hash and keep adding current num to sum and sum %= k
# 3. If sum is found in map it means we already had a previous sum that is a multiple of k
# 4. Thus if the difference is indices is > 1, then we found such a sub-array who sum is a multiple of k
#    hence, return true.

# Best
# Time: O(n). Only one traversal of the array nums is done.
# Space: O(min(n,k)). The HashMap can contain upto min(n,k) different pairings.