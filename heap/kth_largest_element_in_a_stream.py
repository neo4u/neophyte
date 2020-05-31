import heapq

class KthLargest:
    def __init__(self, k, nums):
        self.pool = []
        self.k = k
        for num in nums:
            self.add(num)

    def add(self, val):
        if len(self.pool) < self.k:
            heapq.heappush(self.pool, val)
        elif val > self.pool[0]:
            heapq.heappushpop(self.pool, val)
        return self.pool[0]

# 703. Kth Largest Element in a Stream
# https://leetcode.com/problems/kth-largest-element-in-a-stream/description/


# Time: add() is O(log k), KthLargest.__init__() is O(n log k)
# Space: O(k) for heap
