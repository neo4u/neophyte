import heapq

def smallestRange(self, A):
    pq = [(row[0], i, 0) for i, row in enumerate(A)]
    heapq.heapify(pq)
    
    ans = -1e9, 1e9
    right = max(row[0] for row in A)
    while pq:
        left, i, j = heapq.heappop(pq)
        if right - left < ans[1] - ans[0]:
            ans = left, right
        if j + 1 == len(A[i]):
            return ans
        v = A[i][j+1]
        right = max(right, v)
        heapq.heappush(pq, (v, i, j+1))

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