from typing import List


# Approach 1: Simple Sorting
import bisect
class Solution1:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        medians, window, n = [], [], len(nums)

        for i in range(n):
            in_n = nums[i]
            # Find position where outgoing element should be removed from
            if i >= k:
                out_n = nums[i - k]
                # window.remove(nums[i-k])        # this works too
                window.pop(bisect.bisect(window, out_n) - 1)

            # Maintain the sorted invariant while inserting incoming element
            bisect.insort(window, in_n)

            # Find the medians
            if i >= k - 1:
                medians.append(
                    float((window[k // 2] if k & 1 else (window[k // 2 - 1] + window[k // 2]) * 0.5))
                )

        return medians


# Approach 2: Two Heaps
import heapq
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        max_heap, min_heap = [], []
        for i, x in enumerate(nums[:k]):
            heapq.heappush(max_heap, (-x, i))

        for _ in range(k - (k // 2)):   # Min-heap ends up with equal or 1 more
            self.move(max_heap, min_heap)

        result = [self.get_med(max_heap, min_heap, k)]

        for i, x in enumerate(nums[k:]):
            out_n, in_n = nums[i], x
            if in_n >= min_heap[0][0]:
                heapq.heappush(min_heap, (in_n, i + k))
                if out_n <= min_heap[0][0]: self.move(min_heap, max_heap) # Invalid element out_n is in max_heap so move one element to max_heap to balance no. of valid elements 
            else:
                heapq.heappush(max_heap, (-in_n, i + k))
                if out_n >= min_heap[0][0]: self.move(max_heap, min_heap) # Invalid element out_n is in min_heap so move one element to min_heap to balance no. of valid elements 

            while max_heap and max_heap[0][1] <= i: heapq.heappop(max_heap)
            while min_heap and min_heap[0][1] <= i: heapq.heappop(min_heap)

            result.append(self.get_med(max_heap, min_heap, k))

        return result

    def move(self, h1, h2):
        x, i = heapq.heappop(h1)
        heapq.heappush(h2, (-x, i))

    def get_med(self, h1, h2, k):
        return h2[0][0] * 1.0 if k % 2 == 1 else (-h1[0][0] + h2[0][0]) / 2.0


# 480. Sliding Window Median
# https://leetcode.com/problems/sliding-window-median/description/
