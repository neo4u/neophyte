class Solution:
    def rotatedDigits(self, N):
        res = 0
        for num in range(1, N + 1):
            found = False
            while num:
                d = num % 10
                if d in {3, 4, 7}:
                    found = False
                    break
                if d in {2, 5, 6, 9}: found = True
                num //= 10

            if found: res += 1
        return res

# sol = Solution()
# assert sol.rotatedDigits(2) == 1
