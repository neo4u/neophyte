class Solution(object):
    def subtreeWithAllDeepest(self, root):
        return self.dfs(root)[0]

    def dfs(self, node):
        # Return the result of the subtree at this node.
        if not node: return (None, 0)

        L, R = self.dfs(node.left), self.dfs(node.right)

        if L[1] > R[1]: return (L[0], L[1] + 1)
        if L[1] < R[1]: return (R[0], R[1] + 1)

        return (node, L[1] + 1)


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
