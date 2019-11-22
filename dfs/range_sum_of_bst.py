# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root: return 0

        r_sum, r_val = 0, root.val
        if L < r_val: r_sum += self.rangeSumBST(root.left, L, R)
        if r_val < R: r_sum += self.rangeSumBST(root.right, L, R)
        if L <= r_val <= R: r_sum += r_val

        return r_sum


class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root: return 0

        r_sum, r_val = 0, root.val
        if L < r_val: r_sum += self.rangeSumBST(root.left, L, min(r_val - 1, R))
        if r_val < R: r_sum += self.rangeSumBST(root.right, max(r_val + 1, L), R)
        if L <= r_val <= R: r_sum += r_val

        return r_sum


# 938. Range Sum of BST
# https://leetcode.com/problems/range-sum-of-bst/description/


      4
   2      6
 1   3  5   7

 [15,9,21,7,13,19,23,5,null,11,null,17]
19
21