# Recursive with memoization
class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def uniquePaths(self, m, n):
        cache = {}
        return self.findPath(m, n, cache)

    def findPath(self, m, n, cache):
        if (m, n) in cache:
            return cache[(m, n)]
        elif m == 1 or n == 1:
            return 1

        cache[(m, n)] = self.findPath(m - 1, n, cache) + self.findPath(m, n - 1, cache)
        return cache[(m, n)]


# Dynamic-programming bottom-up
class Solution2:
    # @return an integer
    def uniquePaths(self, m, n):
        aux = [[1 for x in range(n)] for x in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                aux[i][j] = aux[i][j-1]+aux[i-1][j]

        return aux[m - 1][n - 1]
