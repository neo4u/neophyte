import collections
from typing import List


TAB = '\t'
class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        self.graph = self.build_graph(edges)
        self.diameter = 0
        self.dfs(0, -1)
        return self.diameter - 1

    def dfs(self, node, parent, depth=0):
        print(f"{TAB * depth} dfs call node: {node}")
        max1, max2 = 0, 0

        for nbr in self.graph[node]:
            print(f"{TAB * depth} nbr: {nbr}")
            if nbr == parent: continue
            max_from_child = self.dfs(nbr, node, depth + 1)

            if max_from_child > max1:
                max2 = max1
                max1 = max_from_child
            elif max_from_child > max2:
                max2 = max_from_child

        self.diameter = max(self.diameter, max1 + max2 + 1)
        return max1 + 1

    def build_graph(self, edges):
        graph = collections.defaultdict(set)

        for u, v in edges:
            graph[v].add(u)
            graph[u].add(v)

        return graph



# 1245. Tree Diameter
# https://leetcode.com/problems/tree-diameter/description/


sol = Solution()
assert sol.treeDiameter([[0, 1], [0, 2]]) == 2
