require 'set'

# All of these are sequences of vertices and edges. They have the following properties:
# 1. Walk    : Vertices may repeat. Edges may repeat (Closed or Open)
# 2. Trail   : Vertices may repeat. Edges cannot repeat (Open)
# 3. Circuit : Vertices may repeat. Edges cannot repeat (Closed)
# 4. Path    : Vertices cannot repeat. Edges cannot repeat (Open)
# 5. Cycle   : Vertices cannot repeat. Edges cannot repeat (Closed)

def dfs_iterative(graph, start)
  visited, stack = Set.new, [start]

  until stack.empty?
    v = stack.pop()
    visited.add(v)
    stack += (graph[v] - visited).to_a
  end

  visited
end

def dfs(graph, start, visited = nil)
  visited.nil? ? visited = Set.new([start]) : visited.add(start)

  graph[start].each do |v|
    dfs(graph, v, visited) unless visited.include?(v)
  end

  visited
end

def dfs_paths_iterative(graph, src, dst)
  return [src, [src]] if src == dst
  stack = [[src, [src]]]
  paths, shortest = [], nil

  until stack.empty?
    vertex, path = stack.pop()
    (graph[vertex] - Set.new(path)).each do |v|
      curr_path = path + [v]
      if v == dst
        paths << curr_path
        shortest = curr_path if shortest.nil? || curr_path.size < shortest.size
      else
        stack.push([v, curr_path])
      end
    end
  end

  [paths, shortest]
end

def dfs_paths(graph, src, dst, path = nil, paths_shortest = nil)
  path = [src] if path.nil?
  paths_shortest = [[], nil] if paths_shortest.nil?

  if src == dst
    paths_shortest[0] << path
    paths_shortest[1] = path if paths_shortest[1].nil? || path.size < paths_shortest[1].size
    return paths_shortest
  end

  (graph[src] - Set.new(path)).each do |v|
    dfs_paths(graph, v, dst, path + [v], paths_shortest)
  end

  paths_shortest
end

def connected_components(graph)
  visited, components = Set.new, Set.new


  components.to_a
end

# -------------------------------------------------------------------------------
# If the distance between the node and the
# neighbour is lower than the one I have now
# -------------------------------------------------------------------------------
def relax(graph, u, v, d, p)

end

def init_single_source(graph, src)

  [d, p]
end

# -------------------------------------------------------------------------------
# Given a weighted, directed graph G(V,E) with source s and weight function w, the
# Bellman-Ford algorithm returns a boolean value indicating whether or not there is
# a negative-weight cycle that is reachable from the source. If there is such a cycle,
# the algorithm indicates that no solution exists. If there is no such cycle, the
# algorithm produces the shortest paths and their weights.
# Complexity: O(VE)
# -------------------------------------------------------------------------------
def bellman_ford(graph, src)

  [d, p]
end

# graph = {
#   's' => { 'a' => 2, 'b' => 1 },
#   'a' => { 's' => 3, 'b' => 4, 'c' => 8 },
#   'b' => { 's' => 4, 'a' => 2, 'd' => 2 },
#   'c' => { 'a' => 2, 'd' => 7, 't' => 4 },
#   'd' => { 'b' => 1, 'c' => 11, 't' => 5 },
#   't' => { 'c' => 3, 'd' => 5 }
# }
# p dijkstra(graph, 's', 't')

# graph = {
#   'a' => { 'b' => -1, 'c' =>	4 },
#   'b' => { 'c' =>	3, 'd' =>	2, 'e' => 2 },
#   'c' => {},
#   'd' => { 'b' =>	1, 'c' => 5 },
#   'e' => { 'd' => -3 }
# }
# p dijstra_all_v(graph, 'a')
# p(connected_components(graph))
