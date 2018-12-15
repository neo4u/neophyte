# @param {Integer[][]} maze
# @param {Integer[]} start
# @param {Integer[]} destination
# @return {Integer}
def shortest_distance(maze, start, destination)
    return -1 if !maze || !maze[0]

    sx, sy = start
    m, n = maze.size, maze[0].size
    q, visited = [[0, sx, sy]], { [sx, sy] => 0 }
    dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]] # [right, left, down, up]

    while !q.empty?
        dist, i, j = q.shift()

        dirs.each do |x, y|
            r, c, d = i, j, dist

            while (r + x).between?(0, m - 1) && (c + y).between?(0, n - 1) && maze[r + x][c + y] != 0
                r += x; c += y
                d += 1
            end

            if !visited.include?([r, c]) || visited[[r, c]] > d
                visited[[r, c]] = d
                next if [r, c] == destination
                q.push([d, r, c])
            end
        end
    end

    visited.fetch(destination, -1)
end

# Djikstra's shortest path
# The only problem with BFS shortest path above is we cannot stop the first time we reach our destination.
# This can be overcome by using Djikstra's shortest path where we use a prioririty queue instead of a regular queue.

require 'test/unit'
extend Test::Unit::Assertions

maze = [[0,0,1,0,0],
        [0,0,0,0,0],
        [0,0,0,1,0],
        [1,1,0,1,1],
        [0,0,0,0,0]]
assert_equal(shortest_distance(maze, [0,4], [3,2]), -1)
maze = [[0,0,1,0,0],
        [0,0,0,0,0],
        [0,0,0,1,0],
        [1,1,0,1,1],
        [0,0,0,0,0]]
assert_equal(shortest_distance(maze, [0,4], [4,4]), 12)

