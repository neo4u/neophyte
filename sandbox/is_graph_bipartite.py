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
        self.colors[node] = color

        for nbr in graph[node]:
            if self.colors[nbr] != 0 and self.colors[nbr] != -color:
                return False
            if self.colors[nbr] == 0 and not self.dfs(graph, nbr, -color):
                return False

        return True


# 785. Is Graph Bipartite?
# https://leetcode.com/problems/is-graph-bipartite/description/

# [[1,2,3],[0,2],[0,1,3],[0,2]]
