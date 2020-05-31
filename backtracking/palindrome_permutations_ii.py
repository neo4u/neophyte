import collections
from typing import List


class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        counts = collections.Counter(s)
        odd_c_count, mid, result = 0, '', []
        for c, count in counts.items():
            if count % 2 == 1:
                odd_c_count += 1
                mid = c

        if odd_c_count > 1: return []

        to_permute = ''
        for c, count in counts.items():
            to_permute += c * (count // 2)
        if not to_permute: return [mid]
        unq_perms = self.permute_unq(to_permute)

        for perm in unq_perms:
            result.append(perm + mid + perm[::-1])
        return result

    def permute_unq(self, s: str) -> List[str]:
        counts = collections.Counter(s)
        self.result = []
        self.bt(list(s), 0)
        return self.result

    def bt(self, s, s_idx):
        n = len(s)
        if s_idx == n - 1: self.result.append(''.join(s))
        used = set()

        for i in range(s_idx, n):
            c = s[i]
            if c in used: continue
            used.add(c)
            if s_idx != i: self.swap(s, s_idx, i)
            self.bt(s, s_idx + 1)
            if s_idx != i: self.swap(s, s_idx, i)

    def swap(self, s, i, j):
        s[i], s[j] = s[j], s[i]



# 267. Palindrome Permutation II
# https://leetcode.com/problems/palindrome-permutation-ii/description/