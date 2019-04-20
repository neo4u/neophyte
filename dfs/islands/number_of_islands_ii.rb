def dfs(grid, m, n, i, j, visited)
    # puts "dfs called with #{i}, #{j} | grid[i]: #{grid[i]}"
    return if grid[i][j] == '0' || visited[i][j]
    visited[i][j] = true
    dfs(grid, m, n, i - 1, j, visited) if i > 0
    dfs(grid, m, n, i + 1, j, visited) if i < m - 1
    dfs(grid, m, n, i, j - 1, visited) if j > 0
    dfs(grid, m, n, i, j + 1, visited) if j < n - 1
end

def cc(grid, m, n)
    count = 0
    visited = Array.new(m) { Array.new(n, false) }
    0.upto(m - 1) do |i|
        0.upto(n - 1) do |j|
            next if grid[i][j] == '0' || visited[i][j]
            dfs(grid, m, n, i, j, visited)
            count += 1
        end
    end
    puts count
    count
end

# Approach 1: DFS [TLE]
# @param {Integer} m
# @param {Integer} n
# @param {Integer[][]} positions
# @return {Integer[]}
def num_islands2(m, n, positions)
    result = []
    grid = Array.new(m) { "0" * n }

    positions.each do |i, j|
        grid[i][j] = '1'
        result << cc(grid, m, n)
    end

    result
end

class DisjoinSet
    attr_accessor :roots, :count

    def initialize()
        @roots = {}
        @rank = {}
        @count = 0
    end

    def find(x)
        @roots[x] = find(@roots[x]) if x != @roots[x]
        @roots[x]
    end

    def union(x, y)
        par_x, par_y = find(x), find(y)
        return if par_x == par_y

        if @rank[par_x] > @rank[par_y]
            @roots[par_y] = par_x
        elsif @rank[par_x] < @rank[par_y]
            @roots[par_x] = par_y
        else
            @roots[par_y] = par_x
            @rank[par_x] += 1
        end
        @count -= 1
    end

    def set_parent(x)
        @roots[x] = x
        @rank[x] = 0
        @count += 1
    end
end

# Approach 3: Disjoint Set Union Find
# @param {Integer} m
# @param {Integer} n
# @param {Integer[][]} positions
# @return {Integer[]}
def num_islands2(m, n, positions)
    ds = DisjoinSet.new()
    dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    result = []

    positions.each do |i, j|
        ds.set_parent([i, j])
        dirs.each do |di, dj|
            x, y = i + di, j + dj
            next if !x.between?(0, m - 1) || !y.between?(0, n - 1) || !ds.roots.key?([x, y])
            ds.union([i, j], [x, y])
        end
        result.push(ds.count)
    end

    result
end

# 305. Number of Islands II
# https://leetcode.com/problems/number-of-islands-ii/description/

# Key Insight:
# 1. This is an undirected graph in the form of an adjacency matrix
# 2. There is an edge between two horizontally or vertically adjacent nodes of value 1
# 3. The problem is now to find the no. of connected components
#    in the graph after each addLand operation

# Approach 1: Brute force [TLE]
# Approach 2: DFS [TLE]
# Approach 3: Ad hoc
# Approach 4: Disjoint Set Union Find (with rank and path compression)


require 'test/unit'
extend Test::Unit::Assertions

assert_equal(num_islands2(3, 3, [[0,0], [0,1], [1,2], [2,1]]), [1,1,2,3])
