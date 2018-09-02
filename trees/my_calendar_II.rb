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

  # @param {TreeNode} root
  # @return Boolean
  def book(s, e)
    return false if !insertable?(s, e, @root)

    @root = insert(s, e, @root)
    true
  end

  def insertable?(s, e, root)
    return true if root.nil?
    return true if s >= e

    if e <= root.s
      insertable?(s, e, root.left)
    elsif s >= root.e
      insertable?(s, e, root.right)
    else # Overlap
      if root.single_overlap
        false
      elsif s >= root.s && e <= root.e
        true
      else
        insertable?(s, root.s, root.left) && insertable?(root.e, e, root.right)
      end
    end
  end

  private
  # O(logH) solution, where H is the height of BT - we can improve further if we use balanced binary trees
  def insert(s, e, root)
    return root = Node.new(s, e) if root.nil?
    return root if s >= e

    if s >= root.e
      root.right = insert(s, e, root.right)
    elsif e <= root.s
      root.left = insert(s, e, root.left)
    else # Overlap
      root.single_overlap = true
      a = [root.s, s].min
      b = [root.s, s].max
      c = [root.e, e].min
      d = [root.e, e].max

      root.s, root.e = b, c
      root.left, root.right = insert(a, b, root.left), insert(c, d, root.right)
    end

    root
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
