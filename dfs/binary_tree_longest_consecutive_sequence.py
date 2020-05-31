# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Iterative
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        if not root: return 0
        ret = 0
        stack = [(root, 1)]

        while stack:
            node, cnt = stack.pop()
            if node.left:
                stack.append((node.left, cnt+1 if node.left.val == node.val + 1 else 1))
            if node.right:
                stack.append((node.right, cnt+1 if node.right.val == node.val + 1 else 1))
            ret = max(ret, cnt)

        return ret



# Recursive
class Solution:
    def longestConsecutive(self, root, parent=None, length=0):
        if root is None: return length

        isConsecutive = parent is not None and root.val == parent + 1
        length = length + 1 if isConsecutive else 1
        return max(length,
                   self.longestConsecutive(root.left, root.val, length),
                   self.longestConsecutive(root.right, root.val, length))


# Bottom-Up
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        self.max_len = 0
        self.dfs(root)
        return self.max_len

    def dfs(self, node):
        if not node: return 0

        l = self.dfs(node.left) + 1
        r = self.dfs(node.right) + 1

        if node.left and node.left.val != node.val + 1: l = 1
        if node.right and node.right.val != node.val + 1: r = 1

        length = max(l, r)
        self.max_len = max(self.max_len, length)
        return length


# 298. Binary Tree Longest Consecutive Sequence
# https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/description/

# Assuming we're fine with changing the method signature
# (this is a valid submission at the time of writing).

# https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/discuss/389208/Python-bottom-up-DFS-solution
