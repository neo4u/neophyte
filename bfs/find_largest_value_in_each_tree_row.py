from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root: return []
        q, level_map, level = [root], {}, 0

        while q:
            level_q = []
            for node in q:
                if level not in level_map:
                    level_map[level] = node.val
                else:
                    level_map[level] = max(level_map[level], node.val)

                if node.left: level_q.append(node.left)
                if node.right: level_q.append(node.right)

            q = level_q
            level += 1

        return [level_map[i] for i in range(level)]

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root: return []

        result = []
        q = [root]
        while q:
            result.append(max(q, key=lambda x: x.val).val)

            level_q = []
            for node in q:
                if node.left: level_q.append(node.left)
                if node.right: level_q.append(node.right)
            q = level_q

        return result
