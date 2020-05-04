import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Approach 1: DFS + DFS
class Solution1:
    def findClosestLeaf(self, root: TreeNode, k: int) -> int:
        self.path = None
        self.closest_leaf_map = {}
        self.dfs(root, k, [])
        self.dfs_closest_leaf(root)

        min_dist, closest_leaf, n = float('inf'), None, len(self.path)
        for i, node in enumerate(self.path):
            l, d = self.closest_leaf_map[node]
            d += n - 1 - i
            if d < min_dist:
                min_dist = d
                closest_leaf = l

        return closest_leaf.val

    def dfs_closest_leaf(self, node):
        if not node: return None, float('inf')
        if not node.left and not node.right:
            self.closest_leaf_map[node] = node, 0
            return node, 0

        l_node, l_dist, r_node, r_dist = None, float('inf'), None, float('inf')
        l_node, l_dist = self.dfs_closest_leaf(node.left)
        r_node, r_dist = self.dfs_closest_leaf(node.right)

        closest_leaf_dist = min(l_dist, r_dist) + 1
        closest_leaf = l_node if l_dist < r_dist else r_node

        self.closest_leaf_map[node] = closest_leaf, closest_leaf_dist
        return closest_leaf, closest_leaf_dist

    def dfs(self, node, k, path):
        if not node: return
        path = path + [node]

        if node.val == k:
            self.path = path
            return

        self.dfs(node.left, k, path)
        self.dfs(node.right, k, path)


# Approach 2: Use DFS to build graph and BFS to find distance
class Solution:
    def findClosestLeaf(self, root: TreeNode, k: int) -> int:
        self.graph = collections.defaultdict(list)
        self.dfs(root)

        q = [node for node in self.graph if node and node.val == k]
        visited = set(q)

        while q:
            node = q.pop(0)
            if not node: continue
            if len(self.graph[node]) == 1: return node.val # Means that the parent is only neighbor

            for nbr in self.graph[node]:
                if nbr in visited: continue
                visited.add(nbr)
                q.append(nbr)

    def dfs(self, node, parent=None):
        if not node: return

        self.graph[node].append(parent)
        self.graph[parent].append(node)

        self.dfs(node.left, node)
        self.dfs(node.right, node)


n1, n2 = TreeNode(1), TreeNode(2)
n1.left = n2

sol = Solution()
assert sol.findClosestLeaf(n1, 1) == 2

n1 = TreeNode(1)

sol = Solution()
assert sol.findClosestLeaf(n1, 1) == 1


# 742. Closest Leaf in a Binary Tree
# https://leetcode.com/problems/closest-leaf-in-a-binary-tree/description/


# Intuition
# 1. Use DFS to make a adjacency list
# 2. Use BFS from every node having node.val to calculate distance from root wave by wave
# 3. Exit and return dist as soon as you see a leaf of the tree
