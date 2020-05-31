import heapq
import collections


class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if not s or not k or k < 2: return s
        q = [(-freq, c) for c, freq in collections.Counter(s).items()]
        heapq.heapify(q)
        result = []

        while q:
            next_level = []
            for _ in range(k):
                if not q: return ""
                freq, c = heapq.heappop(q)
                result.append(c)

                if len(result) == len(s): return "".join(result)
                freq = -freq - 1
                if freq > 0: next_level.append((-freq, c))

            q.extend(next_level)
            heapq.heapify(q)


# 358. Rearrange String k Distance Apart
# https://leetcode.com/problems/rearrange-string-k-distance-apart/description/

# Each heap operation takes constant time since it holds at most 26 elements. So this allows theta(n) time.

# Similar to Task Scheduler