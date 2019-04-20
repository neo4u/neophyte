class Solution(object):
    def hasPath(self, maze, start, destination):
        return self.helper(maze, destination, start[0], start[1])
        
    
    def helper(self, maze, dest, i, j):
        if [i, j] == dest:
            return True
        if maze[i][j] == 2:
            return False
        up, down, left, right = i, i, j, j
        while up > 0 and maze[up-1][j] != 1:
            up -= 1
        while down < len(maze)-1 and maze[down+1][j] != 1:
            down += 1
        while left > 0 and maze[i][left-1] != 1:
            left -= 1
        while right < len(maze[0])-1 and maze[i][right+1] != 1:
            right += 1
        maze[i][j] = 2
        return self.helper(maze, dest, up, j) or self.helper(maze, dest, down, j) or self.helper(maze, dest, i, left) or self.helper(maze, dest, i, right)


# More Elegant
class Solution2:
    def hasPath(self, maze, start, destination):
        m, n = len(maze), len(maze[0])
        def dfs(x, y, stopped):
            if (x, y) in stopped: return False
            stopped.add((x, y))
            if [x, y] == destination:
                return True
            for i, j in ((-1, 0) , (1, 0), (0, -1), (0, 1)):
                newX, newY = x, y
                while 0 <= newX + i < m and 0 <= newY + j < n and maze[newX + i][newY + j] != 1:
                    newX += i
                    newY += j
                if dfs(newX, newY, stopped):
                    return True
            return False
        return dfs(start[0], start[1], set())