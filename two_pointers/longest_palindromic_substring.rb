# @param {String} s
# @return {String}
def longest_palindrome(s)
    n = s.size()
    dp = Array.new(n) { Array.new(n, false) }
    
    0.upto(n - 1) do |i|
        dp[i][i] = true
    end

    start, max_len = 0, 1

    0.upto(n - 2) do |i|
        next if s[i] != s[i + 1]
        dp[i][i + 1] = true
        start, max_len = i, 2
    end
    
    3.upto(n) do |k|
        0.upto(n - k) do |i|
            # Considering strings of length 3 to n
            j = i + k - 1

            if dp[i + 1][j - 1] && s[i] == s[j]
                dp[i][j] = true
                start, max_len = i, k if k > max_len
            end
        end
    end
    
    s[start...start + max_len]
end


# @param {String} s
# @return {String}
def longest_palindrome2(s)
    longest, n = '', s.size()

    0.upto(n - 1) do |i|
        longest = [
            get_longest_palindrome(s, i, i),     # Case of Odd length palindromes
            get_longest_palindrome(s, i, i + 1), # Case of Even length palindromes
            longest
        ].max_by(&:size)
    end

    longest
end

def get_longest_palindrome(s, l, r)
    while 0 <= l && r < s.size() && s[l] == s[r]
        l -= 1; r += 1
    end

    s[l + 1...r]
end

# 5. Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/description/

# Approach 1: DP
# dp(i, j) represents whether s(i...j) can form a palindromic substring
# dp(i, j) is true when s(i) equals to s(j) and s(i+1 ... j-1) is a palindromic substring.
# When we find a palindrome, check if it's the longest one.

# Time: O(n^2)
# Space: O(n^2)

# Approach 2: Expand from center technique
# Explore all 2n - 1 centers (i, i)s and (i, i + 1)s
# Time: O(n^2)
# Space: O(1)

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(longest_palindrome("a"), "a")
assert_equal(longest_palindrome("ccc"), "ccc")
assert_equal(longest_palindrome("babad"), "bab") # Notice this is bab for DP
assert_equal(longest_palindrome("civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"), "ranynar")


assert_equal(longest_palindrome2("a"), "a")
assert_equal(longest_palindrome2("ccc"), "ccc")
assert_equal(longest_palindrome2("babad"), "aba") # Notice this aba for expand from center
assert_equal(longest_palindrome2("civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"), "ranynar")
