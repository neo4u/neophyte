class Solution(object):
    def removeStones(self, stones):
        graph = collections.defaultdict(list)
        for i, x in enumerate(stones):
            for j in range(i):
                y = stones[j]
                if x[0]==y[0] or x[1]==y[1]:
                    graph[i].append(j)
                    graph[j].append(i)

        N = len(stones)
        ans = 0

        seen = [False] * N
        for i in range(N):
            if not seen[i]:
                stack = [i]
                seen[i] = True
                while stack:
                    ans += 1
                    node = stack.pop()
                    for nei in graph[node]:
                        if not seen[nei]:
                            stack.append(nei)
                            seen[nei] = True
                ans -= 1
        return ans

# [1,2,3,4]

# 947. Most Stones Removed with Same Row or Column
# 

# stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]


# graph = {(x, y) : [(), ()]}


# node : nbrs
# -----------
# 0, 0   [0, 1],
# 0, 1   [0, 0],
