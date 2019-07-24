class Solution(object):
    def reverseWords(self, s):
        arr = list(s)
        self.reverse(arr, 0, len(arr) - 1)
        self.reverse_words(arr)
        arr = self.trim_sides(arr)
        return ''.join(arr)

    def reverse(self, arr, l, r):
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1; r -= 1

    def reverse_words(self, arr):
        l, r = 0, 0
        n = len(arr)
        while r < n:
            while r < n and not arr[r].isspace(): r += 1
            self.reverse(arr, l, r - 1)
            if r < n:
                r += 1; l = r

    # efg abc
    #     l
    #         r

    # def trim_sides(self, arr):
    #     '''str.strip() basically'''
    #     if ''.join(arr).isspace(): return []
    #     l, r = 0, len(arr) - 1
    #     while l < r and arr[l].isspace(): l += 1
    #     while l < r and arr[r].isspace(): r -= 1
    #     return arr[l:r+1]

    # def trim_space(self, word):
    #     '''remove duplicating space in a word'''
    #     if not word: return []
    #     res = [word[0]]
    #     for i in range(1, len(word)):
    #         if res[-1].isspace() and word[i].isspace(): continue
    #         res.append(word[i])
    #     return res

# 151. Reverse Words in a String
# https://leetcode.com/problems/reverse-words-in-a-string-ii/

sol = Solution()
assert sol.reverseWords("the sky is blue") == "blue is sky the"
assert sol.reverseWords("hello world!") == "world! hello"
assert sol.reverseWords("a good example") == "example good a"

# Time: O(n)
# Space: O(1)
