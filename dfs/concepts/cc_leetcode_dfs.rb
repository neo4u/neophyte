def dfs(graph, src, visited)
  visited[src] = true
  graph[src].each { |v| dfs(graph, v, visited) unless visited[v] }
end

def cc(n, graph)
  visited = [false] * n
  count = 0

  0.upto(n - 1) do |v|
    next if visited[v]
    count += 1
    dfs(graph, v, visited)
  end

  count
end

def count_components(n, edges)
  graph = Array.new(n) { [] }
  edges.each do |u, v|
    graph[u] << v
    graph[v] << u
  end

  cc(n, graph)
end

# puts count_components(5, [[0, 1], [1, 2], [2, 3], [3, 4]])