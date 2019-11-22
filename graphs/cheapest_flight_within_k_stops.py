from typing import List


# Approach 2: Dijkstra's with a priority queue
# Traverse K + 2 nodes we get to k + 2th node with k stops excluding src and dst
import collections
import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(dict)
        for u, v, w in flights: graph[u][v] = w
        costs, pq = {}, [(0, 0, src)]

        while pq:
            cost, stops, city = heapq.heappop(pq)

            if stops >= K + 2 and cost > costs.get((stops, city), float('inf')): continue
            if city == dst: return cost

            for nbr, wt in graph[city].items():
                new_cost = cost + wt
                if new_cost < costs.get((stops + 1, nbr), float('inf')):
                    heapq.heappush(pq, (new_cost, stops + 1, nbr))
                    costs[stops + 1, nbr] = new_cost

        return -1


from collections import defaultdict
import heapq

class Solution1:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = defaultdict(dict)
        for u, v, w in flights: graph[u][v] = w

        visited, q = set(), [[0, 0, src]]
        while q:
            cost, step, u = heapq.heappop(q)
            #print(cost, step, u)
            if u == dst: return cost
            if step > K: continue
            visited.add(u)

            for v in graph[u]:
                if v in visited: continue
                heapq.heappush(q, [cost + graph[u][v], step + 1, v])

        return -1

# Approach 3: Bellman-Ford (which is a case of DP)
# class Solution3:
#     def findCheapestPrice(self, cities, flights, src, dst, stops):

#         dp = [inf for i in range(cities)]
#         dp[src] = 0

#         # pre-invariant: dp represents dp[k]
#         for k in range(stops + 1):
#             dpnext = [dp[i] for i in range(cities)]
#             notChanged = True
#             # the order in which we compute the minimum for each dp[k][des] does not matter
#             # so we simply traverse through the edge list and consider each edge once
#             for ori, des, price in flights:
#                 if price + dp[ori] < dpnext[des]:
#                     dpnext[des] = price + dp[ori]
#                     notChanged = False
#             # if dp[k+1] is the same as dp[k], then there will be no change in the following
#             # iterations either, so we simply stop right here 
#             # (all absolute cheapest paths have been found)
#             if notChanged: break
#             dp = dpnext

#         # by pre-invariant and definition of dp, dp[d] now represents the
#         # cheapest price of all paths from @scr to @d with up to k stops
#         return dp[dst]


# 787. Cheapest Flights Within K Stops
# https://leetcode.com/problems/cheapest-flights-within-k-stops/description/


# Approach 1: Maintain cheapest to target
# Don't bother, it's not clear

# Time: O(E * K), where E is the length of flights.
# Space: O(n), the space used to store dis and pre.

# Approach 2: Dijkstra's with a priority queue
# Best for interview

# Time: O(E + (n * log(n))), where E is the total number of flights.
# Space: O(n), the size of the heap.

# Approach 3: Bellman-Ford (which is a case of DP)
# Note sure if this is better in anyways, it's complicated and confusing, 
# First of all why Bellman ford instead of dijstrak's???

# Refer: https://www.geeksforgeeks.org/bellman-ford-algorithm-dp-23/

# dp[k][d] is the cheapest price of all routes from @src to @d
# with up to k+1 nodes (k-1 stops)
# Thus, dp[k][d] = minimum among
# - dp[k-1][d]
# - for all edges(u, d), (cost(u, d) + dp[k-1][u])
# Notice dp[0][d] = 0 if d == src, else inf

# The idea is that, if we want to find the cheapest path from @src to @d
# with up to k+1 nodes, we either go with what's cheapest from @src to @d
# with up to k nodes, or we try all paths to nodes that can connect to @d
# with k nodes, and then append that connecting edge at the end, which would
# yield a path of k+1 nodes

# We claim that if value from second clause of recurrence is taken, then it must
# be a path of k nodes, because if it's p < k nodes, it would have
# been considered earlier during computation of dp[p][d], which makes dp[k-1][d] <= dp[p][d]
# thus it could not have been the minimum that's picked

# notice that dp[k][...] only depends on dp[k-1][...], thus we only keep a single array
# we start with dp[0], which is easy to initialize as we described above

# Time: 
# Space: 

sol = Solution()
n = 3
edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 1
assert sol.findCheapestPrice(n, edges, src, dst, k) == 200

n = 3
edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 0
assert sol.findCheapestPrice(n, edges, src, dst, k) == 500
