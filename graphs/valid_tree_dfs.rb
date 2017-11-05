# @param {Integer} n
# @param {Integer[][]} edges
# @return {Boolean}
def valid_tree(n, edges)
  return false if edges.size != n - 1
  g = 0.upto(n - 1).reduce({}) { |hash, i| hash.merge(i => []) }
  edges.each do |u, v|
    g[u] << v
    g[v] << u
  end
  visited = [false] * n
  dfs(g, 0, visited)
  visited.all?
end

# def dfs(g, src, visited)
#   visited[src] = true
#   g[src].each { |v| dfs(g, v, visited) unless visited[v] }
# end

# n, edges = 6, [[0, 1], [0, 2], [2, 5], [3, 4], [3, 5]]
# # n, edges =
# p valid_tree(n, edges)

# n, edges = 5, [[0,1],[0,2],[1,2],[2,3],[2,4]]
# p valid_tree(n, edges)
