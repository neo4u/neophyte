require 'set'

def bfs(graph, start)
    visited, queue = Set.new, [start]

    while !queue.empty?
        node = queue.shift
        next if visited.include?(node)
        visited.add(node)
        queue += (graph[node] - visited).to_a
    end

    visited
end

# Graph is a hash with node label as key and neighbours list as a value