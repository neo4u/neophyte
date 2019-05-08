# DFS
# def updateBoard(self, board, click):
#     (row, col), directions = click, ((-1, 0), (1, 0), (0, 1), (0, -1), (-1, 1), (-1, -1), (1, 1), (1, -1))
#     if 0 <= row < len(board) and 0 <= col < len(board[0]):
#         if board[row][col] == 'M':
#             board[row][col] = 'X'
#         elif board[row][col] == 'E':
#             mines = []
#             for r, c in directions:
#                 if 0 <= row + r < len(board) and 0 <= col + c < len(board[0]):
#                     mines.append(board[row + r][col + c] == 'M')
#             n = sum()
#             board[row][col] = str(n or 'B')
#             for r, c in directions * (not n): self.updateBoard(board, [row + r, col + c])

#     return board



class Solution(object):
    def updateBoard(self, board, click):
        if not board: return []

        m, n = len(board), len(board[0])
        i, j = click[0], click[1]

        # If a mine ('M') is revealed, then the game is over - change it to 'X'.
        if board[i][j] == 'M':
            board[i][j] = 'X'
            return board

        # run dfs to reveal the board
        self.dfs(board, i, j)
        return board

    def dfs(self, board, i, j):
        if board[i][j] != 'E': return

        m, n = len(board), len(board[0])
        directions = [(-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1), (-1,0)]

        mine_count = 0

        for d in directions:
            ni, nj = i + d[0], j + d[1]
            if 0 <= ni < m and 0 <= nj < n and board[ni][nj] == 'M':
                mine_count += 1

        if mine_count == 0:
            board[i][j] = 'B'
        else:
            board[i][j] = str(mine_count)
            return

        for d in directions:
            ni, nj = i + d[0], j + d[1]
            if 0 <= ni < m and 0 <= nj < n:
                self.dfs(board, ni, nj)

# With visited, works, but we can save space by modifying original board with VE for Visited Empty to avoid processing it again.
class Solution:
    directions = [(-1, 0), (-1, -1), (-1, 1), (0,-1), (0, 1), (1, -1), (1, 0), (1, 1)]
    def updateBoard(self, board, click):
        return self.bfs(board, click)

    def bfs(self, board, click):
        queue = [(click[0], click[1])]
        m, n = len(board), len(board[0])
        visited = set((click[0], click[1]))

        while queue:
            r, c = queue.pop(0)
            if board[r][c] == 'M':
                board[r][c] = 'X'
                break

            # check for adjacent mines
            mines = 0
            for i, j in self.directions:
                dr = r + i
                dc = c + j
                if 0 <= dr < m and 0 <= dc < n and board[dr][dc] == 'M':
                    mines += 1
            board[r][c] = str(mines) if mines else 'B'
            if board[r][c] != 'B': continue

            # add neighbors
            for i, j in self.directions:
                dr = r + i
                dc = c + j
                # BFS could potentially add duplicate (i,j) to the queue so we check that (i,j) is not already in the queue
                if 0 <= dr < m and 0 <= dc < n and (dr,dc) not in visited and board[dr][dc] == 'E':
                    visited.add((dr, dc))
                    queue.append((dr, dc))
                
        return board


# Space improvement, by modifying original array.
class Solution:
    directions = [(-1, 0), (-1, -1), (-1, 1), (0,-1), (0, 1), (1, -1), (1, 0), (1, 1)]
    def updateBoard(self, board, click):
        return self.bfs(board, click)

    def bfs(self, board, click):
        queue = [(click[0], click[1])]
        m, n = len(board), len(board[0])
        while queue:
            r, c = queue.pop(0)
            if board[r][c] == 'M':
                board[r][c] = 'X'
                break

            # check for adjacent mines
            mines = 0
            for i, j in self.directions:
                dr = r + i
                dc = c + j
                if 0 <= dr < m and 0 <= dc < n and board[dr][dc] == 'M':
                    mines += 1

            # At least 1 nbr is a mine, so update the count and continue to next item in queue
            if mines:
                board[r][c] = str(mines)
                continue
            else:
                board[r][c] = 'B'

            # add neighbors
            for i, j in self.directions:
                dr = r + i
                dc = c + j
                # BFS could potentially add duplicate (i,j) to the queue so we check that (i,j) is not already in the queue
                if 0 <= dr < m and 0 <= dc < n and (dr,dc) and board[dr][dc] == 'E':
                    board[dr][dc] = 'VE'
                    queue.append((dr, dc))

        return board


class Solution:
    def updateBoard(self, board, click):
        i, j = click
        if board[i][j] == 'M':
            board[i][j] = 'X'
            return board
        
        n, m = len(board), len(board[0])
        q = collections.deque([(i,j)])
        visited = set((i,j))
        while q:
            x,y = q.popleft()
            count = 0
            neighbors = []
            for pos in [(-1,-1), (-1,0), (-1, 1),(0,-1), (0,1), (1,-1),(1,0),(1,1)]:
                nx,ny = x+pos[0], y+pos[1]
                if 0<=nx<n and 0<=ny<m:
                    c = board[nx][ny]
                    if c == 'M':
                        count += 1
                    elif c == 'E':
                        neighbors.append((nx,ny))
            if count == 0:
                board[x][y] = 'B'
                for pos in neighbors:
                    if pos not in visited:
                        q.append((pos[0], pos[1]))
                        visited.add(pos)
            else:
                board[x][y] = str(count)
        return board