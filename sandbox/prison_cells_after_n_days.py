from typing import List

class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        seen = {}

        while N:
            seen.setdefault(tuple(cells), N)
            N -= 1
            cells = self.nextday(cells)
            print(f"N: {N}, cells: {cells}")
            if tuple(cells) in seen:
                N %= seen[tuple(cells)] - N
        return cells

    def nextday(self, cells):
        return [int(i > 0 and i < 7 and cells[i-1] == cells[i+1]) for i in range(8)]



sol = Solution()
assert sol.prisonAfterNDays([0,1,0,1,1,0,0,1], 7) == [0,0,1,1,0,0,0,0]
assert sol.prisonAfterNDays([1,0,0,1,0,0,1,0], 1000000000) == [0, 0, 1, 1, 1, 1, 1, 0]
