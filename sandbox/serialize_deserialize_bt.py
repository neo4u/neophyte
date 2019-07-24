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




# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))