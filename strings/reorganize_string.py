import heapq
from collections import Counter
class Solution(object):
    def reorganizeString(self, S: str) -> str:
        counts = Counter(S)
        heap = [(-v, k) for k, v in counts.items()]
        heapq.heapify(heap)

        # If any char has frequency more than double of length + 1,
        # return "" as we can't possibly return a string without getting that char twice in sequence
        if any(-nc > (len(S) + 1) / 2 for nc, x in heap): return ""

        result = []
        while len(heap) >= 2:
            nct1, ch1 = heapq.heappop(heap)
            nct2, ch2 = heapq.heappop(heap)
            result.extend([ch1, ch2])
            if nct1 + 1: heapq.heappush(heap, (nct1 + 1, ch1))
            if nct2 + 1: heapq.heappush(heap, (nct2 + 1, ch2))

        return "".join(result) + (heap[0][1] if heap else '')

# Condensed
import heapq
from collections import Counter
class Solution:
    def reorganizeString(self, S: str) -> str:
        counts, result = Counter(S), []
        heap = [(-v, k) for k, v in counts.items()] # max heap
        heapq.heapify(heap)
        if any(-nc > (len(S) + 1) / 2 for nc, _ in heap): return ""

        while len(heap) >= 2:
            nc1, c1 = heapq.heappop(heap)
            nc2, c2 = heapq.heappop(heap)
            result.extend([c1, c2])
            if nc1 + 1: heapq.heappush(heap, (nc1 + 1, c1))
            if nc2 + 1: heapq.heappush(heap, (nc2 + 1, c2))

        return ''.join(result) + (heap[0][1] if heap else '')


# 767. Reorganize String
# https://leetcode.com/problems/reorganize-string/description/


# Approach 1: Heapq
# 1. We store a heap of (count, letter). [In Python, our implementation stores negative counts.]
# 2. We pop the top two elements from the heap (representing different letters with positive remaining count),
#    and then write the most frequent one that isn't the same as the most recent one written.
# 3. After, we push the correct counts back onto the heap.
# 4. Actually, we don't even need to keep track of the most recent one written.
# 5. If it is possible to organize the string,
#    the letter written second can never be written first in the very next writing.
# 6. At the end, we might have one element still on the heap,
#    which must have a count of one. If we do, we'll add that to the answer too.

# Complexity Analysis
# Time: O(NlogA)), where N is the length of S, and A is the size of the alphabet.
#                  If A is fixed, this complexity is O(N). The log A is due to heap data structure.
#                  Map depth of a heap is log n
# Space: O(A). If A is fixed, this complexity is O(1).


solution = Solution()
assert solution.reorganizeString("aab") == "aba"
assert solution.reorganizeString("aaab") == ""
