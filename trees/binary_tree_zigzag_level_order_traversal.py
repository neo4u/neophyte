from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        result, q, dir_flag = [], [root], 1

        while q:
            level_q = []
            temp_q = []
            for node in q:
                temp_q.append(node.val)
                if node.left:   level_q.append(node.left)
                if node.right:  level_q.append(node.right)

            result.append(temp_q[::dir_flag])
            q = level_q
            dir_flag *= -1

        return result


# 103. Binary Tree Zigzag Level Order Traversal
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

#         -> 1->
#     <- 2   <    3 <-
#  -> 4  > 5 >  6  >  7 ->
# <- 8 9 10 11 12 13 14 15 <-
#
# level % 2 = 0 - push to back of list
# level % 2 = 1 - push to front of list
