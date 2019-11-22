from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]: return 0
        self.m, self.n, longest = len(matrix), len(matrix[0]), 0
        self.cache = {}
        self.dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for i in range(self.m):
            for j in range(self.n):
                cur_len = self.dfs(i, j, matrix)
                if cur_len > longest: longest = cur_len

        return longest

    def dfs(self, i, j, matrix):
        if (i, j) in self.cache: return self.cache[i, j]

        longest = 1
        for di, dj in self.dirs:
            x, y = i + di, j + dj
            if not self.valid(x, y) or matrix[x][y] <= matrix[i][j]: continue
            cur_len = 1 + self.dfs(x, y, matrix)
            if cur_len > longest: longest = cur_len

        self.cache[i, j] = longest
        return longest

    def valid(self, i, j):
        return 0 <= i <= self.m - 1 and 0 <= j <= self.n - 1


# 329. Longest Increasing Path in a Matrix
# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/
