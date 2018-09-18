# @param {String} s
# @return {String}
def longest_palindrome(s)
    n = s.length
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

# -------------------------------------------------------------------------------
# dp(i, j) represents whether s(i ... j) can form a palindromic substring
# dp(i, j) is true when s(i) equals to s(j) and s(i+1 ... j-1) is a palindromic substring.
# When we find a palindrome, check if it's the longest one. Time complexity O(n^2).
# -------------------------------------------------------------------------------

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(longest_palindrome("a"), "a")
assert_equal(longest_palindrome("ccc"), "ccc")
assert_equal(longest_palindrome("babad"), "bab")
assert_equal(longest_palindrome("civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"), "ranynar")
