from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# THIS DOESN'T SEEM TO WORK, WHYY????
# class Solution:
#     def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
#         self.result = []
#         self.dfs(root, sum, [])
#         return self.result

#     def dfs(self, node, sum, path):
#         if not node and sum == 0: return self.result.append(path)

#         val, diff = node.val, sum - node.val
#         self.dfs(node.left, sum - val, path + [val])
#         self.dfs(node.right, sum - val, path + [val])


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        self.result = []
        self.dfs(root, sum, [])
        return self.result

    def dfs(self, node, sum, path):
        if not node: return

        if self.is_leaf(node) and sum == node.val:
            path.append(node.val)
            self.result.append(path)

        val, diff = node.val, sum - node.val
        self.dfs(node.left, diff, path + [val])
        self.dfs(node.right, diff, path + [val])

    def is_leaf(self, node):
        return not node.left and not node.right
