def selection_sort(a)
	n = a.size
	0.upto(n - 1) do |i|
		min_idx = i
		(i + 1).upto(n - 1) do |j|
			min_idx = j if a[j] < a[min_idx]
		end
		a[min_idx], a[i] = a[i], a[min_idx]
	end

	a
end

# Two loops
# 1. to iterate through array elements and pick the minimum index
# 2. iterate through rest of the array to pick the element lesser than minimum index

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(selection_sort([1,2,3,4,5,6,7]), [1,2,3,4,5,6,7])
assert_equal(selection_sort([7,6,5,4,3,2,1]), [1,2,3,4,5,6,7])
assert_equal(selection_sort([7,6,5,4,3,2,2,2,2,2,1]), [1,2,2,2,2,2,3,4,5,6,7])
