from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:                            # O(n)
            heapq.heappush(heap, num)               # O(log(n))
            if len(heap) > k: heapq.heappop(heap)   # O(log(n))

        return heap[0]


# 215. Kth Largest Element in an Array
# https://leetcode.com/problems/kth-largest-element-in-an-array/
