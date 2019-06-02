# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        levels = []
        self.dfs(root, levels, 0)
        # self.bfs(root, levels, 0)
        return levels

    def dfs(self, root, levels, level):
        if not root:
            return
        if len(levels) == level:
            levels.append([])
        levels[level].append(root.val)

        self.dfs(root.left, levels, level + 1)
        self.dfs(root.right, levels, level + 1)

    def bfs(self, root, levels, level):
        if not root:
            return
        q = [(root, 0)]

        while q:
            cur, lvl = q.pop(0)
            if lvl == len(levels):
                levels.append([])

            levels[lvl].append(cur.val)

            if cur.left:
                q.append((cur.left, lvl + 1))
            if cur.right:
                q.append((cur.right, lvl + 1))

