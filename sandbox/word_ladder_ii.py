import collections

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        wordList = set(wordList)
        res = []
        q = {}
        q[beginWord] = [[beginWord]]

        while q:
            newlayer = collections.defaultdict(list)
            for w in q:
                if w == endWord: res.extend(k for k in q[w])
                else:
                    for i in range(len(w)):
                        for c in 'abcdefghijklmnopqrstuvwxyz':
                            neww = w[:i] + c + w[i + 1:]
                            if neww in wordList:
                                newlayer[neww] += [j + [neww] for j in q[w]]

            wordList -= set(newlayer.keys())
            q = newlayer

        return res
