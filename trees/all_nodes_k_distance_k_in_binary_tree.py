from typing import List
import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left, self.right = None, None


# Approach 1: Convert Tree to Graph, DFS and then BFS
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.graph = collections.defaultdict(list)
        self.dfs_convert(root, None)
        return self.bfs(target, k)

    def dfs_convert(self, node, parent):
        if not node: return

        if parent:
            self.graph[node.val].append(parent.val)
            self.graph[parent.val].append(node.val)

        self.dfs_convert(node.left, node)
        self.dfs_convert(node.right, node)

    def bfs(self, target, k):
        q, dist, visited = [target.val], 0, set([target.val])

        while q:
            if dist == k: return q
            level_q = []
            for node in q:
                for nbr in self.graph[node]:
                    if nbr in visited: continue
                    level_q.append(nbr)
                    visited.add(nbr)
            q = level_q
            dist += 1

        return []


# Approach 2: Percolate the distance
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.result = []
        self.dfs(root, target, k)
        return self.result

    # Return distance from node to target if exists, else -1
    # Vertex distance: the # of vertices on the path from node to target
    def dfs(self, node, target, k) -> int:
        if not node: return -1
        elif node == target:
            self.subtree_add(node, 0, k)
            return 1
        else:
            l, r = self.dfs(node.left, target, k), self.dfs(node.right, target, k)
            if l != -1:
                if l == k:
                    self.result.append(node.val)
                    # return -1
                self.subtree_add(node.right, l + 1, k)
                return l + 1
            elif r != -1:
                if r == k:
                    self.result.append(node.val)
                    # return -1
                self.subtree_add(node.left, r + 1, k)
                return r + 1
            else:
                return -1

    # Add all nodes 'K - dist' from the node to answer.
    def subtree_add(self, node: TreeNode, dist: int, k: int) -> None:
        if not node: return
        elif dist == k: self.result.append(node.val)
        else:
            self.subtree_add(node.left, dist + 1, k)
            self.subtree_add(node.right, dist + 1, k)



# 863. All Nodes Distance K in Binary Tree
# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/

# Intuition
# 1. We're not given a graph, we're given a tree. What is the diff you ask? Graph is presented as an adj list or adj matrix
#    Where as tree we're given access only to root, else a tree is a type of graph
#    Trees are directed acyclic graphs, so this poses a problem if our target node is a child of a parent
# 2. A simple way to think about it is to do a BFS level by level and exit at K.
#    It becomes a simple BFS with a visited set and we're guaranteed a solution due to the nature of BFS


# Approach 1: BFS

# Steps:
# 1. Do a DFS with an added parameter of parent and at each level, add the parent and node as neighbors to each other
#    in our graph dictionary, and then continue doing that for left and right sub-tree
# 2. Once the graph is built, simply do a BFS, we used a visited set to keep track of visted
# 3. We're guaranteed a valid solution as we're going level by level

# Complexity
# - O(n + m) where n is number of nodes and m is the number of edges but in a binary tree,
#   m is always n-1, so O(n) to be specific
# - Upper bounded by O(n) space where n is number of nodes

# Time: O(n)
# Space: O(n)

# Approach 2: DFS and Percolate Distance
# Time: O(n)
# Space: O(n)
