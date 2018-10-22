# First solution is O(nlogn) which uses a heap to
# place most frequent elements in first priority.

# Second solution is O(n): the number of the most frequent tasks will
# determine the length and tied tasks will exist in the last cycle.

class Solution(object):
    
    # O(nlogn) greedy to place most popular and distinct tasks first
    # Actually, I don't think this is greedy
    # We always place different tasks in a cycle which will minimize steps
    # If not different tasks can be placed in a cycle, place an `idle`.
    
    def _leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        n += 1
        ans = 0
        d = collections.Counter(tasks)
        heap = [-c for c in d.values()]
        heapq.heapify(heap)
        while heap:
            stack = []
            cnt = 0
            for _ in range(n):
                if heap:
                    c = heapq.heappop(heap)
                    cnt += 1
                    if c < -1:
                        stack.append(c + 1)
            for item in stack:
                heapq.heappush(heap, item)
            ans += heap and n or cnt # == if heap then n else cnt
        return ans


    # O(n) # of the most frequent tasks, say longest, will determine the legnth
    # to void counting idle intervals, we count (longest - 1) * (n + 1)
    # then count how many will in the last cycle which means finding ties
    # if counted number is less than # of tasks which means 
    # less frequent tasks can be always placed in such cycle
    # and it won't cause any conflicts with requirement since even most frequent can be settle
    # finally, return max(# of task, total counted number)

    def leastInterval(self, tasks, n):
        d = collections.Counter(tasks)
        counts = d.values()
        longest = max(counts)
        ans = (longest - 1) * (n + 1)
        for count in counts:
            ans += count == longest and 1 or 0
        return max(len(tasks), ans)


# The trick is that Python does not have a max heap queue, so we must make every number negative when we throw it into the heap.
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        if n == 0:
            return len(tasks)

        hs = collections.defaultdict(int)
        for task in tasks:
            hs[task] += 1

        count = 0
        cycle = n + 1

        heap = []

        for k, i in hs.iteritems():
            if i > 0:
                heapq.heappush(heap, (-i))
        while heap:
            worktime = 0
            tmp = []
            for i in xrange(cycle):
                if heap:
                    tmp.append(heapq.heappop(heap))
                    worktime += 1
            for cnt in tmp:
                cnt *= -1
                cnt -= 1
                if cnt > 0:
                    heapq.heappush(heap, -cnt)
            
            count += cycle if len(heap) > 0 else worktime

        return count

# Examples:

# AAAABBBEEFFGG 3

# here X represents a space gap:

# Frame: "AXXXAXXXAXXXA"
# insert 'B': "ABXXABXXABXXA" <--- 'B' has higher frequency than the other characters, insert it first.
# insert 'E': "ABEXABEXABXXA"
# insert 'F': "ABEFABEXABFXA" <--- each time try to fill the k-1 gaps as full or evenly as possible.
# insert 'G': "ABEFABEGABFGA"
# AACCCBEEE 2

# 3 identical chunks "CE", "CE CE CE" <-- this is a frame
# insert 'A' among the gaps of chunks since it has higher frequency than 'B' ---> "CEACEACE"
# insert 'B' ---> "CEABCEACE" <----- result is tasks.length;
# AACCCDDEEE 3

# 3 identical chunks "CE", "CE CE CE" <--- this is a frame.
# Begin to insert 'A'->"CEA CEA CE"
# Begin to insert 'B'->"CEABCEABCE" <---- result is tasks.length;
# ACCCEEE 2

# 3 identical chunks "CE", "CE CE CE" <-- this is a frame
# Begin to insert 'A' --> "CEACE CE" <-- result is (c[25] - 1) * (n + 1) + 25 -i = 2 * 3 + 2 = 8

# The key is to find out how many idles do we need.
# Let's first look at how to arrange them. it's not hard to figure out that we can do a "greedy arrangement": always arrange task with most frequency first.
# E.g. we have following tasks : 3 A, 2 B, 1 C. and we have n = 2. According to what we have above, we should first arrange A, and then B and C. Imagine there are "slots" and we need to arrange tasks by putting them into "slots". Then A should be put into slot 0, 3, 6 since we need to have at least n = 2 other tasks between two A. After A put into slots, it looks like this:

# A ? ? A ? ? A
# "?" is "empty" slots.

# Now we can use the same way to arrange B and C. The finished schedule should look like this:

# A B C A B # A
# "#" is idle

