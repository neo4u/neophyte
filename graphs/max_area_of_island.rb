# @param {Integer[][]} grid
# @return {Integer}
def max_area_of_island(grid)
  m, n = grid.count, grid[0].count
  return 0 if grid.empty?
  max_area = 0

  0.upto(m - 1) do |i|
    0.upto(n - 1) do |j|
      if grid[i][j] == 1
        @area = 0
        dfs(grid, i, j)
        max_area = @area if @area > max_area
      end
    end
  end

  max_area
end

def dfs(grid, i, j)
  m, n = grid.count, grid[0].size
  return if grid[i][j] == 0

  @area += 1
  grid[i][j] = 0

  dfs(grid, i + 1, j) if i < m - 1
  dfs(grid, i - 1, j) if i > 0
  dfs(grid, i, j + 1) if j < n - 1
  dfs(grid, i, j - 1) if j > 0
end

puts max_area_of_island