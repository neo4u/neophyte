from typing import List


class TrieNode:
    def __init__(self):
        self.chars = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        if not word:
            return

        node = self.root
        for char in word:
            if char not in node.chars:
                node.chars[char] = TrieNode()
            node = node.chars[char]
        node.is_word = True


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        self.query_letters = []

        for word in words:
            #reverse word and then insert into the trie
            self.trie.insert(word[-1::-1])

    def query(self, letter: str) -> bool:
        self.query_letters.append(letter)
        node = self.trie.root
        if not letter:
            return False

        for i in range(len(self.query_letters) - 1, -1, -1):
            if self.query_letters[i] in node.chars:
                node = node.chars[self.query_letters[i]]
                if node.is_word:
                    return True
            else:
                return False
        return False



# 1032. Stream of Characters
# https://leetcode.com/problems/stream-of-characters/description/
