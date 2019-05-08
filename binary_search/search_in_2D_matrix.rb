# Approach 1: Virtual flattening the matrix
def search_matrix(matrix, target)
    return false if !matrix || matrix.empty? || !matrix[0] || matrix[0].empty?

    m, n = matrix.size, matrix[0].size
    l, r = 0, m * n - 1

    while l <= r
        mid = (l + r) / 2
        x = matrix[mid / n][mid % n]
        return true if x == target

        x < target ? l = mid + 1 : r = mid - 1
    end

    false
end

# Approach 2: 2D binary search, to find vertically or horizontally
# def search_matrix_dual(matrix, target)
#     return false if !matrix || matrix.empty? || !matrix[0] || matrix[0].empty?
#     @m, @n = matrix.size, matrix[0].size
#     min = [@m, @n].min

#     0.upto(min - 1) do |i|
#         return true if binary_search(matrix, target, i, true)
#         return true if binary_search(matrix, target, i, false)
#     end

#     false
# end

# def binary_search(matrix, target, start, vertical)
#     l = start
#     r = vertical ? @n - 1 : @m - 1

#     while l <= r
#         mid = (l + r) / 2
#         x = vertical ? matrix[start][mid] : matrix[mid][start]
#         x < target ? l = mid + 1 : r = mid - 1
#         return true if x == target
#     end

#     false
# end


# Approach 3: Find row first and then search in row
def search_matrix_find_row_then_in_row(matrix, target)
    return false if !matrix || matrix.empty? || !matrix[0] || matrix[0].empty?
    @m, @n = matrix.size, matrix[0].size

    row = binary_search_find_row(matrix, 0, @m - 1, @n - 1, target) # Find row
    return false if row > @m - 1
    return true if matrix[row][@n - 1] == target

    binary_search_check_row(matrix, 0, @n - 1, row, target)         # Find in row
end

def binary_search_find_row(matrix, l, r, col, target)
    while l <= r
        mid = (l + r) / 2
        x = matrix[mid][col]
        return mid if x == target
        x < target ? l = mid + 1 : r = mid - 1
    end

    l
end

def binary_search_check_row(matrix, l, r, row, target)
    while l <= r
        mid = (l + r) / 2
        x = matrix[row][mid]
        return true if x == target
        x < target ? l = mid + 1 : r = mid - 1
    end

    false
end


# 74. Search a 2D Matrix
# https://leetcode.com/problems/search-a-2d-matrix/description/


# Key Insights:
# 1. We can virtually flatten using clever indexing and do a simple binary search
# 2. Another way is to find the row and find the column within that row, Thus a double binary search if you will.

# Approach 1: Virtual flattening the matrix
# Approach 2: 2D binary search, to find vertically and horizontally
# Approach 3: Find row, then check in row

require 'test/unit'
extend Test::Unit::Assertions

matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
assert_equal(search_matrix(matrix, target), true)
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
assert_equal(search_matrix(matrix, target), false)


matrix = [
    [1,   3,  5,  7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
  ]
target = 3
assert_equal(search_matrix_dual(matrix, target), true)
matrix = [
[1,   3,  5,  7],
[10, 11, 16, 20],
[23, 30, 34, 50]
]
target = 51
assert_equal(search_matrix_dual(matrix, target), false)


matrix = [
    [1,   3,  5,  7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
  ]
target = 3
assert_equal(search_matrix_find_row_then_in_row(matrix, target), true)
matrix = [
[1,   3,  5,  7],
[10, 11, 16, 20],
[23, 30, 34, 50]
]
target = 51
assert_equal(search_matrix_find_row_then_in_row(matrix, target), false)


