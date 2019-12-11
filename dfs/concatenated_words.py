from typing import List


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words = set(words)
        self.memo = {}
        return [word for word in words if self.dfs(word, words)]

    def dfs(self, word, words):
        if word in self.memo: return self.memo[word]
        self.memo[word] = False

        for i in range(1, len(word)):
            prefix, suffix = word[:i], word[i:]
            if prefix in words and suffix in words:
                self.memo[word] = True
                break
            if prefix in words and self.dfs(suffix, words):
                self.memo[word] = True
                break
            if suffix in words and self.dfs(prefix, words):
                self.memo[word] = True
                break
        return self.memo[word]


# 472. Concatenated Words
# https://leetcode.com/problems/concatenated-words/description/
