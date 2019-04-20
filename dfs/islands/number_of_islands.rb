# Approach 1: DFS
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
    m, n = grid.size, grid[0].size
    return if grid[i][j] == '0' # Optional as we're limiting dfs to only when unvisited (== '1')
    grid[i][j] = '0'    # Sink the island/mark as visited
    dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    dirs.each do |di, dj|
        x, y = i + di, j + dj
        next if !x.between?(0, m - 1) || !y.between?(0, n - 1) || grid[x][y] == '0'
        dfs(grid, x, y)
    end
end

# Approach 2: BFS
# @param {Character[][]} grid
# @return {Integer}
def num_islands_bfs(grid)
    return 0 if grid.empty? || grid[0].empty?
    m, n, count = grid.size, grid[0].size, 0

    0.upto(m - 1) do |i|
        0.upto(n - 1) do |j|
            next if grid[i][j] == '0'
            bfs(grid, i, j)
            count += 1
        end
    end

    count
end

def bfs(grid, i, j)
    m, n, q = grid.size, grid[0].size, [[i, j]]
    grid[i][j] = '0' # Mark as visited
    dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    while !q.empty?
        i, j = q.shift()

        dirs.each do |di, dj|
            x, y = i + di, j + dj
            next if !x.between?(0, m - 1) || !y.between?(0, n - 1) || grid[x][y] == '0'
            q.push([x, y])
            grid[x][y] = '0'
        end
    end
end


class DisjoinSet
    attr_accessor :parent,  :rank, :count

    def initialize()
        @parent = {}
        @rank = {}
        @count = 0
    end

    def set_parent(x)
        @parent[x] = x
        @rank[x] = 0
        @count += 1
    end

    def find(x) # with path compression
        @parent[x] = find(@parent[x]) if x != @parent[x]
        @parent[x]
    end

    def union(x, y)
        par_x, par_y = find(x), find(y)
        return if par_x == par_y

        # Union by rank means make the element with higher rank the parent
        # to keep the depth of the tree to a minimum
        if @rank[par_x] > @rank[par_y]      # par_x has greater rank,
            @parent[par_y] = par_x          # So par_x becomes parent of par_y
        elsif @rank[par_y] > @rank[par_x]   # par_y has greater rank,
            @parent[par_x] = par_y          # So par_y becomes parent of par_x
        else                                # Same rank,
            @parent[par_y] = par_x          # so make one parent of the other
            @rank[par_x] += 1               # only increase rank of parent when ranks are same
        end
        @count -= 1                         # Total count of sets reduces by as two sets become one
    end
end

# Approach 3: UF
# @param {Character[][]} grid
# @return {Integer}
def num_islands_uf(grid)
    return 0 if grid.empty? || grid[0].empty?
    m, n = grid.size, grid[0].size
    ds = DisjoinSet.new()
    dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    0.upto(m - 1) do |i|
        0.upto(n - 1) do |j|
            next if grid[i][j] == '0'
            ds.set_parent([i, j])
            dirs.each do |di, dj|
                x, y = i + di, j + dj
                next if !x.between?(0, m - 1) || !y.between?(0, n - 1) || !ds.parent.key?([x, y])
                ds.union([i, j], [x, y]) # Union takes constant time, due to union by rank and path compression
            end
        end
    end

    ds.count
end

# 200. Number of Islands
# https://leetcode.com/problems/number-of-islands/description/


# Approach 1: DFS
# Time: O(m * n)
# Space: O(m * n) in case that the grid map is filled with lands where DFS goes by m * n deep

# Approach 2: BFS
# Time: O(m * n)
# Space: O(min(m, n))

# Approach 3: Union-Find
# Time: O(m * n)
# Space: O(m * n)

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
grid4 = [["1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","0","1","0","1","1"],
        ["0","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","0"],
        ["1","0","1","1","1","0","0","1","1","0","1","1","1","1","1","1","1","1","1","1"],
        ["1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
        ["1","0","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
        ["1","0","1","1","1","1","1","1","0","1","1","1","0","1","1","1","0","1","1","1"],
        ["0","1","1","1","1","1","1","1","1","1","1","1","0","1","1","0","1","1","1","1"],
        ["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","1","1"],
        ["1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1"],
        ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
        ["0","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1"],
        ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
        ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
        ["1","1","1","1","1","0","1","1","1","1","1","1","1","0","1","1","1","1","1","1"],
        ["1","0","1","1","1","1","1","0","1","1","1","0","1","1","1","1","0","1","1","1"],
        ["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","0"],
        ["1","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","0"],
        ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
        ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
        ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"]]

assert_equal(num_islands(grid), 1)
assert_equal(num_islands(grid2), 2)
assert_equal(num_islands(grid3), 2)
assert_equal(num_islands(grid4), 1)

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
grid4 = [["1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","0","1","0","1","1"],
        ["0","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","0"],
        ["1","0","1","1","1","0","0","1","1","0","1","1","1","1","1","1","1","1","1","1"],
        ["1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
        ["1","0","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
        ["1","0","1","1","1","1","1","1","0","1","1","1","0","1","1","1","0","1","1","1"],
        ["0","1","1","1","1","1","1","1","1","1","1","1","0","1","1","0","1","1","1","1"],
        ["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","1","1"],
        ["1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1"],
        ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
        ["0","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1"],
        ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
        ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
        ["1","1","1","1","1","0","1","1","1","1","1","1","1","0","1","1","1","1","1","1"],
        ["1","0","1","1","1","1","1","0","1","1","1","0","1","1","1","1","0","1","1","1"],
        ["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","0"],
        ["1","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","0"],
        ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
        ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
        ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"]]

assert_equal(num_islands_bfs(grid), 1)
assert_equal(num_islands_bfs(grid2), 2)
assert_equal(num_islands_bfs(grid3), 2)
assert_equal(num_islands_bfs(grid4), 1)

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
grid4 = [
    ["1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","0","1","0","1","1"],
    ["0","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","0"],
    ["1","0","1","1","1","0","0","1","1","0","1","1","1","1","1","1","1","1","1","1"],
    ["1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
    ["1","0","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
    ["1","0","1","1","1","1","1","1","0","1","1","1","0","1","1","1","0","1","1","1"],
    ["0","1","1","1","1","1","1","1","1","1","1","1","0","1","1","0","1","1","1","1"],
    ["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","1","1"],
    ["1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1"],
    ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
    ["0","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1"],
    ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
    ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
    ["1","1","1","1","1","0","1","1","1","1","1","1","1","0","1","1","1","1","1","1"],
    ["1","0","1","1","1","1","1","0","1","1","1","0","1","1","1","1","0","1","1","1"],
    ["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","0"],
    ["1","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","0"],
    ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
    ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
    ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"]]

assert_equal(num_islands_uf(grid), 1)
assert_equal(num_islands_uf(grid2), 2)
assert_equal(num_islands_uf(grid3), 2)
assert_equal(num_islands_uf(grid4), 1)