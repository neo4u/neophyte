from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = sorted(event for n, i, j in trips for event in [[i, n], [j, -n]])
        print(f"trips: {trips} | events: {events}")

        for _, v in events:
            capacity -= v
            if capacity < 0: return False

        return True


sol = Solution()
assert sol.carPooling([[2, 1, 5], [3, 5, 7]], 5) == True
assert sol.carPooling([[2, 1, 5], [3, 3, 7]], 4) == False

# assert sol.carPooling([[2, 1, 5], [3, 3, 7]], 5) == True
# assert sol.carPooling([[3, 2, 7], [3, 7, 9], [8, 3, 9]], 11) == True
