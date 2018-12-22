# Given an NxN grid with an array of lamp coordinates.
# Each lamp provides illumination to every square on its x axis, 
# every square on its y axis, and every square that lies on its
# diagonal (think of a Queen in chess). Given an array of 
# query coordinates, determine whether or not the query point is illuminated.
# Moreover, whenever you execute a query, all 
# lamps adjacent to or on that query point are permanently un-illuminated.
# The ranges for the variables/arrays is:
# 10^3 < N < 10^9, 10^3 < lamps < 10^9, 10^3 < queries < 10^9.

class Solution():
    def gridIlluminator(self, n, lamps):
        '''Solve the grid illumination problem.

            T(n, l) = O(l)
            S(n, l) = O(n)
        '''
        self.rows = [False for _ in range(n)]
        self.cols = [False for _ in range(n)]

        self.pos_diags = [False for _ in range((2 * n) - 1)]
        self.neg_diags = [False for _ in range((2 * n) - 1)]

        for i, j in lamps:
            self.rows[i], self.cols[j] = True, True
            self.pos_diags[i + j] = True
            self.neg_diags[n - 1 + i - j] = True

    def is_lit(self, n, x, y):
        return self.rows[x] or self.cols[y] or self.pos_diags[x + y] or self.neg_diags[n - 1 + x - y]


sol = Solution()
dim = 6
sol.gridIlluminator(dim, [(0, 0), (2, 3), (1, 5)])

for i in range(dim):
    for j in range(dim):
        if (i, j) in [(3, 1), (5, 2), (5, 4)]:
            assert not sol.is_lit(dim, i, j)
        else:
            assert sol.is_lit(dim, i, j)

sol = Solution()
dim = 6
sol.gridIlluminator(dim, [(2, 3), (1, 5)])

for i in range(dim):
    for j in range(dim):
        if (i, j) in [(0, 0), (0, 2), (3, 0), (3, 1), (4, 0), (4, 4), (5, 2), (5, 4)]:
            assert not sol.is_lit(dim, i, j)
        else:
            assert sol.is_lit(dim, i, j)
