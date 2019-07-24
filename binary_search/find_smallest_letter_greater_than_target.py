class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target >= letters[-1]: return letters[0]
        n = len(letters)
        l, r = 0, n - 1

        while l < r:
            mid = (l + r) // 2
            if letters[mid] <= target:
                l = mid + 1
            else 
                r = mid

        return letters[l]


# 744. Find Smallest Letter Greater Than Target
# https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/