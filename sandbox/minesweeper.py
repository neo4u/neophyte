class Solution:
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
            mines, blnk_nbrs = 0, []
            for dx, dy in dirs:
                x, y = i + dx, j + dy
                if self.valid_mine(board, x, y):
                    mines += 1
                elif self.valid_blank(board, x, y):
                    blnk_nbrs.append([x, y])

            if mines == 0:
                board[i][j] = "B"
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
