class Solution:
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        
        M = len(dungeon)
        N = len(dungeon[0])
        
        
        queue = collections.deque([(M-1, N-1)])
        explored = set()
        
        while queue:
            r, c = queue.popleft()
            if (r,c) in explored:
                continue

            explored.add((r,c))
            down = dungeon[r+1][c] if r+1 < M else float('inf')
            right = dungeon[r][c+1] if c+1 < N else float('inf')
            if r == M-1 and c == N-1:
                dungeon[r][c] = max(1, -dungeon[M-1][N-1]+1)
            else:
                dungeon[r][c] = max(min(down, right) - dungeon[r][c], 1)
            if r-1 >= 0: queue.append((r-1,c))
            if c-1 >= 0: queue.append((r,c-1))
            
        return dungeon[0][0]

# The minimum health that a knight needs to start from (i, j) is
# the minimum health of that it needs to start from any surrounding cell
# minus the value of the cell.
# To start from the cell with the princess needs 1 minus value of that cell.

# How can we compute this? Since each cell depends on all surrounding cells?
# If we start from the princess cell, we can just consider the left and top cells.
# Is it possible to have loops?
# Then the world has a state, since you can't take the same bonus twice.
# Wait! The knight decides to move only right or down.

class Solution:
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        
        m = len(dungeon)
        n = len(dungeon[0])
        s = 0
        for row in dungeon:
            for x in row:
                if x < 0: s += x
        lo,hi = 1,-s

        while lo <= hi:
            mid = (lo + hi) // 2
            if self.canGet(dungeon,mid):
                hi = mid - 1
            else:
                lo = mid + 1
        return lo


    def canGet(self,dungeon,init):
        m = len(dungeon)
        n = len(dungeon[0])
        dp = [[[False,0] for i in range(n)] for i in range(m)]
        health = init + dungeon[0][0]
        dp[0][0] = [True,health] if health > 0 else dp[0][0]
        for i in range(1,m):
            health += dungeon[i][0]
            dp[i][0][0] = dp[i-1][0][0] and health > 0
            dp[i][0][1] = health

        health = dp[0][0][1]
        for i in range(1,n):
            health += dungeon[0][i]
            dp[0][i][0] = dp[0][i-1][0] and health > 0
            dp[0][i][1] = health


        for i in range(1,m):
            for j in range(1,n):
                if dp[i-1][j][0]:
                    tmp = dp[i-1][j][1] + dungeon[i][j]
                    if tmp > 0: dp[i][j] = (True,tmp)
                if dp[i][j-1][0]:
                    tmp = dp[i][j-1][1] + dungeon[i][j]
                    if tmp > dp[i][j][1]: dp[i][j] = (True,tmp)

        return dp[m-1][n-1][0]



import collections