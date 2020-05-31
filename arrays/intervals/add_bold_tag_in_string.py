from typing import List


class Solution:
    def addBoldTag(self, s, dict):
        #find all overlapping matches
        matches = []
        for word in dict:
            start = 0
            while True:
                start = s.find(word, start)
                if start == -1:
                    break
                else:
                    matches.append([start, start + len(word)])
                    start += 1
        #merge all matches like intervals            
        matches = sorted(matches)
        self.mergeInterval(matches)
        #concatenate string
        ret = ""
        pos = 0
        for start, end in matches:
            ret += s[pos:start] + '<b>' + s[start:end] + '</b>'
            pos = end
        ret += s[pos:]
        return ret

    def mergeInterval(self, intervals):
        start, end = 0, 0
        n = len(intervals)
        while end < n:
            intervals[start] = intervals[end]
            while end < n and intervals[end][0] <= intervals[start][1]:
                intervals[start][1] = max(intervals[start][1], intervals[end][1])
                end += 1
            start += 1
        del intervals[start:]




class Solution:
    def addBoldTag(self, s: str, dict: List[str]) -> str:
        # Step 1: Find intervals - unique intervals sorted by interval start index
        def findIntervals(s: str, dict: List[str]) -> List[List[int]]:
            dictSet = set(dict) #eliminate duplicates from list of substrings
            intervals = []
            for i in range(len(s)):
                for word in dictSet:
                    if s.startswith(word, i):
                        intervals.append([i, i+ len(word)])
            intervals = sorted(intervals, key=lambda x: x[0])
            return intervals

        # Step 2: Merge intervals
        def mergeIntervals(intervals: List[List[int]]) -> List[List[int]]:
            i = 0
            while i < len(intervals) - 1:
                s1, e1 = intervals[i]
                s2, e2 = intervals[i+1]
                if e1 < s2:
                    i += 1
                else:
                    intervals.pop(i+1)
                    intervals.pop(i)
                    intervals.insert(i, [s1, max(e1, e2)])
            return intervals

        # Step 3: Use interval list to get final result: create string with bold tags
        def createString(s: str, intervals: List[List[int]]) -> str:
            # loop through each interval in reverse order to not mess up the interval 
            # indexes:
            # adding bold tags to the string from the begining of the string will make 
            # the subsequent intervals off by the number of bold tags added * 7 as 
            # each pair of bold tags has length 7: len("<b></b>")
            for i in range(len(intervals) -1, -1, -1):
                start, end = intervals[i]
                s = s[:start]+ "<b>" + s[start:end] + "</b>" + s[end:]
            return s
        return createString(s, mergeIntervals( findIntervals( s, dict) ) )


# Approach 1: Merge Intervals

# This problem is another variation of Merge Intervals

# 3 Steps:
# 1. Get/Construct the sorted interval list =>
#   - Some problems might give you the interval list and you just have to sort them by the interval start time.
#   - Other problems like bold tags give you some initial data (ex: string and substring array in this problem) and expect you to construct the sorted interval list.
# 2. Merge over lapping intervals. The resulting interval list should only have disjoint intervals.
# 3. Return the merged interval list or use the merged interval list to get the final result (ex: adding bold tags => <b> at start index and </b> at the end index of each [start, end] interval)
