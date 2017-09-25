require 'set'
def dfs(graph, start)
  visited, stack = Set.new, [start]

  until stack.empty?
    vertex = stack.pop
    unless visited.include?(vertex)
      visited.add(vertex)
      stack += (graph[vertex] - visited).to_a
    end
  end

  visited.to_a
end
