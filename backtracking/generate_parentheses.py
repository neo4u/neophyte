class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return self.bt(n, 0, 0, "", [])

    def bt(self, n, l, r, path, res):
        if len(path) == 2 * n:
            return res.append(path)

        if l < n:
            self.bt(n, l + 1, r, path + "(", res)
        if r < l:
            self.bt(n, l, r + 1, path + ")", res)

        return res
