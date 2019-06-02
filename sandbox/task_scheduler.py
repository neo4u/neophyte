from heapq import heappush, heappop, heapify
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts, time = Counter(tasks), 0
        q = [-x for x in counts.values()]
        heapify(q)

        while q:
            cool, aux = 0, []

            while cool <= n:
                cool += 1; time += 1
                if not q: continue

                curr = abs(heappop(q))
                curr -= 1
                if curr > 0: aux.append(-curr)

                if not q and not aux: break

            if aux:
                q.extend(aux)
                heapify(q)

        return time
