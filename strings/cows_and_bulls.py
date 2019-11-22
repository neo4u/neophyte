class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls, cows, n = 0, 0, len(secret)
        counts = [0] * 10

        for i in range(n):
            s, g = int(secret[i]), int(guess[i])
            if s == g: bulls += 1
            else:
                if counts[s] < 0: cows += 1
                if counts[g] > 0: cows += 1
                counts[s] += 1
                counts[g] -= 1

        return f'{bulls}A{cows}B'


# 299. Bulls and Cows
# https://leetcode.com/problems/bulls-and-cows/description/

# Example 1: secret = '1807', guess = '7810'
# i = 0
# s: 1, g; 7: inc counts[1] and dec counts[7]
# s: 1 | g: 7 | bulls: 0 | cows: 0 | counts: [0, 1, 0, 0, 0, 0, 0, -1, 0, 0]
# i = 1
# 8, 8: bull
# s: 8 | g: 8 | bulls: 1 | cows: 0 | counts: [0, 1, 0, 0, 0, 0, 0, -1, 0, 0]
# 0, 1: inc counts[0] and dec counts[1], counts[g]: 1 > 0 so inc cows
# s: 0 | g: 1 | bulls: 1 | cows: 1 | counts: [1, 0, 0, 0, 0, 0, 0, -1, 0, 0]
# 7, 0: inc counts[7] and dec counts[0], counts[s]: -1 < 0, counts[g]: 1 > 0, inc + 2 cows
# s: 7 | g: 0 | bulls: 1 | cows: 3 | counts: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Example 2: secret = '1123', guess = '0111'
# s: 1 | g: 0 | bulls: 0 | cows: 0 | counts: [-1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
# s: 1 | g: 1 | bulls: 1 | cows: 0 | counts: [-1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
# s: 2 | g: 1 | bulls: 1 | cows: 1 | counts: [-1, 0, 1, 0, 0, 0, 0, 0, 0, 0]
# s: 3 | g: 1 | bulls: 1 | cows: 1 | counts: [-1, -1, 1, 1, 0, 0, 0, 0, 0, 0]


sol = Solution()
assert sol.getHint('1807', '7810') == '1A3B'
assert sol.getHint('1123', '0111') == '1A1B'
assert sol.getHint('1462', '1246') == '1A3B'
