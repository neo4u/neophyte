def dfs(graph, start):
	visited, stack = set(), [start]
	while stack:
		vertex = stack.pop()
		if vertex not in visited:
			visited.add(vertex)
			stack.extend(graph[vertex] - visited)
	return visited

def dfs_recursive(graph, start, visited=None):
	if visited is None:
		visited = set()
	visited.add(start)
	for vertex in graph[start] - visited:
		dfs_recursive(graph, vertex, visited)
	return visited

def bfs(graph, start):
	visited, queue = set(), [start]
	while queue:
		vertex = queue.pop(0)
		if vertex not in visited:
			visited.add(vertex)
			queue.extend(graph[vertex] - visited)
	return visited

# def bfs_recursive(graph, start, visited=None):
def bfs_recursive(graph, start, visited=None, neighbours=None):
	if visited is None:
		visited = {start}

	if neighbours is None:
		neighbours = [start]
	elif neighbours == []:
		return

	while neighbours:
		vertex = neighbours.pop()
		visited.add(vertex)
		neighbours += graph[vertex] - visited

	bfs_recursive(graph, None, visited, neighbours)
	return visited

def bfs_paths(graph, start, end):
	"""
		Something
	"""
	queue = [(start, [start])]
	while queue:
		(vertex, path) = queue.pop(0)
		for next in graph[vertex] - set(path):
			if next == end:
				yield path + [next]
			else:
				queue.append((next, path + [next]))

def dfs_paths_recursive(graph, start, goal, path=None):
	if path is None:
		path = [start]
	if start == goal:
		yield path
	for next in graph[start] - set(path):
		yield dfs_paths_recursive(graph, next, goal, path + [next])

def dfs_paths(graph, start, end):
	stack = [(start, [start])]
	paths = []
	shortest = None
	while stack:
		(vertex, path) = stack.pop()
		for next in graph[vertex] - set(path):
			if next == end:
				curr_path = path + [next]
				paths.append(curr_path)
				if (not shortest) or len(shortest) > len(curr_path):
					shortest = curr_path
			else:
				stack.append((next, path + [next]))
	
	return paths, shortest

def dijkstra(graph, src, dest, visited=[], distances={}, predecessors={}):
	"""
	calculates a shortest path tree routed in src
	"""
	# a few sanity checks
	if src not in graph:
		raise TypeError('The root of the shortest path tree cannot be found')
	if dest not in graph:
		raise TypeError('The target of the shortest path cannot be found')
	# ending condition
	if src == dest:
		# We build the shortest path and display it
		path = []
		pred = dest
		while pred != None:
			path.append(pred)
			pred = predecessors.get(pred, None)
		print('shortest path: ' + str(path) + " cost=" + str(distances[dest]))
	else:
		# if it is the initial  run, initializes the cost
		if not visited:
			distances[src] = 0
		# visit the neighbors
		for neighbor in graph[src]:
			if neighbor not in visited:
				new_distance = distances[src] + graph[src][neighbor]
				if new_distance < distances.get(neighbor, float('inf')):
					distances[neighbor] = new_distance
					predecessors[neighbor] = src
		# mark as visited
		visited.append(src)
		# now that all neighbors have been visited: recurse
		# select the non visited node with lowest distance 'x'
		# run Dijskstra with src='x'
		unvisited = {}
		for k in graph:
			if k not in visited:
				unvisited[k] = distances.get(k, float('inf'))
		x = min(unvisited, key=unvisited.get)
		dijkstra(graph, x, dest, visited, distances, predecessors)

graph = { 
	's': {'a': 2, 'b': 1},
	'a': {'s': 3, 'b': 4, 'c':8},
	'b': {'s': 4, 'a': 2, 'd': 2},
	'c': {'a': 2, 'd': 7, 't': 4},
	'd': {'b': 1, 'c': 11, 't': 5},
	't': {'c': 3, 'd': 5}
}
dijkstra(graph, 's', 't')

# graph = {
# 	'A': set(['B', 'C']),
# 	'B': set(['A', 'D', 'E']),
# 	'C': set(['A', 'F']),
# 	'D': set(['B']),
# 	'E': set(['B', 'F']),
# 	'F': set(['C', 'E'])
# }

# print(dfs(graph, 'A'))
# print(dfs_paths(graph, 'A', 'D'))
# print(dfs(graph, 'C'))
# print(dfs_recursive(graph, 'A'))
# print(list(dfs_paths_recursive(graph, 'C', 'F')))

# print(bfs(graph, 'A'))
# print(bfs_recursive(graph, 'A'))
# print()

# print(list(bfs_paths(graph, 'A', 'F')))