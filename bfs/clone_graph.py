# Definition for a undirected graph node
import collections

class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

# Approach 1: BFS
class SolutionBFS:
    def cloneGraph(self, node):
        if not node: return None
        cloned = {node: Node(node.label)}
        queue = collections.deque([(node, cloned[node])])

        while queue:
            src, dst = queue.pop()
            for nbr in src.neighbors:
                if nbr not in cloned:
                    cloned[nbr] = Node(nbr.val)
                    queue.appendleft((nbr, cloned[nbr]))
                dst.neighbors.append(cloned[nbr])

        return cloned[node]

# Approach 2: DFS
class Solution:
    def cloneGraph(self, node):
        def dfs(node, cloned, depth=1):
            if node in cloned: return cloned[node]

            clone = Node(node.val, [])
            cloned[node] = clone

            for nbr in node.neighbors:
                clone.neighbors.append(dfs(nbr, cloned, depth + 1))

            return clone

        if not node: return None
        cloned = {}
        dfs(node, cloned, 0)

        return cloned[node]


# 133. Clone Graph
# https://leetcode.com/problems/clone-graph/description/

# Approach 1: BFS

# Approach 2: DFS
# Steps:
# 1. Keep a hash k: node, value: cloned node
# 2. Init the hash to empty hash
# 3. start dfs from root node
# 4. if node is in the hash, means its already cloned so just return the value from hash
# 5. Only if it wasn't cloned, create a clone and add to hash.
# 6. Also, only visited each neighbor of the node and do a dfs to get the neighbors clone
# 7. Add the returned cloned to the clone's neighbour
# 8. Return Clone

# node: 1
# node: 1, nbr: [1] Added
#         node: 2
#         node: 2, nbr: [1, 2] Added
#                 node: 1
#                 returning cloned
#                 node: 3
#                 node: 3, nbr: [1, 2, 3] Added
#                         node: 2
#                         returning cloned
#                         node: 4
#                         node: 4, nbr: [1, 2, 3, 4] Added
#                                 node: 1
#                                 returning cloned
#                                 node: 3
#                                 returning cloned
#         node: 4
#         returning cloned


node1, node2, node3, node4 = Node(1, []), Node(2, []), Node(3, []), Node(4, [])

node1.neighbors.append(node2)
node1.neighbors.append(node4)
node2.neighbors.append(node1)
node2.neighbors.append(node3)
node3.neighbors.append(node2)
node3.neighbors.append(node4)
node4.neighbors.append(node1)
node4.neighbors.append(node3)

sol = Solution()

clone1 = sol.cloneGraph(node1)
assert [node.val for node in clone1.neighbors] == [2, 4]

clone2 = clone1.neighbors[0]
assert [node.val for node in clone2.neighbors] == [1, 3]

clone3 = clone2.neighbors[1]
assert [node.val for node in clone3.neighbors] == [2, 4]

clone4 = clone3.neighbors[1]
assert [node.val for node in clone4.neighbors] == [1, 3]
