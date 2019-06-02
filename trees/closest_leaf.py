class Solution(object):
    def findClosestLeaf(self, root, k):
        annotation = {}
        def closest_leaf(root):
            if root not in annotation:
                if not root:
                    ans = float('inf'), None
                elif not root.left and not root.right:
                    ans = 0, root
                else:
                    d1, leaf1 = closest_leaf(root.left)
                    d2, leaf2 = closest_leaf(root.right)
                    ans = min(d1, d2) + 1, leaf1 if d1 < d2 else leaf2
                annotation[root] = ans
            return annotation[root]

        #Search for node.val == k
        path = []
        def dfs(node):
            if not node:
                return
            if node.val == k:
                path.append(node)
                return True

            path.append(node)
            ans1 = dfs(node.left)
            if ans1: return True
            ans2 = dfs(node.right)
            if ans2: return True
            path.pop()

        dfs(root)
        dist, leaf = float('inf'), None
        for i, node in enumerate(path):
            d0, leaf0 = closest_leaf(node)
            d0 += len(path) - 1 - i
            if d0 < dist:
                dist = d0
                leaf = leaf0

        return leaf.val


class Solution(object):
    def findClosestLeaf(self, root, k):
        graph = collections.defaultdict(list)
        def dfs(node, par = None):
            if node:
                graph[node].append(par)
                graph[par].append(node)
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root)
        queue = collections.deque(node for node in graph if node and node.val == k)
        seen = set(queue)

        while queue:
            node = queue.popleft()
            if node:
                if len(graph[node]) == 1:
                    return node.val
                for nei in graph[node]:
                    if nei not in seen:
                        seen.add(nei)
                        queue.append(nei)