import heapq
from typing import List


class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        distances = []     # distances[worker] is 3-tuple of (distance, worker, bike) for each bike

        for i, (x, y) in enumerate(workers):
            distances.append([])
            for j, (x_b, y_b) in enumerate(bikes):
                distance = abs(x - x_b) + abs(y - y_b)
                distances[-1].append((distance, i, j))
            distances[-1].sort(reverse=True)  # reverse so we can pop the smallest distance

        result = [None] * len(workers)
        used_bikes = set()
        queue = [distances[i].pop() for i in range(len(workers))]   # smallest distance for each worker
        heapq.heapify(queue)

        while len(used_bikes) < len(workers):
            _, worker, bike = heapq.heappop(queue)
            if bike not in used_bikes:
                result[worker] = bike
                used_bikes.add(bike)
            else:
                heapq.heappush(queue, distances[worker].pop())  # bike used, add next closest bike

        return result


# Approach 1: Heap
# Steps:
# For each worker, create a sorted list of distances to each bike. The elements of the list are tuples (distance, worker, bike).
# For each worker, add the tuple with the shortest distance to the heap.
# Until each worker has a bike, pop the smallest distance from the heap.
# If this bike is not used, update the result for this worker, else add the next closest tuple for this worker to the heap.

# Approach 2: Sort + Greedy


# W is number of workers, B is number of bikes
# Time: O(WB log(WB))
# Space: O(WB log(WB))
