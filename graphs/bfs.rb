require 'set'

def bfs(graph, start)
  visited, queue = Set.new, [start]

  until queue.empty?
    vertex = queue.shift
    unless visited.include?(vertex)
      visited.add(vertex)
      queue += (graph[vertex] - visited).to_a
    end
  end

  visited
end

def bfs_recursive(graph, start, visited = nil, to_visit = nil)
  visited = Set.new([start]) if visited.nil?

  to_visit = [start] if to_visit.nil?
  return if to_visit.empty?

  until to_visit.empty?
    vertex = to_visit.shift
    visited.add(vertex)
    to_visit += (graph[vertex] - visited).to_a
  end

  visited
end
