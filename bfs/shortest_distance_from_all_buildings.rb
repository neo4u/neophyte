# @param {Integer[][]} grid
# @return {Integer}
def shortest_distance(grid)
    return 0 if grid.empty? || grid[0].empty?

    m, n = grid.size, grid[0].size          # count is the count of nodes
    c = Array.new(m) { Array.new(n, 0) }    # Matrix of the count of reachable buildings from each point in grid
    d = Array.new(m) { Array.new(n, 0) }    # Matrix of sum of distances from buildings to each point in grid
    min_step = Float::INFINITY

    num_buildings = 0
    0.upto(m - 1) do |i|
        0.upto(n - 1) do |j|
            num_buildings += 1 if grid[i][j] == 1
        end
    end
    # puts "num_bs: #{num_buildings}"

    0.upto(m - 1) do |i|
        0.upto(n - 1) do |j|
            next if grid[i][j] != 1 # We do BFS only from each building
            return -1 if !bfs(grid, i, j, c, d, num_buildings) # All 1's should be reachable from each other
        end
    end

    # puts "c"
    # print_matrix(c)
    # puts "d"
    # print_matrix(d)

    0.upto(m - 1) do |i|
        0.upto(n - 1) do |j|
            next if grid[i][j] != 0 || c[i][j] < num_buildings  # we only check the distances for 0 points
            min_step = [min_step, d[i][j]].min
        end
    end

    min_step == Float::INFINITY ? -1 : min_step
end


def bfs(grid, start_x, start_y, c, d, num_buildings)
    count = 1 # Bcuz we only start the BFS after building was found so the count should already be 1
    dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    m, n = grid.size, grid[0].size
    visited = Array.new(m) { Array.new(n, false) }

    q = [[start_x, start_y, 0]] # Start with the building co-ordinates and a distance of 0
    visited[start_x][start_y] = true

    while !q.empty?
        x, y, dist = q.shift()
        dirs.each do |di, dj|
            i, j = x + di, y + dj
            next if !i.between?(0, m - 1) || !j.between?(0, n - 1) || visited[i][j]
            # Only when the points are within the bounds of the matrix && not yet visited
            visited[i][j] = true
            if grid[i][j] == 0 # Only add 0 points to the queue, cuz we only needs distances of each 0 to all 1s
                q.push([i, j, dist + 1])
                d[i][j] += dist + 1
                c[i][j] += 1
            elsif grid[i][j] == 1
                count += 1
            end
        end
    end

    count == num_buildings
end

def print_matrix(matrix)
    matrix.each do |a|
        puts a.inspect
    end
    puts
end

# https://leetcode.com/problems/shortest-distance-from-all-buildings/
# 317. Shortest Distance from All Buildings

# Key Insights
# 1. We can build a house on a 0 point
# 2. We have to reach ALL the 1 points
# 3. We want to choose a 0 point that has the least total distance to all such 1 points
# 4. All 1's should be reachable from each other,
#    because they're not connected means there is no 0 point between then to consider

# Approach 1: BFS from each building to all the 0s
# Steps:
# 1. Perform BFS from each building to each 0
# 2. Keep d as a matrix of distances from each 0 to 1s,
#    then calculate min of them all
# 3. We can use the 4th insight, to prune further BFSs as all 1st must be connected to each other
# 4. We do this by maintaining a count of reachable 1s during each BFS and comparing to number of buildings
# 5. We also maintain array c to count the number of buildings reachable from each 0, and don't consider 0s
#    that can't reach all the buildings

# Time:  O(k * m * n), k is the number of the buildings or O(m^2.n^2) or O(n * 2) or quadratic time
# Space: O(m * n) or O(n) or linear time

require 'test/unit'
extend Test::Unit::Assertions   

assert_equal(shortest_distance([[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]), 7)
assert_equal(shortest_distance([[1]]), -1)
assert_equal(shortest_distance([[1,1]]), -1)
assert_equal(shortest_distance([[1],[1]]), -1)
assert_equal(shortest_distance([[1,2,0]]), -1)
assert_equal(shortest_distance([[1],[2],[0]]), -1)

assert_equal(shortest_distance([[1,0]]), 1)
assert_equal(shortest_distance([[1],[0]]), 1)
assert_equal(shortest_distance([[1,0,1]]), 2)
assert_equal(shortest_distance([[1],[0],[1]]), 2)
assert_equal(shortest_distance([[1,0],[0,1]]), 2)
assert_equal(shortest_distance([[2,0,0],[0,1,0],[1,0,0]]), 2)
assert_equal(shortest_distance([[1,2,0],[0,0,0],[0,0,0]]), 1)
assert_equal(shortest_distance([[0,2,1],[1,0,2],[0,1,0]]), -1)

assert_equal(shortest_distance([[1,1],[0,1]]), -1)
assert_equal(shortest_distance([[1,0,1,0,1]]), -1)
assert_equal(shortest_distance([[1],[0],[1],[0],[1]]), -1)
assert_equal(shortest_distance([
    [1,1,1,1,1,0],
    [0,0,0,0,0,1],
    [0,1,1,0,0,1],
    [1,0,0,1,0,1],
    [1,0,1,0,0,1],
    [1,0,0,0,0,1],
    [0,1,1,1,1,0]
]), 88)
assert_equal(shortest_distance([
    [1,1,1,1,1,1,1,0],
    [0,0,0,0,0,0,0,1],
    [0,1,1,1,1,0,0,1],
    [1,0,0,0,0,1,0,1],
    [1,0,0,1,0,1,0,1],
    [1,0,1,0,0,1,0,1],
    [1,0,0,1,1,0,0,1],
    [1,0,0,0,0,0,0,1],
    [0,1,1,1,1,1,1,0]
]), 226)
