from typing import List


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        moves = {
            0: {1, 3}, 1: {0, 2, 4}, 2: {1, 5},
            3: {0, 4}, 4: {1, 3, 5}, 5: {2, 4}
        }
        visited, dist = set(), 0
        s = "".join(str(c) for row in board for c in row)
        q = [(s, s.index("0"))]

        while q:
            level_q = []

            for s, i in q:
                if s == "123450": return dist
                arr = list(s)

                for move in moves[i]:
                    tmp_nbr = arr                       # Either take a .copy() here
                    self.swap(tmp_nbr, i, move)
                    nbr = "".join(tmp_nbr)
                    self.swap(tmp_nbr, i, move)         # Or do the inverse of the swap, after getting it as a string above
                    if nbr == "123450": return dist + 1
                    if nbr in visited: continue

                    level_q.append((nbr, move))
                    visited.add(nbr)

            q = level_q
            dist += 1

        return -1

    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]


# 773. Sliding Puzzle
# https://leetcode.com/problems/sliding-puzzle/description/


# Intuition:
# The 'moves' hash is generated cuz:
# 0 <-> 1 <-> 2
# ^     ^    ^
# |     |    |
# v     v    v
# 3 <-> 4 <-> 5


sol = Solution()

assert sol.slidingPuzzle([[1, 2, 3], [4, 0, 5]]) == 1
assert sol.slidingPuzzle([[1, 2, 3], [5, 4, 0]]) == -1
assert sol.slidingPuzzle([[4, 1, 2], [5, 0, 3]]) == 5
