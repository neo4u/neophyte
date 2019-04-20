class DSU:
    def __init__(self, N):
        self.ranks = [0] * (N+1)
        self.groups = list(range(N+1))
        
    def find(self, x):
        if self.groups[x] == x:
            return x
        return self.find(self.groups[x])
    
    def union(self, x, y):
        gx = self.find(x)
        gy = self.find(y)
        if gx == gy: 
            return False
        if self.ranks[gx] > self.ranks[gy]:
            self.groups[gy] = gx
        elif self.ranks[gx] < self.ranks[gy]:
            self.groups[gx] = gy
        else:
            self.groups[gy] = gx
            self.ranks[gy] += 1
        return True
        

class Solution:
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        def is_cycle(edge):
            x, y = edge
            while x != y and x in parent:
                x = parent[x]
            return x == y
            
        parent = {}
        first_edge = next_edge = None
        for p, c in edges:
            if c not in parent:
                parent[c] = p
            elif not first_edge and not next_edge:
                first_edge = [parent[c], c]
                next_edge = [p, c]

        if first_edge and next_edge:
            if is_cycle(first_edge):
                return first_edge
            return next_edge
            
        else:
            dsu = DSU(len(edges))
            for x, y in edges:
                if not dsu.union(x, y):
                    return [x, y]
        return []

# 685. Redundant Connection II
# https://leetcode.com/problems/redundant-connection-ii/description/

# Approach 1: DFS
# Approach 2: Disjoin Set Union Find 
# https://leetcode.com/problems/redundant-connection-ii/discuss/108058/one-pass-disjoint-set-solution-with-explain


# https://leetcode.com/problems/redundant-connection-ii/discuss/108070/Python-O(N)-concise-solution-with-detailed-explanation-passed-updated-testcases

# Time: O(n) where n is the number of vertices (and also the number of edges) in the graph.
#                  We perform a depth-first search.
# Space: O(n), the size of the graph.



