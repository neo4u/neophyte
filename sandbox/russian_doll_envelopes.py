class Solution:
    def maxEnvelopes(self, envs):
        envs = sorted(envs, key=lambda e: e[1], reverse=True)
        envs = sorted(envs, key=lambda e: e[0])
        tails, size = [], 0

        for w, h in envs:
            i = self.binary_search(tails, h)
            if i == size:
                tails.append(h)
                size += 1
            else:
                tails[i] = h

        return size

    def binary_search(self, tails, h):
        l, r = 0, len(tails) - 1
        while l <= r:
            mid = (l + r) / 2
            if tails[mid] == h: return mid

            if tails[mid] < h:  l = mid + 1
            else:               r = mid - 1

        return l


# 5 1 2 3
# 8 6 3