class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        if not A:
            return 0

        n, l, r, max_len = len(A), 0, 1, 1

        while r < n:
            prev = A[r - 1] < A[r]
            prev_same = A[r - 1] == A[r]
            
            cur = False
            cur_same = False
            
            if r < n-1:
                cur = A[r] < A[r + 1]
                cur_same = A[r] == A[r + 1]

            if (r == n-1) or (not prev_same and not cur_same and prev ^ cur):
                max_len = max(max_len, r - l + 1)
            else:
                l = r
            r += 1

        return max_len

# [0,8,45,88,48,68,28,55,17,24]
#       l        r

# [9, 4, 2, 10, 7, 8, 8, 1, 9]
    # l            r
# [0, 1, 1, 0, 1, 0, 1, 1, 0, 0]


class Solution2(object):
    def cmp(self, a, b):
        return (a > b) - (a < b)

    def maxTurbulenceSize(self, A):
        N = len(A)
        max_len = 1
        l, r = 0, 1

        while r < N:
            c = self.cmp(A[r - 1], A[r])
            if c == 0:
                l = r
            elif r == N - 1 or c * self.cmp(A[r], A[r + 1]) != -1:
                max_len = max(max_len, r - l + 1)
                l = r
            r += 1
        return max_len

