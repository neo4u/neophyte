def exclusiveTime(self, N, logs):
    ans = [0] * N
    stack = []
    prev_time = 0

    for log in logs:
        fn, typ, time = log.split(':')
        fn, time = int(fn), int(time)

        if typ == 'start':
            if stack:
                ans[stack[-1]] += time - prev_time 
            stack.append(fn)
            prev_time = time
        else:
            ans[stack.pop()] += time - prev_time + 1
            prev_time = time + 1

    return ans


# https://leetcode.com/problems/exclusive-time-of-functions/discuss/105100/Python-Straightforward-with-Explanation