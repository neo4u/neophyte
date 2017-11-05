# #!/bin/ruby

# require 'set'

# def dfs(g, v, visited)
#   visited.add(v)
#   roads = 0
#   g[v].each do |w|
#     roads += dfs(g, w, visited) + 1 unless visited.include?(w)
#   end

#   roads
# end

# def cc(g, city_count, clib, croad)
#   visited = Set.new
#   nlibs, nroads = 0, 0
#   1.upto(city_count) { |i| g[i] = [] if g[i].nil? }
#   g.keys.each do |v|
#     if !visited.include?(v) && !g[v].nil?
#       nroads += dfs(g, v, visited)
#       nlibs += 1
#     end
#   end

#   clib * nlibs + croad * nroads
# end

# q = gets.strip.to_i
# (0..q - 1).each do |_|
#   n, m, clib, croad = gets.strip.split.map(&:to_i)
#   g = {}
#   0.upto(m - 1) do |_|
#     v, w = gets.strip.split.map(&:to_i)
#     g[v] ||= []
#     g[w] ||= []
#     g[v] << w
#     g[w] << v
#   end

#   if croad >= clib
#     puts n * clib
#   else
#     puts cc(g, n, clib, croad)
#   end
# end
