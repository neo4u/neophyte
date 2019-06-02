require 'set'

# Approach 1: DFS detecting cycle
# @param {Integer} num_courses
# @param {Integer[][]} prerequisites
# @return {Boolean}
def find_order_dfs(n, prereqs)
    @graph = Hash.new { |h, k| h[k] = Set.new() }
    @visited, @on_stack, @result = Set.new(), Set.new(), []

    prereqs.each { |u, v| @graph[u].add(v) }
    n.times { |node| return [] if !@visited.include?(node) && dfs_has_cycle?(node) } # find one not visited and start from it

    @result.size == n ? @result : []
end

def dfs_has_cycle?(node)
    @visited.add(node)
    @on_stack.add(node)

    @graph[node].each do |v|
        return true if @on_stack.include?(v)
        return true if !@visited.include?(v) && dfs_has_cycle?(v)
    end

    @result.push(node)
    @on_stack.delete(node) # Making DFS a post-order traversal: popping current when all its children are done
    false
end


# Approach 2: BFS tweaked topological sort
# @param {Integer} num_courses
# @param {Integer[][]} prerequisites
# @return {Boolean}
def find_order_bfs(n, prereqs)
    graph, in_deg = Hash.new { |h, k| h[k] = Set.new }, Hash.new { |h, k| h[k] = 0 }
    visited, q = [], []                                     # Can't use set cuz of order problem

    prereqs.each do |u, v|
        graph[v].add(u)
        in_deg[u] += 1
    end
    n.times { |v| q.push(v) if in_deg[v].zero? }            # find nodes whose in degree == 0

    while !q.empty?                                         # loop all nodes whose in degree == 0
        i = q.shift()
        visited.push(i)                                     # Zero in degree first becomes course we can take last
        graph[i].each do |nbr|
            in_deg[nbr] -= 1                                # Think of this as remove 'node' so all nbs have 1 in_degree less
            q.push(nbr) if in_deg[nbr].zero?                # populate q with node whose in_degress is 0
        end
    end

    visited.size == n ? visited : []
end

# 210. Course Schedule II
# https://leetcode.com/problems/course-schedule-ii/

# Key Insight:
# 1. It comes down to a problem of detecting a cycle in a graph (Checking if its a DAG)
# 2. We need some sort of ordering of courses hence topological sort makes sense
# 3. edge from u to v means u has a pre-req of v
# 4. we can also add edge from v to u, which means we can we v and then take u.


# Approach 1: DFS with keeping track of on_stack nodes
# Steps:
# 1. Iterate through prereqs adding each preerq as a directed edge in graph
#    which is a map from nodes (interger) to list of nodes (array)
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

# Approach 2: BFS with using Kahn's algorithm (in-degree)

# Steps:
# 1. Iterate through prereqs adding each preerq as a directed edge in graph
#    which is a map from nodes (interger) to list of nodes (array)
# 2. Iterate through the courses and get the indegrees of all vertices
# 3. We perform a BFS with a twist that only nodes with an in-degree of 0
#    are added to the q (Kahn's Topological Sort Algorithm)
# 4. For each visited node we reduce the in-degree of the node by 1, before
#    adding 0 in-degree nbs to the queue
# 5. We add nodes to visited from the front and finally return this array

# 3, [[1,0],[2,1]]

# graph
# node nbr  in_deg
# 0    [1]	0
# 1    [2]	1

# in_deg
# node in_deg
# 1 		0
# 2       0
# 0       0

# q []

# visited [0, 1, 2]

# Time: O(N), Essentially, O(V + E), V - number of courses, E - number of prereqs => O(V + V - 1) => O(N)
# Space: O(N)


require 'test/unit'
extend Test::Unit::Assertions

assert_equal(find_order_dfs(2, [[1,0]]), [0,1])
assert_equal(find_order_dfs(2, [[0,1]]), [1,0])
assert_equal(find_order_dfs(2, [[0,1],[1,0]]), [])
assert_equal(find_order_dfs(4, [[1,0],[2,0],[3,1],[3,2]]), [0,1,2,3])


assert_equal(find_order_bfs(2, [[1,0]]), [0,1])
assert_equal(find_order_bfs(2, [[0,1]]), [1,0])
assert_equal(find_order_bfs(2, [[0,1],[1,0]]), [])
assert_equal(find_order_bfs(4, [[1,0],[2,0],[3,1],[3,2]]), [0,1,2,3])
