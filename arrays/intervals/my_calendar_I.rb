class Node
    attr_accessor :left, :right, :s, :e

    def initialize(s, e)
        @s, @e = s, e
        @left, @right = nil, nil
    end
end

class MyCalendar
    def initialize()
        @root = nil
    end

    def book(s, e)
        !insert(s, e, @root).nil?
    end

    private
    def insert(s, e, insert_root)
        @root = Node.new(s, e) if !@root
        return @root if !insert_root

        if e <= insert_root.s
            return insert_root.left ? insert(s, e, insert_root.left) : insert_root.left = Node.new(s, e)
        elsif s >= insert_root.e
            return insert_root.right ? insert(s, e, insert_root.right) : insert_root.right = Node.new(s, e)
        else
            return nil
        end
    end
end


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar.new()
# param_1 = obj.book(start, end)

# 729. My Calendar I
# https://leetcode.com/problems/my-calendar-i/description/

require 'test/unit'
extend Test::Unit::Assertions

calendar = MyCalendar.new()
assert_equal(calendar.book(10, 20), true)
assert_equal(calendar.book(15, 25), false)
assert_equal(calendar.book(20, 30), true)
assert_equal(calendar.book(29, 31), false)
assert_equal(calendar.book(5, 9), true)
assert_equal(calendar.book(1, 6), false)
