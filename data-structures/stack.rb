#!/usr/bin/env ruby

# ------------------------------
# References:
# 1. tack Cormen Implementation
# 2. https://rubymonk.com/learning/books/4-ruby-primer-ascent/chapters/33-advanced-arrays/lessons/86-stacks-and-queues
# ------------------------------
class Stack
  def initialize(size)
    @max_size = size
    @data = []
  end

  def push(x)
    raise 'Stack Overflow' if @data.size + 1 > @max_size
    @data.push(x)
  end

  def pop
    raise 'Stack Underflow' if empty?
    @data.pop
  end

  def top
    @data.empty? ? nil : @data[-1]
  end

  def size
    @data.size
  end

  private

  def full?
    @max_size = @data.size
  end

  def empty?
    @data.empty?
  end
end

stack = Stack.new(5)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
puts stack.top
puts stack.pop
puts stack.top
stack.push(5)
# stack.push(6)
puts stack.pop
puts stack.pop
puts stack.pop
puts stack.pop
puts stack.pop
puts stack.pop
