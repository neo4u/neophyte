from collections import heapq

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        f = collections.defaultdict(dict)

        for a, b, p in flights:
            f[a][b] = p
        q = [(0, src, k + 1)]

        while q:
            p, i, k = heapq.heappop(q)
            if i == dst:
                return p
            if k > 0:
                for j in f[i]:
                    heapq.heappush(q, (p + f[i][j], j, k - 1))

        return -1

import collections

# LC Solution
class Solution2(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        graph = collections.defaultdict(dict)
        for u, v, w in flights:
            graph[u][v] = w

        best = {}
        pq = [(0, 0, src)]

        while pq:
            cost, k, place = heapq.heappop(pq)

            if k > K+1 or cost > best.get((k, place), float('inf')): continue
            if place == dst: return cost

            for nei, wt in graph[place].iteritems():
                newcost = cost + wt
                if newcost < best.get((k+1, nei), float('inf')):
                    heapq.heappush(pq, (newcost, k+1, nei))
                    best[k+1, nei] = newcost

        return -1


# 787. Cheapest Flights Within K Stops
# https://leetcode.com/problems/cheapest-flights-within-k-stops/description/
