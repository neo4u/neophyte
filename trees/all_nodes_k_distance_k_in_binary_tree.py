# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections

class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        self.graph = collections.defaultdict(list)
        self.dfs_convert(root, None)
        print(self.graph)
        return self.bfs(target, K)

    def dfs_convert(self, node, parent):
        if not node: return

        if parent:
            self.graph[node.val].append(parent.val)
            self.graph[parent.val].append(node.val)

        self.dfs_convert(node.left, node)
        self.dfs_convert(node.right, node)


    def bfs(self, target, K):
        q, dist, visited = [target.val], 0, set([target.val])

        while q:
            if dist == K: return q
            level_q = []
            for node in q:
                for nbr in self.graph[node]:
                    if nbr in visited: continue
                    level_q.append(nbr)
                    visited.add(nbr)
            q = level_q
            dist += 1

        return []
