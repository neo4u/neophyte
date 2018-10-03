# @param {Integer[][]} matrix
# @return {Integer[][]}
def update_matrix(matrix)
    m, n = matrix.size(), matrix[0].size()
    dist = Array.new(m) { Array.new(n, Float::INFINITY) }
    q = []

    0.upto(m - 1) do |i|
        0.upto(n - 1) do |j|
            next if matrix[i][j] != 0
            dist[i][j] = 0
            q.push([i, j]) # Put all 0s in the queue.
        end
    end

    while !q.empty?
        i, j = q.shift()

        neighbors(i, j, m, n).each do |next_i, next_j|
            next if dist[next_i][next_j] <= dist[i][j] + 1
            dist[next_i][next_j] = dist[i][j] + 1
            q.push([next_i, next_j])
        end
    end

    dist
end

def neighbors(i, j, m, n)
    neighbours = []

    [[i - 1, j], [i + 1, j], [i , j - 1], [i, j + 1]].each do |new_i, new_j|
        next if !new_i.between?(0, m - 1) || !new_j.between?(0, n - 1)
        neighbours << [new_i, new_j]
    end
    
    neighbours
end

# 542. 01 Matrix
# https://leetcode.com/problems/01-matrix/description/

# Approach #2 Using BFS [Accepted]

# Intuition
# A better brute force: Looking over the entire matrix appears wasteful and hence,
# we can use Breadth First Search(BFS) to limit the search to the nearest 0 found for each 1.
# As soon as a 0 appears during the BFS, we know that the 0 is nearest,
# and hence, we move to the next 1.

# Think again: But, in this approach, we will only be able to update the distance of one 1 using one BFS,
# which could in fact, result in slightly higher complexity than the Approach 1 brute force.
# But hey,this could be optimised if we start the BFS from 0s and
# thereby, updating the distances of all the 1s in the path.

# Algorithm
# For our BFS routine, we keep a queue, q to maintain the queue of cells to be examined next.
# We start by adding all the cells with 0s to q.
# Intially, distance for each 0 cell is 0 and distance for each 1 is INT_MAX, which is updated during the BFS.
# Pop the cell from queue, and examine its neighbours.
# If the new calculated distance for neighbour {i,j} is smaller, we add {i,j} to q and update dist[i][j].

# Complexity analysis

# Time complexity: O(r⋅c)

# Since, the new cells are added to the queue only if their current distance is
# greater than the calculated distance, cells are not likely to be added multiple times.

# Space complexity: O(r⋅c). Additional O(r \cdot c)O(r⋅c) for queue than in Approach #1