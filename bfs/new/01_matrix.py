import collections
# Do a BFS on multiple sources: the squares of the given matrix that have a 0.
# Every time you visit a node, it will be from a path of predecessors that is of shortest distance to a zero.
class Solution(object):
    def updateMatrix(self, A):
        R, C = len(A), len(A[0])
        def neighbors(r, c):
            for cr, cc in ((r-1,c),(r+1,c),(r,c-1),(r,c+1)):
                if 0 <= cr < R and 0 <= cc < C:
                    yield cr, cc
                    
        q = collections.deque([((r, c), 0) 
                for r in range(R)
                for c in range(C)
                if A[r][c] == 0])
        seen = {x for x,_ in q}
        ans = [[0]*C for _ in A]
        while q:
            (r, c), depth = q.popleft()
            ans[r][c] = depth
            for nei in neighbors(r, c):
                if nei not in seen:
                    seen.add(nei)
                    q.append((nei, depth + 1))
        
        return ans

# Concise solution stefan 
class Solution(object):
    def updateMatrix(self, matrix):
        q, m, n = [], len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] != 0:
                    matrix[i][j] = 0x7fffffff
                else:
                    q.append((i, j))
        for i, j in q:
            for r, c in ((i, 1+j), (i, j-1), (i+1, j), (i-1, j)):
                z = matrix[i][j] + 1
                if 0 <= r < m and 0 <= c < n and matrix[r][c] > z:
                    matrix[r][c] = z
                    q.append((r, c))
        return matrix


# Readable solution
from collections import deque
class Solution:
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        
        vis = list()
        for i in range(len(matrix)):
            vis.append([False for _ in range(len(matrix[0]))])
            
        st =  deque()
        R = len(matrix)
        C = len(matrix[0])
        for i in range(R):
            for j in range(C):
                if not matrix[i][j]:
                    st.append((i, j, 0))
        while st:
            (r,c, val) = st.popleft()
            if r < 0 or c < 0 or r >= R or c >= C:
                continue
            
            if not vis[r][c] or (vis[r][c] and matrix[r][c] > val):
                matrix[r][c] = val
                vis[r][c] = True
                val+=1
                st.append((r+1, c, val))
                st.append((r-1, c, val))
                st.append((r, c+1, val))
                st.append((r, c-1, val))
        return matrix

# BFS: first, we find all 0s, and the distance for them are 0.
# We push all of its cooridinates (i, j) to queue and record them as visited.
# Then we check all its neighours, those neighours should have distance 1.
# Then we push those neighours to the queue, and again check the neighours for each one,
# now the distance becomes 2, we will stop when all the cells are checked.

# Since the distances aways increase by one by each iteration,
# so we don't need to worry, that we might find shorter distance later,
# so the current distance + 1 is the best distance that its neighours can get already.

class Solution:
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(matrix), len(matrix[0])
        queue = collections.deque()
        visited = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    visited.add((i, j))
                    queue.append((i, j))
        while queue:
            size = len(queue)
            for _ in range(size):
                i, j = queue.popleft()
                if i - 1 >= 0 and (i-1, j) not in visited:
                    matrix[i-1][j] = matrix[i][j] + 1
                    visited.add((i-1, j))
                    queue.append((i-1, j))
                if i + 1 < m and (i+1, j) not in visited:
                    matrix[i+1][j] = matrix[i][j] + 1
                    visited.add((i+1, j))
                    queue.append((i+1, j))
                if j - 1 >= 0 and (i, j-1) not in visited:
                    matrix[i][j-1] = matrix[i][j] + 1
                    visited.add((i, j-1))
                    queue.append((i, j-1))
                if j + 1 < n and (i, j+1) not in visited:
                    matrix[i][j+1] = matrix[i][j] + 1
                    visited.add((i, j+1))
                    queue.append((i, j+1))
        return matrix
