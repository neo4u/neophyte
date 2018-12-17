# Definition for an interval.
# class Interval
#     attr_accessor :start, :end
#     def initialize(s=0, e=0)
#         @start = s
#         @end = e
#     end
# end

# @param {Interval[]} intervals
# @return {Boolean}
def can_attend_meetings(intervals)
    intervals.sort_by!(&:start)
    0.upto(intervals.size - 1) do |i|
        return false if i > 0 && intervals[i].start < intervals[i - 1].end
    end
    
    true
end