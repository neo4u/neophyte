# @param {Integer[][]} matrix
# @param {Integer} target
# @return {Boolean}
def search_matrix(matrix, target)
    m = matrix.length
    return false if m == 0
    b = matrix[0].length
    return false if b == 0
    i, j = 0, n - 1

    while i < rows and j >= 0
        if matrix[i][j] < target
            i += 1
        elsif matrix[i][j] > target
            j -= 1
        else
            return true
        end
    end

    false
end




# 240. Search a 2D Matrix II
# https://leetcode.com/problems/search-a-2d-matrix-ii/


# Key Insight:
# We start searching the matrix from top right corner,
# initialize the current position to top right corner,
# if the target is greater than the value in current position,
# then the target can not be in entire row of current position because the row is sorted,
# if the target is less than the value in current position,
# then the target can not in the entire column because the column is sorted too.
# We can rule out one row or one column each time,
# so the time complexity is O(m+n).

