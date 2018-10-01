# 209. Minimum Size Subarray Sum
# https://leetcode.com/problems/minimum-size-subarray-sum/

# class Solution:
#     def minSubArrayLen(self, s, nums):
#         """
#         :type s: int
#         :type nums: List[int]
#         :rtype: int
#         """
#         i = j = curSum = 0
#         mini = math.inf
        
#         while j < len(nums):
#             if curSum + nums[j] < s:
#                 curSum = curSum + nums[j]
#                 j += 1
#             else:
#                 mini = min(j-i+1, mini)
#                 curSum = curSum - nums[i]                   
#                 i += 1
                                          
#         return mini if mini != math.inf else 0