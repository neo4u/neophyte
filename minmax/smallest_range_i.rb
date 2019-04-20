# @param {Integer[]} a
# @param {Integer} k
# @return {Integer}
def smallest_range_i(a, k)
    [0, a.max - a.min - 2 * k].max
end

def smallest_range_i(a, k)
    max = a.max
    min = a.min

    mid = (max - min) / 2.0

    if a.length == 1
        0
    elsif  k >= mid
        0
    else
        (max - min) - k * 2
    end 
end

def smallest_range_i(a, k)
    return 0 if a.size == 1
    min, max = a.min, a.max
    return max - min if k.zero? # Can't get them any closer
    max_val -= k                # To make max_val as close to min_val as possible
    return 0 if max - min < k   # If max - min < k, then result will always be 0, as we can over shoot max by adding k to min
    return max - (min + k)      # Otherwise the min difference is max_val - min_val + K
end


# OP provided a confusing description of the problem, so I'll try to dumb it down:
# Given an array, and some number K, find the min value in the array, and the max value in the array.
# Then for any value , 0 <= offset <= K
# find the minimal difference between max_val +- offset and min_val +- offset
# The offset you choose for max_val and min_val can be different.
# For example, given K = 3
# You can do max_val + 1, and min_val - 2


# 908. Smallest Range I
# https://leetcode.com/problems/smallest-range-i/

# Key Insights
# 1. If min(A) + K < max(A) - K, then return max(A) - min(A) - 2 * K
#    If min(A) + K >= max(A) - K, then return 0
# 2. Explanation for If min(A) + K >= max(A) - K, then return 0.
#    Because it means your min with +K can at least equal or overshoot your max with -K,
#    thus if you were to actually pick a K for the min and max, you can have the min and max be equal.
#    Or put it the other way, if your min with the biggest K still can't reach your max - the biggest K,
#    then you cannot possibly have 0 as your difference, as you will end up with some sort of
#    difference between your min and max, even if you give both the min and the max the biggest K value possible.



require 'test/unit'
extend Test::Unit::Assertions

assert_equal(smallest_range_i([[1,2,3],[1,2,3],[1,2,3]]), [1,1])

assert_equal(smallest_range_i([1],0), 0)
assert_equal(smallest_range_i([0,10],2), 6)
assert_equal(smallest_range_i([1,3,6],3), 0)
assert_equal(smallest_range_i([7,8,8],5), 0)



