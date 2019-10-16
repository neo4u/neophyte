from typing import List


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        if not logs: return []
        result, stack = [0] * n, []

        for log in logs:
            fid, ftype, ts = log.split(':')
            fid, ts = int(fid), int(ts)

            if ftype == 'start':
                curr_time = ts
                if stack: result[stack[-1]] += curr_time - prev_time
                stack.append(fid)
            else:
                curr_time = ts + 1
                result[stack.pop()] += curr_time - prev_time
            prev_time = curr_time

        return result


# n = 2
# logs = [
# "0:start:0",
# "1:start:2",
# "1:end:5",
# "0:end:6"]
# Output: [3, 4]

# s [], ts = 0, s = [0], prev_time = 0,
# r [0 0]

# s [0], time - prev_t = 2 - 0, 
# r [2, 0], s [0, 1]

# s[0 1], pt = 2, ct = 5 + 1, 5 + 1 - 2 = 4
# r[2 4], s[0] , pt = 6

# s[0], pt 6, ct = 7, 7 - 6 = 1
# r[3, 4], s[]



# https://leetcode.com/problems/exclusive-time-of-functions/discuss/105100/Python-Straightforward-with-Explanation