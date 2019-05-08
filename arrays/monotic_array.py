class Solution(object):
    def isMonotonic(self, A):
        increasing = decreasing = True

        for i in range(len(A) - 1):
            if A[i] > A[i+1]:
                increasing = False
            if A[i] < A[i+1]:
                decreasing = False
            return False if increasing and decreasing

        return increasing or decreasing



class Solution(object):
    def isMonotonic(self, A):
        increasing = decreasing = False

        for i in range(len(A) - 1):
            if A[i] > A[i+1]:
                increasing = True
            if A[i] < A[i+1]:
                decreasing = True
            if increasing and decreasing: return False

        return True


class Solution:
    def isMonotonic(self, A):
        return self.is_down(A) or self.is_up(A)

    def is_up(self, A):
        s = A[0]
        for i in A:
            if i < s: return False
            s = i
        return True
    
    def is_down(self, A):
        s = A[0]
        for i in A:
            if i > s: return False
            s = i
        return True