from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n, water = len(height), 0
        l, r = 0, n - 1
        l_max, r_max = 0, 0

        while l < r:
            l_max = max(l_max, height[l])
            r_max = max(r_max, height[r])

            if height[l] < height[r]:
                water += l_max - height[l]
                l += 1
            else:
                water += r_max - height[r]
                r -= 1

        return water


# 42. Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water/description/


# Steps:
# 1. We use a 2-pointer approach
# 2. Running pointers l and r
# 3. We check the max on left and right side
# 4. Based on height[l] and height[r] whichever is lesser,
#    it contributes l_max - height[l] or r_max - height[r] towards the water
# 5. we return the total water when l == r
