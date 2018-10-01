
# 643. Maximum Average Subarray I
# https://leetcode.com/problems/maximum-average-subarray-i/

# Sliding window: O(n)
# class Solution(object):
#     def findMaxAverage(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: float
#         """
#         summ = sum(nums[:k])
#         maximum = summ
#         for i in range(1, len(nums)-k+1):
#             summ -= nums[i-1]
#             summ += nums[i+k-1]
#             maximum = max(maximum, summ)
#         return float(maximum) / k