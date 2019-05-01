class Solution:
    def validIPAddress(self, IP):

            def isIPv4(s):
                try: return str(int(s)) == s and 0 <= int(s) <= 255
                except: return False

            def isIPv6(s):
                if len(s) > 4: return False
                if s and s[0] == '-': return False
                try: dec = int(s, 16)
                except: dec = None
                return dec is not None and 0 <= dec <= 0xffff

            if IP.count(".") == 3 and all(isIPv4(i) for i in IP.split(".")):
                return "IPv4"
            if IP.count(":") == 7 and all(isIPv6(i) for i in IP.split(":")):
                return "IPv6"
            return "Neither"