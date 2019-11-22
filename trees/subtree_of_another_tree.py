# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Approach 1: DFS (Starting from every node)
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and not t: return True
        if not s or not t: return False

        # we have O(|t|) for is_same, and then for O(|t|) each for each is_subtree method total of O(|s| * 3|t|) == O(|s| * |t|)
        return self.is_same(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def is_same(self, s, t): # This takes O(t)
        if not s and not t: return True
        if not s or not t: return False

        return s.val == t.val and self.is_same(s.left, t.left) and self.is_same(s.right, t.right)


# Approach 2: Preorder traversal serialization
class Solution1:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and not t: return True
        if not t: return True
        if not s: return False

        self.pre_order_s, self.pre_order_t = [], []
        self.dfs_serialize(s, self.pre_order_s)
        self.dfs_serialize(t, self.pre_order_t)

        s_serial, t_serial = ",".join(self.pre_order_s), ",".join(self.pre_order_t)
        return t_serial in s_serial # String containment can be done in O(n) using Rabin Karp method

    def dfs_serialize(self, node, pre_order):
        if not node: return pre_order.append('#')

        pre_order.append('$' + str(node.val))
        self.dfs_serialize(node.left, pre_order)
        self.dfs_serialize(node.right, pre_order)


# Approach 3: Merkel Hashing
from hashlib import sha256
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        self.merkle(s); self.merkle(t)
        return self.dfs(s, t)

    def merkle(self, node):
        if not node: return ''

        ml, mr = self.merkle(node.left), self.merkle(node.right)
        node._merkle = self._hash(ml + str(node.val) + mr)
        return node._merkle

    def dfs(self, node, t):
        if not node and not t: return True  # Both are None
        if not t: return True               # the tree we're checking for has exhausted a path
        if not node: return False           # the tree we're checking in has exhausted a path

        # Check the merkle at the node as root, if they match then they're same tree, else check in l or r
        return node._merkle == t._merkle or self.dfs(node.left, t) or self.dfs(node.right, t)

    def _hash(self, x):
        mac = sha256()
        mac.update(x.encode('utf8'))
        return mac.hexdigest()



# 572. Subtree of Another Tree
# https://leetcode.com/problems/subtree-of-another-tree/description/


# Approach 1: DFS (Starting from every node)
# Time: O(|s| * |t|)
# Space: O()

# Approach 2: Preorder traversal serialization
# Time: O(|s| * |t|)
# Space: O(log(s))

# Approach 3: Merkel Hashing
# Time: O(|s| + |t|)
# Space: O(log(s))
