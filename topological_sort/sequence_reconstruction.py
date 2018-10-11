# The basic is to get topological sort of seqs nodes,
# if it is unique and equal to org, then true, else False
# Following is how to implement in details:
# in each step,
# if we have more than one node whose incoming nodes count is zero then org is not unique,
# return False

# At last we check if the topological sort contain all nodes in the in seqs and equal to org

from collections import defaultdict


class Solution(object):
    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        adjacent = defaultdict(list)
        incoming_nodes = defaultdict(int)
        nodes = set()

        for arr in seqs:
            nodes |= set(arr)
            for i in range(len(arr)):
                if i == 0:
                    incoming_nodes[arr[i]] += 0
                if i < len(arr) - 1:
                    adjacent[arr[i]].append(arr[i + 1])
                    incoming_nodes[arr[i + 1]] += 1

        cur = [k for k in incoming_nodes if incoming_nodes[k] == 0]
        res = []
        while len(cur) == 1:
            cur_node = cur.pop()
            res.append(cur_node)

            for node in adjacent[cur_node]:
                incoming_nodes[node] -= 1
                if incoming_nodes[node] == 0:
                    cur.append(node)

        if len(cur) > 1:
            return False
        return len(res) == len(nodes) and res == org

# This question can be simplified to three conditions:

# 1. TopSort order exists
# 2. Whether the TopSort order is the only one (Uniqueness of Topological sort,
#     Hamilton path, see https://en.wikipedia.org/wiki/Topological_sorting#Uniqueness).
#     If not, then it means that some pairs have only partial order and no complete order,
#     so the order between the elements cannot be completely determined.
# 3. The only top sort order constructed should be equal to the org.

# index == org.length (check condition 3) && index == map.size()
# (check all the vertex in the graph has been visited, so the top sort order exists, check condition 1)
# How to check only one order? queue.size() should always be one,
# then only one element at a time has indegree to be 0, so you only have one choice (check condition 2)

# Except from the wiki link above
# If a topological sort has the property that all pairs of consecutive vertices in the sorted order are connected by edges,
# then these edges form a directed Hamiltonian path in the DAG.
# If a Hamiltonian path exists, the topological sort order is unique; no other order respects the edges of the path.
# Conversely, if a topological sort does not form a Hamiltonian path,
# the DAG will have two or more valid topological orderings,
# for in this case it is always possible to form a second valid ordering by
# swapping two consecutive vertices that are not connected by an edge to each other.
# Therefore, it is possible to test in linear time whether a unique ordering exists,
# and whether a Hamiltonian path exists, despite the NP-hardness of the Hamiltonian path problem
# for more general directed graphs
