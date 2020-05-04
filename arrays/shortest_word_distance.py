import collections
from typing import List


# Approach 1: Naive
class Solution1:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        idx_map = collections.defaultdict(list)
        for i, word in enumerate(words):
            if word not in [word1, word2]: continue
            idx_map[word].append(i)

        idxs1, idxs2 = idx_map[word1], idx_map[word2]
        result = float('inf')
        for i in idxs1:
            for j in idxs2:
                result = min(result, abs(i - j))

        return result


# Approach 2: Naive with Binary Search
class Solution2:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        idx_map = collections.defaultdict(list)
        for i, word in enumerate(words):
            if word not in [word1, word2]: continue
            idx_map[word].append(i)

        idxs_1, idxs_2 = idx_map[word1], idx_map[word2]
        result = float('inf')
        for i in idxs_1:
            di = self.find_closest(idxs_2, i)
            result = min(abs(idxs_2[di] - i), result)

        return result

    def find_closest(self, idxs, target):
        n = len(idxs)
        l, r = 0, n - 1

        while l < r - 1:
            mid = (l + r) // 2

            if idxs[mid] == target: return mid
            elif idxs[mid] > target: r = mid
            else: l = mid

        if abs(idxs[l] - target) < abs(idxs[r] - target):
            return l

        return r


# Approach 3: One Pass
class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        idx1, idx2 = -1, -1
        result = float('inf')

        for i, w in enumerate(words):
            if w == word1:
                idx1 = i
                if idx2 != -1: result = min(result, abs(idx1 - idx2))

            if w == word2:
                idx2 = i
                if idx1 != -1: result = min(result, abs(idx2 - idx1))

        return result


# 243. Shortest Word Distance
# https://leetcode.com/problems/shortest-word-distance/description/



# Approach 1: Naive
# Time: O(n * n)
# Space: O(n)

# Approach 2: Naive with Binary Search
#


# Approach 3: One Pass
# - For each a, we need to get the recent position of b.
# - For each b, we need to get the recent position of a.
