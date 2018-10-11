from operator import truediv, mul, add, sub


class Solution(object):
    def judgePoint24(self, A):
        if not A:
            return False
        if len(A) == 1:
            return abs(A[0] - 24) < 1e-6

        for i in range(len(A)):
            for j in range(len(A)):
                if i != j:
                    B = [A[k] for k in range(len(A)) if i != k != j]
                    for op in (truediv, mul, add, sub):
                        if (op is add or op is mul) and j > i:
                            continue
                        if op is not truediv or A[j]:
                            B.append(op(A[i], A[j]))
                            if self.judgePoint24(B):
                                return True
                            B.pop()
        return False

# Complexity Analysis
# Time Complexity: O(1). There is a hard limit of 9216 possibilities,
#                  and we do O(1) work for each of them.
# Space Complexity: O(1). Our intermediate arrays are at most 4 elements,
#                   and the number made is bounded by an O(1) factor.
