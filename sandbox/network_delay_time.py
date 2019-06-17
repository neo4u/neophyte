import collections
from typing import List

class Solution(object):
    def networkDelayTime(self, times, N, K):
        self.graph = collections.defaultdict(list)
        for u, v, w in times:
            self.graph[u].append((w, v))

        self.dist = {node: float("inf") for node in range(1, N + 1)}

        self.dfs(K, 0)
        ans = max(self.dist.values())
        return ans if ans < float("inf") else -1

    def dfs(self, node, elapsed):
        if elapsed >= self.dist[node]: return
        self.dist[node] = elapsed

        for time, nei in sorted(self.graph[node]):
            self.dfs(nei, elapsed + time)

import heapq
class Solution2:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
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
                    heapq.heappush(pq, (d + d2, nei))

        return max(dist.values()) if len(dist) == N else -1
