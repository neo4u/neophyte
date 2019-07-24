# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if not root: return []
        used, leaves = set(), []
        lb = self.get_left_boundary(root, used)
        self.get_leaves(root, used, leaves)
        rb = self.get_right_boundary(root, used)
        return lb + leaves + rb

    def get_leaves(self, root, used, leaves):
        if not root or root in used: return
        if not root.left and not root.right: return leaves.append(root)

        self.get_leaves(root.left, used, leaves)
        self.get_leaves(root.right, used, leaves)

    def get_left_boundary(self, root, used):
        path = []

        while root:
            path.append(root.val)
            used.add(root)
            root = root.left

        return path

    def get_right_boundary(self, root, used):
        path = []

        while root:
            if root not in used:
                path.append(root.val)
                used.add(root)

            if root.right:
                root = root.right
            else:
                root = root.left

        return path[::-1]
