def can_attend_meetings(intervals)
    intervals.sort_by! { |a, b| a[0] < b[0] }
    p intervals
    0.upto(intervals.size - 1) do |i|
        return false if i > 0 && intervals[i][0] < intervals[i - 1][1]
    end

    true
end


require 'test/unit'
extend Test::Unit::Assertions


assert_equal(can_attend_meetings([[1,5],[8,9]]), true)
assert_equal(can_attend_meetings([[7,10],[2,4]]), true)

