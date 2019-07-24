class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.isEnd = False
        self.data = None
        self.rank = 0


class AutocompleteSystem(object):
    def __init__(self, sentences, times):
        self.root = TrieNode()
        self.keyword = ""
        for sentence, freq in zip(sentences, times):
            self.addRecord(sentence, freq)

    def addRecord(self, sentence, freq):
        p = self.root
        for c in sentence:
            if c not in p.children:
                p.children[c] = TrieNode()
            p = p.children[c]

        p.isEnd = True
        p.data = sentence
        p.rank -= freq

    def dfs(self, root):
        if not root: return []
        results = []

        if root.isEnd:
            results.append((root.rank, root.data))

        for child in root.children:
            results.extend(self.dfs(root.children[child]))
        return results

    def search(self, sentence):
        p = self.root

        for c in sentence:
            if c not in p.children:
                return []
            p = p.children[c]

        return self.dfs(p)

    def input(self, c):
        results = []
        if c != "#":
            self.keyword += c
            results = self.search(self.keyword)
        else:
            self.addRecord(self.keyword, 1)
            self.keyword = ""

        return [item[1] for item in sorted(results)[:3]]
