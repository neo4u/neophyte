# @param {Integer[][]} envelopes
# @return {Integer}
def max_envelopes(envelopes)
    heights, size = [], 0

    # Sort widths in inc order
    # When width matches, Sort by dec height
    envelopes.sort!() do |x, y|
        x[0] != y[0] ? x[0] - y[0] : y[1] - x[1]
    end

    envelopes.each do |e|
        pos = binary_search(heights, e[1])

        if pos == heights.size # Literal visualization of add or replace (a lil slower)
            heights.push(e[1])
            size += 1
        else
            heights[pos] = e[1]
        end
    end

    size
end

def binary_search(heights, h)
    l, r = 0, heights.size - 1

    while l <= r
        mid = (l + r) / 2
        return mid if heights[mid] == h
        heights[mid] < h ? l = mid + 1 : r = mid - 1
    end

    l
end


# 354. Russian Doll Envelopes
# https://leetcode.com/problems/russian-doll-envelopes/

# Sort the envelopes first by increasing width. For each block of same-width envelopes, sort by decreasing height.
# Then find the longest increasing subsequence of heights.
# Since each same-width sub-array is non-increasing in height, we can never pick more than one height within each width (otherwise heights would be non-increasing)
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
# ----------------------------------------------------------------------------
# My own understanding
# 1. width needs to be strictly increasing
# 2. Height needs to also be strictly increasing

# So if you have the following example set of envelopes: [3,4], [1,2],[3,5]
# if you sort by like this: [1,2], [3,4], [3,5]
# Then you're wrong because while height is strictly inc, width is not

# We've to do something like this:
# for each same width set of envelopes we need to select only the highest height

# An algorithm for such an exact situation is: LIS to the find the strictly inc heights
# So sort inc by width and sort dec by height and do the LIS algorithm on heights
# ----------------------------------------------------------------------------

# Time: O(nlog(n))
# Space: O(n)

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(max_envelopes([[5,4],[6,4],[6,7],[2,3]]), 3)
assert_equal(max_envelopes([[4,5],[4,6],[6,7],[2,3],[1,1]]), 4)
