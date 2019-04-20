# Approach 2: BFS without Priority Queue
# @param {Integer[][]} maze
# @param {Integer[]} start
# @param {Integer[]} destination
# @return {Integer}
def shortest_distance(maze, start, destination)
    return -1 if !maze || !maze[0]

    sx, sy = start
    @maze = maze
    @m, @n = @maze.size, @maze[0].size
    q, visited = [[0, sx, sy]], { [sx, sy] => 0 }
    dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]] # [right, left, down, up]
    counts = 0

    while !q.empty?
        counts += 1
        dist, i, j = q.shift()

        dirs.each do |x, y|
            d, r, c = dist, i, j

            # Inorder to change direction, we need to hit the wall,
            # So keep rolling until valid
            while valid?(r + x, c + y)
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

    visited.fetch(destination, -1) # return -1 if destination is not found in hash
end

def valid?(i, j)
    i.between?(0, @m - 1) && j.between?(0, @n - 1) && @maze[i][j] == 0
end


# Approach 4: BFS with priority queue
# Same as dijkstra's but tweaked to use visited hash to store distances
# Instead of using distances array initialized to infinity

require 'pqueue' # Needs to be installed
def shortest_distance_minq(maze, start, destination)
    return -1 if !maze || !maze[0]

    sx, sy = start
    @maze = maze
    @m, @n = @maze.size, @maze[0].size

    # Define a min queue, using the first element of the array as key
    q = PQueue.new(){ |a, b| a[0] < b[0] }
    q.push([0, sx, sy])

    visited = { [sx, sy] => 0 } # Store every visited node and distance to get there. Start node is initialized to 0.
    dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]] # [right, left, down, up]
    counts = 0

    while !q.empty?
        dist, i, j = q.pop()

        dirs.each do |x, y|
            d, r, c = dist, i, j # distance to get to a point, co-ordinates to that point

            # Inorder to change direction, we need to hit the wall
            while valid?(r + x, c + y)
                r += x; c += y
                d += 1
            end

            # We prune higher distance nodes
            if !visited.include?([r, c]) || d < visited[[r, c]]
                visited[[r, c]] = d             # Update the distance to a node if we found a shorter path
                next if [r, c] == destination   # skip to next if we hit the dst node
                q.push([d, r, c])
                counts += 1
            end
        end
    end

    visited.fetch(destination, -1) # return -1 if destination is not found in hash
end

def valid?(i, j)
    i.between?(0, @m - 1) && j.between?(0, @n - 1) && @maze[i][j] == 0
end


# 505. The Maze II
# https://leetcode.com/problems/the-maze-ii/description/

# The Maze I vs Maze II:
# - In Maze we're just finding a path. Doesn't need to be shortest.
# - Here in the Maze II we're trying to find the shortest path.

# Key Insight:
#  - Ball can't stop mid rolling, it can only stop when it hits a wall
#    At which point, it can also change direction
#  - We need to explore ALL the paths and find the shortest one
#  - We can prune paths where the distance from is more
#    than the currently shortest distance.
#  - With priority queue we'll prune more node visits,
#    because we'll only pick the smallest distance 

# Approach 1: DFS
# Time: O(m * n * max(m,n)),
# Space: O(m * n). Space to store distance for each node/stack depth

# Approach 2: BFS
# Steps:
#   1. Create a distances array initialized to infinity for all points other than start node
#   2. Keep visiting neighbors and update their distances in array
#   3. We use a while to hit the wall in order to explore directions
#   4. Use min pqueue to pick next point, thus visiting smaller nodes first and
#      thus pruning greater distance paths
# Time: O(m * n * max(m,n))
# Space: O(m * n). Space to store distance for each node/queue size

# Approach 3: Dijkstra's Algo with normal queue and traversing the whole distance array for min distance
# Time: O((m * n) ^ 2),
# Space: O(m * n). Space to store distance for each node/queue size

# Approach 4: Dijkstra's with PriorityQueue to get min distance
# Steps:
#   1. Create a distances array initialized to infinity for all points other than start node
#   2. Keep visiting neighbors and update their distances in array
#   3. We use a while to hit the wall in order to explore directions
#   4. Use min pqueue to pick next point, thus visiting smaller nodes first and
#      thus pruning greater distance paths
# Time: O(m * n  * log(m * n)),
# Space: O(m * n). Space to store distance array and pqueue can also grow to size of m * n

# Approach 5: BFS with pqueue
# Steps:
#   1. Create a visited hash initialized to contain start point and 
#   2. Keep visiting neighbors and update their distances in the hash
#   3. We use a while to hit the wall in order to explore directions
#   4. Use min pqueue to pick next point, thus visiting smaller nodes first and
#      thus pruning greater distance paths
# Example Walkthrough:
# start = [0, 4], dest = [4, 4]
# maze = [[0,0,1,0,0],
#         [0,0,0,0,0],
#         [0,0,0,1,0],
#         [1,1,0,1,1],
#         [0,0,0,0,0]]

