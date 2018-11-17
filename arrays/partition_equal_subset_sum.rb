# @param {Integer[]} nums
# @return {Boolean}
def can_partition(nums)
    n = nums.size
    sum = nums.reduce(:+)
    # Edge case — return False if we can't divide sum by 2 without remainders
    return false if sum % 2 != 0
    target = sum / 2
            
    dp = Array.new(n + 1) { Array.new(target + 1, false) }
    0.upto(n) { |i| dp[i][0] = true }
    
    0.upto(n) do |i|
        0.upto(target) do |j|
            dp[i][j] = dp[i - 1][j] # Don't pick the current number
            dp[i][j] ||= dp[i - 1][j - nums[i - 1]] if j >= nums[i - 1] # Pick the current number
        end
    end

    dp[n][target]
end

# Approach 2: 1-D DP, Time: O(n^2), Space: O(n)
# @param {Integer[]} nums
# @return {Boolean}
def can_partition(nums)
    n = nums.size
    sum = nums.reduce(:+)
    # Edge case — return False if we can't divide sum by 2 without remainders
    return false if sum % 2 == 1
    target = sum / 2

    # dp[j] represents if target j can be partitioned
    dp = Array.new(target + 1, false)
    dp[0] = true
    
    1.upto(n - 1) do |i|
        target.downto(0) do |j|
            num = nums[i]
            dp[j] = dp[j] || dp[j - num] if j >= num
        end
    end
    
    dp[target]
end

# 416. Partition Equal Subset Sum
# https://leetcode.com/problems/partition-equal-subset-sum/

# 0/1 knapsack detailed explanation

# This problem is essentially to find whether there are several numbers
# in a set which are able to sum to a specific value (in this problem, the value is sum/2).

# Actually, this is a 0/1 knapsack problem, for each number, we can pick it or not.

# Let dp[i][j] represents the bool of whether we can get sum j from nums 0 to i.
# dp[i][j] = true If we can pick such a numbers from 0-i whose sum is j,
#          = false, otherwise
# Base case: dp[0][0] is true; (zero number consists of sum 0 is true)

# Transition function: For each number, if we don't pick it, dp[i][j] = dp[i - 1][j],
# which means if the first i - 1 elements has made it to j, dp[i][j] would also
# make it to j (we can just ignore nums[i]). If we pick nums[i].
# dp[i][j] = dp[i-1][j-nums[i]], which represents that j is composed of the current value nums[i]
# and the remaining composed of other previous numbers.
# Thus, the transition function is dp[i][j] = dp[i-1][j] || dp[i-1][j-nums[i]]

# Time: O(n^2)
# Space: O(n)

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(can_partition([1,5,11,5]), true)
assert_equal(can_partition([71,70,66,54,32,63,38,98,4,22,61,40,6,8,6,21,71,36,30,34,44,60,89,53,60,56,73,14,63,37,15,58,51,88,88,32,80,32,10,89,67,29,68,65,34,15,88,8,57,78,37,63,73,65,47,39,32,74,31,44,43,4,10,8,96,22,58,87,29,99,79,13,96,21,62,71,34,55,72,3,96,7,36,64,30,6,14,87,12,90,40,13,29,21,94,33,99,86,4,100]), true)