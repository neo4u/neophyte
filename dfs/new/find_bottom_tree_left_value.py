# DFS + stack
class Solution:
    def findBottomLeftValue(self, root):
        if not root:
            return
        max_depth = 0
        stack = [(root, 1)]

        while stack:
            curr, level = stack.pop()
            if curr:
                if level > max_depth:
                    max_depth = level
                    ans = curr.val
                stack.append((curr.right, level + 1))
                stack.append((curr.left, level + 1))
        return ans

class Solution_recursive:
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root, d):
            if root is None:
                return (0, None)
            if not root.left and not root.right:
                return (d, root.val)

            left = dfs(root.left, d + 1)
            right = dfs(root.right, d + 1)

            return left if left[0] >= right[0] else right

        return dfs(root, 0)[1]
