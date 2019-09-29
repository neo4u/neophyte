from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        self.visited = set()
        self.dfs(rooms, 0)
        return len(rooms) == len(self.visited)

    def dfs(self, rooms, src):
        if src in self.visited: return
        self.visited.add(src)
        for nbr in rooms[src]: self.dfs(rooms, nbr)


# 841. Keys and Rooms
# https://leetcode.com/problems/keys-and-rooms/description/
