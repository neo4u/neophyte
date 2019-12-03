# BFS is used to iterate through the nodes, 
# where next node is determined using
# priority queue ordered by its distance from starting node K.
from collections import heapq

class Solution:
    def networkDelayTime(self, times, N, K):
        pq = []
        adj = [[] for _ in range(N+1)]
        for time in times:
            adj[time[0]].append((time[1], time[2]))

        fin, res = set(), 0
        heapq.heappush(pq, (0, K))

        while len(pq) and len(fin) != N:
            cur = heapq.heappop(pq)
            fin.add(cur[1])
            res = cur[0]
            for child, t in adj[cur[1]]:
                if child in fin: continue
                heapq.heappush(pq, (t+cur[0], child))

        return res if len(fin) == N else -1

# Nothing fancy, just apply Dijkstra's algorithm to the input. The only pitfall is that you have to check that all nodes are reachable from source node, else return -1.

# - Yangshun

class Solution2(object):
    def networkDelayTime(self, times, N, K):
        from collections import defaultdict
        nodes = defaultdict(dict)
        Q = set(range(N))
        for u, v, w in times:
            nodes[u - 1][v - 1] = w
        dist = [float('inf')] * N
        dist[K - 1] = 0
        while len(Q):
            u = None
            for node in Q:
                if u == None or dist[node] < dist[u]:
                    u = node
            Q.remove(u)
            for v in nodes[u]:
                alt = dist[u] + nodes[u][v]
                if alt < dist[v]:
                    dist[v] = alt
        d = max(dist)
        return -1 if d == float('inf') else d

import collections
# Leetcode solution dijkstra's without heap
class Solution0(object):
    def networkDelayTime(self, times, N, K):
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        dist = {node: float('inf') for node in range(1, N+1)}
        seen = [False] * (N+1)
        dist[K] = 0

        while True:
            cand_node = -1
            cand_dist = float('inf')
            for i in range(1, N+1):
                if not seen[i] and dist[i] < cand_dist:
                    cand_dist = dist[i]
                    cand_node = i

            if cand_node < 0: break
            seen[cand_node] = True
            for nei, d in graph[cand_node]:
                dist[nei] = min(dist[nei], dist[cand_node] + d)

        ans = max(dist.values())
        return ans if ans < float('inf') else -1


import collections
# Leetcode solution dijkstra's with heap
class Solution0b(object):
    def networkDelayTime(self, times, N, K):
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        pq = [(0, K)]
        dist = {}
        while pq:
            d, node = heapq.heappop(pq)
            if node in dist: continue
            dist[node] = d
            for nei, d2 in graph[node]:
                if nei not in dist:
                    heapq.heappush(pq, (d+d2, nei))

        return max(dist.values()) if len(dist) == N else -1