class Codec:
    def encode(self, strs):
        res = ""
        for s in strs:
            res += str(len(s)) + "_" + s
        return res

    def decode(self, s):
        res, count, i = [], "", 0

        while i < len(s):
            while s[i] != "_":
                count += s[i]
                i += 1

            i += 1
            res.append(s[i : i + int(count)])
            i += int(count)
            count = ""

        return res

# Hello World

# 5_Hello5_World


# i = 0

# 271. Encode and Decode Strings
# https://leetcode.com/problems/encode-and-decode-strings/description/
