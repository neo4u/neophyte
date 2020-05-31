# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        return self.dfs(root)[0]

    def dfs(self, node):
        # Return the result of the subtree at this node.
        if not node: return (None, 0)

        l, r = self.dfs(node.left), self.dfs(node.right)

        if l[1] > r[1]: return (l[0], l[1] + 1)
        if l[1] < r[1]: return (r[0], r[1] + 1)

        return (node, l[1] + 1)


# 865. Smallest Subtree with all the Deepest Nodes
# https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/description/

# Input: [3,5,1,6,2,0,8,null,null,7,4]

#         3
#       /    \
#      /      \
#     5        1 
#    / \      / \
#   6   2    0   8  
#      / \
#     7   4

# Output: [2,7,4]
# Explanation:
