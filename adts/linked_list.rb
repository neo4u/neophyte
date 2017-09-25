class Node
  attr_accessor :val, :next

  def initialize(val, next_node)
    @val = val
    @next = next_node
  end
end

class LinkedList
  def initialize(val)
    @head = Node.new(val, nil)
  end

  def add(val)
    current = @head                                 # Start from the head
    current = current.next until current.next.nil?  # Navigate upto last node
    current.next = Node.new(val, nil)               # Insert the new lement
  end

  def delete(val)
    if @head.val == val
      @head = @head.next
      return true
    end
    prev = @head                                                          # Mark prev as head
    curr = @head.next                                                     # Mark after head element as curr
    prev, curr = curr, curr.next until curr.next.nil? || curr.val == val  # Keep navigating until you find the value or reach the end
    raise 'Value Not Found' if curr.next.nil? && curr.val != val          # Error if value was not found
    prev.next = curr.next                                                 # Set the next of prev element to next of curr elmnt
    curr = nil
  end

  def show
    elements = []
    current = @head
    until current.next.nil?
      elements << current.val
      current = current.next
    end
    elements << current.val
    puts elements.inspect
  end
end

ll = LinkedList.new(1)
ll.show

ll.add(5)
ll.show

ll.add(6)
ll.add(7)
ll.add(8)
ll.add(2000)
ll.show

ll.delete(2000)
ll.show
