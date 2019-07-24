import heapq
from collections import Counter

class Solution(object):
    def reorganizeString(self, S):
        counts = Counter(S)
        pq = [(-v, k) for k, v in counts.items()]
        heapq.heapify(pq)

        # If any char has frequency more than double of length + 1,
        # return "" as we can't possibly return a string without getthing that char twice in sequence
        if any(-nc > (len(S) + 1) / 2 for nc, x in pq):
            return ""

        ans = []
        while len(pq) >= 2:
            nct1, ch1 = heapq.heappop(pq)
            nct2, ch2 = heapq.heappop(pq)
            ans.extend([ch1, ch2])
            if nct1 + 1: heapq.heappush(pq, (nct1 + 1, ch1))
            if nct2 + 1: heapq.heappush(pq, (nct2 + 1, ch2))

        return "".join(ans) + (pq[0][1] if pq else '')

# Condensed
import heapq
class Solution(object):
    def reorganizeString(self, S: str) -> str:
        pq = [(-S.count(x), x) for x in set(S)]
        heapq.heapify(pq)
        if any(-nc > (len(S) + 1) / 2 for nc, x in pq): return ""

        ans = []
        while len(pq) >= 2:
            nct1, ch1 = heapq.heappop(pq)
            nct2, ch2 = heapq.heappop(pq)
            ans.extend([ch1, ch2])
            if nct1 + 1: heapq.heappush(pq, (nct1 + 1, ch1))
            if nct2 + 1: heapq.heappush(pq, (nct2 + 1, ch2))

        return "".join(ans) + (pq[0][1] if pq else '')


# Approach
# We store a heap of (count, letter). [In Python, our implementation stores negative counts.]
# We pop the top two elements from the heap (representing different letters with positive remaining count),
# and then write the most frequent one that isn't the same as the most recent one written.
# After, we push the correct counts back onto the heap.
# Actually, we don't even need to keep track of the most recent one written.
# If it is possible to organize the string,
# the letter written second can never be written first in the very next writing.
# At the end, we might have one element still on the heap,
# which must have a count of one. If we do, we'll add that to the answer too.

# Complexity Analysis
# Time Complexity: O(NlogA)), where N is the length of S, and A is the size of the alphabet.
#                  If A is fixed, this complexity is O(N). The log A is due to heap data structure.
#                  Map depth of a heap is log n
# Space Complexity: O(A). If A is fixed, this complexity is O(1).


# 767. Reorganize String
# https://leetcode.com/problems/reorganize-string/description/

solution = Solution()
assert solution.reorganizeString("aab") == "aba"
assert solution.reorganizeString("aaab") == ""
