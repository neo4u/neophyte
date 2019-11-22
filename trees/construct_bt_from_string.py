# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def str2tree(self, s: str) -> TreeNode:
        if not s: return None
        root, _ = self.dfs(s, 0)
        return root

    def dfs(self, s, i):
        start = i
        while i < len(s) and s[i] in '-0123456789': i += 1  # negative sign or digit
        node = TreeNode(int(s[start:i]))

        # Construct left sub-tree
        if i < len(s) and s[i] == '(':
            i += 1                          # skip '('
            node.left, i = self.dfs(s, i)
            i += 1                          # skip ')'

        # Construct right sub-tree
        if i < len(s) and s[i] == '(':      # still has '(', create right tree
            i += 1                          # skip '('
            node.right, i = self.dfs(s, i)
            i += 1                          # skip ')'

        return node, i                      # Return the root of sub-tree, and index to start consuming chars for next level


# 536. Construct Binary Tree from String
# https://leetcode.com/problems/construct-binary-tree-from-string/description/

# Input: "4(2(3)(1))(6(5))"
# Output: return the tree root node representing the following tree:

#        4
#      /   \
#     2     6
#    / \   / 
#   3   1 5

# 5(1(2))(4(6))
