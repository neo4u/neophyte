# @param {Integer[][]} grid
# @return {Integer}
def max_area_of_island(grid)
    m, n = grid.count, grid[0].count
    return 0 if grid.empty?
    max_area = 0

    0.upto(m - 1) do |i|
        0.upto(n - 1) do |j|
        next if grid[i][j] == 0
        @area = 0
        dfs(grid, i, j)
        max_area = @area if @area > max_area
      end
    end

    max_area
end

def dfs(grid, i, j)
    m, n = grid.size, grid[0].size
    return if grid[i][j] == 0
    grid[i][j] = 0    # Sink the island/mark as visited
    dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    @area += 1

    dirs.each do |di, dj|
        x, y = i + di, j + dj
        dfs(grid, x, y) if x.between?(0, m - 1) && y.between?(0, n - 1)
    end
end

require 'test/unit'
extend Test::Unit::Assertions

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]
grid2 = [[0,0,0,0,0,0,0,0]]

assert_equal(max_area_of_island(grid), 6)
assert_equal(max_area_of_island(grid2), 0)
