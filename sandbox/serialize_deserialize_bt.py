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
        return ",".join(self.pre_order)

    def dfs_serialize(self, node):
        if not node:
            self.pre_order.append("#")
            return

        self.pre_order.append(str(node.val))
        self.dfs_serialize(node.left)
        self.dfs_serialize(node.right)


    def deserialize(self, data):
        """
        Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == '#': return None
        pre_order = data.split(",")
        return self.dfs_deserialize(pre_order)


    def dfs_deserialize(self, pre_order):
        if not pre_order: return None
        val = pre_order.pop(0)
        if val == '#': return None

        root = TreeNode(int(val))
        root.left = self.dfs_deserialize(pre_order)
        root.right = self.dfs_deserialize(pre_order)

        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))