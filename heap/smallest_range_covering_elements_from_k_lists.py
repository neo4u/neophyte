import heapq
from typing import List


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        pq = [(row[0], i, 0) for i, row in enumerate(nums)]
        heapq.heapify(pq)

        result = float('-inf'), float('inf')
        r = max(row[0] for row in nums)
        while pq:
            l, i, j = heapq.heappop(pq)

            if r - l < result[1] - result[0]: result = l, r
            if j + 1 == len(nums[i]): return result

            v = nums[i][j + 1]
            r = max(r, v)
            heapq.heappush(pq, (v, i, j + 1))

# Keep a heap of the smallest elements.
# As we pop element A[i][j], we'll replace it with A[i][j+1].
# For each such element left, we want right, the maximum of the closest value in each row of the array that is >= left, which is also equal to the current maximum of our heap. We'll keep track of right as we proceed.
