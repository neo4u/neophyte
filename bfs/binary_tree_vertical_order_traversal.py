from typing import List
import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        q, level_map = [(root, 0)], collections.defaultdict(list)
        min_l, max_l = 0, 0

        while q:
            node, level = q.pop(0)
            level_map[level].append(node.val)

            if level < min_l: min_l = level
            if level > max_l: max_l = level

            if node.left: q.append((node.left, level - 1))
            if node.right: q.append((node.right, level + 1))

        return list(map(lambda x: level_map[x], range(min_l, max_l + 1)))


# 314. Binary Tree Vertical Order Traversal
# https://leetcode.com/problems/binary-tree-vertical-order-traversal/


# Approach 1: BFS
# Look at the diagram with same file name for better intuition
# 1. Visit each node in a BFS fashion
# 2. Append left sub-tree to 1 level before (level - 1)
# 3. Append right sub-tree to 1 level after (level + 1)
# 4. Collect nodes at each level and return them in an array

# where h is height of the tree, n is number of nodes in tree
# Time: O(nlog(h))
# Space: O(h)

# Example and Test
# Input: [3,9,20,null,null,15,7]

#    3
#   /\
#  /  \
#  9  20
#     /\
#    /  \
#   15   7

n1 = TreeNode(3)
n2l = TreeNode(9)
n2r = TreeNode(20)

n3r1 = TreeNode(15)
n3r2 = TreeNode(7)

n1.left, n1.right = n2l, n2r
n2r.left, n2r.right = n3r1, n3r2
output = [[9], [3, 15], [20], [7]]

sol = Solution()
assert sol.verticalOrder(n1) == output
