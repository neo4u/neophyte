import collections


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if not root: return []

        levels_map, q = collections.defaultdict(list), [(root, 0, 0)]
        min_level, max_level = 0, 0
        result = []

        while q:
            node, x, y = q.pop(0)
            levels_map[x].append((y, -node.val))  # for sorting same position values using reverse, 

            if x < min_level: min_level = x
            if x > max_level: max_level = x

            if node.left: q.append((node.left, x - 1, y - 1))
            if node.right: q.append((node.right, x + 1, y - 1))

        for level in range(min_level, max_level + 1):
            level_values = [-item[1] for item in sorted(levels_map[level], reverse=True)]
            result.append(level_values)

        return result


# Difference:
# 314. If two nodes are in the same row and column, the order should be from left to right.
# 987. If two nodes have the same position (x, y), then the value of the node that is reported first is the value that is smaller.

# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
# 987. Vertical Order Traversal of a Binary Tree
