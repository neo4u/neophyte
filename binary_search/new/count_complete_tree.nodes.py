# compare the depth between left sub tree and right sub tree.
# A, If it is equal, it means the left sub tree is a full binary tree
# B, It it is not , it means the right sub tree is a full binary tree


class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def countNodes(self, root):
        if not root:
            return 0
        leftDepth = self.getDepth(root.left)
        rightDepth = self.getDepth(root.right)
        if leftDepth == rightDepth:
            return pow(2, leftDepth) + self.countNodes(root.right)
        else:
            return pow(2, rightDepth) + self.countNodes(root.left)

    def getDepth(self, root):
        if not root:
            return 0
        return 1 + self.getDepth(root.left)


class Solution:
    def countNodes(self, root):
        if not root: return 0

        dl, dr = self.left_depth(root.left), self.right_depth(root.right)
        if dl == dr:
            return 2**dl - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def left_depth(self, node):
        d = 0
        while node:
            d += 1
            node = node.left
        return d

    def right_depth(self, node):
        d = 0
        while node:
            d += 1
            node = node.right
        return d


# O(log(n)^2)