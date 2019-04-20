# @param {String[]} words
# @return {String}
# @note This uses DFS
def alien_order_dfs(words)
    return '' if !words || words.empty?
    return words[0].reverse() if words.size == 1 # So that pair-wise handling in build_graph doesn't break cuz 1 < a pair
    @graph, @visited, @on_stack, @result = {}, Set.new(), Set.new(), []
    build_graph(words)
    @graph.keys.each { |x| return '' if !@visited.include?(x) && has_cycle?(x) }
    @result.join('')
end

def build_graph(words)
    words.each_cons(2) { |w1, w2| return if !add_words_to_graph(w1, w2) }# Loop through every pair of words and add to graph
end

def add_words_to_graph(w1, w2)
    add_vertices(w1)
    add_vertices(w2)
    m, n = w1.size(), w2.size()
    min_length, found = [m, n].min, false
    0.upto(min_length - 1) do |i|                       # Ordering after the min length doesn't matter
        c1, c2 = w1[i], w2[i]
        next if c1 == c2                                # Skip matching chars
        @graph[c1].add(c2) if !@graph[c1].include?(c2)  # Add edge between w1[i] and w2[i] if it doesn't already exist
        found = true                                    # Found is a flag to show that we found an ordering
        break                                           # Break at the first mismatched character in the two words, cuz words are sorted
    end
    return false if !found && m > n                     # 'abstract', 'abs' is an error. But 'abs', 'abstract' is perfectly fine.
    true
end

def add_vertices(w)
    w.each_char { |c| @graph[c] = Set.new() if !@graph.key?(c) }
end

def has_cycle?(x)
    @visited.add(x)
    @on_stack.add(x)
    @graph[x].each do |nbr|
        return true if @on_stack.include?(nbr)
        return true if !@visited.include?(nbr) && has_cycle?(nbr)
    end
    @on_stack.delete(x)
    @result.unshift(x)
    false
end


# @note This uses BFS and Topological Sort using Kahn's Algorithm
# @param {String[]} words
# @return {String}
def alien_order_bfs(words)
    return '' if !words || words.empty?
    return words[0].reverse if words.size == 1
    @graph, @in_deg, result, q = {}, Array.new(26, 0), '', []
    build_graph_bfs(words)
    @graph.keys.each { |x| q.push(x) if @in_deg[x].zero? }
    while !q.empty?
        next_c = q.shift
        result += (next_c + 'a'.ord).chr
        @graph[next_c].each do |nbr|
            @in_deg[nbr] -= 1
            q.push(nbr) if @in_deg[nbr].zero?
        end
    end
    @graph.size != result.size ? '' : result
end

def build_graph_bfs(words)
    words.each_cons(2) do |w1, w2|
        return if !add_words_to_graph_bfs(w1, w2)
    end
end

def add_words_to_graph_bfs(w1, w2)
    add_vertices_bfs(w1)
    add_vertices_bfs(w2)
    m, n = w1.size, w2.size
    min_len, found = [m, n].min, false
    0.upto(min_len - 1) do |i|
        c1, c2 = w1[i].ord - 'a'.ord, w2[i].ord - 'a'.ord
        next if c1 == c2
        if !@graph[c1].include?(c2)
            @in_deg[c2] += 1
            @graph[c1].add(c2)
        end
        found = true
        break
    end
    
    return false if !found && m > n
    true
end

def add_vertices_bfs(w)
    w.each_char do |c|
        d = c.ord - 'a'.ord
        @graph[d] = Set.new if !@graph.key?(d)
    end
end

# 269. Alien Dictionary
# https://leetcode.com/problems/alien-dictionary/

# Key Insights
# 1. Word list is sorted lexicographically
# 2. We compare two words to get the lexi order of chars first mismatched chars
# 3. We don't use orderings within a word cuz some char may later appear in between those chars in a later word
# 3. If only one word, the the reverse is answer cuz its sorted

# Approach 1: Detecting cycle using DFS
# Steps:
# 1. Build graph by iterating through every pair of words consecutive words and compare
# 2. Compare characters upto first mismatch and break (Why? cuz below)
#    Bcuz first mismatch means there is an ordering from w1 to w2,
#    After the first mis-match the order doesn't mean any ordering,
#    bcuz the order of the words is governed by the first mis-match
# 3. Once you've built a graph, now for each now do a dfs and maintain a visited list
#    while also maintaining at every DFS call the list of nodes on stack, if there is a cycle,
#    One of the nodes on the stack would be visited while on stack, in such a case we return false
# 4. Finally we append to string from front, which is the direction of the order,
#    so first visited node would be last in the order

# Time: O(n), Worst case we iterate through ever char or every word, to build the graph
# Space: O(1), We store every char of every word as the graph,
#        which can be max of 26, neighbors can also only be max of 25

# Approach 2: Detecting cycle using BFS (Kahn's Algorithm)
# Steps;
# 1. Build graph in the same way as before as in DFS
# 2. Compare characters upto first mismatch as before
# 3. However, here we use the Kahn's method and build a in_degrees array
# 4. Use the array and push node with in_degree 0 to the Queue to start
# 5. At every stage we remove the visited node from graph,
#    causing the in degree of all neighbors to reduce by 1
# 6. At every iteration, we push all 0 in degree nodes to Queue
# 7. We end by comparing the visited array size (result size) with the graph size
#    Unequal graph and visited sizes means there was a cycle and hence we return ''
#    Equal graph and visited sizes means all nodes were visited and there was no cycle, thus giving us an ordering

# Time: O(n), Worst case we iterate through ever char or every word, to build the graph
# Space: O(1), We store every char of every word as the graph,
#        which can be max of 26, neighbors can also only be max of 25

require 'set'
require 'test/unit'
extend Test::Unit::Assertions

assert_equal(alien_order_dfs(["z", "x"]), "zx")
assert_equal(alien_order_dfs(["z","z"]), "z")
assert_equal(alien_order_dfs(["z", "x", "z"]), "")
assert_equal(alien_order_dfs(["aac","aabb","aaba"]), "cba")
assert_equal(alien_order_dfs(["wnlb"]), "blnw")
assert_equal(alien_order_dfs(["wrt","wrf","er","ett","rftt"]), "wertf")
assert_equal(alien_order_dfs(["wrt","wrf","er","ett","rftt","te"]), "wertf")

assert_equal(alien_order_bfs(["z", "x"]), "zx")
assert_equal(alien_order_bfs(["z","z"]), "z")
assert_equal(alien_order_bfs(["z", "x", "z"]), "")
assert_equal(alien_order_bfs(["aac","aabb","aaba"]), "cba")
assert_equal(alien_order_bfs(["wnlb"]), "blnw")
assert_equal(alien_order_bfs(["wrt","wrf","er","ett","rftt"]), "wertf")
assert_equal(alien_order_bfs(["wrt","wrf","er","ett","rftt","te"]), "wertf")
