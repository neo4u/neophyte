# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import sys
import collections

class Codec:

    def serialize(self, root):
        """
        Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def dfs(root, res):
            if not root: return
            res.append(str(root.val))
            dfs(root.left, res)
            dfs(root.right, res)

        res = []
        dfs(root, res)
        return ','.join(res)

    def deserialize(self, data):
        """
        Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def dfs(data, vmin, vmax):
            if not data: return None
            val = int(data[0])
            if val < vmin or val > vmax: return None
            data.popleft()
            node = TreeNode(val)
            node.left = dfs(data, vmin, val)
            node.right = dfs(data, val, vmax)
            return node

        if not data: return None
        vmin, vmax = -sys.maxint-1, sys.maxint
        nodes = collections.deque(data.split(','))
        return dfs(nodes, vmin, vmax)


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
