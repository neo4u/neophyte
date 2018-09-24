# @param {Integer[]} height
# @return {Integer}
def max_area(height)
    max_area, l, r = 0, 0, height.length - 1

    while l < r
        max_area = [max_area, [height[l], height[r]].min * (r - l)].max
        height[l] < height[r] ? l += 1 : r -= 1
    end

    max_area
end

# 11. Container With Most Water
# https://leetcode.com/problems/container-with-most-water/description/

