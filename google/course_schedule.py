# Topological sort BFS
class Solution:
    def canFinish(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        # construct graph
        graph = {i: set() for i in range(n)}
        in_degrees = {i:0 for i in range(n)}

        for edge in edges:
            graph[edge[0]].add(edge[1])
            in_degrees[edge[1]] += 1

        # init var
        q = collections.deque()
        visited = set()

        # find nodes whose in degree == 0
        for index, in_degree in in_degrees.items():
            if in_degree == 0:
                q.append(index)

        # loop all nodes whose in degree == 0
        while q:
            index = q.popleft()
            visited.add(index)
            for g in graph[index]:
                in_degrees[g] -= 1
                if in_degrees[g] == 0:
                    q.append(g)
        return len(visited) == n


# 34 / 34 test cases passed.
# Status: Accepted
# Runtime: 52 ms
# 99.68%

# The topological sort is natural for this problem.
# We always take the courses with no unstudied prereqs and so on until we can't take anymore courses.
# The oud[i] is the number of prereqs for course i
# and indegree keeps a list of courses that require course i.

# Topological sort DFS
from collections import defaultdict
import collections
#from set import Set
class Solution2:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {boolean}
    def canFinish(self, num_courses, prereq):
        if num_courses < 2:
            return True

        path = defaultdict(list)
        for c in prereq:
            path[c[0]].append(c[1])

        searched = set()
        for start in path.keys():
            if not self.dfs(path, set(), start, searched):
                 False
        return True

    def dfs(self, path, seen, curr, searched):
        if curr in searched:
            return True

        for x in path[curr]:
            if x in seen: return False

            seen.add(x)
            if not self.dfs(path, seen, x, searched):
                return False

            seen.remove(x)

        searched.add(curr)
        return True
