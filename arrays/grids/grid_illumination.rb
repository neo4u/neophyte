def illuminate(grid)
    n = grid.size
    lamps = find_lamps(grid)

    # Illuminate row
    lamps.each do |lit_r, lit_c|

    end


end

def find_lamps(grid)
    n = grid.size
    lamps = []

    0.upto(n - 1) do |r|
        0.upto(n - 1) do |c|
            lamps.push([r, c]) if grid[r][c]
        end
    end

    lamps
end

# Problem Statement:
# Given an NxN grid with an array of lamp coordinates.
# Each lamp provides illumination to:
# - every square on its x axis,
# - every square on its y axis, and
# - every square that lies on its diagonal (think of a Queen in chess).
# Given an array of  query coordinates, determine whether or not the query point is illuminated.
# Moreover, whenever you execute a query, all lamps adjacent to or on that query point are permanently un-illuminated.
# The ranges for the variables/arrays is:
# 10^3 < N < 10^9, 10^3 < lamps < 10^9, 10^3 < queries < 10^9.

# Example: 
# n = 5, lamps = [[2,1], [2,2]]
# [[0, 0, 0, 0, 0], | [0, 0,  0, 3, 0],
#  [0, 0, 0, 0, 0], | [1, 0,  3, 0, 0],
#  [0, 1, 1, 0, 0], | [0, 1|3,0, 0, 0],
#  [0, 0, 0, 0, 0], | [3, 0,  1, 0, 0],
#  [0, 0, 0, 0, 0]] | [0, 0,  0, 0, 0]]
# illiminate the row for 2, 1
# [[0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0],
#  [1, 1, 1, 1, 1],
#  [0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0]
# illuminate the column for 2, 1
# [[0, 1, 0, 0, 0],
#  [0, 1, 0, 0, 0],
#  [1, 1, 1, 1, 1],
#  [0, 1, 0, 0, 0],
#  [0, 1, 0, 0, 0]]
# illuminate both diagonals for 2, 1
# [[0, 1, 0, 1, 0],
#  [1, 1, 1, 0, 0],
#  [1, 1, 1, 1, 1],
#  [1, 1, 1, 0, 0],
#  [0, 1, 0, 1, 0]]

# Similar 3 step illumination for 2, 2, results in:
# [[1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 0],
#  [1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 0],
#  [1, 1, 1, 1, 1]]


require 'test/unit'
extend Test::Unit::Assertions

assert_equal(grid_illumination, )
