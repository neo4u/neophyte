class Solution:
    def hasPath(self, maze, start, destination):
        m, n = len(maze), len(maze[0])
        def dfs(i, j, stopped):
            if (x, y) in stopped: return False
            stopped.add((x, y))
            if [i, j] == destination:
                return True
            for x, y in ((-1, 0) , (1, 0), (0, -1), (0, 1)):
                r, c = i, j
                while 0 <= r + i < m and 0 <= c + j < n and maze[r + x][c + y] != 1:
                    r += x
                    c += y
                if dfs(r, c, stopped):
                    return True
            return False
        return dfs(start[0], start[1], set())


class Solution:
    def hasPath(self, maze, start, destination):
            Q, n, m = [start], len(maze), len(maze[0])
            dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))

            while Q:
                # Use Q.pop() as DFS or Q.popleft() with deque from collections library for better performance. Kudos to @whglamrock
                i, j = Q.pop(0)

                # Mark as visited
                maze[i][j] = 2
                if i == destination[0] and j == destination[1]: return True

                for x, y in dirs:
                    row = i + x
                    col = j + y

                    # You can only change direction if you hit a wall
                    # Walk all the way down until the walker hit a wall
                    while 0 <= row < n and 0 <= col < m and maze[row][col] != 1:
                        row += x
                        col += y

                    # Retract from the wall
                    row -= x
                    col -= y

                    if maze[row][col] == 0:
                        Q.append([row, col])

            return False