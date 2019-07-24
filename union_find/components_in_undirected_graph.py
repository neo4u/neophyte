class DS:
    def __init__(self):
        self.parent = {}
        self.rank = {}
        self.count = 0

    def find(self, x):
        if x != self.parent[x]: self.parent[x] = self.find(self.parent[x])
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


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ds = DS()
        for node in range(n): ds.set_parent(node)
        for u, v in edges: ds.union(u, v)

        return ds.count


# 323. Number of Connected Components in an Undirected Graph
# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/description/
