# @param {Integer[][]} grid
# @return {Integer}
def shortest_distance(grid)
    m, n, count = grid.size, grid[0].size, 0

    d = Array.new(m) { Array.new(n, 0) } # Maintain a matrix of sum of distances from buildings to each point in grid
    c = Array.new(m) { Array.new(n, 0) } # Maintain a matrix of the count of reachable buildings from each point in grid

    # For each point in matrix which is a building find do a BFS to every 0 in the grid
    0.upto(m - 1) do |i|
        0.upto(n - 1) do |j|
            next if grid[i][j] != 1
            count += 1
            bfs(grid, d, c, i, j)
        end
    end

    # Once the distance and counts matrices are built, Find the point that has the shortest sum of distances
    shortest = Float::INFINITY
    0.upto(m - 1) do |i|
        0.upto(n - 1) do |j|
            shortest = d[i][j] if d[i][j] < shortest && c[i][j] == count
        end
    end

    # Return -1 if we're unable to find a point that is reachable to all the buildings
    shortest != Float::INFINITY ? shortest : -1
end

def bfs(grid, d, c, x, y)
    m, n = grid.size, grid[0].size
    visited = Array.new(m) { Array.new(n, false) }

    q = [[x, y, 0]] # Start with the building co-ordinates and a distance of 0
    visited[x][y] = true

    while !q.empty?
        i, j, dist = q.shift()
        [[-1, 0], [1, 0], [0, -1], [0, 1]].each do |direction|
            next_i, next_j = i + direction[0], j + direction[1]
            next if !next_i.between?(0, m - 1) || !next_j.between?(0, n - 1) ||
                    grid[next_i][next_j] != 0 || visited[next_i][next_j]
            # Only when the points are within the matrix &&
            # grid point is 0 &&
            # point is not yet visited, on then
            # we add the point to the queue of neighbours to be further visited
            c[next_i][next_j] += 1
            d[next_i][next_j] += dist + 1
            q.push([next_i, next_j, dist + 1])
            visited[next_i][next_j] = true
        end
    end
end

# https://leetcode.com/problems/shortest-distance-from-all-buildings/
# 317. Shortest Distance from All Buildings

# Time:  O(k * m * n), k is the number of the buildings or O(m^2.n^2)
# Space: O(m * n)
# Method: BFS from each building to each 0 and keep as a matrix of sum of distances, then calculate min of them all

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(shortest_distance([[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]), 7)
