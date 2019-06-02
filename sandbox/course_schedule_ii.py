import collections

class Solution:
    def findOrder(self, numCourses: int, prereqs: List[List[int]]) -> List[int]:
        self.graph = collections.defaultdict(set)
        self.in_degrees = collections.defaultdict(int)

        for course, prereq in prereqs:
            self.graph[prereq].add(course)
            self.in_degrees[course] += 1

        q, visited, path = [], set(), []
        for node in range(numCourses):
            if self.in_degrees[node] != 0: continue
            q.append(node)
            visited.add(node)
            path.append(node)

        while q:
            node = q.pop(0)

            for nbr in self.graph[node]:
                if nbr in visited: continue
                self.in_degrees[nbr] -= 1
                if self.in_degrees[nbr] == 0:
                    q.append(nbr)
                    visited.add(nbr)
                    path.append(nbr)

        return path if len(path) == numCourses else []
