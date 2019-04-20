def longestIncreasingPath(self, matrix):
    """
    :type matrix: List[List[int]]
    :rtype: int
    """
    if not matrix:
        return 0
    m = len(matrix)
    n = len(matrix[0])
    cache = [[0]*n for _ in range(m)]
    res = 0
    min = -float("inf")
    for i in range(m):
        for j in range(n):
            res = max(res, self.dfs(matrix, min, i, j, m, n, cache))
    return res

def dfs(self, matrix, min, i, j, m, n, cache):
    if i < 0 or i >=m or j < 0 or j >= n or matrix[i][j] <= min:
        return 0
    if cache[i][j]:
        return cache[i][j]
    min = matrix[i][j]
    a = self.dfs(matrix,min, i+1, j, m, n, cache) + 1
    b = self.dfs(matrix,min, i-1, j, m, n, cache) + 1
    c = self.dfs(matrix,min, i, j+1, m, n, cache) + 1
    d = self.dfs(matrix,min, i, j-1, m, n, cache) + 1
    res = max(a,b,c,d)
    cache[i][j] = res
    return res
