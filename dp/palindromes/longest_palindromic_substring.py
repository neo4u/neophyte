class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest, n = "", len(s)

        for i in range(n):
            longest = max(
                self.get_longest_from_center(s, i, i),
                self.get_longest_from_center(s, i, i + 1),
                longest,
                key=len
            )

        return longest

    def get_longest_from_center(self, s, l, r):
        while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
            l -= 1; r += 1

        return s[l + 1:r] # index l + 1 upto r - 1


# 5. Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/description/

# Approach 1: DP
# dp[i, j] represents whether s(i...j) can form a palindromic substring
# dp[i, j] is true when s[i] equals to s[j] and s[i+1 ... j-1] is a palindromic substring.
# When we find a palindrome, check if it's the longest one.

# Time: O(n^2)
# Space: O(n^2)s


# Approach 2: Expand from center using 2-pointer technique
# Explore all 2n - 1 centers (i, i)s and (i, i + 1)s

# Time: O(n^2)
# Space: O(1)


sol = Solution()
assert sol.longestPalindrome("a") == "a"
assert sol.longestPalindrome("ccc") == "ccc"
assert sol.longestPalindrome("babad") == "bab" # Notice this is bab for DP
assert sol.longestPalindrome("civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth") == "ranynar"
