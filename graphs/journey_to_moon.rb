require 'set'

def dfs(graph, start, visited = nil)
  count = 1
  visited.nil? ? visited = Set.new([start]) : visited.add(start)
  graph[start].to_a.each do |v|
    count += dfs(graph, v, visited) unless visited.include?(v)
  end

  count
end

def cc(g)
  visited = Set.new
  counts = []
  g.keys.each do |v|
    counts << dfs(g, v, visited) unless visited.include?(v)
  end
  counts
end

def total_combos(counts)
  sum = 0
  result = 0
  # counts.combination(2) do |a, b| Fails for case 11
  #   result += a * b
  # end

  counts.each do |size|
    result += sum * size
    sum += size
  end

  result
end

N, p = gets.split.map(&:to_i)
g = {}
p.times do
  u, v = gets.split.map(&:to_i)
  g[u] ||= Set.new
  g[v] ||= Set.new
  g[u].add(v)
  g[v].add(u)
end

0.upto(N - 1) do |i|
  g[i] = Set.new if g[i].nil?
end

counts = cc(g)
# p counts
puts total_combos(counts)

