# @param {Integer[][]} dungeon
# @return {Integer}
def calculate_minimum_hp(dungeon)
    m, n = dungeon.size, dungeon[0].size
    q, visited = [[m - 1, n - 1]], Set.new()

    while !q.empty?
        i, j = q.shift()

        next if visited.include?([i, j])
        visited.add([i, j])

        down = i + 1 < m ? dungeon[i + 1][j] : Float::INFINITY
        right = j + 1 < n ? dungeon[i][j + 1] : Float::INFINITY

        if i == m - 1 && j == n - 1
            dungeon[i][j] = [1, -dungeon[m - 1][n - 1] + 1].max
        else
            dungeon[i][j] = [[down, right].min - dungeon[i][j], 1].max
        end

        q.push([i - 1, j]) if i - 1 >= 0
        q.push([i, j - 1]) if j - 1 >= 0
    end

    dungeon[0][0]
end


# Time: O(m * n)
# Space: O(m * n) We can argue that this is O(1) because we're using input array.
# and IO is not counted towards complexity calculations

# The minimum health that a knight needs to start from (i, j) is
# the minimum health of that it needs to start from any surrounding cell
# minus the value of the cell.
# To start from the cell with the princess needs 1 minus value of that cell.

# How can we compute this? Since each cell depends on all surrounding cells?
# If we start from the princess cell, we can just consider the left and top cells.
# Is it possible to have loops?
# Then the world has a state, since you can't take the same bonus twice.
# Wait! The knight decides to move only right or down.

# Questions
# 1. Is replacing the health points on the cell not a problem?
# Answer: Nope. We can only use the health points once.
# 2. Is it DP?
# Answer: Yes. This is DP guised in a BFS method. or bfs with caching. 
# Essentially, once a cell is visited dungeon[i][j] consists of
# the minimum health required to reach that cell and live (have a health >= 1).

require 'set'
require 'test/unit'
extend Test::Unit::Assertions

assert_equal(calculate_minimum_hp([[-2,-3,3],[-5,-10,1],[10,30,-5]]), 7)
assert_equal(calculate_minimum_hp([[2,0,-1]]), 1)