# I found many Python users encounter max-recursion depth problem,
# the critical part is:

# DFS/BFS only the "O" on the wall, instead of DFS from a inner "O" and check whether it hits the wall.

# I brought the idea from StefanPochmann's post, and rewrite it as a "not so concise version" code as below:
class Solution:
    def solve(self, board):
        if not board:
            return
        m, n = len(board), len(board[0])
        leakWall = self.buildLeakWall(board)
        while leakWall:
            i, j = leakWall.pop()
            if 0 <= i < m and 0 <= j < n:
                if board[i][j] == "O":
                    board[i][j] = "S"
                    leakWall += (i-1, j), (i+1, j), (i, j-1), (i, j+1)
        for i in range(m):
            for j in range(n):
                board[i][j] = "O" if board[i][j] == "S" else "X"

    def buildLeakWall(self, board):
        leakWall, m, n = [], len(board), len(board[0])
        for i in range(m):
            if board[i][0] == "O":
                leakWall.append((i, 0))
            if board[i][n-1] == "O":
                leakWall.append((i, n-1))
        for j in range(n):
            if board[0][j] == "O":
                leakWall.append((0, j))
            if board[m-1][j] == "O":
                leakWall.append((m-1, j))
        return leakWall


# In the original post, @StefanPochmann use some tricks to build the wall concisely, and simply filter out the illegal wall when checking.
# Recommend everyone to check it out!

# And a minor reminder:
# The input is like [["X","X","X","X"], ["X","O","O","X"], ["X","X","O","X"], ["X","O","X","X"]]
# NOT ["XXXX", "XOOX", "XXOX", "XOXX"] as the OJ error message shows!
class Solution2:

    def solve(self, board):
        if len(board) == 0:
            return
        height = len(board)
        width = len(board[0])
        def dfs(board, y, x):
            if x < 0 or x >= width or y < 0 or y >= height or board[y][x] != 'O':
                return 
            board[y][x] = 'S'
            dfs(board, y + 1, x)
            dfs(board, y - 1, x)
            dfs(board, y, x + 1)
            dfs(board, y, x - 1)
        for i in range(width):
            if board[0][i] == 'O':
                dfs(board, 0, i)
            if board[height-1][i] == 'O':
                dfs(board, height-1, i)
        for j in range(height):
            if board[j][0] == 'O':
                dfs(board, j, 0)
            if board[j][width-1] == 'O':
                dfs(board, j, width-1)
        for y in range(height):
            for x in range(width):
                if board[y][x] == 'S':
                    board[y][x] = 'O'
                else:
                    board[y][x] = 'X'
