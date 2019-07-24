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

            for _ in range(n):
                node = q.pop(0)
                level_right_node = node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)

            result.append(level_right_node)

        return result

class Solution2:
    def leftSideView(self, root: TreeNode) -> List[int]:
        if not root: return []
        q, result = [root], []

        while q:
            n, level_left_node = len(q), None

            for _ in range(n):
                node = q.pop(0)
                if not level_left_node: level_left_node = node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)

            result.append(level_left_node)

        return result



# 199. Binary Tree Right Side View
# https://leetcode.com/problems/binary-tree-right-side-view/description/
