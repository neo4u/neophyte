class Solution(object):
    def subtreeWithAllDeepest(self, root):
        return self.dfs(root)[0]

    def dfs(node):
        # Return the result of the subtree at this node.
        if not node: return (None, 0)
        L, R = dfs(node.left), dfs(node.right)
        if L[1] > R[1]: return (L.node, L.dist + 1)
        if L[1] < R: return (R.node, R.dist + 1)
        return (node, L.dist + 1)


# 865. Smallest Subtree with all the Deepest Nodes
# https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/description/

