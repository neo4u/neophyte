class TrieNode(object):
    def __init__(self):
        self.word = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    # time: O(n), n: word.length
    # space: O(num of TrieNode*26) = O(num of word.length*26)
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root

        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]

        node.word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for c in word:
            if c not in node.children: return False
            node = node.children[c]
        return node.word

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for i in prefix:
            if i not in node.children: return False
            node = node.children[i]
        return True
