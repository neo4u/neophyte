import collections

class Solution(object):
    def numBusesToDestination(self, routes, S, T):
        if S == T: return 0

        routes = list(map(set, routes))
        graph = collections.defaultdict(set)

        for i, r1 in enumerate(routes):
            for j in range(i + 1, len(routes)):
                r2 = routes[j]
                if any(r in r2 for r in r1):
                    graph[i].add(j)
                    graph[j].add(i)

        seen, targets = set(), set()
        for node, route in enumerate(routes):
            if S in route: seen.add(node)
            if T in route: targets.add(node)

        q = [(node, 1) for node in seen]
        # for node, depth in queue:
        while q:
            n = len(q)
            for i in range(n):
                node, depth = q.pop(0)
                if node in targets: return depth
                for nbr in graph[node]:
                    if nbr not in seen:
                        seen.add(nbr)
                        q.append((nbr, depth + 1))

        return -1


import collections
class Solution2:
    def numBusesToDestination(self, routes, S, T):
        graph = collections.defaultdict(set)
        if S == T: return 0

        for i, route in enumerate(routes):
            for station in route:
                graph[station].add(i)

        visited, bus_count, q = set(graph[S]), 0, list(graph[S])

        while q:
            bus_count += 1
            n = len(q)
            for i in range(n):
                route_idx = q.pop(0)
                for station in routes[route_idx]:
                    if station == T: return bus_count

                    for next_route_idx in graph[station]:
                        if next_route_idx in visited: continue
                        q.append(next_route_idx)
                        visited.add(next_route_idx)

        return -1


# 815. Bus Routes
# https://leetcode.com/problems/bus-routes/description/
