
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.memo = {}
        return self.dfs(s, wordDict)

    def dfs(self, s, word_dict):
        if s in self.memo: return self.memo[s]
        if not s: return []

        result = []
        for word in word_dict:
            if not s.startswith(word): continue

            if len(word) == len(s): result.append(word)
            else:
                results_of_rest = self.dfs(s[len(word):], word_dict)
                for item in results_of_rest:
                    item = f"{word} {item}"
                    result.append(item)
        self.memo[s] = result
        return result


# 140. Word Break II
# https://leetcode.com/problems/word-break-ii/description/

# cat, cats, sand, and, dog

# catsanddogsand
