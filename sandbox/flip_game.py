class Solution:
    def generatePossibleNextMoves(self, s: str) -> List[str]:
        n, result = len(s), []

        for i in range(n - 1):
            if s[i] == '+' and s[i + 1] == '+':
                flip_s = s[:i] + '--' + s[i + 2:]
                result.append(flip_s)

        return result