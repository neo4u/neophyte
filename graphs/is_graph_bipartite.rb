# @param {Integer[][]} graph
# @return {Boolean}
def is_bipartite(graph)
    color, n = {}, graph.size

    0.upto(n - 1) do |node|
        next if color.key?(node)
        stack = [node]
        color[node] = 0

        while !stack.empty?
            node = stack.pop()

            graph[node].each do |v|
                if !color.key?(v)
                    stack.push(v)
                    color[v] = color[node] ^ 1
                elsif color[v] == color[node]
                    return false
                end
            end
        end
    end

    true
end

# 785. Is Graph Bipartite?
# https://leetcode.com/problems/is-graph-bipartite/

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(is_bipartite([[1,3],[0,2],[1,3],[0,2]]), true)


