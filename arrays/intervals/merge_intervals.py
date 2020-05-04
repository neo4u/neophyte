from typing import List
import collections


class Solution:
    def overlap(self, a, b):
        return a.start <= b.end and b.start <= a.end

    # generate graph where there is an undirected edge between intervals u
    # and v iff u and v overlap.
    def build_graph(self, intervals):
        graph = collections.defaultdict(list)

        for i, interval_i in enumerate(intervals):
            for j in range(i + 1, len(intervals)):
                if self.overlap(interval_i, intervals[j]):
                    graph[interval_i].append(intervals[j])
                    graph[intervals[j]].append(interval_i)

        return graph

    # merges all of the nodes in this connected component into one interval.
    def merge_nodes(self, nodes):
        min_start = min(node.start for node in nodes)
        max_end = max(node.end for node in nodes)
        return Interval(min_start, max_end)

    # gets the connected components of the interval overlap graph.
    def get_components(self, graph, intervals):
        visited = set()
        comp_number = 0
        nodes_in_comp = collections.defaultdict(list)

        def mark_component_dfs(start):
            stack = [start]
            while stack:
                node = stack.pop()
                if node not in visited:
                    visited.add(node)
                    nodes_in_comp[comp_number].append(node)
                    stack.extend(graph[node])

        # mark all nodes in the same connected component with the same integer.
        for interval in intervals:
            if interval not in visited:
                mark_component_dfs(interval)
                comp_number += 1

        return nodes_in_comp, comp_number

    def merge(self, intervals):
        graph = self.build_graph(intervals)
        nodes_in_comp, number_of_comps = self.get_components(graph, intervals)

        # all intervals in each connected component must be merged.
        return [self.merge_nodes(nodes_in_comp[comp]) for comp in range(number_of_comps)]



class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: return []
        intervals.sort(key=lambda x: x[0])
        n, merged = len(intervals), [intervals[0]]

        for i in range(1, n):
            curr = intervals[i]
            if curr[0] <= merged[-1][1]:    merged[-1][1] = max(merged[-1][1], curr[1])
            else:                           merged.append(curr)

        return merged


# 56. Merge Intervals
# https://leetcode.com/problems/merge-intervals/description/

# 1. build graph connecting overlapping intervals
# 2. do a dfs to calculate connected components
# 3. Merge all components
# 4. Return merged intervals

# Time: O(n^2)
# Building the graph costs O(V + E) = O(V) + O(E) = O(n) + O(n^2) = O(n^2) time,
# as in the worst case all intervals are mutually overlapping.
# Traversing the graph has the same cost (although it might appear higher at first)
# because our visited set guarantees that each node will be visited exactly once.
# Finally, because each node is part of exactly one component, the merge step costs O(V) = O(n) time.
# This all adds up as follows:
# O(n^2) + O(n^2) + O(n) = O(n^2)

# Space: O(n^2)
# As previously mentioned, in the worst case,
# all intervals are mutually overlapping, so there will be an edge for every pair of intervals.
# Therefore, the memory footprint is quadratic in the input size.

# Time: O(n^2)
# Space: O(n^2)


# Approach 2: Sort by Start Times
# 1. sort by start times
# 2. iterate through interval
# 3. if last of merged has end time < curr intervals start then push the element into merged as it is not overlapping
# 4. if overlappping then merge with last interval by taking max of the ends of merged.last.end and curr.end

# Time: O(nlgn) Other than the sort invocation,
# Space: O(1) (or O(n)), If we can sort intervals in place then O(1)
