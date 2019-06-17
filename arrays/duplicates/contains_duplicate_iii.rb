# @param {Integer[]} nums
# @param {Integer} k
# @param {Integer} t
# @return {Boolean}
# @note This method fails the 40th case. TLE Error
# def contains_nearby_almost_duplicate(nums, k, t)
#   map = {}
#   nums.each_with_index do |num, idx|
#     res = map.keys.select { |key| (num - key).abs <= t && (map[key] - idx).abs <= k }
#     return true if res.length > 0
#     map[num] = idx
#   end

#   false
# end

# @note Using hash for TreeSet as per BST Solution BST not available in Ruby
# def contains_nearby_almost_duplicate(nums, k, t)
#   map = {}
#   nums.each_with_index do |num, idx|
#     s = map.keys.select { |key| key >= num }
#     return true if s <= nums[idx] + t
#     g = map.keys.select { |key| key <= num }
#     return true if nums[idx] <= g + t
#     map[num] = idx
#     map.delete(nums[idx - k]) if map.length > k
#   end

#   false
# end

# @note Method using buckets
def contains_nearby_almost_duplicate(nums, k, t)
    return false if t < 0
    n, d, w = nums.size, {}, t + 1

    0.upto(n - 1) do |i|
        m = nums[i] / w
        return true if d.key?(m)
        return true if d.key?(m - 1) && (nums[i] - d[m - 1]).abs < w
        return true if d.key?(m + 1) && (nums[i] - d[m + 1]).abs < w

        d[m] = nums[i]
        d.delete(nums[i - k] / w) if i >= k
    end

    return false
end

# 220. Contains Duplicate III
# https://leetcode.com/problems/contains-duplicate-iii/description/

# contains_nearby_almost_duplicate([1,2], 0, 1)


require 'test/unit'
extend Test::Unit::Assertions

assert_equal(contains_nearby_almost_duplicate([-1, -1], 1, 0), true)
assert_equal(contains_nearby_almost_duplicate([2, 1], 1, 1), true)
assert_equal(contains_nearby_almost_duplicate([-1, -1], 1, -1), false)
