class Solution(object):
    def rob(self, root):
        return self.robDFS(root)[1];
    def robDFS(self,node):
        if node is None:
            return (0,0)
        l = self.robDFS(node.left)
        r = self.robDFS(node.right)
        return (l[1] + r[1], max(l[1] + r[1], l[0] + r[0] + node.val))

# Let
# f1(node) be the value of maximum money we can rob from the subtree with node as root ( we can rob node if necessary).
# f2(node) be the value of maximum money we can rob from the subtree with node as root but without robbing node.
# Then we have
# f2(node) = f1(node.left) + f1(node.right) and
# f1(node) = max( f2(node.left)+f2(node.right)+node.value, f2(node) ).

# Step by step tackling of the problem
# https://leetcode.com/problems/house-robber-iii/discuss/79330/Step-by-step-tackling-of-the-problem