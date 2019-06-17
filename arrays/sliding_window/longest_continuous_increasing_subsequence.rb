# Approach 1: DP, Time: O(n), Space: O(n)
# class Solution {
#     public int findLengthOfLCIS(int[] nums) {
#         if (nums == null || nums.length == 0) return 0;
#         int n = nums.length;
#         int[] dp = new int[n];
        
#         int max = 1;
#         dp[0] = 1;
#         for (int i = 1; i < n; i++) {
#             if (nums[i] > nums[i - 1]) {
#                 dp[i] = dp[i - 1] + 1;
#             }
#             else {
#                 dp[i] = 1;
#             }
#             max = Math.max(max, dp[i]);
#         }
#         return max;
#     }
# }

# Approach 2: Sliding Window, Time: O(n), Space: O(1)
# @param {Integer[]} nums
# @return {Integer}
def find_length_of_lcis(nums)
    ans = l = 0

    0.upto(nums.size - 1) do |r|
        l = r if r != 0 && nums[r - 1] >= nums[r]  # Reset window to i
        ans = [ans, r - l + 1].max                 # Extend window
    end

    ans
end

# Approach 3: Kadane method, Almost same as DP Time: O(n), Space: O(1)
# @param {Integer[]} nums
# @return {Integer}
def find_length_of_lcis(nums)
    return 0 if !nums || nums.empty?
    max_len, curr_len = 1, 1

    1.upto(nums.size - 1) do |i|
        nums[i] > nums[i - 1] ? curr_len += 1 : curr_len = 1 # Extend or reset
        max_len = [max_len, curr_len].max
    end

    max_len
end

# 674.Longest Continuous Increasing Subsequence
# https://leetcode.com/problems/longest-continuous-increasing-subsequence/

# Approach 1: DP, Time: O(n), Space: O(n)

# Approach 2: Sliding Window, Time: O(n), Space: O(1)
# Intuition and Algorithm
# Every (continuous) increasing subsequence is disjoint,
# and the boundary of each such subsequence occurs whenever nums[i-1] >= nums[i].
# When it does, it marks the start of a new increasing subsequence at nums[i],
# and we store such i in the variable anchor.
# For example, if nums = [7, 8, 9, 1, 2, 3], then anchor starts at 0
# (nums[anchor] = 7) and gets set again to anchor = 3 (nums[anchor] = 1).
# Regardless of the value of anchor, we record a candidate answer of i - anchor + 1,
# the length of the subarray nums[anchor], nums[anchor+1], ..., nums[i];
# and our answer gets updated appropriately.

# Approach 3: Kadane, Time: O(n), Space: O(1)