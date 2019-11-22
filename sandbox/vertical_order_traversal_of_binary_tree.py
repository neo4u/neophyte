from typing import List
import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if not root: return []

        levels_map, q = collections.defaultdict(list), [(root, 0, 0)]
        min_l, max_l = 0, 0
        result = []

        while q:
            node, x, y = q.pop(0)
            levels_map[x].append((y, -node.val))  # We use for sorting same position values using reverse, 

            if x < min_l: min_l = x
            if x > max_l: max_l = x

            if node.left: q.append((node.left, x - 1, y - 1))
            if node.right: q.append((node.right, x + 1, y - 1))

        for level in range(min_l, max_l + 1):
            level_values = [-item[1] for item in sorted(levels_map[level], reverse=True)]
            result.append(level_values)

        return result


# 987. Vertical Order Traversal of a Binary Tree
# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/


# Difference from vertical order traversal:
# 314. If two nodes are in the same row and column, the order should be from left to right.
# 987. If two nodes have the same position (x, y), then the value of the node that is reported first is the value that is smaller.

# Approach 1: BFS
# Steps:
# 1. We'll use the same method as vertical order traversal
# 2. But we'll use these key differences:
# 3. We'll use level_map dict to store all the elements on one level of x co-ordinates
#    i.e. level_map[x] will store elements that have the same x co-ords
#    we'll use level_map[x] to store (y, -value), we store -value cuz,
#    we want values that have same y co-ords to cause the small values before the larger values of value
#    Hence, we'll get something like [(2, -1), (1, -2), (1, -3), (0, -4)], cuz're we're using reverse=True in sort
#    which will be made -ve so we'll end up getting [1,2,3,4]
# 4. Once we've populated level_map using BFS starting from (root, 0, 0), and getting min_level and max_level,
#    we iterate through the levels between min_l and max_l and get the values by sorting the tuples in reverse,
#    thus we get high y co-ords first and then get higher negative values like so: [(2, -1), (1, -2), (1, -3), (0, -4)]
#    then we take the -ve of 1th index of each tuple, to get something like so: [1, 2, 3, 4] for each x
