from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        return self.bt(s, 4)

    def bt(self, s, rem):
        if rem == 0:
            if s: return []
            else: return [""]
        if not s: return []
        result = []

        for i in range(1, min(len(s) + 1, 3 + 1)): # ranges of length of the left is from 1 to 3 so we need bounds 2 to 4
            l, r = s[:i], s[i:]

            if not self.valid(l): continue
            rest = self.bt(r, rem - 1)

            for item in rest:
                if item: result.append(l + "." + item)
                else: result.append(l)

        return result

    def valid(self, s):
        if s[0] == '0' and len(s) > 1: return False
        return 0 <= int(s) <= 255


# 93. Restore IP Addresses
# https://leetcode.com/problems/restore-ip-addresses/description/

sol = Solution()
assert sol.restoreIpAddresses("25525511135") == ["255.255.11.135", "255.255.111.35"]
assert sol.restoreIpAddresses("010010") == ["0.10.0.10", "0.100.1.0"]
