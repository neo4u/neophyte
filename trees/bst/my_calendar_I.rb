class Node
    attr_accessor :left, :right, :s, :e

    def initialize(s, e)
        @s = s
        @e = e
        @left = @right = nil
    end
end

class MyCalendar
    def initialize()
        @root = nil
    end

    def book(s, e)
        !insert(Node.new(s, e)).nil?
    end

    private
    def insert(node, root = nil)
        return @root = node if @root.nil?
        root = @root if root.nil?

        if node.e <= root.s
            root.left.nil? ? root.left = node : insert(node, root.left)
        elsif node.s >= root.e
            root.right.nil? ? root.right = node : insert(node, root.right)
        else
            nil
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
