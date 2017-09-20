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
def bfs_recursive(graph, start, visited=None, children=None):
  if visited is None:
    visited = {start}

  if q is None:
    q = [start]
  elif q == []:
    return

  while children:
    vertex = q.pop()
    visited.add(vertex)
    q += graph[vertex] - visited

  bfs_recursive(graph, None, visited, q)
  return visited

def dfs_paths_recursive(graph, start, goal, path=None):
  if path is None:
    path = [start]
  if start == goal:
    yield path
  for next in graph[start] - set(path):
    yield from dfs_paths_recursive(graph, next, goal, path + [next])

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

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

# print(dfs(graph, 'A'))
# print(dfs_paths(graph, 'A', 'D'))
# print(dfs(graph, 'C'))
# print(dfs_recursive(graph, 'A'))
# print(list(dfs_paths_recursive(graph, 'C', 'F')))

print(bfs(graph, 'A'))
print(bfs_recursive(graph, 'A'))
print()
