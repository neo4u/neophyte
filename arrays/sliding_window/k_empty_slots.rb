# @param {Integer[]} flowers
# @param {Integer} k
# @return {Integer}
def k_empty_slots(flowers, k)
    days = Array.new(flowers.size, 0)

    
end

# 683. K Empty Slots
# https://leetcode.com/problems/k-empty-slots/

# Approach #1: Insert Into Sorted Structure, Time: O(n^2) (Use python for bisect.bisect) 
#              As above, except list.insert is O(N). python insert
# Approach #2: Min Queue (Use python for collection.deque)
# Approach #3: Sliding Window (Implemented above)

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(k_empty_slots([1,3,2], 1), 2)
assert_equal(k_empty_slots([1,2,3], 1), -1)
