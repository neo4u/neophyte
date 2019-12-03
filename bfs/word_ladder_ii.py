import collections
from typing import List


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        patt_words = self.get_patt_words(wordList)
        level = collections.defaultdict(lambda: float('inf'))
        level[beginWord] = 0

        paths, shortest = [], float('inf')
        q = [(beginWord, [beginWord])]

        while q:
            w, path = q.pop(0)
            if len(path) >= shortest: return paths

            for i, _ in enumerate(w):
                p = w[:i] + '*' + w[i + 1:]
                for nbr_w in patt_words[p]:
                    new_path = path + [nbr_w]
                    if nbr_w == endWord:
                        paths.append(new_path)
                        shortest = len(new_path)
                    elif level[nbr_w] > level[w]:
                        q.append((nbr_w, new_path))
                        level[nbr_w] = level[w] + 1
        return paths

    def get_patt_words(self, wordList):
        patt_words = collections.defaultdict(list)
        for w in wordList:
            for i, _ in enumerate(w):
                patt = w[:i] + '*' + w[i + 1:]
                patt_words[patt].append(w)
        return patt_words



class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        patt_words = self.get_patt_words(wordList)
        wordList = set(wordList)
        res, layer = [], {}
        layer[beginWord] = [[beginWord]]

        while layer:
            newlayer = collections.defaultdict(list)
            for w in layer:
                if w == endWord:
                    res.extend(k for k in layer[w])
                else:
                    for i, _ in enumerate(w):
                        p = w[:i] + '*' + w[i + 1:]
                        for nbr_w in patt_words[p]:
                            if nbr_w not in wordList: continue
                            newlayer[nbr_w] += [j + [nbr_w] for j in layer[w]]

            wordList -= set(newlayer.keys())
            layer = newlayer

        return res

    def get_patt_words(self, wordList):
        patt_words = collections.defaultdict(list)
        for w in wordList:
            for i, _ in enumerate(w):
                patt = w[:i] + '*' + w[i + 1:]
                patt_words[patt].append(w)
        return patt_words


# 126. Word Ladder II
# https://leetcode.com/problems/word-ladder-ii/description/
