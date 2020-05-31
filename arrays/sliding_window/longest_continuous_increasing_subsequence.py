from typing import List


# Approach 1: DP, Time: O(n), Space: O(n)
class Solution:
    def findLengthOfLCIS(self, nums):
        if not nums: return 0
        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            if nums[i - 1] >= nums[i]: continue
            dp[i] = dp[i - 1] + 1

        return max(dp)


# Approach 2: Sliding Window, Time: O(n), Space: O(1)
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums: return 0

        l, r, max_len, n = 0, 1, 1, len(nums)
        if n < 2: return 1

        while r < n:
            curr, prev = nums[r], nums[r - 1]
            if curr <= prev:
                l = r
            else:
                max_len = max(max_len, r - l + 1)
            r += 1

        return max_len






# 674. Longest Continuous Increasing Subsequence
# https://lejetcode.com/problems/longest-continuous-increasing-subsequence/description/


# 674.Longest Continuous Increasing Subsequence
# https://leetcode.com/problems/longest-continuous-increasing-subsequence/

# Approach 1: DP, Time: O(n), Space: O(n)

# Approach 2: Sliding Window, Time: O(n), Space: O(1)
# Intuition:
# 
# For example, if nums = [7, 8, 9, 1, 2, 3], then anchor starts at 0


# Approach 3: Kadane, Time: O(n), Space: O(1)
