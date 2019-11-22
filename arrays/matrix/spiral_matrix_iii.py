from typing import List


class Solution:
    def spiralMatrixIII(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        result = [(r0, c0)]
        if R * C == 1: return result

        # For walk length k = 1, 3, 5 ...
        for k in range(1, 2*(R+C), 2):

            # For direction (dr, dc) = east, south, west, north;
            # and walk length dk...
            dirs = [(0, 1, k), (1, 0, k), (0, -1, k + 1), (-1, 0, k + 1)]
            for dr, dc, dk in dirs:
                # For each of dk units in the current direction ...
                for _ in range(dk):

                    # Step in that direction
                    r0 += dr; c0 += dc

                    # If on the grid ...
                    if 0 <= r0 < R and 0 <= c0 < C:
                        result.append((r0, c0))
                        if len(result) == R * C:
                            return result


# 885. Spiral Matrix III
# https://leetcode.com/problems/spiral-matrix-iii/description/
