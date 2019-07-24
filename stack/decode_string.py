class Solution(object):
    def decodeString(self, s):
        stack = []
        stack.append(["", 1])
        num = ""

        for ch in s:
            if ch.isdigit():
                num += ch
            elif ch == '[':
                stack.append(["", int(num)])
                num = ""
            elif ch == ']':
                st, k = stack.pop()
                stack[-1][0] += st * k
            else:
                stack[-1][0] += ch

        return stack[0][0]

# 3[a2[c]]

# [['', 1]]

# num = 3
# [['', 1], ['', 3]], num = ''


def helper(s):
    res = ""
    while s:
        num = ""
        while s and s[-1].isdigit():
            num += s.pop()

        if num:
            num = int(num)
            s.pop()
            res += helper(s) * num
        else:
            c = s.pop()
            if c not in "[]":
                res += c
            if c == ']':
                break
    return res

class Solution(object):
    def decodeString(self, s):
        return helper(list(s)[::-1])

