# Approach 1: BFS
def has_path(maze, src, dst)
    @maze = maze
    q, @m, @n = [start], @maze.size, @maze[0].size
    dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]] # [right, left, down, up]

    while !q.empty?
        i, j = q.shift()
        maze[i][j] = 2
        return true if [i, j] == destination

        dirs.each do |x, y|
            r, c = i, j
            while valid?(r + x, c + y)
                r += x; c += y
            end
            q.push([r, c]) if @maze[r][c].zero?
        end
    end

    false
end

def valid?(r, c)
    r.between?(0, @m - 1) && c.between?(0, @n - 1) && @maze[r][c] != 1
end

require 'set'
# Approach 2: DFS
def has_path_dfs(maze, src, dst)
    @maze, @m, @n = maze, maze.size, maze[0].size 
    dfs(src, dst)
end

DIRS = [[0, 1], [0, -1], [1, 0], [-1, 0]] # [right, left, down, up]
def dfs(s, d)
    i, j = s
    return false if @maze[i][j] == 2
    @maze[i][j] = 2
    return true if s == d

    DIRS.each do |x, y|
        r, c = s
        while valid?(r + x, c + y)
            r += x; c += y
        end
        return true if dfs([r, c], d)
    end

    false
end

def valid?(r, c)
    r.between?(0, @m - 1) && c.between?(0, @n - 1) && @maze[r][c] != 1
end

# 490. The Maze
# https://leetcode.com/problems/the-maze/description/

# Apporach 1: BFS, Time: O(m * n), Space: O(m * n)
# Approach 2: DFS, Time: O(m * n), Space: O(m * n)


require 'test/unit'
extend Test::Unit::Assertions

# BFS Tests
maze = [[0,0,1,0,0],
        [0,0,0,0,0],
        [0,0,0,1,0],
        [1,1,0,1,1],
        [0,0,0,0,0]]
assert_equal(has_path(maze, [0,4], [3,2]), false)
maze = [[0,0,1,0,0],
        [0,0,0,0,0],
        [0,0,0,1,0],
        [1,1,0,1,1],
        [0,0,0,0,0]]
assert_equal(has_path(maze, [0,4], [4,4]), true)

# DFS Tests
maze = [[0,0,1,0,0],
        [0,0,0,0,0],
        [0,0,0,1,0],
        [1,1,0,1,1],
        [0,0,0,0,0]]
assert_equal(has_path_dfs(maze, [0,4], [3,2]), false)
maze = [[0,0,1,0,0],
        [0,0,0,0,0],
        [0,0,0,1,0],
        [1,1,0,1,1],
        [0,0,0,0,0]]
assert_equal(has_path_dfs(maze, [0,4], [4,4]), true)
