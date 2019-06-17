class DS:
    def __init__(self,):
        self.parent = {}
        self.rank = {}
        self.count = 0

    def find(self, x):
        if x != self.parent[x]: self.parent[x] = self.find(self.parent[x])
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
    def removeStones(self, stones):
        ds = DS()

        for i, j in stones:
            x, y = f"x_{i}", f"y_{j}"
            print([i, j])
            if not ds.has_parent(x): ds.set_parent(x)
            if not ds.has_parent(y): ds.set_parent(y)
            print("Before")
            ds.print_ds()
            ds.union(x, y)
            print("After")
            ds.print_ds()

        return len(stones) - ds.count


class Solution3:
    def removeStones(self, stones):
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        for i, j in stones:
            rows[i].add(j)
            cols[j].add(i)

        seen_x, seen_y = set(), set()
        comps = 0
        for i, j in stones:
            if i not in seen_x:
                comps += 1
                self.dfs_row(i, seen_x, seen_y, rows)
                self.dfs_col(j, seen_x, seen_y, cols)
    
        return len(stones) - comps

    def dfs_row(i, seen_x, seen_y, rows):
        seen_x.add(i)
        for j in rows[i]:
            if j not in seen_y:
                dfs_col(j)

    def dfs_col(j, seen_x, seen_y, cols):
        seen_y.add(j)
        for i in cols[j]:
            if i not in seen_x:
                dfs_row(i)

class DS:
    def __init__(self,):
        self.parent = {}
        self.rank = {}
        self.count = 0

    def find(self, x):
        if x not in self.parent: return float('inf')
        if x != self.parent[x]: self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

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

class Solution4:
    def removeStones(self, stones):
        ds = DS()

        for i, j in stones:
            print([i, j])
            if ds.find(i) == float('inf'): ds.set_parent(i)
            if ds.find(j) == float('inf'): ds.set_parent(~j)
            ds.union(i, ~j)
            ds.print_ds()

        return len(stones) - ds.count


import collections
class Solution5(object):
    def removeStones(self, stones):
        n = len(stones)
        graph = {}
        for i, s in enumerate(stones):
            graph[i] = []
            for j in range(i):
                y = stones[j]
                if s[0] == y[0] or s[1] == y[1]:
                    graph[i].append(j)
                    graph[j].append(i)

        print(graph)
        visited, count = set(), 0

        for node in graph.keys():
            if node in visited: continue
            count += 1
            self.dfs(graph, node, visited)

        return len(stones) - count

    def dfs(self, graph, node, visited):
        visited.add(node)
        for n in graph[node]:
            if n in visited:
                continue
            self.dfs(graph, n, visited)


import collections
class Solution2(object):
    def removeStones(self, stones):
        graph = collections.defaultdict(list)
        for i, x in enumerate(stones):
            for j in range(i):
                y = stones[j]
                if x[0] == y[0] or x[1] == y[1]:
                    graph[i].append(j)
                    graph[j].append(i)

        N = len(stones)
        ans = 0

        seen = [False] * N
        for i in range(N):
            if not seen[i]:
                stack = [i]
                seen[i] = True
                while stack:
                    ans += 1
                    node = stack.pop()
                    for nei in graph[node]:
                        if not seen[nei]:
                            stack.append(nei)
                            seen[nei] = True
                ans -= 1

        return ans


# 947. Most Stones Removed with Same Row or Column
# https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/description/

# [1,2,3,4]
# stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
# graph = {(x, y) : [(), ()]}