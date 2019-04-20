def smallest_range(nums)

end

# import heapq
# given m lists and and about k elements in each list

# class Solution:
#     def smallestRange(self, nums):
#         """
#         :type nums: List[List[int]]
#         :rtype: List[int] 
#         """
        
#         # Let's call each array in nums a bucket
#         # Use an indices array to trace the bucket indices
#         # [bucket 0's index, bucket 1's index, ...]
#         indices = [0 for _ in range(len(nums))]
        
#         # min heap storing: (value in each bucket, bucket id)
#         min_heap = [(num[0], bid) for (bid, num) in enumerate(nums)]
#         heapq.heapify(min_heap)
        
#         # global upper/ lower bound to be returned
#         upper = max([num[0] for num in nums])
#         lower = min_heap[0][0]
        
#         # trace the max value
#         high = upper
        
#         while True:
            
#             # move the index of smallest value's bucket forward
#             min_val, bid = heapq.heappop(min_heap)
#             indices[bid] += 1
#             ind = indices[bid] 
            
#             # cannot move the smallest value's bucket index forward anymore
#             # exit the loop
#             # Note: increase the index for other buckets cannot make the range
#             # smaller anymore because the lower bound won't change and the
#             # upper bound only increases
#             if ind == len(nums[bid]):
#                 break
            
#             # add the new element to the min heap
#             heapq.heappush(min_heap, (nums[bid][ind], bid))
            
#             # trace the maximum
#             high = max(high, nums[bid][ind])
            
#             # get the current group minimum from heap
#             low = min_heap[0][0]
            
#             # update bound if the group range is smaller
#             if high - low < upper - lower:
#                 lower, upper = low, high
        
#         return [lower, upper]
        

# 632. Smallest Range
# https://leetcode.com/problems/smallest-range/


# Key Insights
# 1.
# 2.
# 3.

# Steps:


# Time: O(m*k * log(m))
# Space: O(m)

require 'test/unit'
extend Test::Unit::Assertions


assert_equal(smallest_range([[1,2,3],[1,2,3],[1,2,3]]), [1,1])