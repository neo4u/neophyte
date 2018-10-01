from collections import heapq
import collections

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        f = collections.defaultdict(dict)
        for a, b, p in flights:
            f[a][b] = p
        heap = [(0, src, k + 1)]
        while heap:
            p, i, k = heapq.heappop(heap)
            if i == dst:
                return p
            if k > 0:
                for j in f[i]:
                    heapq.heappush(heap, (p + f[i][j], j, k - 1))
        return -1

# It happen to be the same idea of Dijkstra's algorithm, but we need to keep the path while explore the grape.

# Adapted dijkstra
# Note: The code has been updated at 2018-2-18 17:33:41 (MST) to fix a bug pointed by @chang17 and @jray319. Thanks!
# Their test case should be added in. The testcases for the contest did not cover those.
# The fix makes the solution not really a Dijkstra that it is losing some property that Dijkstra has to use a priority queue. Instead, it falls into a BFS like solution.
# But since I effectively adapt it from Dijkstra, I decide to remain the original code in the bottom for anyone who is interested in the changes.

# This is basically an implementation for the Dijkstra algorithm based on the description in the book "Cracking the coding interview", page 634. Its description is really clear.
# The only thing that is "adapted" is highlighted in the code # this two lines are important below.

# Using vanila Dijkstra can help us figure out the shortest weighted path from the src to dst.
# But then we lose the information of those paths that can reach dst with less stop.
# So I record the information into the results list. Once it somehow reaches the dst from a path, we record it.

class Solution2(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        remain, ret, stop = [], float('inf'), 0
        weights = [sys.maxint for i in range(n)]
        graph = [{} for i in range(n)]
        for s,d,w in flights:
            graph[s][d]=w

        heapq.heappush(remain, (0, src))
        weights[src] = 0
        while remain and stop <= K:
            tmp, remain = remain, []
            while tmp:
                weight, node = heapq.heappop(tmp)
                for tonode, toweight in graph[node].items():
                    if weights[tonode] > weight + toweight:
                        weights[tonode] = weight + toweight
                        heapq.heappush(remain, (weights[tonode], tonode))    
                    # this two lines are important
                    if tonode == dst and weights[tonode]<ret:
                        ret = weights[tonode]
            stop+=1
        return ret if ret < float('inf') else -1


# Leetcode solution

class Solution3(object):
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

# Complexity Analysis
# Time Complexity: O(E + n \log n)O(E+nlogn), where EE is the total number of flights.
# Space Complexity: O(n)O(n), the size of the heap.