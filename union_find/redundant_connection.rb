# Approach 1: DFS
# @param {Integer[][]} edges
# @return {Integer[]}
def find_redundant_connection(edges)
    @graph = Hash.new() { |h, k| h[k] = Set.new() }

    edges.each do |u, v|
        visited = Set.new()
        return [u, v] if @graph.key?(u) && @graph.key?(v) && dfs(u, v, visited)
        @graph[u].add(v)
        @graph[v].add(u)
    end
end

def dfs(s, d, visited)
    return if visited.include?(s)
    visited.add(s)
    return true if s == d

    @graph[s].to_a.map { |n| dfs(n, d, visited) }&.any?
end


class DisjoinSet
    attr_accessor :roots, :ranks

    def initialize()
        @roots = Hash.new() { |h, k| h[k] = k }
        @ranks = Hash.new() { |h, k| h[k] = 0 }
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

# Approach 2: Disjoin Set Union-Find
# @param {Integer[][]} edges
# @return {Integer[]}
def find_redundant_connection_uf(edges)
    ds = DisjoinSet.new()
    edges.each do |x, y|
        return [x, y] if !ds.union(x, y)
    end

    nil
end

# 684. Redundant Connection
# https://leetcode.com/problems/redundant-connection/description/

# Approach 1: DFS
# Appraoch 2: Disjoin Set Union-Find

require 'set'
require 'test/unit'
extend Test::Unit::Assertions

assert_equal(find_redundant_connection([[1,2], [1,3], [2,3]]), [2,3])
assert_equal(find_redundant_connection([[1,2], [2,3], [3,4], [4,1], [1,5]]), [4,1])
assert_equal(find_redundant_connection([[3,4],[1,2],[2,4],[3,5],[2,5], [4,5]]), [2,5])


assert_equal(find_redundant_connection_uf([[1,2], [1,3], [2,3]]), [2,3])
assert_equal(find_redundant_connection_uf([[1,2], [2,3], [3,4], [4,1], [1,5]]), [4,1])
