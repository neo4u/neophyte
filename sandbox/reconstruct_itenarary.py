import collections
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        path = []
        for u, v in tickets: graph[u].append(v)
        for city in graph.keys(): graph[city].sort()

        return self.dfs(graph, 'JFK', path)

    def dfs(self, graph, city, path):
        while graph[city]:
            next_city = graph[city].pop(0)
            self.dfs(graph, next_city, path)

        path.insert(0, city)
        return path

# https://www.geeksforgeeks.org/euler-circuit-directed-graph/

sol = Solution()
assert sol.findItinerary(
    [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
) == ["JFK","MUC","LHR","SFO","SJC"]
assert sol.findItinerary(
    [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
) == ["JFK","ATL","JFK","SFO","ATL","SFO"]

assert sol.findItinerary(
    [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
) == ["JFK","NRT","JFK","KUL"]
