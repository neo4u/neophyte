#!/bin/ruby

require 'set'

def get_cost(n, m, cl, cr, adj_list)
  return n * cl if cl <= cr
  visited = {}
  total_cost = 0
  (1..n).each do |i|
    next if visited[i]
    # Cover all nodes using dfs and check the size of component the current vextex is in
    connected_grid_size = dfs(i, adj_list, visited)
    # Add 1 library per component of the graph
    total_cost += ((connected_grid_size - 1) * cr) + cl
  end

  total_cost
end

def dfs(i, adj_list, visited)
  visited[i] = 1
  connected_grid_size = 1
  if adj_list[i] && !adj_list.empty?
    adj_list[i].each do |k, v|
      connected_grid_size += dfs(k, adj_list, visited) unless visited[k]
    end
  end
  connected_grid_size
end

# q = gets.strip.to_i
# costs = []
# q.times do
#   n, m, cl, cr = gets.strip.split.map(&:to_i)
#   adj_list = {}
#   m.times do
#     u, v = gets.strip.split.map(&:to_i)
#     adj_list[u] ||= Set.new
#     adj_list[v] ||= Set.new
#     adj_list[u].add(v)
#     adj_list[v].add(u)
#   end

#   costs << get_cost(n, m, cl, cr, adj_list)
# end

# costs.each { |cost| puts cost }
