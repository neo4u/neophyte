from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        if not graph: return True
        n = len(graph)
        self.colors = [0] * n

        for i in range(n):
            if self.colors[i] == 0 and not self.dfs(graph, i, 1):
                return False

        return True

    def dfs(self, graph, node, color):
        if self.colors[node] != 0: return self.colors[node] == color
        self.colors[node] = color

        for nbr in graph[node]:
            if not self.dfs(graph, nbr, -color): return False

        return True



# 785. Is Graph Bipartite?
# https://leetcode.com/problems/is-graph-bipartite/description/

# Intuition
# 1. Bi-partite means that We should be able to color divide the graph into 2 sets such that
#    all the edges go from one set to the other
# 2. This can also be seen as if we color a node in one color and its neighbours in a second color,
#    the entire graph will only be colored into 2 colors for a bi-partite graph

# Steps:
# 1. We use DFS to color the entire graph
# 2. Within the DFS, we pass the node to start color and the color to start with,
#    we return true/false based on if coloring was possible or not
