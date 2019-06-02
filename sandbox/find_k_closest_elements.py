from bisect import bisect_left

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        if x < arr[0]:
            return arr[:k]
        elif x > arr[-1]:
            return arr[-k:]
        else:
            i = bisect_left(arr, x)
            l, r = max(0, i - k - 1), min(i + k - 1, n - 1)

            while r - l + 1 > k:
                if abs(arr[l] - x) <= abs(arr[r] - x):
                    r -= 1
                else:
                    l += 1

        return arr[l:r + 1]