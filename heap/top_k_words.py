# Approach 1: Sort
class Solution(object):
    def topKFrequent(self, words, k):
        count = collections.Counter(words)
        candidates = count.keys()
        candidates.sort(key=lambda w: (-count[w], w))
        return candidates[:k]


# Approach 2: Heap
class Solution2(object):
    def topKFrequent(self, words, k):
        count = collections.Counter(words)
        heap = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]

# Solution doesn't work because words same frequency have to be returned in lexicographical order
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = collections.Counter(words)
        heap = []
        for word, freq in count.items():
            heapq.heappush(heap, (freq, word))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [heapq.heappop(heap)[1] for _ in range(k)][::-1]
# 692. Top K Frequent Words
# https://leetcode.com/problems/top-k-frequent-words/description/

# Key Insights:

# 1. Frequency and Order are important here, as opposed to problem 347.
# 2. Quick Select won't work, cuz order is important
# 3. heapify in python takes care of ordering words when there is a tie in frequency

# Approach 1: Sorting
# Steps:
# 1. Use Counter class to build frequency map
# 2. Get the keys from the freq map in candidates
# 3. And sort the candidates using 1st key and the words themselves as the 2nd key
#    Sorting tuples sorting on 1st field first and 2nd field on ties
# 4. Return the 1st k candidate words

# Time: O(nlog(n))
# Space: O(n)

# Approach 2: Heap
# Steps:
# 1. Use Counter class to get words and counts
# 2. Use negative frequencies to simulate max heap
# 3. Build heap out of the count dictionary as a tuple
#    This heap operation takes care of ordering words when frequencies are tied, in sorted order
# 5. Now just form an array of words out of popping k elements from heap and using their words

# Time: O(n + klog(n)) Build heap is O(n), pop from heap is O(log(n))
# Space: O(n), We store all the elements in heap, and not just k
