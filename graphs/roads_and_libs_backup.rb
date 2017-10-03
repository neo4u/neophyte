#!/bin/ruby

def dfs(g, v, visited)
  visited[v] = true
  roads = 0
  #puts "at #{v}"
  g[v].each do |w|
      if not visited[w]
          roads += dfs(g, w, visited) + 1
      end
  end
  return roads
end

def cc(g, clib, croad)
  p g
  visited = Array.new(g.size, false)

  nlibs, nroads = 0, 0
  for v in (1..g.size-1)
    if not visited[v]
      nroads += dfs(g, v, visited)
      nlibs += 1
    end
  end
  puts "libs:#{nlibs}  roads:#{nroads}"
  return clib*nlibs + croad*nroads
end

q = gets.strip.to_i
for a0 in (0..q-1)
  n, m, clib, croad = gets.strip.split.map(&:to_i)
  g = Array.new(n + 1) { Array.new }
  for i in (1..m)
    v, w = gets.strip.split.map(&:to_i)
    g[v] << w
    g[w] << v
  end

  if croad >= clib
    puts n*clib
  else
    puts cc(g, clib, croad)
  end
end