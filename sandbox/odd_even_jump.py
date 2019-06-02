class Solution(object):
    def oddEvenJumps(self, A):
        N = len(A)

        def make(B):
            ans = [None] * N
            stack = []  # invariant: stack is decreasing
            for i in B:
                while stack and i > stack[-1]:
                    ans[stack.pop()] = i
                stack.append(i)
            return ans

        B = sorted(range(N), key = lambda i: A[i])
        oddnext = make(B)
        B.sort(key = lambda i: -A[i])
        evennext = make(B)

        odd = [False] * N
        even = [False] * N
        odd[N-1] = even[N-1] = True

        for i in range(N-2, -1, -1):
            if oddnext[i] is not None:
                odd[i] = even[oddnext[i]]
            if evennext[i] is not None:
                even[i] = odd[evennext[i]]

        return sum(odd)


# [10,13,12,14,15]

# b   [0, 2, 1, 3, 4]
# s   [4]
# on  [2, 3, 3, 4, None]

# [-10,-13,-12,-14,-15]
# [0, 2, 1, 3, 4]
# B = [4, 3, 1, 2, 0]
# s   [4, 3, 2, 0]
# en  [n, 2, n, n, n]

# on  [2, 3, 3, 4, None]
# en  [n, 2, n, n, n]

# o [f, f, f, f, t]
# e [f, f, f, f, t]

# i = 3
# on[3] = 4
# o [f, f, f, t, t]
# en[3] = None

# i = 2
# on[2] = 3
# e[3] = f
# o [2] = f
# o [f, f, f, f, t]
# en[2] = None
# e [f, f, f, f, t]

# i = 1
# on[1]  = 3
# e[3] = f
# o [1] = f
# o [f, f, f, f, t]
# en[1] = 2
# o[2] = f
# e[1] = f
# e [f, f, f, f, t]

# i = 0
# on[0] = 2
# e[2] = f
# o[0] = f
# o [f, f, f, f, t]
# en[0] = None