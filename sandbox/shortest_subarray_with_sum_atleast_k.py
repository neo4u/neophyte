# Doesn't work cuz of the below example.
# class Solution:
#     def shortestSubarray(self, A: List[int], K: int) -> int:
#         l, r, min_len, win_sum = 0, 0, len(A) + 1, 0

#         while r < len(A):
#             win_sum += A[r]

#             while win_sum >= K:
#                 min_len = min(min_len, r - l + 1)
#                 win_sum -= A[l]
#                 l += 1
#             r += 1

#         return min_len if min_len != len(A) + 1 else 0


# [84, -37, 32, 40, 95]
# 167

# (2, 79), (3, 119), (4, 214)
# min_len = 3

# 214
import collections
class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        n = len(A)
        q, min_len, pre_sum = collections.deque([(-1,0)]), n+1, 0

        for i, num in enumerate(A):
            pre_sum += num
            if num > 0:
                while q and pre_sum - q[0][1] >= K:
                    min_len = min(min_len, i - q.popleft()[0])
            else:
                while q and q[-1][1] >= pre_sum:
                    q.pop()
            q.append((i, pre_sum))

        return -1 if min_len == n + 1 else min_len


# First we build a prefix sum array pre_sum so that pre_sum[j]-pre_sum[i] will be the sum of subarray A[i+1:j+1].
# So once there is a pre_sum[j] - pre_sum[i] >= K, we have a candidate length j-i. So we can implement slide window here to find out smallest j-i.

# To slide window, we append previous iterated index to a queue as left end and current iterating index as right end.
# So left end would be q[0] and right end would be i. Once we found pre_sum[i] - pre_sum[q[0]] >= K, we have a valid window.
# Then we keep reducing window's size by left popping q (increase left end) until window comes to be invalid(pre_sum[i] - pre_sum[q[0]] < k).

# Since K >= 1, we don't need to consider decreasing pre_sum elements.
# For example, if we have pre_sum[i:i+4] = [4,8,2], we just retain [2] and pop out [4,8] since pre_sum[i:i+2], pre_sum[i+1:i] or A[i-1:i+1], A[i:i+1] will never be a candidate subarray.
# given a new pre_sum 10
# [4, 8, 2, 10] now [2, 10] is feasible (>= K) then it is better than [4, 10] or [8, 10]
# [2, 10] is not feasible then [4, 10] and [8, 10] will also not be feasible.

# So we can reduce our queue size by maintaining a mono-increasing queue.

# Furthermore, we can build prefix sum array and mono-increasing queue at the same time.
# And we also update our candidate subarray length simultaneously. So our queue element will be a tuple of (left_index, pre_sum).
# In such way, if current iterating element a is larger than 0, we only update slide window, if it's smaller or equal to 0, we only update queue.

# Why does monotone increasing help us find candidates:
# 1. Infeasible candidates at the start may cause us to expand our window to right, without being able to contract,
#    and while contracting the window from left, our bad candidates cause our window to look bad thus preventing us
#    from contracting and finding better candidates later in the window.
# 2. Feasible candidates at the front may be a waste of cycles if there is a better candidate later in the window
