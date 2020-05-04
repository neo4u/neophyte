import collections
from typing import List


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        patt_words = self.get_patt_words(wordList)
        wordList = set(wordList)
        result, q  = [], {beginWord: [[beginWord]]}

        while q:
            level_q = collections.defaultdict(list)
            for w in q:
                if w == endWord: result.extend(path for path in q[w])
                else:
                    for i, _ in enumerate(w):
                        p = w[:i] + '*' + w[i + 1:]
                        for nbr_w in patt_words[p]:
                            if nbr_w not in wordList: continue
                            level_q[nbr_w].extend(path + [nbr_w] for path in q[w])
            wordList -= set(level_q.keys())
            q = level_q
        return result

    def get_patt_words(self, word_list):
        patt_words = collections.defaultdict(list)
        for w in word_list:
            for i, _ in enumerate(w):
                patt = w[:i] + '*' + w[i + 1:]
                patt_words[patt].append(w)
        return patt_words


# 126. Word Ladder II
# https://leetcode.com/problems/word-ladder-ii/description/
