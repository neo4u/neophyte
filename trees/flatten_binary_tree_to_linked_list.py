# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def flatten(self, root: TreeNode) -> None:
        if not root: return None

        tmp_l, tmp_r = root.left, root.right
        self.flatten(root.left)
        self.flatten(root.right)

        if not tmp_l: return

        root.right = tmp_l
        root.left = None

        while tmp_l.right: tmp_l = tmp_l.right
        tmp_l.right = tmp_r


# 114. Flatten Binary Tree to Linked List
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/


#     1
#    / \
#   2   5
#  / \   \
# 3   4   6

#      1
#     / \
#    2   5
#   / \   \
#  3   4   6
#       \
#         5
#          \
#           6

#      1
#     / \
#   nil  2
#       / \ 
#      3   4 
#           \
#             5
#              \
#               6

#   2
#  / \
# 3   4
#  \   \
#   4   5
#    \   \
#     5    6
#      \
#       6

#   2
#  / \
# nil  3
#       \
#        4
#         \
#          5
#           \
#            6

# 3
#  \
#   4
#    \
#     5
#      \
#       6

# 114. Flatten Binary Tree to Linked List
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/


# Key Insights:
# 1. If there is no left-subtree, we don't need to cut off the link between rootand root.right
#    to fit flattened left subtree in between.
# 2. Other wise do exactly what the question says word to word

# Approach 1: Recursive
# Steps:
# 0. Base case is to return if you hit a None node
# 1. Flatten right sub-tree, store it in tmp
# 2. At this point we can return if there is no left sub-tree, if there is the go to 3
# 3. Flatten left sub-tree, store it in tail
# 4. Move to tail onto the tail of the left sub-tree. Since its been flattened, it only has right children
# 5. Attach the left sub-tree to the right of root
# 6. Attach the right sub-tree (tmp) to the right tail of left-subtree

# Time: O(n)
# Space: O(n)

# Approach 2: Iterative

# Steps:


# Time: O(n)
# Space: O(1)
