import heapq

class Solution:
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        height = []
        for b in buildings:
            height.append((b[0],-b[2]))
            height.append((b[1],b[2]))

        height = sorted(height, key = lambda x: [x[0], x[1]])

        pq = [0]
        prev = 0

        for h in height:
            if h[1] < 0:
                heapq.heappush(pq, h[1])
            else:
                pq.remove(-h[1])
                heapq.heapify(pq)

            cur = -pq[0]
            if prev != cur:
                result.append((h[0], cur))
                prev = cur

        return result

class Solution:
    def getSkyline(self, buildings):
        events = sorted([(L, -H, R) for L, R, H in buildings] + list({(R, 0, None) for _, R, _ in buildings}))
        res, hp = [[0, 0]], [(0, float("inf"))]
        for x, negH, R in events:
            while x >= hp[0][1]: 
                heapq.heappop(hp)
            if negH: 
                heapq.heappush(hp, (negH, R))
            if res[-1][1] + hp[0][0]: 
                res += [x, -hp[0][0]],
        return res[1:]
        
        points = []
        for b in buildings:
            points.append((b[0], 0, b[2])) # start is 0
            points.append((b[1], 1, b[2])) # end is 1, when sorting, start go first

        points.sort(key=lambda p:(p[0], p[1]))

        heap = []
        ans = []
        for p in points:
            lastHeight = 0 if not heap else -heap[0][0]
            if p[1] == 0: #start
                heapq.heappush(heap, (-p[2], p[1], p[0]))
                if lastHeight < -heap[0][0]:
                    if ans and ans[-1][0] == p[0]:
                        ans[-1][1] = p[2]
                    else:
                        ans.append([p[0], p[2]])
            else:
                for i in range(len(heap)):
                    if heap[i][1] == 0 and -heap[i][0] == p[2]:
                        del heap[i]
                        break
                heapq.heapify(heap)
                if not heap:
                    if ans and ans[-1][0] == p[0]:
                        ans[-1][1] = 0
                    else:
                        ans.append([p[0], 0])
                elif lastHeight > -heap[0][0]:
                    if ans and ans[-1][0] == p[0]:
                        ans[-1][1] = -heap[0][0]
                    else:
                        ans.append([p[0], -heap[0][0]])
        return ans