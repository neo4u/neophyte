# @param {Integer[][]} matrix
# @return {Integer}
def longest_increasing_path(matrix)
    return 0 if !matrix || matrix.empty?
    m, n, result = matrix.size, matrix[0].size, 0

    cache = Array.new(m) { Array.new(n, 0) }
    prev = -Float::INFINITY

    0.upto(m - 1) do |i|
        0.upto(n - 1) do |j|
            result = [result, dfs(matrix, prev, i, j, m, n, cache)].max
        end
    end

    result
end

def dfs(matrix, prev, i, j, m, n, cache)
    return 0 if !i.between?(0, m - 1) || !j.between?(0, n - 1) || matrix[i][j] <= prev
    return cache[i][j] if cache[i][j] != 0

    prev = matrix[i][j]

    a = dfs(matrix, prev, i + 1, j, m, n, cache)
    b = dfs(matrix, prev, i - 1, j, m, n, cache)
    c = dfs(matrix, prev, i, j + 1, m, n, cache)
    d = dfs(matrix, prev, i, j - 1, m, n, cache)
    result = [a, b, c, d].max + 1
    cache[i][j] = result

    result
end


# Complexity Analysis
# Time complexity: O(mn). Each vertex/cell will be calculated once and only once,
#                  and each edge will be visited once and only once.
#                  The total time complexity is then O(V+E).
#                  V is the total number of vertices and E is the total number of edges.
#                  In our problem, O(V) = O(mn), O(E) = O(4V) = O(mn).
# Space complexity: O(mn)O(mn). The cache dominates the space complexity.

# Strategy
# Keep track of longest increasing path for every neighbour + 1
# Use this cache if the node is revisited
# Only add current node to the path if the value at i, j is > than prev value (ret 0 if <=)