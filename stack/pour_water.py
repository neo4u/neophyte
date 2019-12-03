from typing import List

# Approach 1: O(V * N)
class Solution1:
    def pourWater(self, heights: List[int], V: int, K: int) -> List[int]:
        n = len(heights)

        for _ in range(V):
            curr = K

            # Move left
            while curr > 0 and heights[curr] >= heights[curr - 1]: curr -= 1

            # Move right
            while curr < n - 1 and heights[curr] >= heights[curr + 1]: curr += 1

            # Move left to K
            while curr > K and heights[curr] == heights[curr - 1]: curr -= 1

            heights[curr] += 1

        return heights


# Approach 2: O(V + N)
class Solution:
    def pourWater(self, heights: List[int], V: int, K: int) -> List[int]:
        l_fall, r_fall, l, r, n = [], [], K, K, len(heights)

        for _ in range(V):
            # Push left boundary as long as neighbour to left is less than l
            while l > 0 and heights[l - 1] <= heights[l]:
                l -= 1
                # At each move push into stack if curr height is less than where l was
                if heights[l] < heights[l + 1]: l_fall.append(l)

            # Push right boundary as long as neighbour to right is less than r
            while r < n - 1 and heights[r + 1] <= heights[r]:
                r += 1
                # At each move push into stack if curr height is less than where r was
                if heights[r] < heights[r - 1]: r_fall.append(r)

            # If we have elements in l_fall stack it means the drop moves left
            if l_fall:
                fall = l_fall[-1]
                heights[fall] += 1
                # Pop the currently filling position if i levels up to its right height
                if heights[fall] == heights[fall + 1]: l_fall.pop()
                # Once the drop has fallen at 'fall' position, the next position to fill would be 'fall - 1', until fall hits l
                if l < fall: l_fall.append(fall - 1)
            # If we have elements in r_fall stack it means the drop moves right
            elif r_fall:
                fall = r_fall[-1]
                heights[fall] += 1
                # Pop the currently filling position if it levels up to its left height
                if heights[fall] == heights[fall - 1]: r_fall.pop()
                # Once the drop has fallen at 'fall' position, the next position to fill would be 'fall + 1', until fall hits r
                if r > fall: r_fall.append(fall + 1)
            # If both stacks are empty it means the drop stays at K
            else:
                heights[K] += 1
                # Once the drop has fallen at 'K' position, the next position to fill from left would be 'K - 1' and right 'K + 1'
                if l < K: l_fall.append(K - 1)
                if r > K: r_fall.append(K + 1)

        return heights


# 755. Pour Water
# https://leetcode.com/problems/pour-water/description/

# Approach 1:
# Intuition:
# - Imagine a needle which is the index into the heights array
# - Each time we have a new drop we check the heights starting from K
# - We fill one by one to the left starting from K
# - Once, the curr pointer becomes higher than its right side,
# - We fill one by one to the right
# - Once, the heights of curr is equal to its left, we move our needle back to K,
#   because that's where we fill when the drop won't eventually move to left or right

# Time: O(V * N)
# Space: O(1)

# Approach 2: Two stacks, two pointers
# - We use l_fall and r_fall to as monotone stacks to store the next fall position
# - We use l and r to mark the left and right boundaries

# Time: O(V + N)
# Space: O(N)

# https://leetcode.com/problems/pour-water/discuss/113003/C++JavaPython-O(V+N)-time-solution-using-2-pointers-and-2-stacks


sol = Solution()
assert sol.pourWater([2, 1, 1, 2, 1, 2, 2], 4, 3) == [2, 2, 2, 3, 2, 2, 2]
assert sol.pourWater([1, 2, 3, 4], 2, 2) == [2, 3, 3, 4]
assert sol.pourWater([3, 1, 3], 5, 1) == [4, 4, 4]
