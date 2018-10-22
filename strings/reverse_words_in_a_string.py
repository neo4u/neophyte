
class Solution(object):
    def reverseWords(self, s):
        s = s.split()

        ans = []
        for i in range(len(s)):
            if (s[len(s)-1-i]):  # Not needed but just in case
                ans.append(s[len(s)-1-i].strip())

        return " ".join(ans)


solution = Solution()
assert solution.reverseWords(" a b ") == "b a"
assert solution.reverseWords("what are you doing?") == "doing? you are what"
