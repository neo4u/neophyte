require 'set'

# All of these are sequences of vertices and edges. They have the following properties:
# 1. Walk    : Vertices may repeat. Edges may repeat (Closed or Open)
# 2. Trail   : Vertices may repeat. Edges cannot repeat (Open)
# 3. Circuit : Vertices may repeat. Edges cannot repeat (Closed)
# 4. Path    : Vertices cannot repeat. Edges cannot repeat (Open)
# 5. Cycle   : Vertices cannot repeat. Edges cannot repeat (Closed)

def dfs(graph, start, visited = nil)
	visited.nil? ? visited = Set.new([start]) : visited.add(start)

	graph[start].each do |node|
		dfs(graph, node, visited) unless visited.inclue?(node)
	end

	visited
end

def connected_components(graph)
	visited, components = Set.new, []

	graph.keys.each do |node|
	  components << dfs(graph, node, visited) unless visited.include?(node)
	end

	components
end

def dfs_paths_enumerate(graph, src, dst, visited, paths = nil)
	visited.nil? ? visited = Set.new([src]) : visited.add(node)
	paths = [] if paths.nil?

	return paths << visited.to_a if src == dst

	graph[src].each do |node|
		dfs_paths_enumerate(graph, node, dst, visited, paths) unless visited.include?(node)
	end

	paths
end

def dfs_shortest_path(graph, src, dst, path = nil, shortest = nil)
	visited.nil? ? visited = Set.new([src]) : visited.add(node)
	shorest = path if src == dst && shortest.nil? || path.size < shortest.size

	graph[src].each do |node|
		dfs_shortest_path(graph, node, dst, visited, shortest) unless visited.include?(node)
	end

	shorest
end