#     pq                                | visited hash
# --------------------------------------------------------------------------------
# [[0, 0, 4]]                           | {[0, 4]=>0}
# [[2, 2, 4], [1, 0, 3]]                | {[0, 4]=>0, [0, 3]=>1, [2, 4]=>2}
# [[2, 1, 3], [2, 2, 4]]                | {[0, 4]=>0, [0, 3]=>1, [2, 4]=>2, [1, 3]=>2}
# [[2, 1, 3]]                           | {[0, 4]=>0, [0, 3]=>1, [2, 4]=>2, [1, 3]=>2}
# [[5, 1, 0], [3, 1, 4]]                | {[0, 4]=>0, [0, 3]=>1, [2, 4]=>2, [1, 3]=>2, [1, 4]=>3, [1, 0]=>5}
# [[5, 1, 0]]                           | {[0, 4]=>0, [0, 3]=>1, [2, 4]=>2, [1, 3]=>2, [1, 4]=>3, [1, 0]=>5}
# [[6, 0, 0], [6, 2, 0]]                | {[0, 4]=>0, [0, 3]=>1, [2, 4]=>2, [1, 3]=>2, [1, 4]=>3, [1, 0]=>5, [2, 0]=>6, [0, 0]=>6}
# [[8, 2, 2], [6, 0, 0]]                | {[0, 4]=>0, [0, 3]=>1, [2, 4]=>2, [1, 3]=>2, [1, 4]=>3, [1, 0]=>5, [2, 0]=>6, [0, 0]=>6, [2, 2]=>8}
# [[8, 2, 2], [7, 0, 1]]                | {[0, 4]=>0, [0, 3]=>1, [2, 4]=>2, [1, 3]=>2, [1, 4]=>3, [1, 0]=>5, [2, 0]=>6, [0, 0]=>6, [2, 2]=>8, [0, 1]=>7}
# [[9, 2, 1], [8, 2, 2]]                | {[0, 4]=>0, [0, 3]=>1, [2, 4]=>2, [1, 3]=>2, [1, 4]=>3, [1, 0]=>5, [2, 0]=>6, [0, 0]=>6, [2, 2]=>8, [0, 1]=>7, [2, 1]=>9}
# [[10, 4, 2], [9, 1, 2], [9, 2, 1]]    | {[0, 4]=>0, [0, 3]=>1, [2, 4]=>2, [1, 3]=>2, [1, 4]=>3, [1, 0]=>5, [2, 0]=>6, [0, 0]=>6, [2, 2]=>8, [0, 1]=>7, [2, 1]=>9, [4, 2]=>10, [1, 2]=>9}
# [[10, 4, 2], [9, 1, 2]]               | {[0, 4]=>0, [0, 3]=>1, [2, 4]=>2, [1, 3]=>2, [1, 4]=>3, [1, 0]=>5, [2, 0]=>6, [0, 0]=>6, [2, 2]=>8, [0, 1]=>7, [2, 1]=>9, [4, 2]=>10, [1, 2]=>9}
# [[10, 4, 2]]                          | {[0, 4]=>0, [0, 3]=>1, [2, 4]=>2, [1, 3]=>2, [1, 4]=>3, [1, 0]=>5, [2, 0]=>6, [0, 0]=>6, [2, 2]=>8, [0, 1]=>7, [2, 1]=>9, [4, 2]=>10, [1, 2]=>9}
# [[12, 4, 0]]                          | {[0, 4]=>0, [0, 3]=>1, [2, 4]=>2, [1, 3]=>2, [1, 4]=>3, [1, 0]=>5, [2, 0]=>6, [0, 0]=>6, [2, 2]=>8, [0, 1]=>7, [2, 1]=>9, [4, 2]=>10, [1, 2]=>9, [4, 4]=>12, [4, 0]=>12}

# without pq: 14 visits
# With pqueue: 13 visits (1 path pruned)

# Time: O(m * n  * log(m * n)),
# Space: O(m * n). Space to store distance array and pqueue can also grow to size of m * n

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

maze = [[0,0,1,0,0],
        [0,0,0,0,0],
        [0,0,0,1,0],
        [1,1,0,1,1],
        [0,0,0,0,0]]
assert_equal(shortest_distance_minq(maze, [0,4], [3,2]), -1)
maze = [[0,0,1,0,0],
        [0,0,0,0,0],
        [0,0,0,1,0],
        [1,1,0,1,1],
        [0,0,0,0,0]]
assert_equal(shortest_distance_minq(maze, [0,4], [4,4]), 12)
