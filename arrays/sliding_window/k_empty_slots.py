class Solution(object):
    def kEmptySlots(self, flowers, k):
        days = [0] * len(flowers)

        for day, position in enumerate(flowers, 1):
            days[position - 1] = day

        ans = float('inf')
        left, right = 0, k+1

        while right < len(days):
            for i in xrange(left + 1, right):
                if days[i] < days[left] or days[i] < days[right]:
                    left, right = i, i+k+1
                    break
            else:
                ans = min(ans, max(days[left], days[right]))
                left, right = right, right+k+1

        return ans if ans < float('inf') else -1

# Time and Space Complexity: O(N). The analysis is the same as in Approach #2.

import bisect

class Solution(object):
    def kEmptySlots(self, flowers, k):
        active = []

        for day, flower in enumerate(flowers, 1):
            i = bisect.bisect(active, flower)
            print(f"start of day:{day}, bisect_idx:{i}, flower:{flower}, active:{active}")
            print(f"neighbours:{active[i-(i>0):i+1]}")

            for neighbor in active[i-(i>0):i+1]:
                if abs(neighbor - flower) - 1 == k:
                    return day

            active.insert(i, flower)
            print(f"end of day:{day}, bisect_idx:{i}, flower:{flower}, active:{active}")
            print("\n")

        return -1

sol = Solution()
assert sol.kEmptySlots([1,3,2], 1) == 2
assert sol.kEmptySlots([6,1,5,2,4,3], 2) == 4
