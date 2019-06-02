# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def str2tree(self, s: str) -> TreeNode:
        self.open, self.close = "(", ")"
        root, _ = self.construct_subtree(s, 0)
        return root

    def construct_subtree(self, s, i):
        if i == len(s):
            return None, -1

        num = ""
        while i < len(s) and s[i] not in [self.open, self.close]:  # Construct root
            num += s[i]
            i += 1

        root = TreeNode(int(num))

        if i == len(s):
            return root, i
        if s[i] == self.close:
            return root, i + 1
        else:  # Construct left
            root.left, j = self.construct_subtree(s, i + 1)

        if j == len(s):
            return root, j
        if s[j] == self.close:
            return root, j + 1
        else:  # Construct right
            root.right, k = self.construct_subtree(s, j + 1)

        return root, k + 1

# 6(5)

# Input: "4(2(3)(1))(6(5))"
# Output: return the tree root node representing the following tree:

#        4
#      /   \
#     2     6
#    / \   / 
#   3   1 5  