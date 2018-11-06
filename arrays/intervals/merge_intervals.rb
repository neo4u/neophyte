# Definition for an interval.
class Interval
    attr_accessor :start, :end
    def initialize(s=0, e=0)
        @start = s
        @end = e
    end
end

# @param {Interval[]} intervals
# @return {Interval[]}
def merge(intervals)
    intervals.sort_by!(&:start)
    merged = []
    
    intervals.each do |i|
        if merged.empty? || merged.last.end < i.start
            merged.push(i)
        else
            merged.last.end = [merged.last.end, i.end].max
        end
    end
    
    merged
end

# 56. Merge Intervals
# https://leetcode.com/problems/merge-intervals/description/

# Approach
# 1. sort by start times
# 2. iterate through interval
# 3. if last of merged has end time < curr intervals start
#    then push the element into merged as it is not overlapping
# 4. if overlappping then merge with last interval by taking max of the ends of merged.last.end and curr.end

# Complexity Analysis
# Time: O(nlog(n)), Due to the sort
# Space: O(1), Sort in-place

require 'test/unit'
extend Test::Unit::Assertions

intervals_arr = [[1,3],[2,6],[8,10],[15,18]]
intervals = intervals_arr.map do |i|
    Interval.new(*i)
end

expected_intervals_arr = [[1,6],[8,10],[15,18]]
expected_intervals = expected_intervals_arr.map do |i|
    Interval.new(*i)
end

ret_ints = merge(intervals)
assert_equal(ret_ints.length, expected_intervals.length)
0.upto(expected_intervals.length - 1) do |i|
    assert_equal(ret_ints[i].start, expected_intervals[i].start)
    assert_equal(ret_ints[i].end, expected_intervals[i].end)
end
