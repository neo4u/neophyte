import collections
from typing import List
import string


class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        wordList, result, q = set(wordList), [], {}
        q[beginWord] = [[beginWord]]

        while q:
            level_q = collections.defaultdict(list)

            for w in q:
                if w == endWord: result.extend(k for k in q[w])
                else:
                    for i in range(len(w)):
                        for c in string.ascii_lowercase:
                            next_w = w[:i] + c + w[i + 1:]
                            if next_w not in wordList: continue
                            level_q[next_w] += [j + [next_w] for j in q[w]]

            wordList -= set(level_q.keys())
            q = level_q

        return result


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordDict = set(wordList)
        if endWord not in wordDict: return []

        front, back = {beginWord}, {endWord}
        parents = collections.defaultdict(set)
        direction = 1
        chars = set(string.ascii_lowercase)

        while front and back:
            if len(front) > len(back):
                front, back = back, front
                direction *= -1

            wordDict -= front
            next_level = set()

            for w in front:
                for i in range(len(beginWord)):
                    p1, p2 = w[:i], w[i + 1:]
                    for c in chars:
                        next_w = p1 + c + p2
                        if next_w in wordDict:
                            next_level.add(next_w)
                            if direction == 1:  parents[next_w].add(w)
                            else:               parents[w].add(next_w)

            if next_level & back:
                result = [[endWord]]
                while result and result[0][0] != beginWord:
                    result = [[p]+r for r in result for p in parents[r[0]]]
                return result

            front = next_level

        return []
