# BFS + queue
class Solution:
    def findBottomLeftValue(self, root):
        if not root:
            return

        max_depth = 0
        queue = [(root, 1)]

        while queue:
            curr, level = queue.pop(0)
            if curr:
                if level > max_depth:
                    max_depth = level
                    ans = curr.val
                queue.append((curr.left, level + 1))
                queue.append((curr.right, level + 1))
        return ans
