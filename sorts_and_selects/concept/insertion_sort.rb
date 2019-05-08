def insertion_sort(a)
    n = a.size

    1.upto(n - 1) do |j|
        i, key = j - 1, a[j]

        while i >= 0 && a[i] > key
            a[i + 1] = a[i]
            i -= 1
        end
        a[i + 1] = key #unless i == j - 1 # i + 1 holds the last moved element's position
    end

    a
end

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(insertion_sort([1,2,3,4,5,6,7]), [1,2,3,4,5,6,7])
assert_equal(insertion_sort([7,6,5,4,3,2,1]), [1,2,3,4,5,6,7])
assert_equal(insertion_sort([7,6,5,4,3,2,2,2,2,2,1]), [1,2,2,2,2,2,3,4,5,6,7])
