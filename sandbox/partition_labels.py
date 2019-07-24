class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last = {c: i for i, c in enumerate(S)}
        i = l = 0
        ans = []
        for r, c in enumerate(S):
            i = max(i, last[c])     # Push window
            if r == i:              # Check if we reached the end of the window
                ans.append(r - l + 1)
                l = r + 1
        return ans

# abac
# r = 0, l = 0
# i = max(0, 2) = 2

# r 1
# i = max(1, 2) = 2, l = 0

# r 2
# i = max(2, 2) = 2, l = 0
# ans =  2 - 0 + 1 = 3, l = 3

# r 3
# i = max(2, 3) = 3, l = 3
# r == i => r - l + 1 = 3 - 3 + 1 = 1
# a [3, 1]


# last
# a 2
# b 1
# c 3