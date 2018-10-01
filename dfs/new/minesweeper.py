class Solution:

    directions = [(-1, 0), (-1, -1), (-1, 1), (0,-1), (0, 1), (1, -1), (1, 0), (1, 1)]

    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        # return self.bfs(board, click)
        return self.dfs(board, click)

    def dfs(self, board, click):
        stack = [(click[0], click[1])]
        m, n = len(board), len(board[0])
        while stack:
            r, c = stack.pop() # last inserted element
            
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

            # add neighbors
            for i, j in self.directions:
                dr = r + i
                dc = c + j
                if 0 <= dr < m and 0 <= dc < n and board[r][c] == 'B' and board[dr][dc] == 'E':
                    stack.append((dr, dc))

        return board
