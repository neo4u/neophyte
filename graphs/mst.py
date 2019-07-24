from ds import DS


class Solution:
    def find_mst(self, edges):
        edges = sorted(edges, key=lambda x: x[2])
        vertices = set()
        for u, v, _ in edges:
            vertices.add(u)
            vertices.add(v)
        vrtx_count, ds, edge_count, i, result = len(vertices), DS(), 0, 0, []

        while edge_count < vrtx_count - 1:
            u, v, _ = edges[i]
            i += 1
            if not ds.has_parent(u): ds.set_parent(u)
            if not ds.has_parent(v): ds.set_parent(v)

            if not ds.union(u, v): continue
            result.append((u, v))
            edge_count += 1

        return result

sol = Solution()
print(sol.find_mst([(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)])) # == [(2, 3), (0, 3), (0, 1)]
