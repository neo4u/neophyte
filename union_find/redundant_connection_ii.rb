class DS
    attr_accessor :roots, :ranks

    def initialize()
        @roots = Hash.new { |h, k| h[k] = k }
        @ranks = Hash.new { |h, k| h[k] = 0 }
    end

    def find(x)
        @roots[x] = find(@roots[x]) if x != @roots[x]
        @roots[x]
    end

    def union(x, y)
        par_x, par_y = find(x), find(y)
        return false if par_x == par_y

        if @ranks[par_x] > @ranks[par_y]
            @roots[par_y] = par_x
        elsif @ranks[par_y] > @ranks[par_x]
            @roots[par_x] = par_y
        else
            @roots[par_y] = par_x
            @ranks[par_x] += 1
        end

        true
    end
end


def find_redundant_directed_connection(edges)
    n = edges.size
    parent, ds = Array.new(n + 1, -1), DS.new()
    first_edge, second_edge, cycle_edge = -1, -1, -1

    0.upto(n - 1) do |i|
        p, c = edges[i]
        if parent[c] == -1
            parent[c] = i
            cycle_edge = i if !ds.union(p, c)
        else
            first_edge = parent[c]
            second_edge = i
        end
        puts "edge: #{edges[i]} first: #{first_edge} second: #{second_edge} cycle: #{cycle_edge}"
    end

    return edges[second_edge] if cycle_edge == -1   #  no cycle found by removing second
    return edges[cycle_edge] if second_edge == -1   #  no edge removed
    return edges[first_edge]
end


# Input: [[2,1],[3,1],[4,2],[1,4]]
# Output:     [1,4]
# Expected: [2,1]


# 4 ----> 2 ----> 1
#         3 ----->

# 685. Redundant Connection II
# https://leetcode.com/problems/redundant-connection-ii/description/

# Approach 1: DFS
# Approach 2: Disjoin Set Union Find 
# https://leetcode.com/problems/redundant-connection-ii/discuss/108058/one-pass-disjoint-set-solution-with-explain
# https://leetcode.com/problems/redundant-connection-ii/discuss/108070/Python-O(N)-concise-solution-with-detailed-explanation-passed-updated-testcases


# The input graph either has loop or no loop, either has a node with dual-parent or no such node.
# When there is a node with two parents, we can label the two edges to its parents as E1 and E2
# following the order of their appearance in the input list. We have 4 cases:
# 1. yes loop, yes dual. One of E1 and E2 must be in the loop. Need to remove the one that's in the loop.
# 2. no loop, yes dual. Need to remove E2 because it's the latter one.
# 3. yes loop, no dual. Need to remove the last edge added to the loop.
# 4. no loop, no dual. Impossible.

# Steps in my solution:
# 1. go through all edges and save parent(s) for each node in a dictionary.
#    If one node has already got a parent, save the current edge in extra. So E1 is in the dictionary and E2 is in extra.
# 2. if there is a node with two parents, start from that node and see if there is a loop in the dictionary. If there is a loop, remove E1. Otherwise remove E2, because either E2 is in a loop in the input graph or the input graph doesn't have a loop.
# 3. if there is no such node, there must be a loop in the dictionary. Note that the root node must be in the loop, so start from any node and we will end up in the loop. Find the loop and remove the last edge added into the loop.

# Discussions:

# 1. the method works with generalized notation of nodes, i.e. the N nodes doesn't need to be labeled as 1..N.
# 2. I don't like how I implemented the 3rd step. Suggestions are welcome!


# Time: O(n), we process all the edges
# Space: O(n)

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(find_redundant_directed_connection([[1,2], [1,3], [2,3]]), [2,3])
assert_equal(find_redundant_directed_connection([[1,2], [2,3], [3,4], [4,1], [1,5]]), [4,1])
