class Solution:
    def validIPAddress(self, IP):
        if IP.count(".") == 3 and all(self.isIPv4(part) for part in IP.split(".")): return "IPv4"
        if IP.count(":") == 7 and all(self.isIPv6(part) for part in IP.split(":")): return "IPv6"
        return "Neither"

    def isIPv4(self, s):
        try:
            return str(int(s)) == s and 0 <= int(s) <= 255
        except ValueError:
            return False

    def isIPv6(self, s):
        if len(s) > 4: return False
        if s and s[0] == '-': return False

        try:
            dec = int(s, 16)
        except:
            dec = None

        return dec is not None and 0 <= dec <= 0xffff


class Solution:
    def validIPAddress(self, IP: str) -> str:
        grps = []
        idx = IP.find('.')
        ip_type = 'IPv4'

        if idx != -1:
            grps = IP.split('.')
            if len(grps) != 4: return 'Neither'
        else:
            grps = IP.split(':')
            if len(grps) != 8: return 'Neither'
            ip_type = 'IPv6'

        if ip_type == 'IPv4':
            for chunk in grps:
                if not chunk: return 'Neither'
                if not chunk.isnumeric(): return 'Neither'
                if len(chunk) > 1 and chunk[0] == '0': return 'Neither'
                if chunk and chunk[0] == '-': return 'Neither'

                num = int(chunk)
                if not 0 <= num <= 255: return 'Neither'
        else:
            for chunk in grps:
                if not chunk: return 'Neither'

                for c in chunk:
                    if not ('0' <= c <= '9' or 'a' <= c <= 'f' or 'A' <= c <= 'F'):
                        return 'Neither'

                if int(chunk, 16) < 0: return 'Neither'
                if len(chunk) > 4: return 'Neither'

        return ip_type

# Cleaner
class Solution:
    def validIPAddress(self, IP: str) -> str:
        grps = []
        idx = IP.find('.')
        ip_type = 'IPv4'

        if idx != -1:
            grps = IP.split('.')
            if len(grps) != 4: return 'Neither'
        else:
            grps = IP.split(':')
            if len(grps) != 8: return 'Neither'
            ip_type = 'IPv6'

        if ip_type == 'IPv4':
            if all(self.valid_ipv4_chunk(chunk) for chunk in grps): return 'IPv4'
        else:
            if all(self.valid_ipv6_chunk(chunk) for chunk in grps): return 'IPv6'

        return 'Neither'

    def valid_ipv4_chunk(self, chunk):
        if not chunk: return False
        if len(chunk) > 1 and chunk[0] == '0': return False
        if not chunk.isnumeric(): return False
        if chunk and chunk[0] == '-': return False

        num = int(chunk)
        if not 0 <= num <= 255: return False
        return True

    def valid_ipv6_chunk(self, chunk):
        if not chunk: return False

        for c in chunk:
            if not ('0' <= c <= '9' or 'a' <= c <= 'f' or 'A' <= c <= 'F'):
                return False

        if int(chunk, 16) < 0: return False
        if len(chunk) > 4: return False
        return True


# 468. Validate IP Address
# https://leetcode.com/problems/validate-ip-address/description/


# Intuition:
# Main things to check will be:
# 1. How many parts after split
# 2. Does each part adhere to the range in the decimal form or in string form itself to avoid type casting
# 3. 


sol = Solution()
assert sol.validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334:") == 'Neither'




# Samples for defang
# assert sol.validIPAddress("127[.]0[.]0[.]1")
# assert sol.validIPAddress("127.0.0.1")
# assert sol.validIPAddress("127/./0[.]0[.]1")
# assert not sol.validIPAddress("127asdfasdf[.]0[.]0[.]256")
