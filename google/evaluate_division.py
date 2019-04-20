import collections

class Solution(object):
    def calcEquation(self, equations, values, queries):
        def dfs(start, end, path, paths):
            print(f"path: {path} | paths: {paths} | visited: {vis}")
            if start == end and start in G:
                paths[0] = path
                return
            if start in vis:
                return
            vis.add(start)
            for node in G[start]:
                dfs(node, end, path * W[start, node], paths)


        G, W = collections.defaultdict(set), collections.defaultdict(float)
        for (A, B), V in zip(equations, values):
            G[A], G[B] = G[A] | {B}, G[B] | {A}
            W[A, B], W[B, A] = V, 1.0 / V
            
        res = []
        for X, Y in queries:
            paths, vis = [-1.0], set()
            dfs(X, Y, 1.0, paths)
            print(f"paths: {paths}")
            res.append(paths[0])

        return res


class Solution2(object):
    def calcEquation(self, equations, values, queries):
        graph = {}
        def build_graph(equations, values):
            def add_edge(f, t, value):
                if f in graph:
                    graph[f].append((t, value))
                else:
                    graph[f] = [(t, value)]
            
            for vertices, value in zip(equations, values):
                f, t = vertices
                add_edge(f, t, value)
                add_edge(t, f, 1/value)
        
        def find_path(query):
            b, e = query
            
            if b not in graph or e not in graph:
                return -1.0
                
            q = collections.deque([(b, 1.0)])
            visited = set()
            
            while q:
                front, cur_product = q.popleft()
                if front == e:
                    return cur_product
                visited.add(front)
                for neighbor, value in graph[front]:
                    if neighbor not in visited:
                        q.append((neighbor, cur_product*value))
            
            return -1.0

        build_graph(equations, values)
        return [find_path(q) for q in queries]

class Solution3:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        res = []
        parent = {}    # i.e. [a, b] then parent[a] = b
        weight = {}    # i.e. a / b = 2.0, then weight[a] = 2.0
        ufind = UnionFind(parent, weight)
        for i, edge in enumerate(equations):
            x1, x2 = edge[0], edge[1]
            val = values[i]
            if x1 not in parent and x2 not in parent:
                parent[x1] = x2
                parent[x2] = x2
                weight[x1] = val
                weight[x2] = 1
            elif x1 not in parent:
                parent[x1] = x2
                weight[x1] = val
            elif x2 not in parent:    # weight[x1] already exists, if make x2 be x1's parent. then weight[x1] will be overwrite.
                parent[x2] = x1
                weight[x2] = 1 / val
            else:
                ufind.union(x1, x2, val)
                
        for x1, x2 in queries:
            if x1 not in parent or x2 not in parent or ufind.find(x1) != ufind.find(x2):
                res.append(-1.0)
            else:
                factor1 = weight[x1]
                factor2 = weight[x2]
                res.append(factor1 / factor2)
        return res

class UnionFind():
    def __init__(self, parent, weight):
        self.parent = parent
        self.weight = weight

    def find(self, vertex):
        if self.parent[vertex] == vertex:
            return vertex
        root = self.find(self.parent[vertex])
        self.weight[vertex] *= self.weight[self.parent[vertex]]
        self.parent[vertex] = root
        return root

    def union(self, vertex1, vertex2, val):
        root1 = self.find(vertex1)
        root2 = self.find(vertex2)
        self.weight[root1]= self.weight[vertex2] * val / self.weight[vertex1]
        self.parent[root1] = root2


equations = [["a", "b"], ["b", "c"]]
values = [2.0, 3.0]
queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]

sol = Solution()
assert sol.calcEquation(equations, values, queries) == [6.0, 0.5, -1.0, 1.0, -1.0]

sol2 = Solution2()
assert sol.calcEquation(equations, values, queries) == [6.0, 0.5, -1.0, 1.0, -1.0]

sol3 = Solution3()
assert sol.calcEquation(equations, values, queries) == [6.0, 0.5, -1.0, 1.0, -1.0]
