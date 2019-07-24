class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        self.dfs(rooms, 0, visited)
        return len(visited) == len(rooms)

    def dfs(self, rooms, node, visited):
        if node in visited: return
        visited.add(node)

        for nbr in rooms[node]:
            self.dfs(rooms, nbr, visited)


# 841. Keys and Rooms
# https://leetcode.com/problems/keys-and-rooms/description/
