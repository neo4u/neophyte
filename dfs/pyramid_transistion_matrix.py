from typing import List
import collections
import itertools


class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        self.graph = collections.defaultdict(set)
        for u, v, w in allowed: self.graph[u, v].add(w)
        return self.dfs(tuple(bottom))

    def dfs(self, bottom: tuple) -> bool:
        if len(bottom) == 1: return True
        return any(self.dfs(cand) for cand in self.generate(bottom))

    def generate(self, s: tuple) -> List[tuple]:
        n = len(s)
        tups = list(self.graph[s[i - 1], s[i]] for i in range(1, n))
        return list(itertools.product(*tups))


# 756. Pyramid Transition Matrix
# https://leetcode.com/problems/pyramid-transition-matrix/description/


sol = Solution()
assert sol.pyramidTransition("BCD", ["BCG", "CDE", "GEA", "FFF"]) == True
assert sol.pyramidTransition("AABA", ["AAA", "AAB", "ABA", "ABB", "BAC"]) == False
