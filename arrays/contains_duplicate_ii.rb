# @param {Integer[]} nums
# @param {Integer} k
# @return {Boolean}
def contains_nearby_duplicate(nums, k)
  map = {}
  nums.each_with_index do |num, idx|
    return true if map.key?(num) && (map[num] - idx).abs <= k
    map[num] = idx
  end

  false
end

# 219. Contains Duplicate II
# https://leetcode.com/problems/contains-duplicate-ii

