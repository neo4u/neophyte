from typing import List
import collections


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word: return True
        if not board or not board[0]: return False
        self.dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Pre-process and check feasibility of solution, else return false
        board_c = collections.Counter([c for row in board for c in row])
        word_c = collections.Counter(word)
        for c in word_c:
            if c not in board_c or word_c[c] > board_c[c]:
                return False

        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if self.dfs(board, i, j, word): return True

        return False

    def dfs(self, board, i, j, word):
        if not word: return True
        if not self.valid_char_match(board, i, j, word): return False

        c = board[i][j]  # first character is found, check the remaining part
        board[i][j] = "#"  # avoid visit agian
        for dx, dy in self.dirs:
            x, y = i + dx, j + dy
            if self.dfs(board, x, y, word[1:]): return True

        board[i][j] = c
        return False

    def valid_char_match(self, board, i, j, word):
        return  0 <= i <= len(board) - 1 and 0 <= j <= len(board[0]) - 1 and word[0] == board[i][j]


# 79. Word Search
# https://leetcode.com/problems/word-search/description/

# Intuition:
# 1. Words are available horizontally or vertically
# 2. One requirement for the word to exist is that,
#    all the chars of the word should be present in the matrix

# Steps:
# A. Pre-Process (Just an optimization for early exit, not required for the main portion of the algorithm)
#   1. Pre-processing involves getting the count of every char on the board in 'board_c',
#      processing the word itself to get the counts of each char in 'word_c'
#   2. Now we iterate over the chars in the given 'word' and if any of the below happens we return false:
#      - If any char is not present in 'board_c'
#      - if the count of any char doesn't is less than the desired count as per 'word_c'
# B. dfs part
#   1. From every position (i, j) in the matrix, we start a recusrive search
#      and for every char we find we remove it from the search string and continue search for the rest
#      For example, If we're searching for cat and we find 'c' at board[0][0],
#      we continue searching the four directions for the rest of the board for word[1:],
#      which in this case will be 'at', in
#   2. Once, we find a char, we mark that (i, j) as "#" to mark it as visited for the current instance of DFS
#   3. If dfs(next_dir, rest_of_the_word) doesn't yield true, we set the char back to what it was and return False (WHy????)
#      We're doing this because each dfs will need its own visited set. We don't want to contaminate the results for the next DFS.
#      Our marking with a '#' is just to mark it as visited for the current DFS


# Time: O((mn)^2)
# Space: O(mn)
