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

def dfs_recursive(graph, start, visited = nil)
  visited ||= Set.new
  visited.add(start)
  (graph[start] - visited).to_a.each do |vertex|
    dfs_recursive(graph, vertex, visited)
  end

  visited.to_a
end

def dfs_paths(graph, src, dst)
  stack = [[src, [src]]] # Current vertex and path upto the curr vertex
  paths = []
  shortest = nil

  until stack.empty?
    vertex, path = stack.pop
    (graph[vertex] - Set.new(path)).to_a.each do |next_vertex|
      if next_vertex == dst
        curr_path = path + [next_vertex]
        paths.push(curr_path)
        shortest = curr_path if shortest.nil? || shortest.size > curr_path.size
      else
        stack.push([next_vertex, path + [next_vertex]])
      end
    end
  end

  [paths, shortest]
end

def bfs(graph, start)
  visited, queue = Set.new, [start]
  until queue.empty?
    puts "visited: #{visited.to_a} | queue: #{queue}"
    vertex = queue.shift
    unless visited.include?(vertex)
      visited.add(vertex)
      queue += (graph[vertex] - visited).to_a
    end
  end

  visited.to_a
end

def bfs_recursive(graph, start, visited = nil, neighbours = nil)
  visited = Set.new([start]) if visited.nil?

  neighbours = [start] if neighbours.nil?
  return if neighbours.empty?

  until neighbours.empty?
    vertex = neighbours.shift
    visited.add(vertex)
    neighbours += (graph[vertex] - visited).to_a
  end
  bfs_recursive(graph, nil, visited, neighbours)

  visited.to_a
end

graph = {
  'A' => Set.new(['B', 'C']),
  'B' => Set.new(['A', 'D', 'E']),
  'C' => Set.new(['A', 'F']),
  'D' => Set.new(['B']),
  'E' => Set.new(['B', 'F']),
  'F' => Set.new(['C', 'E'])
}

# # p(dfs(graph, 'A'))
# # p(dfs_recursive(graph, 'A'))
# print(dfs_paths(graph, 'A', 'D'))
# # print(dfs(graph, 'C'))
# # print(dfs_recursive(graph, 'A'))
# # print(list(dfs_paths_recursive(graph, 'C', 'F')))

p(bfs(graph, 'A'))
p(bfs_recursive(graph, 'A'))
p()
