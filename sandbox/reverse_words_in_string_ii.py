class Solution:
    def reverseWords(self, str):
        self.reverse(str, 0, len(str) - 1)
        self.reverse_word(str)

    def reverse_word(self, a):
        l, r = 0, 0
        while r < len(a):
            while r < len(a) and a[r] != ' ':
                r += 1
            self.reverse(a, l, r - 1)
            r += 1
            l = r

    def reverse(self, a, l, r):
        while l < r:
            a[l], a[r] = a[r], a[l]
            l += 1; r -= 1


class Solution:
    def reverseWords(self, s):
        p = 0
        for i in range(len(s)):
            if s[i] == ' ':
                s[p:i] = s[p:i][::-1]
                p = i + 1

        s[p:] = s[p:][::-1]

        s.reverse()


# r o c k   s t a r]
# l       l
#             r