import collections

class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False


class WordDictionary(object):
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for c in word:
            node = node.children[c]
        node.isWord = True

    def search(self, word):
        node = self.root
        self.result = False
        self.dfs(node, word)
        return self.result

    def dfs(self, node, word):
        if not word:
            if node.isWord: self.result = True
            return

        if word[0] == ".":
            for child_val in node.children.values():
                self.dfs(child_val, word[1:])
        else:
            node = node.children.get(word[0])
            if not node: return
            self.dfs(node, word[1:])
