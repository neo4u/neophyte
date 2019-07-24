class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        out_degree, in_degree = [0] * (N + 1), [0] * (N + 1)
        for a, b in trust:
            out_degree[a] += 1
            in_degree[b] += 1

        for i in range(1, N + 1):
            if out_degree[i] == 0 and in_degree[i] == N - 1:
                return i

        return -1

# Find the Town Judge
