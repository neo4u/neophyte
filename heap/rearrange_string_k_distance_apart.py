from collections import Counter
import heapq

class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if not s or not k or k < 2: return s
        q = [(-freq, c) for c, freq in Counter(s).items()]
        heapq.heapify(q)
        result = []

        while q:
            pushback = []
            for _ in range(k):
                if not q: return ""
                freq, c = heapq.heappop(q)
                result.append(c)

                if len(result) == len(s): return "".join(result)
                if freq < -1: pushback.append((freq + 1, c))

            q.extend(pushback)
            heapq.heapify(q)


# 358. Rearrange String k Distance Apart
# https://leetcode.com/problems/rearrange-string-k-distance-apart/description/

# Each heap operation takes constant time since it holds at most 26 elements. So this allows theta(n) time.
