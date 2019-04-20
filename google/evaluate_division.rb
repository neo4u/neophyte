# Approach 1: DFS
# @param {string[][]} equations
# @param {Float[]} values
# @param {string[][]} queries
# @return {Float[]}
def calc_equation_dfs(equations, values, queries)
    @graph = Hash.new { |h, k| h[k] = Set.new() }
    @weights = Hash.new { |h, k| h[k] = 0.0 }
    @result_list = []

    equations.zip(values) do |edge, w|
        a, b = edge
        @graph[a].add(b); @graph[b].add(a)
        @weights[[a, b]], @weights[[b, a]] = w, 1.0 / w
    end

    queries.each do |x, y|
        @dfs_path, visited = -1.0, Set.new()
        dfs(x, y, visited, 1.0)
        @result_list.push(@dfs_path)
    end

    @result_list
end


def dfs(src, dst, visited, path)
    if src == dst && @graph.key?(src)
        @dfs_path = path
        return
    end

    return if visited.include?(src)
    visited.add(src)

    @graph[src].each do |node|
        dfs(node, dst, visited, path * @weights[[src, node]])
    end
end

# Approach 2: BFS
# @param {string[][]} equations
# @param {Float[]} values
# @param {string[][]} queries
# @return {Float[]}
def calc_equation_bfs(equations, values, queries)
    graph = build_graph(equations, values)
    queries.map { |q| find_path(graph, q) }
end

def build_graph(equations, values)
    graph = {}
    equations.zip(values) do |edge, value|
        f, t = edge
        add_edge(graph, f, t, value)
        add_edge(graph, t, f, 1.0 / value)
    end

    graph
end

def add_edge(graph, f, t, value)
    if graph.key?(f)
        graph[f].push([t, value])
    else
        graph[f] = [[t, value]]
    end
end

def find_path(graph, query)
    b, e = query
    return -1.0 if !graph.key?(b) || !graph.key?(e)
    q, visited = [[b, 1.0]], Set.new()

    while !q.empty?
        front, cur_product = q.shift()
        return cur_product if front == e
        visited.add(front)

        graph[front].each do |neighbor, value|
            next if visited.include?(neighbor)
            q.push([neighbor, cur_product * value])
        end
    end

    -1.0
end

class DisjointSet
    def initialize(parent, weight)
        @parent = parent
        @weight = weight
    end

    def find(v)
        return v if @parent[v] == v
        root = find(@parent[v])
        @weight[v] *= @weight[@parent[v]]
        @parent[v] = root

        root
    end

    def union(v1, v2, val)
        root1, root2 = find(v1), find(v2)
        @weight[root1] = @weight[v2] * val / @weight[v1]
        @parent[root1] = root2
    end
end

# Approach 3: Union-Find
# @param {string[][]} equations
# @param {Float[]} values
# @param {string[][]} queries
# @return {Float[]}
def calc_equation_uf(equations, values, queries)
    result, parent, weight = [], {}, {}
    ds = DisjointSet.new(parent, weight)

    equations.each_with_index do |edge, i|
        x1, x2 = edge
        val = values[i]

        if !parent.include?(x1) && !parent.include?(x2)
            parent[x1], parent[x2] = x2, x2
            weight[x1], weight[x2] = val, 1.0
        elsif !parent.include?(x1)
            parent[x1] = x2
            weight[x1] = val
        elsif !parent.include?(x2)
            parent[x2] = x1
            weight[x2] = 1.0 / val
        else
            ds.union(x1, x2, val)
        end
    end

    queries.each do |x1, x2|
        if !parent.include?(x1) || !parent.include?(x2) || ds.find(x1) != ds.find(x2)
            result.push(-1.0)
        else
            factor1 = weight[x1]
            factor2 = weight[x2]
            result.push(factor1 / factor2)
        end
    end

    result
end


# 399. Evaluate Division
# https://leetcode.com/problems/evaluate-division/description/

# Key Insights
# 1. A series of equations A / B = k can be seen as a graph
# 2. Nodes on either sides of an edge are the dividend and divisor A and B
# 3. The weight of the edge itself is the result of the division.
# 4. Hence, we create the graph and traverse it with DFS/BFS/DSUF to get our result.


# Approach 1: DFS
# Steps:
# 1. Iterate through the given equations and
#    build a directed graph (hash with dividend as key and a set of divisors as values)
#    and with a hash of weights (hash with list of [a, b] as key and weight of the edge as the value)
# 2. Iterate through the queries (x, y) and do a path_finding using dfs from x (src) to y (dst)
# 3. The key bit is path

# Complexity is K * O(N + M) where N and M are the number of nodes and edges,
# and K is the number of queries.
# How many nodes can we have? It's 2 * E,
# where E is the number of equations (2 different nodes per each equation).
# We can have at most E edges in the graph.

# So total complexity is O(K * E), with O(E) additional space for the graph.


# Approach 2: BFS
# This is the simplest and most elegant solution IMO.
# Regarding the time complexity, if there are m queries, q equations and n distinct values,
# the without optimization, by definition of BFS, it will be O(m(q+n)) ~ O(m * n^2)
# as q can grow to the order of n^2.
# After optimization you suggested, I think it will be O(q+n) ~ O(n^2)
# for all the m queries as we traverse each path at most once during all the queries,
# so I the the amortized time complexity will be O(n^2/m)..


# Approach 3: Union-Find or Disjoint Set
# each operation of UnionFind costs nearly O(1) (according to wiki) 
# when using both path compression and union-by-rank.
# but this problem naturally can't use union-by-rank.
# The find and union operation can costs up to O(V)
# if the tree like a linklist in worst case.
# Therefore, the time should be O(E)O(V) + O(Q)O(V),
# where E stands for equations, Q for queries,
# and V for vertices number. Since V <= 2E,
# the worst time complexity is O(EE + QE).
# space: O(E)


require 'set'
require 'test/unit'
extend Test::Unit::Assertions

equations = [["a", "b"], ["b", "c"]]
values = [2.0, 3.0]
queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
assert_equal(
    calc_equation_dfs(equations, values, queries),
    [6.0, 0.5, -1.0, 1.0, -1.0]
)
assert_equal(
    calc_equation_bfs(equations, values, queries),
    [6.0, 0.5, -1.0, 1.0, -1.0]
)
assert_equal(
    calc_equation_uf(equations, values, queries),
    [6.0, 0.5, -1.0, 1.0, -1.0]
)

equations = [["a","b"],["e","f"],["b","e"]]
values = [3.4,1.4,2.3]
queries = [["b","a"],["a","f"],["f","f"],["e","e"],["c","c"],["a","c"],["f","e"]]
assert_equal(
    calc_equation_dfs(equations, values, queries),
    [0.29411764705882354,10.947999999999999,1.0,1.0,-1.0,-1.0,0.7142857142857143]
)
assert_equal(
    calc_equation_bfs(equations, values, queries),
    [0.29411764705882354,10.947999999999999,1.0,1.0,-1.0,-1.0,0.7142857142857143]
)
assert_equal(
    calc_equation_uf(equations, values, queries),
    [0.29411764705882354,10.947999999999999,1.0,1.0,-1.0,-1.0,0.7142857142857143]
)
