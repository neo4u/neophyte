# @param {Integer[]} nums
# @return {Integer}
def find_duplicate(nums)
    # find intersection of two runners
    tortoise = hare = nums[0]
    while true
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        break if tortoise == hare
    end

    # Find entrance to cycle
    p1, p2 = nums[0], tortoise
    p1, p2 = nums[p1], nums[p2] while p1 != p2

    p1
end

# 287. Find the Duplicate Number
# https://leetcode.com/problems/find-the-duplicate-number/description/

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(find_duplicate([3,1,3,4,2]), 3)
assert_equal(find_duplicate([1,3,4,2,2]), 2)
