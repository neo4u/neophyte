def addBinary(self, a, b):
    a, b = list(a), list(b)
    res, carry = [], 0
    while a or b:
        n1 = n2 = 0
        if a: n1 = int(a.pop())
        if b: n2 = int(b.pop())
        
        tmp = n1 + n2 + carry
        carry = 0
        if tmp == 1 or tmp == 0:
            res.append(tmp)
        elif tmp == 2:
            res.append(0)
            carry += 1
        else:
            res.append(1)
            carry += 1
    if carry:
        res.append(carry)
    return ''.join(str(d) for d in res)[::-1]

# add two binary from back to front, I think it is very self explained, when 1+1 we need a carry.
class Solution:
    def addBinary(self, a, b):
        if '' in (a, b): return a or b
        if a[-1] == '1' and b[-1] == '1':
            return self.addBinary('1', self.addBinary(a[:-1], b[:-1])) + '0'
        if a[-1] == '0' and b[-1] == '0':
            return self.addBinary(a[:-1], b[:-1]) + '0'

        return self.addBinary(a[:-1], b[:-1]) + '1'

# One liner using in-built constructs
class Solution:
    def addBinary(self, a, b):
        return bin(eval('0b' + a) + eval('0b' + b))[2:]

# 67. Add Binary
# https://leetcode.com/problems/add-binary/
