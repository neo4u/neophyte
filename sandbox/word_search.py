from typing import List
import collections

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word: return True
        if not board or not board[0]: return False

        # Pre-process and check feasibility of solution, else return false
        board_c = collections.Counter([c for row in board for c in row])
        word_c = collections.Counter(word)
        for c in word_c:
            if c not in board_c or word_c[c] > board_c[c]:
                return False

        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if self.bt(board, i, j, word):
                    return True

        return False

    def bt(self, board, i, j, word):
        if len(word) == 0: return True
        if not self.valid_char_match(board, i, j, word): return False

        c = board[i][j]  # first character is found, check the remaining part
        board[i][j] = "#"  # avoid visit agian
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dx, dy in dirs:
            x, y = i + dx, j + dy
            if self.bt(board, x, y, word[1:]): return True

        board[i][j] = c
        return False

    def valid_char_match(self, board, i, j, word):
        return  0 <= i <= len(board) - 1 and 0 <= j <= len(board[0]) - 1 and word[0] == board[i][j]