# Now we have a way to arrange tasks. But the problem only asks for number of CPU intervals, so we don't need actually arrange them. Instead we only need to get the total idles we need and the answer to problem is just number of idles + number of tasks.
# Same example: 3 A, 2 B, 1 C, n = 2. After arranging A, we have:
# A ? ? A ? ? A
# We can see that A separated slots into (count(A) - 1) = 2 parts, each part has length n. With the fact that A is the task with most frequency, it should need more idles than any other tasks. In this case if we can get how many idles we need to arrange A, we will also get number of idles needed to arrange all tasks. Calculating this is not hard, we first get number of parts separated by A: partCount = count(A) - 1; then we can know number of empty slots: emptySlots = partCount * n; we can also get how many tasks we have to put into those slots: availableTasks = tasks.length - count(A). Now if we have emptySlots > availableTasks which means we have not enough tasks available to fill all empty slots, we must fill them with idles. Thus we have idles = max(0, emptySlots - availableTasks);
# Almost done. One special case: what if there are more than one task with most frequency? OK, let's look at another example: 3 A 3 B 2 C 1 D, n = 3
# Similarly we arrange A first:
# A ? ? ? A ? ? ? A
# Now it's time to arrange B, we find that we have to arrange B like this:
# A B ? ? A B ? ? A B
# we need to put every B right after each A. Let's look at this in another way, think of sequence "A B" as a special task "X", then we got:
# X ? ? X ? ? X
# Comparing to what we have after arranging A:
# A ? ? ? A ? ? ? A
# The only changes are length of each parts (from 3 to 2) and available tasks. By this we can get more general equations:
# partCount = count(A) - 1
# emptySlots = partCount * (n - (count of tasks with most frequency - 1))
# availableTasks = tasks.length - count(A) * count of tasks with most frenquency
# idles = max(0, emptySlots - availableTasks)
# result = tasks.length + idles

# What if we have more than n tasks with most frequency and we got emptySlot negative? Like 3A, 3B, 3C, 3D, 3E, n = 2. In this case seems like we can't put all B C S inside slots since we only have n = 2.
# Well partCount is actually the "minimum" length of each part required for arranging A. You can always make the length of part longer.
# E.g. 3A, 3B, 3C, 3D, 2E, n = 2.
# You can always first arrange A, B, C, D as:
# A B C D | A B C D | A B C D
# in this case you have already met the "minimum" length requirement for each part (n = 2), you can always put more tasks in each part if you like:
# e.g.
# A B C D E | A B C D E | A B C D

# emptySlots < 0 means you have already got enough tasks to fill in each part to make arranged tasks valid. But as I said you can always put more tasks in each part once you met the "minimum" requirement.

# To get count(A) and count of tasks with most frequency, we need to go through inputs and calculate counts for each distinct char. This is O(n) time and O(26) space since we only handle upper case letters.
# All other operations are O(1) time O(1) space which give us total time complexity of O(n) and space O(1)

# Algorithm
# 1. This is an extremely tricky problem.
# 2. The main idea is to schedule the most frequent tasks as frequently as possible. Begin with scheduling the most frequent task. Then cool-off for n, and in that cool-off period schedule tasks in order of frequency, or if no tasks are available, then be idle.
#     Exampe: Say we have the following tasks: [A,A,A,B,C,D,E] with n =2
#     Now if we schedule using the idea of scheduling all unique tasks once and then calculating if a cool-off is required or not, then we have: A,B,C,D,E,A,idle,dile,A i.e. 2 idle slots.
#     But if we schedule using most frequent first, then we have:
#     2.1: A,idle,idle,A,idle,idle,A
#     2.2: A,B,C,A,D,E,A i.e. no idle slots. This is the general intuition of this problem.
# 3.The idea in two can be implemented using a heap and temp list. This is illustrated in the code below.

# Time complexity is O(N * n) where N is the number of tasks and n is the cool-off period.
# Space complexity is O(1) - will not be more than O(26).

from heapq import heappush, heappop
from collections import Counter
class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        curr_time, h = 0, []
        for k,v in Counter(tasks).items():
            heappush(h, (-1*v, k))
        while h:
            i, temp = 0, []
            while i <= n:
                curr_time += 1
                if h:
                    x,y = heappop(h)
                    if x != -1:
                        temp.append((x+1,y))
                if not h and not temp:
                    break
                else:
                    i += 1
            for item in temp:
                heappush(h, item)
        return curr_time

# Approach 1: Using sorting Time: O(time), Space: O(1)
# Approach 2: Using pqueue, Time: O(n), Space: O(1)
# Approach 3: Calculating the idle slots, Time: O(n), Space: O(1)