require 'set'

# All of these are sequences of vertices and edges. They have the following properties:
# 1. Walk    : Vertices may repeat. Edges may repeat (Closed or Open)
# 2. Trail   : Vertices may repeat. Edges cannot repeat (Open)
# 3. Circuit : Vertices may repeat. Edges cannot repeat (Closed)
# 4. Path    : Vertices cannot repeat. Edges cannot repeat (Open)
# 5. Cycle   : Vertices cannot repeat. Edges cannot repeat (Closed)

def dfs(graph, start, visited = nil)
  visited.nil? ? visited = Set.new([start]) : visited.add(start)

  graph[start].to_a.each do |v|
    dfs(graph, v, visited) unless visited.include?(v)
  end

  visited
end

def dfs_paths(graph, src, dst, path = nil, paths_shortest = nil)
  path = [src] if path.nil?
  paths_shortest = [[], nil] if paths_shortest.nil?

  if src == dst
    paths_shortest[0] << path
    paths_shortest[1] = path if paths_shortest[1].nil? || paths_shortest[1].size > path.size
    return paths_shortest
  end

  (graph[src] - Set.new(path)).to_a.each do |v|
    dfs_paths(graph, v, dst, path + [v], paths_shortest)
  end

  paths_shortest
end

def connected_components(graph)
  visited, components = Set.new, []

  graph.keys.each do |v, _|
    components << dfs(graph, v, visited).to_a.sort unless visited.include?(v)
  end

  components
end

# -------------------------------------------------------------------------------
# If the distance between the node and the
# neighbour is lower than the one I have now
# -------------------------------------------------------------------------------
def relax(graph, u, v, d, p)
  puts "d[v]: #{d[v]}| d[u]: #{d[u]} | graph[u][v]: #{graph[u][v]}"
  if d[v] > d[u] + graph[u][v] # Relaxation Property
    d[v] = d[u] + graph[u][v]
    p[v] = u
  else
    puts "can't relax"
    return
  end
end

def init_single_source(graph, src)
  d = {}                      # Stands for destination
  p = {}                      # Stands for predecessor
  graph.each do |v, _|
    d[v] = Float::INFINITY    # Set all nodes are far from src
    p[v] = nil                # Initially they don't have any preds
  end
  d[src] = 0                  # For the source we know how to reach
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
  d, p = init_single_source(graph, src)

  # Run this until is converges
  0.upto(graph.size - 1) do |_|
    graph.each do |u|
      graph[u].each do |v|        # For each neighbour of u
        relax(graph, u, v, d, p)  # Relax it
      end
    end
  end

  graph.each do |u|
    graph[u].each do |v|
      return nil if d[v] > d[u] + graph[u][v]
    end
  end

  [d, p]
end

def extract_min(q, d)
  min = [nil, Float::INFINITY]
  q.each do |k|
    min = [k, d[k]] if d[k] < min[1]
  end
  q.delete(min[0])

  min[0]
end

def dijstra_all_v(graph, src)
  d, p = init_single_source(graph, src)

  q = graph.keys

  until q.empty?
    u = extract_min(q, d) # Must use priority queue here for optimization
    graph[u].keys.each do |v|
      relax(graph, u, v, d, p)
    end
  end

  [d, p]
end

def dijkstra(graph, src, dst, visited = nil, d = {}, p = {})
  puts "dijstra called with src: #{src} | dst: #{dst}"
  # http://www.gilles-bertrand.com/2014/03/dijkstra-algorithm-python-example-source-code-shortest-path.html
  raise TypeError('The root of the shortest path tree cannot be found') unless graph.include?(src)
  raise TypeError('The target of the shortest path cannot be found') unless graph.include?(dst)
  visited ||= Set.new()
  if src == dst
    # We build the shortest path and display it
    path, pred = [], dst
    until pred.nil?
      path.push(pred)
      pred = p.fetch(pred, nil)
    end
    return [path, d[dst]]
  end

  d[src] = 0 if visited.empty?
  # visit the neighbors
  (graph[src].keys - visited.to_a).each do |v|
    puts "v is: #{v} | src is: #{src} | d[src] is: #{d[src]} | graph[src][v] is: #{graph[src][v]}"
    # next if visited.include?(neighbor)
    new_distance = d[src] + graph[src][v]
    if new_distance < d.fetch(v, Float::INFINITY)
      d[v] = new_distance
      p[v] = src
    end
  end

  visited.add(src)
  unvisited = {}
  graph.each do |k, _|
    unvisited[k] = d.fetch(k, Float::INFINITY) unless visited.include?(k)
  end
  x = unvisited.group_by { |_, v| v }.min_by { |k, _| k }.last.first[0]
  dijkstra(graph, x, dst, visited, d, p)
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
#   'a' => { 'b' => -1, 'c' =>  4 },
#   'b' => { 'c' =>  3, 'd' =>  2, 'e' => 2 },
#   'c' => {},
#   'd' => { 'b' =>  1, 'c' => 5 },
#   'e' => { 'd' => -3 }
# }
# p dijstra_all_v(graph, 'a')
# p(connected_components(graph))









def dfs_iterative(graph, start)
	visited, stack = Set.new, [start]
  
	until stack.empty?
	  v = stack.pop
	  visited.add(v)
	  stack += (graph[v] - visited).to_a
	end
  
	visited
  end

def dfs_paths_iterative(graph, src, dst)
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