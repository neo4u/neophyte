import collections

class Solution:
    def customSortString(self, S: str, T: str) -> str:
        count = collections.Counter(T)
        ans = []

        for c in S:
            ans.append(c * count[c])
            count.pop(c)

        for c in count:
            ans.append(c * count[c])

        return "".join(ans)

