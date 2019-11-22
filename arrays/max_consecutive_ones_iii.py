   def longestOnes(self, A, K):
        i = 0
        for j in xrange(len(A)):
            K -= 1 - A[j]
            if K < 0:
                K += 1 - A[i]
                i += 1
        return j - i + 1



class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_len = 0
        l, r = 0, 0
        n = len(nums)

        while r < n:
            if nums[r] == 0:
                l = r + 1
            else:
                max_len = max(max_len, r - l + 1)
            r += 1
        return max_len



# [1,1,0,1,1,1]
#        l
#             r

# 1004. Max Consecutive Ones III
# https://leetcode.com/problems/max-consecutive-ones-iii/discuss/