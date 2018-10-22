# @param {Character[][]} grid
# @return {Integer}
def num_islands(grid)
    return 0 if grid.empty? || grid[0].empty?
    m, n, count = grid.size, grid[0].size, 0

    0.upto(m - 1) do |i|
        0.upto(n - 1) do |j|
            next if grid[i][j] == '0'
            dfs(grid, i, j)
            count += 1
        end
    end

    count
end

def dfs(grid, i, j)
    return if grid[i][j] == '0'
    grid[i][j] = '0'

    dfs(grid, i - 1, j) if i > 0
    dfs(grid, i + 1, j) if i < grid.size - 1
    dfs(grid, i, j - 1) if j > 0
    dfs(grid, i, j + 1) if j < grid[0].size - 1
end

require 'test/unit'
extend Test::Unit::Assertions

grid = ["11110",
        "11010",
        "11000",
        "00000"]
grid2 = ['100',
         '000',
         '001']
grid3 = ["111111",
         "100001",
         "101101",
         "100001",
         "111111"]

assert_equal(num_islands(grid), 1)
assert_equal(num_islands(grid2), 2)
assert_equal(num_islands(grid3), 2)
