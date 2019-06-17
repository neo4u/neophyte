# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
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

import collections
class Solution2(object):
    def findClosestLeaf(self, root, k):
        graph = collections.defaultdict(list)

        def dfs(node, par=None):
            if node:
                graph[node].append(par)
                graph[par].append(node)
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root)
        queue = collections.deque(node for node in graph if node and node.val == k)
        seen = set(queue)

        while queue:
            node = queue.popleft()
            if node:
                if len(graph[node]) == 1:
                    return node.val
                for nei in graph[node]:
                    if nei not in seen:
                        seen.add(nei)
                        queue.append(nei)


n1, n2 = TreeNode(1), TreeNode(2)
n1.left = n2

sol = Solution()
assert sol.findClosestLeaf(n1, 1) == 2

n1 = TreeNode(1)

sol = Solution()
assert sol.findClosestLeaf(n1, 1) == 1




