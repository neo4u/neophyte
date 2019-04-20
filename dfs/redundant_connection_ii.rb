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


# 685. Redundant Connection II
# https://leetcode.com/problems/redundant-connection-ii/description/

# Approach 1: DFS
# Approach 2: Disjoin Set Union Find 
# https://leetcode.com/problems/redundant-connection-ii/discuss/108058/one-pass-disjoint-set-solution-with-explain
# https://leetcode.com/problems/redundant-connection-ii/discuss/108070/Python-O(N)-concise-solution-with-detailed-explanation-passed-updated-testcases

# Time: O(n), we process all the edges
# Space: O(n)

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(find_redundant_directed_connection([[1,2], [1,3], [2,3]]), [2,3])
assert_equal(find_redundant_directed_connection([[1,2], [2,3], [3,4], [4,1], [1,5]]), [4,1])
