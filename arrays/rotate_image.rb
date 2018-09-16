# @param {Integer[][]} matrix
# @return {Void} Do not return anything, modify matrix in-place instead.
def rotate(a)
	n = a.size - 1

	0.upto(n / 2) do |row|
		row.upto(n - 1 - row) do |col|
			tmp = a[row][col] 					 	# save top
			a[row][col] = a[n - col][row]		 	# left to top
			a[n - col][row] = a[n - row][n - col]	# bottom to left
			a[n - row][n - col]	= a[col][n - row]	# right to bottom
			a[col][n - row] = tmp					# top to right
		end
	end

	a
end

def rotate_anti(a)
	n = a.size - 1

	0.upto(n / 2) do |row|
		row.upto(n - 1 - row) do |col|
			tmp = a[row][col] 					 	# save top
			a[row][col] = a[col][n - row]		 	# right to top
			a[col][n - row] = a[n - row][n - col]	# bottom to right
			a[n - row][n - col]	= a[n - col][row]	# left to bottom
			a[n - col][row] = tmp					# top to right
		end
	end

	a
end

require 'test/unit'
extend Test::Unit::Assertions

a = [
	[1,2,3],
	[4,5,6],
	[7,8,9]
]
rotated_a = [
	[7,4,1],
	[8,5,2],
	[9,6,3]
]
assert_equal(rotate(a), rotated_a)

a = [
	[ 5, 1, 9,11],
	[ 2, 4, 8,10],
	[13, 3, 6, 7],
	[15,14,12,16]
]
rotated_a =  [
	[15,13, 2, 5],
	[14, 3, 4, 1],
	[12, 6, 8, 9],
	[16, 7,10,11]
]
assert_equal(rotate(a), rotated_a)

a = [
	[1,2,3],
	[4,5,6],
	[7,8,9]
]
rotated_a = [
	[3,6,9],
	[2,5,8],
	[1,4,7]
]
assert_equal(rotate_anti(a), rotated_a)

a = [
	[1,2,3,4],
	[5,6,7,8],
	[9,10,11,12],
	[13,14,15,16]
]
rotated_a =  [
	[4,8,12,16],
	[3,7,11,15],
	[2,6,10,14],
	[1,5,9,13]
]
assert_equal(rotate_anti(a), rotated_a)