# Approach 2: Brute-force with cumulative sum, Time: O(n^2), Space: O(n)
# @param {Integer[]} nums
# @param {Integer} k
# @return {Boolean}
def check_subarray_sum_brutal(nums, k)
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
            puts map
            return true if i - map[sum] >= 2
        else
            map[sum] = i
        end
    end

    puts map
    false
end


# 523. Continuous Subarray Sum
# https://leetcode.com/problems/continuous-subarray-sum/

# Approach 1: Brute-force, Time: O(n^3), Space: O(1)
# Approach 2: Brute-force with cumulative sum array, Time: O(n^2), Space: O(n)
# Approach 3: Hash-map with cumulative sum % k (k != 0), Time: O(n), Space: O(min(n, k))

# Algorithm
# 1. Maintain a hash map with cumulative sum % k as keys and current index as value
# 2. Iterate through hash and keep adding current pre_sum  %= k to the hash with value as the index of that pre_sum
# 3. If sum is found in map it means we already had a previous sum that is a multiple of k
# 4. Thus if the difference is indices is > 1, then we found such a sub-array who sum is a multiple of k
#    hence, return true.

# why do we insert key, value pair 0, -1 at the start into map
# Consider that the first element itself is the sub-array sum multiple of k
# Example:
# [2, 3, 4], k = 2
# i = 0, pre_sum = 2, pre_sum % k = 0,
# Our hash so far is: { 0 => -1 }
# 0 is found in the hash, so we check if i - map[pre_sum] >= 2
# 0 - (-1) == 1 which is not >= 2, so we have to move on

# i = 1, pre_sum = 0 + 3 == 3, pre_sum % k = 1
# we add to map => { 0 => -1, 1 => 1}, we move on

# i = 2, pre_sum = 1 + 4 == 5, pre_sum % k = 1
# we have that in our map so, we check if i - map[i] >= 2
# 2 - 1 == 1 which is not >= 2, hence we're done and return false
# And thsu we find that there is no such continuous subarray sum.

# if we didn't, have the 0 and -1 added to the map
# consider the corner cases:
# [0], 0        -> false. Map would be {0 => -1}, 0 - -1 == 1 not >= 2 causes us to return false
# [5, 2, 4], 5  -> false. Map would be {0 => -1, 2 => 1, 1 => 2}. Thus never returning true
# [0, 0], 100   -> true, Map would be {0 => -1}, but when i = 1, i - map[pre_sum%k] == 1 - -1 == 2, thus we return true
# [1,5], -6     -> true, Map would be {0 => -1, -5 => 0}, then at i = 1, we get pre_sum % k = -5 + 5 == 0 % -6 == 0, thus 1 - -1 == 2


# Best
# Time: O(n). Only one traversal of the array nums is done.
# Space: O(min(n,k)). The HashMap can contain upto min(n,k) different pairings.

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(check_subarray_sum([0,0], 0), true)
assert_equal(check_subarray_sum([2, 3, 4], 2), false)
assert_equal(check_subarray_sum([1,5], -6), true)
assert_equal(check_subarray_sum([0,0], 100), true)
assert_equal(check_subarray_sum([0], 0), false)
assert_equal(check_subarray_sum([5, 2, 4], 5), false)


