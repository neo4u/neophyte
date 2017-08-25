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
    @data.push(x)
  end

  def pop
    @data.empty? ? nil : @data.pop
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
