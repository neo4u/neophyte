# @param {Integer[]} height
# @return {Integer}
def trap(height)
  l, r = 0, height.size - 1
  l_max, r_max, water = 0, 0, 0

  while l < r
    l_max = [l_max, height[l]].max
    r_max = [r_max, height[r]].max
    if l_max < r_max
      water += l_max - height[l]
      l += 1
    else
      water += r_max - height[r]
      r -= 1
    end
  end

  water
end

# 42. Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water/description/
# Explore stack solution as well

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 6)
