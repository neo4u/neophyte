# Approach 1: BFS
# @param {Integer[][]} maze
# @param {Integer[]} start
# @param {Integer[]} destination
# @return {Boolean}
def has_path(maze, start, destination)
    q, m, n = [start], maze.size, maze[0].size
    dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]] # [right, left, down, up]

    while !q.empty?
        i, j = q.shift()
        maze[i][j] = 2
        return true if [i, j] == destination

        dirs.each do |x, y|
            r, c = i, j
            
            # Keep going in the same direction till you hit a wall
            while (r + x).between?(0, m - 1) && (c + y).between?(0, n - 1) && maze[r + x][c + y] == 0
                r += x; c += y
            end

            q.push([r, c]) if maze[r][c].zero?
        end
    end

    false
end

# Approach 2: DFS
# @param {Integer[][]} maze
# @param {Integer[]} start
# @param {Integer[]} destination
# @return {Boolean}
def has_path2(maze, start, destination)
    dfs(maze, start, destination)
end

DIRS = [[0, 1], [0, -1], [1, 0], [-1, 0]] # [right, left, down, up]
def dfs(maze, s, d)
    m, n = maze.size, maze[0].size
    i, j = s
    return false if maze[i][j] == 2
    maze[i][j] = 2
    return true if s == d

    DIRS.each do |x, y|
        r, c = s

        # Keep going in the same direction till you hit a wall
        while (r + x).between?(0, m - 1) && (c + y).between?(0, n - 1) && maze[r + x][c + y] != 1
            r += x; c += y
        end

        return true if dfs(maze, [r, c], d)
    end

    false
end

# 490. The Maze
# https://leetcode.com/problems/the-maze/description/

# Apporach 1: BFS, Time: O(m * n), Space: O(m * n)
# Approach 2: DFS, Time: O(m * n), Space: O(m * n)

require 'set'
require 'test/unit'
extend Test::Unit::Assertions

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
maze = [[0,0,1,0,0],
        [0,0,0,0,0],
        [0,0,0,1,0],
        [1,1,0,1,1],
        [0,0,0,0,0]]
assert_equal(has_path2(maze, [0,4], [3,2]), false)
maze = [[0,0,1,0,0],
        [0,0,0,0,0],
        [0,0,0,1,0],
        [1,1,0,1,1],
        [0,0,0,0,0]]
assert_equal(has_path2(maze, [0,4], [4,4]), true)
