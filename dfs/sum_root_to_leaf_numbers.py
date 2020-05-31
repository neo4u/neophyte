# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.sum = 0
        self.dfs(root, '')
        return self.sum

    def dfs(self, node, num_str):
        if not node: return

        value = num_str + str(node.val)
        is_leaf = not node.left and not node.right

        if is_leaf:
            self.sum += int(value)
        else:
            self.dfs(node.left, value)
            self.dfs(node.right, value)


# 129. Sum Root to Leaf Numbers
# https://leetcode.com/problems/sum-root-to-leaf-numbers/description/

# Similar Problems
# https://leetcode.com/problems/sum-root-to-leaf-numbers/discuss/585184/Clean-Python-Solution-(DFS-With-Other-Similar-Problems)
