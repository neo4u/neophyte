# @param {Integer[]} a
# @return {Integer}
def repeated_n_times(a)
    n = a.size / 2
    counts = Hash.new { |h, k| h[k] = 0 }
    a.each { |num| counts[num] += 1 }

    counts.select { |k, v| v == n }.keys.first
end


# Approach 2: Assuming disntance of 2 away.
# @param {Integer[]} a
# @return {Integer}
def repeated_n_times2(a)
    0.upto(a.size - 1) do |i|
        return a[i] if a[i - 1] == a[i] || a[i - 2] == a[i]
    end
end

# @param {Integer[]} a
# @return {Integer}
def repeated_n_times_for_clarity(a)
    0.upto(a.size - 1) do |i|
        if a[i - 1] == a[i]
            puts "Returning #{a[i]} because #{a[i - 1]} == #{a[i]} | i - 1: #{i - 1}, i: #{i}"
            return a[i]
        end

        if a[i - 2] == a[i]
            puts "Returning #{a[i]} because #{a[i - 2]} == #{a[i]} | i - 2: #{i - 2}, i: #{i}"
            return a[i]
        end
    end
end

# 961. N-Repeated Element in Size 2N Array
# https://leetcode.com/contest/weekly-contest-116/problems/n-repeated-element-in-size-2n-array/

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(repeated_n_times([1,2,3,3]), 3)
assert_equal(repeated_n_times([3,1,2,3]), 3)
assert_equal(repeated_n_times([2,1,2,5,3,2]), 2)
assert_equal(repeated_n_times([5,1,5,2,5,3,5,4]), 5)

assert_equal(repeated_n_times2([1,2,3,3]), 3)
assert_equal(repeated_n_times2([3,1,2,3]), 3)
assert_equal(repeated_n_times2([2,1,2,5,3,2]), 2)
assert_equal(repeated_n_times2([5,1,5,2,5,3,5,4]), 5)
