# @param {Integer[][]} rooms
# @return {Void} Do not return anything, modify rooms in-place instead.
INF = 2147483647
def walls_and_gates(rooms)
    return if !rooms || rooms.empty? || rooms[0].empty?
    m, n = rooms.size, rooms[0].size
    dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    q = []

    0.upto(m - 1) do |i|
        0.upto(n - 1) do |j|
            q.push([i, j]) if rooms[i][j] == 0
        end
    end

    while !q.empty?
        i, j = q.shift()
        dirs.each do |dx, dy|
            x, y = i + dx, j + dy
            next if !x.between?(0, m - 1) || !y.between?(0, n - 1) || rooms[x][y] != INF # out of bounds or already found a gate
            rooms[x][y] = rooms[i][j] + 1
            q.push([x, y])
        end
    end
end


# 286. Walls and Gates
# https://leetcode.com/problems/walls-and-gates/description/

# Key Insights
# 1. We just have to modify distances in place, so nothing to return
# 2. We don't need a visited set in this case, cuz visited means shortest gate was found

# Steps
# 1. We can visit all empty spaces from each gate
# 2. While visiting a cell, if it was already visited from another gate,
#    it means we don't have to visit it again
# 3. Nothing to return

# Time: O(m * n)
# Space: O(m * n)
