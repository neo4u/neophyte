from collections import defaultdict
from typing import List

TAB = '\t'

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = self.make_graph(connections) # vertex i ==> [its neighbors]
        node = 0             # The label of the current node
        rank = 0                # Please note this rank is NOT the num (name) of the vertex itself, it is the order of your DFS level
        prev = -1               # Dummy value. Start value doesn't matter. Used to keep track of prev node
        visited = [False] * n   # common DFS/BFS method to mark whether this node is seen before
        lowest = [0] * n        # here lowestRank[i] represents the lowest order of vertex that can reach this vertex i
        self.result = []             # For the result

        self.dfs(graph, node, prev, visited, lowest, rank)
        return self.result

    def dfs(self, graph: dict, node: int, prev: int, visited: List[int], lowest: List[int], rank: int) -> None:
        lowest[node], visited[node] = rank, True
        print(f'{TAB * rank}DFS to: {node}')
        print(f'{TAB * rank}Lowest: {lowest}')

        for nbr in graph[node]:
            print(f'{TAB * rank}nbr: {nbr}')
            if prev == nbr: continue # do not include the incoming path to this vertex since this is the possible ONLY bridge (critical connection) that every vertex needs
            if not visited[nbr]: self.dfs(graph, nbr, node, visited, lowest, rank + 1)

            lowest[node] = min(lowest[node], lowest[nbr]) # take the min of the current vertex's and next vertex's ranking
            print(f'{TAB * rank}Lowest: {lowest}')

            if lowest[nbr] >= rank + 1: # If all the neighbors lowest rank is higher than mine + 1, then it means I am one connecting critical connection
                print(f'{TAB * rank}lowest[nbr]: {lowest[nbr]}, rank + 1: {rank + 1}')
                self.result.append([nbr, node])
        print(f'{TAB * rank}result: {self.result}')

    def make_graph(self, connections):
        graph = defaultdict(list)

        for k, v in connections:
            graph[k].append(v)
            graph[v].append(k)

        return graph



# class Solution:
#     def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
#         graph = [[] for _ in range(n)]      ## vertex i ==> [its neighbors]
#         currentRank = 0                     ## please note this rank is NOT the num (name) of the vertex itself, it is the order of your DFS level
#         lowestRank = [i for i in range(n)]  ## here lowestRank[i] represents the lowest order of vertex that can reach this vertex i
#         visited = [False for _ in range(n)] ## common DFS/BFS method to mark whether this node is seen before

#         ## build graph:
#         for u, v in connections:
#             ## this step is straightforward, build graph as you would normally do
#             graph[u].append(v)
#             graph[v].append(u)

#         res = []
#         prevVertex = -1 ## This -1 a dummy. Does not really matter in the beginning.
#         # It will be used in the following DFS because we need to know where the current DFS level comes from.
#         # You do not need to setup this parameter, I setup here ONLY because it is more clear to see what are passed on in the DFS method.
#         currentVertex = 0 ## we start the DFS from vertex num 0 (its rank is also 0 of course)
#         self._dfs(res, graph, lowestRank, visited, currentRank, prevVertex, currentVertex)
#         return res

#     def _dfs(self, res, graph, lowestRank, visited, currentRank, prevVertex, currentVertex):
#         visited[currentVertex] = True
#         lowestRank[currentVertex] = currentRank

#         for nextVertex in graph[currentVertex]:
#             if nextVertex == prevVertex: continue ## do not include the the incoming path to this vertex since this is the possible ONLY bridge (critical connection) that every vertex needs.

#             if not visited[nextVertex]:
#                 self._dfs(res, graph, lowestRank, visited, currentRank + 1, currentVertex, nextVertex)
#                 # We avoid visiting visited nodes here instead of doing it at the beginning of DFS.
#                 # the reason is, even that nextVertex may be visited before, we still need to update my lowestRank using the visited vertex's information.

#             lowestRank[currentVertex] = min(lowestRank[currentVertex], lowestRank[nextVertex])
#             # take the min of the current vertex's and next vertex's ranking
#             if lowestRank[nextVertex] >= currentRank + 1: ####### if all the neighbors lowest rank is higher than mine + 1, then it means I am one connecting critical connection ###
#                 res.append([currentVertex, nextVertex])


sol = Solution()
assert list(map(sorted, sol.criticalConnections(4, [[0, 1], [1, 2], [2, 0], [1, 3]]))) == list(map(sorted, [[1, 3]]))
# assert list(map(sorted, sol.criticalConnections(6, [[0, 1], [1, 2], [2, 0], [1, 3], [3, 4], [4, 5], [5, 3]]))) == list(map(sorted, [[1, 3]]))

# Intuition:
# - An edge is a critical connection, if and only if it is not in a cycle.
# - So, if we discard all cycle edges, then critical connections remain.
# - We use DFS to decide if a edge is in the cycle, we use concept of rank
