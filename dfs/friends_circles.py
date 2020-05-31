from typing import List


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        N = len(M)
        visited = set()
        result = 0

        for i in range(N):
            if i in visited: continue
            self.dfs(M, i, visited)
            result += 1

        return result

    def dfs(self, M, row, visited):
        for stdnt_id, is_friend in enumerate(M[row]):
            if not is_friend or stdnt_id in visited: continue
            visited.add(stdnt_id)
            self.dfs(M, stdnt_id, visited)

# 547. Friend Circles
# https://leetcode.com/problems/friend-circles/description/
