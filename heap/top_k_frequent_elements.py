
# Heap: klog(N)
# Klog(N) - Create a frequency map and then add every tuple (frequency, item) to a max heap. Then extract the top k elements.
import heapq
from collections import Counter, defaultdict
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        heap = [(-1*v1, k1) for k1,v1 in Counter(nums).items()]
        heapq.heapify(heap)
        result = []
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        return result

# Heap: Nlog(k)
# Create a frequency map.
# Add k tuples (frequency, item) to min-heap.
# Iterate from k+1st tuple to Nth tuple. If the tuple frequency is more than top of heap, pop from heap and add the tuple.
# Finally the heap will have k largest frequency numbers

# Bucket Sort
from collections import Counter, defaultdict
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq, result = Counter(nums), []
        inverse_freq = defaultdict(list)
        for k1,v1 in freq.items():
            inverse_freq[v1].append(k1)
        for x in range(len(nums), 0, -1):
            if x in inverse_freq:
                result.extend(inverse_freq[x])
                if len(result) >= k:
                    break
        return result[:k]

# 347. Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/

# Approach 1: Min heap
# Approach 2: Min-heap
# Approach 3: Bucket Sort
