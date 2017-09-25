# require 'set'

# def dfs(graph, start)
#   visited, stack = Set.new, [start]

#   until stack.empty?
#     vertex = stack.pop
#     unless visited.include?(vertex)
#       visited.add(vertex)
#       stack += (graph[vertex] - visited).to_a # Yes. You can remove a list from a set.
#     end
#   end

#   visited
# end

# def dfs_recursive(graph, start, visited = nil)
#   visited ||= Set.new
#   visited.add(start)
#   (graph[start] - visited).to_a.each do |vertex|
#     dfs_recursive(graph, vertex, visited)
#   end

#   visited
# end

# def dfs_paths(graph, src, dst)
#   return [src, [src]] if src == dst
#   stack = [[src, [src]]]
#   paths, shortest = [], nil

#   until stack.empty?
#     vertex, path = stack.pop
#     (graph[vertex] - Set.new(path)).to_a.each do |v|
#       if v == dst
#         path += [v]
#         paths.push(path)
#         shortest = path if shortest.nil? || shortest.size > path.size
#       else
#         stack.push([v, path + [v]])
#       end
#     end
#   end

#   [paths, shortest]
# end

# # def dfs_paths_recursive(graph, start, goal, path=None):
# # 	if path is None:
# # 		path = [start]
# # 	if start == goal:
# # 		yield path
# # 	for next in graph[start] - set(path):
# # 		yield from dfs_paths_recursive(graph, next, goal, path + [next])

# def dfs_paths_recursive(graph, src, dst, path = nil, paths_shortest = nil)
#   path = [src] if path.nil?
#   paths_shortest = [[], nil] if paths_shortest.nil?

#   if src == dst
#     paths_shortest[0] << path
#     paths_shortest[1] = path if paths_shortest[1].nil? || paths_shortest[1].size > path.size
#     return paths_shortest
#   end

#   (graph[src] - Set.new(path)).to_a.each do |v|
#     dfs_paths_recursive(graph, v, dst, path + [v], paths_shortest)
#   end

#   paths_shortest
# end

# def bfs(graph, start)
#   visited, queue = Set.new, [start]
#   until queue.empty?
#     vertex = queue.shift
#     unless visited.include?(vertex)
#       visited.add(vertex)
#       queue += (graph[vertex] - visited).to_a
#     end
#   end

#   visited
# end

# # def bfs_paths(graph, start, end):
# # 	"""
# # 		Something
# # 	"""
# # 	queue = [(start, [start])]
# # 	while queue:
# # 		(vertex, path) = queue.pop(0)
# # 		for next in graph[vertex] - set(path):
# # 			if next == end:
# # 				yield path + [next]
# # 			else:
# # 				queue.append((next, [path + [next]))

# def bfs_paths(graph, src, dst)
#   return [src, [src]] if src == dst
#   queue = [[src, [src]]]
#   paths = []
#   shortest = nil

#   until queue.empty?
#     p(queue)
#     vertex, path = queue.shift
#     (graph[vertex] - Set.new(path)).to_a.each do |v|
#       curr_path = path + [v]
#       if v == dst
#         paths.push(curr_path)
#         shortest = curr_path if shortest.nil? || shortest.size > curr_path.size
#       else
#         queue.push([v, curr_path])
#       end
#     end
#   end

#   [paths, shortest]
# end

# def bfs_recursive(graph, start, visited = nil, neighbours = nil)
#   visited = Set.new([start]) if visited.nil?

#   neighbours = [start] if neighbours.nil?
#   return if neighbours.empty?

#   until neighbours.empty?
#     vertex = neighbours.shift
#     visited.add(vertex)
#     neighbours += (graph[vertex] - visited).to_a
#   end
#   bfs_recursive(graph, nil, visited, neighbours)

#   visited
# end

# graph = {
#   'A' => Set.new(['B', 'C']),
#   'B' => Set.new(['A', 'D', 'E']),
#   'C' => Set.new(['A', 'F']),
#   'D' => Set.new(['B']),
#   'E' => Set.new(['B', 'F']),
#   'F' => Set.new(['C', 'E']),
#   'G' => Set.new(['H', 'I']),
#   'H' => Set.new(['J', 'G']),
#   'I' => Set.new(['G', 'J']),
#   'J' => Set.new(['H', 'I'])
# }

# # p(dfs(graph, 'A'))
# # p(dfs_recursive(graph, 'A'))
# # print(dfs_paths(graph, 'A', 'D'))
# # print(dfs(graph, 'C'))
# # print(dfs_recursive(graph, 'A'))
# # p(bfs_paths(graph, 'A', 'F'))
# # p(dfs_paths_recursive(graph, 'A', 'C'))

# # p(bfs(graph, 'A').to_a)
# # p(bfs_recursive(graph, 'A').to_a)
# # p()

# def check_component(v, components)
#   components.each_with_index { |c, idx| return idx + 1 if c.include?(v) }

#   nil
# end

# def connected_components(graph)
#   vertices = graph.keys()
#   components = []
#   vertices.each do |v|
#     components << dfs(graph, v).to_a.sort if check_component(v, components).nil?
#   end

#   components
# end

# p(connected_components(graph))

