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
        return ','.join(self.pre_order)

    def dfs_serialize(self, node):
        if not node: return

        self.pre_order.append(str(node.val))
        self.dfs_serialize(node.left)
        self.dfs_serialize(node.right)

    def deserialize(self, data):
        if not data: return

        pre_order = data.split(',')
        return self.dfs_deserialize(pre_order)

    def dfs_deserialize(self, pre_order, vmin=float('-inf'), vmax=float('inf')):
        if not pre_order: return
        val = int(pre_order[0])
        if not vmin <= val <= vmax: return
        pre_order.pop(0)

        root = TreeNode(val)
        root.left = self.dfs_deserialize(pre_order, vmin, val - 1)
        root.right = self.dfs_deserialize(pre_order, val + 1, vmax)
        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

# 449. Serialize and Deserialize BST
# https://leetcode.com/problems/serialize-and-deserialize-bst/

# Complexity Analysis
# Time complexity: in both serialization and deserialization functions,
#                  we visit each node exactly once, thus the time complexity is O(N),
#                  where N is the number of nodes, i.e. the size of tree.
# Space complexity: in both serialization and deserialization functions,
#                   we keep the entire tree, either at the beginning or at the end,
#                   therefore, the space complexity is O(N).

# Time: O(n)
# Space: O(n)

# Diff from #297.
# Like others have noted, the primary difference in the problem statement is:
# the encoded string needs to be as compact as possible.

# One of the ways a BST tree is different from a general binary tree is:
# its structure is wholly dependent on the order in which the values are inserted.
# A string created from a preorder traversal of a BST will tell you the order in which
# the values were inserted into the tree. Since you just need the order the values were inserted,
# you do not need to account for null nodes in the string with "#" or "null".
# Hence, the final string contains only the values and separators, which makes it the most compact possible.

sol = Codec()
print(sol.serialize(None))
