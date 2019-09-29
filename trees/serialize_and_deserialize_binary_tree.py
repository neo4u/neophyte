# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        self.pre_order = []
        self.dfs_serialize(root)
        return ",".join(self.pre_order)

    def dfs_serialize(self, node):
        if not node: return self.pre_order.append('#')

        self.pre_order.append(str(node.val))
        self.dfs_serialize(node.left)
        self.dfs_serialize(node.right)

    def deserialize(self, data):
        if not data: return None

        pre_order = data.split(',')
        return self.dfs_deserialize(pre_order)

    def dfs_deserialize(self, pre_order):
        if not pre_order: return None

        if pre_order[0] == '#':
            pre_order.pop(0)
            return None

        root = TreeNode(int(pre_order.pop(0)))
        root.left = self.dfs_deserialize(pre_order)
        root.right = self.dfs_deserialize(pre_order)

        return root

# Approach 2: BFS pre-order / Iterative approach (Seems faster on LC inputs)
import collections
class Codec:
    def serialize(self, root):
        if not root: return []
        result = []
        que = collections.deque([root])
        while que:
            node = que.popleft()
            if not node:
                result.append('#')
                continue
            else:
                result.append(str(node.val))
            que.extend([node.left, node.right])
        return ' '.join(result)

    def deserialize(self, data):
        if not data: return None
        iterData = iter(data.split(' '))
        root = TreeNode(next(iterData))
        que = collections.deque([root])
        while que:
            node = que.popleft()
            if not node: continue
            val = next(iterData)
            node.left = TreeNode(int(val)) if val != '#' else None
            que.append(node.left)
            val = next(iterData)
            node.right = TreeNode(int(val)) if val != '#' else None
            que.append(node.right)
        return root


# 297. Serialize and Deserialize Binary Tree
# https://leetcode.com/problems/serialize-and-deserialize-bst/description/

# Approach 1: DFS using pre-order
# Steps:
# 1. Serialize using pre-order traversal using depth first search and represent null by "#"
# 2. Deserialize by traversing the serialized tree and using recursion. O(n).

# Approach 2: BFS using queue and iterative approach and pre_order
# Time: O(n), visit n nodes once
# Space: O(n), store the entire tree in array and string

#     1
#    / \
#   2   3
#      / \
#     4   5

root = TreeNode(1)
l, r = TreeNode(2), TreeNode(3)
r1, r2 = TreeNode(4), TreeNode(5)
root.left, root.right = l, r
r.left, r.right = r1, r2

codec = Codec()
assert codec.serialize(root) == "1,2,#,#,3,4,#,#,5,#,#"
new_root = codec.deserialize("1,2,#,#,3,4,#,#,5,#,#")

assert new_root.val == root.val
assert new_root.left.val == l.val
assert new_root.right.val == r.val
assert new_root.right.left.val == r1.val
assert new_root.right.right.val == r2.val
