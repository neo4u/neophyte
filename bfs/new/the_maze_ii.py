from collections import heapq

class Solution:
    def shortestDistance(self, maze, start, destination):
        m, n, q, stopped = len(maze), len(maze[0]), [(0, start[0], start[1])], {(start[0], start[1]):0}
        while q:
            dist, x, y = heapq.heappop(q)
            if [x, y] == destination:
                return dist
            for i, j in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                newX, newY, d = x, y, 0
                while 0 <= newX + i < m and 0 <= newY + j < n and maze[newX + i][newY + j] != 1:
                    newX += i
                    newY += j
                    d += 1
                if (newX, newY) not in stopped or dist + d < stopped[(newX, newY)]:
                    stopped[(newX, newY)] = dist + d
                    heapq.heappush(q, (dist + d, newX, newY))
        return -1


# https://leetcode.com/problems/the-maze-ii/discuss/173441/Python-or-Comparing-BFS-and-Djikstra-solutions

# BFS Solution
# This question is similar to the regular BFS traversal in a grid, with the only exeception being that we cannot change direction until we hit the boundary/obstacle. This forces us to traverse along thr maze till one of the two conditions are met. The other catch is unlike regular BFS, where we are gaurenteed that we have the shortest distance the first time we reach our destination, is no longer true(as due to above condition, we are changing the fundamental assumption in BFS shortest paths that all edges are of equal distance, this is no longer true). Therefore, we have to exhaustively search all the paths.

# Time Complexity : My understanding is it is O(V+E) ~ O(mn + 4mn) ~ O(mn) (not 100% sure about this)

# Djikstra's shortest path
# The only problem with BFS shortest path above is we cannot stop the first time we reach our destination. This can be overcome by using Djikstra's shortest path where we use a prioririty queue instead of a regular queue.

from collections import deque
import heapq
class Solution2:
    def shortestDistance(self, maze, start, destination):
        [sx,sy] = start
        [ex,ey] = destination
        if not any(maze):
            return -1
        m,n = len(maze), len(maze[0])
        visited = {(sx,sy) : 0}
        q = deque([(0, sx, sy)])
        ## For Djikstra's method ==>
        ## q = [(0,sx, sy)]
        while q:
            (pd,px,py) = q.popleft()
            # For Djikstra's method ==>
        # (pd,px,py) = heapq.heappop(q)
            for dx,dy in [(0,1),(-1,0),(0,-1),(1,0)]:
                d,x,y=pd,px,py
                while 0<=x+dx<m and 0<=y+dy<n and maze[x+dx][y+dy] == 0:
                    x,y,d = x+dx, y+dy, d+1
                if (x,y) not in visited or visited[(x,y)] > d:
                    visited[(x,y)] = d
                    if (x,y) == (ex,ey):
                        continue
            # For Djikstra's method ==>
            # return d

                    q.append((d,x,y))
            # For Djikstra's method ==>
            # q = heapq.heappush(q, (0,sx, sy))

        return visited.get((ex,ey), -1)

