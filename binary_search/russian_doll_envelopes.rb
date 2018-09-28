# @param {Integer[][]} envelopes
# @return {Integer}
def max_envelopes(envelopes)
    tails, n = [], envelopes.size()
    # Concept of patience sorting. ???? WTF
    # sort first by increasing width
    # within each subarray of same-width envelopes
    # sort by decreasing height
    envelopes.sort!() do |x, y|
        if x[0] != y[0]
            x[0] - y[0]
        else
            y[1] - x[1] # This is KEY for this ordering to work
        end
    end

    # now find the length of the longest increasing subsequence of heights.
    # Since each same-width block was sorted non-increasing, 
    # we can only pick at most one height within each block
    # otherwise, the sequence would be non-increasing
    0.upto(n - 1) do |i|
        e = envelopes[i]
        p = binary_search(tails, e)
        p == tails.size ? tails.push(e) : tails[p] = e
    end

    tails.size
end

def binary_search(a, key)
    l, r = 0, a.size

    while l < r
        mid = (l + r) / 2
        a[mid][1] < key[1] ? l = mid + 1 : r = mid
    end

    l
end

# Sort the envelopes first by increasing width. For each block of same-width envelopes, sort by decreasing height.
# Then find the longest increasing subsequence of heights.
# Since each same-width subarray is non-increasing in height, we can never pick more than one height within each width (otherwise heights would be non-increasing)
# Thus, the resulting longest increasing heights subsequence is also increasing in width.

# Example:

# input
# [[5,4],[6,4],[6,7],[2,3]]

# sort by increasing widths, then decreasing heights:
# [[2,3],[5,4],[6,7],[6,4]]

# Get the heights:
# [3,4,7,4]

# Find the length longest increasing subsequence:
# [3,4,7]

# (Note that we could not have picked more than one evelope with width 6)

# Answer: 3
# Time: O(log(n))
# Space: O(n)

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(max_envelopes([[5,4],[6,4],[6,7],[2,3]]), 3)
assert_equal(max_envelopes([[4,5],[4,6],[6,7],[2,3],[1,1]]), 4)
