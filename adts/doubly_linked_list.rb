class Node
  attr_accessor :val, :next, :prev

  def initialize(val, prev_node, next_node)
    @val = val
    @prev = prev_node
    @next = next_node
  end

  def to_s
    node_prev = @prev.nil? ? 'nil' : @prev.val
    node_next = @next.nil? ? 'nil' : @next.val
    print("( prv:#{node_prev}, val:#{@val}, nxt:#{node_next} )")
  end
end

class LinkedList
  def initialize(val)
    @head = Node.new(val, nil, nil)
  end

  def add(val)
    curr = @head                            # Start from the head
    curr = curr.next until curr.next.nil?   # Navigate upto last node
    curr.next = Node.new(val, curr, nil)    # Insert the new element
  end

  def delete(val)
    if @head.val == val
      @head = @head.next
      @head.prev = nil
      return true
    end
    prev = @head                                                          # Mark prev as head
    curr = @head.next                                                     # Mark after head element as curr
    prev, curr = curr, curr.next until curr.next.nil? || curr.val == val  # Keep navigating until you find the value or reach the end
    raise 'Value Not Found' if curr.next.nil? && curr.val != val          # Error if value was not found
    prev.next = curr.next                                                 # Set the next of prev element to next of curr elmnt
    curr.next.prev = prev unless curr.next.nil?                           # Set prev of element after deleted to one before deleted
    curr = nil
  end

  def show()
    current = @head
    until current.next.nil?
      print(current.to_s)
      current = current.next
      print(' -> ')
    end
    print(current.to_s)
    puts
  end
end

ll = LinkedList.new(1)
ll.show()

ll.add(5)
ll.show()

ll.add(6)
ll.add(7)
ll.add(8)
ll.add(2000)
ll.show

ll.delete(2000)
ll.show()

ll.delete(5)
ll.show()
