from heapq import heappush, heappop

class MedianFinder:
    def __init__(self):
        self.min_heap, self.max_heap = [], []

    def addNum(self, num: int) -> None:
        heappush(self.min_heap, num)
        heappush(self.max_heap, -heappop(self.min_heap))

        m, n = len(self.min_heap), len(self.max_heap)
        if m < n: # min heap should be larger
            heappush(self.min_heap, -heappop(self.max_heap))

    def findMedian(self) -> float:
        m, n = len(self.min_heap), len(self.max_heap)
        if m == n: return (self.min_heap[0] - self.max_heap[0]) / 2
        return self.min_heap[0]



# 295. Find Median from Data Stream
# https://leetcode.com/problems/find-median-from-data-stream/description/

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()