# @param {Integer[][]} matrix
# @return {Void} Do not return anything, modify matrix in-place instead.
def rotate(matrix)
  m, n = matrix.length, matrix[0].length
  puts "Before"
  puts matrix.map(&:inspect)
  matrix.reverse!
  0.upto(m - 1) do |i|
    0.upto(i - 1) do |j|
      matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    end
  end
  puts "After"
  puts matrix.map(&:inspect)
  matrix
end

def anti_rotate(matrix)
  m, n = matrix.length, matrix[0].length
  puts "Before"
  puts matrix.map(&:inspect)
  matrix.each { |row| row.reverse! }
  0.upto(m - 1) do |i|
    0.upto(i - 1) do |j|
      matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    end
  end
  puts "After"
  puts matrix.map(&:inspect)
  matrix
end

require "test/unit"
extend Test::Unit::Assertions

in_matrix = [[1,2,3],
             [4,5,6],
             [7,8,9]]

out_matrix = [[7,4,1],
              [8,5,2],
              [9,6,3]]

assert_equal(rotate(in_matrix), out_matrix)

in_matrix = [[ 5, 1, 9,11],
             [ 2, 4, 8,10],
             [13, 3, 6, 7],
             [15,14,12,16]]

out_matrix = [[15,13, 2, 5],
              [14, 3, 4, 1],
              [12, 6, 8, 9],
              [16, 7,10,11]]
assert_equal(rotate(in_matrix), out_matrix)

in_matrix = [[1,2,3],
             [4,5,6],
             [7,8,9]]

out_matrix = [[3,6,9],
              [2,5,8],
              [1,4,7]]

assert_equal(anti_rotate(in_matrix), out_matrix)

in_matrix = [[ 5, 1, 9,11],
             [ 2, 4, 8,10],
             [13, 3, 6, 7],
             [15,14,12,16]]

out_matrix = [[11, 10, 7, 16],
              [9, 8, 6, 12],
              [1, 4, 3, 14],
              [5, 2, 13, 15]]
assert_equal(anti_rotate(in_matrix), out_matrix)
