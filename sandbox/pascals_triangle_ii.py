class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        prev = []

        for i in range(rowIndex + 1):
            curr = []
            for j in range(i + 1):
                to_insert = 1 if j == 0 or j == i else prev[j - 1] + prev[j]
                curr.append(to_insert)
            prev = curr

        return prev