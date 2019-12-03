from typing import List
import collections


class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word) -> None:
        node = self.root
        for c in word: node = node.children[c]
        node.is_word = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.result, trie = [], Trie()
        root = trie.root
        self.dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        self.m, self.n = len(board), len(board[0])
        for w in words: trie.insert(w)

        for i in range(self.m):
            for j in range(self.n):
                self.dfs(board, root, i, j, "")

        return self.result

    def dfs(self, board, node: TrieNode, i: int, j: int, path: str) -> None:
        if node.is_word:
            self.result.append(path)
            node.is_word = False
        if not self.in_bounds(i, j): return

        c = board[i][j]
        node = node.children.get(c) # This is basically same as node.children[c], but somehow using this is causing memory exceeded error
        if not node: return

        board[i][j] = "#"
        for di, dj in self.dirs:
            x, y = i + di, j + dj
            self.dfs(board, node, x, y, path + c)
        board[i][j] = c

    def in_bounds(self, i: int, j: int) -> bool:
        return  0 <= i <= self.m - 1 and 0 <= j <= self.n - 1




# Quick Version, to focus on efficiency and not on clarity
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0]: return False
        self.m, self.n, root = len(board), len(board[0]), {}

        for word in words:
            trie = root
            for c in word:
                if c not in trie:
                    trie[c] = {}
                trie = trie[c]
            trie['#'] = word

        self.result = []
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] in root: self.dfs(board, i, j, root)

        return self.result

    def dfs(self, board, i, j, parent):
        c, board[i][j] = board[i][j], '{'
        trie = parent[c]
        if '#' in trie:
            self.result.append(trie['#'])
            trie.pop('#')

        if i and board[i - 1][j] in trie:               self.dfs(board, i - 1, j, trie)
        if i < self.m - 1 and board[i + 1][j] in trie:  self.dfs(board, i + 1, j, trie)
        if j and board[i][j - 1] in trie:               self.dfs(board, i, j - 1, trie)
        if j < self.n - 1 and board[i][j + 1] in trie:  self.dfs(board, i, j + 1, trie)

        board[i][j] = c
        if not trie: parent.pop(c)


# 212. Word Search II
# https://leetcode.com/problems/word-search-ii/description/
