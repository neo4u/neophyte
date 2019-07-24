import collections

class Solution:
    def canFinish(self, numCourses: int, prereqs: List[List[int]]) -> bool:
        self.graph = collections.defaultdict(set)
        self.in_degrees = collections.defaultdict(int)

        for course, prereq in prereqs:
            self.graph[prereq].add(course)
            self.in_degrees[course] += 1

        q = []
        for node in range(numCourses):
            if self.in_degrees[node] != 0: continue
            q.append(node)
            numCourses -= 1

        while q:
            node = q.pop(0)

            for nbr in self.graph[node]:
                self.in_degrees[nbr] -= 1
                if self.in_degrees[nbr] == 0:
                    q.append(nbr)
                    numCourses -= 1

        return numCourses == 0
