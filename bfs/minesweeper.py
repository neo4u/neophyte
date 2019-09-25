from typing import List


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if not board: return []
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
            for d in directions:
                ni, nj = i + d[0], j + d[1]
                if 0 <= ni < m and 0 <= nj < n:
                    self.dfs(board, ni, nj)
        else:
            board[i][j] = str(mine_count)
            return


class Solution2:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if not board or not board[0]: return board
        dirs = [[0, -1], [0, 1], [-1, 0], [1, 0], [-1, -1], [-1, 1], [1, -1], [1, 1]]
        i, j = click
        if board[i][j] == "M":
            board[i][j] = "X"
            return board

        q = [click]
        while q:
            i, j = q.pop(0)
            mines = 0
            blnk_nbrs = []
            for dx, dy in dirs:
                x, y = i + dx, j + dy
                if self.valid_mine(board, x, y):
                    mines += 1
                elif self.valid_blank(board, x, y):
                    blnk_nbrs.append([x, y])

            if mines == 0:
                board[i][j] = "B"
                for nbr_x, nbr_y in blnk_nbrs:
                    board[nbr_x][nbr_y] = 'VE'
                q.extend(blnk_nbrs)
            else:
                board[i][j] = str(mines)

        return board

    def valid_blank(self, board, i, j):
        m, n = len(board), len(board[0])
        return 0 <= i <= m - 1 and 0 <= j <= n - 1 and board[i][j] == "E"

    def valid_mine(self, board, i, j):
        m, n = len(board), len(board[0])
        return 0 <= i <= m - 1 and 0 <= j <= n - 1 and board[i][j] == "M"
