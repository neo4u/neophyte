
# Approach 1: Max Heap
import heapq
from collections import Counter
class Solution1(object):
    def topKFrequent(self, nums, k):
        heap = [(-val, key) for key, val in Counter(nums).items()]
        heapq.heapify(heap) # O(n)
        result = []

        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        return result


# Approach 2: Min-Heap
import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums, k):
        heap = []
        for num, freq in Counter(nums).items():
            heapq.heappush(heap, (freq, num))

            if len(heap) > k:
                heapq.heappop(heap)

        return [item[1] for item in heap]


# Approach 3: Bucket Sort
import collections
class Solution3:
    def topKFrequent(self, nums, k):
        result = []
        n = len(nums)
        counts_bucket = [[] for _ in range(n)]

        for num, freq in collections.Counter(nums).items():
            counts_bucket[freq - 1].append(num)

        for i in range(n - 1, -1, -1):
            if not counts_bucket[i]: continue
            result += counts_bucket[i]
            if len(result) >= k: break

        return result[:k]


# # Approach 4: Quick-Select
import random
import collections
class Solution:
    def topKFrequent(self, nums, k):
        def quick_select(a, l, r, K):
            if l == r: return
            mid = rand_partition(a, l, r)

# 5,6,5,3,4,5,2

            if K < mid:
                quick_select(a, l, mid - 1, K)
            elif K > mid:
                quick_select(a, mid + 1, r, K)
            else:
                return

        def rand_partition(a, l, r):
            i = random.randint(l, r)
            a[r], a[i] = a[i], a[r]
            return partition(a, l, r)

        def partition(a, l, r):
            i = l - 1
            pivot = a[r][1]
            for j in range(l, r):
                if a[j][1] > pivot: continue
                i += 1
                a[i], a[j] = a[j], a[i]

            a[i + 1], a[r] = a[r], a[i + 1]
            return i + 1

        counts = list(collections.Counter(nums).items())
        n = len(counts)
        quick_select(counts, 0, n - 1, n - k)
        return [x[0] for x in counts[n - k:]]


# 347. Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/

# Key Insight:
# 1. Within top K order is not important, we just need the top K frequent elements

# Approach 1: Max heap
# Steps:
# 1. Create a frequency map
# 2. Add every tuple (frequency, item) to a max heap
# 3. Then extract the top k elements

# Time: nlog(n)(n + k) log(n) => nlog(n)
# Space: O(n)

# Approach 2: Min-heap
# 1. Create a frequency map.
# 2. Add k tuples (frequency, item) to min-heap.
# 3. Iterate from k + 1 th tuple to nth tuple.
#    Now that size is k, Do a heapreplace only if new tuple's count is > than smallest on the pqueue
# 4. Finally the heap will have k largest frequency numbers, return it.
# Note: Order doesn't matter for the answer

# Time: O(nlog(k))
# Space: O(k)

# Approach 3: Bucket Sort
# Steps:
# 1. Create a count_bucket array of size = len(nums), initialized with values []
# 2. Use Counter class to get frequencies of each number
# 3. Use count as buckets to append every element with count c to index c - 1 in count
# 4. Now we move from back of the count array, pick buckets that aren't empty and add them to the result
#    until the result is of size k.

# Time: O(n)
# Space: O(n)

# Approach 4: Quick Select
# Steps:
# 1. Get the counts using collections.counter
# 2. Do a quick select on the counts list using n - k as K,
#    Thus, converting kth smallest to kth largest
# 3. Now we'll have the elements after n - kth positing all having k largest frequencies
# 4. Return the actual elements from those items

# Time: O(n), Avg case due to randomization
# Space: O(1)

sol = Solution()
assert sol.topKFrequent([1,1,1,2,2,3], 2) in ([1,2], [2,1])