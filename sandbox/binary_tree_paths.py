class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        return self.dfs(root, [], [])

    def dfs(self, node, path, paths):
        if not node: return paths
        path = path + [str(node.val)]

        if not node.left and not node.right:
            paths.append("->".join(path))
            return paths
        else:
            self.dfs(node.left, path, paths)
            self.dfs(node.right, path, paths)

        return paths