import collections

class Solution(object):
    def findRedundantConnection(self, edges):
        graph = collections.defaultdict(set)

        def dfs(source, target):
            print(f"s: {source} | d: {target} | seen: {seen}")
            if source not in seen:
                seen.add(source)
                if source == target: return True
                return any(dfs(nei, target) for nei in graph[source])

        for u, v in edges:
            seen = set()
            if u in graph and v in graph and dfs(u, v):
                return u, v
            graph[u].add(v)
            graph[v].add(u)

class DSU(object):
    def __init__(self):
        self.par = range(1001)
        self.rnk = [0] * 1001

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        elif self.rnk[xr] < self.rnk[yr]:
            self.par[xr] = yr
        elif self.rnk[xr] > self.rnk[yr]:
            self.par[yr] = xr
        else:
            self.par[yr] = xr
            self.rnk[xr] += 1
        return True

class Solution2(object):
    def findRedundantConnection(self, edges):
        dsu = DSU()
        for edge in edges:
            if not dsu.union(*edge):
                return edge


sol = Solution()
sol.findRedundantConnection([[1,2], [1,3], [2,3]]) == (2,3)


# 684. Redundant Connection
# https://leetcode.com/problems/redundant-connection/description/

# Approach 1: DFS
# Appraoch 2: Disjoin Set Union-Find
