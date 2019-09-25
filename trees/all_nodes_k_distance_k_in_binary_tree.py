# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = Non

# Approach 1: Convert Tree to Graph
import collections
class Solution:
    def distanceK(self, root: TreeNode, target: int, K: int) -> List[int]:
        self.graph = collections.defaultdict(list)
        self.dfs_convert(root, None)
        print(self.graph)
        return self.bfs(target, K)

    def dfs_convert(self, node, parent):
        if not node: return

        if parent:
            self.graph[node.val].append(parent.val)
            self.graph[parent.val].append(node.val)

        self.dfs_convert(node.left, node)
        self.dfs_convert(node.right, node)


    def bfs(self, target, K):
        q, dist, visited = [target.val], 0, set([target.val])

        while q:
            if dist == K: return q
            level_q = []
            for node in q:
                for nbr in self.graph[node]:
                    if nbr in visited: continue
                    level_q.append(nbr)
                    visited.add(nbr)
            q = level_q
            dist += 1

        return []

# Approach 2: Percolate the distance
class Solution(object):
    def distanceK(self, root, target, K):
        ans = []

        # Return distance from node to target if exists, else -1
        # Vertex distance: the # of vertices on the path from node to target
        def dfs(node):
            if not node: return -1
            elif node is target:
                subtree_add(node, 0)
                return 1
            else:
                L, R = dfs(node.left), dfs(node.right)
                if L != -1:
                    if L == K:
                        ans.append(node.val)
                        # return -1
                    subtree_add(node.right, L + 1)
                    return L + 1
                elif R != -1:
                    if R == K:
                        ans.append(node.val)
                        # return -1
                    subtree_add(node.left, R + 1)
                    return R + 1
                else:
                    return -1

        # Add all nodes 'K - dist' from the node to answer.
        def subtree_add(node, dist):
            if not node:    return
            elif dist == K: ans.append(node.val)
            else:
                subtree_add(node.left, dist + 1)
                subtree_add(node.right, dist + 1)

        dfs(root)
        return ans


# Approach 1: BFS


# Approach 2: DFS
