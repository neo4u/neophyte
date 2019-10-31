from typing import List
import collections
import itertools


class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        self.graph = collections.defaultdict(set)

        for u, v, w in allowed: self.graph[u, v].add(w)
        return self.dfs(bottom)

    def dfs(self, bottom):
        if len(bottom) == 1: return True
        return any(self.dfs(cand) for cand in self.generate(bottom))

    def generate(self, A):
        n = len(A)
        tup = list(self.graph[A[i], A[i + 1]] for i in range(n - 1))
        product = list(itertools.product(*tup))
        return product


# 756. Pyramid Transition Matrix
# https://leetcode.com/problems/pyramid-transition-matrix/description/


sol = Solution()
assert sol.pyramidTransition("BCD", ["BCG", "CDE", "GEA", "FFF"]) == True
assert sol.pyramidTransition("AABA", ["AAA", "AAB", "ABA", "ABB", "BAC"]) == False
