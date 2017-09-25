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

  visited
end

def dfs_recursive(graph, start, visited = nil)
  visited = Set.new([start]) if visited.nil?
  (graph[start] - visited).to_a.each { |v| dfs_recursive(graph, v, visited) }

  visited
end

def dfs_paths(graph, src, dst)
  return [src, [src]] if src == dst # Trivial case of src being the destination
  stack = [[src, [src]]]            # [vertex, path up to the vertex]
  paths, shortest = [], nil         # Init the paths and shortest path

  until stack.empty?
    vertex, path = stack.pop
    (graph[vertex] - Set.new(path)).to_a.each do |v|
      curr_path = path + [v]
      if v == dst
        paths << curr_path
        shortest = curr_path if shortest.nil? || shortest.size > curr_path.size
      else
        stack.push([v, curr_path])
      end
    end
  end

  [paths, shortest]
end

def dfs_paths_recursive(graph, src, dst, path = nil, paths_shortest = nil)
  path = [src] if path.nil?
  paths_shortest = [[], nil] if paths_shortest.nil?

  if src == dst
    paths_shortest[0] << path
    paths_shortest[1] = path if paths_shortest[1].nil? || paths_shortest[1].size > path.size
    return paths_shortest
  end

  (graph[src] - Set.new(path)).to_a.each do |v|
    dfs_paths_recursive(graph, v, dst, path + [v], paths_shortest)
  end

  paths_shortest
end

def check_component(v, components)
  components.each_with_index { |c, idx| return idx + 1 if c.include?(v) }

  nil
end

def connected_components(graph)
  vertices = graph.keys()
  components = []
  vertices.each do |v|
    components << dfs(graph, v).to_a.sort if check_component(v, components).nil?
  end

  components
end

# p(connected_components(graph))
