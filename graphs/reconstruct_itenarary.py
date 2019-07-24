import collections
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for u, v in tickets: graph[u].append(v)
        for city in graph.keys(): graph[city].sort()

        return self.dfs(graph, 'JFK', [])[::-1]

    def dfs(self, graph, city, path):
        while graph[city]:
            next_city = graph[city].pop(0)
            self.dfs(graph, next_city, path)

        path.append(city)
        return path

# Here is some points to understand this algs and hope it helps.

# In Eulerian paths, there must exist a start node(which is JFK in this problem) and a end node.
# End node can be start node or another node.
# end node is start node iff all nodes has even degree.
# end node is another node iff there is another odd degree node and start node has an odd degree.
# So, the algorithm is to find the end node first and delete the path to this node(backtrack), meanwhile using PriorityQueue to guarantee lexical order.
# Really amazing solution, I always don't know how to deal with Euler Path and know I begin to be some less confused.


# Input: [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
# Output: ["JFK","LHR","SJC","SFO","MUC"]
# Expected: ["JFK","MUC","LHR","SFO","SJC"]

# jfk: [muc]
# muc: [lhr]
# lhr: [sfo]
# sfo: [sjc]
# [sjc, sfo, lhr, muc, jfk] reverse this to get answer

# jfk nc = muc
#     [sjc, sfo, lhr, muc, jfk]
#     dfs(muc, [])
#         [sjc, sfo, lhr, muc]
#         dfs(lhr, [])
#             [sjc, sfo, lhr]
#             dfs(sfo, [])
#                 [sjc, sfo]
#                 dfs(sjc, [])
#                 [sjc]

# jfk: [muc]
# muc: [lhr]
# lhr: [sfo]
# sfo: [sjc, blr]
# blr: [sfo]

# jfk nc = muc
#     []
#     dfs(muc, [])
#         []
#         dfs(lhr, [])
#             dfs(sfo, [])
#                 dfs(blr, [])
#                 [blr]
#                 dfs(sjc, [blr])
#                 [blr, sjc]
#             return [blr, sjc, sfo]
#          ret  [blr, sjc, sfo, lhr]



# https://www.geeksforgeeks.org/euler-circuit-directed-graph/


# Hamiltonian Path vs Spanning Tree
# https://www.quora.com/What-is-the-difference-between-hamiltonian-path-and-spanning-tree


sol = Solution()
assert sol.findItinerary(
    [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
) == ["JFK","MUC","LHR","SFO","SJC"]
# Graph
# jfk: [muc]
# muc: [lhr]
# lhr: [sfo]
# sfo: [sjc]

assert sol.findItinerary(
    [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
) == ["JFK","ATL","JFK","SFO","ATL","SFO"]
# graph
# jfk: [sfo, atl]
# sfo: [atl]
# atl: [jfk, sfo]
# jfk -> atl -> jfk -> sfo -> atl -> sfo
# jfk: []
# sfo: []
# ztl: [sfo]
# jfk -> sfo -> ztl -> jfk -> ztl -> sfo

assert sol.findItinerary(
    [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
) == ["JFK","NRT","JFK","KUL"]

# graph

# jfk: [kul, nrt]
# nrt: [jfk]

# dfs(jfk, [])
#     dfs(kul, [])
#     ret [kul]
#     dfs(nrt, [kul])
#         dfs(jfk, [kul])
#         return [kul, jfk]
#     return [kul, jfk, nrt]
# return [kul, jfk, nrt, jfk] reverse to get answer
