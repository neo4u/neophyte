# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Float}
def find_median_sorted_arrays(a, b)
  k = (a.size + b.size) / 2

  even = (a.size + b.size).even?
  ans = find(a, b, k + 1).to_f

  (ans + real_find(a, b, k)) / 2 if even
end

def find(a, b, k)
  loop do
    a, b = b, a if a.size > b.size

    return b[k - 1] if a.empty?
    return [a.first, b.first].min if k == 1

    x = [a.size, k / 2].min
    y = k - x;
    ax = a[x - 1]
    by = b[y - 1]

    return ax if ax == by

    if ax > by
      b = b[y..-1]
      k -= y
    else
      a = a[x..-1]
      k -= x
    end
  end
end

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(find_median_sorted_arrays([1, 3], [2]), 2.0)
assert_equal(find_median_sorted_arrays([1, 2], [1, 2]), 2.5)
