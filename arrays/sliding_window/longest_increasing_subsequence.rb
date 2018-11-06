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

# Approach 2: Binary Search
# @param {Integer[]} nums
# @return {Integer}
def length_of_lis(nums)
    tails, size = Array.new(nums.size), 0
    nums.each do |x|
        # Binary search on tails to find the right postion for x
        pos = bin_search(tails, x)

        # pos represents the correct position for x
        tails[pos] = x
        size = [pos + 1, size].max
    end
    size
end

def bin_search(a, x)
    l, r = 0, a.size
    while l < r
        mid = (l + r) / 2
        tails[mid] < x ? l = mid + 1 : r = mid
    end
    l
end

# Approach 3: Sliding Window, Time: O(n), Space: O(1)
# @param {Integer[]} nums
# @return {Integer}
def find_length_of_lcis(nums)
    ans = anchor = 0

    0.upto(nums.size - 1) do |i|
        anchor = i if i != 0 && nums[i - 1] >= nums[i]  # Reset window to i
        ans = [ans, i - anchor + 1].max                 # Extend window
    end

    ans
end

# Kadane method, Almost same as DP Time: O(n), Space: O(1)
# @param {Integer[]} nums
# @return {Integer}
def find_length_of_lcis(nums)
    return 0 if !nums || nums.empty?
    longest_so_far, longest_curr = 1, 1

    1.upto(nums.size - 1) do |i|
        nums[i] > nums[i - 1] ? longest_curr += 1 : longest_curr = 1 # Extend or reset
        longest_so_far = [longest_so_far, longest_curr].max
    end

    longest_so_far
end


# 300. Longest Increasing Subsequence
# https://leetcode.com/problems/longest-increasing-subsequence/

# Approach 1: DP, Time: O(n), Space: O(n)
# https://www.geeksforgeeks.org/longest-increasing-subsequence-dp-3/

# Approach 2: Binary Search, Time: O(nlog(n)), Space: O(1)
# Intuition and Algorithm
# This solution is essentialy binary search + Dynamic Programming (tails)
# tails is an array storing the smallest tail of all increasing subsequences with length i+1 in tails[i] scanned so far.
# For example, say we have nums = [4,5,6,3], then all the available increasing subsequences are:

# len = 1:  [4], [5], [6], [3] => tails[0] = 3
# len = 2:  [4, 5], [5, 6]     => tails[1] = 5
# len = 3:  [4, 5, 6]          => tails[2] = 6

# We can easily prove that tails is a increasing array.
# Therefore it is possible to do a binary search in tails array to find the one needs update.
# Each time we only do one of the two:
# (1) if x is larger than all tails, append it, increase the size by 1
# (2) if tails[i-1] < x <= tails[i], update tails[i]
# The above replace or append is enforce by the pos returned by the binary search
# Appending means length of LIS has increased by 1
# Replacing means we found a better tail for the curr LIS

# Approach 3: Sliding Window, Time: O(n), Space: O(n)
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

