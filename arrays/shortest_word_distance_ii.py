from typing import List
import collections


class WordDistance:
    def __init__(self, words: List[str]):
        self.idxs = collections.defaultdict(list)
        for i, w in enumerate(words):
            self.idxs[w].append(i)

    def shortest(self, w1: str, w2: str) -> int:
        idxs1, idxs2 = self.idxs[w1], self.idxs[w2]
        m, n = len(idxs1), len(idxs2)
        i, j = 0, 0
        min_diff = float('inf')

        while i < m and j < n:
            min_diff = min(min_diff, abs(idxs1[i] - idxs2[j]))
            if idxs1[i] < idxs2[j]: i += 1
            else:                   j += 1

        return min_diff


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)


# 244. Shortest Word Distance II
# https://leetcode.com/problems/shortest-word-distance-ii/description/


# Intuition:
# - We build a dictionary of words to indexes where each of them occurs
# - The values are naturally sorted because we traverse from left to right while populating self.idxs dictionary
# - Hence we can apply the 2-pointer approach to ensure that min_diff is minimized

# Approach 1: 2 Pointer
# Time: O(n), Each call of shortest takes O(n)
# Space: O(n), This is at the class level
