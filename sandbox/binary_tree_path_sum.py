class Node:
    def __init__(self, value):
        self.val = value
        self.left, self.right = None, None

class Solution:
    def find_path_sum(self, root, target):
        return self.dfs(root, target)

    def dfs(self, node, rem):
        if not node: return rem == 0
        if rem < 0: return False

        return self.dfs(node.left, rem - node.val) or self.dfs(node.right, rem - node.val)

root = Node(50)
l, r = Node(17), Node(76)
l1, l2, r1 = Node(9), Node(23), Node(54)

root.left, root.right = l, r
root.left.left, root.left.right = l1, l2
root.right.left = r1

sol = Solution()
assert sol.find_path_sum(root, 180) == True
