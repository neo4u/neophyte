
# Steps
# Split
# Sort split parts in place

def partition(a, p, r)
	i, pivot = p - 1, a[r]			# Choose the index before the pth index and Choose the last element as pivot

	p.upto(r - 1) do |j|			# Loop from p to r-1 swapping elements to either side of pivot
		next if a[j] > pivot		# Move to next if curr element greater than pivot
		i += 1						# Increment index i for current pivot placement index
		a[i], a[j] = a[j], a[i]		# Swap elements at pivot placement index with the current index j
	end

	a[i + 1], a[r] = a[r], a[i + 1] # Move the pivot element to its final place: index before which elements < pivot
	i + 1							# return pivot index
end

def quick_sort(a, p = nil, r = nil)
	p, r = 0, a.size - 1 if p.nil? && r.nil?
	return if p >= r

	q = partition(a, p, r)
	quick_sort(a, p, q - 1)
	quick_sort(a, q + 1, r)

	a
end

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(quick_sort([1,2,3,4,5,6,7]), [1,2,3,4,5,6,7])
assert_equal(quick_sort([7,6,5,4,3,2,1]), [1,2,3,4,5,6,7])
assert_equal(quick_sort([7,6,5,4,3,2,2,2,2,2,1]), [1,2,2,2,2,2,3,4,5,6,7])