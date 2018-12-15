# Not Scalable as q keeps growing with the of pushes.
# Space: O(n)
class HitCounter2
    def initialize()
        @q = []
    end

    # Time: O(1)
    def hit(timestamp)
        @q.push(timestamp)
    end

    # pop elements Time: O(n)
    def get_hits(timestamp)
        while !@q.empty? && timestamp - @q.first >= 300
            @q.shift
        end

        @q.size
    end
end

# Scalable Solution: Space: O(1)
class HitCounter
    def initialize()
        # Initialize the second element of each cell to the index + 1
        @times = Array.new(300, 0)
        @hits = Array.new(300, 0)
    end

    # Time: O(1)
    def hit(timestamp)
        i = timestamp % 300
        if @times[i] != timestamp
            @times[i] = timestamp
            @hits[i] = 1
        else
            @hits[i] += 1
        end
    end

    # Time: O(1)
    def get_hits(timestamp)
        total = 0
        0.upto(299) do |i|
            total += @hits[i] if timestamp - @times[i] < 300
        end
        total
    end
end

# 362. Design Hit Counter
# https://leetcode.com/problems/design-hit-counter/

# Approach 1: Using Queue, hit() Time: O(1), get_hits() Time: O(n), Space: O(n)
# Approach 2: Using Modular Arithmatic (Buckets) hit() Time: O(1), get_hits() Time: O(1), Space: O(1)

require 'test/unit'
extend Test::Unit::Assertions

counter = HitCounter.new()
counter.hit(1)
counter.hit(2)
counter.hit(3)
assert_equal(counter.get_hits(4), 3)
counter.hit(300)
assert_equal(counter.get_hits(300), 4)
assert_equal(counter.get_hits(301), 3)
