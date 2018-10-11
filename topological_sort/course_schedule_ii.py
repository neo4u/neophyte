class Solution:
    def findOrder(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        # construct graph
        graph = {i: set() for i in range(n)}
        in_degrees = {i: 0 for i in range(n)}

        for edge in edges:
            graph[edge[0]].add(edge[1])
            in_degrees[edge[1]] += 1

        # init var
        q = collections.deque()
        visited = []

        # find nodes whose in degree == 0
        for index, in_degree in in_degrees.items():
            if in_degree == 0:
                q.append(index)

        # loop all nodes whose in degree == 0
        while q:
            index = q.popleft()
            visited.append(index)
            for g in graph[index]:
                in_degrees[g] -= 1
                if in_degrees[g] == 0:
                    q.append(g)

        return visited[::-1] if len(visited) == n else []

# The code is almost the same as "course schedule". The only difference is we keep the courses taken instead of remove them, everything else is the same.
import collections
