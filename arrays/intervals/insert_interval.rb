def insert(intervals, new_interval)
    return [new_interval] if intervals.empty?
    ix1 =  intervals.map(&:end).each_with_index.to_a.bsearch do |e,_|
        e >= new_interval.start
    end&.last

    ix2 = intervals.map(&:start).each_with_index.to_a.bsearch do |s,_|
        s > new_interval.end
    end&.last

    if ix1.nil?
        intervals + [new_interval]
    elsif ix1 == ix2
        intervals[0...ix1] + [new_interval] + intervals[ix1..-1]
    else
        ix2 ||= intervals.size
        s = [intervals[ix1].start, new_interval.start].min
        e = [intervals[ix2-1].end, new_interval.end].max
        intervals[0...ix1] + [Interval.new(s,e)] + intervals[ix2..-1]
    end
end

# 57. Insert Interval
# https://leetcode.com/problems/insert-interval/

# By far the best solution I have seen is of O(n) time (some solutions claim to be of O(logn) turns out to be O(n)).
# One of the simplest ideas is to compare each interval in intervals (intervals[i])
# with newInterval and then perform respective operations according to their relationships.

# If they overlap, merge them to newInterval;
# If intervals[i] is to the left of newInterval, push intervals[i] to the result vector;
# If newInterval is to the left of intervals[i], push newInterval and all the remaining intervals (intervals[i], ..., intervals[n - 1]) to the result vector.
# The code is as follows.

# Time: O(log(n)) or O(n). Not fully sure the finds for low and high take log(n),
#       but the last return statement may take O(n)
# Space: O(n)
