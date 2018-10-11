# @param {String[]} words
# @return {String}
# @note This uses DFS
def alien_order(words)
    return "" if !words || words.empty?
    graph = build_graph(words)

    visited, visiting, result = Set.new(), Set.new(), []
    graph.keys.each do |node|
        return '' if !visited.include?(node) && has_cycle_topo_dfs?(node, graph, visited, visiting, result)
    end

    result.reverse!().join('')
end

def build_graph(words)
    graph = {}
    0.upto(words.size() - 2) do |i|
        w1, w2 = words[i], words[i + 1]
        return {} if !add_words_to_graph(graph, w1, w2)
    end
    add_vertices(words.last, graph)
    graph
end

def has_cycle_topo_dfs?(x, g, visited, visiting, result)
    visited.add(x)
    visiting.add(x)
    g[x].each do |neighbor|
        return true if visiting.include?(neighbor)
        return true if !visited.include?(neighbor) && has_cycle_topo_dfs?(neighbor, g, visited, visiting, result)
    end
    visiting.delete(x)
    result.push(x)
    false
end

def add_words_to_graph(graph, w1, w2)
    add_vertices(w1, graph)
    add_vertices(w2, graph)
    m, n = w1.size(), w2.size()
    min_length, found = [m, n].min, false

    0.upto(min_length - 1) do |i|   # Ordering after the min length doesn't matter
        next if w1[i] == w2[i]      # Skip matching chars
        graph[w1[i]].add(w2[i])     # Add edge between w1[i] and w2[i]
        found = true
        break
    end

    return false if !found && m > n # 'abstract', 'abs' is an error. But 'abs', 'abstract' is perfectly fine.
    true
end

def add_vertices(w, graph)
    w.each_char do |c|
        graph[c] = Set.new() if !graph.include?(c)
    end
    # Modified by reference, no need for return
end

# @note This uses BFS
# @param {String[]} words
# @return {String}
def alien_order2(words)
    graph, in_degree = {}, Array.new(26, 0)

    init_graph(words, graph, in_degree)
    add_edges(words, graph, in_degree)

    q, result = [], ''
    0.upto(25) do |i|
        q.push(i) if in_degree[i] == 0 && graph.include?(i)
    end

    while !q.empty?
        next_c = q.shift()
        result += (next_c + 'a'.ord).chr
        greater_set = graph[next_c]

        greater_set.each do |greater|
            in_degree[greater] -= 1
            q.push(greater) if in_degree[greater] == 0
        end
    end

    graph.size() != result.size() ? '' : result
end

def init_graph(words, graph, in_degree)
    # Initialize the graph and 
    words.each do |word|
        word.each_char do |c|
            key = c.ord - 'a'.ord
            in_degree[key] = 0
            graph[key] = Set.new()
        end
    end
end

def add_edges(words, graph, in_degree)
    0.upto(words.size - 2) do |i|
        w1, w2 = words[i], words[i + 1]
        m, n = w1.size(), w2.size()
        min_len = [m, n].min
        0.upto(min_len - 1) do |j|
            next if w1[j] == w2[j]
            k1 = w1[j].ord - 'a'.ord
            k2 = w2[j].ord - 'a'.ord
            count = in_degree[k2]
            if !graph[k1].include?(k2)
                in_degree[k2] = count + 1
                graph[k1].add(k2)
            end
            break
        end
    end
end

require 'set'
require 'test/unit'
extend Test::Unit::Assertions

# 269. Alien Dictionary
# https://leetcode.com/problems/alien-dictionary/

# Definition of lexicographical
# Lexicographical order is defined in following way. When we compare s and t,
# first we find the leftmost position with differing characters: si ≠ ti.
# If there is no such position (i. e. s is a prefix of t or vice versa) the shorter string is lower in order.
# Otherwise, we compare characters si and ti according to their order in alphabet.

assert_equal(alien_order(["z", "x"]), "zx")
assert_equal(alien_order(["z", "x", "z"]), "")
assert_equal(alien_order(["aac","aabb","aaba"]), "cba")
assert_equal(alien_order(["wnlb"]), "blnw")
assert_equal(alien_order(["wrt","wrf","er","ett","rftt"]), "wertf")
assert_equal(alien_order(["wrt","wrf","er","ett","rftt","te"]), "wertf")

assert_equal(alien_order2(["z", "x"]), "zx")
assert_equal(alien_order2(["z", "x", "z"]), "")
assert_equal(alien_order2(["aac","aabb","aaba"]), "cba")
assert_equal(alien_order2(["wnlb"]), "blnw")
assert_equal(alien_order2(["wrt","wrf","er","ett","rftt"]), "wertf")
assert_equal(alien_order2(["wrt","wrf","er","ett","rftt","te"]), "wertf")

