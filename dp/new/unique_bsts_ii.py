class Solution(object):
    def generateTrees(self, n):
        if n == 0:
            return []
        tree_list = [[[None]] * (n + 2) for i in xrange( n+ 2)]
        for i in xrange(1, n+1):
            tree_list[i][i] = [TreeNode(i)]
            for j in xrange(i-1, 0, -1):
                tree_list[j][i] = []
                for k in xrange(j, i+1):
                    for left in tree_list[j][k-1]:
                        for right in tree_list[k+1][i]:
                            root = TreeNode(k)
                            (root.left, root.right) = (left, right)
                            tree_list[j][i].append(root)
        return tree_list[1][n]

# Using reversed
class Solution:
    # @return a list of tree node

    def generateTrees(self, n):
        if n == 0:
            return [None]
        tree_list = [[[None]] * (n + 2) for i in range(n + 2)]
        for i in range(1, n + 1):
            tree_list[i][i] = [TreeNode(i)]
            for j in reversed(range(1, i)):
                tree_list[j][i] = []
                for k in range(j, i + 1):
                    for left in tree_list[j][k - 1]:
                        for right in tree_list[k + 1][i]:
                            root = TreeNode(k)
                            (root.left, root.right) = (left, right)
                            tree_list[j][i].append(root)
        return tree_list[1][n]