from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root: return []
        q, result = [root], []

        while q:
            n, level_right_node = len(q), None

            for _ in range(n):
                node = q.pop(0)
                level_right_node = node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)

            result.append(level_right_node)

        return result


class Solution2:
    def leftSideView(self, root: TreeNode) -> List[int]:
        if not root: return []
        q, result = [root], []

        while q:
            n, level_left_node = len(q), None

            for _ in range(n):
                node = q.pop(0)
                if not level_left_node: level_left_node = node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)

            result.append(level_left_node)

        return result


# 199. Binary Tree Right Side View
# https://leetcode.com/problems/binary-tree-right-side-view/description/

# Intuition
# 1. At every level we will only be able to see the right most node
# 2. Hence this is same as level order traversal when we only store the right most node
# 3. For level order traversal BFS is an obvious choice

# Approach 2: BFS, Store only right most per level
# Steps:
# 1. We use a q and enqueue the root into it to start off the algorithm
# 2. While we have elements in the q, we keep a number 'n' of elements to process at this level,
#    and we keep 'level_right_node' to keep track of the right most node processed so far
# 3. We loop through n times, popping elements from the q,
#    updating the level_right_node for each node processed at that level from left to right
# 4. We also enqueue left and right, children to the queue to be processed as part of next batch or level
