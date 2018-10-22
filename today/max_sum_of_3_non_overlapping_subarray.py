class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, K):
        W = [] #array of sums of windows
        sum_ = 0
        for i, x in enumerate(nums):
            sum_ += x
            if i >= K: sum_ -= nums[i-K]
            if i >= K-1: W.append(sum_)

        left = [0] * len(W)
        best = 0
        for i in range(len(W)):
            if W[i] > W[best]:
                best = i
            left[i] = best

        right = [0] * len(W)
        best = len(W) - 1
        for i in range(len(W) - 1, -1, -1):
            if W[i] >= W[best]:
                best = i
            right[i] = best

        ans = None
        for j in xrange(K, len(W) - K):
            i, k = left[j-K], right[j+K]
            if ans is None or (W[i] + W[j] + W[k] >
                    W[ans[0]] + W[ans[1]] + W[ans[2]]):
                ans = i, j, k
        return ans

# 689. Maximum Sum of 3 Non-Overlapping Subarrays
# https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/

# Complexity Analysis
# Time Complexity: O(N), where NN is the length of the array.
#                  Every loop is bounded in the number of steps by N, and does O(1) work.
# Space complexity: O(N). W, left, and right all take O(N) memory.

