#!/usr/bin/env ruby

class Queue
  def initialize(size)
    @max_size = size
    @data = []
  end

  def enqueue(x)
    raise "Overflow" if @data.size + 1 > @max_size
    @data.push(x)
  end

  def dequeue
    raise "Underflow" if empty?
    @data.shift
  end

  def empty?
    @data.empty?
  end

  def show
    puts "#{@data}"
  end
end

q = Queue.new(5)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.show

# q.enqueue(6)

q.dequeue
q.dequeue
q.dequeue
q.dequeue
q.dequeue
q.show

q.dequeue

