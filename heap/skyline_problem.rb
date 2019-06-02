# Algorithm
# 1. Build a hash called height_map which records the "heights" (keys) and number of same "height" values
# 2. Build an array of points , which seaprates out the lef-edge of the building with height (by negating the height value) and right-edge and height (positive value)
# 3. For each point, the max height is got by the keys and checking the current height and previous height 
# 4. Retain if same value is not repeated

require_relative '../adts/priority_queue'

def get_skyline(buildings)
    return [] if !buildings || buildings.empty?
    result, heights = [], []

    buildings.each do |b|
        heights.push([b[0], -b[2]])
        heights.push([b[1], b[2]])
    end

    heights.sort!
    prev = 0
    points_pq = PriorityQueue.new([0])

    heights.each do |h|
        if h[1] < 0
            points_pq.add(-h[1])
        else
            points_pq.delete(h[1])
        end

        curr = points_pq.peek()
        result.push([h[0], curr]) if curr != prev
        prev = curr
    end

    result
end


require 'test/unit'
extend Test::Unit::Assertions

assert_equal(
    get_skyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]),
    [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]]
)
assert_equal(get_skyline([]),[])
assert_equal(get_skyline([[0,1,3]]),[[0,3],[1,0]])
assert_equal(get_skyline([[0,2147483647,2147483647]]), [[0,2147483647],[2147483647,0]])
assert_equal(get_skyline([[0,2,3],[2,5,3]]),[[0,3],[5,0]])
