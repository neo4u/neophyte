class Solution:
    def minStickers(self, stickers, target):
        m = len(stickers)
        stkr_counts = [[0] * 26 for y in range(m)]
        for i in range(m):
            for c in stickers[i]:
                stkr_counts[i][ord(c) - ord("a")] += 1

        dp = {}
        dp[""] = 0

        return self.bt(dp, stkr_counts, target)

    def bt(self, dp, stkr_cnts, target):
        if target in dp: return dp[target]

        n = len(stkr_cnts)
        tar = [0] * 26
        for c in target:
            tar[ord(c) - ord("a")] += 1

        ans = float("inf")
        for i in range(n):
            if stkr_cnts[i][ord(target[0]) - ord("a")] == 0: continue

            s = ""
            for j in range(26):
                if tar[j] > stkr_cnts[i][j]:
                    s += chr(ord("a") + j) * (tar[j] - stkr_cnts[i][j])

            tmp = self.bt(dp, stkr_cnts, s)
            if tmp != -1:
                ans = min(ans, 1 + tmp)

        dp[target] = -1 if ans == float("inf") else ans
        return dp[target]


import collections

class Solution:
    def minStickers(self, stickers, target):
        t_count = collections.Counter(target)
        stkr_cntrs = [collections.Counter(sticker) & t_count for sticker in stickers]
        n = len(stkr_cntrs)

        for i in range(n - 1, -1, -1):
            if any(stkr_cntrs[i] == stkr_cntrs[i] & stkr_cntrs[j] for j in range(n) if i != j): # if A == A & B, then B contains A and then some chars.
                stkr_cntrs.pop(i)

        stickers = ["".join(stkr_cntr.elements()) for stkr_cntr in stkr_cntrs]
        dp = [-1] * (1 << len(target))
        dp[0] = 0

        for state in range(1 << len(target)):
            if dp[state] == -1: continue
            for sticker in stickers:
                now = state
                for letter in sticker:
                    for i, c in enumerate(target):
                        if (now >> i) & 1: continue
                        if c == letter:
                            now |= 1 << i
                            break
                if dp[now] == -1 or dp[now] > dp[state] + 1:
                    dp[now] = dp[state] + 1

        return dp[-1]
