def find_min(nums)
    l, r = 0, nums.size - 1

    while l < r
        return nums[l] if nums[l] < nums[r]

        mid = (l + r) / 2
        nums[mid] > nums[r] ? l = mid + 1 : r = mid
    end

    nums[l]
end


# [3,4,5,1,2]

# 5,6,7,1,2,3,4


# 153. Find Minimum in Rotated Sorted Array
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

# 1. Find inflection point
# 2. Find an array such that first element is smaller than the last
# 3. Keep eliminating half until we are left 
# Time: O(log(n))
# Space: O(1)

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(find_min([3,4,5,1,2]), 1)
assert_equal(find_min([4,5,6,7,0,1,2]), 0)
assert_equal(find_min([1]), 1)
assert_equal(find_min([1, 1]), 1)
assert_equal(find_min([]), -1)

assert_equal(find_min_simple([3,4,5,1,2]), 1)
assert_equal(find_min_simple([4,5,6,7,0,1,2]), 0)
assert_equal(find_min_simple([1]), 1)
assert_equal(find_min_simple([]), nil)
