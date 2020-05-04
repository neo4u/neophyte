# Definition for an interval.
class Interval
    attr_accessor :start, :end
    def initialize(s=0, e=0)
        @start = s
        @end = e
    end
end

# @param {Interval[]} intervals
# @param {Interval} new_interval
# @return {Interval[]}
def insert(intervals, new_interval)
    return [new_interval] if !intervals || intervals.empty?
    return intervals if !new_interval
    n = intervals.size

    # The map below is essentially just doing what is being done in the below code, but concisely without storing permanent variables
    # starts, ends = Array.new(n), Array.new(n)
    # 0.upto(n - 1) do |i|
    #     starts[i] = intervals[i].start
    #     ends[i] = intervals[i].end
    # end

    # If we can't find elements in the array that match the criteria (bsearch returns nil), choose n as the index
    # Before bsearch we're doing to_a as bsearch only works on Array and not on Enumerator type, map however works on enumerator type
    i = intervals.each_with_index.map.to_a.bsearch { |e, _| e.end >= new_interval.start }&.last || n # equivalent to bisect_left in python, O(log(n))
    j = intervals.each_with_index.map.to_a.bsearch { |s, _| s.start > new_interval.end }&.last || n # equivalent to bisect_right in python, O(log(n))

    new_interval.start = [new_interval.start, intervals[i].start].min if i < n  # We merge new_int's start with interval[i]'s start,
                                                                                # i because, all intervals < index i don't have any overlap with the new_intvl, overlap can only occur in ith inteval,
                                                                                # because of the condition e >= new_interval.start while doing a binary search
    new_interval.end = [new_interval.end, intervals[j - 1].end].max if 0 < j    # We merge new_int's end with intervals[j - 1]'s end,
                                                                                # j - 1 because, intervals with index j and greater don't have any overlap with the new_intvl

    left = intervals[0, i]
    right = intervals[j, n]

    left + [new_interval] + right # O(n), stiching the arrays together
end


# 57. Insert Interval
# https://leetcode.com/problems/insert-interval/

# Intuition
# 1. We're given a list of intervals sorted by the start time,
#    also an interval to insert which could overlap with one or more existing intervals
# 2. We've to handle overlap accordingly, For ex:
#    - No Overlap: intervals = [[1, 2], [9, 10]] and to_insert = [5, 8] := result = [[1, 2], [5, 8], [9, 10]]
#    - Full Overlap: intervals = [[1, 2], [5, 10]] and to_insert = [5, 8] := result = [[1, 2], [5, 10]]
#    - 1 Overlap: intervals = [[1, 2], [8, 10]] and to_insert = [5, 9] := result = [[1, 2], [5, 10]]
#    - > 1 Overlap: intervals = [[1, 5], [8, 10]] and to_insert = [4, 9] := result = [[1, 10]]

# Approach 1: Binary Search on starts and ends arrays
# Steps
# 1. Binary Search ends for e >= new_interval.start,
#    i.e. Find the index i into intervals where all the ends to the left of i are < new_interval[0]
# 2. Binary Search starts for s > new_interval.end,
#    i.e. Find the index into intervals where all the starts to the right of i are > new_interval[0]
# 3. Use n if there is no such index for both the searches
# 4. Merge new_interval's start with interval i's start
# 5. Merge new_interval's end with interval j - 1's end
# 6. Final form the left part, middle part and right part
# 6. Return the combination of the tree parts



require 'test/unit'
extend Test::Unit::Assertions

intervals = [
    Interval.new(1,3),
    Interval.new(6,9)
]
new_interval = Interval.new(2,5)
output = insert(intervals, new_interval)

assert_equal(output[0].start, 1)
assert_equal(output[0].end, 5)
assert_equal(output[1].start, 6)
assert_equal(output[1].end, 9)

intervals = [
    Interval.new(1,2),
    Interval.new(3,5),
    Interval.new(6,7),
    Interval.new(8,10),
    Interval.new(12,16)
]
new_interval = Interval.new(4,8)
output = insert(intervals, new_interval)
[
    Interval.new(1,2),
    Interval.new(3,10),
    Interval.new(12,16)
]
assert_equal(output[0].start, 1)
assert_equal(output[0].end, 2)
assert_equal(output[1].start, 3)
assert_equal(output[1].end, 10)
assert_equal(output[2].start, 12)
assert_equal(output[2].end, 16)

intervals = [
    Interval.new(1,5),
]
new_interval = Interval.new(2,3)
output = insert(intervals, new_interval)
assert_equal(output[0].start, 1)
assert_equal(output[0].end, 5)

intervals = [
    Interval.new(1,2),
    Interval.new(6,9)
]
new_interval = Interval.new(3,5)
output = insert(intervals, new_interval)
assert_equal(output[0].start, 1)
assert_equal(output[0].end, 2)
assert_equal(output[1].start, 3)
assert_equal(output[1].end, 5)
assert_equal(output[2].start, 6)
assert_equal(output[2].end, 9)
