import collections

class Solution:
    def findOrder(self, n, edges):
        # construct graph
        graph = collections.defaultdict(set)
        in_degrees = collections.defaultdict(int)

        for course, prereq in edges:
            graph[prereq].add(course)
            in_degrees[course] += 1

        q, visited = [], []
        for node in range(n):
            if in_degrees[node] != 0: continue
            q.append(node)
            visited.append(node)

        while q:
            node = q.pop(0)

            for nbr in graph[node]:
                in_degrees[nbr] -= 1
                if in_degrees[nbr] == 0:
                    q.append(nbr)
                    visited.append(nbr)

        return visited if len(visited) == n else []
