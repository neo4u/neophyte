# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        self.max_len = 0
        self.dfs(root, root)
        return self.max_len

    def dfs(self, node, parent):
        if not node: return 0, 0

        li, ld = self.dfs(node.left, node)
        ri, rd = self.dfs(node.right, node)
        self.max_len = max(self.max_len, li + rd + 1, ld + ri + 1)

        if node.val == parent.val + 1: return max(li, ri) + 1, 0
        if node.val == parent.val - 1: return 0, max(ld, rd) + 1

        return 0, 0


# 549. Binary Tree Longest Consecutive Sequence II
# https://leetcode.com/problems/binary-tree-longest-consecutive-sequence-ii/description/

#      8
#    7   9
#   6      0
#  5         0



# Pattern from other tree problems
# https://leetcode.com/problems/binary-tree-longest-consecutive-sequence-ii/discuss/389210/Python-bottom-up-DFS-solution-(56-ms-beat-93.37)





# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        self.max_len = 0
        self.dfs(root)
        return self.max_len - 1

    def dfs(self, node):
        if not node: return 0

        l = self.dfs(node.left)
        r = self.dfs(node.right)

        if node.left:
            if abs(node.left.val - node.val) != 1:
                l = 0
            else:
                l += 1

        if node.right:
            if abs(node.right.val - node.val) != 1:
                r = 0
            else:
                r += 1

        length = max(l, r)
        self.max_len = max(self.max_len, length, l + r + 1)
        return length


