# @param {Integer[][]} matrix
# @return {Integer}
def longest_increasing_path(matrix)
    return 0 if !matrix || matrix.empty?
    @m, @n, result = matrix.size, matrix[0].size, -Float::INFINITY
    @cache = Array.new(@m) { Array.new(@n, 0) }
    0.upto(@m - 1) do |i|
        0.upto(@n - 1) do |j|
            result = [result, dfs(matrix, i, j)].max
        end
    end

    result
end

def dfs(matrix, i, j)
    return @cache[i][j] if @cache[i][j] != 0
    curr = matrix[i][j]
    @cache[i][j] = 1 + [
        i > 0 && curr < matrix[i - 1][j] ? dfs(matrix, i - 1, j) : 0,       # up
        j > 0 && curr < matrix[i][j - 1] ? dfs(matrix, i, j - 1) : 0,       # left
        i < @m - 1 && curr < matrix[i + 1][j] ? dfs(matrix, i + 1, j) : 0,  # down
        j < @n - 1 && curr < matrix[i][j + 1] ? dfs(matrix, i, j + 1) : 0   # right
    ].max # In return of last statement is returned and assigned the value assigned is returned
end


# Key Insights:
# 1. Works for largest increasing or decreasing
# 2. We need to store the longest path upto every node in a cache

# Approach 1: DFS
# No Implmentation
# Steps:
# 1. Do a DFS from each node to get the maximum path from that node
# 2. Further do a DFS only if the path is increase, (curr val < next node's val)
# Time: O(2 ^ (m + n))
# Space: O(mn), Stack

# Approach 2: DFS with Memoization
# 1. Iterate through every neighbour and do a DFS, which return the longest inc path from that i, j
# 2. Use cache to cache visited nodes and their longest inc path
# 3. Within the DFS for every up, down, left, right nbr do a dfs
#    if only if the curr value < than the nbr's value
# 4. If a node was found in cache during the DFS to be non-zero then use the cached value
# Time: O(mn), O(V) = O(mn), O(E) = O(4V) = O(mn).
# Space: O(mn), For the memoization


require 'test/unit'
extend Test::Unit::Assertions

assert_equal(longest_increasing_path([[9,9,4],[6,6,8],[2,1,1]]), 4)
assert_equal(longest_increasing_path([[3,4,5],[3,2,6],[2,2,1]]), 4)
assert_equal(longest_increasing_path([[1]]), 1)
assert_equal(longest_increasing_path([[1,2]]), 2)
assert_equal(longest_increasing_path([[1,2],[2,3]]), 3)
assert_equal(longest_increasing_path([[6,8],[7,2]]), 2)
assert_equal(longest_increasing_path([[7,7,5],[2,4,6],[8,2,0]]), 4)

