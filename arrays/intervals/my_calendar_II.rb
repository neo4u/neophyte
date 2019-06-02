class Node
    attr_accessor :s, :e, :left, :right, :single_overlap

    def initialize(s, e)
        @s = s
        @e = e
        @left = nil
        @right = nil
        @single_overlap = false
    end
end

class MyCalendarTwo
    def initialize()
        @root = nil
    end

    def book(s, e)
        return false if !insertable?(s, e, @root)

        insert(s, e, @root)
        true
    end

    def insertable?(s, e, insert_root)
        return true if !insert_root
        return true if s >= e

        if e <= insert_root.s
            insertable?(s, e, insert_root.left)
        elsif s >= insert_root.e
            insertable?(s, e, insert_root.right)
        else # Overlap
            if insert_root.single_overlap
                false
            elsif s >= insert_root.s && e <= insert_root.e
                true
            else
                insertable?(s, insert_root.s, insert_root.left) && insertable?(insert_root.e, e, insert_root.right)
            end
        end
    end

    private
    # O(logH) solution, where H is the height of BT - we can improve further if we use balanced binary trees
    def insert(s, e, insert_root)
        node = Node.new(s, e)
        @root = node if !@root
        return node if !insert_root

        if s >= insert_root.e
            insert_root.right = insert(s, e, insert_root.right)
        elsif e <= insert_root.s
            insert_root.left = insert(s, e, insert_root.left)
        else # Overlap
            insert_root.single_overlap = true
            a = [insert_root.s, s].min
            b = [insert_root.s, s].max
            c = [insert_root.e, e].min
            d = [insert_root.e, e].max

            insert_root.s, insert_root.e = b, c
            insert_root.left, insert_root.right = insert(a, b, insert_root.left), insert(c, d, insert_root.right)
        end

        insert_root
    end
end


require 'test/unit'
extend Test::Unit::Assertions

calendar = MyCalendarTwo.new()
assert_equal(calendar.book(10, 20), true)
assert_equal(calendar.book(50, 60), true)
assert_equal(calendar.book(10, 40), true)
assert_equal(calendar.book(5, 15), false)
assert_equal(calendar.book(5, 10), true)
assert_equal(calendar.book(25, 55), true)
