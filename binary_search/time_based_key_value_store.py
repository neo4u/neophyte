import bisect
import collections


class TimeMap:
    def __init__(self):
        self.time_map = collections.defaultdict(list)

    def set(self, key: str, value: str, ts: int) -> None:
        self.time_map[key].append((ts, value))

    def get(self, key: str, ts: int) -> str:
        vals = self.time_map[key]
        if not vals: return ''

        i = bisect.bisect(vals, (ts, chr(255)))
        return vals[i - 1][1] if i else ''


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)


# 981. Time Based Key-Value Store
# https://leetcode.com/problems/time-based-key-value-store/description/
