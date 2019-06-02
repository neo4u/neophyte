import collections

class Solution:
    def canFinish(self, numCourses: int, prereqs: List[List[int]]) -> bool:
        self.graph = collections.defaultdict(set)
        self.in_degrees = collections.defaultdict(int)

        for course, prereq in prereqs:
            self.graph[prereq].add(course)
            self.in_degrees[course] += 1

        q, visited = [], set()
        for node in range(numCourses):
            if self.in_degrees[node] != 0: continue
            q.append(node)
            visited.add(node)

        while q:
            node = q.pop(0)

            for nbr in self.graph[node]:
                if nbr in visited: continue
                self.in_degrees[nbr] -= 1
                if self.in_degrees[nbr] == 0:
                    q.append(nbr)
                    visited.add(nbr)

        return numCourses == len(visited)
