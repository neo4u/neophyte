class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        return sorted(logs, key=self.custom_cmp)

    def custom_cmp(self, log):
        iden, rest = log.split(" ", 1)
        return (0, rest, iden) if rest[0].isalpha() else (1,)
