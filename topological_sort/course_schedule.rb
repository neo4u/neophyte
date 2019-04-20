require 'set'

# Approach 1: DFS detecting cycle
# @param {Integer} num_courses
# @param {Integer[][]} prerequisites
# @return {Boolean}
def can_finish(num_courses, prerequisites)
    @graph = Hash.new { |h, k| h[k] = [] }
    @visited = Set.new()
    @on_stack = Set.new()

    prerequisites.each do |u, v|
        @graph[u].push(v)
    end

    num_courses.times do |node|
        return false if !@visited.include?(node) && dfs_has_cycle?(node) # find one not visited and start from it
    end

    true
end

# Return false if circular dependency
def dfs_has_cycle?(node)
    @on_stack.add(node)

    @graph[node].each do |v|
        return true if @on_stack.include?(v)                        # Circular dependency
        return true if !@visited.include?(v) && dfs_has_cycle(v)    # Recursively find unvisited nodes and do a DFS
    end

    @visited.add(node)     # can also be placed before visiting children, so place is not important
    @on_stack.delete(node) # making DFS a post-order traversal: deleting current when all its children are done
    false
end


# Approach 2: BFS tweaked topological sort
# @param {Integer} num_courses
# @param {Integer[][]} prerequisites
# @return {Boolean}
def can_finish_bfs(n, prereqs)
    graph = Hash.new { |h, k| h[k] = [] }
    visited = []    # Can't use set cuz of order problem
    in_deg = Hash.new { |h, k| h[k] = 0 }
    q = []

    prereqs.each do |u, v|
        graph[u].push(v)
        in_deg[v] += 1
    end
    # find nodes whose in degree == 0
    n.times { |v| q.push(v) if in_deg[v].zero? }

    # loop all nodes whose in degree == 0
    while !q.empty?
        node = q.shift()
        visited.unshift(node) # Add from front to maintain the order that we can take courses in
        
        graph[node].each do |nbr|
            in_deg[nbr] -= 1                    # Think of this as remove 'node' so all nbs have 1 in_degree less
            q.push(nbr) if in_deg[nbr].zero?    # populate q with node whose in_degress is 0
        end
    end

    visited.size == n
end


# 207. Course Schedule
# https://leetcode.com/problems/course-schedule/description/

# Key Insight:
# 1. It comes down to a problem of detecting a cycle in a graph (Checking if its a DAG)
# 2. We need some sort of ordering of courses hence topological sort makes sense

# Approach 1: DFS with keeping track of on_stack nodes (VERY SLOW)
# Steps:
# 1. Iterate through prereqs adding each preerq as a directed edge in dictionary graph
#    which is a map from nodes (interger) to list of nodes (array of ints)
# 2. Now iterate through courses and do a DFS for each course
# 3. If DFS returns false for any course we return false, else we return true,
#    return false means a praticular course didn't have the prerequirements met
# 4. In dfs method we traverse the nbs and their nbs and so on for all nbs of the given node
# 5. In doing so, we keep track of the currently on stack nodes or visiting nodes if you will using on_stack.
#    The purpose of on_stack is to see if any of the courses have a circular dependency
#    or in other words if our graph has a cycle.
#    Example: 1 -> 2 -> 3 -> 4 -> 1, 1 -> 2 -> 3 -> 4 -> 2 or 1 -> 2 -> 3 -> 4 -> 3
#    Such a combo of prerequirements cannot be met due to the cycle

# Time: O(N), Essentially, O(V + E), V - number of courses, E - number of prereqs => O(V + V - 1) => O(N)
# Space: O(N)

# Approach 2: BFS with using Kahn's algorithm (in-degree) (VERY FAST For leetcode inputs)
# Steps:
# 1. Iterate through prereqs adding each preerq as a directed edge in graph
#    which is a map from nodes (interger) to list of nodes (array on ints)
# 2. Iterate through the courses and get the indegrees of each of the vertices
# 3. We perform a BFS with a tweak that only nodes with an in-degree of 0
#    are added to the q (Kahn's Topological Sort Algorithm)
# 4. For each visited node we reduce the in-degree of the node by 1, before
#    adding 0 in-degree nbs to the queue
# 5. We add nodes to visited from the front and finally return true
#    if this list has the same size as the number of courses.

# Time: O(N), Essentially, O(V + E), V - number of courses, E - number of prereqs => O(V + V - 1) => O(N)
# Space: O(N)


require 'test/unit'
extend Test::Unit::Assertions

assert_equal(can_finish(2, [[1,0]] ), true)
assert_equal(can_finish(2, [[1,0],[0,1]]), false)
assert_equal(can_finish(5, [[0, 4], [4,3],[3,2], [2, 1], [1, 4]]), false)

assert_equal(can_finish_bfs(2, [[1,0]]), true)
assert_equal(can_finish_bfs(2, [[1,0],[0,1]]), false)
assert_equal(can_finish_bfs(5, [[0, 4], [4,3],[3,2], [2, 1], [1, 4]]), false)
