# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def dfs(root, ans):
            if root is None:
                ans.append("#")
                return
            ans.append(str(root.val))
            dfs(root.left, ans)
            dfs(root.right, ans)

        ans = []
        dfs(root, ans)
        astr = ",".join(ans)
        return astr

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def dfs(data, index):
            if index[0] >= len(data):
                return None
            val = data[index[0]]
            if val == '#':
                return None
            root = TreeNode(val)
            index[0] += 1
            root.left = dfs(data, index)
            index[0] += 1
            root.right = dfs(data, index)
            return root

        if not data:
            return None
        data = data.split(",")
        index = [0]
        return dfs(data, index)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

# Complexity Analysis
# Time complexity: in both serialization and deserialization functions,
#                  we visit each node exactly once, thus the time complexity is O(N),
#                  where N is the number of nodes, i.e. the size of tree.
# Space complexity: in both serialization and deserialization functions,
#                   we keep the entire tree, either at the beginning or at the end,
#                   therefore, the space complexity is O(N).

# Time: O(n)
# Space: O(n)
