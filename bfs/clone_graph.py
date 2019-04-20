# Definition for a undirected graph node
import collections

class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node

    def cloneGraph(self, node):
        if not node: return None
        cloned = {node: UndirectedGraphNode(node.label)}
        queue = collections.deque([(node, cloned[node])])

        while queue:
            src, dst = queue.pop()
            for v in src.neighbors:
                if v not in cloned:
                    cloned[v] = UndirectedGraphNode(v.label)
                    queue.appendleft((v, cloned[v]))
                dst.neighbors.append(cloned[v])
        
        return cloned[node]


