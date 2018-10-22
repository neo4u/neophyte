# Steps

# split
# sort
# merge

def merge(a, p, q, r)
	n1, n2 = q - p + 1, r - (q + 1) + 1
	left, right = [], []

	0.upto(n1 - 1) do |i|
		left[i] = a[p + i]
	end

	0.upto(n2 - 1) do |j|
		right[j] = a[q + 1 + j]
	end

	p.upto(r) do |k|
		return if left.empty? && right.empty?

		a[k] = 	if left.empty? && !right.empty?
					right.shift
				elsif right.empty? && !left.empty?
					left.shift
				else
					left.first < right.first ? left.shift : right.shift 
				end
	end
end

def merge_sort(a, p = nil, r = nil)
	p, r = 0, a.size - 1 if p.nil? && r.nil?
	return if p >= r

	q = (p + r) / 2
	merge_sort(a, p, q)
	merge_sort(a, q + 1, r)
	merge(a, p, q, r)

	a
end

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(merge_sort([1,2,3,4,5,6,7]), [1,2,3,4,5,6,7])
assert_equal(merge_sort([7,6,5,4,3,2,1]), [1,2,3,4,5,6,7])
assert_equal(merge_sort([7,6,5,4,3,2,2,2,2,2,1]), [1,2,2,2,2,2,3,4,5,6,7])
