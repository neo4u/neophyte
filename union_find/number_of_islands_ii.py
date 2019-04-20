class DSU:
    def __init__(self):
        self.parents = {}
        self.count = 0
        
    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        par_x, par_y = self.find(x), self.find(y)
        if par_x != par_y:
            self.count -= 1
            self.parents[par_y] = par_x

    def setParent(self, x):
        self.parents[x] = x
        self.count += 1
        

class Solution:
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        dsu = DSU()
        ans = []
        for po in positions:
            idx = po[0]*n+po[1]
            dsu.setParent(idx)
            for di in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                x, y = po[0]+di[0], po[1]+di[1]
                if 0 <= x < m and 0 <= y < n and x*n+y in dsu.parents:
                    dsu.union(idx, x*n+y)
            ans.append(dsu.count)
        return ans