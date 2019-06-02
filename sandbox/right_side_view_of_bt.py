# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root: return []
        q, result = [root], []

        while q:
            n, level_right_node = len(q), None

            for i in range(n):
                node = q.pop(0)
                level_right_node = node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)

            result.append(level_right_node)

        return result
