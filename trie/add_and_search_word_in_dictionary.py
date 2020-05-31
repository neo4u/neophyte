import collections

class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for c in word:
            node = node.children[c]
        node.is_word = True

    def search(self, word):
        node = self.root
        self.result = False
        self.dfs(node, word)
        return self.result

    def dfs(self, node, word):
        if not word:
            if node.is_word: self.result = True
            return

        if word[0] == ".":
            for child_val in node.children.values():
                self.dfs(child_val, word[1:])
        else:
            node = node.children.get(word[0])
            if not node: return
            self.dfs(node, word[1:])



# 211. Add and Search Word - Data structure design
# https://leetcode.com/problems/add-and-search-word-data-structure-design/description/


# Steps:
# 1. Firstly, we do a add word, which adds each 
