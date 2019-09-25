from typing import List

# Approach 1: Sort


# Approach 2: Heap
import heapq
class Solution2:
    def kClosest(self, points, K):
        return heapq.nsmallest(K, points, lambda x, y: x**2 + y**2)

import heapq
class Solution3:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        for (x, y) in points:
            dist = -(x*x + y*y)
            if len(heap) == K:
                heapq.heappushpop(heap, (dist, x, y))
            else:
                heapq.heappush(heap, (dist, x, y))

        return [(x, y) for (dist, x, y) in heap]


# Approach 3: Quick Select
import random
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if not k or not points: return []
        n = len(points)
        if k == n: return points
        self.quick_select(points, k, 0, n - 1)
        return points[:k]

    def quick_select(self, points, k, l, r):
        if l == r: return
        q = self.rand_partition(points, k, l, r)
        if q == k: return

        if k < q:   self.quick_select(points, k, l, q - 1)
        else:       self.quick_select(points, k, q + 1, r)

    def rand_partition(self, points, k, l, r):
        q = random.randint(l, r)
        points[r], points[q] = points[q], points[r]
        return self.partition(points, k, l, r)

    def partition(self, points, k, l, r):
        i, pivot = l - 1, self.distance(points[r])

        for j in range(l, r):
            if self.distance(points[j]) >= pivot: continue
            i += 1
            points[i], points[j] = points[j], points[i]

        points[i + 1], points[r] = points[r], points[i + 1]
        return i + 1

    def distance(self, point):
        x, y = point
        return x**2 + y**2



# 973. K Closest Points to Origin
# https://leetcode.com/problems/k-closest-points-to-origin/description/


# Approach 1: Sort
# Steps:
# 1. Sort using distances (x^2 + y^2) as key for sorting the given points
# 2. Select the first k elements

# Time: O(nlog(n))
# Space: O(1)

# Approach 2: Heap

# Time: O(N * log(k))
# Space: O(k)

# Approach 3: Quick Select (Optimal)
# Steps:
# 1. Do quick select on points to get k smallest distances
# 2. while partitioning them, use distance of the point from origin as pivot

# Time: avg O(n), worst O(n ^ 2)
# Space: O(n)

sol = Solution()
assert sol.kClosest([[0, 1], [1, 0]], 2) == [[0, 1], [1, 0]]
