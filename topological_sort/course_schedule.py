import collections
from typing import List


# Topological sort BFS
class Solution:
    def canFinish(self, numCourses: int, prereqs: List[List[int]]) -> bool:
        graph = collections.defaultdict(set)
        in_degrees = collections.defaultdict(int)

        for course, prereq in prereqs:
            graph[prereq].add(course)
            in_degrees[course] += 1

        q = []
        for node in range(numCourses):
            if in_degrees[node] != 0: continue
            q.append(node)
            numCourses -= 1

        while q:
            node = q.pop(0)

            for nbr in graph[node]:
                in_degrees[nbr] -= 1
                if in_degrees[nbr] == 0:
                    q.append(nbr)
                    numCourses -= 1

        return numCourses == 0


# 207. Course Schedule
# https://leetcode.com/problems/course-schedule/description/

# Key Insight:
# 1. It comes down to a problem of detecting a cycle in a graph (Checking if its a DAG)
# 2. We need some sort of ordering of courses hence topological sort makes sense

# Approach 1: DFS with keeping track of on_stack nodes (VERY SLOW)
# Steps:
# 1. Iterate through prereqs adding each preerq as a directed edge in dictionary graph
#    which is a map from nodes (interger) to list of nodes (array of ints)
# 2. Now iterate through courses and do a DFS for each course
# 3. If DFS returns false for any course we return false, else we return true,
#    return false means a praticular course didn't have the prerequirements met
# 4. In dfs method we traverse the nbs and their nbs and so on for all nbs of the given node
# 5. In doing so, we keep track of the currently on stack nodes or visiting nodes if you will using on_stack.
#    The purpose of on_stack is to see if any of the courses have a circular dependency
#    or in other words if our graph has a cycle.
#    Example: 1 -> 2 -> 3 -> 4 -> 1, 1 -> 2 -> 3 -> 4 -> 2 or 1 -> 2 -> 3 -> 4 -> 3
#    Such a combo of prerequirements cannot be met due to the cycle

# Time: O(N), Essentially, O(V + E), V - number of courses, E - number of prereqs => O(V + V - 1) => O(N)
# Space: O(N)

# Approach 2: BFS with using Kahn's algorithm (in-degree) (VERY FAST For leetcode inputs)
# Steps:
# 1. Iterate through prereqs adding each preerq as a directed edge in graph
#    which is a map from nodes (interger) to list of nodes (array on ints)
# 2. Iterate through the courses and get the indegrees of each of the vertices
# 3. We perform a BFS with a tweak that only nodes with an in-degree of 0
#    are added to the q (Kahn's Topological Sort Algorithm)
# 4. For each visited node we reduce the in-degree of the node by 1, before
#    adding 0 in-degree nbs to the queue
# 5. We add nodes to visited from the front and finally return true
#    if this list has the same size as the number of courses.

# Time: O(N), Essentially, O(V + E), V - number of courses, E - number of prereqs => O(V + V - 1) => O(N)
# Space: O(N)


# The topological sort is natural for this problem.
# We always take the courses with no unstudied prereqs and so on until we can't take anymore courses.
# The oud[i] is the number of prereqs for course i
# and indegree keeps a list of courses that require course i.


sol = Solution()
assert sol.canFinish(2, [[1,0]] ) == True
assert sol.canFinish(2, [[1,0],[0,1]]) == False
assert sol.canFinish(5, [[0, 4], [4,3],[3,2], [2, 1], [1, 4]]) == False

# sol2 = Solution2()
# assert sol2.canFinish(2, [[1,0]] ) == True
# assert sol2.canFinish(2, [[1,0],[0,1]]) == False
# assert sol2.canFinish(5, [[0, 4], [4,3],[3,2], [2, 1], [1, 4]]) == False
