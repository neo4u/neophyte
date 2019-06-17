# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """
        Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        self.pre_order = []
        self.dfs_serialize(root)
        return ','.join(self.pre_order)

    def dfs_serialize(self, root):
        if not root: return

        self.pre_order.append(str(root.val))
        self.dfs_serialize(root.left)
        self.dfs_serialize(root.right)

    def deserialize(self, data):
        """
        Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data: return None
        pre_order = data.split(',')
        return self.dfs_deserialize(pre_order, -float('inf'), float('inf'))

    def dfs_deserialize(self, pre_order, vmin, vmax):
        if not pre_order: return None

        val = int(pre_order[0])
        if val < vmin or val > vmax: return None
        pre_order.pop(0)

        node = TreeNode(val)
        node.left = self.dfs_deserialize(pre_order, vmin, val)
        node.right = self.dfs_deserialize(pre_order, val, vmax)

        return node


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
