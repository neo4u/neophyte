class DS:
    def __init__(self,):
        self.parent = {}
        self.rank = {}
        self.count = 0

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def has_parent(self, x):
        return x in self.parent

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py: return False

        if self.rank[px] > self.rank[py]:
            self.parent[py] = px
        elif self.rank[py] > self.rank[px]:
            self.parent[px] = py
        else:
            self.parent[py] = px
            self.rank[px] += 1

        self.count -=1
        return True

    def set_parent(self, x):
        self.parent[x] = x
        self.rank[x] = 0
        self.count += 1

    def print_ds(self):
        print(self.parent)
        print(self.count)


class Solution:
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        m, n = len(words1), len(words2)
        if m != n: return False
        ds = DS()

        for pair in pairs:
            x, y = pair
            if not ds.has_parent(x): ds.set_parent(x)
            if not ds.has_parent(y): ds.set_parent(y)
            ds.union(x, y)

        for i in range(m):
            w1, w2 = words1[i], words2[i]
            if w1 == w2: continue

            if not ds.has_parent(w1) or not ds.has_parent(w2): return False
            if ds.find(w1) != ds.find(w2): return False

        return True


import collections
class Solution:
    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        m, n = len(words1), len(words2)
        if m != n: return False

        graph = collections.defaultdict(list)
        for u, v in pairs:
            graph[u].append(v)
            graph[v].append(u)

        for w1, w2 in zip(words1, words2):
            if w1 == w2: continue
            if not self.dfs(graph, w1, w2, set()): return False

        return True


    def dfs(self, graph, s, d, visited):
        if s == d: return True
        visited.add(s)
        for nbr in graph[s]:
            if nbr not in visited and self.dfs(graph, nbr, d, visited): return True

        return False

sol = Solution()
assert sol.areSentencesSimilarTwo(
    ["great","acting","skills"],
    ["fine","drama","talent"],
    [["great","good"],["fine","good"],["drama","acting"],["skills","talent"]]
)

# 737. Sentence Similarity II
# https://leetcode.com/problems/sentence-similarity-ii/description/