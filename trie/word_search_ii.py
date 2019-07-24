import collections
class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False

class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True

    def search(self, word):
        node = self.root
        for w in word:
            node = node.children.get(w)
            if not node:
                return False
        return node.isWord
    
class Solution(object):
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        result = []
        trie = Trie()
        node = trie.root
        self.dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for w in words: trie.insert(w)

        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                self.dfs(board, node, m, n, i, j, "", result)

        return result

    def dfs(self, board, node, m, n, i, j, path, words_found):
        if node.isWord:
            words_found.append(path)
            node.isWord = False
        if not self.in_bounds(m, n, i, j): return

        c = board[i][j]
        node = node.children.get(c)
        if not node: return

        board[i][j] = "#"
        for dx, dy in self.dirs:
            self.dfs(board, node, m, n, i + dx, j + dy, path + c, words_found)
        board[i][j] = c

    def in_bounds(self, m, n, i, j):
        return  0 <= i <= m - 1 and 0 <= j <= n - 1


# 212. Word Search II
# https://leetcode.com/problems/word-search-ii/description/
