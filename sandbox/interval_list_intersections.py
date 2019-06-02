class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        m, n = len(A), len(B)
        result = []

        while i < m and j < n:
            a1, a2 = A[i]
            b1, b2 = B[j]
            if self.has_overlap(a1, a2, b1, b2):
                intersect = [max(a1, b1), min(a2, b2)]
                result.append(intersect)

            if a2 < b2: i += 1
            elif b2 < a2: j += 1
            else:
                i +=1 ; j += 1

        return result

    def has_overlap(self, a1, a2, b1, b2):
        return b1 <= a1 <= b2 or a1 <= b1 <= a2






# 4 8

# 1 3

""" ------
            -------

        -------
    --------------- 
    
    ------------
            ---------------

    """