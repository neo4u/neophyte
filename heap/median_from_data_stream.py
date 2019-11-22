from heapq import heappush, heappop
class MedianFinder:
    def __init__(self):
        self.max_heap, self.min_heap = [], [] # lower nums, higher nums

    def addNum(self, num: int) -> None:
        heappush(self.max_heap, -num)
        heappush(self.min_heap, -heappop(self.max_heap))

        m, n = len(self.max_heap), len(self.min_heap)
        if m < n: # max heap can only be larger by 1, so if n is greater we're breaking this property
            heappush(self.max_heap, -heappop(self.min_heap))

    def findMedian(self) -> float:
        m, n = len(self.max_heap), len(self.min_heap)
        if m == n: return (-self.max_heap[0] + self.min_heap[0]) / 2
        return -self.max_heap[0]


# from heapq import heappush, heappop
# class MedianFinder:
#     def __init__(self):
#         self.max_heap, self.min_heap = [], [] # lower nums, higher nums

#     def addNum(self, num: int) -> None:
#         heappush(self.min_heap, num)
#         heappush(self.max_heap, -heappop(self.min_heap))

#         m, n = len(self.max_heap), len(self.min_heap)
#         #s min heap can have len greater by 1, so if m is greater we're breaking this property
#         if m > n: heappush(self.min_heap, -heappop(self.max_heap))

#     def findMedian(self) -> float:
#         m, n = len(self.min_heap), len(self.max_heap)
#         if m == n: return (self.min_heap[0] - self.max_heap[0]) / 2
#         return self.min_heap[0]



# 295. Find Median from Data Stream
# https://leetcode.com/problems/find-median-from-data-stream/description/


# Time: addNum: O(log(n)), findMedian: O(1)
# Space: O(n)

# Steps:
# 1. Use two heaps 1 max_heap for lower half, and min_heap for the higher half of the list
# 2. When addNum() method is called:
#     - first heappush the num in max_heap
#     - Then heappop from max_heap and heappush into min_heap
#     - If at any point len(max_heap) < len(min_heap) then, pop from min_heap and insert into max_heap
#     - This ensure that max_heap is always equal or 1 element greater in size than min_heap
# 5. For findMedian:
#     - if lens are equal then return the average of tops of heaps
#     - else return top of max_heap


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
