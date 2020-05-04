from typing import List


# Approach 2: Heap
import heapq
class SummaryRanges1:
    def __init__(self):
        self.heap = []
        self.seen = set()

    def addNum(self, val):
        if val in self.seen: return

        self.seen.add(val)
        heapq.heappush(self.heap, [val, val])

    def getIntervals(self):
        stack = []

        while self.heap:
            cur = heapq.heappop(self.heap)
            if stack and cur[0] <= stack[-1][1] + 1: stack[-1][1] = max(stack[-1][1], cur[1])
            else:                                    stack.append(cur)

        self.heap = stack
        return self.heap


# Approach 2: Binary Search
class SummaryRanges:
    def __init__(self):
        self.intervals = []

    def addNum(self, val: int) -> None:
        n = len(self.intervals)
        l, r = 0, n - 1

        while l <= r:                                                           # find pos to insert, will be l after loop exit
            mid = (l + r) // 2
            x = self.intervals[mid]

            if x[0] <= val <= x[1]: return
            elif x[0] > val:        r = mid - 1
            else:                   l = mid + 1

        pos = l
        self.intervals.insert(pos, [val, val])                                  # insert the interval at pos

        if pos < n and val + 1 == self.intervals[pos + 1][0]:                   # merge with next interval
            self.intervals[pos][1] = self.intervals[pos + 1][1]
            del self.intervals[pos + 1]

        if pos > 0 and val - 1 == self.intervals[pos - 1][1]:                   # merge with prev interval
            self.intervals[pos][0] = self.intervals[pos - 1][0]
            del self.intervals[pos - 1]

    def getIntervals(self) -> List[List[int]]:
        return self.intervals



# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()


# 352. Data Stream as Disjoint Intervals
# https://leetcode.com/problems/data-stream-as-disjoint-intervals/description/


# Approach 1: Heap
# Time: addNum: log(n) per number, getIntervals(): n * log(n)
# Space: O(n), worst case each number has it's own interval

# Heap:
# addNum() n times is O(n * log n),
# getIntervals() once is O(n * log n)

# BST:
# addNumb() n times is O(n * log n),
# getIntervals() once is O(n), it just travel once.

# Approach 2: Binary Search
# Time: addNum() log(n) for finding pos, n for adding cuz of array insertion of python, getIntervals(): O(1)
# Space: O(n), worst case each number has it's own interval


# Q: Why we can't do while l < r kinda binary search
# Explanation:
# Example: stream = [1, 3, 7, 2, 6,...]
# 1
# we don't enter the while loop cuz l = 0 and r = -1 so l <= r is false
# self.intervals = [1, 1] after we insert

# 3
# we enter while l = 0, r = 0
#  l < r will be False
# hence we won't enter the loop and this will cause pos = 0, which is not where we want to insert [3, 3]
# but while l <= r will be True, will cause pos = 1 as is supposed to be the case

# Approach 1 tests
sol = SummaryRanges1()
sol.addNum(1)
assert sol.getIntervals() == [[1, 1]]
sol.addNum(3)
assert sol.getIntervals() == [[1, 1], [3, 3]]
sol.addNum(7)
assert sol.getIntervals() == [[1, 1], [3, 3], [7, 7]]
sol.addNum(2)
assert sol.getIntervals() == [[1, 3], [7, 7]]
sol.addNum(6)
assert sol.getIntervals() == [[1, 3], [6, 7]]
sol.addNum(25)
assert sol.getIntervals() == [[1, 3], [6, 7], [25, 25]]
sol.addNum(9)
assert sol.getIntervals() == [[1, 3], [6, 7], [9, 9], [25, 25]]
sol.addNum(8)
assert sol.getIntervals() == [[1, 3], [6, 9], [25, 25]]

# Approach 2 tests
sol = SummaryRanges()
sol.addNum(1)
assert sol.getIntervals() == [[1, 1]]
sol.addNum(3)
assert sol.getIntervals() == [[1, 1], [3, 3]]
sol.addNum(7)
assert sol.getIntervals() == [[1, 1], [3, 3], [7, 7]]
sol.addNum(2)
assert sol.getIntervals() == [[1, 3], [7, 7]]
sol.addNum(6)
assert sol.getIntervals() == [[1, 3], [6, 7]]
sol.addNum(25)
assert sol.getIntervals() == [[1, 3], [6, 7], [25, 25]]
sol.addNum(9)
assert sol.getIntervals() == [[1, 3], [6, 7], [9, 9], [25, 25]]
sol.addNum(8)
assert sol.getIntervals() == [[1, 3], [6, 9], [25, 25]]
