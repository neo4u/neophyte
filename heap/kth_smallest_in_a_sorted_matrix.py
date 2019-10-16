from typing import List


# Approach 1: Binary Search
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        start, end = matrix[0][0], matrix[n - 1][n - 1]

        while start < end:
            mid = start + (end - start) // 2
            smaller, larger = (matrix[0][0], matrix[n - 1][n - 1])
            count, smaller, larger = self.count_less_equal(matrix, mid, smaller, larger)

            if count == k:  return smaller
            if count < k:   start = larger  # search higher
            else:           end = smaller  # search lower

        return start

    def count_less_equal(self, matrix, mid, smaller, larger):
        count, n = 0, len(matrix)
        r, c = n - 1, 0

        while r >= 0 and c < n:
            if matrix[r][c] > mid:
                # as matrix[r][c] > mid, let's keep track of the smallest number > mid
                larger = min(larger, matrix[r][c])
                r -= 1
            else:
                # as matrix[r][c] <= mid, let's keep track of the biggest number <= mid
                smaller = max(smaller, matrix[r][c])
                count += r + 1
                c += 1

        return count, smaller, larger


# Approach 2: heap (Optimal)
import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        heap, result = [(matrix[r][0], r, 0) for r in range(min(k, n))], 0
        heapq.heapify(heap)

        for _ in range(k):
            result, r, c = heapq.heappop(heap)
            new_c = c + 1
            if new_c < n:
                heapq.heappush(heap, (matrix[r][new_c], r, new_c))

        return result



# 378. Kth Smallest Element in a Sorted Matrix
# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/


# Approach 1: Binary Search
# Grokking the coding interview solution

# Similar to
# Actually, if u've done problem 719. Find K-th Smallest Pair Distance
# The idea behind the two problems with binary search is exactly the same:
# Similar solution for 719. Find K-th Smallest Pair Distance

# Also don't forget to check out this fantastic post by @fun4LeetCode
# Approach the problem using the "trial and error" algorithm


# Approach 2: heap (Optimal)
# Steps:
# 1. Push every 0th element of each row into a heap
# 2. We pop k times from the heap
# 3. For every heappop, if the next column index is in range of the matrix,
#    we push the element in the next column,
# 4. If the col index is not in range, then we just move to the next iteration


# Time: O(klogn), Cuz O(min(n,k) + klog(n)) = O(klogn), O(min(n,k) = first loop for putting into heap
#                 and k pushes leading to k * log(n)
# Space: O(k)
