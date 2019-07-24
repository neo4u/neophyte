class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        a_ptr, b_ptr = 0, 0
        a, b = self.get_parts(version1), self.get_parts(version2)
        m, n = len(a), len(b)

        while a_ptr < m or b_ptr < n:
            a_part = a[a_ptr] if a_ptr < m else 0
            b_part = b[b_ptr] if b_ptr < n else 0
            if a_part == b_part:
                a_ptr += 1; b_ptr += 1
                continue

            return -1 if a_part < b_part else 1

        return 0

    def get_parts(self, s):
        return list(map(int, s.split('.')))
