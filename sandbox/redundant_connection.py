class DS:
    def __init__(self):
        self.parent = {}
        self.rank = {}
        self.count = 0

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def has_parent(self, x):
        return x in self.parent

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py: return False

        if self.rank[px] > self.rank[py]:
            self.parent[py] = px
        elif self.rank[py] > self.rank[px]:
            self.parent[px] = py
        else:
            self.parent[py] = px
            self.rank[px] += 1

        self.count -= 1
        return True

    def set_parent(self, x):
        self.parent[x] = x
        self.rank[x] = 0
        self.count += 1

    def print_ds(self):
        print(self.parent)
        print(self.count)

import collections
class Solution:
    def findRedundantConnection(self, edges):
        ds = DS()

        for u, v in edges:
            if not ds.has_parent(u): ds.set_parent(u)
            if not ds.has_parent(v): ds.set_parent(v)
            if not ds.union(u, v): return [u, v]

        return []


import collections
class Solution:
    def findRedundantConnection(self, edges):
        if not edges: return []
        self.graph = collections.defaultdict(set)

        for u, v in edges:
            visited = set()
            if u in self.graph and v in self.graph and self.dfs(u, v, visited): return [u, v]
            self.graph[u].add(v)
            self.graph[v].add(u)

        return []

    def dfs(self, s, d, visited):
        visited.add(s)
        if s == d: return True

        for nbr in self.graph[s]:
            if nbr not in visited and self.dfs(nbr, d, visited): return True

        return False