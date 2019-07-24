import heapq

class Solution(object):
    def kthSmallest(self, matrix, k):
        heap = [(row[0], r, 0) for r, row in enumerate(matrix) if row]
        heapq.heapify(heap)

        for _ in range(k - 1):
            _, row, col = heapq.heappop(heap)

            if col + 1 < len(matrix[row]):
                heapq.heappush(heap, (matrix[row][col + 1], row, col + 1))

        return heap[0]

# 378. Kth Smallest Element in a Sorted Matrix
# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/