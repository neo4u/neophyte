class Solution:
    def diffWaysToCompute(self, s: str) -> List[int]:
        level_results = []

        for i, c in enumerate(s):
            if c not in ['+', '-', '*']: continue

            l, r = s[:i], s[i + 1:]
            l_results, r_results = self.diffWaysToCompute(l), self.diffWaysToCompute(r)

            for d1 in l_results:
                for d2 in r_results:
                    if c == "+":
                        level_results.append(d1 + d2)
                    elif c == "-":
                        level_results.append(d1 - d2)
                    else:
                        level_results.append(d1 * d2)

        if not level_results: level_results.append(int(s))
        return level_results