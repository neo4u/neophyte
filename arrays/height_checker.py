class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        new_heights = sorted(heights)
        count = 0

        for x, y in zip(heights, new_heights):
            count += (x != y)

        return count
