from typing import List


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


class SolutionTEST:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums: return []
        l, r, seq, n = 0, 1, [], len(nums)

        while r < n:
            curr, prev = nums[r], nums[r - 1]

            if curr <= prev:
                l = r
            else:
                if r - l + 1 > len(seq):
                    seq = nums[l:r + 1]
            r += 1

        return seq


# https://leetcode.com/problems/longest-continuous-increasing-subsequence/description/


sol = SolutionTEST()
sol.findLengthOfLCIS([-1, 0, 10, 1, 4, 5, 10]) == [-1, 0, 10]
sol.findLengthOfLCIS([-1, 0, 1, 0, 1, 4, 5, 10]) == [1, 4, 5, 10]
