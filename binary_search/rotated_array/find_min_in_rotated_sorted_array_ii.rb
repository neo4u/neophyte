def find_min(nums)
    l, r = 0, nums.size - 1

    while l <= r
        l += 1 while l < r && nums[l] == nums[l + 1]
        r -= 1 while r > l and nums[r] == nums[r - 1]
        return nums[l] if l == r

        mid = (l + r) / 2
        nums[mid] > nums[r] ? l = mid + 1 : r = mid     # Setup l and r for next iteration, eliminating the useless half based on requirement conditions.
    end

    -1
end

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(find_min([3,4,5,1,2]), 1)
assert_equal(find_min([4,5,6,7,0,1,2]), 0)
assert_equal(find_min([10,1,10,10,10]), 1)
assert_equal(find_min([1,3,5]), 1)
assert_equal(find_min([2,2,2,0,1]), 0)
