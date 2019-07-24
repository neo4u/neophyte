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
# https://leetcode.com/problems/longest-continuous-increasing-subsequence/description/