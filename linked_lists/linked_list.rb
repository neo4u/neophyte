#!/usr/bin/env ruby

class Node
  attr_accessor :val, :nxt

  def initialize(val, nxt_node)
    @val = val
    @nxt = nxt_node
  end
end

class LinkedList
  def initialize(val)
    @head = Node.new(val, nil)
  end

  def add(val)
    cur = @head                   # Start from the head
    cur = cur.nxt while cur.nxt   # Navigate upto last node
    cur.nxt = Node.new(val, nil)  # Insert the new lement
  end

  def delete(val)
    if @head.val == val
      @head = @head.nxt
      return
    end
    prv, cur = @head, @head.nxt                                   # Start search from 2nd element
    prv, cur = cur, cur.nxt while cur.nxt && cur.val != val       # Keep navigating until you find the value or reach the end
    raise 'Value Not Found' if cur.nxt.nil? && cur.val != val     # Error if value was not found
    prv.nxt = cur.nxt                                             # Set the nxt of prv element to nxt of cur elmnt
  end

  def reverse()
    cur, prv = @head, nil
    prv, prv.nxt, cur = cur, prv, cur.nxt while cur
    # while cur
    #   nxt = cur.nxt  # Prepare the nxt item for processing in nxt
    #   cur.nxt = prv  # The prv value that starts at nil becomes the nxt item in the list with respect to the cur node for reversal
    #   prv = cur      # The cur node becomes prv for the next iteration
    #   cur = nxt      # The prepared nxt node becomes the current node for the next iternation
    # end

    @head = prv
  end

  def show
    elements = []
    curent = @head
    until curent.nxt.nil?
      elements << curent.val
      curent = curent.nxt
    end
    elements << curent.val
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

ll.delete(5)
ll.show

ll.reverse()
ll.show
