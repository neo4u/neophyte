from typing import List
import collections
import itertools


class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        self.graph = collections.defaultdict(set)

        for u, v, w in allowed: self.graph[u, v].add(w)
        return self.dfs(bottom)

    def dfs(self, bottom):
        print(f"dfs call with: {bottom}")
        if len(bottom) == 1: return True
        return any(self.dfs(cand) for cand in self.generate(bottom))

    def generate(self, s):
        n = len(s)
        tups = list(self.graph[s[i], s[i + 1]] for i in range(n - 1))
        print(tups)
        # products = list(itertools.product(*tups))
        products = list(self.product(tups))
        print(f"products: {products}")
        return products

    def product(self, tups):
        if not tups: yield ()
        else:
            for a in tups[0]:
                for prod in self.product(tups[1:]):
                    yield (a,) + prod

# 756. Pyramid Transition Matrix
# https://leetcode.com/problems/pyramid-transition-matrix/description/


sol = Solution()
# assert sol.pyramidTransition("BCD", ["BCG", "CDE", "GEA", "FFF"]) == True
assert sol.pyramidTransition("AABA", ["AAA", "AAB", "ABA", "ABB", "BAC"]) == False
