import collections
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.graph = collections.defaultdict(list)

        for src, dst in tickets: self.graph[src].append(dst)
        for city in self.graph: self.graph[city].sort()

        return self.dfs("JFK", [])[::-1]

    def dfs(self, city, path):
        while self.graph[city]:
            next_city = self.graph[city].pop(0)
            self.dfs(next_city, path)
        path.append(city)

        return path


# 332. Reconstruct Itinerary
# https://leetcode.com/problems/reconstruct-itinerary/description/


# Intuition:
# 1. The problem is to reconstruct the exact order or airports travelled given the tickets
# 2. This is a problem of finding the 'Eulerean Circuit', 
# 3. It's easy to understand as a reverse of a post order traversal
# 4. It's like finding a topological sort, but only this is for a Directed Cyclic Graph as opposed to a DAG,
#    That is the problem of Eulerean Path
# 5. The only thing is if two paths exist from a given airport,
#    then we pick lexical order hence we sort the destinations, from each city
# 6. Hierholzer’s Algorithm
#    https://www.geeksforgeeks.org/hierholzers-algorithm-directed-graph/


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
