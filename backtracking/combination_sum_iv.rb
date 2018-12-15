# Approach 1: Recursion with memoization
# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer}
def combination_sum4(nums, target)
    return 0 if !nums || nums.empty?
    recurse(nums, target, {0 => 1})
end

def recurse(nums, target, cache)
    return cache[target] if cache.key?(target)
    cache[target] = 0 if !cache.key?(target)

    nums.each do |x|
        next if target - x < 0
        cache[target] += recurse(nums, target - x, cache)
    end

    cache[target]
end

# Approach 2: Bottom-up DP
# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer}
def combination_sum4(nums, target)
    dp = Array.new(target + 1, 0)
    dp[0] = 1

    1.upto(target) do |i|
        nums.each do |x|
            dp[i] += dp[i - x] if i - x >= 0
        end
    end

    dp[target]
end

# Combination Sum IV
# https://leetcode.com/problems/combination-sum-iv/

# Approach 1: Dynamic programming top-down (Recursion with memoization)
# Approach 2: DP bottom-up

# Follow Up
# What if negative numbers are allowed?
# PROBLEM: For negative numbers the combination length can be unbounded,
# as we can keep subtracting and adding 1 unlimited number of times to get the same target
# SOLUTION: Keep a bound k on the combination sequence length.

# Most similar to combination sum ii as duplicates are allowed
# Similar to word_break II in terms of recurse with memoization