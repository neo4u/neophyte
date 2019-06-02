from heapq import heappush, heappop

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        workers = [(w/q, w, q) for w, q in zip(wage, quality)]
        workers.sort()
        heap, sumq, ans = [], 0, float('inf')

        for ratio, w, q in workers:
            sumq += q
            heappush(heap, -q)

            if len(heap) > K: sumq -= abs(heappop(heap))
            if len(heap) == K: ans = min(ans, ratio * sumq)

        return ans


# r 2        3 4 5 6  7
# q 10       9 8 7 6  5

# c 20 27  

# 24/3, 30/2, 30/1
# 8.0,  15.0  30


# 10/ 5 , 20/ 6, 30/4
# 2.0, 3.3, 7.5

# 5,4,3

# group: 1
# (5,6,4)
# 7.5 (5+6+4)
# 7.5 * 15 = 112.5

# group 2:
# (5,4,3)
# 8 * (12) = 96