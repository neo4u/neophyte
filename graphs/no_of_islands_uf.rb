

def cc(grid, m, n)

end

# @param {Character[][]} grid
# @return {Integer}
def num_islands(grid)
  return 0 if grid.nil? || grid.empty?
  m, n = grid.size, grid[0].size
  # puts "m: #{m} | n: #{n}"
  cc(grid, m, n)
end

grid = ["11110", "11010", "11000", "00000"]
puts num_islands(grid)

grid2 = ['100','000', '001']
puts num_islands(grid2)

grid3 = ["111111", "100001", "101101", "100001", "111111"]
puts num_islands(grid3)
