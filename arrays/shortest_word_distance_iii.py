from typing import List


class Solution1:
    def shortestWordDistance(self, words: List[str], word1: str, word2: str) -> int:
        result = float('inf')
        wp, wd = -1, None

        for i, w in enumerate(words):
            if w == word1 or w == word2:
                if wp == -1:
                    wd = w
                    wp = i
                elif w == wd:
                    if word1 == word2:
                        result = min(result, i - wp)
                    wp = i
                else:
                    result = min(result, i - wp)
                    wd = w
                    wp = i

        return result

# Only check if word1 and word2 is same once and save it in a boolean and use it wisely.
# This way we don't lose the speed and the code remain clean.


class Solution:
    def shortestWordDistance(self, words: List[str], word1: str, word2: str) -> int:
        idx1, idx2 = -1, -1
        min_diff = float('inf')

        for i, w in enumerate(words):
            if idx1 < idx2:                     # always update the smaller loc first
                if w == word1:      idx1 = i
                elif w == word2:    idx2 = i
            else:
                if w == word2:      idx2 = i
                elif w == word1:    idx1 = i

            if idx1 != -1 and idx2 != -1:
                min_diff = min(min_diff, abs(idx2 - idx1))

        return min_diff


class Solution:
    def shortestWordDistance(self, words: List[str], word1: str, word2: str) -> int:
        n = len(words)
        min_diff = n
        idx1, idx2 = -1, -1

        for i, w in enumerate(words):
            if w == word1:
                idx1 = i
                if idx2 != -1: min_diff = min(min_diff, idx1 - idx2)

            if w == word2:
                idx2 = i
                if idx1 != -1 and idx1 != idx2: min_diff = min(min_diff, idx2 - idx1)

        return min_diff

# O(n) time O(1) space:


# 245. Shortest Word Distance III
# https://leetcode.com/problems/shortest-word-distance-iii/description/
