# require 'pp'

# def dfs(grid, m, n, i, j, visited)
#   # puts "dfs called with #{i}, #{j} | grid[i]: #{grid[i]}"
#   return if grid[i][j] == '0' || visited[i][j]
#   visited[i][j] = true
#   dfs(grid, m, n, i - 1, j, visited) if i > 0
#   dfs(grid, m, n, i + 1, j, visited) if i < m - 1
#   dfs(grid, m, n, i, j - 1, visited) if j > 0
#   dfs(grid, m, n, i, j + 1, visited) if j < n - 1
# end

# def cc(grid, m, n)
#   count = 0
#   visited = Array.new(m) { Array.new(n, false) }
#   0.upto(m - 1) do |i|
#     0.upto(n - 1) do |j|
#       next if grid[i][j] == '0' || visited[i][j]
#       dfs(grid, m, n, i, j, visited)
#       count += 1
#     end
#   end
#   puts count
#   count
# end

# # @param {Integer} m
# # @param {Integer} n
# # @param {Integer[][]} positions
# # @return {Integer[]}
# def num_islands2(m, n, positions)
#   result = []
#   grid = Array.new(m) { "0" * n }
#   positions.each do |i, j|
#     pp grid
#     # puts "i: #{i} | j: #{j}"
#     grid[i][j] = '1'
#     pp grid
#     result << cc(grid, m, n)
#   end

#   result
# end

# p num_islands2(3, 3, [[0,0], [0,1], [1,2], [2,1]])