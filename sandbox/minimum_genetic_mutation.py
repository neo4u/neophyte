import collections
from typing import List

class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank = set(bank)

        patt_to_seqs = collections.defaultdict(set)
        for seq in bank:
            for i in range(len(seq)):
                pattern = seq[0:i] + '*' + seq[i + 1:]
                patt_to_seqs[pattern].add(seq)
        print(patt_to_seqs)

        q, visited, dist = [start], set([start]), 0
        while q:
            n = len(q)
            for i in range(n):
                w = q.pop(0)
                if w == end: return dist

                for j in range(len(w)):
                    patt = w[0:j] + '*' + w[j + 1:]
                    nbrs = patt_to_seqs[patt]
                    for nbr in nbrs:
                        if nbr in visited: continue
                        visited.add(nbr)
                        q.append(nbr)
            dist += 1

        return -1


sol = Solution()
assert sol.minMutation("AACCGGTT", "AAACGGTA", ["AACCGGTA","AACCGCTA","AAACGGTA"]) == 2
