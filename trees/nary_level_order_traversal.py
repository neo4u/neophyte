# Recursion is easy to implement and understand by definition
# https://en.wikipedia.org/wiki/Tree_traversal#Post-order_(LRN).


# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        def dfs(root, res):
            for child in root.children:
                dfs(child, res)
            res.append(root.val)
            return res

        if root == None: return []
        return dfs(root, [])


# Iteration is basically pre-order traversal but rather than go left,
# go right first then reverse its result.
class Solution(object):
    def postorder(self, root):
            res = []
            if root == None: return res

            stack = [root]
            while stack:
                curr = stack.pop()
                res.append(curr.val)
                stack.extend(curr.children)

            return res[::-1]